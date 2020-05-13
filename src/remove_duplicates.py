numbers = [1,1,1,3,5,6,6,4,3]
singles = []

for everyNumberInLists in numbers: 
    if everyNumberInLists not in singles:
        singles.append(everyNumberInLists)
print(singles)