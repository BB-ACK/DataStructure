import FindMinMax
from SumRange import sumRange # Sumrange.sumRange가 아니라 바로 함수 사용가능
import random

A = []
for _ in range(10):
    A.append(random.randint(1, 1000))

print("(min, max) : ", FindMinMax.findMinMax(A))
print("sum = ", sumRange(1, 100, 7))