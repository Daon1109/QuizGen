
import ast
import pandas as pd


def dictreturn():
    maindict = []
    with open('C:/Coding/doodles/QuizGen/templates/data.txt', 'r', encoding='utf-8') as f:
        raw = f.readlines()
    if pd.DataFrame(raw).empty:
        return []
    else:
        for line in raw:
            line = line.rstrip(',\n')
            if line.strip():  # 빈 줄 방지
                maindict.append(ast.literal_eval(line))       #문자열 생긴 거 그대로 맞는 자료형으로 변환(여기선 dict)
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
            pre_input = {"id":int(ex_dict[len(ex_dict)-1]["id"])+1, "hanja":spl_result[id][0], "huneum":spl_result[id][1], "O":0, "X":0, "finalstat":"N", "uTime":0}     # dictionary form
        ex_dict.append(pre_input)
    for fi in range(len(ex_dict)):
        if fi==0:
            f.write(str(ex_dict[fi]))
            #result = result+str(ex_dict[fi])
        else:
            f.write(',\n'+str(ex_dict[fi]))
            #result = result+',\n'+str(ex_dict[fi])
    f.close()
