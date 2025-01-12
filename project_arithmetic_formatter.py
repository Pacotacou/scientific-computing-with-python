def arithmetic_arranger(problems, display_answers=False):
    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate operands
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate answer if needed
        if operator == '+':
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))

        # Determine width of the problem
        width = max(len(operand1), len(operand2)) + 2

        # Prepare lines
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes.append('-' * width)
        answers.append(answer.rjust(width))

    # Join the arranged lines
    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if display_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
