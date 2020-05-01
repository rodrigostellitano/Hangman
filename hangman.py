import random
import re
import os

class WordRepeatException(Exception):
    pass

class Rangman():

    def __init__(self):
        #screen = [' ','cabeça', 'cabeça e tronco', 'cabeça, tronco e braços', 'cabeça, tronco, braços e pernas', False]
        self.screen = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''', False]
        self.list_hidden = []
        #lista de erros
        self.list_wrong = []
        #lista de erros + acertos para não se repetir
        self.already_try = []

        self.pattern = '[a-zA-Z]'
        
        self.count_list_word = 0
        self.count_rangman = 0

    
    #Quando ganhar
    def winner(self):
        os.system('cls')
        for i in range(10):  
            print("YOU WIN!")
            print('Você ganhou a palavra era: ' + self.word)
        exit()

    #Quando perder
    def lost(self):
        os.system('cls')
        for i in range(10):
            print("YOU LOSE!")
        print('Você perdeu a palavra era: ' + self.word)
        exit()

    #Escolhe a Palavra
    def choose_word(self):
        # Puxou a palavra aleatória
        self.word = random.choice(open('hangman_db.txt').readlines())

        # Pq estou usando o [:-1] ? A palavra vinha com um /n no final e não sabia tirar
        self.list_word = list(self.word.upper())[:-1]

        # print(list_word)
        # print(self.word)

        # Tamanho da palavra
        len_word = len(self.list_word)

        # Cria a lista escondida de acordo com o tamanho da palavra
        for i in range(len_word):
            self.list_hidden.append('_')

        # print(self.list_hidden)
        # print(len_word)
        # print(word)

    #Verifica a tentativa
    def verify_try(self,word):
                
        
        self.count_list_word = 0
      
        #Lista de letras que já foram tentadas
        self.already_try.append(word)
        

        if word in self.list_word:
                 
            for i in self.list_word:
                
                if word == i:
                    self.list_hidden[self.count_list_word] = word
                    #serve para sinalizar que encontrou uma palavra
                self.count_list_word += 1
        else:
            self.count_rangman += 1
            self.list_wrong.append(word)
          
        print('Palavra', self.list_hidden)
     
    #Tela Principal do jogo
    def screen_rangaman(self):
        
        eastegg = 0
        
        self.choose_word()
        #print(self.word)

        while self.screen[self.count_rangman] != False:
            #os.system('cls')
            print(self.screen[self.count_rangman])           
            print('Letras Incorretas: ', self.list_wrong)

            if self.list_hidden == self.list_word:
                self.winner()

            # Verifica se só inseriu uma letra
            while True:
                print('Quantidade de Letras ', self.list_hidden)
                try:
                    print(self.list_word)
                    try_word = input('Digite uma letra: ').upper()
                   
                    #print(try_word)

                    #Verifica se é uma letra e não é numero ou caracter especial
                    if re.match(self.pattern, try_word) is None or len(try_word) > 1 :
                        raise ValueError
                    elif try_word in self.already_try:
                        raise WordRepeatException
                    else:
                        break
                
                except WordRepeatException:
                    print(self.screen[self.count_rangman]) 
                    print('Você ja tentou essa letra, digite outra!')
                    print('Letras Incorretas: ', self.list_wrong)
                    
                   
                except ValueError:
                    print(self.screen[self.count_rangman]) 
                    print('Só é possivel inserir UMA letra e não pode inserir numéros e caracteres especiais')
                    print('Letras Incorretas: ', self.list_wrong)


                    eastegg += 1
                    if eastegg > 5:
                        print("só pode ta de sacanagem, o programa acabou! vlw")
                        exit()
            self.verify_try(try_word)
                    

        self.lost()

# Main
Rangman1 = Rangman()

Rangman1.screen_rangaman()

