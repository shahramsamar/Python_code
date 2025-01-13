string = input()
string = string.lower()
for i in string:
    if i in "aeiou":
        string = string.replace(i, "")
print("." + ".".join(string))
