"""
def table_de_multiplication(n, min=1 , max=1):
    n2 = ""
    while n2 == max:
        for n2 in range(max):
            mult(n+min)






def mult(n, n2):
   n = ""

"""




def table_de_multiplication_question():
    
    table_de = input("Quelle table de multiplication : ")
    commencer_de = input("Vous voulez commencer de : ")
    terminer_a = input("Et terminer à : ")
    while terminer_a < commencer_de:
        print("ERREUR : Terminer doit être supérieur à commencer ")
        commencer_de = input("Vous voulez commencer de : ")
        terminer_a = input("Et terminer à : ")
    for i in range(int(commencer_de), int(terminer_a)+1):
        print(i, "X", table_de, "=", int(table_de)*int(i))
    

table_de_multiplication_question()
