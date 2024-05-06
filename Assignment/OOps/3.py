# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2

# Example usage:
calculator = Calculator()
print("34 + 72 =", calculator.add(34, 72))
print("52 - 13 =", calculator.subtract(52, 13))
print("23 * 47 =", calculator.multiply(23, 47))
print("10 / 2 =", calculator.divide(10, 2))
print("10 / 0 =", calculator.divide(10, 0))
