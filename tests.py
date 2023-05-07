# j = input("|")
# a = 0

# def jautajumi(j):
#     f = open("jautajumi.txt", "r")
#     a = int(input(f.read(97)) )
#     print(a) 

# jautajumi(j)

# for i in range(10):
#     jautajumi(j)


# a = f.read(97)
# print(a)
# f.close()
f = open("jautajumi.txt", "r")
read = f.readlines()
modif = []
j = "|"


for line in read:
    if line[-1] == '\n' :
        modif.append(line[: -1])
    else:
        modif.append(line)
        

print(modif)


a = 0

for i in range ():
    print(i)
    break



# def jautajumi(j):
#     f = open("jautajumi.txt", "r")
#     a = int(input(f.readlines()) )

#     print(a) 

# count = 0

# for i in jautajumi(j):
#     count = count + 1
#     jautajumi(j)





