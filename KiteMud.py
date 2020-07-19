import random
from time import sleep
from KiteMun_opt import *

print("欢迎进入武侠世界！！！！！")
print("正在加载中..............")
sleep(1)
name = input("请输入名称：")
print("-------创建人物--------")
sleep(1)
h1 = Hero()
h1.name = name
print(name + "欢迎您加入游戏")
h1.showAll()

while 1 < 2:
    s1 = selectopt()

    if s1 == 1:
        go1 = random.randint(1, 5)
    elif s1 == 2:
        go1 = random.randint(1, 3)
    elif s1 == 3:
        go1 = random.randint(1, 5)
    else:
        go1 = 0

    if go1 == 0:
        print(h1.name + "打坐休息...")
        sleep(2)
        print(h1.name + "恢复生命值5")

        h1.showAll()
    else:
        gw1 = Monster()
        gw1.setGrade(s1)
        print(h1.name + "移动了10步")
        print("发现一个怪物" + gw1.name)
        gw1.showAll()
        print("-----------------------")
        print("决定命运：1.战斗 2.逃跑")
        go = input("请选择")
        if go == "1":
            while (h1.vVitality > 0) and (gw1.vVitality > 0):
                print(gw1.name + "向你发起攻击..")
                h1.vVitality = h1.vVitality - gw1.vHurt
                print(h1.name+"生命力减"+str(gw1.vHurt))
                h1.showAll()
                print("-----------------------")
                sleep(1)
                opt2 = input("请选择：1攻击；2 逃跑")
                print("-----------------------")
                if opt2 == "1":
                    print(h1.name+"向"+gw1.name+"打出一拳")
                    print("一下命中"+gw1.name)
                    print(gw1.name+"生命值减"+str(h1.vHurt))
                    gw1.vVitality = gw1.vVitality - h1.vHurt
                    print("-----------------------")
                    gw1.showAll()
                    sleep(1)
                    print("-----------------------")
                else:
                    print(gw1.name + "向你发起攻击..")
                    h1.vVitality = h1.vVitality - gw1.vHurt
                    print(h1.name + "生命力减" + str(gw1.vHurt))
                    h1.showAll()
                    print("-----------------------")
                    sleep(1)

                    break
            if gw1.vVitality == 0:
                print(h1.name+"杀死了一只"+gw1.name)
                print(h1.name+"等级加1")
                h1.addGrden()
                h1.showAll()
            if h1.vVitality == 0:
                print(h1.name+"被"+gw1.name+"杀死了！")
                exit()

        else:
            sleep(2)
