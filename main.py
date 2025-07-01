# This is a sample Python script.

from db_CRUD import*
from fileCrud import print_authors, print_info

while True:
    authors = load_authors()
    print_info()
    choice = input()

    match choice:
        case "1":
            print_authors(authors)
        case "2":
            add_author(authors)
        case "3":
            correct_author(authors)
        case "4":
            delete_authors(authors)
        case "5":
            print("Exit page:")
            break














