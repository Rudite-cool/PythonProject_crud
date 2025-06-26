# This is a sample Python script.


books = [
    {
        'id': 1,
        "name": "Agatha",
        "surname": "Christie",
        "title": "The Clocks",
        "genre": "Detective"
    },
    {
        'id': 2,
        "name": "George",
        "surname": "Orwell",
        "title": "Farm",
        "genre": "Allegory"
    },
    {
        'id': 3,
        "name": "Charlotte",
        "surname": "Brontë",
        "title": "Jane Eyre",
        "genre": "Novel"
    }
]
id_counter=3

while True:
    print("---------------------------------------------")
    print("1. Show all books")
    print("2. Add new book")
    print("3. Correct list")
    print("4. Delete book")
    print("5. Exit")
    print("-----------------Selection:-------------------")
    choise = input()

    match choise:
        case "1":
            print("Book Details:")
            for book in books:
                print(f"Id: {book['id']}, Name: {book['name']}, Title: {book['title']}, Genre: {book['genre']}")
            print("-----------------------------------------------------------------")
        case "2":
            print("Add new:")
            print("add name")
            name = input()
            print("add surname")
            surname = input()
            print("add title")
            title = input()
            print("add genre")
            genre = input()
            id_counter += 1
            books.append(
            {
                'id': id_counter,
                "name": name,
                "surname": surname,
                "title": title,
                "genre": genre
            }
            )
        case "3":
            print("Select id to be corrected:")
            id_to_correct = input()
            for book in books:
                if id_to_correct == str(book['id']):
                    print(f"{book['id']},Name: {book['name']}, Title: {book['title']}, Genre: {book['genre']}")
                    print("Correct:")
                    print("correct name")
                    name = input()
                    print("correct surname")
                    surname = input()
                    print("add title")
                    title = input()
                    print("add genre")
                    genre = input()
                    break
        case "4":
            print("Select id to be deleted:")
            id_to_delete = input()
            for book in books:
                if id == str(book['id']):
                    print(f"{book['id']}. Delete: Books {book['name']} {book['surname']} {book['title']} {book['genre']}")
                    print("Book deleted.")
                    break

        case "5":
            print("Exit page:")
            break






