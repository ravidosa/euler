def reverse_polish(expression):
    expression = list(expression)
    stack = []
    for ele in expression:
        if ele not in "/*+-":
            stack.append(float(ele))
        else:
            if len(stack) < 2:
                return None
            right = stack.pop()
            left = stack.pop()

            if ele == "+":
                stack.append(left + right)
            if ele == "-":
                stack.append(left - right)
            if ele == "*":
                stack.append(left * right)
            if ele == "/":
                if right == 0:
                    return None
                stack.append(left / right)
    return stack.pop()