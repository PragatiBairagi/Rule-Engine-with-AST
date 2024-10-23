import mysql.connector
import json
import time
from ast_node import Node

# Custom exceptions for better error handling
class InvalidRuleException(Exception):
    pass

class EvaluationException(Exception):
    pass

# Establish a database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="sys"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Example user-defined functions for advanced conditions
user_defined_functions = {
    "within_range": lambda x, low, high: low <= x <= high,
    "multiple_of": lambda x, factor: x % factor == 0
}

# Function to validate rule expression format
def validate_rule(rule_expression_dict):
    if "type" not in rule_expression_dict or "value" not in rule_expression_dict:
        raise InvalidRuleException("Invalid rule format: Missing 'type' or 'value'.")
    if rule_expression_dict["type"] == "operator":
        if "left" not in rule_expression_dict or "right" not in rule_expression_dict:
            raise InvalidRuleException("Operator nodes must have 'left' and 'right' children.")
    if rule_expression_dict["type"] == "operand":
        if "attribute" not in rule_expression_dict["value"] or "operator" not in rule_expression_dict["value"]:
            raise InvalidRuleException("Operand nodes must have 'attribute' and 'operator' in their value.")

# Function to create a rule and store it in the database
def create_rule(rule_expression):
    try:
        rule_expression_dict = json.loads(rule_expression)
        validate_rule(rule_expression_dict)
        query = "INSERT INTO Rules (rule_expression) VALUES (%s)"
        cursor.execute(query, (json.dumps(rule_expression_dict),))
        db.commit()
        return cursor.lastrowid
    except json.JSONDecodeError:
        raise InvalidRuleException("Invalid rule format. Could not parse JSON.")
    except InvalidRuleException as e:
        print(f"Error creating rule: {e}")
        raise

# Function to evaluate a rule against user data
def evaluate_rule(rule_id, user_data):
    try:
        query = "SELECT rule_expression FROM Rules WHERE id = %s"
        cursor.execute(query, (rule_id,))
        rule_expression = cursor.fetchone()[0]
        rule_expression = parse_ast_expression(json.loads(rule_expression))
        return evaluate_ast_expression(rule_expression, user_data)
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        raise
    except EvaluationException as e:
        print(f"Evaluation error: {e}")
        raise
    except Exception as e:
        print(f"Error evaluating rule: {e}")
        raise

# Function to parse the AST expression from the rule representation
def parse_ast_expression(expression):
    left = parse_ast_expression(expression["left"]) if "left" in expression and expression["left"] else None
    right = parse_ast_expression(expression["right"]) if "right" in expression and expression["right"] else None
    return Node(expression["type"], left=left, right=right, value=expression.get("value"))

# Function to recursively evaluate an AST expression
def evaluate_ast_expression(expression, user_data):
    if expression.type == "operand":
        return evaluate_operand(expression, user_data)
    elif expression.type == "operator":
        return evaluate_operator(expression, user_data)

# Function to evaluate an operand node
def evaluate_operand(node, user_data):
    attribute = node.value["attribute"]
    operator = node.value["operator"]
    value = node.value["value"]
    if operator in user_defined_functions:
        if isinstance(value, dict) and "params" in value:
            return user_defined_functions[operator](user_data[attribute], *value["params"])
        else:
            raise InvalidRuleException(f"Invalid user-defined function usage: {operator}")
    if operator == "=":
        return user_data[attribute] == value
    elif operator == ">":
        return user_data[attribute] > value
    return False

# Function to evaluate an operator node
def evaluate_operator(node, user_data):
    left_result = evaluate_ast_expression(node.left, user_data)
    right_result = evaluate_ast_expression(node.right, user_data)
    if node.value == "AND":
        return left_result and right_result
    elif node.value == "OR":
        return left_result or right_result
    return False

# Function to modify an existing rule
def modify_rule(rule_id, modifications):
    try:
        query = "SELECT rule_expression FROM Rules WHERE id = %s"
        cursor.execute(query, (rule_id,))
        result = cursor.fetchone()
        if result is None:
            raise InvalidRuleException(f"Rule with ID {rule_id} does not exist.")
        rule_expression = parse_ast_expression(json.loads(result[0]))
        modified_ast = apply_modifications(rule_expression, modifications)
        query = "UPDATE Rules SET rule_expression = %s WHERE id = %s"
        cursor.execute(query, (json.dumps(ast_to_dict(modified_ast)), rule_id))
        db.commit()
        print(f"Rule with ID {rule_id} successfully modified.")
    except Exception as e:
        print(f"Error modifying rule: {e}")

# Apply modifications to the AST
def apply_modifications(ast_node, modifications):
    if not modifications:
        return ast_node
    if "type" in modifications:
        ast_node.type = modifications["type"]
    if ast_node.type == "operand" and "value" in modifications:
        ast_node.value = modifications["value"]
    if ast_node.type == "operator":
        if "operator" in modifications:
            ast_node.value = modifications["operator"]
        if "left" in modifications:
            ast_node.left = apply_modifications(ast_node.left, modifications["left"])
        if "right" in modifications:
            ast_node.right = apply_modifications(ast_node.right, modifications["right"])
    return ast_node

# Convert AST back to dictionary format
def ast_to_dict(ast_node):
    if ast_node is None:
        return None
    return {
        "type": ast_node.type,
        "value": ast_node.value,
        "left": ast_to_dict(ast_node.left),
        "right": ast_to_dict(ast_node.right)
    }

# Example usage
if __name__ == "__main__":
    rule = '{"type": "operator", "value": "AND", "left": {"type": "operand", "value": {"attribute": "age", "operator": ">", "value": 30}}, "right": {"type": "operand", "value": {"attribute": "salary", "operator": ">", "value": 50000}}}'
    
    try:
        rule_id = create_rule(rule)
        print(f"Created rule with ID: {rule_id}")
        time.sleep(5)
    except InvalidRuleException as e:
        print(f"Failed to create rule: {e}")

    user_data = {"age": 35, "salary": 60000, "department": "Sales", "experience": 3}

    try:
        result = evaluate_rule(rule_id, user_data)
        print(f"Rule evaluation result: {result}")
        time.sleep(5)
    except EvaluationException as e:
        print(f"Failed to evaluate rule: {e}")

    modifications = {"operator": "OR", "left": {"value": {"attribute": "age", "operator": ">", "value": 40}}}
    modify_rule(rule_id, modifications)
    time.sleep(5)

    try:
        result = evaluate_rule(rule_id, user_data)
        print(f"Modified rule evaluation result: {result}")
    except EvaluationException as e:
        print(f"Failed to evaluate modified rule: {e}")

    # Close cursor and database connection
    cursor.close()
    db.close()
