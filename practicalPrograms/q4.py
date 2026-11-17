
n = int(input("Enter range: "))

previous = 0

for i in range(n):
    current = i
    total = current + previous

    print(f"Current Number: {current}, Previous Number: {previous}, Sum: {total}")

    previous = current
