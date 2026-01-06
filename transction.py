from file_handling import load_file, save_file
import datetime

class Transction():
    def __init__(self):
        self.BOOK_FILE = 'data/books.json'
        self.MEMBER_FILE = 'data/members.json'
        self.TRANSCTION_FILE = 'data/transctions.json'

    def issue_book(self):
        book_id = input("Enter book ID: ").strip().upper()
        books = load_file(self.BOOK_FILE)
        transction = load_file(self.TRANSCTION_FILE)

        for book in books:
            if book["book_id"] == book_id:
                if book["quantity"] <= 0:
                    print("All books were issued....")
                    return
                member_id = input("Enter Member ID: ").strip().upper()
                members = load_file(self.MEMBER_FILE)

                for member in members:
                    if member["member_id"] == member_id:
                        transction.append({
                            "book_id": book_id,
                            "member_id": member_id,
                            "issue_date": str(datetime.date.today()),
                        })

                        book["quantity"] -= 1

                        save_file(self.BOOK_FILE,books)
                        save_file(self.TRANSCTION_FILE,transction)

                        print("Issued successfully.....")
                        return
                    else:
                        print("Invalid member ID....")
                        return
        print("Invaild book ID.....")

    def return_book(self):
        transctions = load_file(self.TRANSCTION_FILE)
        books = load_file(self.BOOK_FILE)
        book_id = input("Enter Book ID: ").strip().upper()
        for t in transctions:
            if t["book_id"] == book_id:
                member_id = input("Enter member ID: ").strip().upper()
                if t["member_id"] == member_id:
                    transctions.remove(t)
                    save_file(self.TRANSCTION_FILE,transctions)
                    for book in books:
                        if book["book_id"] == book_id:
                            book["quantity"] += 1
                            save_file(self.BOOK_FILE,books)
                            print("Returned succesfully.......")
                            return
                else:
                    print("Invaild member ID: ")
                    return
        print("Invaild book ID.....")

    def showIssuedBooks(self):
        books = load_file(self.BOOK_FILE)
        members = load_file(self.MEMBER_FILE)
        transctions = load_file(self.TRANSCTION_FILE)
        
        print("---------------------------ISSUED BOOKS------------------------------")
        print("---------------------------------------------------------------------")
        for t in transctions:
            for m in members:
                if t["member_id"] == m["member_id"]:
                    for book in books:
                        if book["book_id"] == t["book_id"]:
                            print(f"{m["name"]}---------{book["title"]}------{t["issue_date"]}")
                            



