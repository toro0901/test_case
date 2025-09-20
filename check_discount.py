#if文課題③

def check_discount(price):
    if price >= 10000:
        return "20%割引"
    elif price >= 5000 and price <10000:
        return "10%割引"
    else:
        return "割引なし"

print(check_discount(11000)) #20%割引
print(check_discount(7000)) #10%割引
print(check_discount(4500)) #割引なし