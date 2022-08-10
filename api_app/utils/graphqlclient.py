"""Use graphQL protocol"""

"""get information from URL fo pokemon"""
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import requests, json

# https://github.com/PokeAPI/pokebase
# https://pokeapi.co/docs/v2
def evolutionchain(id:int):
        
    # Select your transport with a defined url endpoint
    url= f"https://beta.pokeapi.co/graphql/v1beta/"
    transport = AIOHTTPTransport(url)

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    # Provide a GraphQL query
    query = gql(
        """
        query MyQuery {
            pokemon_v2_evolutionchain(where: {id: {_eq: %s}}) {
                pokemon_v2_pokemonspecies {
                    name
                }
                id
            }
        }
        """ % id
    )
    
        
    # Execute the query on the transport
    result = client.execute(query)
    # print(result)
    
    return result

def get_info(name:str):
    info = {}

    url=f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response= requests.get(url)

    jres= response.json()

    info['name'] = jres['name']
    info['height'] = jres['height']
    info['weight'] = jres['weight']
    stats = jres['stats']
    list_base_stats = []
    for stat in stats:
        base_stats={
            'base_stat': stat['base_stat'],
            'name': stat['stat']['name']
        }
        list_base_stats.append(base_stats)
    info['base_stats']=list_base_stats


    return info    




def parameters(id:int):
    
    # Select your transport with a defined url endpoint
    response = evolutionchain(id)
    # obtengo los nombres
    data = response['pokemon_v2_evolutionchain']
    evolutions = data[0]['pokemon_v2_pokemonspecies']


    list_info_full = []
    for evolution in evolutions:
        information_full = {}
        information_full['id_evolution'] = id
        information_full['evolution'] = evolutions   # lista con los nombres
        
        particular_info = get_info(name=evolution['name']) # obtengo el resto de datos particulares.

        information_full['name'] = particular_info['name']
        information_full['height'] = particular_info['height']
        information_full['weight'] = particular_info['weight']
        information_full['base_stats'] = particular_info['base_stats']
        list_info_full.append(information_full)
    
    # import pdb; pdb.set_trace()  # debug
    
    return list_info_full

