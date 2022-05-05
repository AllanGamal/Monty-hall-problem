count_goat = 0
count_car = 0
doors = ['goat', 'goat', 'goat']

# get a random number between 0 and 1
def random_number():
    import random
    return random.randint(0, 2)

doors[random_number()] = 'car'


# loop 1000 times
for i in range(1000000):
    count = 0
    doors = ['goat', 'goat', 'car']
    
    answer = random_number()
    doors[answer] = 'car' # = 2
    reply = random_number() # = 1

    repans = [reply, answer] # = [1, 2]

    for door in doors:
        if count == reply or count == answer:
            count += 1
            continue   
        else:
            ropen = count # count = 0
            break
    for door in range(len(doors)):
        if door == ropen or door == reply:
            continue
        else:
            reply = door
            break
    if reply == answer:
        count_car += 1
    else:
        count_goat += 1
        
    
print(count_car/(count_goat+count_car))
print(count_goat)
