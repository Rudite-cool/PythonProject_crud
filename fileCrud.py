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

def add_authors(authors):
    print("Adding author:")
    name = input("Add name: ")
    surname = input("Add surname: ")
    new_id = str(int(authors[-1]['id']) + 1) if len(authors) > 0 else '1'
    authors.append({
        'id': new_id,
        'name': name,
        'surname': surname,
    })
    save_authors(authors)
    print("Author added!")

def correct_authors(authors):
    print("Select ID to be corrected:")
    id = input()
    for auth in authors:
        if id == str(auth['id']):
            print(f"{auth['id']}, Name: {auth['name']}, Surname: {auth['surname']}")
            auth['name'] = input("Correct name: ")
            auth['surname'] = input("Correct surname: ")
            save_authors(authors)
            print("Author updated!")
            return
    print("Author not found!")

def delete_authors(authors):
    id_to_delete = input("Select ID to be deleted: ")
    for auth in authors:
        if id_to_delete == str(auth['id']):
            print(f"{auth['id']}. Delete: {auth['name']} {auth['surname']}")
            authors.remove(auth)
            save_authors(authors)
            print("Author deleted!")
            return
    print("Author not found!")

def print_info():
    print("---------------------------------------")
    print("1. Show all authors")
    print("2. Add author")
    print("3. Correct author")
    print("4. Delete author")
    print("5. Exit")
    print("------------------Select--------------------")

def print_authors(authors):
    print("Author list:")
    for auth in authors:
        print(f"{auth['id']}: {auth['name']} {auth['surname']}")
    print("--------------------------------------------------")





