#if文課題①

def check_age(age):
    if age >= 18:
        return "大人です"
    else:
        return "未成年です"

print(check_age(19)) #大人です
print(check_age(17)) #未成年です
