import pandas as pd

def fileOut(what, intMorethan):
    f = open("originalSorted.txt",'w')
    for el in what:
        if(el[1]>intMorethan):
            f.writelines("%s\n" % el)
    f.close()

def tagFrequency (dataList, list):
    for string in dataList:
        words = str(string).split("; ")
        for word in words:
         flag = 1
         for tag in enumerate(list):
             if (tag[1][0] == word):
                 flag = 1
                 tags[tag[0]][1] += 1
                 break
             elif (tag[1][0] != word):
                 flag = -1
         if (flag == -1):
             tags.append([word, 1])


data = pd.read_csv("Data.csv")
#tags = [[";",0]]
#tagFrequency(data["Теги"], tags)
#tags.sort(key = lambda num: num[1], reverse = True)
#print(tags)
#fileOut(tags)

objectives = []
aim = ['э','л','е','к','т']
cutData = data.drop(data[data["Бренд"] != "oral-b"].index)
print(cutData)
for string in cutData["Товар"]:
    words = str(string).split(" ")
    drobWord = list(words)
    matches = 0
    print(drobWord)
    for word in enumerate(drobWord):
        print(word[0], word[1], word[0][0], word[1][0])
        if (word[1][0:4:] == aim[0:4:]):
            print(word[1][0:4:], aim[0:4:])
            objectives.append(cutData.drop(columns="IDПользователя").iloc[word[0]]["IDПользователя"])
print(objectives)
