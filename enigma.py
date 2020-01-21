route1 = 0
route2 = 0
route3 = 0

def rotor1(letter, startPoint, first, forward):
	global route1
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']]
	if startPoint is not None and first:
		route1 = connections[0].index(startPoint)
	if forward:
		route1 = route1 + 1
	index = connections[0].index(letter)
	index = (index - route1) % 26
	letter = connections[1][index]
	print(letter)
	return letter

def rotor2(letter, startPoint, first, forward):
	global route2
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']]
	if startPoint is not None and first:
		route2 = connections[0].index(startPoint)
	if forward:
		route2 = route2 + 1
	index = connections[0].index(letter)
	index = (index - route2) % 26
	letter = connections[1][index]
	print(letter)
	return letter

def rotor3(letter, startPoint, first, forward):
	global route3
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']]
	if startPoint is not None and first:
		route3 = connections[0].index(startPoint)
	if forward:
		route3 = route3 + 1
	index = connections[0].index(letter)
	index = (index - route3) % 26
	letter = connections[1][index]
	print(letter)
	return letter

def rotor4(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']]
	if startPoint is not None and first:
		route = connections[0].index(startPoint)
	route +=1
	index = connections[0].index(letter)
	index = (index - route) % 26
	letter = connections[1][index]
	print(letter)
	return letter

def rotor5(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter

def rotor6(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter

def rotor7(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter

def rotor8(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter

def rotorBeta(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q', 'M', 'D', 'R', 'T', 'A', 'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter			   
   
	
def rotorGamma(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L', 'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter 
	
def reflectorB(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V', 'Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W'],
				   ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter 

def reflectorC(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V', 'F', 'V', 'P', 'J', 'I', 'O', 'Y', 'R', 'Z', 'X', 'W', 'Q', 'U'],
				   ['F', 'V', 'P', 'J', 'I', 'O', 'Y', 'R', 'Z', 'X', 'W', 'Q', 'U', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print(letter)
	return letter 

def plugboardSetup():
	plugboard = [ [ 0 for i in range(10) ] for j in range(2) ] 
	options = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Ninth", "Tenth"]

	j=0
	while j<10:
		pb = input("{} pluboard connection: ".format(options[j])).upper()
		i=0
		plugboard[i][j] = pb[:1]
		i=1
		plugboard[i][j] = pb[1:]
		j+=1
	return plugboard

def rotorSetup():
	list = []
	setup = []
	options = ["1", "2", "3"]
	for i in range(0, 3):
		list.append(input("rotor {}: ".format(options[i])))
	for j in range(0, 3):
		if list[j] == '1':
			setup.append(rotor1)
		elif list[j] == '2':
			setup.append(rotor2)
		elif list[j] == '3':
			setup.append(rotor3)
		elif list[j] == '4':
			setup.append(rotor4)
		elif list[j] == '5':
			setup.append(rotor5)
		elif list[j] == '6':
			setup.append(rotor6)
		elif list[j] == '7':
			setup.append(rotor7)
		elif list[j] == '8':
			setup.append(rotor8)
		elif list[j] == "Beta":
			setup.append(rotorBeta)
		elif list[j] == "Gamma":
			setup.append(rotorGamma)
	startPoints = []
	for k in range(0, 3):
		startPoints.append(input("rotor {}, Start Point: ".format(setup)))
	#package = [setup, startPoints]
	return setup, startPoints
	
def reflectorSetup():
	reflector = input("reflector: ")
	if reflector == 'B':
		reflector = reflectorB
	elif reflector == 'C':
		reflector = reflectorC
	return reflector
	
def encryption(letter, setup, startPoints, reflector, plugboard, first):
	if letter in plugboard[0] or letter in plugboard[1]:
		index = plugboard[0].index(letter)
		letter = plugboard[1][index]
	print(letter)
	z = 0
	for rotor in setup:
		letter = rotor(letter, startPoints[z], first, True)
		z+=1
	letter = reflector(letter)
	for rotor in setup[::-1]:
		letter = rotor(letter, None, None, False)
	if letter in plugboard[0] or letter in plugboard[1]:
		index = plugboard[0].index(letter)
		letter = plugboard[1][index]
	print(letter)
	
def main():
	first = True
	plugboard = plugboardSetup()
	rotorSet = rotorSetup()
	setup = rotorSet[0]
	startPoints = rotorSet[1]
	reflector = reflectorSetup()
	while True:
		letter = input("Letter?")
		encryption(letter, setup, startPoints, reflector, plugboard, first)
		first = False
	return

main()
	

	

