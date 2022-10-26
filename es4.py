#stampare ogni nome del gruppo e lo mette in colonna
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)

#mette in colonna tutte le lettere di una parola
for x in "banana":
print(x)

#con break si puo stoppare la stampa
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#con continue non stampi quello che ce con x ==
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#da 0 fino al numero tra parentesi non compreso
for x in range(6):
  print(x)

#da 2 a 30 non incluso incrementando di 3
for x in range(2, 30, 3):
  print(x)


