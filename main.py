import random

numbers=list(range(10))
l_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
u_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
all_lists=[]
Users=[]

login=input("Felhasználónév:")
if(login in Users):



    print("Ez egy jelszó generáló program.\n")
    while True:
        try:
            usege=input("\nMihhez kell a jelszó (weboldal/applikáció/stb.):")

            if(usege==""):
                break
            h=int(input("\tHány karakterből álljon a jelszó:"))
            option=input("\tLegyen benne minden (igen/nem):")

            if(option=="igen"):
                all_lists.append(numbers)
                all_lists.append(l_letters)
                all_lists.append(u_letters)
            elif(option=="nem"):
                num=input("\tLegyenek benne számok (igen/nem):")
                l=input("\tLegyenek benne kisbetűk (igen/nem):")
                u=input("\tLegyenek benne nagybetűk (igen/nem):")


                if(num=="igen"):
                    all_lists.append(numbers)
                elif(num!="nem"):
                    raise ValueError
                if(l=="igen"):
                    all_lists.append(l_letters)
                elif (l != "nem"):
                    raise ValueError
                if(u=="igen"):
                    all_lists.append(u_letters)
                elif(u!="nem"):
                    raise ValueError
                if(len(all_lists)==0):
                    raise IndexError
            else:
                raise ValueError


            if(h==0 or h>100):
                print("A jelszó hossza nem megfelelő. Próbálkozzon újra!")
            else:
                while True:
                    passw = ""
                    for i in range(h):
                        list=random.choice(all_lists)
                        character=random.choice(list)
                        passw=passw+str(character)
                    print("\t",passw)
                    re=input("\tRegenerálás:")
                    if(re==""):
                        break

                with open("jelszavak.txt","a",encoding="UTF-8") as f:
                    f.write(str("\n")+usege+str(":\n\t")+passw)

        except Exception:
            raise ValueError("Nem megfelelő értéket adott meg.")
            raise IndexError("Válasszon ki legalább egy listát.")



else:
    print("Nem megfelelő felhasználó nevet adott meg.")