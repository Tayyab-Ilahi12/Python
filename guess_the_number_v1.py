##Author:
##Description: My program guess the given number by another user.

N = int(raw_input("Enter number to be guessed between 10 and 100, inclusive:"))
if N >= 10 and N <= 100:
    guess1 = int(raw_input("Enter your first guess:"))
    if guess1 == N:
        print N,"is correct."
    elif guess1 != N:
        print "Not correct."
        guess2 = int(raw_input("Enter your Second guess:"))
        if guess2 == N:
            print N,"is correct."
            print "Ending game."
        else:
            print "You did not guess the number with in 2 attempts."
            print "The target number was",N
            print "You guess were",guess1,"and",guess2
else:
    print N,"is not between 10 and 100"
