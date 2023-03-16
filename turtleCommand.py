import turtle as t;
import random as r;

from time import sleep;

moveDistance = 20;
rotateAngle = 90;

t.shape("turtle");

t.width(3);

t.shapesize(1, 1);

print("Commands:\nf - move forward\nl - turn left and move forward\nr - turn right and move forward\nq - exit program");

commandList = ["f", "l", "r"];

while (True):

    randCom = r.sample(commandList, 1);
    command = ''.join(randCom);

    moveDistance = r.randint(10, 20);

    #command = str(input("Command: "));

    if (command == "f"):

        t.forward(moveDistance);

    elif (command == "l"):

        t.left(rotateAngle);
        t.forward(moveDistance);

    elif (command == "r"):

        t.right(rotateAngle);
        t.forward(moveDistance);

    elif (command == "q"):

        print("Good Bye!");
        t.bye();
        break;

    else:

        print("Wrong Command!");

    sleep(0.5);

