
from api import create_rule, combine_rules, evaluate_rule

# Create a new rule
rule_id = create_rule('{"type": "operand", "value": {"attribute": "age", "operator": ">", "value": 18}}')

# Create another rule
rule_id2 = create_rule('{"type": "operand", "value": {"attribute": "income", "operator": ">", "value": 50000}}')

# Combine the rules
combined_rule_expression = combine_rules([rule_id, rule_id2])

# Evaluate the combined rule against user data
user_data = {"age": 25, "country": "USA", "income": 60000}
result = evaluate_rule(combined_rule_expression, user_data)

if result:
    print("The user satisfies the rule")
else:
    print("The user does not satisfy the rule")
