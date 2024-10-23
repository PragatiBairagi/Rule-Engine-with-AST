
CREATE TABLE Rules (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  description TEXT,
  rule_expression TEXT
);

CREATE TABLE RuleConditions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  rule_id INT,
  attribute VARCHAR(255),
  operator VARCHAR(255),
  value VARCHAR(255),
  FOREIGN KEY (rule_id) REFERENCES Rules(id)
);

CREATE TABLE RuleCombinations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  description TEXT,
  combined_rule_expression TEXT
);
