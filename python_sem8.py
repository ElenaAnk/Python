
def write_name():
    name=input("Введите имя: ").capitalize()
    return name

def write_surname():
    surname=input("Введите фамилию: ").capitalize()
    return surname

def write_phone():
    phone=input("Введите телефон: ")
    return phone

def write_adress():
    adress=input("Введите адрес: ").title()
    return adress

def input_data():
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open("phonebook.txt", "a",encoding="utf-8") as data:
        data.write(f"{name} {surname}: {phone}, {adress}\n")

def print_data():
    with open("phonebook.txt", "r",encoding="utf-8") as data:
        data_first=data.readlines()
        for line in data_first:
            print(line)

def search_line():
    search=input("Введите данные для поиска: ")
    with open("phonebook.txt","r",encoding="utf-8") as data:
        temp=data.readlines()
        for line in temp:
            if search in line:
                print(line)

def interface():
    command=0
    while command!="6":
        print("""Что вы хотите сделать?
              1- записать данные
              2- посмотреть данные
              3- найти данные
              4- изменить данные
              5- удалить данные
              6- выход""")
        command = input("Введите номер операции: ")
        while command not in ("1","2","3","4","5","6"):
            print("Введите корректный номер операции")
            command=input("Введите номер операции: ")
        if command =="1":
            input_data()
        elif command == "2":
            print_data()
        elif command == "3":
            search_line()
        elif command == "4":
            change_data()
        elif command == "5":
            delete_data()

def change_element():
    
    old_str=input("Введите элемент,который хотите изменить: ")
    new_str=input("Введите новые данные: ")
    with open("phonebook.txt","r",encoding="utf-8") as data:
         old_data =data.read()
    new_data = old_data.replace(old_str,new_str)
    with open("phonebook.txt","w",encoding="utf-8") as data:
        data.write(new_data)
         
def change_str():
    old_str=input("Введите элемент строки,которую хотите заменить: ")
    with open("phonebook.txt","r",encoding="utf-8") as data, open("phonebook_new.txt","w",encoding="utf-8") as data_new:
     for line in data:
        if old_str not in line:
            data_new.write(line)
    
    import os
    os.remove("phonebook.txt")
    os.rename("phonebook_new.txt", "phonebook.txt")

    input_data()

def change_data():
    command=0
    while command!="3":
        print("""Что вы хотите изменить?
              1- изменить элемент(ы) справочника
              2- заменить полностью строку справочника
              3- выход""")
        command = input("Введите номер операции: ")
        while command not in ("1","2","3"):
            print("Введите корректный номер операции")
            command=input("Введите номер операции: ")
        if command =="1":
            change_element()
        elif command == "2":
            change_str()    

def delete_data():
    old_str=input("Введите элемент(ы) строки,которую хотите удалить: ")
    with open("phonebook.txt","r",encoding="utf-8") as data, open("phonebook_new.txt","w",encoding="utf-8") as data_new:
     for line in data:
        if old_str not in line:
            data_new.write(line)

    import os
    os.remove("phonebook.txt")
    os.rename("phonebook_new.txt", "phonebook.txt")
                 

interface()