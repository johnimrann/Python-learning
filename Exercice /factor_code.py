def recupérer_et_afficher_info_personne(numero_personne):
    nom = input("Nom de la personne "+ str(numero_personne)+ " :" )
    age = input("Age de la personne "+ str(numero_personne)+ " :")
    print("La personne est ", "son age est", age + "ans")
    print("Son nom comporte", len(nom), "lettres")

"""
On peut factoriser aussi c'est appel de fonction:

recupérer_et_afficher_info_personne(1)
recupérer_et_afficher_info_personne(2)
recupérer_et_afficher_info_personne(3) 

"""
def boucle_reaip():
    nb_personne = input("Nombre personne :")
    int_nb_personne = int(nb_personne)
    for i in range(int_nb_personne):
        recupérer_et_afficher_info_personne(i+1)

# Appel de ma fonction de boucle :

boucle_reaip()
