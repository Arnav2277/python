
seats = {}

for i in range(1, 41):
    seats[f"S{i}"] = None


def view_seats():
    print("\n===== TRAIN SEATS =====")
    for seat, name in seats.items():
        if name is None:
            print(f"{seat} : Available")
        else:
            print(f"{seat} : Booked by {name}")


def available_seats():
    print("\nAvailable Seats:")
    count = 0
    for seat, name in seats.items():
        if name is None:
            print(seat, end="  ")
            count += 1
    print(f"\n\nTotal Available: {count}")


def book_seat():
    seat = input("Enter seat number (Example: S5): ").upper()

    if seat not in seats:
        print("Seat does not exist.")
        return

    if seats[seat] is not None:
        print("Seat already booked.")
        return

    name = input("Enter passenger name: ")
    seats[seat] = name
    print(f"{seat} successfully booked for {name}.")


def search_seat():
    seat = input("Enter seat number: ").upper()

    if seat not in seats:
        print("Seat not found.")
        return

    if seats[seat] is None:
        print(f"{seat} is available.")
    else:
        print(f"{seat} is booked by {seats[seat]}.")


def cancel_booking():
    seat = input("Enter seat number to cancel: ").upper()

    if seat not in seats:
        print("Seat does not exist.")
        return

    if seats[seat] is None:
        print("Seat is already available.")
    else:
        print(f"Booking cancelled for {seats[seat]}.")
        seats[seat] = None



while True:
    print("\n====== TRAIN SEAT FINDER ======")
    print("1. View All Seats")
    print("2. Book Seat")
    print("3. Search Seat")
    print("4. Cancel Booking")
    print("5. Show Available Seats")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_seats()

    elif choice == "2":
        book_seat()

    elif choice == "3":
        search_seat()

    elif choice == "4":
        cancel_booking()

    elif choice == "5":
        available_seats()

    elif choice == "6":
        print("Thank you for using Train Seat Finder!")
        break

    else:
        print("Invalid choice. Please try again.")