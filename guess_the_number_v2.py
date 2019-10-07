##Author:
##Description: My program guess the given number by another user.

N = int(raw_input("Enter number to be guessed between 10 and 100, inclusive:"))
i = True
j = 1
if N >= 10 and N <= 100:
    while(i):
        print "Enter guess",j,":"
        guess = int(raw_input())
        if guess == N:
            print N,"is correct."
            print "Ending game."
            break
        else:
            j = j+1
            continue
else:
    print N,"is not between 10 and 100"
