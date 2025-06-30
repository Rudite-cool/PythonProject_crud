# This is a sample Python script.
from fileCrud import correct_authors, delete_authors, load_authors, add_authors, print_authors, print_info

authors = load_authors()

while True:
    print_info()
    choice = input()

    match choice:
        case "1":
            print_authors(authors)
        case "2":
            add_authors(authors)
        case "3":
            correct_authors(authors)
        case "4":
            delete_authors(authors)
        case "5":
            print("Exit page:")
            break











