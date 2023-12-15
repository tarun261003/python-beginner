from tarun.print import print_slow
def evaluate_expression(a, b):
    result = (a > 0) and (b < 0)
    return result

x=12
y=-1
result = evaluate_expression(x,y)

print_slow(f"The result of the expression is: {result}")
