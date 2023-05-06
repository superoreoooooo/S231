import yaml
from GPT3Connect import getAns

def getQ(bg, role) :
    return str("배경은 " + bg + " 배경이고, 역할은 " + role + "으로 해줘.")

def getPrompt() :
    f = open("Project/Data/prompt.txt", "r", encoding="UTF-8")
    p = f.readlines()
    f.close()
    return str(p[0])

def asDict(answer) :
    ans_sp = answer.split("\n")
    _data = {}
    _npcName = ""
    _story = ""
    _quest = {}
    for s in range(0, len(ans_sp) - 3, 1) :
        if (ans_sp[s] != "") :
            #print(ans_sp[s])
            if ("NPC" in ans_sp[s] and "이름" in ans_sp[s]) :
                _npcName = ans_sp[s].split(":")[1]
            elif ("스토리" in ans_sp[s] and ans_sp[s].find("스토리") == 0) :
                _story = ans_sp[s].split(":")[1]
            else :
                pass
            for i in range(1, 5, 1) :
                if ("퀘스트" in ans_sp[s] and str(i) in ans_sp[s]) :
                    __quest = {}
                    _Q_1stname = ""
                    _Q_2ndName = ""
                    _Q_story = ""
                    _Q_task = ""
                    _Q_reward = ""

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
    
    _data["이름"] = _npcName
    _data["스토리"] = _story
    _data["퀘스트"] = _quest

    return _data

prompt = getPrompt()
question = getQ("판타지", "왕실 직속 기사")

print("prompt : " +  prompt, end = "\n================================================\n")
print("question : " + question, end = "\n================================================\n")

ans = getAns(prompt, question)

dt = asDict(ans)
print(dt)

with open("Project/Data/result.yml", "w") as f:
    yaml.dump(dt, f, default_flow_style=False, allow_unicode=True)

f1 = open("Project/Data/text.txt", "w")

ans_split = ans.split("\n")

for i in ans_split :
    f1.writelines(i)
    f1.writelines("\n")

print("file saved!" + f1.name)

f1.close()