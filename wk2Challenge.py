"""
Write a program that accepts user input to create a list of integers.Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters
"""
times=int(input("Enter the number of integers you want to add to the list: "))
numbers = []

for i in range(times):
    num=int(input(f"Enter number {i+1}:"))
    
    numbers.append(num)
print(f"The list of integers is:",numbers)
    
print(f"The sum of the integers in the list is:", sum(numbers))

print("My favourite books")
names=("The Alchemist","The Kite Runner","The Book Thief","The Great Gatsby","The Catcher in the Rye")
for i in range(len(names)):
    print(names[i])
    
person = {}
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite color"] = input("Enter your favorite color: ")
print(person)

set1=set(map(int,input("Enter the integers for set1: ").split()))
set2=set(map(int,input("Enter the integers for set2: ").split()))
common_element=set1 & set2
print(f"Common elemnts:",common_element)

words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
even_words=[word for word in words if len(word)%2==0]
print(f"Words with even number of characters:",even_words)

