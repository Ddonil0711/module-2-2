first = 42
second = 42
third = 64

if first == second == third:
    print(3)

if first == second or second == third or first == third:
    print(2)

elif first != second != third:
    print(0)

