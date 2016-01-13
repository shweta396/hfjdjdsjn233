''' ask user input
save input in list and tuple
if user enters 'H' stop entering
'''

l=[] #list declaration
val=0 #initialize value

while(val!='H'): #terminate condition
	val=raw_input('enter value:')
	l.append(val) #append values
l.remove('H') #dont want H in list so remove it
	
t=tuple(l) #list to tuple (function that convert from list to tuple because tuple cant append)

print t
print l