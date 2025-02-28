parola1 = input("Inserici la prima parola ")
parola2 = input("Inserici la seconda parola ")

# #parola al contrario
# for i in range(0,len(parola1), 1):
#     if parola1[i] == parola2[len(parola1)-1-i]:
#         continue
#     else:
#         print("Non è l'anagramma")
#         break

# print(parola1, "è l'anagramma di ", parola2)

lista_parola1 = [*parola1]
lista_parola2 = [*parola2]

if len(parola1) != len(parola2):
    print(parola1, "NON è l'anagramma di ", parola2)
else:
    for i in lista_parola1:
        if i in lista_parola2:
            lista_parola2.remove(i)
    if lista_parola2 == []:
        print(parola1, "è l'anagramma di ", parola2)

