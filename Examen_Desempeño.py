students = []


def registre_student():
    try:

        id= int(input("INgrese ID: "))
        name=input("Enter your name: ") 
        age= int(input("Enter your age: "))
        program =input("Enter your program: ")
        state = input("Enter your state(active / passive): ")

        student = {
            "id": id,
            "name": name,
            "age" : age,
            "program": program,
            "state" : state
        }

        students.append(student)
        print("Student registre")

    except ValueError:
        print("mistake : you migth registre number in ID and age")


def see_students():
    if len(students) == 0:
        print("there is not student registre")

    else:
        for e in students:
            print(e)

def search_student():
    try:
        id= int(input("enter ID: "))

        for e in students:
            if e ["id"] == id:
                print("Student search")

                print(e)
                return
            
        print("student no search")

    except ValueError:
        print("mistake: the ID must number")

def update_student():
    try:
        id = int(input("enter id update: "))

        for e in students:
            if e ["id"] == id:
                print("if not update")

                name = input("new name: ")
                age = input("new age: ")
                program = input("new program: ")
                state = input("new state: ")

                if name != "" :
                    e["name"] = name
                if age != "":
                    e["age"] = int(age)
                if program != "":
                    e["program"] = program
                if state != "":
                    e["state"] = state

                print("student update succefull")

                return
            
        print("student not search")

    except  ValueError:
        print("mistake: Age and ID incorrect")


def remove_student ():
    try:
        id = int(input("enter a student remove: "))

        for e in students:
            if e ["id"] == id:
                students.remove(e)
                print("Student remove")

    except ValueError:
        print("mistake : The ID  can be number")


def menu ():
    while True:
        print("1. Enter student")
        print("2. See studen")
        print("3. Search studen")
        print("4. New information about student")
        print("5. remove student")
        print("6. Exit, thank so much")

        opcion = input("choose a opcion: ")

        if opcion == "1":
            registre_student()
        elif opcion == "2":
            see_students()
        elif opcion == "3":
            search_student()
        elif opcion =="4":
            update_student()
        elif opcion == "5":
            remove_student()
        elif opcion == "6":
            print("Exit system")

            break
        else:
            print("try again")


menu ()




    


        





        
    

    






    


