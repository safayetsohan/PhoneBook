name = []
phone_no = []
email = []
address = []
y_n = 0
def main():
    print("__________________Welcome To Phone Book________________\n")
    print("\t 1) Add Contact\n\t 2) Delete Contact\n\t 3) Search Contact\n\t 4) See All Contact\n\t 5) Exit")
    choose = int(input("Please Choose A Number Between 1 to 5: "))
    choosen_function(choose)

def choosen_function(choosen):
    if (choosen == 1):
        person_name = input("Enter Name: ")
        name.append(person_name)

        mobile = input("Enter Phone No: ")
        phone_no.append(mobile)

        mail = input("Enter Email: ")
        email.append(mail)

        addr = input("Enter Address: ")
        address.append(addr)

        y_n = input("Do you want Save More(Y/N): ")
        yes_or_No(y_n)
        return main()
    elif (choosen == 2):
        search =  input("Please Enter Phone Number: ")

        if search in phone_no:
            for i in [i for i, x in enumerate(phone_no) if x == search]:
                name.pop(i)
                phone_no.pop(i)
                email.pop(i)
                address.pop(i)

            print("Delete Complete")
            return main()
        elif search not in phone_no:
            print("Phone No is Not valid")
            return main()
    elif (choosen==3):
        search1 = input("Please Enter Phone Number: ")

        if search1 in phone_no:
            for i in [i for i, x in enumerate(phone_no) if x == search1]:  #find the position of search1 in list
                print("Name: ",name[i])
                print("Phone No: ", phone_no[i])
                print("Name: ", email[i])
                print("Name: ", address[i])

            return main()
        elif search1 not in phone_no:
            print("Phone No is Not valid")
            return main()
    elif (choosen == 4):
        print("\t\t\t\tName\n")
        for n in name:
            print("Name: " +n)
        print("\t\t\t\tPhone_NO\n")
        for p in phone_no:
                print("Phone_No: " + p)
        print("\t\t\tEmail\n")
        for e in email:
            print(e)
        print("\t\t\t\tAddress\n")
        for a in address:
            print(a)
        return main()
    elif(choosen==5):
        return exit()
    else:
        print("Please Enter Correct Number :)")
        return main()




if __name__ == "__main__":
    main()
