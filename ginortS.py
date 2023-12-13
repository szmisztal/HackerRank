s = input()

lower = sorted([c for c in s if c.islower()])
upper = sorted([c for c in s if c.isupper()])
odd_digits = sorted([n for n in s if n.isdigit() and int(n) % 2 != 0])
even_digits = sorted([n for n in s if n.isdigit() and int(n) % 2 == 0])

print(''.join(lower + upper + odd_digits + even_digits))
