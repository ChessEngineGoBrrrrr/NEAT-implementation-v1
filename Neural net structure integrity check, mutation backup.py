import random
Inovation_Num_List = []
fitness = []
import chess
board = chess.Board()
import os
import re
Game_State = []
Eval_List = []
species = 40
# how to install a package (pip install) go to cmd and do   cd C:\Users\user\AppData\Local\Programs\Python\Python311\Scripts and than pip install *insert package*
def fen_to_input(fen): 
    tempBit = []
    fen = fen.split()
    splitFen = fen[0].split("/")
    for s in range(len(splitFen)):
        for letter in splitFen[s]:
            if letter == "w":
                tempBit.append(1)
            if letter == "r":
                tempBit.append(-5)
            if letter == "n":
                tempBit.append(-3)
            if letter == "b":
                tempBit.append(-4)
            if letter == "q":
                tempBit.append(-9)
            if letter == "k":
                tempBit.append(-15)
            if letter == "p":
                tempBit.append(-1)
            if letter == "R":
                tempBit.append(5)
            if letter == "N":
                tempBit.append(3)
            if letter == "B":
                tempBit.append(4)
            if letter == "Q":
                tempBit.append(9)
            if letter == "K":
                tempBit.append(15)
            if letter == "P":
                tempBit.append(1)
            if letter == "1":
                tempBit.append(0)
            if letter == "2":
                tempBit.append(0)
                tempBit.append(0)
            if letter == "3":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
            if letter == "4":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
            if letter == "5":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
            if letter == "6":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
            if letter == "7":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
            if letter == "8":
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
                tempBit.append(0)
    if fen[1] == "w":
        tempBit.append(1)
    else:
        tempBit.append(-1)
    return(tempBit)   
def Generate_Neural_Net_Nodes():
	Master_Nodes = []
	for n in range(512):
		Master_Nodes.append([[ 0 , "input" , 0,round(random.uniform(-3,3), 2) ],[ 1 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 2 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 3 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 4 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 5 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 6 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 7 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 8 , "input" , 0 ,round(random.uniform(-3,3), 2)], [ 9 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 10 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 11 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 12 , "input" , 0, round(random.uniform(-3,3), 2) ], [ 13 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 14 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 15 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 16 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 17 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 18 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 19 , "input" , 0, round(random.uniform(-3,3), 2) ], [ 20 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 21 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 22 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 23 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 24 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 25 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 26 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 27 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 28 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 29 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 30 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 31 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 32 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 33 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 34 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 35 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 36 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 37 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 38 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 39 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 40 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 41 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 42 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 43 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 44 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 45 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 46 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 47 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 48 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 49 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 50 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 51 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 52 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 53 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 54 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 55 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 56 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 57 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 58 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 59 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 60 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 61 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 62 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 63 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 64 , "input" , 0,round(random.uniform(-3,3), 2) ], [ 65 , "output" , 1,round(random.uniform(-3,3), 2) ]])
	return(Master_Nodes)
def Generate_Neural_Net_Links():
	Master_Links = []
	for n in range(512):
		Master_Links.append([])
	return(Master_Links)
Master_Nodes = Generate_Neural_Net_Nodes()
Master_Links = Generate_Neural_Net_Links()
print(len(Master_Links))
def Calculate_Species_Distance(Net_Num_1, Net_Num_2):
	Inovation_List_Species_Distance = []
	weight_difrance = 0
	Excess_Amount = 0
	Disjoint_Amount = 0
	Max_Net_Num_1 = -1
	Max_Net_Num_2 = -1
	important1 = 3
	#finds excess genes
	for j in range(len(Master_Links[Net_Num_1])):
		if Max_Net_Num_1 < Master_Links[Net_Num_1][j][4]:
			Max_Net_Num_1 = Master_Links[Net_Num_1][j][4]
	for j in range(len(Master_Links[Net_Num_2])):
		if Max_Net_Num_2 < Master_Links[Net_Num_2][j][4]:
			Max_Net_Num_2 = Master_Links[Net_Num_2][j][4]
	Net_Conections_Copy_1 = Master_Links[Net_Num_1]
	Net_Conections_Copy_2 = Master_Links[Net_Num_2]
	if Max_Net_Num_1 < Max_Net_Num_2:
		excess_is_1 = False
	else:
		excess_is_1 = True
	if excess_is_1 == True:
		for j in range(len(Master_Links[Net_Num_1])):
			if Master_Links[Net_Num_1][j][4] > Max_Net_Num_2:
				Net_Conections_Copy_1[j][4] = "Excess"
				if Net_Conections_Copy_1[j][4] == 'valid':
					Excess_Amount += 1
	else:
		for j in range(len(Master_Links[Net_Num_2])):
			if Master_Links[Net_Num_2][j][4] > Max_Net_Num_1:
				Net_Conections_Copy_2[j][4] = "Excess"
				if Net_Conections_Copy_2[j][4] == 'valid':
					Excess_Amount += 1
	#finds disjoint genes
	for j in range(len(Net_Conections_Copy_1)):
		if Net_Conections_Copy_1[j][4] != "Excess":
			Disjoint = True
			for i in range(len(Net_Conections_Copy_2)):
				if Net_Conections_Copy_1[j][4] == Net_Conections_Copy_2[i][4]:
					Disjoint = False		
		else:
			Disjoint = False
		if Disjoint == True:
			Net_Conections_Copy_1[j][4] = "Disjoint"
			if Net_Conections_Copy_1[j][2] == 'valid':
				Disjoint_Amount += 1
	for j in range(len(Net_Conections_Copy_2)):
		if Net_Conections_Copy_2[j][4] != "Excess":
			Disjoint = True
			for i in range(len(Net_Conections_Copy_1)):
				if Net_Conections_Copy_2[j][4] == Net_Conections_Copy_1[i][4]:
					Disjoint = False		
		else:
			Disjoint = False
		if Disjoint == True:
			Net_Conections_Copy_2[j][4] = "Disjoint"
			if Net_Conections_Copy_2[j][2] == 'valid':
				Disjoint_Amount += 1
	for j in range(len(Master_Links[Net_Num_1])):
		if Master_Links[Net_Num_1][j][4] != "Disjoint" and Master_Links[Net_Num_1][j][4] != "Excess":
			Inovation_List_Species_Distance.append([Master_Links[Net_Num_1][j][4]])
	print(Inovation_List_Species_Distance)
	for j in range(len(Inovation_List_Species_Distance)):
		for i in range(len(Master_Links[Net_Num_1])):	
			if Master_Links[Net_Num_1][i][4] == Inovation_List_Species_Distance[j][0]:
				Inovation_List_Species_Distance[j].append(Master_Links[Net_Num_1][i][3])
	print(Inovation_List_Species_Distance)
	for j in range(len(Inovation_List_Species_Distance)):
		for i in range(len(Master_Links[Net_Num_2])):	
			if Master_Links[Net_Num_2][i][4] == Inovation_List_Species_Distance[j][0]:
				Inovation_List_Species_Distance[j].append(Master_Links[Net_Num_2][i][3])
	for j in range(len(Inovation_List_Species_Distance)):
		weight_difrance = abs(Inovation_List_Species_Distance[j][1] - Inovation_List_Species_Distance[j][2]) + weight_difrance
	print(round(weight_difrance/len(Inovation_Num_List),2))	
	for i in range(len(Master_Links[Net_Num_2])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_2][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_2][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_2][i][4] = Inovation_Num_List[j][2]
	for i in range(len(Master_Links[Net_Num_1])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_1][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_1][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_1][i][4] = Inovation_Num_List[j][2]
	if excess_is_1 == True:
		print(Excess_Amount, Disjoint_Amount, weight_difrance, Excess_Amount/len(Master_Links[Net_Num_1]) + Disjoint_Amount/len(Master_Links[Net_Num_1]) + weight_difrance)
		return(Excess_Amount/len(Master_Links[Net_Num_1]) + Disjoint_Amount/len(Master_Links[Net_Num_1]) + weight_difrance)
	if excess_is_1 == False:
		print(Excess_Amount, Disjoint_Amount, weight_difrance, Excess_Amount/len(Master_Links[Net_Num_2]) + Disjoint_Amount/len(Master_Links[Net_Num_2]) + weight_difrance)
		return(Excess_Amount/len(Master_Links[Net_Num_2]) + Disjoint_Amount/len(Master_Links[Net_Num_2]) + weight_difrance)
def Mutate_Links(Net_Num):
	Conection_alredy_exists = False
	i = 0
	Conection_Num_1 = random.randint(0, len(Master_Nodes[Net_Num]) - 1)
	#finds to nodes to conect
	while True:
		Conection_Num_1 = random.randint(0, len(Master_Nodes[Net_Num]) - 1)
		if Master_Nodes[Net_Num][Conection_Num_1][2] == 0:
			Conection_Num_2 = random.randint(65, len(Master_Nodes[Net_Num]) - 1)
		else:
			Conection_Num_2 = random.randint(0, len(Master_Nodes[Net_Num]) - 1)
		Conection_alredy_exists = False
		if Master_Nodes[Net_Num][Conection_Num_1][2] < Master_Nodes[Net_Num][Conection_Num_2][2]:	
			for j in range(len(Master_Links[Net_Num])):
				Conection_alredy_exists = False
				if Conection_Num_1 == Master_Links[Net_Num][j][0] and Conection_Num_2 == Master_Links[Net_Num][j][1]:
					Conection_alredy_exists = True
					break
		else:
			for j in range(len(Master_Links[Net_Num])):
				Conection_alredy_exists = False
				if Conection_Num_1 == Master_Links[Net_Num][j][1] and Conection_Num_2 == Master_Links[Net_Num][j][0]:
					Conection_alredy_exists = True
					break		
		if (Master_Nodes[Net_Num][Conection_Num_1][2] != Master_Nodes[Net_Num][Conection_Num_2][2] and Conection_alredy_exists == False):
			break
		else:
			print("poki")
	if Master_Nodes[Net_Num][Conection_Num_1][2] < Master_Nodes[Net_Num][Conection_Num_2][2]:
		for j in range(len(Inovation_Num_List)):
			Inov_is_Equal = False
			if Inovation_Num_List[j][0] == Conection_Num_1 and Inovation_Num_List[j][1] == Conection_Num_2:
				Inovation_Num = Inovation_Num_List[j][2]
				Inov_is_Equal = True
				break
		if len(Inovation_Num_List) != 0:
			if Inov_is_Equal == False:
				Inovation_Num = len(Inovation_Num_List)
				Inovation_Num_List.append([Conection_Num_1, Conection_Num_2, Inovation_Num])
		else: 
			Inovation_Num = 0
			Inovation_Num_List.append([Conection_Num_1, Conection_Num_2, Inovation_Num])
		return([Conection_Num_1, Conection_Num_2, "valid", round(random.uniform(-5,5), 2), Inovation_Num])
	else:
		for j in range(len(Inovation_Num_List)):
			Inov_is_Equal = False
			if Inovation_Num_List[j][0] == Conection_Num_2 and Inovation_Num_List[j][1] == Conection_Num_1:
				Inovation_Num = Inovation_Num_List[j][2]
				Inov_is_Equal = True
				break
		if len(Inovation_Num_List) != 0:
			if Inov_is_Equal == False:
				Inovation_Num = len(Inovation_Num_List)
				Inovation_Num_List.append([Conection_Num_2, Conection_Num_1, Inovation_Num])

		else: 
			Inovation_Num = 0
			Inovation_Num_List.append([Conection_Num_2, Conection_Num_1, Inovation_Num])
		return([Conection_Num_2, Conection_Num_1, "valid", round(random.uniform(-5,5), 2), Inovation_Num])
def Mutate_Nodes(Net_Num):
	global Historic_Queue
	Devide = False
	#Finds a conection to add a node to
	while True:	
		Disable_Conection = random.randint(0, len(Master_Links[Net_Num]) - 1)
		if Master_Links[Net_Num][Disable_Conection][2] != "invalid":
			break
	begining = Master_Links[Net_Num][Disable_Conection][0]
	to = Master_Links[Net_Num][Disable_Conection][1]
	Master_Links[Net_Num][Disable_Conection][2] = "invalid"
	#sees if its a new inovation number or its alredy been asigned
	for j in range(len(Inovation_Num_List)):
			Inov_is_Equal = False
			if Inovation_Num_List[j][0] == begining and Inovation_Num_List[j][1] == len(Master_Nodes[Net_Num]):
				Inovation_Num = Inovation_Num_List[j][2]
				Inov_is_Equal = True
				break
	#if it is new and the list isnt empty ads a new inovation number to the list along with the coresponding node combo
	if Inov_is_Equal == False and len(Inovation_Num_List) != 0:
		Inovation_Num = len(Inovation_Num_List)
		Inovation_Num_List.append([begining, len(Master_Nodes[Net_Num]), Inovation_Num])
	#random selects id it devids by anum or somthn else
	Master_Links[Net_Num].append([begining, len(Master_Nodes[Net_Num]), "valid", round(random.uniform(-5,5), 2), Inovation_Num])
	#repetes the previous 2 steps
	for j in range(len(Inovation_Num_List)):
			Inov_is_Equal = False
			if Inovation_Num_List[j][0] == len(Master_Nodes[Net_Num]) and Inovation_Num_List[j][1] == to :
				Inovation_Num = Inovation_Num_List[j][2]
				Inov_is_Equal = True
				break
	if Inov_is_Equal == False and len(Inovation_Num_List) != 0:
		Inovation_Num = len(Inovation_Num_List)
		Inovation_Num_List.append([len(Master_Nodes[Net_Num]), to, Inovation_Num])
	Master_Links[Net_Num].append([len(Master_Nodes[Net_Num]), to, "valid", Master_Links[Net_Num][Disable_Conection][3], Inovation_Num])
	#starts the layer incrementing and actualy generates the new nodes
	if Master_Nodes[Net_Num][to][2]  - Master_Nodes[Net_Num][begining][2] == 1:
		if to != 65:
			Master_Nodes[Net_Num][to][2] += 1
		Historic_Queue = []
		print(begining, to, Master_Nodes[Net_Num][to])
		Layer_Ajust(Net_Num, [to])
		New_Layer = Master_Nodes[Net_Num][begining][2] + 1
	else:
		New_Layer = Master_Nodes[Net_Num][begining][2] + 1
	Master_Nodes[Net_Num].append([len(Master_Nodes[Net_Num]), "hidden", New_Layer, round(random.uniform(-3,3), 2)])
Historic_Queue = []
def Layer_Ajust(Net_Num, queue):
#Forward breath for search algorthm moving all node that are direct "ofsprings" one layer forward
	# PROBLEM CONECTIONS GOING MORE THAN ONE LAYER LIKE FRO LAYER 1 TO 3 ARE CAUSING UNWANTED INDEXING OF THE LAYER
	global Historic_Queue
	Nodes_To_Increment = []
	Temp_queue = []
	Queue_Full_Of_End_Node = False
	Node_Layer_Incremented = False
	for i in range(len(queue)):
			#looks if the queue has only end nodes or one end node and increments its layer once
		if queue[i] != 65:
			Queue_Full_Of_End_Node = False
			break
		else: Queue_Full_Of_End_Node = True
	print(queue, Net_Num * 100)
	Historic_Queue.append([])
	print(Historic_Queue, "cucusbintifertimontertulcusdeport")
	if len(queue) != 0:
		if (queue[0] == 65 and len(queue) == 1) or Queue_Full_Of_End_Node == True:
			Master_Nodes[Net_Num][65][2] += 1
		else:
			#actual algorithm
			for i in range(len(queue)):
				for j in range(len(Master_Links[Net_Num])):
					if Master_Links[Net_Num][j][0] == queue[i] and Master_Links[Net_Num][j][2] != "invalid" and Master_Nodes[Net_Num][Master_Links[Net_Num][j][1]][2] - Master_Nodes[Net_Num][queue[i]][2] == 0:
						Node_Layer_Incremented = False
						for l in range(len(Historic_Queue[len(Historic_Queue) - 1])):
							if Historic_Queue[len(Historic_Queue) - 1][l] == Master_Links[Net_Num][j][1]:
								Node_Layer_Incremented = True
								break
							else:
								Node_Layer_Incremented = False
						if Node_Layer_Incremented == False:
							if Master_Links[Net_Num][j][1] != 65:	
								Master_Nodes[Net_Num][Master_Links[Net_Num][j][1]][2] += 1
								Historic_Queue[len(Historic_Queue) - 1].append(Master_Links[Net_Num][j][1])
							Temp_queue.append(Master_Links[Net_Num][j][1])
			queue = Temp_queue
			Layer_Ajust(Net_Num, queue)
def Mutate_Weight(Net_Num):
	for a in range(len(Master_Links[Net_Num])):
		if random.randint(1, 10) < 7 and Master_Links[Net_Num][a][2] != "invalid":
			Master_Links[Net_Num][a][3] = round(Master_Links[Net_Num][a][3] + round(random.uniform(-0.2, 0.2), 2), 2)
		elif random.randint(1, 10) < 4 and Master_Links[Net_Num][a][2] == "disabled":
			Master_Links[Net_Num][a][2] = "valid"
		elif random.randint(1, 10) < 2 and Master_Links[Net_Num][a][2] != "invalid":
			Master_Links[Net_Num][a][3] = round(Master_Links[Net_Num][a][3] + round(random.uniform(-2, 2), 2), 2)
def Mutate_Bias(Net_Num):
	for a in range(len(Master_Nodes[Net_Num])):
		if random.randint(1, 10) < 3 and Master_Nodes[Net_Num][a][0]:
			Master_Nodes[Net_Num][a][3] = Master_Nodes[Net_Num][a][3] + round(random.uniform(-0.7,0.7), 2)
def Disable_Conection(Net_Num, Conection_Num):
	Master_Links[Net_Num][Conection_Num][2] = "disabled"
def Fitness(Actual_Eval, Net_Eval):
	Fitness = 0
	if Actual_Eval > Net_Eval and (Actual_Eval > 3 or Actual_Eval < -3):
		Fitness = Actual_Eval - Net_Eval
	elif Actual_Eval > Net_Eval and (Actual_Eval < 1.5 and Actual_Eval > -1.5):
		Fitness = (Actual_Eval - Net_Eval) * 3
	elif Actual_Eval < Net_Eval and (Actual_Eval > 1.5 or Actual_Eval < -1.5):
		Fitness = Net_Eval - Actual_Eval
	elif Actual_Eval < Net_Eval and (Actual_Eval < 1.5 and Actual_Eval > -1.5):
		Fitness = (Net_Eval - Actual_Eval) * 3
	if (Actual_Eval > 0 and Net_Eval > 0) or (Actual_Eval < 0 and Net_Eval < 0):
		Fitness -= 1
	return(Fitness)
def Hoinky_Boinky(Net_Num_1, Net_Num_2, Net_2_Is_Unique=True):
	Max_Net_Num_1 = -1
	Ofspring_Nodes = []
	Max_Net_Num_2 = -1
	if Net_2_Is_Unique == False:
		Net_Num_2 = 0
		Master_Links[0] = Master_Links[Net_Num_1]
		Master_Nodes[0] = Master_Nodes[Net_Num_1]
		Mutate_Weight(0)
		for j in range(2):
			Mutate_Nodes(0)
			Mutate_Links(0)
	important1 = 3
	global Fitness_List
	Ofspring_Conections = []
	#finds excess genes
	for j in range(len(Master_Links[Net_Num_1])):
		if Max_Net_Num_1 < Master_Links[Net_Num_1][j][4]:
			Max_Net_Num_1 = Master_Links[Net_Num_1][j][4]
	for j in range(len(Master_Links[Net_Num_2])):
		if Max_Net_Num_2 < Master_Links[Net_Num_2][j][4]:
			Max_Net_Num_2 = Master_Links[Net_Num_2][j][4]
	Net_Conections_Copy_1 = Master_Links[Net_Num_1].copy()
	Net_Conections_Copy_2 = Master_Links[Net_Num_2].copy()
	if Max_Net_Num_1 < Max_Net_Num_2:
		excess_is_1 = False
	else:
		excess_is_1 = True
	if excess_is_1 == True:
		for j in range(len(Master_Links[Net_Num_1])):
			if Master_Links[Net_Num_1][j][4] > Max_Net_Num_2:
				Net_Conections_Copy_1[j][4] = "Excess"
	else:
		for j in range(len(Master_Links[Net_Num_2])):
			if Master_Links[Net_Num_2][j][4] > Max_Net_Num_1:
				Net_Conections_Copy_2[j][4] = "Excess"
	#finds disjoint genes
	for j in range(len(Net_Conections_Copy_1)):
		if Net_Conections_Copy_1[j][4] != "Excess":
			Disjoint = True
			for i in range(len(Net_Conections_Copy_2)):
				if Net_Conections_Copy_1[j][4] == Net_Conections_Copy_2[i][4]:
					Disjoint = False		
		else:
			Disjoint = False
		if Disjoint == True:
			Net_Conections_Copy_1[j][4] = "Disjoint"
	for j in range(len(Net_Conections_Copy_2)):
		if Net_Conections_Copy_2[j][4] != "Excess":
			Disjoint = True
			for i in range(len(Net_Conections_Copy_1)):
				if Net_Conections_Copy_2[j][4] == Net_Conections_Copy_1[i][4]:
					Disjoint = False		
		else:
			Disjoint = False
		if Disjoint == True:
			Net_Conections_Copy_2[j][4] = "Disjoint"
	#Does the breeding depending on fitness(The last else asumes that after checking wich is biger they are equal)
	for i in range(len(Master_Links[Net_Num_2])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_2][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_2][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_2][i][4] = Inovation_Num_List[j][2]
	for i in range(len(Master_Links[Net_Num_1])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_1][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_1][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_1][i][4] = Inovation_Num_List[j][2]
	print(Net_Conections_Copy_1,"space si demanded of me right?",Net_Conections_Copy_2, "im number 111111")
	if Fitness_List[Net_Num_1] > Fitness_List[Net_Num_2]:
		for j in range(len(Net_Conections_Copy_1)):
			if Net_Conections_Copy_1[j][4] != "Excess" and Net_Conections_Copy_1[j][4] != "Disjoint":
				if round(random.uniform(0, 2), 2) < 1.3:
					Ofspring_Conections.append(Master_Links[Net_Num_1][j])
				else:
					for i in range(len(Net_Conections_Copy_2)):
						if Net_Conections_Copy_2[i][4] == Net_Conections_Copy_1[j][4]:
							Ofspring_Conections.append(Master_Links[Net_Num_2][i])
			elif Net_Conections_Copy_1[j][4] == "Excess" or Net_Conections_Copy_1[j][4] == "Disjoint":
				Ofspring_Conections.append(Master_Links[Net_Num_1][j])
	elif Fitness_List[Net_Num_1] < Fitness_List[Net_Num_2]:
		for j in range(len(Net_Conections_Copy_2)):
			if Net_Conections_Copy_2[j][4] != "Excess" and Net_Conections_Copy_2[j][4] != "Disjoint":
				if round(random.uniform(0, 2), 2) < 1.3:
					Ofspring_Conections.append(Master_Links[Net_Num_2][j])
				else:
					for i in range(len(Net_Conections_Copy_1)):
						if Net_Conections_Copy_1[i][4] == Net_Conections_Copy_2[j][4]:
							Ofspring_Conections.append(Master_Links[Net_Num_1][i])
			elif Net_Conections_Copy_2[j][4] == "Excess" or Net_Conections_Copy_1[j][4] == "Disjoint":
				Ofspring_Conections.append(Master_Links[Net_Num_2][j])
	else:
		for j in range(len(Net_Conections_Copy_1)):
			if Net_Conections_Copy_1[j][4] != "Excess" and Net_Conections_Copy_1[j][4] != "Disjoint":
				if round(random.uniform(0, 2), 2) < 1:
					Ofspring_Conections.append(Master_Links[Net_Num_1][j])
				else:
					for i in range(len(Net_Conections_Copy_2)):
						if Net_Conections_Copy_2[i][4] == Net_Conections_Copy_1[j][4]:
							Ofspring_Conections.append(Master_Links[Net_Num_2][i])
			if round(random.uniform(0, 2), 2) < 1 and important1 == 3:
				important1 = 1
			else:
				important1 = 2
			if important1 == 1 and Net_Conections_Copy_1[j][4] == "Excess" and Net_Conections_Copy_1[j][4] == "Disjoint":
				Ofspring_Conections.append(Master_Links[Net_Num_1][j])
			else:
				Ofspring_Conections.append(Master_Links[Net_Num_2][i])
	print(Ofspring_Conections, "im number 222222")
	#makes sure the inovation nums are correct
	for i in range(len(Master_Links[Net_Num_2])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_2][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_2][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_2][i][4] = Inovation_Num_List[j][2]
	for i in range(len(Master_Links[Net_Num_1])):
		for j in range(len(Inovation_Num_List)):
			if Master_Links[Net_Num_1][i][0] == Inovation_Num_List[j][0] and Master_Links[Net_Num_1][i][1] == Inovation_Num_List[j][1]:
				Master_Links[Net_Num_1][i][4] = Inovation_Num_List[j][2]
	Alredy_seen = []
	Alredy_Seeeen = False
	for j in range(len(Ofspring_Conections)):
		for i in range(len(Alredy_seen)):
			if Alredy_seen[i] == Ofspring_Conections[j][0]:
				Alredy_Seeeen = True
				break
		if Alredy_Seeeen != True and Ofspring_Conections[j][0] > 65:
			Alredy_seen.append(Ofspring_Conections[j][0])
		Alredy_Seeeen = False
		for i in range(len(Alredy_seen)):
			if Alredy_seen[i] == Ofspring_Conections[j][1]:
				Alredy_Seeeen = True
				break
		if Alredy_Seeeen != True and Ofspring_Conections[j][1] > 65:
			Alredy_seen.append(Ofspring_Conections[j][1])
		Alredy_Seeeen = False
	Alredy_seen = sorted(Alredy_seen)
	for node in Alredy_seen:
		Ofspring_Nodes.append([node, "hidden" , 0 ,round(random.uniform(-3,3), 2) ])
	print(Ofspring_Conections,Alredy_seen, "im number 3333333")
	return(Ofspring_Conections)		
Curent_Layer_ToBe_Calculated = 1
Current_Layer = []
Caclulate_Return = 1
def Calculate(Net_Num):
	global Current_Layer
	Sum_Current_Node = 0
	Exists_Alredy = False
	global Caclulate_Return
	global Curent_Layer_ToBe_Calculated
	if len(Current_Layer) > 0:	
		if Current_Layer[len(Current_Layer) - 1][0] == 65:
			for j in range(len(Current_Layer)):
				if Current_Layer[j][0] == 65:
					Caclulate_Return = Current_Layer[j][1]
					return(0)
	#caLculates layer by layer biginning from the first hidden layer.Traces back conections and calculates like that
	First_Layer = fen_to_input(chess.Board().fen())
	Buffer_Layer = []
	if Curent_Layer_ToBe_Calculated == 1:	
		for j in range(len(Master_Nodes[Net_Num])):
			for i in range(len(Master_Links[Net_Num])):
				if (Master_Nodes[Net_Num][j][2] == Curent_Layer_ToBe_Calculated and Master_Nodes[Net_Num][j][0] == Master_Links[Net_Num][i][1]) and Master_Links[Net_Num][i][2] == "valid":
					Sum_Current_Node = Sum_Current_Node + First_Layer[Master_Links[Net_Num][i][0]]*Master_Links[Net_Num][i][3]
					Exists_Alredy = True
			if Exists_Alredy == True:


				if Master_Nodes[Net_Num][j][0] > 65:
					Sum_Current_Node = Sum_Current_Node + Master_Nodes[Net_Num][j][3]
				if Sum_Current_Node > 0 or Sum_Current_Node == 0:
					Current_Layer.append([Master_Nodes[Net_Num][j][0],round(Sum_Current_Node,2), Master_Nodes[Net_Num][j][2]])
				else: 
					 Current_Layer.append([Master_Nodes[Net_Num][j][0],round(Sum_Current_Node*0.5, 2), Master_Nodes[Net_Num][j][2]])
			Exists_Alredy = False
			Sum_Current_Node = 0
		Curent_Layer_ToBe_Calculated = 1 + Curent_Layer_ToBe_Calculated
	else:
		for j in range(len(Master_Nodes[Net_Num])):
			for i in range(len(Master_Links[Net_Num])):
				if (Master_Nodes[Net_Num][j][2] == Curent_Layer_ToBe_Calculated and Master_Nodes[Net_Num][j][0] == Master_Links[Net_Num][i][1]) and Master_Links[Net_Num][i][2] == "valid":
					for k in range(len(Current_Layer)):
						if Current_Layer[k][0] == Master_Links[Net_Num][i][0]:	
							Sum_Current_Node = Sum_Current_Node + Current_Layer[k][1]*Master_Links[Net_Num][i][3]
							Exists_Alredy = True
			if Exists_Alredy == True:

				if Master_Nodes[Net_Num][j][0] > 65:	
					Sum_Current_Node = Sum_Current_Node + Master_Nodes[Net_Num][j][3]
				if Sum_Current_Node > 0 or Sum_Current_Node == 0:
					Current_Layer.append([Master_Nodes[Net_Num][j][0],round(Sum_Current_Node, 2), Master_Nodes[Net_Num][j][2]])
				else:
					 Current_Layer.append([Master_Nodes[Net_Num][j][0],round(Sum_Current_Node * 0.5, 2), Master_Nodes[Net_Num][j][2]])
			Exists_Alredy = False
			Sum_Current_Node = 0
		Curent_Layer_ToBe_Calculated = 1 + Curent_Layer_ToBe_Calculated
	Calculate(Net_Num)
Bad_Games = []
for j in range(len(Master_Links)):
	for i in range(200):
		chance = random.randint(1, 10)
		if chance > 8:
			if len(Master_Links[j]) > 0:	
				Mutate_Nodes(j)
			else:	
				Master_Links[j].append(Mutate_Links(j))
		if chance > 2 and chance <= 8:
			Master_Links[j].append(Mutate_Links(j))
		if chance <= 2:
			Mutate_Bias(j)
Fitness_Specimens = [] 
Target_Species_Number = 50
Allowed_Species_Distance = 50
def Next_Generation_Generate(Last_Species_Amout_More, Allowed_Species_Distance):
	global Fitness_Specimen
	Global_Avrage = 0
	Total_Ofsprings = 0
	Amout_off_Ofsprings_That_Resault = 0
	Species_Avrage_Fitness_List = []
	Return_Species = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,]
	if Last_Species_Amout_More == True:
		Allowed_Species_Distance -= 1
	else:
		Allowed_Species_Distance += 1
	Species = [[0]]
	for j in range(len(Master_Nodes)-1):
		Species_Has_Been_Found = False
		for i in range(len(Species)):
			if Calculate_Species_Distance(j + 1, Species[i][0]) < Allowed_Species_Distance:
				Species[i].append(j + 1)
				Species_Has_Been_Found = True
				print(Species, "suptimetmus")
				break
			else:
				Species_Has_Been_Found = False
		if Species_Has_Been_Found == False:
			Species.append([j + 1])
			print(Species, 'sorticoftarmilnof')
	for j in range(len(Species)):
		for l in range(len(Species[j])):
			Return_Species[Species[j][l]] = j
	for j in range(len(Species)):
		Species_Avrage_Fitness_List.append([j, Fitness_List[Species[j][0]]])
	for j in range(len(Species)):
		for l in range(len(Species[j])):
			if l != 0:
				Species_Avrage_Fitness_List[j][1] = Species_Avrage_Fitness_List[j][1] + Fitness_List[Species[j][l]]
	print( Species_Avrage_Fitness_List)
	for j in range(len(Species_Avrage_Fitness_List)):
		Species_Avrage_Fitness_List[j][1] = Species_Avrage_Fitness_List[j][1]/(len(Species[Species_Avrage_Fitness_List[j][0]])*len(Species[Species_Avrage_Fitness_List[j][0]]))
	print( Species_Avrage_Fitness_List)
	for j in range(len(Species_Avrage_Fitness_List)):
		Global_Avrage = Global_Avrage + Species_Avrage_Fitness_List[j][1]
	Global_Avrage = Global_Avrage/len(Species_Avrage_Fitness_List)
	print(Species_Avrage_Fitness_List)
	for j in range(len(Species_Avrage_Fitness_List)):
		Species_Avrage_Fitness_List[j].append(Species_Avrage_Fitness_List[j][1]/Global_Avrage*len(Species[Species_Avrage_Fitness_List[j][0]]))
		Total_Ofsprings = Species_Avrage_Fitness_List[j][1]/Global_Avrage*len(Species[Species_Avrage_Fitness_List[j][0]]) + Total_Ofsprings
	Total_Ofsprings = 512/Total_Ofsprings
	print(Species_Avrage_Fitness_List, "shshshhshshhshshsshhshshshshhsh")
	for j in range(len(Species_Avrage_Fitness_List)):
		Species_Avrage_Fitness_List[j][2] = round(Species_Avrage_Fitness_List[j][2]*Total_Ofsprings, 0)
	for j in range(len(Species_Avrage_Fitness_List)):
		Amout_off_Ofsprings_That_Resault = Amout_off_Ofsprings_That_Resault + Species_Avrage_Fitness_List[j][2]
	print(Species_Avrage_Fitness_List, Species,Amout_off_Ofsprings_That_Resault)
	if Amout_off_Ofsprings_That_Resault > 512:
		for j in range(len(Species_Avrage_Fitness_List)):
			if Species_Avrage_Fitness_List[j][2] > 50:
				Species_Avrage_Fitness_List[j][2] = Species_Avrage_Fitness_List[j][2] - (Amout_off_Ofsprings_That_Resault - 512)
				break
	if Amout_off_Ofsprings_That_Resault < 512:
		Species_Avrage_Fitness_List[0][2] = Species_Avrage_Fitness_List[0][2] + (512 - Amout_off_Ofsprings_That_Resault)	
	Amout_off_Ofsprings_That_Resault = 0
	for j in range(len(Species_Avrage_Fitness_List)):
		Amout_off_Ofsprings_That_Resault = Amout_off_Ofsprings_That_Resault + Species_Avrage_Fitness_List[j][2]
	print(Return_Species,Species_Avrage_Fitness_List, Species,Amout_off_Ofsprings_That_Resault)
	return(Return_Species,Species_Avrage_Fitness_List, Species,Amout_off_Ofsprings_That_Resault)
def Fitness_Calculate():
	global Curent_Layer_ToBe_Calculated
	global Current_Layer
	global Caclulate_Return
	global Fitness_List
	global Batch_Size
	game = random.randint(0, len(File_Procesed_New) - 1)
	Fitness_List = []
	for j in range(512):
		chess.Board(File_Procesed_New[game][1])
		if File_Procesed_New[game][0][1] == "mate":
			Eval = 300
		else:
			Eval = round(File_Procesed_New[game][0][3]/100, 2)
		#Eval = File_Procesed[game][0]
		Caclulate_Return = 15
		Current_Layer = []
		Curent_Layer_ToBe_Calculated = 1
		Calculate(j)
		Fitness_List.append(Fitness(Eval, Caclulate_Return))
	print(Fitness_List)
	for i in range(Batch_Size - 1):
		game = random.randint(0, len(File_Procesed_New) - 1)
		for j in range(512):
			chess.Board(File_Procesed_New[game][1])
			if File_Procesed_New[game][0][1] == "mate":
				Eval = 300
			else:
				Eval = round(File_Procesed_New[game][0][3]/100, 2)
			Caclulate_Return = 15
			Current_Layer = []
			Curent_Layer_ToBe_Calculated = 1
			print(game)
			Calculate(j)
			Fitness_List[j] = Fitness_List[j] + Fitness(Eval, Caclulate_Return)
	Max_Fitness = 0
	for j in range(len(Fitness_List)):
		Fitness_List[j] = round(Fitness_List[j]/Batch_Size, 2)
	for j in range(len(Fitness_List)):
		Fitness_List[j] = Fitness_List[j]*-1
	for j in range(len(Fitness_List)):
		if Fitness_List[j] + 100 > 0:	
			Fitness_List[j] = round((Fitness_List[j] + 100)*(Fitness_List[j] + 100), 2)
		else:
			Fitness_List[j] = round(Fitness_List[j]/-70, 2)
	print(Fitness_List)

Batch_Size = 10

def Make_New_Population():
	Fitness_Calculate()
	global Fitness_List
	bullshit = Next_Generation_Generate(True, 60)
	Species = bullshit[2]
	Offspring_List = bullshit[1]
	Copy_Master_Links = Master_Links[:]
	Copy_Master_Nodes = Master_Nodes[:]
	Roulette_List = []
	Sum_Species = 0
	index = 0
	Parent_2 = -1
	for j in range(len(Species)):
		Parent_2 = -1
		Roulette_List = []
		Sum_Species = 0
		for i in range(len(Species[j])):
			Sum_Species = Sum_Species + Fitness_List[Species[j][i]]
		Roulette_List = [round(Fitness_List[Species[j][0]]/Sum_Species*100, 2)]	
		for i in range(len(Species[j])):		
			if i != 0:
				Roulette_List.append(round(Fitness_List[Species[j][i]]/Sum_Species*100 + Roulette_List[i - 1], 2))
		print(Roulette_List)
		print(Offspring_List[j][2])
		if len(Species[j]) == 1:
			for i in range(int(Offspring_List[j][2])):
				Original_Net_0_Links = Master_Links[0]
				Original_Net_0_Nodes = Master_Nodes[0]
				Copy_Master_Links[index] = Hoinky_Boinky(Species[j][0], 0, False)
				Master_Links[0] = Original_Net_0_Links
				Master_Nodes[0] = Original_Net_0_Nodes
				index += 1
				print(Copy_Master_Links[index - 1])
		if Offspring_List[j][2] != 0 and len(Species[j]) != 1:
			for i in range(int(Offspring_List[j][2])):
				Random_Number = round(random.uniform(0, 100), 2) 
				for l in range(len(Roulette_List)):
					if Random_Number < Roulette_List[l]:
						Parent_1 = l
						print(Parent_1, "parent1")
						break
				Parent_2 = Parent_1
				while Parent_1 == Parent_2:
					Random_Number = round(random.uniform(0, 100), 2) 
					for l in range(len(Roulette_List)):
						if Random_Number < Roulette_List[l]:
							Parent_2 = l
							print(Parent_2, "parent2", Parent_1)
							break
				Copy_Master_Links[index] = Hoinky_Boinky(Species[j][Parent_1], Species[j][Parent_2], True)
				index += 1
			print(Copy_Master_Links[index - 1])
	print(Copy_Master_Links)
#for j in range(len(bullshit[1])):
	#if bullshit[1][j][2] == 0:
		#for i in range(len(bullshit[2][bullshit[1][j][0]])):
		#	Copy_Master_Nodes[bullshit[2][bullshit[1][j][0]][i]] = ["null"]
		#	Copy_Master_Links[bullshit[2][bullshit[1][j][0]][i]] = ["null"]
#print(Copy_Master_Links, Copy_Master_Nodes)
Make_New_Population()
Offspring_Lst = Hoinky_Boinky(0,1)
print(Offspring_Lst)
Alredy_seen = []
Alredy_Seeeen = False
for j in range(len(Offspring_Lst)):
	for i in range(len(Alredy_seen)):
		if Alredy_seen[i] == Offspring_Lst[j][0]:
			Alredy_Seeeen = True
			break
	if Alredy_Seeeen != True and Offspring_Lst[j][0] > 65:
		Alredy_seen.append(Offspring_Lst[j][0])
	Alredy_Seeeen = False
	for i in range(len(Alredy_seen)):
		if Alredy_seen[i] == Offspring_Lst[j][1]:
			Alredy_Seeeen = True
			break
	if Alredy_Seeeen != True and Offspring_Lst[j][1] > 65:
		Alredy_seen.append(Offspring_Lst[j][1])
	Alredy_Seeeen = False
Alredy_seen = sorted(Alredy_seen)
Alredy_seen = []
for j in range(len(Master_Links[0])):
	for i in range(len(Alredy_seen)):
		if Alredy_seen[i] == Master_Links[0][j][0]:
			Alredy_Seeeen = True
			break
	if Alredy_Seeeen != True and Master_Links[0][j][0] > 65:
		Alredy_seen.append(Master_Links[0][j][0])
	Alredy_Seeeen = False
print(sorted(Alredy_seen))
Alredy_seen = []
for j in range(len(Master_Links[1])):
	for i in range(len(Alredy_seen)):
		if Alredy_seen[i] == Master_Links[1][j][0]:
			Alredy_Seeeen = True
			break
	if Alredy_Seeeen != True and Master_Links[1][j][0] > 65:
		Alredy_seen.append(Master_Links[1][j][0])
	Alredy_Seeeen = False
print(sorted(Alredy_seen))
Alredy_seen = []
print(Master_Links[0])
print(Master_Nodes[0])
print(Master_Nodes[1])
print(Master_Links[1])