# import re
business_cardlist=[{'name': 'hong', 'gender': 'M', 'email': 'hong@gmail.com', 'company': 'S'},
          {'name': 'kim', 'gender': 'F', 'email': 'kim@gmail.com', 'company': 'A'},
          {'name': 'lee', 'gender': 'M', 'email': 'lee@gmail.com', 'company': 'B'},
          {'name': 'han', 'gender': 'F', 'email': 'han@gmail.com', 'company': 'C'}]
page=3

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 명함 정보 입력
    C - 현재 명함 정보 조회
    P - 이전 명함 정보 조회
    N - 다음 명함 정보 조회
    U - 명함 정보 수정
    D - 명함 정보 삭제
    Q - 프로그램 종료
    ''').upper() 

    if choice=="I":        
        print("명함 정보 입력")
        card={'name':'','phone':'',"email":'',"company":''}
        card['name'] = input('이름 >>> ')

        while True:
            card['phone'] = input('성별(M,F) >>> ').upper()
            if card['phone'] in ('M','F'):
                break

        while True:
            card['email'] = input('email >>> ')
            check = 0
            for item in business_cardlist:
                if item['email'] == card['email']:
                    check=1
                    break
            if check == 0 :
                break  
            print('중복되는 이메일이 있습니다.')  

        while True:
            card['company'] = input('회사명 ')
            if card['company'].isdigit() and len(card['company']) == 4 :
                card['company'] = int(card['company'])
                break

        print(card)
        business_cardlist.append(card)
        print(business_cardlist)
        page = len(business_cardlist)-1

    elif choice=="C":
        print("현재 명함 정보 조회")
        if page >= 0:
            print('현재 페이지는 {}페이지 입니다.'.format(page+1))
            print(business_cardlist[page])
        else:
            print('입력된 내용이 없습니다.')
        
    elif choice == 'P':
        print("이전 명함 정보 조회")
        if page <= 0:
            print('첫번째 페이지 입니다.')
            print(business_cardlist[page])
        else:
            page -= 1
            print('현재 페이지는 {}페이지 입니다.'.format(page+1))
            print(business_cardlist[page])
    elif choice == 'N':
        print("다음 명함 정보 조회")
        if page >= len(business_cardlist)-1:
            print('마지막 페이지입니다.')
            print(business_cardlist[page])
        else:
            page += 1
            print("현재 페이지는 {}쪽 입니다".format(page + 1))
            print(business_cardlist[page])
    elif choice=='D':
        print("명함 정보 삭제")
        email = input('삭제하려는 명함의 이메일을 입력하세요 >>> ').strip()
        delok = 0
        for idx,i in enumerate(business_cardlist):
            if i['email'] == email:
                data = business_cardlist.pop(idx)
                print('{}님의 정보가 삭제되었습니다.'.format(data['name']))
                delok=1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
        print(business_cardlist)
        page = len(business_cardlist)-1
    elif choice=="U": 
        print("명함 정보 수정")
        while True:
            choice1=input('수정하시려는 명함 정보의 이메일을 입력하세요 : ') # 이메일 존재 여부 체크 필요
            idx=-1
            for i in range(0,len(business_cardlist)):
                if business_cardlist[i]['email'] == choice1:
                    idx=i
            if idx==-1:
                print('등록되지 않은 이메일입니다.')       
                break
                        
            choice2=input('''
            다음 중 수정하실 정보를 골라주세요 
                    name, gender, company
            (수정할 정보가 없으면 'exit' 입력)
            ''')
            if choice2 in ('name','gender','company'):
                business_cardlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                break
            elif choice2 =='exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break
    elif choice=="Q":
        print("프로그램 종료")
        break