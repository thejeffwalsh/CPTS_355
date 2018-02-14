#Jeffrey Chandler Walsh
#Dynamic or Static scoping Postscript interpreter
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
        dictStack[len(dictStack) - 1][1][name] = value
    else:
        tupleDict = (0, {})
        tupleDict[1][name] = value
        dictPush(tupleDict)


def dictPop():
    return dictStack.pop()


def dictPush(hold):
    dictStack.append(hold)


def findStaticLink(index, token):
    if (token in dictStack[index][1]) or (index is 0):
        return index
    return findStaticLink(dictStack[index][0], token)

def lookupHelper(chain):
    if chain is 0:
        return [0]
    return [chain] + lookupHelper(dictStack[chain][0])

def lookup(name, scope):
    if scope is 'dynamic':
        if len(dictStack) is 0:
            return None
        for d in reversed(dictStack):
            if name in list(d[1].keys()):
                return d[1][name]
        return None

    else:
        if len(dictStack) is 0:
            return None
        elif name in dictStack[len(dictStack) - 1][1]:
            return dictStack[len(dictStack) - 1][1][name]
        else:
            staticChain = lookupHelper(dictStack[len(dictStack) - 1][0])
            for chain in staticChain:
                if name in list(dictStack[chain][1].keys()):
                    return dictStack[chain][1][name]
        return None




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
        if op1 is op2:
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
            if op1 is False:
                opPush(False)
            elif op2 is False:
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
            if op1 is False and op2 is True:
                opPush(True)
            elif op2 is False and op1 is True:
                opPush(True)
            elif op1 is False and op2 is False:
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
            if op1 is False:  # get rid of op2 isinstance and check if its boolean not integer
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
    if len(opStack) is 0:  # global opStack for each function
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


def end(): #only use for dynamic scoping
    if len(dictStack) > 0:  # according to slide, end operator pops the top dict from dict stack
        dictPop()  # and throws it away
    else:
        debug("Error")


def psDict(): #only use for dynamic scoping
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
        if c is '}':
            return rest
        elif c is '{':
            rest.append(groupMatching(it))
        #        elif c.isdigit():
        #            rest.append(int(c))
        #        elif c[0] is '-':
        #            rest.append(-abs(int(it)))
        else:
            rest.append(c)
    return False


def parse(s):
    rest = []
    it = iter(s)
    for c in it:
        if c is '}':
            return False
        elif c is '{':
            rest.append(groupMatching(it))
        elif c.isdigit():
            rest.append(int(c))
        elif c is '-':
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

ps = {'add': add, 'sub': sub, 'mul': mul, 'div': div, 'eq': eq, 'lt': lt, 'gt': gt, 'length': length,
      'get': get, 'getinterval': getinterval, 'and': psAnd, 'or': psOr, 'not': psNot, 'roll': roll,
      'dup': dup, 'exch': exch, 'copy': copy, 'pop': pop, 'clear': clear,
      'def': psDef, 'stack': stack, 'if': psif, 'ifelse': psifelse}
def interpretSPS(tokens, scope):

    for token in tokens:
        try:
            opPush(int(token))
        except:
            try:
                ps[token]()
            except:
                if token is "true":
                    opPush(True)
                elif token is "false":
                    opPush(False)
                elif token[0] is '/' or token[0] is '(':
                    opPush(str(token))

                else:
                    defn = lookup(str(token), scope)
                    staticChain = []
                    if defn is not None:
                        if type(defn) is type([]):
                            dictPush((findStaticLink(len(dictStack) - 1, token), {}))
                            interpretSPS(defn, scope)

                        else:
                            opPush(defn)
                    else:
                        opPush(token)
    dictPop()

def interpreter(s): #s is a string
    print("dynamic")
    interpretSPS(parse(tokenize(s)), "dynamic")
    clear()
    clearDict()
    print("static")
    interpretSPS(parse(tokenize(s)), "static")



###### this function is not in hw just to help me with it #################
def clearDict():  # clears stack
    if len(dictStack) is 0:  # global dictStack for each function
        debug("Error")
    else:
        while len(dictStack) > 0:
            dictPop()


########################################################################
##################################################################



############# Test functions/Cases ####################
if __name__ is '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    check = {True: passedMsg, False: failedMsg}  # Condenses True/False test into Dictionary

    input1 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
     /chic {
     /n 1 def
     /egg2 { n } def
     m n
     egg1
     egg2
     stack } def
    n
    chic"""

    print("Interprator:")
    clear()
    interpreter(input1)
    #clear()
    #interpreter(input2)
    #clear()
    #interpreter(input3)
    #clear()
    #interpreter(input4)
