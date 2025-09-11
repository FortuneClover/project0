def searching(business_cardlist):
    print("명함 검색")
    find = input("찾으시는 명함의 전화번호를 입력해주세요.")
    for idx, i in enumerate(business_cardlist):
        if i['phone'] == find:
            data = business_cardlist.pop(idx)
            print('{}'.format(data['memo']))
            break