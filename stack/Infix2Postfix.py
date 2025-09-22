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