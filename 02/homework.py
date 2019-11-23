user_input = input("V jakém patře bydlíš? ")
try:
    level = int(user_input)
    if level > 200:
        print("Jsi si jistý, že žiješ na zemi?")
    elif level > 50:
        print("To žiješ pěkně vysoko")
    elif level > 10:
        print("Nemotá si tě hlava?")
    elif level > 1:
        print("Máš pěkný rozhled")
    elif level == 0:
        print("Žiješ si pěkně při zemi")
    elif level > -2:
        print("To ti moc nezávidím")
    else:
        print("Jsi z rodu trpaslíků?")

except ValueError:
    print("Nerozumím, zadej číslo ")
