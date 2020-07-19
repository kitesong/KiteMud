import random
from time import sleep


class honor:
    name = "英雄xxxx"
    Deng= 1
    Shengming = 100
    gongji = 2

gName = "土狼"
gDengji = 1
gGongji = 1
gShengming = 10

print("欢迎进入武侠世界！！！！！")
print("正在加载中..............")
sleep(1)
print("-------创建人物--------")
name = input("请输入名称：")
print(name+"欢迎您加入游戏")
print("您的等级："+str(Dengji))
print("您的生命值："+str(Shengming))
print("1.出发，2.等待")
go = input("请选择:")
if go == "1":
    gon=1
else:
    print("日月更替，一切随风而去")
    exit()
print("向前走去。。。。")
print("哈哈哈！！！正饿呢，来了一个吃的！！！")
print("你遇到一个怪物：土狼1只")
print("决定命运：1.战斗 2.逃跑")
go = input("请选择")
if go == "1":
    print("你杀死了"+gName)
else:
    print("你被%s杀死了", gName)
sleep(2)
print("游戏结束了！！！！")


