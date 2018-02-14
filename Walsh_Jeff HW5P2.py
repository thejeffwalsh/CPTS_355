import re

opStack = []
dictStack = []

debug_level = 0


def debug(*s):
    if debug_level > 0:
        print(s)


def opPop():
    return opStack.pop()
    pass

def opPush(value):
    opStack.append(value)
    pass


def define(name, value):
    if len(dictStack) > 0:
        dictStack[len(dictStack) - 1][name] = value
    else:
        newDict = {}
        newDict[name] = value
        dictStack.append(newDict)


def dictPop():
    return dictStack.pop()


def dictPush(hold):
    dictStack.append(hold)


def lookup(name):
    if len(dictStack) == 0:
        return False
    for d in reversed(dictStack):
        if name in list(d.keys()):
            return d[name]
    return False


####################### Arithmetic operators #######################################

def add():  # add two top stack vals
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1 + op2)
    else:
        debug("Error")


def sub():  # subtract two top stack vals
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op2 - op1)
    else:
        debug("Error")


def mul():  # multiply two top stack values
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1 * op2)
        opPush(op1 * op2)
    else:
        debug("Error")


def div():  # divides two top stack values
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op2 / op1)
    else:
        debug("Error")


def eq():  # see if two numbers are equal
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        debug("Error")


def lt():  # less than operator
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op1 > op2:
            opPush(True)
        else:
            opPush(False)
    else:
        debug("Error")


def gt():  # greater than operator
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op2 < op1:
            opPush(True)
        else:
            opPush(False)
    else:
        debug("Error")


###############################################################################

####################### String operators ########################################

def length():  # gets length of string
    if len(opStack) > 0:
        value = opPop()
        lengths = len(value[1:-1])
        opPush(lengths)


def get():  # according to slides, get() gets the string and index value from stack
    if len(opStack) > 0:  # then pushes the ASCII value of the character at the position of the index value
        op1 = opPop()  # onto the stack
        op2 = opPop()
        op3 = ord(op2[op1])
        opPush(op3)
    else:
        debug("Error")


def getinterval():  # gets string, index, and count from the stack
    if len(opStack) > 0:  # returns the substring of the string starting from index to count
        count = opPop()  # pushes the substring onto the stack
        index = opPop()
        inputStrings = opPop()
        intervals = inputStrings[index:count]
        opPush(intervals)
    else:
        debug("Error")


#############################################################################

#################### Boolean operators ######################################

def psAnd():  # and operator
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, bool) and (isinstance(op2, bool)):
            if op1 == False:
                opPush(False)
            elif op2 == False:
                opPush(False)
            else:
                opPush(True)
        else:
            debug("Error")


def psOr():  # or operator
    if len(opStack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op2, bool) and (isinstance(op2, bool)):
            if op1 == False and op2 == True:
                opPush(True)
            elif op2 == False and op1 == True:
                opPush(True)
            elif op1 == False and op2 == False:
                opPush(False)
            else:
                opPush(True)
        else:
            debug("Error")


def psNot():  # !False = True, it does that
    global opStack
    if len(opStack) > 0:
        op1 = opPop()
        if isinstance(op1, bool):
            if op1 == False:  # get rid of op2 isinstance and check if its boolean not integer
                opPush(True)
            else:
                opPush(False)
        else:
            debug("Error")


###############################################################################

#################### stack manipulation and print operators ###################
def dup():  # duplicates top stack value
    op1 = opPop()
    opPush(op1)
    opPush(op1)


def roll():
    if (len(opStack) > 1):
        rollAmt = opPop()  # Total Rolls
        numVals = opPop()  # Number of values to be rolled
        originalLength = len(opStack)
        copyOpStack = opStack
        if rollAmt > 0 or numVals < 0:
            tempOpStack = copyOpStack[originalLength - numVals:]  # Stores Values to Rotate in Temp
            tempOpStack = tempOpStack[-rollAmt:] + tempOpStack[:-rollAmt]  # Rotates only values within m range
            copyOpStack = copyOpStack[:originalLength - numVals]  # Removes last m values from the list
            copyList = copyOpStack + tempOpStack  # Appends rotated Temp list to copyList
            clear()
            for x in copyList:
                opPush(x)  # Updates w/ rolled list
        else:
            debug("Error")


def exch():  # switches top two values with each other
    if len(opStack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        debug("Error: opPop - Operand stack is empty")


def pop():  # pop function which is the same as the opPop() function
    if len(opStack) > 0:
        x = opStack[len(opStack) - 1]
        opStack.pop(len(opStack) - 1)
        return x
    else:
        debug("Error: opPop - Operand stack is empty")


def copy(n):  # copies first n items and pushes onto stack
    opList = []
    for i in range(n):
        opList.insert(i, opPop())
    opList.reverse()
    for a in opList:
        opPush(a)
    for b in opList:
        opPush(b)


def clear():  # clears stack
    if len(opStack) == 0:  # global opStack for each function
        debug("Error")
    else:
        while len(opStack) > 0:
            opPop()


def stack():
    if len(opStack) > 0:
        for p in reversed(opStack):
            print(p)
    else:
        debug("Error: opPop - Operand stack is empty")


######################## Dictionary operators #############################################

def begin():  # according to slide, begin operator takes a dictionary from the top of the
    if len(opStack) > 0:  # operand stack and pushes it on the dictionary stack
        op1 = opPop()
        dictPush(op1)
    else:
        debug("Error")


def end():
    if len(dictStack) > 0:  # according to slide, end operator pops the top dict from dict stack
        dictPop()  # and throws it away
    else:
        debug("Error")


def psDict():
    if len(dictStack) >= 0:
        opPop()
        opPush({})
    else:
        debug("Error")


def psDef():
    value = opPop()
    name = opPop()
    name = name[1:]
    define(name, value)
    pass


def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


def groupMatching(tokens):
    rest = []
    negs = []
    it = iter(tokens)
    for c in it:
        if c == '}':
            return rest
        elif c == '{':
            rest.append(groupMatching(it))
        #        elif c.isdigit():
        #            rest.append(int(c))
        #        elif c[0] == '-':
        #            rest.append(-abs(int(it)))
        else:
            rest.append(c)
    return False


def parse(s):
    rest = []
    it = iter(s)
    for c in it:
        if c == '}':
            return False
        elif c == '{':
            rest.append(groupMatching(it))
        elif c.isdigit():
            rest.append(int(c))
        elif c == '-':
            rest.append(groupMatching(it))
        else:
            rest.append(c)
    return rest



    ######################## Conditionals #####################################################


# ------------------------
# if and ifelse operators
def psif():
    code = opPop()
    bool = opPop()
    if bool:
        interpretSPS(code)
    pass


def psifelse():
    else_code = opPop()
    if_code = opPop()
    bool_cond = opPop()
    if bool_cond:
        interpretSPS(if_code)
    else:
        interpretSPS(else_code)
    pass


def interpretSPS(tokens):
    for token in tokens:
        try:
            opPush(int(token))
        except:
            if token == "add":
                add()
            elif token == "sub":
                sub()
            elif token == "mul":
                mul()
            elif token == "div":
                div()
            elif token == "eq":
                eq()
            elif token == "lt":
                lt()
            elif token == "gt":
                gt()
            elif token == "length":
                length()
            elif token == "get":
                get()
            elif token == "getinterval":
                getinterval()
            elif token == "and":
                psAnd()
            elif token == "or":
                psOr()
            elif token == "not":
                psNot()
            elif token == "if":
                psif()
            elif token == "ifelse":
                psifelse()
            elif token == "dup":
                dup()
            elif token == "exch":
                exch()
            elif token == "pop":
                pop()
            elif token == "roll":
                roll()
            elif token == "copy":
                copy()
            elif token == "clear":
                clear()
            elif token == "stack":
                stack()
            elif token == "dict":
                psDict()
            elif token == "begin":
                begin()
            elif token == "end":
                end()
            elif token == "def":
                psDef()
            elif token == "true":
                opPush(True)
            elif token == "false":
                opPush(False)
            elif token[0] == '/':
                opPush(str(token))
            elif token[0] == '(':
                opPush(str(token))
            else:
                defn = lookup(str(token))
                if defn != False:
                    if type(defn) == type([]):
                        interpretSPS(defn)
                    else:
                        opPush(defn)
                else:
                    opPush(token)


def interpreter(s):  # s is a string
    interpretSPS(parse(tokenize(s)))


###### this function is not in hw just to help me with it #################
def clearDict():  # clears stack
    if len(dictStack) == 0:  # global dictStack for each function
        debug("Error")
    else:
        while len(dictStack) > 0:
            dictPop()


########################################################################
##################################################################



############# Test functions/Cases ####################
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    check = {True: passedMsg, False: failedMsg}  # Condenses True/False test into Dictionary

    input1 = """
    /square {
     dup mul
    } def
    (square)
    4 square
    dup 16 eq true and
    {(pass)} {(fail)} ifelse stack"""

    input2 = """
    (facto) dup length /n exch def
    /fact {
     0 dict begin
     /n exch def
     n 2 lt
     { 1}
     {n 1 sub fact n mul }
     ifelse
     end
    } def
    n fact stack
    """

    input3 = """
    /lt6 { 6 lt } def
    1 2 3 4 5 6 4 -3 roll
    dup dup lt6 exch 3 gt and {mul mul} if
    stack
    clear
    """

    input4 = """
    (CptS355_HW5) 4 3 getinterval
    (355) eq
    {(You_are_in_CptS355)} if
     stack
     """

    print(tokenize(input2))
    print(parse(tokenize(input2)))
    print("Interprator:")
    clear()
    interpreter(input1)
    clear()
    interpreter(input2)
    clear()
    interpreter(input3)
    clear()
    interpreter(input4)
