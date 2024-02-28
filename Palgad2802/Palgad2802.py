# #Rabota v Klasse
from Palgamoodul import *

# palgad=[1200,2500,750,395,1200,2500]
# inimesed=["A","B","C","D","E","D"]

# while True:
#     print("0-Andmete ekraanile\n1-Andmete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n4-Soorterimine\n")
#     vastus=int(input())
#     if vastus==0:
#         naita_andmed(inimesed,palgad)
#     elif vastus==1:
#         inimesed,palgad=andmete_lisamine(inimesed,palgad)
#     elif vastus==2:
#         inimesed.palgad=andmete_kustutamine(inimesed,palgad)
#     elif vastus==3:
#         rikkad_inimesed=kellel_on_suurim_palk(inimesed,palgad)
#         print(rikkad_inimesed)
#     elif vastus==4:
#         inimesed,palgad=soorterimine(inimesed,palgad)
        



usernames = ["user1", "user2"]  
passwords = ["password1", "password2"]

while True:
    print("\nValige toiming:")
    print("1. Reegistreerimine")
    print("2. Autoseerimine")
    print("3. Muuda parooli")
    print("4. Uuendada parooli")
    print("5. Välju")
    
    choice = input("Valige toiming: ")
    
    if choice == "1":
        username = input("Sisestage oma kasutajanimi: ")
        password = input("Sisestage oma parool: ")
        register(username, password, usernames, passwords)
        
    elif choice == "2":
        username = input("Sisestage oma kasutajanimi: ")
        password = input("Sisestage oma parool: ")
        authorize(username, password, usernames, passwords)
        
    elif choice == "3":
        username = input("Sisestage oma kasutajanimi: ")
        old_password = input("Sisesta vana parool: ")
        new_password = input("Sisestage uus parool: ")
        change_password(username, old_password, new_password, usernames, passwords)
        
    elif choice == "4":
        username = input("Sisestage oma kasutajanimi: ")
        new_password = input("Sisestage uus parool: ")
        reset_password(username, new_password, usernames, passwords)
        
    elif choice == "5":
        print("Programm lõpetatud.")
        break
        
    else:
        print("Vale valik. Proovi uuesti.")

