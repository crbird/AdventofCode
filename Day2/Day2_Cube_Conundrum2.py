#https://adventofcode.com/2023/day/2

def checkTheStuff(s, val):
    for char in s:
        if not char.isnumeric():
            s = s.replace(char, '')
    if int(s) > int(val):
        return int(s)
    return int(val)

def colorSorter(cubes, bagContains):
    for m in cubes:
        #print(m)
        if "red" in m: #check red cubes
            bagContains[0] = checkTheStuff(m, bagContains[0])
        if "green" in m: #check green cubes
            bagContains[1] = checkTheStuff(m, bagContains[1])
        if "blue" in m: #check blue cubes
            bagContains[2] = checkTheStuff(m, bagContains[2])
    return bagContains

file1 = open('Day2_input.txt', 'r')
powerSum = 0
bagContains = [0, 0, 0] #red, green, blue

for line in file1:
    gameNumber = int(line.split(':')[0][4:]) #snag Game # out of line
    hands = line.split(':')[1].split(';')    #split input into each ; seperated handful of cubes
    for n in hands:             #loop for each set in a game
        cubes = n.split(',')    #each dice is its own string
        bagContains = colorSorter(cubes, bagContains)
    
    powerSum += bagContains[0] * bagContains[1] * bagContains[2]
    print(bagContains)
    print(str(powerSum))
    bagContains = [0, 0, 0]
    

print("Final sum = " + str(powerSum))
file1.close()