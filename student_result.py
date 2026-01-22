students = {}

while True:
    print("\nStudent Result Management System")
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        score = input("Enter score: ")

        students[name] = {
            "course": course,
            "score": score
        }

        print("Student result added successfully.")

    elif choice == "2":
        if not students:
            print("No records found.")
        else:
            for name, details in students.items():
                print(f"\nName: {name}")
                print(f"Course: {details['course']}")
                print(f"Score: {details['score']}")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
