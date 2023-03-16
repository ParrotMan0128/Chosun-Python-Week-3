def isPass(value):

    return ("합격입니다." if value >= 60 else "불합격입니다.");

score = int(input("성적을 입력하시오: "));

print(isPass(score));