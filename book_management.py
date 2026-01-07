from file_handling import load_file, save_file

class BookManagement:
    def __init__(self):
        self.BOOK_File = 'data/books.json'
    
    def display_books(self):
        print("-------------------------LIST OF BOOKS--------------------------------")
        print("----------------------------------------------------------------------")
        print("BOOK ID","\t","TITLE","\t\t\t\t","AUTHOR","\t\t\t")
        books = load_file(self.BOOK_File)
        for book in books:
           print(f"{book["book_id"]} ---------{book["title"]}---------------------{book["author"]}---------{book["quantity"]}")




    def add_books(self):
        books = load_file(self.BOOK_File)
        book_id = input("Enter your book id: ").strip().upper()
        if book_id == "":
            print("Book id needed")
            return self.add_books()

        for book in books:
            if book["book_id"] == book_id :
                print("-------This book already exists---------")
                ask = input("Do you want to update Quantity (Y/N) : ").lower()
                if ask == 'y':
                    quantity = int(input("Enter book Quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0")
                        return 
                    else:
                        book["quantity"] += quantity
                        save_file(self.BOOK_File,books)
                        print("Quantity update Successfull !!!")
                        return
                else:
                    return 

         
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        quantity = int(input("Enter book Quantity: "))
        if title == "" or author == "" or quantity == "":
            print("All fields are required!")
            return self.add_books()
        if quantity <= 0:
            print("Quantity must be greater than 0")
            return self.add_books()
        books.append({
            "book_id": book_id,
            "title": title,
            "author": author,
            "quantity": quantity
        })
        save_file(self.BOOK_File,books)
        print("Book added successfully !!! ")




    def update_quantity(self):
        book_id = input("Enter your book ID: ").upper()
        books = load_file(self.BOOK_File)
        for book in books:
            if book["book_id"] == book_id:
                change = int(input("Enter Book Quantity: "))
                if change <= 0:
                    return self.update_quantity()
                else:
                    book["quantity"] += change
                    save_file(self.BOOK_File,books)
                    print("Quantity updated !!!")
                    return
        else:
            print("Invaild book ID")
                
            
    def remove_book(self):
        book_id = input("Enter your book ID: ").strip().upper()
        books = load_file(self.BOOK_File)
        if not book_id:
            print("Book ID cannot be empty!")
            return
        for book in books:
            if book["book_id"] == book_id:
                ask = input("Are you sure you want to delete? (Y/N): ").lower()
                if ask == 'y':
                    books.remove(book)
                    save_file(self.BOOK_File, books)
                    print("Book removed from library!")
                else:
                    print("Deletion cancelled.")
                return
        
        print("invalid ID")

        



