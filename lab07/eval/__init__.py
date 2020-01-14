def BinaryTree(r):
    return r 

def getRootVal(root):
    return root[0]

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def inorder(tree, exp):
    #if there are values existing in tree, then it will append a parenthesis around each left and right branch
    #in order to account for order of operation. 

    if tree:
        exp.append('(')
        inorder(getLeftChild(tree), exp)
        exp.append(getRootVal(tree))
        inorder(getRightChild(tree), exp)
        exp.append(')')
    #return list with an expression to be solved
    return exp

def evalTree(tree, env):
    value = ""
    left=tree[1]
    right=tree[2]
    expr = inorder(tree, [])
    for i in range(len(expr)):
        #if the value in expr[i] is alphanumeric, it will compare with each variable in the environment
        #if the value in expr[i] matches a value in the environment, it will be assigned to expr[i]
        if expr[i].isalnum():
            for j in range(len(env)):
                envx=env[j]
                if expr[i] == envx[0]:
                    expr[i] = envx[1]
    #convert the list expr into a string 
    exprStr = "".join(map(str, expr))

    #check if there are any variables that did not get replaced (did not match any value in envrionment)
    for a in range(len(exprStr)):
        if exprStr[a].isalpha():
            return None
    
    try:
        value=eval(exprStr)
    except ZeroDivisionError:
        return "Can not divide by zero"
    return value


