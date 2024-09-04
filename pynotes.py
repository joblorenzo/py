# VARIABLES ** convection SNAKE_CASE
  #VAR GLOBAL out a function || VAR LOCAL == DECLARED in FUNCTIONS
  #main X non modificabile ma richiamabile in DEF, reINIZIALIZZO dentro def con global x = 1
# == != > < >= <= += *= /=
global globale #questo comando prima di reiniziallizzara la reinizialliza globalmente
globale = "globale" #altrimenti basta un return o utilizzare quel valore subito
number = 5                      #var num
text = 'Hello World'            #var string
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
print(text)
print(text[6])                  #var string: print letter 6 == 7th
print(text[-1])                 #var string: print letter string -1
print(len(text))                #len == lunghezza variabile
print(type(text))               #type == return data TYPE
print(alphabet.find('z'))       #find == position in string
print(alphabet.find(text[0]))   
print(text.lower())             #lower == trasforma str in lowercase

index = alphabet.find(text[0].lower()) #applico lower a text position 0, ciclo find
print (index)
shifted = 3 #alphabet[index + number]  #0+5 h(pos0)+5 == m
print(shifted)

# FOR IF else 

text = 'Hello Zaira'
shift = 3
def caesar():           #FUNCTION

  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ''

  for char in text.lower():
    if char == ' ':
      encrypted_text += char
    else:
      index = alphabet.find(char)
      new_index = (index + shift) % len(alphabet)
      encrypted_text += alphabet[new_index]
  print('plain text:', text)
  print('encrypted text:', encrypted_text)

caesar() #call tu function



#FUNCTIONS