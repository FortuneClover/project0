# import re
business_cardlist=[{'name': 'hong', 'phone': '000-0000-0000', 'email': 'hong@gmail.com', 'company': 'S', 'memo' : list('work on S')},
          {'name': 'kim', 'phone': '111-1111-1111', 'email': 'kim@gmail.com', 'company': 'A', 'memo' : list('work on A')},
          {'name': 'lee', 'phone': '222-2222-2222', 'email': 'lee@gmail.com', 'company': 'B', 'memo' : list('work on B')},
          {'name': 'han', 'phone': '333-3333-3333', 'email': 'han@gmail.com', 'company': 'C', 'memo' : list('work on C')}]
page=3

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 명함 정보 입력
    C - 현재 명함 정보 조회
    P - 이전 명함 정보 조회
    N - 다음 명함 정보 조회
    F - 명함 검색
    D - 명함 정보 삭제
    M - 명함 메모 추가
    Q - 프로그램 종료
    ''').upper() 

    if choice=="I":        
        print("명함 정보 입력")
        card={'name':'','phone':'',"email":'',"company":'', "memo" : list()}
        card['name'] = input('이름 >>> ')

        while True:
            card['phone'] = input('phone number >>> ')
            if len(card['phone']) == 13 :
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

        card['company'] = input('회사명 ')
        card['memo'] = input('메모 ')
        

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

    elif choice == 'F':
        print("명함 검색")
        find = input("찾으시는 명함의 전화번호를 입력해주세요.")
        for idx, i in enumerate(business_cardlist):
            if i['phone'] == find:
                data = business_cardlist.pop(idx)
                print('{}'.format(data['memo']))
                break
            

    elif choice=='D':
        print("명함 정보 삭제")
        phone = input('삭제하려는 명함의 전화번호를 입력하세요 >>> ').strip()
        delok = 0
        for idx,i in enumerate(business_cardlist):
            if i['phone'] == phone:
                data = business_cardlist.pop(idx)
                print('{}님의 정보가 삭제되었습니다.'.format(data['phone']))
                delok=1
                break
        if delok == 0:
            print('등록되지 않은 전화번호입니다.')
        print(business_cardlist)
        page = len(business_cardlist)-1
    elif choice=="M": 
        print("명함 메모 추가")
        while True:
            choice1=input('수정하시려는 명함 정보의 전화번호를 입력하세요 : ')
            idx=-1
            for i in range(0,len(business_cardlist)):
                if business_cardlist[i]['email'] == choice1:
                    idx=i
            if idx==-1:
                print('등록되지 않은 전화번호입니다.')       
                break
                        
            business_cardlist[idx]["memo"].append(input('수정할 메모의 내용을 입력하세요 :'))
            
    elif choice=="Q":
        print("프로그램 종료")
        break