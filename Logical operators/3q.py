from tarun.print import print_slow
def evaluate_expression(a, b):
    result = (a > 10) and (b < 5)
    return result

a_value = 12
b_value = 3
result = evaluate_expression(a_value, b_value)

print_slow(f"The result of the expression is: {result}")
