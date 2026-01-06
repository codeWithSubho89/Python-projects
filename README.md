A simple console-based Library Management System built using Python and JSON file storage.
This project allows librarians to manage books, members, and book transactions such as issuing and returning books.

▶️ How to Run the Project

    Make sure Python 3 is installed.

    Clone or download the project.

    Create a folder named data in the project root.

    Inside data, create empty files:

    books.json

    members.json

    transctions.json

    Run the program:    

🚀 Features
    📘 Book Management

        Add new books

        Display all books

        Update book quantity

        Remove books from the library

    👤 Member Management

        Add new members

        Display members

        Activate / Deactivate members

        Delete members

    🔄 Transactions

        Issue books to members

        Return books

        View issued book details


Library-Management-System/
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── transctions.json
│
├── book_management.py
├── member_management.py
├── transction.py
├── file_handling.py
├── main.py
└── README.md


🛠️ Technologies Used

    Python 3

    JSON (for data storage)

    OS module (file handling)

    Datetime module


📦 Data Storage

All data is stored locally using JSON files:

    books.json → Book records

    members.json → Member records

    transctions.json → Issued book records