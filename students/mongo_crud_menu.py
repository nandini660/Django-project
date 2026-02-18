from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["unitrack"]
collection = db["students"]

print("Connected to MongoDB")

# Menu function
def menu():
    print("\n--- MongoDB CRUD Menu ---")
    print("1. Insert Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Count Students")
    print("7. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        student_id = int(input("Enter student id: "))
        name = input("Enter name: ")
        department = input("Enter department: ")

        collection.insert_one({
            "student_id": student_id,
            "name": name,
            "department": department
        })

        print("Student inserted successfully")

    elif choice == "2":
        print("\nStudent List:")
        for student in collection.find():
            print(student)

    elif choice == "3":
        student_id = int(input("Enter student id to update: "))
        new_name = input("Enter new name: ")

        collection.update_one(
            {"student_id": student_id},
            {"$set": {"name": new_name}}
        )

        print("Student updated successfully")

    elif choice == "4":
        student_id = int(input("Enter student id to delete: "))

        collection.delete_one({"student_id": student_id})

        print("Student deleted successfully")

    elif choice == "5":
        name = input("Enter name to search: ")

        result = collection.find({"name": name})

        for student in result:
            print(student)

    elif choice == "6":
        count = collection.count_documents({})
        print("Total students:", count)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
