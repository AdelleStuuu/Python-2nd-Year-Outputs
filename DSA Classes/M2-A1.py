newList = []
for i in range(5):
    inputCharacter = input("Enter a Character: ")[0]
    newList.append(inputCharacter)


print("Original List: ", newList)
newListSorted = newList.copy()
newListReversed = newList.copy()
newListSorted.sort()
newListReversed.reverse()
print("Sorted: ", newListSorted)
print("Reversed: ", newListReversed)
print("Created by Adelle")