route1 = 0
route2 = 0
route3 = 0
route4 = 0
route5 = 0
route6 = 0
route7 = 0
route8 = 0
routeBeta = 0
routeGamma = 0
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
	print("After rotor 1: " + letter)
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
	print("After rotor 2: " + letter)
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
	print("After rotor 3: " + letter)
	return letter
def rotor4(letter, startPoint, first, forward):
	global route4
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']]
	if startPoint is not None and first:
		route4 = connections[0].index(startPoint)
	if forward:
		route4 = route4 + 1
	index = connections[0].index(letter)
	index = (index - route4) % 26
	letter = connections[1][index]
	print("After rotor 4: " + letter)
	return letter
def rotor5(letter, startPoint, first, forward):
	global route5
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']]
	if startPoint is not None and first:
		route5 = connections[0].index(startPoint)
	if forward:
		route5 = route5 + 1
	index = connections[0].index(letter)
	index = (index - route5) % 26
	letter = connections[1][index]
	print("After rotor 5: " + letter)
	return letter
def rotor6(letter, startPoint, first, forward):
	global route6
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']]
	if startPoint is not None and first:
		route6 = connections[0].index(startPoint)
	if forward:
		route6 = route6 + 1
	index = connections[0].index(letter)
	index = (index - route6) % 26
	letter = connections[1][index]
	print("After rotor 6: " + letter)
	return letter
def rotor7(letter, startPoint, first, forward):
	global route7
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']]
	if startPoint is not None and first:
		route7 = connections[0].index(startPoint)
	if forward:
		route7 = route7 + 1
	index = connections[0].index(letter)
	index = (index - route7) % 26
	letter = connections[1][index]
	print("After rotor 7: " + letter)
	return letter
def rotor8(letter, startPoint, first, forward):
	global route8
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']]
	if startPoint is not None and first:
		route8 = connections[0].index(startPoint)
	if forward:
		route8 = route8 + 1
	index = connections[0].index(letter)
	index = (index - route8) % 26
	letter = connections[1][index]
	print("After rotor 8: " + letter)
	return letter
def rotorBeta(letter, startPoint, first, forward):
	global routeBeta
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q', 'M', 'D', 'R', 'T', 'A', 'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S']]
	if startPoint is not None and first:
		routeBeta = connections[0].index(startPoint)
	if forward:
		routeBeta = routeBeta + 1
	index = connections[0].index(letter)
	index = (index - routeBeta) % 26
	letter = connections[1][index]
	print("After rotor beta: " + letter)
	return letter			   
   
	
def rotorGamma(letter, startPoint, first, forward):
	global routeGamma
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
				   ['F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L', 'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D']]
	if startPoint is not None and first:
		routeGamma = connections[0].index(startPoint)
	if forward:
		routeGamma = routeGamma + 1
	index = connections[0].index(letter)
	index = (index - routeGamma) % 26
	letter = connections[1][index]
	print("After rotor gamma: " + letter)
	return letter 
	
def reflectorB(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V', 'Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W'],
				   ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print("After reflector B: " + letter)
	return letter 
def reflectorC(letter):
	connections = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V', 'F', 'V', 'P', 'J', 'I', 'O', 'Y', 'R', 'Z', 'X', 'W', 'Q', 'U'],
				   ['F', 'V', 'P', 'J', 'I', 'O', 'Y', 'R', 'Z', 'X', 'W', 'Q', 'U', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V']]
	index = connections[0].index(letter)
	letter = connections[1][index]
	print("After reflector C: " + letter)
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
	rotorNames = []
	options = ["1", "2", "3"]
	for i in range(0, 3):
		list.append(input("rotor {}: ".format(options[i])))
	for j in range(0, 3):
		if list[j] == '1':
			setup.append(rotor1)
			rotorNames.append('1')
		elif list[j] == '2':
			setup.append(rotor2)
			rotorNames.append('2')
		elif list[j] == '3':
			setup.append(rotor3)
			rotorNames.append('3')
		elif list[j] == '4':
			setup.append(rotor4)
			rotorNames.append('4')
		elif list[j] == '5':
			setup.append(rotor5)
			rotorNames.append('5')
		elif list[j] == '6':
			setup.append(rotor6)
			rotorNames.append('6')
		elif list[j] == '7':
			setup.append(rotor7)
			rotorNames.append('7')
		elif list[j] == '8':
			setup.append(rotor8)
			rotorNames.append('8')
		elif list[j].lower() == "beta":
			setup.append(rotorBeta)
			rotorNames.append("Beta")
		elif list[j].lower() == "gamma":
			setup.append(rotorGamma)
			rotorNames.append("Gamma")
	startPoints = []
	for k in range(0, 3):
		startPoints.append(input("rotor {}, Start Point: ".format(rotorNames[k])))
	return setup, startPoints

def reflectorSetup():
	reflector = input("reflector: ")
	if reflector.upper() == 'B':
		reflector = reflectorB
	elif reflector.upper() == 'C':
		reflector = reflectorC
	return reflector

def encryption(letter, setup, startPoints, reflector, plugboard, first):
	if letter in plugboard[0]:
		index = plugboard[0].index(letter)
		letter = plugboard[1][index]
	elif letter in plugboard[1]:
		index = plugboard[1].index(letter)
		letter = plugboard[0][index]
	print("After plugboard: " + letter)
	z = 0
	for rotor in setup:
		letter = rotor(letter, startPoints[z], first, True)
		z+=1
	letter = reflector(letter)
	for rotor in setup[::-1]:
		letter = rotor(letter, None, None, False)

	if letter in plugboard[0]:
		index = plugboard[0].index(letter)
		letter = plugboard[1][index]
	elif letter in plugboard[1]:
		index = plugboard[1].index(letter)
		letter = plugboard[0][index]
	print("Final encryption: " + letter)
	
def main():
	first = True
	plugboard = plugboardSetup()
	rotorSet = rotorSetup()
	setup = rotorSet[0]
	startPoints = rotorSet[1]
	reflector = reflectorSetup()
	while True:
		letter = input("Letter: ")
		encryption(letter, setup, startPoints, reflector, plugboard, first)
		first = False
	return
main()