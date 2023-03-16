import math as m;

heignt = float(input("신장을 입력하시오(m): "));
weight = float(input("체중을 입력하시오(kg): "));

bmi = weight / m.pow(heignt, 2);

if (bmi >= 35):

    print("3단계 고도 비만");

elif (bmi >= 30):

    print("2단계 비만");

elif(bmi >= 25):

    print("1단계 비만");

elif (bmi >= 23):

    print("비만 전단계");

else:

    print("몰?루");