# # j = input("|")
# # a = 0

# # def jautajumi(j):
# #     f = open("jautajumi.txt", "r")
# #     a = int(input(f.read(97)) )
# #     print(a) 

# # jautajumi(j)

# # for i in range(10):
# #     jautajumi(j)


# # a = f.read(97)
# # print(a)
# # f.close()
# f = open("jautajumi.txt", "r")
# read = f.readlines()
# modif = []
# j = "|"


# for line in read:
#     if line[-1] == '\n' :
#         modif.append(line[: -1])
#     else:
#         modif.append(line)
        

# print(modif)


# a = 0

# for i in range ():
#     print(i)
#     break



# # def jautajumi(j):
# #     f = open("jautajumi.txt", "r")
# #     a = int(input(f.readlines()) )

# #     print(a) 

# # count = 0

# # for i in jautajumi(j):
# #     count = count + 1
# #     jautajumi(j)


 # Open the file for reading
        f = open("jautajumi.txt", "r")
            # Read the file contents
            contents = f.read()
            
            # Split the contents into individual questions
            questions = contents.split("\n\n")
            
            # Initialize an empty list to store the questions and answers
            atbildes = []
            
            # Loop through each question
            for question in questions:
                # Split the question into the question itself and the answer
                question, answer = question.split("\n")
                
                # Prompt the user for an answer
                user_answer = input(f"{question}\n")
                
                # Convert the user's answer to an integer
                try:
                    user_answer = int(user_answer)
                except ValueError:
                    print("Invalid answer. Please enter an integer.")
                    user_answer = input(f"{question}\n")
                
                # Add the question and answer to the list
                atbildes.append((question, user_answer))
            
            # Return the list of question and answer tuples
                return atbildes
    






