from PublicReference.base import *

# 2020.6.25 数据有待修正 
# 2020.8.14 添加韩服新护石
#           爆弹罗网添加跳跃释放选项
# 2020.8.20 修正覆灭之枪护石提升


# 武器重剑
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '重剑':
#             return round(self.CD / self.恢复 * 1.1, 1)
            


# 重剑精通
class 巅峰狂徒技能0(被动技能):
    名称 = '重剑精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(1.25 + 0.025 * (self.等级 - 20), 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)
        



# 火药改良
class 巅峰狂徒技能1(被动技能):
    名称 = '火药改良'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        return round(1 + 0.015 * self.等级, 5)


# 一觉被动
class 巅峰狂徒技能2(被动技能):
    名称 = '终极火力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.02 * self.等级, 5)


# 二觉被动
class 巅峰狂徒技能3(被动技能):
    名称 = '无法者之歌'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
class 巅峰狂徒技能4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 超卓之心
class 巅峰狂徒技能5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


# 觉醒之抉择
class 巅峰狂徒技能6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

# 双重散射
class 巅峰狂徒技能7(主动技能):
    名称 = '双重散射'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 2
    基础 = 1725.5 - 攻击段数 * 0.5
    成长 = 195.9
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


# 爆裂斩击
class 巅峰狂徒技能8(主动技能):
    名称 = '爆裂斩击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    攻击段数 = 2
    基础 = 1962.4 - 攻击段数 * 0.5
    成长 = 221.3
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


# 剑刃爆弹
class 巅峰狂徒技能9(主动技能):
    名称 = '剑刃爆弹'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 11
    基础 = 4061.333333 - 攻击段数 * 0.5
    成长 = 451
    CD = 12
    TP成长 = 0.10
    TP上限 = 5

#广域散射
class 巅峰狂徒技能10(主动技能):
    名称 = '广域散射'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    攻击段数 = 1
    基础 = 3084 - 攻击段数 * 0.5
    成长 = 351
    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    
# G型火焰爆弹
class 巅峰狂徒技能11(主动技能):
    名称 = 'G型火焰爆弹'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    攻击段数 = 8
    基础 = 3568.333333 - 攻击段数 * 0.5
    成长 = 392
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


# 爆裂斩
class 巅峰狂徒技能12(主动技能):
    名称 = '爆裂斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    攻击段数 = 3
    基础 = 6713.333333 - 攻击段数 * 0.5
    成长 = 757
    CD = 15
    TP成长 = 0.10
    TP上限 = 5


# 爆弹罗网
class 巅峰狂徒技能13(主动技能):
    名称 = '爆弹罗网'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    
    基础 = 425.8333333 + 57.33333333 * 7 - 0.5 * 8
    成长 = 48.5 + 7 * 7
    攻击次数 = 1
    
    基础2 = 1278.833333  - 0.5
    成长2 = 145.5
    攻击次数2 = 6
   

    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 2 * 3.5 #描述错误
        elif x == 1:
            self.攻击次数2 = 2 * 3.8 #描述错误，改动位置

# 裂地爆刃
class 巅峰狂徒技能14(主动技能):
    名称 = '裂地爆刃'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    攻击段数 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1


    基础 = 9551 - 攻击段数 * 0.5
    成长 = 1076


    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.92
            self.倍率 *= 1.24
        elif x == 1:
            self.CD *= 0.92
            self.倍率 *= 1.24*1.07#改动位置，待测试

# 惊喜大礼
class 巅峰狂徒技能15(主动技能):
    名称 = '惊喜大礼'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    攻击段数 = 6
    基础 = 17084 - 攻击段数 * 0.5
    成长 = 1935
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.89
            self.倍率 *= 1.07
        elif x == 1:
            self.CD *= 0.89
            self.倍率 *= 1.15#改动位置


# 一觉
class 巅峰狂徒技能16(主动技能):
    名称 = 'G型烬灭榴弹'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    攻击段数 = 13
    基础 = (34765.84762 - 攻击段数 * 0.5) * 1.1
    成长 = 10495.17143  * 1.1#三级效果，忘了补上
    CD = 145


# 完美击球
class 巅峰狂徒技能17(主动技能):
    名称 = '完美击球'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1


    基础 = 3581 - 0.5
    成长 = 403
    攻击次数 = 1

    基础2 = 8329.666667 - 0.5
    成长2 = 941.5
    攻击次数2 = 1

    护石状态 = 0


    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 0
            self.倍率 = 1.24
            self.护石状态 = 1
        elif x == 1:
            self.攻击次数2 = 0
            self.倍率 = 1.34#改动位置，具体待测试
            self.护石状态 = 1

    def 等效CD(self, 武器类型,输出类型):
        if self.护石状态 == 0:
            return round(self.CD  / self.恢复, 1)
        else:
            return round(8.3 * 0.88, 1)
        
# 夺命焰火

class 巅峰狂徒技能18(主动技能):
    名称 = '夺命焰火'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    
    基础 = 5074.6 + 7612.2 - 1
    成长 = 573 + 859.5
    攻击次数 = 1

    基础2 = 3167.6 - 0.5
    成长2 = 358.3
    攻击次数2 = 4

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.1
            self.攻击次数2 *= 1.23
        elif x == 1:
            self.攻击次数 *= 1.1
            self.攻击次数2 *= 1.39#改动位置，具体待测试
 
# 爆弹华尔兹
class 巅峰狂徒技能19(主动技能):
    名称 = '爆弹华尔兹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 5462.7
    成长 = 617.7
    攻击次数 = 3

    基础2 = 4920.2
    成长2 = 555.7
    攻击次数2 = 5

    CD = 40
    
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 += 3
            self.倍率 *= 1.38
            self.CD *=0.9
# 覆灭之枪
class 巅峰狂徒技能20(主动技能):
    名称 = '覆灭之枪'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    攻击段数 = 1
    基础 = 50430.8 - 攻击段数 * 0.5
    成长 = 5693.7
    CD = 50

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.40
# 二觉
class 巅峰狂徒技能21(主动技能):
    名称 = '终焉：硝烟狂欢'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    攻击段数 = 17
    基础 = 88115.33333 - 攻击段数 * 0.5
    成长 = 26597.5
    CD = 180


巅峰狂徒技能列表 = []
i = 0
while i >= 0:
    try:
        exec('巅峰狂徒技能列表.append(巅峰狂徒技能' + str(i) + '())')
        i += 1
    except:
        i = -1

巅峰狂徒技能序号 = dict()
for i in range(len(巅峰狂徒技能列表)):
    巅峰狂徒技能序号[巅峰狂徒技能列表[i].名称] = i

巅峰狂徒一觉序号 = 0
巅峰狂徒二觉序号 = 0
巅峰狂徒三觉序号 = 0
for i in 巅峰狂徒技能列表:
    if i.所在等级 == 50:
        巅峰狂徒一觉序号 = 巅峰狂徒技能序号[i.名称]
    if i.所在等级 == 85:
        巅峰狂徒二觉序号 = 巅峰狂徒技能序号[i.名称]
    if i.所在等级 == 100:
        巅峰狂徒三觉序号 = 巅峰狂徒技能序号[i.名称]

巅峰狂徒护石选项 = ['无']
for i in 巅峰狂徒技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        巅峰狂徒护石选项.append(i.名称)

巅峰狂徒符文选项 = ['无']
for i in 巅峰狂徒技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        巅峰狂徒符文选项.append(i.名称)


class 巅峰狂徒角色属性(角色属性):
    实际名称 = '巅峰狂徒'
    角色 = '枪剑士'
    职业 = '战线佣兵'

    武器选项 = ['重剑']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 2.0
    
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(巅峰狂徒技能列表)
        self.技能序号 = deepcopy(巅峰狂徒技能序号)

class 巅峰狂徒(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 巅峰狂徒角色属性()
        self.角色属性A = 巅峰狂徒角色属性()
        self.角色属性B = 巅峰狂徒角色属性()
        self.一觉序号 = 巅峰狂徒一觉序号
        self.二觉序号 = 巅峰狂徒二觉序号
        self.三觉序号 = 巅峰狂徒三觉序号
        self.护石选项 = deepcopy(巅峰狂徒护石选项)
        self.符文选项 = deepcopy(巅峰狂徒符文选项)

    def 护石判断(self):
        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '爆弹罗网':
                sign = 1
        if sign == 0:
            self.爆弹罗网护石跳跃选项.setEnabled(False)
            self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)
            self.爆弹罗网护石跳跃选项.setChecked(False)
        else:
            self.爆弹罗网护石跳跃选项.setEnabled(True)
            self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())
        self.爆弹罗网护石跳跃选项=QCheckBox('爆弹罗网护石跳跃释放',self.main_frame2)
        self.爆弹罗网护石跳跃选项.resize(140,20)
        self.爆弹罗网护石跳跃选项.move(320,360)
        self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)
        self.爆弹罗网护石跳跃选项.setToolTip('跳跃释放爆弹罗网，仅佩戴护石时生效')

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           if int(setfile[0].replace('\n', '')) == 1:
              self.爆弹罗网护石跳跃选项.setChecked(True)
           else:
              self.爆弹罗网护石跳跃选项.setChecked(False)
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            if self.爆弹罗网护石跳跃选项.isChecked():
               setfile.write('1\n')
            else:
               setfile.write('0\n')
        except:
            pass


    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.爆弹罗网护石跳跃选项.isChecked():
            属性.技能栏[属性.技能序号['爆弹罗网']].攻击次数 = 0
        

