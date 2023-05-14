def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = jautajumi = {"1. Cik zirņi var ieiet vienā glāzē?: ": "D", 
"2. Kas ir smagāks - 1 kilograms kartupeļu vai 1 kilograms betona?: ": "A", 
"3. Kāda paliek maize, kad to iemērt Melnajā jūrā?: ": "C", 
"4. Kādā krāsā bija Napoleona baltais zirgs?: ": "C", 
"5. Virtuvē uz galda stāv 3 āboli. Tu paņem 2 ābolus. Cik āboli tev tagad ir?: ": "B", 
"6. Jānis stāv aiz Kārļa, bet Kārlis stāv aiz Jāņa. Kā tas ir iespējams?: ": "D", 
"7. Ko saka izdegusi spuldzīte?: ": "A", 
"8. Kas ugunī nedeg un ūdenī neslīkst?: ": "C", 
"9. Ar kādu slimību uz zemes neslimo?: ": "C", 
"10. Ar kādu ātrumu jāskrien sunim, lai nedzirdētu pie viņa astes piesietās pannas radīto troksni?: ": "D"}

options = [["A Pāris desmiti",  "B Pāris simti",  "C Viss atkarīgs no glāzes izmēra",  "D Necik"],
["A Abi vienādi",  "B Kilograms kartupeļu",  "C Kilograms betona",  "D Kilograms biezpiena"],
["A Tā tiek nolādēta",  "B Tā paliek melna",  "C Tā paliek slapja",  "D Tā saraujas"],
["A Brūnā",  "B Pelēkā",  "C Baltā",  "D Melnā"],
["A 1",  "B 2",  "C 3",  "D 0"],
["A Kārlis sēž Jānim klēpī",  "B Jānis sēž Kārlim klēpī",  "C Viņi stāv ar sejām viens pret otru",  "D Viņi stāv ar mugurām viens pret otru"],
["A Neko",  "B Kurš izslēdza gaismu?",  "C Eu!?",  "D Tā nebija mana vaina..."],
["A Ods",  "B Ķieģelis",  "C Ledus",  "D Koks"],
["A Ar gribu",  "B Ar iesnām",  "C Ar jūras slimību",  "D Ar bronhītu"],
["A Ar 5 km/h",  "B Ar 10km/h",  "C Ar 50 km/h",  "D Ar 0 km/h"],]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
