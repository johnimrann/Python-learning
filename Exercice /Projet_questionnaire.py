str_reponse = ""
def choix(ans1, ans2):
    print(ans1, ans2)
    reponse = input("Please enter the answers : ")
    #str_reponse = str(reponse)
    return reponse
    
def answer_letter(bonne_rep):
    if str_reponse == str(bonne_rep):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

def question(your_question):
    print(your_question)

def factor_quest():
    global str_reponse
    question("Quelle est la capitale de la France?")
    str_reponse = choix("Luxembourg" , "Paris")
    answer_letter("b")



