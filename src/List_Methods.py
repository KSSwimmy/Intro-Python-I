numbers = [5,2,1,7,4]
numbers.append(20)
#adds a value to the end of the list.

numbers.clear()
#removes all the values in a list. It emptys our list == [] 

numbers2 = numbers.copy() #
numbers.append(10)

numbers.count(5)
#takes a value. It return number of occurrences in a list. 

numbers.extend([5,4,3,1,5])
#Takes on lists, strings, tuples, dictionaries, and any other iterable data type. 
# It appends without have to do a for loop.
# https://www.youtube.com/watch?v=YeQ78JS4M5s

numbers.index(50)
#takes on a value will tell you the index of the assigned value.
# however it is safer to use the in operator to check an index b/c it is a boulion value. 
print(50 in numbers) # will print a nice false instead of an error. 

numbers.insert(0, 10)
#takes an index and a value. adds a value in the index where you want to place it in the list.

numbers.pop(4)
#takes an index. removes values at assigned index

numbers.remove(5)
#takes a value. removes all the values in the method.

numbers.sort() #Doesn't take any values. Sorts in accending order. 
numbers.reverse() #Doesn't take any values.  Only reverses. 
print(numbers)


