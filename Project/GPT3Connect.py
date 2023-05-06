import openai

def getAns(condition, Q) :
    f = open("Project/Data/ApiKey.txt", "r", encoding="UTF-8")
    openai.api_key = f.readline()
    f.close()
    result = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "system", "content" : condition},
            {"role" : "user", "content" : Q}
        ]
    )
    #print(result['choices'][0]['message']['content'])
    return (result['choices'][0]['message']['content'])


""" 

@deprecated
c = "넌 지금부터 내가 알려주는 배경과 역할에 따라 게임 NPC의 이름과 스토리, 그리고 역할에 따른 퀘스트 (배경, 역할과 관련있는 물품(물품 이름도 배경에 맞게 지어줘, 가져와야 하는 물품 개수와 그 물품을 어떻게 구할 수 있는지도)을 모아오기 또는 배경, 역할과 관련있는 무언가(몬스터나 적대적인 생명체도 괜찮고, 동물 사냥도 좋아. 다만 그걸 배경에 따라 이름을 명시해서 정확하게 작성해줘. 그리고 배경에 따라 어디서 그 무언가를 잡을 수 있는지도 작성해 줘야 해.)를 몇마리 잡아오기)를 작성해 주면 돼. 퀘스트를 완료했을때 그에 따른 보상도 작성해줘. 보상은 NPC의 직업과 퀘스트의 내용과 관련이 있어야 하고, 어떤 아이템을 몇개, 그리고 그 아이템의 종류(사용 아이템, 장비(갑옷 등), 무기, 기타 아이템 등..)도 작성해 줘야 해. 또한, 퀘스트 보상에는 경험치또한 아이템과 같이 주어야만 해. 그리고 퀘스트 보상에는 돈이 포함될 수 있어. 예상되는 퀘스트의 난이도에 따른 적당한 양의 재화를 추가해 줬으면 좋겠어. 형식은 NPC 이름 : 이름, 스토리 : 스토리, 퀘스트 : \n 퀘스트1이름 : 내용 : 태스크 : 보상 / \n 퀘스트2이름 : 내용 : 태스크 : 보상 .. 의 형식으로 작성해주면 될 것 같아. 한번의 대답에는 한명의 NPC만 작성해야만 하고, 퀘스트는 4개가 되어야 해. 스토리에 잘 어울리고 퀘스트와 역할 사이가 자연스러우면 고마울 것 같아."
bg = "판타지"
role = "사냥꾼"
q = "배경은 " + bg + " 배경이고, 역할은 " + role + "으로 해줘."

getAns(c, q)
"""