""""use with https://pokeapi.co/docs/v2"""


import requests 

def protocolpokeapi(id=1):

    url=f"https://pokeapi.co/api/v2/pokemon/{id}/"
    

    try:
        response = requests.get(url)
    except:
        return ""
    return response