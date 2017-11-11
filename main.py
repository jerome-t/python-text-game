"""
Text-based RPM in french
Created by Jerome Tissieres - November 2017
"""

from room import Room
from item import Item
from character import Enemy, Character, Friend


# Define the rooms
cuisine = Room("la cuisine")
cuisine.set_description("Une cuisine sombre et sale.")

salle_a_manger = Room("la salle a manger")
salle_a_manger.set_description("Une grande salle à manger pour 8 personnes.")

salon = Room("le salon")
salon.set_description("Un salon accueillant avec un grand canapé.")



# Define the links between the rooms
cuisine.link_room(salle_a_manger, "sud")
salle_a_manger.link_room(cuisine, "nord")
salle_a_manger.link_room(salon, "ouest")
salon.link_room(salle_a_manger, "est")



# Define the items
fromage = Item("fromage")
fromage.set_readable_name("du fromage")
fromage.set_description("Il sent encore plus mauvais que le zombie !")
cuisine.set_item(fromage)

livre = Item("livre")
livre.set_readable_name("un livre")
livre.set_description("Un très gros livre intitulé \"Python pour les nuls\".")
salon.set_item(livre)



# Define the people
dave = Enemy("Dave", "Un zombie puant")
dave.set_conversation("Arrrgggg... yahhhhh... manger...")
dave.set_weakness("fromage")
salon.set_character(dave)

olga = Friend("Olga", "Un squelette sympa")
olga.set_conversation("Salut ! Je suis un tas d'os.")
cuisine.set_character(olga)

tabatha = Enemy("Tabatha", "Une énorme araignée aux pattes velues.")
tabatha.set_conversation("Pfffff.... Je m'ennuie...")
tabatha.set_weakness("livre")
salle_a_manger.set_character(tabatha)



#Start:
current_room = cuisine
backpack = []
dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    object = current_room.get_item()
    if object is not None:
        object.describe()

    command = input("Que voulez-vous faire ?\n[nord, sud, est, ouest, parler, attaquer, prendre]\n> ")

# Se déplacer entre les room
    if command in ["nord", "sud", "est", "ouest"]:
        current_room = current_room.move(command)


# Parler a quelqu'un
    elif command == "parler":
        if inhabitant is not None:
            print("[Tu dis]: Bonjour! ")
            inhabitant.talk()
        else:
            print("Il n'y a personne a qui parler ici.")


# Attaquer quelqu'un
    elif command == "attaquer":
        if inhabitant is not None:
            print("Avec quoi veux-tu l'attaquer ?")
            print("Contenu de ton sac : ")
            print(backpack)
            fight_with = input(" > ")

            # Avons-nous ceci dans le sac?
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Bien joué !")
                else:
                    print("Tu as mort !")
                    print("Fin du jeu.")
                    dead = True
            else:
                print("Tu n'as pas " + fight_with)
        else:
            print("Il n'y a personne avec qui se battre ici.")


# Prendre qqchose
    elif command == "prendre":
        if object is not None:
            print("Tu as mis " + object.get_readable_name() + " dans ton sac.")
            backpack.append(object.get_name())
            current_room.set_item(None)
        else:
            print("Il n'y a rien a prendre ici !")


# Commande inconnue
    else:
        print("Je ne sais pas comment faire ceci : " + command)

