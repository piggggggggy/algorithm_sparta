# 스파르타 알고리즘 강의 2주차 숙제2번문제
# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()
    orders.sort()
    orders = [menus.index(j) + 1 for j in orders]
    menus = [menus.index(i) + 1 for i in menus]
    print(orders)
    print(menus)
    index_min = 0
    index_max = len(menus)-1
    index_mid = (index_min + index_max) // 2
    print(index_mid)
    for i in orders:
        while index_max > index_min:
            if menus[index_mid] == i:
                orders.remove(i)
                print(orders)
                return
            if menus[index_mid] > i:
                index_max = index_mid - 1
            else:
                index_min = index_mid + 1
            index_mid = (index_max + index_min) // 2
            print(index_mid)
    result = 0
    print(orders)
    if len(orders) == 0:
        result = True
    else:
        result = False
    return result
# 이분탐색이 모든 경우에 효율적인 방법은 아니다!@!
# 튜터님은 set을 활용


result = is_available_to_order(shop_menus, shop_orders)
print(result)