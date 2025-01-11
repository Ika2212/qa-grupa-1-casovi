#srpski, engleski, nemacki
#sr, en, de
#Zdravo, Hello, Haloo

odabran_jezik_odabran_jezik_test_vrednost = "sr"
odabran_jezik = odabran_jezik_test_vrednost
prevod = " " #dobijen
ocekivan_prevod = "Zdravo"
if odabran_jezik == "sr":
    prevod = "Zdravo"
if odabran_jezik == "eng":
    prevod = "Hello"
if odabran_jezik == "de":
    prevod = "Hallo"
else:
    print(f"Test nije prosao, proverite prevod za: {odabran_jezik}")
    
    


input ("Odaberite jezik(srp, de, eng): ")
if odabran_jezik == "sr":
    print("Zdravo")
    
elif odabran_jezik == "en": 
    print("Hello")
    
elif odabran_jezik == "de":
    print("Hallo")
    
else:
    print("Prevod nije podrzan")
    
    
 
 

