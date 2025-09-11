def past(business_cardlist, page):  
    print("이전 명함 정보 조회")
    if page <= 0:
        print('첫번째 페이지 입니다.')
        print(business_cardlist[page])
    else:
        page -= 1
        print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(business_cardlist[page])