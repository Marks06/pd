stop = '0'
print('-----------------------')
Lietotajvards = 'Marks'
Parole = '12345'
if Parole <= str(5): #Pārbauda vai parole ir lielāka par 5
    print('--------------------------\n')
    print('Pieslēgties\n')
    lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu : ')
    paroles = input('Lūdzu, ievadiet savu paroli : ')
    while stop == '0':
        if lietotajs == Lietotajvards and paroles == Parole:
            print('Pieslēgšanās veiksmīga')
            break
        elif lietotajs != Lietotajvards:
            for i in range (1,6):
                print (i,'meiģinājuma skaits') 
                print('Lietotājvārds nav pareizs! ievadi vēlreiz:')
                lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu : ')
                if i == 5:
                    print('Atļāuts mēģināt pieslēgties 5 reizes!')
                    exit()
                elif lietotajs != Lietotajvards: 
                    continue
                else:
                    print('Pareizs lietotājvārds!')
                    break
        elif paroles != Parole:
            for i in range (1,6):
                print (i,'meiģinājuma skaits') 
                print('parole nav pareiza! ievadiet vēlreiz :')
                paroles = input('Lūdzu, ievadiet savu paroli : ')
                if i == 5:
                    print('Atļāuts mēģināt pieslēgties 5 reizes!')
                    exit()
                elif paroles != Parole:
                    print('Nepariezi!')
                    continue
                else:
                    print('Pareiza parole')
                    break
else: 
    print('Parole pārsniedz 5 burtus!') #ja parole pārsniedz 5 burtus programma beidzas
    exit()
pirmais_skaitlis = int(input('Ievadi vienu veselu skaitli: '))
otrais_skaitlis = int(input('Ievadi otru veselu skaitli: '))
if pirmais_skaitlis < 0 or otrais_skaitlis < 0:   #ja kāds no skaitļiem ir negatīvs raksta ka nevar būt negatīvs
    print('Nevar būt negatīvi skaiļi')
elif pirmais_skaitlis >  otrais_skaitlis : 
    print('0')
else:
    for i in range (pirmais_skaitlis, otrais_skaitlis):
        if i <= otrais_skaitlis:
            print('Veselu secīgi piaugošu skailtļu no ',pirmais_skaitlis,' līdz ',otrais_skaitlis, 'summa ir: ',str(pirmais_skaitlis) + str((pirmais_skaitlis+1)))
        elif i > otrais_skaitlis:
            exit()
if str(lietotajs) or str(Lietotajvards) or str(paroles) or str(Parole) or str(pirmais_skaitlis) or str(otrais_skaitlis) == 'stop':
    exit()
