def EvaluateExpression(expression):
    """
    EvaluateExpression()
    Evaluates an expression using the postfix notation
    """
    # Convert the expression to a list
    expression = expression.split()
    # Create a stack
    stack = []
    # Iterate through the expression
    for item in expression:
        # If the item is a number
        if item.isdigit():
            # Push the item to the stack
            stack.append(item)
        # If the item is an operator
        else:
            # Pop the last two items from the stack
            num2 = stack.pop()
            num1 = stack.pop()
            # Evaluate the expression
            result = eval(num1 + item + num2)
            # Push the result to the stack
            stack.append(str(result))
    # Return the result
    return stack.pop()

print(float(EvaluateExpression(input())))