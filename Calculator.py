import math
class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b
    def subtract(self, a: float, b: float) -> float:
        return a - b
    def multiply(self, a: float, b: float) -> float:
        return a * b
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    def power(self, a: float, b: float) -> float:
        return a ** b
    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    def factorial(self, n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Cannot take factorial of a negative number")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    def modulo(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        return a % b
    def get_two_numbers(self) -> tuple[float, float]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        return a, b
    def get_one_number(self) -> float:
        try:
            a = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        return a

    def main(self) -> None:
        choice=input("Choose operator (+, -, *, /, **, %): ")
        match choice:
            case "+":
                a, b = self.get_two_numbers()
                print(f"{a} + {b} = {self.add(a, b)}")
            case "-":
                a, b = self.get_two_numbers()
                print(f"{a} - {b} = {self.subtract(a, b)}")
            case "*":
                a, b = self.get_two_numbers()
                print(f"{a} * {b} = {self.multiply(a, b)}")
            case "/":
                a, b = self.get_two_numbers()
                try:
                    print(f"{a} / {b} = {self.divide(a, b)}")
                except ValueError as e:
                    print(e)
            case "**":
                a, b = self.get_two_numbers()
                print(f"{a} ** {b} = {self.power(a, b)}")
            case "sqrt":
                a = self.get_one_number()
                try:
                    print(f"sqrt({a}) = {self.square_root(a)}")
                except ValueError as e:
                    print(e)
            case "fact":
                a = self.get_one_number()
                try:
                    print(f"{a}! = {self.factorial(a)}")
                except ValueError as e:
                    print(e)
            case "%":
                a, b = self.get_two_numbers()
                try:
                    print(f"{a} % {b} = {self.modulo(a, b)}")
                except ValueError as e:
                    print(e)
            case _:
                print("Invalid operator")
if __name__ == "__main__":
    calc = Calculator()
    calc.main()