#https://adventofcode.com/2023/day/2

def checkTheStuff(s, val):
    for char in s:
        if not char.isnumeric():
            s = s.replace(char, '')
    if int(s) > val:
        return False
    return True

def colorSorter(cubes, bagContains):
    for m in cubes:
        #print(m)
        if "red" in m: #check red cubes
            if not checkTheStuff(m, bagContains[0]):
                return False
        if "green" in m: #check green cubes
            if not checkTheStuff(m, bagContains[1]):
                return False
        if "blue" in m: #check blue cubes
            if not checkTheStuff(m, bagContains[2]):
                return False
    return True

file1 = open('Day2_input.txt', 'r')
sum = 0
bagContains = [12, 13, 14] #red, green, blue

for line in file1:
    gameNumber = int(line.split(':')[0][4:]) #snag Game # out of line
    hands = line.split(':')[1].split(';')    #split input into each ; seperated handful of cubes
    for n in hands:             #loop for each set in a game
        cubes = n.split(',')    #each dice is its own string
        possible = colorSorter(cubes, bagContains)
        if not possible:
            break
    if possible:
        print("Game " + str(gameNumber) + ": True")
        sum += gameNumber
    else:
        print("Game " + str(gameNumber) + ": False")

print("Final sum = " + str(sum))
file1.close()