import csv

headers = ['id', 'name', 'surname']

def load_authors():
    with open('english_authors_list.csv', mode='r', encoding='utf-8') as file:
        print("-----------------------------------------------------------------")
        authors = list(csv.DictReader(file))
        for auth in authors:
            print(f"{auth['id']}: {auth['name']} {auth['surname']}")
        return authors

def save_authors(authors):
    with open('english_authors_list.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(authors)

def create_authors(authors):
    print("adding authors:")
    print("add name")
    name = input()
    print("add surname")
    surname = input()
    new_id = str(int(authors[-1]['id']) + 1) if len(authors) > 0 else '1'
    authors.append(  {
                    'id': new_id,
                    "name":name,
                    "surname":surname,
                })
    save_authors(authors)

def correct_authors(authors):
    print("select id to be corrected.")
    id = input()
    for auth in authors:
        if id == str(auth['id']):
            print(f"{auth['id']}, Name: {auth['name']}, Surname: {auth['surname']}")
            auth['name'] = input("Correct name: ")
            auth['surname'] = input("Correct surname: ")
            save_authors(authors)

def delete_authors(authors):
    id_to_delete = input("Select id to be deleted: ")
    for auth in authors:
        if id_to_delete == str(auth['id']):
            print(f"{auth['id']}. Delete: {auth['name']} {auth['surname']} ")
            authors.remove(auth)
            print("Author deleted!")
        save_authors(auth)
def print_info():
    authors = load_authors()  # <-- Ielasām datus no CSV faila

    while True:
        print("---------------------------------------------")
        print("1. Show all authors")
        print("2. Add author")
        print("3. Edit author")
        print("4. Delete author")
        print("5. Exit")
        choice = input("Choose: ")







