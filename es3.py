#utilizzo condizioni matematiche come uguale,maggiore
a = 33
b = 200
if b > a:
  print("b is greater than a")

#
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#La parola chiave elif è un modo Python per dire "se le condizioni precedenti non erano vere, prova questa condizione".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#La parola chiave else cattura tutto ciò che non è catturato dalle condizioni precedenti.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Se hai solo un'istruzione da eseguire, puoi metterla sulla stessa riga dell'istruzione if.
if a > b: print("a is greater than b")

#Se hai una sola istruzione da eseguire puoi metterla tutta sulla stessa riga:
a = 2
b = 330
print("A") if a > b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#La parola chiave or è un operatore logico e viene utilizzata per combinare istruzioni condizionali:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Puoi avere istruzioni if ​​all'interno di istruzioni if, questo è chiamato istruzioni if ​​annidate.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass