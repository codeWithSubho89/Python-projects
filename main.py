from book_management import BookManagement
from member_management import Member
from transction import Transction

def main():
    bm = BookManagement()
    mm = Member()
    t = Transction()

    while True:
        print("\n---------- LIBRARY MANAGEMENT SYSTEM ----------")
        print("Press 1: Add Book")
        print("Press 2: View Books")
        print("Press 3: Update Quantity")
        print("Press 4: Remove Book")
        print("Press 5: Add Member")
        print("Press 6: Remove Member")
        print("Press 7: Display Member")
        print("Press 8: DeActivate & Activate Member")
        print("Press 9: Issue Book")
        print("Press R: Return Book")
        print("Press D: Issue Details")
        print("Press 0: Exit")
        print("------------------------------------------------")

        choice = input("Enter Choice: ").strip().lower()

        if choice == '1':
            bm.add_books()
        elif choice == '2':
            bm.display_books()
        elif choice == '3':
            bm.update_quantity()
        elif choice == '4':
            bm.remove_book()
        elif choice == '5':
            mm.add_member()
        elif choice == '6':
            mm.delete_member()
        elif choice == '7':
            mm.disply_member()
        elif choice == '8':
            mm.deAcivate_member()
        elif choice == '9':
            t.issue_book()
        elif choice == 'r':
            t.return_book()
        elif choice == 'd':
            t.showIssuedBooks()
        elif choice == '0':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

main()

        

