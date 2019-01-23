

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
        word_in_digits = self.wordToDigits(word)
        word_length = len(word)
        
        currentNodeChildren = self.root.children
        
        word_exists = True
        
        for i in range(word_length):
            current_digit = str(word_in_digits[i])
        
            # Sprawdzamy czy w slowniku dzieci aktualnego wezla znajduje sie dana cyfra (klucz)
            if current_digit in currentNodeChildren and word_exists:
                
                # Znalezlismy dany klucz wsrod dzieci, dlatego mozemy przejsc do przeszukiwania dzieci dla kolejnej cyfry (klucza)
                currentNodeChildren =  currentNodeChildren[current_digit]
                
                # Jesli cyfra, ktora aktualnie sprawdzalismy jest ostatnia dla danego slowa
                # to sprawdzamy czy dodawane slowo (word) znajduje sie w zbiorze slow
                if i == word_length - 1 and word not in currentNodeChildren[current_digit].words:
                    currentNodeChildren[current_digit].words.add(word)
                    continue
                
             
            word_exists = False
            tempNode = Node()
            if(i == word_length - 1):
                tempNode.words.add(word)
            currentNodeChildren[current_digit] = tempNode
            currentNodeChildren = currentNodeChildren[current_digit]
            
            
            
            # ------------- End of loop ---------------
        
        
        
    
    

x = T9Dictionary()
#print(x.wordToDigits("pores"))
x.prepareDictionary('words10k.txt')


"""
class Trie {
protected:
	std::string wordToDigits(std::string word);
	Node head;
public:
	bool prepareDictionary(std::string path);
	void insert(std::string word);
	void showStartingWith(std::string digits);
};F

"""

"""
std::string Trie::wordToDigits(std::string word) {
	std::stringstream ss;
	char ch;
	for (unsigned i = 0; i < word.length(); i++) {
		ch = word[i];
		if (ch >= 'a' && ch <= 'c')
			ss << 2;
		else if (ch >= 'd' && ch <= 'f')
			ss << 3;
		else if (ch >= 'g' && ch <= 'i')
			ss << 4;
		else if (ch >= 'j' && ch <= 'l')
			ss << 5;
		else if (ch >= 'm' && ch <= 'o')
			ss << 6;
		else if (ch >= 'p' && ch <= 's')
			ss << 7;
		else if (ch >= 't' && ch <= 'v')
			ss << 8;
		else if (ch >= 'w' && ch <= 'z')
			ss << 9;
	}
	return ss.str();
}
    """