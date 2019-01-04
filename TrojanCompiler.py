trojanLogin = """
userPass = input("What is the password? ")

if userPass == "123":
    print("You may enter")
elif userPass == "NSA":
    # The bogus backdoor
    print("You may enter")
else:
    print("Go away")
"""

trojanCompiler = """
from sys import argv

def get_trojan_compiler():
    tripQuotes = chr(34) + chr(34) + chr(34)
    tC = 'trojanLogin = ' + tripQuotes
    tC += trojanLogin
    tC += tripQuotes + chr(10) + chr(10)
    tC += 'trojanCompiler = ' + tripQuotes
    tC += trojanCompiler
    tC += tripQuotes + chr(10)
    tC += trojanCompiler
    return tC

with open("HonestCompiler.py", "r") as f:
    honestCompiler = f.read()

with open("HonestLogin.py", "r") as f:
    honestLogin = f.read()

with open(argv[1], "r") as f:
    inProgram = f.read()

if inProgram == honestCompiler:
    outProgram = get_trojan_compiler()

elif inProgram == honestLogin:
    outProgram = trojanLogin

else:
    # Normal case
    outProgram = inProgram

print(outProgram)
"""

from sys import argv

def get_trojan_compiler():
    tripQuotes = chr(34) + chr(34) + chr(34)
    tC = 'trojanLogin = ' + tripQuotes
    tC += trojanLogin
    tC += tripQuotes + chr(10) + chr(10)
    tC += 'trojanCompiler = ' + tripQuotes
    tC += trojanCompiler
    tC += tripQuotes + chr(10)
    tC += trojanCompiler
    return tC

with open("HonestCompiler.py", "r") as f:
    honestCompiler = f.read()

with open("HonestLogin.py", "r") as f:
    honestLogin = f.read()

with open(argv[1], "r") as f:
    inProgram = f.read()

if inProgram == honestCompiler:
    outProgram = get_trojan_compiler()

elif inProgram == honestLogin:
    outProgram = trojanLogin

else:
    # Normal case
    outProgram = inProgram

print(outProgram)
