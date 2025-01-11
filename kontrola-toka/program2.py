broj = 4

if broj < 0:
    print("Broj je negativan")
else:
    if broj > 0:
        print("Broj je pozitivan")
    else:
       print("Broj je nula")
       
       
if broj < 0:
    print("Broj je negativan")
elif broj > 0:
    print("Broj je pozitivan")
else broj == 0:
    print("Broj je nula")
    
brzina = 200
ogranicenje = 80
if brzina > 0:
    print("Vozilo se krece")
    if brzina <= ogranicenje:
        print("Brzina je u redu")
    elif brzina > ogranicenja * 2:
        print("Nasilnicka voznja")
    elif brzina - ogranicenje > 10: