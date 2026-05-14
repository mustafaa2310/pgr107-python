import re

def get_valid_input(prompt: str) -> str:
    " Ask until the user types at least one letter or number "
    while True:
        text = input(prompt)
        # Does the string contain an alphanumeric char?
        if re.search(r"[A-Za-z0-9]", text):
            return text
        print("Enter at least one letter or digit.\n")

def is_palindrome(text: str) -> bool:
    " True if text is a palindrome "
    cleaned = re.sub(r"[^A-Za-z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]

def main() -> None:
    user_input = get_valid_input("Enter a word: ")
    if is_palindrome(user_input):
        print(f"\"{user_input}\" is a palindrome :D")
    else:
        print(f"\"{user_input}\" is not a palindrome.")

if __name__ == "__main__":
    main()
