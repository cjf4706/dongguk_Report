print("안녕하세요, 전원을 켜시려면 '1'을 입력해주세요.")
print("전원을 켜지 않고 종료하시려면, '0'번을 입력해주세요.")
select_1 = int(input("숫자를 입력해주세요: "))
while True:
	if select_1 == 0:
		print("프로그램을 종료합니다.")
		break;
	elif (select_1 == 1):
		print("전원이 켜집니다.")
		break;
	else:
		print("잘못된 입력입니다. 다시 입력해주세요.")
		break;
//각 문단에 Break를 적용하지 않으면 무한루프가 발생
//WHile 문이 동작하는 조건을 수정해 봐야겠음