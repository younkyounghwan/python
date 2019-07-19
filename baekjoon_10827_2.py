from decimal import Decimal
a, b = map(Decimal, input().split())

answer = ("{:f}".format(pow(a, b)))
print(answer)