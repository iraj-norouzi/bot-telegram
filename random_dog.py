import requests
def rand_dog():
    url = 'https://dog.ceo/api/breed/airedale/images/random'
    reponse = requests.get(url)
    reponse = reponse.json()
    reponse = reponse['message']
    print (reponse)
    return reponse
#rand_dog()