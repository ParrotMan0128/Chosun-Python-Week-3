def isPlusOrMinus(value):

    return ("양수입니다." if value >= 0 else "음수입니다.");

input = int(input("임의의 정수를 입력하시오: "));

print(isPlusOrMinus(input));