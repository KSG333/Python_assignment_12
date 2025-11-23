# 과제 32
num1 = {2, 5, 7, 8, 9}
num2 = {0, 1, 3, 7, 9}
print(num1|num2)
print(num1&num2)


# 과제33
num1 = {2, 5, 7, 8, 9}
num2 = {0, 1, 3, 7, 9}
print(num1 - num2)
print(num1 ^ num2)


# 과제34
num1 = {2, 5, 7, 8, 9}
num1 |= {100}
print(num1)


# 과제35
a = {100, 200, 300, 400, 500}
a &= {400, 500, 600, 700}       # intersection_update
print(a)
a -= {400, 500, 600, 700}       # difference_update
print(a)
a ^= {400,500,600,700}          # symmetric_difference_update
print(a)


# 과제 36
a = {100, 200, 300, 400, 500}
result = (a <= {100, 200, 300, 400, 500})      # 부분집합
result1 = (a >= {100, 200, 300, 400, 500})     # 상위집합
if result == True and result1 == True:
    print("동시")
elif result == True:
    print("부분")
elif result1 == True:
    print("상위")


# 과제37
num1 = {2, 5, 7, 8, 9}
num1.add(1000)
num1.discard(1000)
print(num1)


# 과제38
multiples = {x for x in range(1,101) if x % 3 == 0 and x % 5 == 0}
print(multiples)