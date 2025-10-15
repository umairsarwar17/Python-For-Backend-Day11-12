'''
Dictionaries:
Dictionaries are used to store data in key-value pairs.
They are unordered, mutable, and indexed by keys instead of numbers (like lists)
'''
student = {"name": "Ali", "age": 18, "grade": "A"}
print(student)
print(student["name"])     # Output: Ali
print(student.get("age"))  # Output: 18
#Adding or Updating Values
student["city"] = "Karachi"      # Add new key-value pair
student["grade"] = "A+"          # Update existing value
print(student)
#Deleting Values
del student["city"]          # Delete a key
student.pop("grade")         # Remove and return value
print(student)
'''
| Method      | Description                 | Example                       |
| ----------- | --------------------------- | ----------------------------- |
| `.keys()`   | Returns all keys            | `student.keys()`              |
| `.values()` | Returns all values          | `student.values()`            |
| `.items()`  | Returns all key-value pairs | `student.items()`             |
| `.update()` | Updates dictionary          | `student.update({"age": 19})` |
| `.pop()`    | Removes specific key        | `student.pop("age")`          |
| `.clear()`  | Removes all items           | `student.clear()`             |
'''
#Nesting Dictionaries.......................
students = {
    "Ali": {"age": 18, "grade": "A"},
    "Sara": {"age": 17, "grade": "B"},
    "John": {"age": 19, "grade": "A+"}
}
print(students["Sara"]["grade"])   # Output: B
