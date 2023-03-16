def isOddOrEven(value):

    return ("짝수입니다." if value % 2 == 0 else "홀수입니다.");

input = int(input("정수를 입력하시오: "));

print(isOddOrEven(input));

