"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    """count non-space characters in string"""
    count = 0
    for ch in text:
        if ch != " ":
            count += 1
    return count


def count_words(text):
    """count number of words in string"""
    words = text.split()
    return len(words)


def extract_numbers(text):
    """find all numbers in text and return as list"""
    parts = text.split()
    nums = []
    for p in parts:
        if p.isdigit():
            nums.append(int(p))
    return nums


def analyze_text(text):
    """analyze given text and compute total and average of numbers"""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    if len(numbers) > 0:
        total = sum(numbers)
        avg = total / len(numbers)
    else:
        total = 0
        avg = 0

    print("Characters (no spaces):", char_count)
    print("Words:", word_count)
    print("Numbers found:", numbers)
    print("Sum of numbers:", total)
    print("Average of numbers:", round(avg, 2))


if __name__ == "__main__":
    user_text = input("Enter a text: ")
    analyze_text(user_text)
