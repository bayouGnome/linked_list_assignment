from client import Client
from linkedlist import LinkedList


def main():
    client_list = LinkedList()

    print ("Boudreaux's Barbershop")
    condition = True
    while condition:
        print("Type the number for the action you wish to perform and then hit Enter.")
        print("1. Add a new client")
        print("2. Display a list of all current clients")
        print("3. Search for a client")
        print("4. Delete a client")
        print("5. Quit")
        answer = input("What do you want to do? ")

        if answer == '1':
            name = input("Provide the clients name: ")
            phone = input("Provide the clients phone number: ")
            birthdate = input("Provide the clients D.O.B. in MMDDYYYY :")
            print()
            client_obj = Client(name, phone, birthdate)
            client_list.append(client_obj)

        elif answer == '2':
            print(client_list)

        elif answer == '3':
            search_for = input("Enter name to search: ")
            if search_for in client_list:
                print(search_for + " is in the list")
            else:
                print(search_for + "is not in the list")

        elif answer == '4':
            #delete client
            to_delete = input("Enter client name to delete")
            client_list.delete(to_delete)

        elif answer == '5':
            condition = False
            return
        else:
            pass






if __name__ == "__main__":
    main()

