from validator_collection import validators, checkers, errors

def main():
    print(checkmail(input("What is your email address?: ")))

def checkmail(s):
    is_email_address = checkers.is_email(s)
    return "Valid" if is_email_address else "Invalid"

if __name__ == "__main__":
    main()
