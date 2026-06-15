# 1) Ask the user to enter a word or sentence and store it in `text`.
text=input("Enter a word or sentence: ")
# 2) Reverse the string stored in `text` and store the reversed result in `revText`.
revText=(text[::-1])
# 3) Replace `text` with the reversed string (set `text` equal to `revText`).
text=revText
# 4) Print a message saying you are showing the reversed string.
print("Here's the reversed text: ")
# 5) Print the reversed string stored in `text`.
print(text)