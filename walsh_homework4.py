from collections import defaultdict
def make_ttable(s1,s2): 
	myDict = {}
	for key, value in zip(s1, s2):
		myDict[key] = value
	return myDict
		
	
def trans(ttable,s):
	#write your code here
	tempStr = ""
	for x in s:
		if x in ttable:
			tempStr += ttable[x]
		else: 
			tempStr += x
	return tempStr
	
	
def testtrans():
	ttable = make_ttable('abc', 'xyz')
	revttable = make_ttable('xyz', 'abc')
	if trans(ttable, "Now I know my abc's") != "Now I know my xyz's":
		return False
	if trans(revttable, trans(ttable,"Now I know my abc's")) != "Now I know mb abc's":
		return False
	if trans(ttable,'') != '':
		return False
	if trans(make_ttable('',''), "abc") != 'abc':
		return False
	return True
	
def gemsbyColor(gColors):
	tempDict = {}
	for i, j in gColors.items():
		tempDict[j] = tempDict.get(j,[])
	tempDict = dict(tempDict)
	return tempDict
	
def dict2List (d):
	L =sorted(d.items())
	for i in rnge(len(L)):
		L[i] = (L[i][0], sorted(L[i][1]))
	return L
			
def testGems():
	gColors3={'jadeite':'purple', 'amethyst':'purple', 'howlite':'white',
    'danburite':'white', 'goshenite':'white', 'calcite':'orange',
    'sodalite':'white', 'enstatite':'green', 'andesine':'orange', 'zircon':'orange'}

	gColors2={'pearl':'pink', 'kunzite':'pink', 'agate':'blue',
	'diamond':'blue', 'iolite':'blue', 'spiney':'red',
	'azurite':'blue', 'apatite':'green', 'coral':'red', 'carnelian':'red'}

	gColors={'scapolite':'yellow', 'heliodor':'yellow', 'topaz':'blue',
	'zircon':'blue', 'moonstone':'blue', 'garnet':'red',
	'aquamarine':'blue', 'emerald':'green', 'ruby':'red', 'beryl':'red'}

	print(dict2List({'yellow': ['heliodor', 'scapolite'], 'blue': ['aquamarine','moonstone','topaz', 'zircon'], 'red': ['beryl', 'garnet', 'ruby'], 'green': ['emerald']}))
	
	if dict2List(gemsbyColor(gColors)) != dict2List({'yellow': ['heliodor', 'scapolite'], 'blue': ['aquamarine','moonstone','topaz', 'zircon'], 'red': ['beryl', 'garnet', 'ruby'], 'green': ['emerald']}):
		return False
	
	if dict2List(gemsbyColor(gColors2))!= dict2List({'pink': ['kunzite', 'pearl'], 'blue': ['agate', 'azurite','diamond', 'iolite'], 'red': ['carnelian', 'coral', 'spiney'], 'green': ['apatite']}):
		return False
		
	if dict2List(gemsbyColor(gColors3))!= dict2List({'purple': ['amethyst', 'jadeite'], 'white': ['danburite', 'goshenite', 'howlite', 'sodalite'], 'orange': ['andesine', 'calcite', 'zircon'], 'green': ['enstatite']}):
		return False
		
	return True

	
def histo1(S):
	Str = S.replace(" ", "")
	Str = Str.upper()
	myDict = defaultdict(int)
	myList = []
	for x in Str:
		myDict[x] += 1
	for x, y in myDict.items():
		myList.append((x,y))
	listFixed = sorted(set(myList), key=lambda x: x[0])
	listFixed = sorted(listFixed, key=lambda x: x[1])
	return listFixed

def histo2(S):
	Str = S.replace(" ", "")
	Str = Str.upper()
	myList = []
	i = 0
	for x in Str:
		myList.insert(i, Str.count(Str[i]))
		i += 1
	listFixed = list(zip(Str, myList))
	listFixed = sorted(set(listFixed), key=lambda x: x[0])
	listFixed = sorted(listFixed, key=lambda x: x[1])
	return listFixed	
	
def testhisto():
	if histo1('Cpts355 --- Assign1') != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('G', 1), ('I', 1), ('N', 1), ('P', 1), ('T', 1), ('5', 2), ('-', 3), ('S', 3)]:
		return False
		
	if histo2('Cpts355 --- Assign1') != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('G', 1), ('I', 1), ('N', 1), ('P', 1), ('T', 1), ('5', 2), ('-', 3), ('S', 3)]:
		return False
		
	if histo1('Testing Function 123 234') != [('1', 1), ('4', 1), ('C', 1), ('E', 1), ('F', 1), ('G', 1), ('O', 1), ('S', 1), ('U', 1), ('2', 2), ('3', 2), ('I', 2), ('N', 3), ('T', 3)]:
		return False
		
	if histo2('Testing Function 123 234') != [('1', 1), ('4', 1), ('C', 1), ('E', 1), ('F', 1), ('G', 1), ('O', 1), ('S', 1), ('U', 1), ('2', 2), ('3', 2), ('I', 2), ('N', 3), ('T', 3)]:
		return False
		
	if histo1('This is a string') != [('A', 1), ('G', 1), ('H', 1), ('N', 1), ('R', 1), ('T', 2), ('I', 3), ('S', 3)]:
		return False
		
	if histo2('This is a string') != [('A', 1), ('G', 1), ('H', 1), ('N', 1), ('R', 1), ('T', 2), ('I', 3), ('S', 3)]:
		return False
		
	return True
	
def execute(funDict, fun, args):
	for k, v in funDict.items():
		if k == fun:
			a = v(*args)
	return a
	
	
def testExecute():
	funDict = {"add": lambda x,y: (x+y), "concat3": lambda a,b,c: (a+","+b+","+c),"mod2": lambda n: (n % 2)}
  
	if execute(funDict, "concat3", ["one","two","three"]) != 'one,two,three':
		return False
  
	if execute(funDict, "mod2", [40]) != 0:
		return False

	if execute(funDict, "add", [1,7]) != 8:
		return False

	return True
	
if __name__ == '__main__':
	passedMsg = "%s passed"
	failedMsg = "%s failed"
	if testtrans():
		print( passedMsg % 'testtrans' )
	else:
		print( failedMsg % 'testtrans' )
		pass
	if testGems():
		print( passedMsg % 'testGems' )
	else:
		print( failedMsg % 'testGems' )
		pass
	if testhisto():
		print( passedMsg % 'testhisto' )
	else:
		print( failedMsg % 'testhisto' )
		pass
	if testExecute():
		print( passedMsg % 'testExecute' )
	else:
		print(failedMsg% 'testExecute' )
