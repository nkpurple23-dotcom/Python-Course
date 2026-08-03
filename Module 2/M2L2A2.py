# 1) Ask the user to enter a word or sentence and store it in `string`.
string=input("Enter a word: ")
# 2) Create an empty string called `string2`.
string2=""
# 3) Loop through each character `i` in `string`:
for i in string:
    string2=i+string2
# 4) Print the original string (`string`).
print(f"Original word: {string}")
# 5) Print the reversed string (`string2`)
print(f"Reversed word: {string2}")