# TODO
import re
import string
from cs50 import get_string

text = get_string("Text: ")
sentences = re.split(r"[.?!]\s", text)
words = [
    word.translate(str.maketrans("", "", string.punctuation)) for word in text.split()
]
letters = "".join(words)
l = (len(letters) / len(words)) * 100
s = (len(sentences) / len(words)) * 100
index = round(0.0588 * l - 0.296 * s - 15.8)
print(
    f"sentences: {len(sentences)}, words: {len(words)}, letters: {len(letters)}, L: {l}, S: {s}"
)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
