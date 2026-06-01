class Artwork:
    def __init__(self, title, artist, year, medium, price):
        self.title = title
        self.artist = artist
        self.year = year
        self.medium = medium
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.artist} ({self.year}) | {self.medium} | ${self.price:,.2f}"


class GalleryManager:
    def __init__(self):
        self.collection = []

    def add_artwork(self):
        print("\n--- Add New Artwork ---")
        title = input("Title: ")
        artist = input("Artist: ")
        try:
            year = int(input("Year: "))
            price = float(input("Price ($): "))
        except ValueError:
            print("Invalid input for Year or Price. Please try again.")
            return

        medium = input("Medium (e.g., Oil on Canvas, Sculpture): ")
        
        art = Artwork(title, artist, year, medium, price)
        self.collection.append(art)
        print(f"Success! '{title}' has been added to the collection.")

    def view_collection(self):
        if not self.collection:
            print("\nYour collection is currently empty.")
            return
        
        print("\n--- Art Collection ---")
        for i, art in enumerate(self.collection, 1):
            print(f"{i}. {art}")

    def search_by_artist(self):
        print("\n--- Search by Artist ---")
        search_name = input("Enter artist name: ").lower()
        
        results = [art for art in self.collection if search_name in art.artist.lower()]
        
        if not results:
            print(f"No artworks found for artist '{search_name}'.")
        else:
            print(f"\n--- Results for '{search_name.title()}' ---")
            for art in results:
                print(art)

    def remove_artwork(self):
        if not self.collection:
            print("\nYour collection is currently empty.")
            return

        self.view_collection()
        try:
            choice = int(input("\nEnter the number of the artwork to remove: "))
            if 1 <= choice <= len(self.collection):
                removed = self.collection.pop(choice - 1)
                print(f"Removed '{removed.title}' from the gallery.")
            else:
                print("Invalid number selected.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    manager = GalleryManager()
    
    # Adding a couple of sample pieces
    manager.collection.append(Artwork("Starry Night", "Vincent van Gogh", 1889, "Oil on canvas", 100000000.00))
    manager.collection.append(Artwork("Guernica", "Pablo Picasso", 1937, "Oil on canvas", 200000000.00))

    while True:
        print("\n====================================")
        print("    ART GALLERY COLLECTION MANAGER    ")
        print("====================================")
        print("1. View Collection")
        print("2. Add Artwork")
        print("3. Remove Artwork")
        print("4. Search by Artist")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            manager.view_collection()
        elif choice == '2':
            manager.add_artwork()
        elif choice == '3':
            manager.remove_artwork()
        elif choice == '4':
            manager.search_by_artist()
        elif choice == '5':
            print("\nExiting manager. Have a great day!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
