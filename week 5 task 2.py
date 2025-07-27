def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
num = 18
result = is_even_or_odd(num)
print(f"{num} is {result}")  