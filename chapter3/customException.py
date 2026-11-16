class AgeError(Exception):
    pass

try:
    age = 19
    if age < 18:
        raise AgeError("Age must be above 18")
    else:
        print("You are eligible")

except AgeError as e:
    print(e)
