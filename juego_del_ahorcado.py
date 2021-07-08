import os
import random


def get_words():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        words = [word.strip().lower() for word in f]
    return words


def run():
    os.system('clear')
    words = get_words()
    word = random.choice(words) # seleccionando una palabra al azar en la lista words
    word_show_usr = list('_' * len(word)) # palabra que se le muestra al usuario 
    intent = len(word) * 2
    
    while word_show_usr != list(word):
        
        print('Bienvenido al juego del ahorcado\ntienes: ' + str(intent) + ' intentos para adivinar la palabra\nde lo contrario pierdes el juego, vamos!\n')
        for i in word_show_usr:
            print(i, end=' ')
        letter_usr = input('\n\nIngresa una letra: \n').strip().lower()
        
        try:
            if len(letter_usr) > 1 or len(letter_usr) < 1:
                raise ValueError('El dato ingresado ' + str(letter_usr) + ' no es valido') 
        except ValueError as ve:
            print(ve)
            return False
        
        os.system('clear')
        c = 0
        
        for letter in word:
            
            if letter == letter_usr:
                word_show_usr.pop(c)
                word_show_usr.insert(c, letter_usr)
                intent += 1
            c += 1
        intent -= 1
        if intent <= 0:
            result = 'Perdiste'
            break
        result = 'Ganaste'
    
    print('¡' + result + '! la palabra era: ' + str(word) + ', obtubiste: ' + str(intent) + ' Puntos')


if __name__ == '__main__':
    run()