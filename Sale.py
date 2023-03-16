def isMoreThan100(value):

    if (price >= 100):

        print("10층에서 사은품을 받아가세요.");
        return value * 0.85

    else:

        return value * 0.9

price = int(input("정가를 입력하시오: "));

print("할인된 가격: " + str(isMoreThan100(price)));