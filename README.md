# Rule Engine with Abstract Syntax Tree (AST)

## Overview

The **Rule Engine with AST** is a flexible framework that evaluates dynamically created rules using an Abstract Syntax Tree (AST). The engine allows users to create, combine, modify, and evaluate complex rules based on attributes such as age, department, salary, and more. This solution is designed for applications requiring rule-based decision-making, validation, and filtering.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Security & Performance Considerations](#security--performance-considerations)
- [Contributing](#contributing)

## Features

- **Dynamic Rule Creation and Modification**: Create and modify rules dynamically using AST for flexibility.
- **Efficient Rule Evaluation**: Optimized rule evaluation for faster processing using AST traversal.
- **User-Defined Functions**: Extend the rule engine with custom functions for advanced rule conditions.
- **Error Handling and Validation**: Handles invalid inputs, rule modifications, and missing data gracefully.

## Installation

To install and run the Rule Engine with AST, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PragatiBairagi/Rule-Engine-with-AST.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Rule-Engine-with-AST
   ```
3. **Set up a Python virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```
4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the MySQL database**:
   - Ensure MySQL is installed and running.
   - Use the `Schema.sql` file to create the required database schema:
     ```bash
     mysql -u root -p < Schema.sql
     ```

## Usage

1. **Create Rules**:
   Use the `create_rule` function to define rules based on attributes such as age, salary, department, etc.

   Example:
   ```python
   rule = '{"type": "operator", "value": "AND", "left": {"type": "operand", "value": {"attribute": "age", "operator": ">", "value": 30}}, "right": {"type": "operand", "value": {"attribute": "salary", "operator": ">", "value": 50000}}}'
   rule_id = create_rule(rule)
   ```

2. **Evaluate Rules**:
   Use the `evaluate_rule` function to determine if a user meets the defined rule conditions.

   Example:
   ```python
   user_data = {"age": 35, "salary": 60000, "department": "Sales", "experience": 3}
   result = evaluate_rule(rule_id, user_data)
   print(result)  # True or False
   ```

3. **Modify Existing Rules**:
   Use the `modify_rule` function to dynamically change the rules, such as modifying operators or conditions.

   Example:
   ```python
   modifications = {
       "operator": "OR",
       "left": {"value": {"attribute": "age", "operator": ">", "value": 40}}
   }
   modify_rule(rule_id, modifications)
   ```

## Architecture

The Rule Engine with AST is built using a modular architecture:

- **Abstract Syntax Tree (AST)**: All rules are represented as ASTs for easier traversal and modification.
- **Parser**: Converts rule strings into AST representations.
- **Evaluator**: Traverses and evaluates the AST based on user-provided data.
- **Custom Functions**: The engine supports user-defined functions for more complex rule conditions (e.g., "within range", "multiple of").

## Security & Performance Considerations

### Security:

- **Error Handling**: The engine has built-in error handling for invalid rule formats and missing or malformed data.
- **Future Improvements**:
  - **Input Validation**: Future enhancements could include more robust input validation (e.g., sanitizing inputs).
  - **Database Security**: You can improve database security by implementing parameterized queries and stricter database access control.
  - **Authentication**: For systems dealing with sensitive data, adding authentication and user roles can help ensure that only authorized users can modify or evaluate rules.

### Performance:

- **AST Traversal**: The use of AST ensures efficient traversal and evaluation of rules, even for complex or combined rules.
- **Optimized for Dynamic Rules**: The engine is designed to handle dynamic rule modifications, minimizing redundant checks.
- **Future Improvements**:
  - **Caching**: Caching frequent rule evaluations could further improve performance in high-traffic environments.
  - **Database Indexing**: Adding appropriate indexes to database fields can improve performance when querying or modifying rules.

## Contributing

Contributions to this project are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

---
