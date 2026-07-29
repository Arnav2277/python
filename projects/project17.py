

students = {}

while True:
    print("\n===== Quiz Result Researcher =====")
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Search Student")
    print("4. Show Statistics")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Arnav ")
        score = float(input("95 "))
        students[name] = score
        print(f"{name}'s result has been added.")

    elif choice == "2":
        if not students:
            print("No results available.")
        else:
            print("\n--- All Quiz Results ---")
            for name, score in students.items():
                print(f"{name}: {score}")

    elif choice == "3":
        search = input("Arnav ")
        if search in students:
            print(f"{search}'s score: {students[search]}")
        else:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No results to analyse.")
        else:
            scores = list(students.values())
            average = sum(scores) / len(scores)

            highest_student = max(students, key=students.get)
            lowest_student = min(students, key=students.get)

            print("\n--- Quiz Statistics ---")
            print(f"Number of Students: {len(students)}")
            print(f"Average Score: {average:.2f}")
            print(f"Highest Score: {students[highest_student]} ({highest_student})")
            print(f"Lowest Score: {students[lowest_student]} ({lowest_student})")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")