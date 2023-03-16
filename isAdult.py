def isAdult(value):

    return ("minor" if value < 21 else "adult");

age = int(input("나이를 입력: "));

print(isAdult(age));