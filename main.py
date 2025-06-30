# This is a sample Python script.
from fileCrud import correct_authors, delete_authors, create_authors, print_info, load_authors

authors = load_authors()


def print_authors(authors):
    pass


while True:
    print_info()
    choice = input()


    match choice:
        case "1":
            print_authors(authors)
        case "2":
            create_authors(authors)
        case "3":
            correct_authors(authors)
        case "4":
            delete_authors(authors)
        case "5":
            print("Exit page:")
            break







