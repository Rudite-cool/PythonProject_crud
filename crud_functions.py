from main import books


def show_books():
    print("Book Details:")
    for book in books:
        print(f"Id: {book['id']}, Name: {book['name']}, Title: {book['title']}, Genre: {book['genre']}")
    print("-----------------------------------------------------------------")

def add_book():
    global id_counter
    print("Add new:")
    name = input("Add name: ")
    surname = input("Add surname: ")
    title = input("Add title: ")
    genre = input("Add genre: ")
    id_counter += 1
    books.append({
        'id': id_counter,
        "name": name,
        "surname": surname,
        "title": title,
        "genre": genre
    })
    print("Book added!")

def correct_book():
    id_to_correct = input("Select id to be corrected: ")
    for book in books:
        if id_to_correct == str(book['id']):
            print(f"{book['id']}, Name: {book['name']}, Surname: {book['surname']}, Title: {book['title']}, Genre: {book['genre']}")
            book['name'] = input("Correct name: ")
            book['surname'] = input("Correct surname: ")
            book['title'] = input("Correct title: ")
            book['genre'] = input("Correct genre: ")
            print("Book updated!")
            return
    print("Book not found!")

def delete_book():
    id_to_delete = input("Select id to be deleted: ")
    for book in books:
        if id_to_delete == str(book['id']):
            print(f"{book['id']}. Delete: {book['name']} {book['surname']} {book['title']} {book['genre']}")
            books.remove(book)
            print("Book deleted!")
            return
    print("Book not found!")
