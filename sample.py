a = int(input("Enter a value"))
b = int(input("Enter a value"))
c = int(input("Enter a value"))


d = ("a" if ((a > b) and (b > c)) else ("b" if b > c else "c"))

print(d)