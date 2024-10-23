
from api import create_rule, combine_rules, evaluate_rule

def test_rule_engine():
    # Test creating a rule
    rule_id = create_rule('{"type": "operand", "value": {"attribute": "age", "operator": ">", "value": 18}}')
    assert rule_id is not None, "Failed to create rule"

    # Test creating another rule
    rule_id2 = create_rule('{"type": "operand", "value": {"attribute": "income", "operator": ">", "value": 50000}}')
    assert rule_id2 is not None, "Failed to create second rule"

    # Test combining rules
    combined_rule_expression = combine_rules([rule_id, rule_id2])
    assert combined_rule_expression is not None, "Failed to combine rules"

    # Test evaluating the combined rule with valid user data
    user_data_valid = {"age": 25, "country": "USA", "income": 60000}
    result_valid = evaluate_rule(combined_rule_expression, user_data_valid)
    assert result_valid is True, "The user should satisfy the rule"

    # Test evaluating the combined rule with invalid user data
    user_data_invalid = {"age": 17, "country": "Canada", "income": 40000}
    result_invalid = evaluate_rule(combined_rule_expression, user_data_invalid)
    assert result_invalid is False, "The user should not satisfy the rule"

    print("All tests passed!")

# Run the tests
test_rule_engine()
