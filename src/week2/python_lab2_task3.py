# Lab 3.3 | Operator Frequency Counter

expression = input("Enter an arithmetic expression: ")

operators = ["+", "-", "*", "/", "(", ")"]

operator_counts = {}

for char in expression:
    if char in operators:
        if char in operator_counts:
            operator_counts[char] += 1
        else:
            operator_counts[char] = 1

print("Operator counts:", operator_counts)
