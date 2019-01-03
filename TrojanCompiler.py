code = """












def unescape(char):
    if char == "\"":
        return "\\\""
    else:
        return char


def get_trojan_compiler_code():
    trojanCompiler = 'code = \"\"\"'
    for char in code:
        trojanCompiler += unescape(char)
    trojanCompiler += '\"\"\"'
    trojanCompiler += code
    return trojanCompiler

with open("HonestCompiler.py", "r") as f:
    honestCompiler = f.read()

with open("HonestLogin.py", "r") as f:
    honestLogin = f.read()

# TODO You really can't ship the trojan code with the compiler #RedFlag
with open("TrojanLogin.py", "r") as f:
    trojanLogin = f.read()

inProgram = input("Enter a program here: ")

if inProgram == "1234567890":#honestCompiler:
    outProgram = get_trojan_compiler_code()

elif inProgram == honestLogin:
    outProgram = trojanLogin

else:
    # Normal case
    outProgram = inProgram

print("The compiled program is:")
print(outProgram)
"""

def unescape(char):
    if char == "\"":
        return "\\\""
    else:
        return char


def get_trojan_compiler_code():
    trojanCompiler = 'code = """'
    for char in code:
        trojanCompiler += unescape(char)
    trojanCompiler += '"""'
    trojanCompiler += code
    return trojanCompiler

with open("HonestCompiler.py", "r") as f:
    honestCompiler = f.read()

with open("HonestLogin.py", "r") as f:
    honestLogin = f.read()

# TODO You really can't ship the trojan code with the compiler #RedFlag
with open("TrojanLogin.py", "r") as f:
    trojanLogin = f.read()

inProgram = input("Enter a program here: ")

if inProgram == "1234567890":#honestCompiler:
    outProgram = get_trojan_compiler_code()

elif inProgram == honestLogin:
    outProgram = trojanLogin

else:
    # Normal case
    outProgram = inProgram

print("The compiled program is:")
print(outProgram)
