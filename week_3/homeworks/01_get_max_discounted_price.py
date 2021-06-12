# 스파르타 알고리즘 강의 3주차 숙제1번문제
# Q.
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

shop_prices = [50000, 1500000]
user_coupons = []


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    sum_price = 0
    if len(prices) >= len(coupons):
        for i in range(len(coupons)):
            sum_price += prices[i] * (100-coupons[i])/100
        result = sum_price + sum(prices[len(coupons):])
    else:
        for j in range(len(prices)):
            sum_price += prices[j] * (100-coupons[j])/100
        result = sum_price
    return int(result)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.