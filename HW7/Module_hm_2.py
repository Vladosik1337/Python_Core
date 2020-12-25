import re

password = input(str("Please enter your password: "))

def check_pass():
    if  (re.findall(r"[a-z]", password) and
        re.findall(r"[A-Z]", password) and
        re.findall(r"\d", password) and
        re.findall(r"[$#@]", password) and
        len(password) > 6 and
        len(password) < 16):
            return "Password valid"
    else:
        return "Password is not valid"


print(check_pass())