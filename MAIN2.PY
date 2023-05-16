import os
from colorama import Fore

def tests():

    minejumi = []
    pareizatb = 0
    qnum = 1

    print(Fore.RED + "TESTS: Vai vari atbildēt pareizi uz 10 āķīgiem jautājumiem?")

    for key in jautajumi:
        print(Fore.BLUE + "-------------------------")
        print(Fore.LIGHTBLACK_EX + key)
        for i in opcijas[qnum-1]:
            print(i)
        atbilde = input("Ievadi (A, B, C, vai D): ")
        atbilde = atbilde.upper()
        minejumi.append(atbilde)

        pareizatb += check_atb(jautajumi.get(key), atbilde)
        qnum = qnum + 1

    disp_rezult(pareizatb, minejumi)

# -------------------------
def check_atb(answer, atbilde):

    if answer == atbilde:
        print(Fore.GREEN + "Pareizi!")
        return 1
    else:
        print(Fore.RED + "Nepareizi!")
        return 0

# -------------------------
def disp_rezult(pareizatb, minejumi):
    print(Fore.BLUE + "-------------------------")
    print(Fore.GREEN + "REZULTĀTS")
    print(Fore.BLUE + "-------------------------")

    print(Fore.LIGHTBLACK_EX + "Atbildes: ", end="")
    for i in jautajumi:
        print(jautajumi.get(i), end=" ")
    print()

    # print("Minējumi: ", end="")
    # for i in minejumi:
    #     print(i, end=" ")
    # print()



    with open("atbildes.txt", "w") as f:
        for atbilde in minejumi:
            f.write(atbilde + " ")
    
    with open("atbildes.txt", "r") as f:
        tavi = f.read()
        print("Jūsu atbildes: ", tavi)

    score = int((pareizatb/len(jautajumi)) * 100)
    print("Jūsu rezultāts ir: " + str(score) + "%")

    if score == 100:
        print("Apsveicu ar perfektu rezultātu!")
    
    
    os.remove("atbildes.txt")
    

# -------------------------


def velreiz():

    response = input(Fore.RED + "Vai vēlies mēģināt vēlreiz? (Jā vai Nē): ")
    response = response.upper()

    if response == "JĀ":
        return True
    else:
        return False
# -------------------------


jautajumi = {"1. Cik zirņi var ieiet vienā glāzē?: ": "D", 
"2. Kas ir smagāks - 1 kilograms kartupeļu vai 1 kilograms betona?: ": "A", 
"3. Kāda paliek maize, kad to iemērt Melnajā jūrā?: ": "C", 
"4. Kādā krāsā bija Napoleona baltais zirgs?: ": "C", 
"5. Virtuvē uz galda stāv 3 āboli. Tu paņem 2 ābolus. Cik āboli tev tagad ir?: ": "B", 
"6. Jānis stāv aiz Kārļa, bet Kārlis stāv aiz Jāņa. Kā tas ir iespējams?: ": "D", 
"7. Ko saka izdegusi spuldzīte?: ": "A", 
"8. Kas ugunī nedeg un ūdenī neslīkst?: ": "C", 
"9. Ar kādu slimību uz zemes neslimo?: ": "C", 
"10. Ar kādu ātrumu jāskrien sunim, lai nedzirdētu pie viņa astes piesietās pannas radīto troksni?: ": "D"}

opcijas = [["A Pāris desmiti",  "B Pāris simti",  "C Viss atkarīgs no glāzes izmēra",  "D Necik"],
["A Abi vienādi",  "B Kilograms kartupeļu",  "C Kilograms betona",  "D Kilograms biezpiena"],
["A Tā tiek nolādēta",  "B Tā paliek melna",  "C Tā paliek slapja",  "D Tā saraujas"],
["A Brūnā",  "B Pelēkā",  "C Baltā",  "D Melnā"],
["A 1",  "B 2",  "C 3",  "D 0"],
["A Kārlis sēž Jānim klēpī",  "B Jānis sēž Kārlim klēpī",  "C Viņi stāv ar sejām viens pret otru",  "D Viņi stāv ar mugurām viens pret otru"],
["A Neko",  "B Kurš izslēdza gaismu?",  "C Eu!?",  "D Tā nebija mana vaina..."],
["A Ods",  "B Ķieģelis",  "C Ledus",  "D Koks"],
["A Ar gribu",  "B Ar iesnām",  "C Ar jūras slimību",  "D Ar bronhītu"],
["A Ar 5 km/h",  "B Ar 10km/h",  "C Ar 50 km/h",  "D Ar 0 km/h"],]



tests()
 
while velreiz():
    tests()

print(Fore.GREEN + "Paldies par piedalīšanos!")
