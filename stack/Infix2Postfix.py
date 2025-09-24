from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix # 후위표기식 -> 계산

def precedence(op):
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    elif (op == '*' or op == '/'): return 2
    else: return -1

def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push(term)
        
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
            
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())
    return output



# Test
if __name__ == "__main__":
    print('중위 표기식 후위 표기 변환\n')

    infix1 = ['8','/','2','-','3','+','(','3','*','2',')']
    infix2 = ['1','/','2','*','4','*','(','1','/','4',')']
    infix3 = ['(','6','3',')','*','2','+','20','/','(','10','+','5',')']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)
    postfix3 = Infix2Postfix(infix3)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)
    result3 = evalPostfix(postfix3)

    print(' 중위표기:', infix1)
    print(' 후위표기', postfix1)
    print(' 게산결과:', result1, end ='\n\n')

    print(' 중위표기:', infix2)
    print(' 후위표기', postfix2)
    print(' 게산결과:', result2, end ='\n\n')

    print(' 중위표기:', infix3)
    print(' 후위표기', postfix3)
    print(' 게산결과:', result3)