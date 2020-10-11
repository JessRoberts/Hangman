# Write your code here
import random


print("H A N G M A N")
game = input('Type "play" to play the game, "exit" to quit:')
print('\n')

while game == 'play':
    words = ('python', 'java', 'kotlin', 'javascript')
    strip = random.choice(words)
    turns = 8
    b = set()
    a = ''
    c = set()
    while turns != 0:
        def rep_mul(main_string):
            for elem in main_string:
                if elem in b:
                    main_string = main_string
                else:
                    main_string = main_string.replace(elem, "-")
            return main_string

        next_dash = rep_mul(strip)

        print(next_dash)

        a = input("Input a letter:")
        if a not in c:
            if a in strip:
                b.update(a)
                c.update(a)
                print('\n')
            elif len(a) != 1:
                print("You should input a single letter")
                if turns == 0:
                    break
                else:
                    print('\n')
            elif not a.islower():
                print("It is not an ASCII lowercase letter")
                if turns == 0:
                    break
                else:
                    print('\n')
            else:
                print("No such letter in the word")
                c.update(a)
                turns += -1
                if turns == 0:
                    break
                else:
                    print('\n')
            if b == set(strip):
                break
        else:
            print("You already typed this letter")
            print('\n')
    if b == set(strip):
        print(strip)
        print('You guessed the word!')
        print('You survived!\n')

    else:
        print('You lost!\n')

    game = input('Type "play" to play the game, "exit" to quit:')