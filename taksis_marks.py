
pasazieru_skaits = int((input('Cik būs pasažieri? :'))) #jautā cik ir pasažieru skaits 
if pasazieru_skaits > 3 :  #pārbauda vai pasažieru skaits lielāks par 3 , ja ir, tad nepieņems pasažierus
    print('Nevar būt vairāk par 3 pasažieriem!') 
laiks = int((input('Cik ir pulkstenis? (ievadi veselu skaitli, piem 14.00 kā 14):')))
km = int((input('Cik km brauksi? :')))
if laiks > 21 and laiks < 6 : #vai ir nakts
    print('Cena par km :',km*0.77, 'eur') 
elif laiks < 21 and laiks > 6 : #vai ir diena
    print('Cena par km:',km*0.37, 'eur')
transporta_vieta = (input('Vai taksis ir stāvietā pie dzelzceļa? (j,n):')) #jautā vai taksists ir stāvietā pie dzelzsceļa
if transporta_vieta == 'j' :
    print('Nolīgšanas cena :',2.00,'eur')
elif transporta_vieta == 'n' :
    print('Izsaukuma cena :',2.50 , 'eur')
gaidisana = int((input('Cik ilgs būs taksista gaidīšanas laiks? (raksti minūtēs): ')))
transporta_noteikums = (input('Vai tev ir bārda? (j,n):'))
if transporta_noteikums == 'j': #programmas palildinājums
    print('Taksists tevi nepieņem')
diena = laiks<21 and laiks>6 #lai radītu čeka apakšā
nakts = laiks>21 and laiks<6 #lai radītu čeka apakšā
if diena:  #lai radītu čeka apakšā
    print('cena par km :',km*0.37)  #lai radītu čeka apakšā
elif nakts :   #lai radītu čeka apakšā
    print('cena par km :',km*0.77)   #lai radītu čeka apakšā
print('Gaidīšanas laiks : ',gaidisana*0.15, 'eur') #lai radītu čeka apakšā
if laiks > 21 and laiks < 6 and transporta_vieta == 'j' and transporta_noteikums == 'n': #ja atbilst dotajiem kritērijiem tad izprintē cenas
    print('Kopējā cena par braucienu : ', km*0.77+2.00+gaidisana*0.15)
elif laiks > 21 and laiks < 6 and transporta_vieta == 'n' and transporta_noteikums == 'n' : 
    print('Kopējā cena par braucienu : ', km*0.77+2.50+gaidisana*0.15) 
elif laiks < 21 and laiks > 6 and transporta_vieta == 'n' and transporta_noteikums == 'n':
    print('Kopējā cena par braucienu : ', km*0.37+2.50+gaidisana*0.15)
elif laiks < 21 and laiks > 6 and transporta_vieta == 'j' and transporta_noteikums == 'n' :
    print('Kopējā cena par braucienu : ', km*0.77+2.00+gaidisana*0.15) 
else:    #ja kautkas ir nepareizi ierakstīts
    print('Ievadi pareizi datus') 