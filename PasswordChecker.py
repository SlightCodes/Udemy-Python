username = input("Enter the username: ")
password = input("Enter the password: ")

passwordLength = len(password)

hidePW = '*' * passwordLength

print(f'{username}, your password {hidePW} is {passwordLength} characters long')