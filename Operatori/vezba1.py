temperatura = 1
grad = "Beograd"
opis = "Sneg"

print("Temperatura: ", int(temperatura), "C", "Grad: ", grad, "Opis: ", opis )

#Trenutna temperatura: 1 stepen
#Grad: "Beograd"
#Trenutno je: sneg

print("Trenutna temperatura: ", int(temperatura), "stepen", "\n", "Grad: ", grad, "\n", "Trenutno je: ", opis)

print("Trenutna temperatura:", temperatura, "stepen")
print(f"Trenutna temperatura: {temperatura} stepen\nGrad: {grad}\nTrenutno je: {opis}")


ispis = "Trenutna temperatura: " + str(temperatura)
print(ispis)

opis_prognoze = "Trenutno je: " + opis
print(opis_prognoze)

# unesite prvi broj, drugi broj, ispis rezultat
broj1 = 20 #input ("Unesi prvi broj: ")
broj2 = 50 #input ("Unesi drugi bro")
rezultat = int(broj1) + int(broj2) # + - * / aritmeticki operateri
#print("Rezultat je: ", str(broj1 + broj2))
ocekivano = 60
# == operator poredjenja - jednakosti
print(rezultat == ocekivano)
print(f"Rezultat je: {rezultat}")
print(10 / 2)

# deljenje bez ostatka
print(10 // 2)
print(9 // 2)

#stepenovanje, posle ** je stepen
print(3 ** 2)
print(3 ** 4)

#celobrojni ostatak od deljenja (modula)
print(10 % 3) # 3 * 3 + 1 # taj ostatak je rezulata
print(10 % 2) # 2 * 5 + 0
print(7 % 2) # 2 * 3 + 1

# r na kvadrat pi - povrsina kruga
poluprecnik = 5
pi = 3.14
povrsina = poluprecnik * poluprecnik * pi
povrsina = poluprecnik ** 2 * pi
print(povrsina)

# Testiramo
ocekivano = 78.5
dobijeno = povrsina

print(ocekivano == dobijeno)
print(- ocekivano)

auto_x = 0
parking_x = 40

#auto_x += parking_x  auto je odmah stigao
print(auto_x)
# auto se pomera za 10
auto_x +=10
print(auto_x)
auto_x +=10
print(auto_x)
auto_x +=10
print(auto_x)
auto_x +=10
print(auto_x)
 #proveriti da li je auto na poziciji parkinga i dobija se rezultat True
print("Stigao", auto_x == parking_x)

auto_x -= 5
print("Stigao", auto_x == parking_x)

auto_x *= 2
print(auto_x)

