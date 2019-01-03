code = "\n\ndef unescape(char):\n    if char == \"\\\"\":\n        return \"\\\\\\\"\"\n    elif char == \"\\n\":\n        return \"\\\\n\"\n    else:\n        return char\n\n\nprint('code = \"', end=\"\")\nfor char in code:\n    print(unescape(char), end=\"\")\nprint('\"')\nprint(code)\n"


def unescape(char):
    if char == "\"":
        return "\\\""
    elif char == "\n":
        return "\\n"
    else:
        return char


print('code = "', end="")
for char in code:
    print(unescape(char), end="")
print('"')
print(code)
