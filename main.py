print("TESTS: Vai vari atbildēt pareizi uz 10 āķīgiem jautājumiem?") #vēlāk uzlikt treknāku tekstu, nomainīt krāsu moš aķīgs sarkanu

jautajumi = ("1. Cik zirņi var ieiet vienā glāzē?: ", 
"2. Kas ir smagāks - 1 kilograms kartupeļu vai 1 kilograms betona?: ", 
"3. Kāda paliek maize, kad to iemērt Melnajā jūrā?: ", 
"4. Kādā krāsā bija Napoleona baltais zirgs?: ", 
"5. Virtuvē uz galda stāv 3 āboli. Tu paņem 2 ābolus. Cik āboli tev tagad ir?: ", 
"6. Jānis stāv aiz Kārļa, bet Kārlis stāv aiz Jāņa. Kā tas ir iespējams?: ", 
"7. Ko saka izdegusi spuldzīte?: ", 
"8. Kas ugunī nedeg un ūdenī neslīkst?: ", 
"9. Ar kādu slimību uz zemes neslimo?: ", 
"10. Ar kādu ātrumu jāskrien sunim, lai nedzirdētu pie viņa astes piesietās pannas radīto troksni?: ")

opcijas = (("A Pāris desmiti",  "B Pāris simti",  "C Viss atkarīgs no glāzes izmēra",  "D Necik"),
("A Abi vienādi",  "B Kilograms kartupeļu",  "C Kilograms betona",  "D Kilograms biezpiena"),
("A Tā tiek nolādēta",  "B Tā paliek melna",  "C Tā paliek slapja",  "D Tā saraujas"),
("A Brūnā",  "B Pelēkā",  "C Baltā",  "D Melnā"),
("A 1",  "B 2",  "C 3",  "D 0"),
("A Kārlis sēž Jānim klēpī",  "B Jānis sēž Kārlim klēpī",  "C Viņi stāv ar sejām viens pret otru",  "D Viņi stāv ar mugurām viens pret otru"),
("A Neko",  "B Kurš izslēdza gaismu?",  "C Eu!?",  "D Tā nebija mana vaina..."),
("A Ods",  "B Ķieģelis",  "C Ledus",  "D Koks"),
("A Ar gribu",  "B Ar iesnām",  "C Ar jūras slimību",  "D Ar bronhītu"),
("A Ar 5 km/h",  "B Ar 10km/h",  "C Ar 50 km/h",  "D Ar 0 km/h"),)

atbildes = ()
minejumi = []

punkti = 0

jautajumi_num = 0