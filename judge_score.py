# if文課題②

def judge_score(score):
    if score >= 80:
        return "優秀です"
    elif score >= 60 and score < 80:
        return"合格です"
    else:
        return "不合格です"

print(judge_score(90)) #優秀です
print(judge_score(75)) #合格です
print(judge_score(55)) #不合格です
