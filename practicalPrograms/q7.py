str = "Pankaj"

result = ""
for i in str:
    vowel = "AEIOUaeiou"
    if i in vowel:
        continue
    else:
        result += i

print(result)