import time

action_time = 0
A_time = 0
B_time = 0
C_time = 0
print("안녕하세요, 전원을 켜시려면 '1'을 입력해주세요.")
print("전원을 켜지 않고 종료하시려면, '0'번을 입력해주세요.")
select_1 = int(input("숫자를 입력해주세요: "))
while True:
	if select_1 == 0:
		print("프로그램을 종료합니다.")
		break;
	elif (select_1 == 1):
		print("전원이 켜집니다.")
		print("A/B/C 기능별 동작 시간을 설정해주세요.(최대 10초)\n")
		while True:
			A_time = int(input("기능 A: (초)"))
			if A_time > 10:
				print("시간은 최대 10초까지 설정 가능합니다.")
				continue;
			elif A_time == 0:
				print("시간은 0초 이상 설정하셔야 합니다.")
				continue;
			else: 
				print("시간이 설정되었습니다. 입력된 시간은",A_time,"초 입니다.\n")
			break;
		while True:
			B_time = int(input("기능 B: (초)"))
			if B_time > 10:
				print("시간은 최대 10초까지 설정 가능합니다.")
				continue;
			elif B_time == 0:
				print("시간은 0초 이상 설정하셔야 합니다.")
				continue;
			else: 
				print("시간이 설정되었습니다. 입력된 시간은",B_time,"초 입니다.\n")
			break;
		while True:
			C_time = int(input("기능 C: (초)"))
			if C_time > 10:
				print("시간은 최대 10초까지 설정 가능합니다.")
				continue;
			elif C_time == 0:
				print("시간은 0초 이상 설정하셔야 합니다.")
				continue;
			else: 
				print("시간이 설정되었습니다. 입력된 시간은",C_time,"초 입니다.\n")
			break;
		time.sleep(1)
		print ("A,B,C 기능에 대한 시간 설정이 완료됐습니다.\n설정된 시간은 다음과 같습니다.")
		print ("1. 기능A:",A_time)
		print ("2. 기능B:",B_time)
		print ("3. 기능C:",C_time)
		select_2 = int(input("기능을 작동시키려면 '1'을 입력해주세요.\n'0'을 누르면 이전 단계로 돌아갑니다."))
		if select_2 == 0:
			continue;
		elif select_2 == 1:
			print ("기능 A가 동작합니다.")
			while True:
				print ("남은 시간은",A_time-action_time,"초 입니다.")
				time.sleep(1)
				action_time += 1
				if action_time == A_time:
					break;	
			action_time = 0	
			print ("기능 B가 동작합니다.")
			time.sleep(1)
			while True:
				print ("남은 시간은",B_time-action_time,"초 입니다.")
				time.sleep(1)
				action_time += 1
				if action_time == B_time:
					break;	
			action_time = 0	
			print("기능 C가 동작합니다.")
			time.sleep(1)
			while True:
				print ("남은 시간은",C_time-action_time,"초 입니다.")
				time.sleep(1)
				action_time += 1
				if action_time == C_time:
					break;	
			print("모든 기능이 동작을 종료 했습니다.. 프로그램을 종료합니다.")
			break;
	else:
		print("잘못된 입력입니다. 다시 입력해주세요.")
	