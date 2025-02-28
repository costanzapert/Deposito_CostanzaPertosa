età = int(input("Quale età hai? "))
if età < 18:
    print("Mi dispiace, non puoi vedere un film.")
else:
        print("Puoi vedere un film nella lista, scegli tra i seguenti:")
        film = ["A", "B", "C"] 
        scelta_film = input("Scegli tra A, B, C")
        print(scelta_film)
