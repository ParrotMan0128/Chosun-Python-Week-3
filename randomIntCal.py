import random as r;

def isCorrect(a, b):

    if (a == b):

        return True;
    
    else:

        return False;

#PLUS
x = r.randint(1, 100);
y = r.randint(1, 100);

answer = int(input(f"{x} + {y} = "))

print(isCorrect(x+y, answer));

#MINUS
x = r.randint(1, 100);
y = r.randint(1, 100);

answer = int(input(f"{x} - {y} = "))

print(isCorrect(x-y, answer));

