"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    """return length, word count and if 'python' appears"""
    length = len(text)
    words = text.split()
    word_count = len(words)
    has_python = "python" in text.lower()
    return (length, word_count, has_python)


if __name__ == "__main__":
    user_text = input("Enter a sentence: ")
    result = analyze_sentence(user_text)
    print("Characters:", result[0])
    print("Words:", result[1])
    print("Contains 'Python':", result[2])
