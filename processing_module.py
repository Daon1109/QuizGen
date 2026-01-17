
import ast
import pandas as pd


def dictreturn():
    maindict = []
    with open('C:/Coding/doodles/QuizGen/templates/data.txt', encoding="utf-8") as f:
        if pd.DataFrame(f).empty:   # 파일 비었는지 확인
            return []
        else:
            raw = f.read().split('\n')
    for i in range(len(raw)):
        raw[i] = raw[i].rstrip(',')
        maindict.append(ast.literal_eval(raw[i]))       #문자열 생긴 거 그대로 맞는 자료형으로 변환(여기선 dict)
    return maindict

def dictionerizer(ex_dict, textinput):
    # append dictionary to raw list
    spl_result = []
    tplant_list = []
    for dct in ex_dict:
        tplant_list = [dct["hanja"], dct["huneum"]]
        spl_result.append(tplant_list)
    rememberNkill=len(ex_dict)

    # spliting process
    spl_temp = textinput.split(', ')
    for i in range(len(spl_temp)):
        spl_result.append(spl_temp[i].split(' ', 1))

    # delete duplicated ones
    hanja_num=len(spl_result)
    j=0
    while j < hanja_num:
        k=j
        while k < hanja_num:
            print(f"{j}, {k}, {len(spl_result)}")
            if j == k:
                k=k+1
            else:
                if spl_result[j][0] == spl_result[k][0]:            # delete k
                    if spl_result[j][1] == spl_result[k][1]:
                        del spl_result[k:k+1]
                        hanja_num=hanja_num-1
                    else:           # 이거 웹 쪽에서 다시 받아서 처리해야 함(한자 중복하지만 뜻 중복 안하는 경우)
                        
                        return "data_already_exist"
                else:
                    k=k+1
        j=j+1
    # to inherit dictionary
    for kl in range(rememberNkill):
        del spl_result[0:1]

    # append to data file(dict type)
    f = open("C:/Coding/doodles/QuizGen/templates/data.txt", 'w', encoding='utf-8')
    for id in range(len(spl_result)):
        if ex_dict==[]:
            pre_input = {"id":1, "hanja":spl_result[id][0], "huneum":spl_result[id][1], "O":0, "X":0, "finalstat":"N", "uTime":0}     # dictionary form
        else:
            pre_input = {"id":int(ex_dict[len(ex_dict)-1]["id"])+1, "hanja":spl_result[id][0], "huneum":spl_result[id][1], "O":0, "X":0, "uTime":0}     # dictionary form
        ex_dict.append(pre_input)
    for fi in range(len(ex_dict)):
        if fi==0:
            f.write(str(ex_dict[fi]))
            #result = result+str(ex_dict[fi])
        else:
            f.write(',\n'+str(ex_dict[fi]))
            #result = result+',\n'+str(ex_dict[fi])
    f.close()
    





'''
# test
di = [
    {"id":1, "hanja":"前", "huneum":"앞 전", "O":4, "X":1, "uTime":10},
    {"id":2, "hanja":"張", "huneum":"베풀 장", "O":3, "X":2, "uTime":10},
    {"id":3, "hanja":"雙", "huneum":"두 쌍", "O":2, "X":5, "uTime":10},
    {"id":4, "hanja":"及", "huneum":"미칠 급", "O":3, "X":4, "uTime":10}
    ]
txt = "前 앞 전, 張 베풀 장, 雙 두 쌍, 及 미칠 급, 前 앞 전, 張 베풀 장, 俚 속될 리, 前 앞 전, 張 베풀 장, 雙 두 쌍, 及 미칠 급, 俚 속될 리, 前 앞 전, 張 베풀 장, 在 있을 재, 惑 미혹할 혹, 六 여섯 육, 藝 재주 예, 妍 고울 연, 憂 근심 우, 薄 엷을 박, 斯 이 사, 流 흐를 류, 淺 얕을 천, 貧 가난할 빈, 矣 어조사 의"
afed = ""

dictionerizer([], txt)
'''

#print(dictreturn())