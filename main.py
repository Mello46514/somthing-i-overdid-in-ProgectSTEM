

keepdic = [
    int(input("Enter a number: ")),
    int(input("Enter a number: ")),
    int(input("Enter a number: "))
]

dic = [
    keepdic[0],
    keepdic[1],
    keepdic[2]
]

for i in range(0,3):
    if dic[i] == min(keepdic):
        dic[i] = 0
        print(dic[i])
    if dic[i] == max(keepdic):
        dic[i] = 0
        print(dic[i])

print(str(min(keepdic)) + " " + str(max(dic)) + " " + str(max(keepdic)))


#its a godamn sorting algorythm for three characters, it wanted me to find just the smallest...
