#https://adventofcode.com/2023/day/1#part2

def isNumberWord(string):
  match string:
    case "zero":
        return 0
    case "one":
        return 1
    case "two":
        return 2
    case "three":
        return 3
    case "four":
        return 4
    case "five":
        return 5
    case "six":
        return 6
    case "seven":
        return 7
    case "eight":
        return 8
    case "nine":
        return 9
    case _:
        #print("not a word")
        return 12


def forwardIter(s):
    i = 0 #string index
    
    #there is some weird shit going on with the slice notation end number
    #I'm just rolling with it
    
    for char in s.strip():
        #print("i = " + str(i) + ", char = " + char)
        if s[i].isnumeric():
            #print(s[i])
            return int(s[i])
        if i >= 2: #check for 3 character numbers (one, two, six)
            n = isNumberWord(s[i-2:i+1])
            if n == 1 or n == 2 or n == 6:
                #print("word: " + str(n))
                return n
        if i >= 3: #check for 4 character numbers (four, five, nine, zero)
            n = isNumberWord(s[i-3:i+1])
            if n == 4 or n == 5 or n == 9 or n == 0:
                #print("word: " + str(n))
                return n
        if i >= 4: #check for 5 character numbers (three, seven, eight)
            n = isNumberWord(s[i-4:i+1])
            if n == 3 or n == 7 or n == 8:
                #print("word: " + str(n))
                return n
        
        #increment string index
        i += 1
    return 0
  
def backwardsIter(s):
    length = len(s.strip()) - 1
    i = length #string index
    #print("length: " + str(length) + s[length])
    
    #there is some weird shit going on with the slice notation end number
    #I'm just rolling with it
    
    for char in s.strip():
        #print("i = " + str(i) + ", char = " + str(s[i]))
        if s[i].isnumeric():
            #print(s[i])
            return int(s[i])
        if i >= 2: #check for 3 character numbers (one, two, six)
            n = isNumberWord(s[i-2:i+1])
            if n == 1 or n == 2 or n == 6:
                #print("word: " + str(n))
                return n
        if i >= 3: #check for 4 character numbers (four, five, nine, zero)
            n = isNumberWord(s[i-3:i+1])
            if n == 4 or n == 5 or n == 9 or n == 0:
                #print("word: " + str(n))
                return n
        if i >= 4: #check for 5 character numbers (three, seven, eight)
            n = isNumberWord(s[i-4:i+1])
            if n == 3 or n == 7 or n == 8:
                #print("word: " + str(n))
                return n
        
        #increment string index
        i -= 1
    return 0  

#beggining or something
file1 = open('Day1_input.txt', 'r')
sum = 0

for line in file1:
    a = forwardIter(line)
    b = backwardsIter(line)
    
    #remove the 0 cause input file doesnt ever use items
    if int(b) == 0:
        number = int(str(a) + str(a))
    else:
        number = int(str(a) + str(b))
    
    #print(number)
    sum += number

print("Final sum = " + str(sum))
file1.close()