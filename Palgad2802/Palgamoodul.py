import random



# def andmete_lisamine(i:list,p:list)->any:
#     """Karina,Mark,Erik,Doris,Eva,Vadim,Nikita"""
#     while True:
#         try:
#             n=int(input("Mitu inimest"))
#             if n>0: break
#         except:
#             print("Viga. Proovi uuesti!")
#     for j in range(n):
#         nimi=input("Nimi: ")
#         palk=int(input("Palk: "))
#         i.ippend(nimi)
#         p.append(palk)
#     return i,p

# def naita_andmed(i:list,p:list):
#     """
#     """
#     for j in range(len(i)):
#         print(i[j],"-",p[j])
        
# def andmete_kustutamine(i:list,p:list)->any:
#     """
#     """
#     nimi=input("Keda kustutada ära?(nimi) ")
#     if nimi not in i:
#         print(f"{nimi} puudub")
#     else:
#         for j in range(len(i)):
#             if nimi==i[j]:
#                 p.pop(i.index(nimi))
#                 i.remove(nimi)
#     return i,p

# def kellel_on_suurim_palk(i:list,p:list)->list:
#     """
#     """
#     nimed=[]
#     max_palk=max(p)
#     ind=p.index(max_palk)
#     for palk in p:
#         if max_palk==palk:
#             nimi=i[p.index(palk,ind)]
#             nimed.append(nimi)
#             ind+=1
#     return nimed

# def soorterimine(i:list,p:list)->any:
#     """
#     """
#     for n in range(0,len(i)):
#         for m in range(n,len(i)):
#             if p[n]>p[m]:
#                 p[n],p[m]=p[m],p[n]
#                 i[n],i[m]=i[m],i[n]
#     return i,p
 


def generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    password = ''.join([random.choice(ls) for x in range(12)])
    
    return password

print("Automaatne loodud parool:", generate_password())


def register(username, password, usernames, passwords):
    if username in usernames:
        print("Sama nimega kasutaja on juba olemas.")
    else:
        usernames.append(username)
        passwords.append(password)
        print("Kasutaja registreerimine õnnestus.")


def authorize(username, password, usernames, passwords):
    if username in usernames:
        index = usernames.index(username)
        if passwords[index] == password:
            print("Autoriseerimine õnnestus.")
        else:
            print("vale salasõna.")
    else:
        print("Selle nimega kasutajat pole.")


def change_password(username, old_password, new_password, usernames, passwords):
    if username in usernames:
        index = usernames.index(username)
        if passwords[index] == old_password:
            passwords[index] = new_password
            print("Parooli muutmine õnnestus.")
        else:
            print("Kehtetu vana parool.")
    else:
        print("Selle nimega kasutajat pole.")


def reset_password(username, new_password, usernames, passwords):
    if username in usernames:
        index = usernames.index(username)
        passwords[index] = new_password
        print("Parooli lähtestamine õnnestus.")
    else:
        print("Selle nimega kasutajat pole.")

