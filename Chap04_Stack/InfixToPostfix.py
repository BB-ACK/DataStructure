from ArrayStack import ArrayStack

# 중위 표기 수식에서 연산자 우선순위 확인을 위한 함수
def order(op): 
    if(op == "(" or op == ")"): return 0
    elif(op == "+" or op == "-"): return 1
    else: return 2

def infixToPostfix(expr):
    S = ArrayStack()
    postfix = []

    for term in expr:
        if term in "(":
            S.push(term)
    
        elif term in ")":
            while not S.isEmpty():
                op = S.pop()
                if op == "(": break
                else:
                    postfix.append(op)
                
        elif term in "+-*/":
            while not S.isEmpty():
                op = S.peek()
                if(order(term) <= order(op)):
                    postfix.append(S.pop())
                else: break
            S.push(term)
        
        else: # 숫자인 경우
            postfix.append(term)

    while not S.isEmpty(): # 다 돌고나서 남은 연산자들 처리    
        postfix.append(S.pop())
    
    return postfix

if __name__ == "__main__":
    infix = input("Input Infix Expr... ")
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)