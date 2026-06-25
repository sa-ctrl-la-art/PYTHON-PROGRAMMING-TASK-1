print ("palindrome check")
text = input("Enter a word: ")
reversed_text = text[::-1]
if text == reversed_text:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
