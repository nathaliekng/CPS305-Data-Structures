#Name: Nathalie Ng
#ID: 500921963
import random
import matplotlib.pyplot as plt

def generate(lenS, lenA, alphabet):
#generate random string by getting a random integer and matching the integer to a letter in the alphabet
    string = ""
    for i in range(lenS):
        a = random.randint(0,lenA-1)
        string = string + alphabet[a]
    return string

def calcScore(newstr, target):
#generate score for similarity of generated string and given string
    similar = 0
    for i in range(len(target)):
        if newstr[i] == target[i]:
            similar = similar + 1
    return similar/len(target)*100
    
    
def monkeyTypist():
    #creating the scatter plot
    x = []
    y = []

    plt.xlabel('Iteration')
    plt.ylabel('Score of best string')
    plt.title("Monkey Typist")

    target = list("methinks it is like a weasel") 
    lenS = len(target)
    alphabet = list("abcdefghijklmnopqrstuvwxyz ") 
    lenA = len(alphabet)
    epoch = 0
    bestStr = generate(lenS, lenA, alphabet)
    bestScore = calcScore(bestStr, target)
    print("String                       Score    Epoch")
    newScore = 0
    while bestScore < 100:
        if bestScore==100:
            break
        newStr = bestStr
        if newScore<=bestScore:
            #to check the first incorrect letter if the entire string is still incorrect
            for i in range(len(newStr)):
                if newStr[i] != target[i]:
                    #if the letters don't match, it will generate a new letter to replace the old letter
                    a = random.randint(0, lenA - 1)
                    newLetter = alphabet[a]
                    strList = list(newStr)
                    strList[i] = newLetter
                    strApp = ''.join(strList)
                    newStr = strApp
                    epoch = epoch + 1
                    break
            newScore = calcScore(newStr, target)
        if newScore > bestScore:
            bestScore = newScore
            bestStr = newStr
        if epoch%100==0:
            print("%s %f %d" % ("".join(bestStr), bestScore, epoch))
            #appending to list for graph values
            x.append(epoch)
            y.append(bestScore)

    #print and append the final score and epoch values to print at 100%, and plot at 100%
    print("%s %f %d" % ("".join(bestStr), bestScore, epoch))
    x.append(epoch)
    y.append(bestScore)
    plt.scatter(x,y, label = 'graph', color = 'k', marker = '*')
    plt.show()