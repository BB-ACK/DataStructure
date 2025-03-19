def iFact(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i

    return result

def rFact(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * rFact(n-1)

print("iFact = %d" % iFact(5))
print("rFact = %d" % rFact(5))