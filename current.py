def current(business_cardlist, page):
    print("현재 명함 정보 조회")
    if page >= 0:
        print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(business_cardlist[page])
    else:
        print('입력된 내용이 없습니다.')