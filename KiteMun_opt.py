import random


class Hero:
    name = "英雄xxxx"
    vGrade = 1  # 等级
    vVitality = 100  # 生命力
    vHurt = 10  # 攻击力

    def show(self):
        print(name + "的生命值" + str(self.vVitality))

    def showAll(self):
        print("----" + self.name + "----")
        print("等级：" + str(self.vGrade))
        print("生命力：" + str(self.vVitality))
        print("攻击力：" + str(self.vHurt))

    def addGrden(self):
        self.vGrade = self.vGrade + 1
        self.vVitality = self.vVitality+10
        self.vHurt = self.vHurt+2


class Monster:
    name = "土狼" + str(random.randint(1001, 20001))
    vGrade = 1  # 等级
    vVitality = 100  # 生命力
    vHurt = 1 # 攻击力

    def show(self):
        print(name + "的生命值" + str(self.vVitality))

    def setGrade(self, i):
        self.vGrade = i
        self.vVitality = i * 20
        self.vHurt = (i * 2)

    def showAll(self):
        print("----" + self.name + "----")
        print("等级：" + str(self.vGrade))
        print("生命力：" + str(self.vVitality))
        print("攻击力：" + str(self.vHurt))



def selectopt():
    print("请选择：1 向前走；2.向左走；3向右走.4.打坐休息")
    s1 = input("请选择：")
    return int(s1)
