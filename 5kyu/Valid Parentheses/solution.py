def valid_parentheses(string):
    neededRightPar = 0
    for x in string:
        if x == "(":
            neededRightPar+=1
        elif x == ")":
            neededRightPar-=1
        if neededRightPar < 0:
            return False
    return True if neededRightPar == 0 else False