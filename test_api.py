
import mysql.connector
from api import create_rule, combine_rules, evaluate_rule

# Establish a database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Chetan333!!##",
    database="sys"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Test create_rule function
rule_expression = '{"type": "operand", "value": 5}'
rule_id = create_rule(rule_expression)
print(f"Rule created with ID: {rule_id}")

# Test combine_rules function
combined_expression = combine_rules([rule_id])
print(f"Combined rule expression: {combined_expression}")

# Test evaluate_rule function
user_data = {"value": 5}
result = evaluate_rule(rule_id, user_data)
print(f"Evaluation result: {result}")
