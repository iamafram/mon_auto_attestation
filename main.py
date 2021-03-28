from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from os import system
from tqdm import tqdm


dico = {
    "id_and_class" : [
        "field-firstname", "field-lastname", "field-birthday",
        "field-placeofbirth", "field-city", "field-address",
        "field-zipcode", "field-heuresortie", "quarantine-button",
        "checkbox-sport", "generate-btn", "checkbox-1-sport"
    ],
    "champs" : [
        "firstname", "lastname", "JJ/MM/AAAA",
        "place_of_bitrh", "city", "adresse",
        "zip_code", "hour", "arison_sortie"
        ]
}

def sortie() :
    system('clear')
    print("""
    --- Tout d'abord quelle est la raison de votre sortie  ? ---


    [1] Activité physique et promenade 
    [2] Achats
    [3] Accompagnement des enfants à l’école
    [4] Etablissement culturel ou lieu de culte
    [5] Démarches administratives ou juridiques
    [6] Activité professionnelle, enseignement et formation, mission d’intérêt général
    [7] Santé (consultations et soins)
    [8] Motif familial impérieux, personnes vulnérables ou précaires ou gardes d’enfants
    [9] Situation de handicap
    [10] Convocation judiciaire ou administrative
    [11] Déménagement
    [12] Déplacement de transit vers les gares et les aéroports
    
    ---------""")

    while True : 
        try :
            choix = int(input(" - "))
            while not(choix > 0 and choix < 13) : 
                choix = int(input("Veuillez entrer un nombre entre 1 et 12 : \n - "))
            break
        except ValueError :
            print("Veuillez entrer un entier ! ")

    return choix

def traite_sortie() :
    resultat = sortie()

    if resultat == 1 : dico["id_and_class"][11] = "checkbox-1-sport"
    elif resultat == 2 : dico["id_and_class"][11] = "checkbox-3-achats"
    elif resultat == 3 : dico["id_and_class"][11] = "checkbox-4-enfants"
    elif resultat == 4 : dico["id_and_class"][11] = "checkbox-5-culte_culturel"
    elif resultat == 5 : dico["id_and_class"][11] = "checkbox-6-demarche"
    elif resultat == 6 : dico["id_and_class"][11] = "checkbox-8-travail"
    elif resultat == 7 : dico["id_and_class"][11] = "checkbox-9-sante"
    elif resultat == 8 : dico["id_and_class"][11] = "checkbox-10-famille"
    elif resultat == 9 : dico["id_and_class"][11] = "checkbox-11-handicap"
    elif resultat == 10 : dico["id_and_class"][11] = "checkbox-12-judiciaire"
    elif resultat == 11 : dico["id_and_class"][11] = "checkbox-13-demenagement"
    elif resultat == 12 : dico["id_and_class"][11] = "checkbox-14-transit"

def saisie() :

    print("--- Identité --- \n ")
    dico["champs"][0] = input("quel est votre prénom ?")
    dico["champs"][1] = input("quel est votre nom ?")
    dico["champs"][2] = input("quel est votre date de naissance ? [JJ/MM/AAAA] ?")
    dico["champs"][3] = input("quel est votre lieu de naissance ?")
    dico["champs"][4] = input("quel est votre ville ?")
    dico["champs"][5] = input("quel est votre adresse postale ?")
    dico["champs"][6] = int(input("quel est votre code postal ?"))
    dico["champs"][7] = datetime.now().strftime('%H:%M')

    print("\n \n Le début de l'opération va commencer, une fenêtre va s'ouvrir \n")


def partie() :
    driver.find_element_by_id(dico["id_and_class"][0]).send_keys(dico["champs"][0])
    driver.find_element_by_id(dico["id_and_class"][1]).send_keys(dico["champs"][1])
    driver.find_element_by_id(dico["id_and_class"][2]).send_keys(dico["champs"][2])
    driver.find_element_by_id(dico["id_and_class"][3]).send_keys(dico["champs"][3])
    driver.find_element_by_id(dico["id_and_class"][4]).send_keys(dico["champs"][4])
    driver.find_element_by_id(dico["id_and_class"][5]).send_keys(dico["champs"][5])
    driver.find_element_by_id(dico["id_and_class"][6]).send_keys(dico["champs"][6])
    driver.find_element_by_id(dico["id_and_class"][7]).send_keys(dico["champs"][7])

    time.sleep(0.5)

    driver.find_element_by_class_name(dico["id_and_class"][8]).click()

    driver.find_element_by_id(dico["id_and_class"][11]).click()

    driver.find_element_by_id(dico["id_and_class"][10]).click()
    

options = Options()
# options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")

traite_sortie()
saisie()

driver = webdriver.Chrome(options=options)
driver.get("https://media.interieur.gouv.fr/attestation-deplacement-derogatoire-covid-19/")

time.sleep(3)
driver.refresh()

partie()
