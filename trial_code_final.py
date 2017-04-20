def word_num(x,current_word):
	
	unit_word = ['one','two','three','four','five','six','seven','eight','nine']
	tens_word = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	word_in_ten = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	hundreds_number,tens_number,number,flag = 0,0,0,0
	next, next2, next3, next4 = '','','',''
	i = x.split().index(current_word)
	while True:	

		if x.split()[i] in tens_word:
			try:
				next = x.split()[i+1]
				if next in unit_word:
					number = (tens_word.index(x.split()[i]) + 2) * 10 + unit_word.index(next) + 1
					flag = 2
					break
				else:
					number = (tens_word.index(x.split()[i]) + 2) * 10
					flag = 1
					break
			except IndexError:
				number = (tens_word.index(x.split()[i]) + 2) * 10
				flag = 1
				break				

		elif x.split()[i] == 'ten':
			number = 10
			flag = 1
			break

		elif x.split()[i] in unit_word + word_in_ten:
			try:
				next = x.split()[i+1]
				if next == 'hundred':
					try:
						next2 = x.split()[i+2]
						if next2 == 'and':
							try:
								next3 = x.split()[i+3]							
								if next3 in unit_word + word_in_ten:
									hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
									number = hundreds_number + ((unit_word.index(next3) + 1) if x.split()[i+3] in unit_word else (word_in_ten.index(next3) + 11))
									flag = 4
									break
								elif next3 in tens_word:
									try:
										next4 = x.split()[i+4]
										if next4 in unit_word:
											hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
											tens_number = (tens_word.index(next3) + 2) * 10
											number = hundreds_number + tens_number + (unit_word.index(next4) + 1)
											flag = 5
											break
										else:
											hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
											number = hundreds_number + ((tens_word.index(next3) + 2) * 10)
											flag = 4
											break
									except IndexError:
										hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
										number = hundreds_number + ((tens_word.index(next3) + 2) * 10)
										flag = 4
										break
									
								else:
									number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
									flag = 2
									break
							except IndexError:
								number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
								flag = 2
								break

						elif next2 in unit_word + word_in_ten:
							hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
							number = hundreds_number + ((unit_word.index(next2) + 1) if x.split()[i+2] in unit_word else (word_in_ten.index(next2) + 11))
							flag = 3
							break
						elif next2 in tens_word:
							try:
								next4 = x.split()[i+3]
								if next4 in unit_word:
									hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
									tens_number = (tens_word.index(next2) + 2) * 10
									number = hundreds_number + tens_number + (unit_word.index(next4) + 1)
									flag = 4
									break
								else:
									hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
									number = hundreds_number + ((tens_word.index(next2) + 2) * 10)
									flag = 3
									break
							except IndexError:
								hundreds_number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
								number = hundreds_number + ((tens_word.index(next2) + 2) * 10)
								flag = 3
								break
							
						else:
							number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
							flag = 2
							break
					except IndexError:
						number = (unit_word.index(x.split()[i]) + 1) * 100 if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11) * 100
						flag = 2
						break
					
				else:
					number = (unit_word.index(x.split()[i]) + 1) if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11)
					flag = 1
					break
			
			except IndexError:
				number = (unit_word.index(x.split()[i]) + 1) if x.split()[i] in unit_word else (word_in_ten.index(x.split()[i]) + 11)
				flag = 1
				break
				
		if number == 0:
			break		
	return number, flag

def user_control_program():
	
	global motor_positions #This defines the positions of the motor in real time. 90 when the program begins

	while True:
	
		my_os.system('clear')

		print('motor positions:\nmotor 1: {0[0]}\nmotor 2: {0[1]}\nmotor 3: {0[2]}\nmotor 4: {0[3]}\nmotor 5: {0[4]}\n'.format(motor_positions))

		x=raw_input("Type in your command and press enter to execute it. Our robot would move accordingly.\nBut remember that it could only be instructed to move left or right with a maximum angle of 90 on either side.\nEnter 'quit' or 'q' to quit.\nEnjoy!\n> ")
		x=x.lower()

		if x in ['q','quit']:
			break

		direction,direction_send,direction_index_list,ip_dir,degree,error,error_prompts,error_found,choice,chosen = input_translation(x)

		for i in error.keys():
			if error[i]:
				print(error_prompts[i])
				error_found = True

		if error_found == True:
			raw_input("\n\nPress any key to continue.")
			continue

		print("\n\n")

		while True:

			
			print('This arm would now move',ip_dir,'by',degree,'degrees')
			
			chosen = raw_input("If that's what you intended, type in 'y' or 'yes' to proceed or else 'n' or 'no' to retry.\n> ")
	
			if chosen.lower() in choice[0]:
				motor_in_question = int(direction_index_list.index(direction_send[ip_dir])/2)
				motor_positions[motor_in_question] = motor_positions[motor_in_question] + ( degree if  direction_index_list.index(direction_send[ip_dir]) % 2 == 0 else -degree)				
				#send = str(motor_positions[motor_in_question]) + direction_send[ip_dir]
				send = str(degree) + direction_send[ip_dir]

				print('Send to arduino:',send)
				send_to_arduino(send)
				print('motor positions:\nmotor 1: {0[0]}\nmotor 2: {0[1]}\nmotor 3: {0[2]}\nmotor 4: {0[3]}\nmotor 5: {0[4]}\n'.format(motor_positions))
				print("\n\nWe were pleased to help you. See you soon.")
				raw_input()
				break
			elif chosen.lower() in choice[1]:
				print("\n\nWe apologize for misinterpretation. Please try again.")
				raw_input()
				break
			else:
				print('\n\nInvalid choice. Press any key to reply again. ')
				raw_input()
				my_os.system('clear')

def input_translation(x):
	global motor_positions

	direction = ['left','right','front','back','up','down','clockwise','anticlockwise','grasp','leave']
	direction_send = {'left':'l','right':'r','front':'f','back':'b','up':'u','down':'d','clockwise':'c','anticlockwise':'a','grasp':'g','leave':'t'}
	direction_index_list = ['l','r','f','b','u','d','c','a','g','t']
	ip_dir = ''
	degree = 0
	max_degree = 180
	error = {'direction_not':True,'direction_twice':False,'value_not':True,'value_twice':False,'value_exceeded':False,'value_negative':False}
	error_prompts = {'direction_not':'Error: Direction not specified.','direction_twice':'Error: Direction specifed multiple times.','value_not':'Error: Angle not specified.','value_twice':'Error: Angle specified multiple times.','value_exceeded':'Error: Max value is 359.','value_negative':'Error: Angle has to be a postive integer'}
	error_found = False
	temp_degree = 0
	skipped = 0
	choice = [['y','yes'],['n','no']]
	chosen = ''

	for i in x.split():

		if i in direction:
			if len(ip_dir)>0:
				error['direction_twice'] = True
			ip_dir = i
			error['direction_not'] = False

		if degree > 0:
			try:
				degree = int(i)	
				error['value_twice'] = True			
			except ValueError:
				if skipped == 0:
					temp_degree,skipped = word_num(x,i)
					if temp_degree != 0:
						degree = temp_degree
						error['value_twice'] = True				

		try:
			degree = int(i)
			error['value_not'] = False
			if degree > max_degree:
				error['value_exceeded'] = True
			if degree < 0:
				error['value_negative']=True
		except ValueError:
			if skipped == 0:
				temp_degree,skipped = word_num(x,i)
				if temp_degree != 0:
					degree = temp_degree
					if degree > 0:
						error['value_not'] = False
						if degree > max_degree:
							error['value_exceeded'] = True
			
		if skipped > 0:
			skipped = skipped - 1

	return direction,direction_send,direction_index_list,ip_dir,degree,error,error_prompts,error_found,choice,chosen

def automation_configuration_program():

	global motor_positions
	
	command_list = []
	log = []
	
	while True:
		my_os.system('clear')
		print('Go on typing the commands that you want to execute serially.\n"q" or "quit" to quit logging and save and exit.\n"t" or "terminate" to quit without saving\n')

		if len(log)!=0 :
			print('Command list:')
			for i in log:
				deg = ''.join(j for j in i[:] if j.isdigit())				
				print('move {0} by {1}'.format(direction[direction_index_list.index(i[0])],deg))
		

		x=raw_input('> ')
		x=x.lower()

		if x in ['q','quit']:
			save = open('automated_config.txt','w')
			content = ''

			for j in command_list:
				content = content + str(j) + '\n'
			save.write(content)
			save.close()
			break
		elif x in ['t','terminate']:
			command_list = []
			break
		else:
			pass

		direction,direction_send,direction_index_list,ip_dir,degree,error,error_prompts,error_found,choice,chosen = input_translation(x)
		
		for i in error.keys():
			if error[i]:
				print(error_prompts[i])
				error_found = True

		if error_found == True:
			raw_input("\n\nPress any key to continue.")
			continue
		
		print("\n\n")

		while True:
			my_os.system('clear')

			if len(log)!=0 :
				print('Command list:')
				my_os.system('clear')
				for i in log:	
					deg = ''.join(j for j in i[:] if j.isdigit())			
					print('move {0} by {1}'.format(direction[direction_index_list.index(i[0])],deg))
				print('\n')
			
			print('Your direction is:',ip_dir,'by',degree,'degrees')
			
			chosen = raw_input("If that's what you intended, type in 'y' or 'yes' to proceed or else 'n' or 'no' to retry.\n> ")
	
			if chosen.lower() in choice[0]:
				motor_in_question = int(direction_index_list.index(direction_send[ip_dir])/2)
								
				#send = str(motor_positions[motor_in_question] + ( degree if  direction_index_list.index(direction_send[ip_dir]) % 2 == 0 else -degree)) + direction_send[ip_dir]
				send = str(degree) + direction_send[ip_dir]

				print("command recorded")
				log.append(ip_dir + str(degree))
				command_list.append(send)
				raw_input()
				break
			elif chosen.lower() in choice[1]:
				print("\n\nWe apologize for misinterpretation. Please try again.")
				raw_input()
				break
			else:
				print('\n\nInvalid choice. Press any key to reply again. ')
				raw_input()
				my_os.system('clear')		

def automated_movement_program():
	import select,sys
	global motor_positions
	x = ''
	direction,direction_send,direction_index_list,ip_dir,degree,error,error_prompts,error_found,choice,chosen = input_translation(x)
	delay = 3
	read_execute = open('automated_config.txt','r')
	my_os.system('clear')
	read = read_execute.readlines()
	read_execute.close()
	while True:
		print('Press any two keys in succession to quit')
		for i in read:			
			print('Sending: {0} to arduino and executing. {1} seconds to wait'.format(i.rstrip(),delay))
			send_to_arduino(i.rstrip())
			deg = int(''.join(j for j in i[:] if j.isdigit()))
			motor_in_question = direction_index_list.index(i.rstrip()[-1])//2
			motor_positions[motor_in_question] = motor_positions[motor_in_question] + (deg if  direction_index_list.index(i.rstrip()[-1]) % 2 == 0 else -deg)			

			a,b,c = select.select([sys.stdin],[],[],delay)
			if (a):
				break
		if (a):
			break			
		my_os.system('clear')
	

def send_to_arduino(send):

	import serial
	import time
	ser = serial.Serial('/dev/ttyACM2', 9600)
	print send
	f = open("automated_config.txt", "w")
	print(send)
	f.write(send)
	f.close()

	f = open("automated_config.txt", "r")
	while 1:
		line = f.readline()
		if not line:
			break
		ser.write(line)
		time.sleep(1)
	f.close()
	#Read this comment: remove pass and type the code for sending data to arduino via the PWM of raspberry pi. Use 'send' (variable sent to this function) as the data
	

def reset_program():
	global motor_positions
	x = ''
	direction,direction_send,direction_index_list,ip_dir,degree,error,error_prompts,error_found,choice,chosen = input_translation(x)
	for i in list(range(5)):
		deviation = motor_positions[i] - 90
		if deviation > 0:
			
			send = str(deviation) + direction_index_list[(2*i)+1]
		elif deviation < 0:
			send = str(deviation + (-2)*deviation) + direction_index_list[2*i]
		else:
			continue
		send_to_arduino(send)
		motor_positions[i]=90
	raw_input('Press any key to quit')
	
def initiation_program():

	global my_os	
	import os as my_os

	global motor_positions
	motor_positions = [90,90,90,90,90]
	
	while True:
		my_os.system('clear')
		main_choice = raw_input('Hello and welcome to our chatbot program.\n"0" for entering in user control mode.\n"1" for editing the automated configuration.\n"2" for intiating the automated movement program.\n"3" to reset the arm to default position\n> ')
		if main_choice.lower() in ['0','zero']:
			user_control_program()
		elif main_choice.lower() in ['1','one']:
			automation_configuration_program()
		elif main_choice.lower() in ['2','two']:
			automated_movement_program()
		elif main_choice.lower() in ['3','three']:
			reset_program()
		else:
			print('Invalid Choice.')
			raw_input()

initiation_program()
