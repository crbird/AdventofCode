#https://adventofcode.com/2023/day/1
file1 = open('Day1_input.txt', 'r')
sum = 0

for line in file1:
    a = 12
    b = 12
    occurance = 0
    number = 0
    #print(line.strip())
    for char in line.strip():
        if char.isnumeric():
            if occurance == 0:
                    a = char
                    occurance += 1
            else:
                b = char
    
    #remove the 0 cause input file doesnt ever use items
    if int(b) == 12:
        number = int(str(a) + str(a))
    else:
        number = int(str(a) + str(b))
        
    #add that line's number to sum
    sum += number
    #print(number)
    
print("Final sum = " + str(sum))
file1.close()