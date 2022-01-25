
def request_name():
    name=""
    name = input("What is your name ? ") 

    while name == "":    
        print("ERROR : Please type your name")
        name = input("What is your name ? ") 
    return name

def request_old(person_name):
    age_pro = 0
    while age_pro == 0:
        old = input(person_name + ", how old are you ? ")
        try:
            age_pro = int(old)
        except:
            print("ERROR : You must type a number ")
        if age_pro <= 10:
            print(person_name + ", you are a child")
        elif 12 <= age_pro < 17:
            print(person_name + ", you are adolescent")
        elif age_pro == 17:
            print(person_name + ", you are almost major")
        elif age_pro == 18:
            print(person_name + ", congradulation, you are almost major")
        elif age_pro > 18:
            print(person_name + ", you are major")
        elif age_pro >= 60:
            print(person_name + ", you are senior")
        else :
            print(person_name + ", you are minor")

    return age_pro
    


def print_person_info(person_name, age_pro):  
    print(person_name + ", you have", age_pro,"years old")
    print(person_name + ", you will have",age_pro+1, "years old next years")

 
def type_password(person_name):
    type_password = input(person_name + ", type your password : ")
    while not type_password == mot_de_passe :
            print("ERROR : You must type a true password !")
            type_password = input(person_name + ", type your password : ")
    return type_password

name = request_name()
age_pro = request_old(name)


print_person_info(name, age_pro)
mot_de_passe = input(name + ", create your password : ")
type_password(name)
print("Password is true : You are connected",name + "...")












    