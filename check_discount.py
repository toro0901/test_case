#if文課題③

def check_discount(price):
    #10000円以上 → 「20%割引」
    if price >= 10000:
        print("20%割引")
    #5000円以上10000円未満 → 「10%割引」
    elif price >= 5000 and price <10000:
        print("10%割引")
    #5000円未満 → 「割引なし」
    else:
        print("割引なし")

price = 4000
check_discount(price)
