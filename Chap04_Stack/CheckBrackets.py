# 괄호 검사 알고리즘
from ArrayStack import ArrayStack

def checkBrakets(str):
    S = ArrayStack()

    for ch in str:
        # 여는 괄호는 대입
        if ch == "[" or ch == "{" or ch == "(":
            S.push(ch)
        # 닫는 괄호에서 분석
        elif ch == "]" or ch == "}" or ch == ")":
            if S.isEmpty():
                return False # Error 2
            else:
                open = S.pop() # 여는 괄호
                if (ch == "]" and open != "[") or \
                (ch == "}" and open != "{") or \
                (ch == ")" and open != "("):
                    return False # Error 3
    return S.isEmpty() # Error 1

if __name__ == "__main__":
    s1 = "{ [ ( ) ] }"
    s2 = "( ( ) ( )"
    s3 = "[ ( ] )"

    print(s1, "---->", checkBrakets(s1))
    print(s2, "---->", checkBrakets(s2))
    print(s3, "---->", checkBrakets(s3))

