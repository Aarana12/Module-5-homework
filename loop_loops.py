if __name__ == "__main__":
    pokemon = ('picachu', 'charmander', 'bulbasaur')
    print(pokemon[0])

    pokemon = { 
        'starter1' : 'picachu',
        'starter2' : 'charmander',
        'starter3' : 'bulbasaur',
    }

    print(pokemon)

    name = tuple('Areli Arana')
    print('i' in name)

    numbers = []
    for i in range(2, 9):
        print(i)

    i = 2
    while i < int(10):
        print(i)
        i += 1

    string = 'This is a simple string'
    for letter in string:
        print(letter)
    
    
    loop = ('this', 'is', 'a', 'simple', 'set')
    number = [1, 2, 3]

    for word in loop:
        for letter in number:
            print(f'number = {letter}; word = {word}')


    
