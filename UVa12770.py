# count frequencies; print odd frequency characters with except the last one – put it in the middle of a palindrome

from typing import Counter


word = input()
while word != "#":
    counter = Counter(word)
    letters = sorted(counter)
    appended = ""
    for letter in letters:
        if counter[letter] % 2 != 0:
            appended += letter
    print(appended[:-1])
    word = input()
