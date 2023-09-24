# 猜拳游戏
from random import *
print('猜拳游戏！')
ssc_dict = {'剪刀': 1, '石头': 2, '布': 3}    # 玩家字典
gtb_dict = {v: k for k, v in ssc_dict.items()}    # 电脑字典
while True:
    computer = randrange(1, 4)    # 电脑随机出拳
    gamer = input('请猜拳：')
    if gamer not in ssc_dict:
        print('只能出剪刀，石头，布，请重新猜拳！')
        continue
    print(f'电脑：{gtb_dict[computer]} 你：{gamer}')
    if abs(computer - ssc_dict[gamer]) == 2:
        if computer > ssc_dict[gamer]:
            computer = 0
        else:
            computer = 4
    if ssc_dict[gamer] > computer:
        print('你赢了！')
    elif ssc_dict[gamer] == computer:
        print('平局，继续！')
        continue
    else:
        print('你输了！')
