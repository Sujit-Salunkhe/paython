games=9
scores=[10,5,20,20,4,5,2,25,1]
max=min=scores[0]
maxscore=0
minscores=0
for i in range(len(scores)):
    if (max < scores[i]):
        max=scores[i]
        maxscore +=1
    elif (min > scores[i]):
        minscores +=1
        min=scores[i]
print(maxscore,minscores)


x=9
print(x)