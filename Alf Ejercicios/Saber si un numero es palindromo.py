#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra= input("Please write a word: ")

while ' ' in palabra:
    print("La palabra o puede contener espacios.")
    palabra= input("Please write another word: ")

palabra_al_revez= palabra

list_palabra= list(palabra)
palabra_al_revez= list(palabra_al_revez)
palabra_al_revez.reverse()

if list_palabra == palabra_al_revez:
    print('{} is a palindrome'.format(palabra))
else:
    print('{} is not a palindrome'.format(palabra))
