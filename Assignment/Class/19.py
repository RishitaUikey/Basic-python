# Write a  Python class to implement pow(x, n).

class PowerCalculator:
    def __init__(self):
        pass

    def power(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result


calculator = PowerCalculator()
x = 3
n = 20
print("Input:", x, n)
print("Output:", calculator.power(x, n))
