import requests
import json

def haveibeenpwned(email):
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + email
    headers = {'hibp-api-key': 'YOUR_HIBP_API_KEY_HERE'}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print("Cette adresse email n'a pas été compromise dans une fuite de données connue.")
    elif response.status_code == 200:
        data = json.loads(response.text)
        print("Cette adresse email a été compromise dans les fuites de données suivantes :")
        for i in range(len(data)):
            print("- " + data[i]['Title'])

def intelx(query):
    url = "https://public.intelx.io/intelx/search"
    headers = {'x-key': 'YOUR_INTELEX_API_KEY_HERE'}

    payload = {
        "term": query,
        "buckets": "",
        "maxresults": 10
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        if data['status'] == "ok" and len(data['records']) > 0:
            print("Voici les résultats de recherche pour '" + query + "' sur Intelx :")
            for i in range(len(data['records'])):
                print("- " + data['records'][i]['title'])
        else:
            print("Aucun résultat de recherche trouvé sur Intelx pour '" + query + "'.")
    else:
        print("Erreur lors de la recherche sur Intelx.")

# Demande à l'utilisateur l'adresse email, le numéro de téléphone ou l'adresse IP à vérifier
query = input("Entrez une adresse email, un numéro de téléphone ou une adresse IP : ")

# Vérifie si l'adresse email a été compromise dans une fuite de données avec HaveIBeenPwned
if "@" in query:
    haveibeenpwned(query)

# Recherche les résultats de recherche pour le numéro de téléphone ou l'adresse IP sur Intelx
else:
    intelx(query)
