cold =(1,213)
hot =(3,94)
funny=(90,100)
close = (0,5)
joes_distance = 7
joes_funniness = 97
sam = 0
San_Antonio = 100
Georgia = 99

def GetFuzzyValues(List,Label):
	"Prints the membership of every value between the values of a 2-tuple"
	for i in range(List[0],List[-1]+1):
		print(str(i) + ' is ' + str((float(i)-List[0]) / (List[-1]-List[0])) + ' ' + Label)

def Membership(x,List):
	"Returns the membership of a value in a list."
	top=(float(x)-List[0])
	bottom=(List[-1]-List[0])
	M= top/bottom
	return M

def Is(x,List):
	"Returns true if a value is in the value range of a list"
	if x >= List[0]:
		if x<= List[-1]:
			print(Membership(x,List))
			return True
	print(Membership(x,List))
	return False 

def Get(List,x,i=0):
	steps=0
	while x<=List[1]:
		print (x,Membership(x,List))
		x=x+i
		print('steps: {}'.format(steps))
		steps=steps+1

def document(f):
	print(f.__name__ +': '+ f.__doc__+'\n')

print(Is(7,cold))
print(Is(92,hot))
print(Is(joes_funniness,funny))
print(Is(joes_distance,close))
print(Is(joes_distance,cold))
print("")
print(Is(joes_funniness,hot))
print("")
Get(close,sam,.1)
print(Is(Georgia,hot))
print("")

document(Is)
document(Membership)
document(GetFuzzyValues)
