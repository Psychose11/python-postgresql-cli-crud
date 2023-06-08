#pip install psycopg2
#sudo service postgresql start : démarrage services
#sudo -u postgres psql : création de la base et connection entant que "postgres"
#ALTER USER postgres WITH PASSWORD 'nouveau_mot_de_passe'; changement de mot de passe de postgresql 


#CREATE DATABASE Data;
#\c Data; selection de la base




#creation de la table
#CREATE TABLE utilisateurs (
    #id SERIAL PRIMARY KEY,
    #nom VARCHAR(50)
#); creation de la table

import psycopg2

#connexion à la base data
conn = psycopg2.connect(
    host="localhost",
    database="data",
    user="postgres",
    password="postgres"
)
   cursor = conn.cursor()

def ajout():
   
 
    nouveau_titan = input("Quel est le nom du nouveau titan?  : \n")
    requete="INSERT INTO titans (nom) VALUES (%s);"
    cursor.execute(requete , (nouveau_titan,))
    conn.commit()
    print("nouveau titan ajouté\n")
    Send a message.
def supprimer():
   
    delete=input("quel est le titan à supprimer? : ")
    requete="DELETE FROM titans where numero = (%d);"
    cursor.execute(requete , (delete,))    
    conn.commit()
    print("titan supprimé")
    
def afficher():
    select_query = "SELECT numero,nom FROM titans;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("voici nos titans :")
    for row in rows:
        print(row[0]," -",row[1])
   

    
def process_choice(choice):
    if choice == "1":
        afficher()
    elif choice == "2":
        ajout()
    elif choice == "3":
        supprimer()
    elif choice == "4":
        modifier()
    else:
        print("Choix invalide")


print("Bienvenue sur les titans\n")

while True:
    print("Entrez votre choix:\n 1 - Afficher la liste\n 2 - Ajouter un nouveau titan\n 3 - Supprimer un titan\n 4 - Modifier un titan\n")

    user_choice = input("Votre choix : ")

    process_choice(user_choice)
    
    
    
cursor.close()
conn.close()