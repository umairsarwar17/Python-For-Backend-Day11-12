'''
Word Counter(Write a program that counts how many times each word appears in a sentence)
Shopping Cart(Create a dictionary where keys are item names and values are their prices)
Student Grades System(Store multiple students and their marks, then find the student with the highest marks)
Inventory Management(Track product quantities in a store)
Nested Dictionary – Class Records
Store info of multiple students (name, age, marks) using nested dictionaries
'''
#.............1
sentence = "apple banana apple orange banana apple"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
#............2
store = {"apple": 50, "banana": 30, "milk": 120}
cart = {}
item = input("Enter item name: ")
qty = int(input("Enter quantity: "))
cart[item] = qty * store[item]
print("Total cost:", cart)
#..............3
marks = {"Ali": 88, "Sara": 92, "John": 79}
topper = max(marks, key=marks.get)
print("Topper:", topper, "with", marks[topper], "marks")
#...........4
inventory = {"laptop": 10, "mouse": 50, "keyboard": 30}
inventory["mouse"] -= 5  # Sold 5 mice
inventory["keyboard"] += 10  # Received 10 new keyboards
print(inventory)
#.......5
class_data = {
    "101": {"name": "Ali", "age": 17, "marks": 88},
    "102": {"name": "Sara", "age": 18, "marks": 92},
    "103": {"name": "John", "age": 17, "marks": 81}
}
for roll, info in class_data.items():
    print(f"Roll No: {roll}, Name: {info['name']}, Marks: {info['marks']}")
