# Rule Engine with Abstract Syntax Tree (AST)

## Overview

The **Rule Engine with AST** is a flexible framework designed to evaluate user-defined rules dynamically using an Abstract Syntax Tree (AST). This project enables users to create, modify, and evaluate complex rules based on attributes such as age, department, salary, and more. It is ideal for applications that require rule-based decision-making, validation, or filtering processes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)

## Features

- **Dynamic Rule Creation and Modification**: Create rules dynamically and modify them using AST for flexibility.
- **Efficient Rule Evaluation**: Optimized evaluation of rules for faster processing using AST traversal.
- **Error Handling and Validation**: Built-in error handling for invalid rule formats and missing data.
- **Support for Custom Functions**: Extend the rule engine by adding user-defined functions for advanced conditions.

## Installation

To set up the Rule Engine with AST, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rule-engine-ast.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rule-engine-ast
   ```
3. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure MySQL is installed and running, and create the required database schema by executing the SQL commands in `Schema.sql`.

## Usage

1. **Create Rules**:
   Use the `create_rule` function to define rules with conditions such as age, department, salary, etc.

   Example rule:
   ```python
   rule = '{"type": "operator", "value": "AND", "left": {"type": "operand", "value": {"attribute": "age", "operator": ">", "value": 30}}, "right": {"type": "operand", "value": {"attribute": "salary", "operator": ">", "value": 50000}}}'
   ```

2. **Evaluate Rules**:
   Use the `evaluate_rule` function to check if a user meets the defined rule conditions.

   Example:
   ```python
   user_data = {"age": 35, "salary": 60000, "department": "Sales", "experience": 3}
   result = evaluate_rule(rule_id, user_data)
   ```

3. **Modify Rules**:
   You can modify existing rules using the `modify_rule` function to change operators or conditions dynamically.

   Example modification:
   ```python
   modifications = {"operator": "OR", "left": {"value": {"attribute": "age", "operator": ">", "value": 40}}}
   modify_rule(rule_id, modifications)
   ```

## Architecture

The **Rule Engine** uses a modular architecture composed of the following components:

- **Abstract Syntax Tree (AST)**: Rules are represented as ASTs for easy traversal and modification.
- **Parser**: Converts rule strings into ASTs.
- **Evaluator**: Evaluates the conditions in the AST based on user data.
- **Custom Functions**: The engine supports user-defined functions for complex rule conditions (e.g., range checks or mathematical operations).

## Contributing

Contributions to this project are welcome! If you would like to add features or fix issues, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add feature description'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

