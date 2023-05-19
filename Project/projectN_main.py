import yaml
import os
import time
from GPT3Connect import getAns

name = ""

def getQ(bg, role) :
    return str("배경은 " + bg + " 배경이고, 역할은 " + role + "으로 해줘.")

def getPrompt() :
    f = open("Project/Data/prompt.txt", "r", encoding="UTF-8")
    p = f.readlines()
    f.close()
    return str(p[0])

def check(answer) :
    if ("NPC" in answer and "1" in answer and "2" in answer and "3" in answer and "4" in answer and "스토리" in answer and answer.count("\n") <= 28) :
        return True
    else :
        return False

def asDict(answer) :
    global name
    ans_sp = answer.split("\n")
    _data = {}
    _npcName = ""
    _story = ""
    _quest = {}
    s = 0

    if (not check(answer)) :
        print("error!")
        return False

    try :
        #for s in range(0, len(ans_sp) - 5, 1) :
        while (s <= len(ans_sp) - 5) :
            if (ans_sp[s] != "") :
                #print(ans_sp[s])
                if ("NPC" in ans_sp[s] and "이름" in ans_sp[s]) :
                    _npcName = ans_sp[s].split(":")[1]
                    name = _npcName
                    print(name)
                elif ("스토리" in ans_sp[s] and ans_sp[s].find("스토리") == 0) :
                    _story = ans_sp[s].split(":")[1]
                else :
                    pass
                for i in range(1, 5, 1) :
                    if (("퀘스트" in ans_sp[s] and str(i) in ans_sp[s]) or (ans_sp[s][0] == str(i))) :
                        __quest = {}

                        _Q_1stname = ans_sp[s].split(":")[1]
                        _Q_2ndName = ans_sp[s + 1].split(":")[1]
                        _Q_story = ans_sp[s + 2].split(":")[1]
                        _Q_task = ans_sp[s + 3].split(":")[1]
                        _Q_reward = ans_sp[s + 4].split(":")[1]

                        __quest["제목"] = _Q_1stname
                        __quest["부제"] = _Q_2ndName
                        __quest["내용"] = _Q_story
                        __quest["과제"] = _Q_task
                        __quest["보상"] = _Q_reward

                        _quest["퀘스트" + str(i)] = __quest
                    if (i == 4) :
                        break
            s += 1
    except :
        print("error!")
        return False
    
    _data["이름"] = _npcName
    _data["스토리"] = _story
    _data["퀘스트"] = _quest

    return _data

def save(strs) :
    now = time
    time_format = "%y%m%d_%H%M%S"

    """
    hr = str(now.localtime().tm_hour)
    min = str(now.localtime().tm_min)
    sec = str(now.localtime().tm_sec)
    if (len(hr) == 1) :
        hr = "0" + hr
    if (len(min) == 1) :
        min = "0" + min
    if (len(sec) == 1) :
        sec = "0" + sec
    fn = "Project/Logs/log_" + hr + "_" + min + "_" + sec + ".log"
    """
    fn = "Project/Logs/log_" + time.strftime(time_format, now.localtime()) + ".log"
    f3 = open(fn, "w", encoding="UTF-8")

    for i in strs.split("\n") :
        f3.writelines(i)
        f3.writelines("\n")

    print("log saved! " + f3.name)

    f3.close()

def saveAsTxt(string, FileName) :
    f1 = open(FileName + "/" + name + ".txt", "w", encoding="UTF-8")

    for i in string.split("\n") :
        f1.writelines(i)
        f1.writelines("\n")

    print("file saved as TXT! " + f1.name)

    f1.close()

def saveAsYaml(dictionary, FileName) :
    f2 = open(FileName + "/" + name + ".yml", "w", encoding="UTF-8")

    with open(FileName + "/" + name + ".yml", "w", encoding="UTF-8") as f:
        yaml.dump(dictionary, f, default_flow_style=False, allow_unicode=True)
        
    print("file saved as YAML! " + f2.name)

    f2.close()

def run(backGround, role) :
    print("Generating....")

    prompt = getPrompt()
    question = getQ(backGround, role)
    #question = getQ("판타지", "왕실 직속 기사")

    #print("prompt : " +  prompt, end = "\n================================================\n")
    #print("question : " + question, end = "\n================================================\n")

    ans = getAns(prompt, question)
    #print(ans)

    save(ans)

    dt = asDict(ans)
    if (dt == False) :
        print("Error! regenerating...!")
        run(backGround, role)
        return
    else :
        pass
    #print(dt)

    FileName = "Project/Data/" + name
    try :
        if not os.path.exists(FileName) :
            os.mkdir(FileName)
    except OSError :
        print("ERROR")

    saveAsTxt(ans, FileName)

    saveAsYaml(dt, FileName)

    print("complete!")

    return dt

"""

backG = str(input("배경을 입력하세요 : "))
role = str(input("역할을 입력하세요 : "))

run(backG, role)
"""