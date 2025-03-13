class Book:
    book_title_set = set()
    # Constructor
    def __init__(self, title, genre, ISBN, numOfPages):
        self.title = title
        self.genre = genre
        self.ISBN = ISBN
        self.numOfPages = numOfPages

    # Return to Menu
    def return_to_menu(self):
        valid_choices = {'y': self.LibraryMenu, 'n': self.Exit}
        valid_choice = False
        while not valid_choice:
            choice = input("Return to menu?[y/n]: ")
            if choice not in valid_choices:
                print("ERROR | invalid_input")
            else:
                valid_choice = True
        valid_choices[choice]()

    # Search Book File
    def search_book_file(self):
        valid_book_title = False

        while valid_book_title == False:
            book_title = input("Search | Book Title: ")
            if book_title not in Book.book_title_set:  # If Input is not Blank
                print("ERROR | invalid_book_title_input")
            else:
                valid_book_title = True
        return book_title

    # [1] | Create Book File
    def CreateBookFile(self):
        print("creating book file...")
        valid_book_title = False

        while valid_book_title == False:
            book_title = input("Book Title: ")

            if book_title.strip():  # If Input is not Blank
                valid_book_title = True
            else:
                print("ERROR | invalid_book_title_input")

        Book.book_title_set.add(book_title) # Add Book Title to Booklist

        with open('.txt/' + book_title + '.txt', 'w') as book:
            book.write("Title: " + book_title + '\n')

        print("successfully created book file!")
        self.return_to_menu()

    # [2] | Input Book Information
    def InputBookInformation(self):
        print("input book information...")
        valid_book_title = False
        valid_book_genre = False
        valid_book_ISBN = False
        valid_book_num_of_pages = False

        book_title = self.search_book_file()

        print("book file found!")
        while valid_book_genre == False:
            book_genre = input("Genre: ")
            if book_genre.strip():
                valid_book_genre = True
            else:
                print("ERROR | invalid_book_genre_input")

        while valid_book_ISBN == False:
            book_ISBN = input("ISBN: ")
            if book_ISBN.strip():
                valid_book_ISBN = True
            else:
                print("ERROR | invalid_book_ISBN_input")

        while valid_book_num_of_pages == False:
            book_num_of_pages = int(input("# of Pages: "))
            if book_num_of_pages > 0:
                valid_book_num_of_pages = True
            else:
                print("ERROR | num_of_pages_must_be_at_least_one")

        with open('.txt/' + book_title + '.txt', 'a') as book:
            book.write("Genre: " + book_genre + '\n')
            book.write("ISBN: " + book_ISBN + '\n')
            book.write("# of Pages: " + str(book_num_of_pages))

        print("book information completed!")
        self.return_to_menu()

    # [3] | Read Book File
    def ReadBookFile(self):
        print("reading book file...")
        book_title = self.search_book_file()

        print("-------FILE  CONTENT-------")
        with open('.txt/' + book_title + '.txt', 'r') as book:
            readContent = book.read()
            print(readContent)
        print("---------------------------")

        self.return_to_menu()

    # [4] | Update Book Information
    def UpdateBookInformation(self):
        print("updating book information...")
        book_title = self.search_book_file()

        with open('.txt/' + book_title + '.txt', 'r') as book:
            line = book.readlines()
            print("book file found!")
            print("-------FILE  CONTENT-------")
            print("".join(line))
            print("---------------------------")

        print("[ Title | Genre | ISBN | Page Number ]")
        valid_input = False
        while not valid_input:
            info = input("Edit Information: ").lower()

            if info == "title":
                line_number = 0
                valid_input = True
            elif info == "genre":
                line_number = 1
                valid_input = True
            elif info == "isbn":
                line_number = 2
                valid_input = True
            elif info == "page number":
                line_number = 3
                valid_input = True
            else:
                print("Invalid Input. Please Enter the Information to Edit.")

        info_edit = input("Updated Info: ") + '\n'
        line[line_number] = info_edit

        with open(f'.txt/{book_title}.txt', 'w') as book:
            book.writelines(line)

        print("information updated successfully!")
        self.return_to_menu()

    # [5] | Delete Book File
    def DeleteBookFile(self):
        print("deleting book file...")
        self.return_to_menu()

    # [6] | Create Book File
    def ShowBookList(self):
        print("showing book list...")
        self.return_to_menu()

    # [7] | Borrow Book
    def BorrowBook(self):
        print("borrowing book...")
        self.return_to_menu()

    # [8] | Return Book
    def ReturnBook(self):
        print("returning book...")
        self.return_to_menu()

    # [9] | Search Book
    def SearchBook(self):
        print("searching book...")
        self.return_to_menu()

    # [10] | Borrow History
    def BorrowHistory(self):
        print("displaying borrow history...")
        self.return_to_menu()

    # [11] | Return History
    def ReturnHistory(self):
        print("displaying return history...")
        self.return_to_menu()

    # [12] | Table of Contents
    def TableOfContents(self):
        print("displaying table of contents...")
        self.return_to_menu()

    # [13] | Exit
    def Exit(self):
        print("exiting system...")
        exit()

    # Display Library Menu
    def LibraryMenu(self):
        # Function Library
        input_choice = {
            1: self.CreateBookFile,
            2: self.InputBookInformation,
            3: self.ReadBookFile,
            4: self.UpdateBookInformation,
            5: self.DeleteBookFile,
            6: self.ShowBookList,
            7: self.BorrowBook,
            8: self.ReturnBook,
            9: self.SearchBook,
            10: self.BorrowHistory,
            11: self.ReturnHistory,
            12: self.TableOfContents,
            13: self.Exit
        }

        while True:
            print("===+==+==+== iLMS ==+==+==+===")
            print("| -Library-Management-System- |")
            print("-_-_-_-_-_-[LIBRARY]-_-_-_-_-_-")
            print("-------------------------------")
            print("[1] | Create Book File")
            print("[2] | Input Book Information")
            print("[3] | Read Book File")
            print("[4] | Update Book Information")
            print("[5] | Delete Book File")
            print("[6] | Show Booklist")
            print("[7] | Borrow Book")
            print("[8] | Return Book")
            print("[9] | Search Book")
            print("[10] | Borrow History")
            print("[11] | Return History")
            print("[12] | Table of Contents")
            print("[13] | Exit")
            print("-------------------------------")

            # Exception Handling
            try:
                choice = int(input(">> "))
                if choice in input_choice:
                    input_choice[choice]()
                else:
                    print("ERROR | out_of_bounds_input")
            except ValueError:
                print("ERROR | invalid_input")

b1 = Book("To Kill a Mockingbird", "Non-Fiction", 117591120149, 273)
default = Book("", "", "", 0)
#default.Menu() # [PROGRAM]
default.LibraryMenu() # [DEBUGGING]
