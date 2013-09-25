from random import randint
    # greet player
    # get player name
    # choose random number between 1 and 100
    # while True:
    #     get guess
    #     if guess is incorrect:
    #         give hint
    #     else:
    #         congratulate player

print "HEY! What's your name?"

name = raw_input("> ")

rand_number = randint(1, 100)

print "%s, please choose a number between 1 and 100." % name

wrong = True
count = 0

while wrong:
    try:
        guess = int(raw_input("> "))
        if 1 <= guess <= 100:
            count += 1
            if guess > rand_number:
                print "Too high. Please try again."
            elif guess < rand_number:
                print "Too low. Please try again."
            else:
                print "Congratulations, %s! You got it in %d tries!" % (name, count)
                wrong = False
        else:
            print "This integer is not between 1 and 100. Please try again."
    except ValueError:
        print "That is not an integer. Please try again."

