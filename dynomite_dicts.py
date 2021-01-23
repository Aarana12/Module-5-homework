if __name__ == "__main__":
    pokedex = {
        'Venosaur' : ['Grass', 'Poisen'],
        'Charizard' : ['Fire', 'Flying'],
        'Blatoise' : ['Water']
    }
    print(pokedex)

    del pokedex['Blatoise']

    print(pokedex)
