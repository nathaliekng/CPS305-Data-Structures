#Nathalie Ng 500921963
#I showed up to the lab at the start time and was told everyone had to leave the building. I wasn't sure what was happening with the lab so I left as I was told.
from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["!"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    postFix = " ".join(postfixList)
    operandStack = Stack()
    tokenList = postFix.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token == "!":
            #if statement for factorial
            operand1 = int(operandStack.pop())
            result = operand1 * (operand1 - 1)
            for i in range(operand1 - 2):
                result = result * (i + 1)
            operandStack.push(result)
        else:
            operand2 = int(operandStack.pop())
            operand1 = int(operandStack.pop())
            if token =="*":
                result = operand1 * operand2
            elif token =="/":
                result = operand1/operand2
            elif token =="+":
                result = operand1+operand2
            else:
                result = operand1-operand2
            operandStack.push(result)
    return postFix, operandStack.pop()

x, y = infixToPostfix("( 2 + 2 ) ! + 8")
print(x, "\nEvaluates to:", y)
