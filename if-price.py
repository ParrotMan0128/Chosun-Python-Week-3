def isExpensive(value):

    if(value > 20000):

        return True;

    else:

        return False;

price = int(input("상품의 가격을 입력 해주세요.\n"));

if (isExpensive(price)):

    deliveryCost = 0;

else:

    deliveryCost = 3000;

print(isExpensive(price));
print("배송비는 " + str(deliveryCost) + "원 입니다.\n");