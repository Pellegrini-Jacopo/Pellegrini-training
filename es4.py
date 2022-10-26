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

#abbino i nomi di un grtuppo con quelli dell'altro
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#se metti past eviti errori da parte del sistem
for x in [0, 1, 2]:
  pass

#Gli array vengono utilizzati per memorizzare più valori in una singola variabile:
cars = ["Ford", "Volvo", "BMW"]

#Ottieni il valore del primo elemento dell'array:
x = cars[0]

#Restituisce il numero di elementi cars nell'array:
x = len(cars)

#Stampa ogni elemento carsnell'array:
for x in cars:
  print(x)

#Aggiungi un altro elemento cars all'array:
cars.append("Honda")

#Elimina il primo elemento carsdell'array:
cars.pop(0)

#