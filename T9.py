

class Node:
    def __init__(self):
        self.children = dict()
        self.words = set()
    
class T9Dictionary:
    
    def __init__(self):
        self.root = Node()
    
    def wordToDigits(self, word):     
        digits_in_word  = ''
        for character in word:
            if (character >= 'a' and character <= 'c'):
                digits_in_word = digits_in_word + '2'
            elif (character >= 'd' and character <= 'f'):
                digits_in_word = digits_in_word + '3'
            elif (character >= 'g' and character <= 'i'):
                digits_in_word = digits_in_word + '4'
            elif (character >= 'j' and character <= 'l'):
                digits_in_word = digits_in_word + '5'
            elif (character >= 'm' and character <= 'o'):
                digits_in_word = digits_in_word + '6'
            elif (character >= 'p' and character <= 's'):
                digits_in_word = digits_in_word + '7'
            elif (character >= 't' and character <= 'v'):
                digits_in_word = digits_in_word + '8'
            elif (character >= 'w' and character <= 'z'):
                digits_in_word = digits_in_word + '9'
    	
        return digits_in_word
    
    def prepareDictionary(self, filename):
        with open(filename) as file:
            for word in file:
                self.insertWord(word)
                
    def insertWord(self, word):
        word = word.lower()
        word = word.rstrip()
        word_in_digits = self.wordToDigits(word)
        word_in_digits_length = len(word_in_digits)
        
        current_node = self.root
        word_exists = True       
        for i in range(word_in_digits_length):
            current_digit = int(word_in_digits[i])

            # Sprawdzamy czy w slowniku dzieci aktualnego wezla znajduje sie dana cyfra (klucz)
            if current_digit in current_node.children and word_exists:
                
                # Znalezlismy dany klucz wsrod dzieci, dlatego mozemy przejsc do przeszukiwania dzieci dla kolejnej cyfry (klucza)
                current_node = current_node.children[current_digit]
                
                # Jesli cyfra, ktora aktualnie sprawdzalismy jest ostatnia dla danego slowa
                # to sprawdzamy czy dodawane slowo (word) znajduje sie juz w zbiorze slow
                if i == word_in_digits_length - 1 and word not in current_node.words:
                    current_node.words.add(word)
        
                continue
                
            # Jesli co najmniej raz nie udalo sie znalezc dziecka z danym kluczem, to ta czesc bedzie sie wykonywala do konca

            word_exists = False
            current_node.children[current_digit] = Node()
            if i == word_in_digits_length - 1:
                current_node.children[current_digit].words.add(word)

            
            current_node = current_node.children[current_digit]      
            
        # ------------- End of loop ---------------
        
    def showStartingWith(self, word_in_digits):
        word_in_digits_length = len(word_in_digits)
        
        current_node = self.root
        for i in range(word_in_digits_length):
            current_digit = int(word_in_digits[i])
            
            # Jesli w mapie dzieci nie ma dziecka o danej cyfrze(kluczu), to z pewnoscia nie uzyskamy podpowiedzi
            if current_digit not in current_node.children:
                print('Brak podpowiedzi')
                return
            
            current_node = current_node.children[current_digit]
                
        def showWords(current_node):
           for word in current_node.words:
               print(word + '\t')
               
           for key in current_node.children.keys():
               showWords(current_node.children[key])
                
        showWords(current_node)
            
        
        
    
    

x = T9Dictionary()
#print(x.wordToDigits("absence"))
#x.prepareDictionary('words10k.txt')
x.prepareDictionary('words10k.txt')
#x.showStartingWith('2')

print(x.root.children[2].words)

########################### TK INTER ########################