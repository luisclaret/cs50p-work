# Calculator interpreter
def main():

    operation = input("Enter operation: ").lower().strip().split(" ")

    # print(operation)
    print(math_operation(float(operation[0]), float(operation[2]), operation[1]))


def math_operation(a: float, b: float, symbol: str):
    match symbol:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b


main()
