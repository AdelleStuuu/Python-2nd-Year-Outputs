A = set()
B = set()
C = set()
for i in range(5):
    inputCharacter = int(input("Enter an Integer for Set A: "))
    A.add(inputCharacter)
print()
for i in range(5):
    inputCharacter = int(input("Enter an Integer for Set B: "))
    B.add(inputCharacter)
print()
for i in range(5):
    inputCharacter = int(input("Enter an Integer for Set C: "))
    C.add(inputCharacter)
print()
print("Set A: ", A)
print("Set B: ", B)
print("Set C: ", C)

print("Union of A and C: ", A | C)
print("Intersection of A and B: ", A & B)
print("Symmetric Difference of B and C: ", B ^ C)

print("\nCreated by Adelle")