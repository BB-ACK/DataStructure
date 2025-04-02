from ArrayStack import ArrayStack

def evalPostfix(expr): # ["8", "2", "/" ...]
    S = ArrayStack()

    for term in expr:
        if term in "+-*/": # 연산자이거나
            val2 = S.pop()
            val1 = S.pop()

            if term == "+": S.push(val1 + val2)
            elif term == "-": S.push(val1 - val2)
            elif term == "*": S.push(val1 * val2)
            else: S.push(val1 / val2)

        else: # 숫자이거나
            S.push(float(term))

    return S.pop()

if __name__ == "__main__":
    str = "8 2 / 3 - 3 2 * +"
    expr = str.split()

    print(str, " --> ", evalPostfix(expr))