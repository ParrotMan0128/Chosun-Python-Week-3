def compareTwoNum(x, y):

    max_value = (x if x > y else y);
    min_value = (y if x > y else x);

    returnValue = [max_value, min_value];

    return returnValue;

x = int(input("첫번 째 수를 입력: "));
y = int(input("두번 째 수를 입력: "));

print("큰 수: " + str(compareTwoNum(x, y)[0]));
print("작은 수 " + str(compareTwoNum(x, y)[1]));