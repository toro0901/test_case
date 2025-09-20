# if文課題②

def judge_score(score):
    #80点以上 → 「優秀です」
    if score >= 80:
        print("優秀です")
    #60点以上80点未満 → 「合格です」
    elif score >= 60 and score < 80:
        print("合格です")
    #60点未満 → 「不合格です」
    else:
        print("不合格です")

score = 50
judge_score(score)
