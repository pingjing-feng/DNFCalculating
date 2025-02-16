from math import *
from PublicReference.base import *


# 武器巨剑
class 职业主动技能(主动技能):

    data0 = []
    data1 = []
    data2 = []
    data3 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    #def 等效CD(self, 武器类型):
        #if 武器类型 == '巨剑':
            #return round(self.CD / self.恢复 * 1.1, 1)

# 骑士信念
class 技能0(被动技能):
    名称 = '骑士信念'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    冷却关联技能=['所有']
    非冷却关联技能 = ['天马流星落','暮光之灵黄昏独角兽','生命之律·神木擎天']
    def CD缩减倍率(self,武器类型):
        return 0.9

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

# 一觉被动 由于一觉二觉主动不受剑盾猛攻连锁BUFF加成，所以这里有个额外的加成，这个一绝被动加成吃两次
# 例如：一绝被动=1.42，二觉受到的加成为1.42*1.42
class 技能1(被动技能):
    名称 = '自然恩泽'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['天马流星落','暮光之灵黄昏独角兽','生命之律·神木擎天']


    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00+0.02 * self.等级, 5)
    def 加成倍率2(self,武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00+0.02 * self.等级, 5)

# 二觉被动
class 技能2(被动技能):
    名称 = '信仰鼓舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

# 剑盾猛攻 一级默认13%，但测试实际为12.5%，游戏内显示每2级提高1%，但测试伤害实际为每级0.5%
# 剑盾猛攻本身不受剑盾猛攻连锁BUFF加成，一二觉也不受加成，剑盾强袭加成=（剑盾猛攻加成+5%）*连锁层数
class 技能3(职业主动技能):
    名称 = '剑盾猛攻'
    所在等级 = 30
    等级上限 = 16
    基础等级 = 6
    # 基础 = 906.4
    # 成长 = 273.6
    #挥盾物理攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 1180, 1453, 1727, 2000, 2274, 2548, 2821, 3095, 3369, 3642, 3916, 4190, 4463, 4737, 5010, 5284, 5558, 5831, 6105, 6379]]
    #推进物理攻击力：<data1>%
    # data1 = [0, 1266, 1560, 1854, 2147, 2441, 2735, 3029, 3322, 3616, 3910, 4204, 4497, 4791, 5085, 5378, 5672, 5966, 6260, 6553, 6847]
    CD = 0.5
    关联技能 = ['所有']
    非关联技能 = ['剑盾猛攻','剑盾强袭','天马流星落','暮光之灵黄昏独角兽','生命之律·神木擎天']
    关联技能2 = ['剑盾强袭']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.72 + 0.03 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.72 + 0.03 * self.等级+0.3, 5)

# 盾挑    技能太多了，这个就不写上去了，Z，吃基础精通
# class 技能7(职业主动技能):
#    名称 = '盾挑'
#    所在等级 = 1
#    等级上限 = 20
#    基础等级 = 10
#    基础 = 89
#    成长 = 11
#    CD = 2
#    TP成长 = 0.08
#    TP上限 = 5

# 强踢
class 技能4(职业主动技能):
    名称 = '强踢'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    data0 = [(i*1.0) for i in [0, 762, 839, 916, 994, 1071, 1148, 1226, 1303, 1380, 1458, 1535, 1612, 1690, 1767, 1844, 1922, 1999, 2076, 2154, 2231, 2308, 2386, 2463, 2540, 2617, 2695, 2772, 2849, 2927, 3004, 3081, 3159, 3236, 3313, 3391, 3468, 3545, 3623, 3700, 3777, 3855, 3932, 4009, 4087, 4164, 4241, 4319, 4396, 4473, 4551, 4628, 4705, 4783, 4860, 4937, 5015, 5092, 5169, 5247, 5324, 5401, 5478, 5556, 5633, 5710, 5788, 5865, 5942, 6020, 6097]]
    # 基础 = 684.7
    # 成长 = 77.3
    CD = 5

# 盾击
class 技能5(职业主动技能):
    名称 = '盾击'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    data0 = [(i*1.0) for i in [0, 327, 360, 393, 426, 459, 492, 526, 559, 592, 625, 658, 692, 725, 758, 791, 824, 857, 891, 924, 957, 990, 1023, 1057, 1090, 1123, 1156, 1189, 1222, 1256, 1289, 1322, 1355, 1388, 1421, 1455, 1488, 1521, 1554, 1587, 1621, 1654, 1687, 1720, 1753, 1786, 1820, 1853, 1886, 1919, 1952, 1986, 2019, 2052, 2085, 2118, 2151, 2185, 2218, 2251, 2284, 2317, 2351, 2384, 2417, 2450, 2483, 2516, 2550, 2583, 2616]]
    # 基础 = 293.9
    # 成长 = 33.1
    CD = 3

# 致命突刺
class 技能6(职业主动技能):
    名称 = '致命突刺'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    # 基础 = 163.1
    # 成长 = 22.9
    data0 = [(i*1.0) for i in [0, 186, 210, 234, 256, 278, 303, 325, 348, 370, 394, 417, 438, 462, 485, 509, 530, 554, 576, 600, 622, 644, 668, 691, 714, 737, 759, 782, 804, 828, 851, 875, 897, 919, 943, 965, 988, 1011, 1034, 1057, 1079, 1103, 1127, 1149, 1171, 1193, 1217, 1241, 1262, 1285, 1309, 1466, 1491, 1516, 1544, 1568, 1594, 1619, 1644, 1671, 1696, 1722, 1747, 1772, 1799, 1825, 1850, 1876, 1901, 1928, 1952]]
    #最大蓄气时物理攻击力：<data1>%
    # data1 = [0, 234, 264, 292, 320, 348, 378, 406, 434, 463, 492, 520, 548, 576, 606, 636, 662, 693, 721, 750, 776, 805, 835, 864, 892, 921, 949, 978, 1006, 1035, 1064, 1093, 1121, 1149, 1178, 1207, 1234, 1264, 1294, 1321, 1349, 1377, 1408, 1436, 1463, 1493, 1522, 1550, 1577, 1605, 1636, 1833, 1864, 1896, 1928, 1960, 1992, 2023, 2056, 2089, 2120, 2153, 2184, 2217, 2248, 2281, 2312, 2345, 2379, 2409, 2440]
    CD = 3

# 愤怒冲撞
class 技能7(职业主动技能):
    名称 = '愤怒冲撞'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1895.9
    # 成长 = 214.1
    data0 = [(i*1.23) for i in [0, 2110, 2324, 2538, 2752, 2966, 3180, 3395, 3609, 3823, 4037, 4251, 4465, 4679, 4894, 5108, 5322, 5536, 5750, 5963, 6177, 6392, 6606, 6820, 7034, 7248, 7462, 7677, 7891, 8105, 8319, 8533, 8747, 8961, 9176, 9390, 9604, 9818, 10032, 10246, 10460, 10675, 10889, 11103, 11316, 11530, 11744, 11958, 12173, 12387, 12601, 12815, 13029, 13243, 13457, 13672, 13886, 14100, 14314, 14528, 14742, 14956, 15171, 15385, 15599, 15813, 16027, 16241, 16455, 16669, 16883]]
    CD = 9
    # 攻击倍率 = 1.23

# 破武之轮
class 技能8(职业主动技能):
    名称 = '破武之轮'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1071.6
    # 成长 = 160.4
    #挥剑物理攻击力：<data1>%
    data0 = [(i*1.0) for i in [0, 411, 491, 546, 599, 653, 701, 759, 809, 861, 914, 969, 1023, 1071, 1130, 1179, 1233, 1284, 1340, 1394, 1442, 1497, 1550, 1604, 1655, 1710, 1761, 1814, 1866, 1922, 1974, 2027, 2082, 2132, 2184, 2237, 2292, 2345, 2396, 2447, 2502, 2556, 2609, 2664, 2715, 2766, 2817, 2873, 2927, 2979, 3035, 3083, 3137, 3191, 3245, 3296, 3350, 3403, 3456, 3509, 3562]]
    #剑气物理攻击力：<data2>%
    data1 = [(i*1.0) for i in [0, 821, 980, 1091, 1196, 1304, 1401, 1517, 1617, 1722, 1827, 1938, 2045, 2142, 2258, 2358, 2465, 2568, 2679, 2786, 2883, 2994, 3099, 3207, 3309, 3420, 3521, 3627, 3731, 3842, 3948, 4053, 4164, 4262, 4368, 4472, 4583, 4689, 4790, 4893, 5003, 5111, 5216, 5327, 5430, 5531, 5634, 5745, 5852, 5957, 6068, 6165, 6272, 6381, 6488, 6591, 6698, 6805, 6911, 7017, 7123]]
    攻击次数2 = 1
    # TP成长 = 0.10
    # TP上限 = 5
    CD = 6

# 守护神鹿
class 技能9(职业主动技能):
    名称 = '守护神鹿'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [(i*1.226) for i in [0, 272, 299, 327, 354, 382, 409, 438, 465, 493, 520, 548, 575, 603, 631, 659, 686, 714, 741, 769, 796, 823, 852, 879, 907, 934, 962, 989, 1017, 1045, 1073, 1100, 1128, 1155, 1183, 1210, 1238, 1266, 1294, 1321, 1349, 1376, 1404, 1431, 1459, 1487, 1514, 1542, 1569, 1597, 1624, 1652, 1680, 1708, 1735, 1763, 1790, 1818, 1845, 1874, 1901, 1929, 1956, 1984, 2011, 2039, 2066, 2094, 2122, 2149, 2177]]
    攻击次数 = 6
    # 基础 = 1466.4
    # 成长 = 165.6
    CD = 6
    # 攻击倍率 = 1.226

# 审判之盾
class 技能10(职业主动技能):
    名称 = '审判之盾'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    #挥舞物理攻击力：<data0>%
    data0 = [(i*1.208) for i in [0, 266, 293, 320, 347, 374, 401, 428, 455, 482, 509, 536, 563, 590, 617, 644, 671, 698, 725, 752, 779, 806, 833, 860, 887, 914, 941, 968, 995, 1022, 1049, 1076, 1103, 1130, 1157, 1184, 1211, 1238, 1265, 1292, 1319, 1346, 1373, 1400, 1427, 1454, 1481, 1508, 1535, 1562, 1590, 1617, 1644, 1671, 1698, 1725, 1752, 1779, 1806, 1833, 1860, 1887, 1914, 1941, 1968, 1995, 2022, 2049, 2076, 2103, 2130]]
    #攻击审判状态的敌人时攻击力：<data1>%
    data1 = [(i*1.208) for i in [0, 186, 205, 224, 243, 262, 280, 299, 318, 337, 356, 375, 394, 413, 432, 451, 470, 488, 507, 526, 545, 564, 583, 602, 621, 640, 659, 678, 696, 715, 734, 753, 772, 791, 810, 829, 848, 867, 886, 904, 923, 942, 961, 980, 999, 1018, 1037, 1056, 1075, 1094, 1113, 1131, 1150, 1169, 1188, 1207, 1226, 1245, 1264, 1283, 1302, 1321, 1339, 1358, 1377, 1396, 1415, 1434, 1453, 1472, 1491]]
    攻击次数2 = 10
    # 基础 = 1910
    # 成长 = 216
    CD = 7
    # 攻击倍率 = 1.208

# 破甲冲击
class 技能11(职业主动技能):
    名称 = '破甲冲击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 1621.8
    # 成长 = 183.2
    #冲击波攻击力：<data0>%
    data0 = [(i*1.22) for i in [0, 1805, 1989, 2172, 2355, 2538, 2721, 2905, 3088, 3271, 3454, 3637, 3821, 4004, 4187, 4370, 4553, 4737, 4920, 5103, 5286, 5469, 5653, 5836, 6019, 6202, 6385, 6569, 6752, 6935, 7118, 7302, 7485, 7668, 7851, 8034, 8218, 8401, 8584, 8767, 8950, 9134, 9317, 9500, 9683, 9866, 10050, 10233, 10416, 10599, 10782, 10966, 11149, 11332, 11515, 11698, 11882, 12065, 12248, 12431, 12614, 12798, 12981, 13164, 13347, 13530, 13714, 13897, 14080, 14263, 14447]]
    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.22

# 精灵之跃 蓄力提高15%伤害，默认一瞬间释放也提高3%，冲击波不受加成，一级刮痧技能就不写那么多了
class 技能12(职业主动技能):
    名称 = '精灵之跃'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 2675.8
    # 成长 = 302.2
    # 冲撞物理攻击力：<data0>%
    # 蓄气时攻击力增加率：15%
    data0 = [(i*1.05) for i in [0, 2978, 3281, 3583, 3885, 4187, 4489, 4792, 5094, 5396, 5698, 6000, 6303, 6605, 6907, 7209, 7511, 7814, 8116, 8418, 8720, 9023, 9325, 9627, 9929, 10231, 10534, 10836, 11138, 11440, 11742, 12045, 12347, 12649, 12951, 13253, 13556, 13858, 14160, 14462, 14764, 15067, 15369, 15671, 15973, 16275, 16578, 16880, 17182, 17484, 17786, 18089, 18391, 18693, 18995, 19298, 19600, 19902, 20204, 20506, 20809, 21111, 21413, 21715, 22017, 22320, 22622, 22924, 23226, 23528, 23831]]
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.05

# 神木刺击
class 技能13(职业主动技能):
    名称 = '神木刺击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 2420.6
    # 成长 = 273.4
    data0 = [(i*1.23) for i in [0, 2694, 2968, 3241, 3515, 3788, 4062, 4335, 4608, 4882, 5155, 5429, 5702, 5975, 6249, 6522, 6796, 7069, 7342, 7616, 7889, 8163, 8436, 8709, 8983, 9256, 9530, 9803, 10076, 10350, 10623, 10897, 11170, 11443, 11717, 11990, 12264, 12537, 12811, 13084, 13357, 13631, 13904, 14178, 14451, 14724, 14998, 15271, 15545, 15818, 16091, 16365, 16638, 16912, 17185, 17458, 17732, 18005, 18279, 18552, 18825, 19099, 19372, 19646, 19919, 20192, 20466, 20739, 21013, 21286, 21559]]
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.23

# 铁壁推进 持盾推进8秒，18hit，但一般学1级用来刮痧，这里就做1hit使用
class 技能14(职业主动技能):
    名称 = '铁壁推进'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 367.4
    # 成长 = 41.6
    # 攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 409, 451, 493, 534, 575, 617, 659, 701, 742, 783, 825, 867, 908, 950, 991, 1033, 1075, 1116, 1157, 1199, 1241, 1283, 1324, 1365, 1407, 1449, 1490, 1532, 1573, 1615, 1657, 1698, 1739, 1781, 1823, 1865, 1906, 1947, 1989, 2031, 2072, 2114, 2155, 2197, 2239, 2280, 2321, 2363, 2405, 2447, 2488, 2529, 2571, 2613, 2654, 2696, 2737, 2779, 2821, 2862, 2903, 2945, 2987, 3029, 3070, 3111, 3154, 3195, 3236, 3278]]
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

# 自然束缚
class 技能15(职业主动技能):
    名称 = '自然束缚'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 4000.3
    # 成长 = 451.7
    #藤条捆绑的物理攻击力：<data0>%
    data0 = [(i*1.117) for i in [0, 2226, 2452, 2678, 2904, 3129, 3355, 3581, 3807, 4033, 4259, 4485, 4711, 4936, 5162, 5388, 5614, 5840, 6066, 6292, 6518, 6743, 6969, 7195, 7421, 7647, 7873, 8099, 8325, 8550, 8776, 9002, 9228, 9454, 9680, 9906, 10131, 10357, 10583, 10809, 11035, 11261, 11487, 11713, 11938, 12164, 12390, 12616, 12842, 13068, 13294, 13520, 13745, 13971, 14197, 14423, 14649, 14875, 15101, 15327, 15552, 15778, 16004, 16230, 16456, 16682, 16908, 17134, 17359, 17585, 17811]]
    #藤条拉回物理攻击力：<data1>%
    data1 = [(i*1.117) for i in [0, 2226, 2452, 2678, 2904, 3129, 3355, 3581, 3807, 4033, 4259, 4485, 4711, 4936, 5162, 5388, 5614, 5840, 6066, 6292, 6518, 6743, 6969, 7195, 7421, 7647, 7873, 8099, 8325, 8550, 8776, 9002, 9228, 9454, 9680, 9906, 10131, 10357, 10583, 10809, 11035, 11261, 11487, 11713, 11938, 12164, 12390, 12616, 12842, 13068, 13294, 13520, 13745, 13971, 14197, 14423, 14649, 14875, 15101, 15327, 15552, 15778, 16004, 16230, 16456, 16682, 16908, 17134, 17359, 17585, 17811]]
    攻击次数2 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.117

# 一刀两断
class 技能16(职业主动技能):
    名称 = '一刀两断'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 3502.4
    # 成长 = 395.6
    #战意攻击力： <data0>%
    data0 = [(i*1.192) for i in [0, 1442, 1589, 1735, 1882, 2028, 2174, 2321, 2467, 2613, 2760, 2906, 3053, 3199, 3345, 3492, 3638, 3784, 3931, 4077, 4224, 4370, 4516, 4663, 4809, 4956, 5102, 5248, 5395, 5541, 5687, 5834, 5980, 6127, 6273, 6419, 6566, 6712, 6858, 7005, 7151, 7298, 7444, 7590, 7737, 7883, 8029, 8176, 8322, 8469, 8615, 8761, 8908, 9054, 9201, 9347, 9493, 9640, 9786, 9932, 10079, 10225, 10372, 10518, 10664, 10811, 10957, 11103, 11250, 11396, 11543]]
    #敌人断开时伤害：<data1>%
    data1 = [(i*1.192) for i in [0, 2456, 2706, 2955, 3204, 3453, 3703, 3952, 4201, 4450, 4699, 4949, 5198, 5447, 5696, 5946, 6195, 6444, 6693, 6943, 7192, 7441, 7690, 7940, 8189, 8438, 8687, 8937, 9186, 9435, 9684, 9934, 10183, 10432, 10681, 10931, 11180, 11429, 11678, 11928, 12177, 12426, 12675, 12924, 13174, 13423, 13672, 13921, 14171, 14420, 14669, 14918, 15168, 15417, 15666, 15915, 16165, 16414, 16663, 16912, 17162, 17411, 17660, 17909, 18159, 18408, 18657, 18906, 19156, 19405, 19654]]
    攻击次数2 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.192
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.data0 = [(i*3.42) for i in self.data0]
            self.攻击次数2 = 0
            # self.倍率 *= 1.2653516366
        elif x == 1:
            # self.倍率 *= 1.3467485255
            self.data0 = [(i*3.64) for i in self.data0]
            self.攻击次数2 = 0

# 飓风旋枪 刺击2HIT，旋风10hit
class 技能17(职业主动技能):
    名称 = '飓风旋枪'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 基础 = 7114.3
    # 成长 = 803.7
    #刺击攻击力：<data0>%
    data0 = [(i*1.175) for i in [0, 2574, 2836, 3098, 3359, 3620, 3881, 4142, 4404, 4665, 4926, 5187, 5448, 5710, 5971, 6232, 6493, 6755, 7016, 7278, 7539, 7800, 8061, 8322, 8584, 8845, 9106, 9367, 9628, 9890, 10151, 10413, 10674, 10935, 11196, 11458, 11719, 11980, 12241, 12502, 12764, 13025, 13286, 13547, 13808, 14070, 14332, 14593, 14854, 15115, 15376, 15638, 15899, 16160, 16421, 16682, 16944, 17205, 17466, 17728, 17989, 18250, 18512, 18773, 19034, 19295, 19556, 19818, 20079, 20340, 20601]]
    攻击次数 = 2
    #旋转攻击力：<data1>%
    data1 = [(i*1.175) for i in [0, 277, 305, 333, 361, 390, 417, 446, 474, 502, 530, 558, 586, 614, 643, 670, 699, 727, 755, 783, 812, 839, 868, 896, 924, 952, 981, 1008, 1036, 1065, 1092, 1121, 1149, 1177, 1205, 1234, 1261, 1290, 1318, 1346, 1374, 1403, 1430, 1458, 1487, 1514, 1543, 1571, 1599, 1627, 1656, 1683, 1712, 1740, 1768, 1796, 1825, 1852, 1881, 1909, 1936, 1965, 1993, 2021, 2049, 2078, 2105, 2134, 2162, 2190, 2218]]
    攻击次数2 = 10
    CD = 25
    演出时间 = 2
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.175
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            # 护石是加算还是乘算待定
            self.data1 =[(i*1.49) for i in self.data1]
            # self.倍率 *= 1.1714  
            self.CD *= 0.90
        elif x == 1:
            self.data1 =[(i*1.74) for i in self.data1]
            # self.倍率 *= 1.258886811
            self.CD *= 0.90

# 天陨断空斩
class 技能18(职业主动技能):
    名称 = '天陨断空斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 10129.2
    # 成长 = 1143.8
    #旋转劈砍物理攻击力：<data0>%
    data0 = [(i*1.233) for i in [0, 1465, 1614, 1763, 1911, 2060, 2208, 2358, 2506, 2655, 2803, 2952, 3101, 3250, 3398, 3547, 3695, 3844, 3993, 4142, 4290, 4439, 4587, 4737, 4885, 5034, 5182, 5331, 5480, 5629, 5777, 5926, 6074, 6224, 6372, 6521, 6669, 6818, 6967, 7116, 7264, 7413, 7561, 7711, 7859, 8008, 8156, 8305, 8454, 8603, 8751, 8900, 9048, 9197, 9346, 9495, 9643, 9792, 9940, 10090, 10238, 10387, 10535, 10684, 10833, 10982, 11130, 11279, 11427, 11577, 11725]]
    #上劈物理攻击力：<data1>%
    data1 = [(i*1.233) for i in [0, 1127, 1242, 1355, 1470, 1584, 1699, 1813, 1928, 2042, 2156, 2271, 2385, 2500, 2614, 2729, 2842, 2957, 3071, 3186, 3300, 3415, 3528, 3643, 3758, 3872, 3987, 4101, 4215, 4329, 4444, 4558, 4673, 4787, 4902, 5015, 5130, 5245, 5359, 5474, 5588, 5702, 5816, 5931, 6045, 6160, 6274, 6388, 6502, 6617, 6731, 6846, 6961, 7075, 7189, 7303, 7418, 7532, 7647, 7761, 7875, 7989, 8104, 8218, 8333, 8448, 8561, 8676, 8790, 8905, 9019]]
    攻击次数2 = 1
    #闪光下劈的物理攻击力：<data2>%    
    data2 = [(i*1.233) for i in [0, 1691, 1862, 2034, 2205, 2377, 2549, 2720, 2891, 3063, 3235, 3407, 3578, 3749, 3921, 4093, 4265, 4435, 4607, 4779, 4951, 5122, 5293, 5465, 5637, 5808, 5980, 6151, 6323, 6494, 6666, 6838, 7010, 7181, 7352, 7524, 7696, 7868, 8038, 8210, 8382, 8554, 8725, 8896, 9068, 9240, 9411, 9583, 9754, 9926, 10097, 10269, 10441, 10612, 10784, 10955, 11127, 11299, 11470, 11641, 11813, 11985, 12157, 12327, 12499, 12671, 12843, 13014, 13185, 13357, 13529]]
    攻击次数3 = 1
    #闪光下劈的冲击波物理攻击力：<data3>%
    data3 = [(i*1.233) for i in [0, 6990, 7699, 8408, 9117, 9827, 10535, 11245, 11953, 12663, 13372, 14081, 14790, 15500, 16208, 16918, 17626, 18336, 19045, 19754, 20463, 21173, 21882, 22591, 23300, 24009, 24719, 25427, 26137, 26845, 27555, 28264, 28973, 29682, 30392, 31100, 31810, 32518, 33228, 33937, 34646, 35355, 36065, 36774, 37483, 38192, 38901, 39611, 40319, 41029, 41738, 42447, 43156, 43865, 44574, 45284, 45992, 46702, 47410, 48120, 48829, 49538, 50248, 50957, 51666, 52375, 53084, 53793, 54503, 55211, 55921]]
    攻击次数4 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.233
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.data1 = [(i*2.3) for i in self.data1]
            self.data2 = [(i*1.79) for i in self.data2]
            self.data3 = [(i*1.14) for i in self.data3]
            # self.倍率 *= 1.2053
        elif x == 1:
            self.攻击次数 = 0
            self.data1 = [(i*2.3) for i in self.data1]
            self.data2 = [(i*1.79) for i in self.data2]
            self.data3 = [(i*1.27) for i in self.data3]
            # self.倍率 *= 1.2859

# 一觉 1+4+1 hit
class 技能19(职业主动技能):
    名称 = '天马流星落'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 32891.3
    成长 = 9930.6
    #一斩物理攻击力：<data0>%
    data0 = [(i*1.201) for i in [0, 3211, 3956, 4701, 5446, 6190, 6935, 7680, 8425, 9170, 9915, 10659, 11404, 12149, 12894, 13639, 14384, 15129, 15873, 16617, 17362, 18107, 18852, 19597, 20341, 21086, 21831, 22576, 23321, 24066, 24810, 25555, 26300, 27045, 27790, 28535, 29280, 30024, 30768, 31513, 32258, 33003, 33748, 34492, 35237, 35982, 36727, 37472, 38217, 38961, 39706, 40451, 41196, 41941, 42686, 43431, 44175, 44919, 45664, 46409, 47154, 47899, 48643, 49388, 50133, 50878, 51623, 52368, 53113, 53857, 54602]]
    #二斩多段攻击物理攻击力：<data1>%
    data1 = [(i*1.201) for i in [0, 1894, 2334, 2774, 3212, 3652, 4092, 4532, 4970, 5410, 5850, 6288, 6728, 7168, 7607, 8046, 8486, 8926, 9364, 9804, 10244, 10683, 11122, 11562, 12002, 12441, 12880, 13320, 13759, 14198, 14638, 15078, 15517, 15956, 16396, 16835, 17274, 17714, 18153, 18593, 19032, 19472, 19911, 20350, 20790, 21229, 21669, 22108, 22548, 22987, 23426, 23866, 24305, 24745, 25184, 25624, 26063, 26502, 26942, 27381, 27821, 28260, 28700, 29139, 29578, 30018, 30457, 30897, 31336, 31775, 32215]]
    攻击次数2 = 4
    #天马冲锋物理攻击力：<data2>%
    data2 = [(i*1.201) for i in [0, 32033, 39461, 46889, 54317, 61745, 69173, 76602, 84030, 91457, 98885, 106313, 113742, 121170, 128598, 136025, 143453, 150882, 158310, 165738, 173166, 180594, 188022, 195450, 202878, 210306, 217734, 225162, 232591, 240018, 247446, 254874, 262302, 269731, 277159, 284586, 292014, 299442, 306871, 314299, 321727, 329155, 336582, 344011, 351439, 358867, 366295, 373723, 381151, 388579, 396007, 403435, 410863, 418292, 425720, 433147, 440575, 448003, 455432, 462860, 470288, 477716, 485143, 492572, 500000, 507428, 514856, 522284, 529712, 537140, 544568]]
    攻击次数3 = 1
    CD = 145
    # 攻击倍率 = 1.201

# 生命审判
class 技能20(职业主动技能):
    名称 = '生命审判'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    # 基础 = 9299.1
    # 成长 = 1049.9
    #爆炸物理攻击力：<data0>%
    data0 = [(i*1.237) for i in [0, 10349, 11399, 12449, 13498, 14549, 15599, 16649, 17698, 18748, 19798, 20849, 21898, 22948, 23998, 25048, 26098, 27148, 28198, 29248, 30297, 31348, 32398, 33448, 34497, 35547, 36597, 37648, 38697, 39747, 40797, 41847, 42897, 43947, 44997, 46047, 47096, 48147, 49197, 50247, 51296, 52346, 53397, 54447, 55496, 56546, 57596, 58646, 59696, 60746, 61796, 62846, 63895, 64946, 65996, 67046, 68095, 69145, 70196, 71246, 72295, 73345, 74395, 75446, 76495, 77545, 78595, 79644, 80694, 81745, 82795]]
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.237
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.08
        elif x == 1:
            self.倍率 *= 1.08 + 0.09

# 壁垒突袭
class 技能21(职业主动技能):
    名称 = '壁垒突袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 基础 = 16225.2
    # 成长 = 1831.8
    #盾牌击打攻击力：<data0>%
    data0 = [(i*1.201) for i in [0, 6320, 6961, 7602, 8242, 8884, 9525, 10166, 10807, 11448, 12090, 12731, 13372, 14013, 14655, 15295, 15936, 16577, 17219, 17860, 18501, 19142, 19784, 20425, 21066, 21706, 22348, 22989, 23630, 24271, 24912, 25554, 26195, 26836, 27477, 28118, 28759, 29400, 30041, 30683, 31324, 31965, 32606, 33248, 33889, 34530, 35170, 35812, 36453, 37094, 37735, 38376, 39018, 39659, 40300, 40941, 41582, 42223, 42864, 43505, 44147, 44788, 45429, 46070, 46712, 47353, 47993, 48634, 49276, 49917, 50558]]
    #盾牌破碎时攻击力：<data1>%
    data1 = [(i*1.201) for i in [0, 11737, 12927, 14118, 15308, 16499, 17690, 18881, 20071, 21262, 22452, 23643, 24833, 26025, 27216, 28406, 29597, 30787, 31978, 33169, 34360, 35550, 36741, 37931, 39122, 40313, 41504, 42694, 43885, 45076, 46266, 47457, 48648, 49839, 51029, 52220, 53410, 54601, 55792, 56983, 58173, 59364, 60554, 61745, 62937, 64127, 65318, 66508, 67699, 68889, 70080, 71271, 72462, 73652, 74843, 76033, 77224, 78415, 79606, 80797, 81987, 83178, 84368, 85559, 86750, 87941, 89131, 90322, 91512, 92703, 93894]]
    攻击次数2 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    # 攻击倍率 = 1.201
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.data2 = [(i*0.34) for i in self.data1]
            攻击次数3 = 1
            # self.倍率 *= 1.221
        elif x == 1:
            self.data2 = [(i*0.47) for i in self.data1]
            攻击次数3 = 1
            # self.倍率 *= 1.3055

# 剑盾强袭
class 技能22(职业主动技能):
    名称 = '剑盾强袭'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 基础 = 22287.6
    # 成长 = 2516.4
    # [剑盾猛攻]连锁伤害额外增加量：+5%
    data0 = [(i*1.209) for i in [0, 24804, 27321, 29837, 32354, 34870, 37386, 39903, 42419, 44936, 47452, 49969, 52485, 55001, 57518, 60034, 62551, 65067, 67584, 70100, 72616, 75133, 77649, 80166, 82682, 85198, 87715, 90231, 92748, 95264, 97781, 100297, 102813, 105330, 107846, 110363, 112879, 115396, 117912, 120428, 122945]]
    CD = 40
    # 攻击倍率 = 1.209
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35

# 自然之怒  1+6+1 hit
class 技能23(职业主动技能):
    名称 = '自然之怒'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 26353
    # 成长 = 2976
    #盾牌攻击物理攻击力：<data0>%
    data0 = [(i*1.203) for i in [0, 5114, 5633, 6152, 6670, 7189, 7708, 8227, 8746, 9264, 9783, 10303, 10821, 11340, 11858, 12377, 12897, 13415, 13934, 14453, 14972, 15491, 16009, 16528, 17047, 17566, 18085, 18604, 19122, 19641, 20161, 20679, 21198, 21716, 22235, 22755, 23273, 23792, 24311, 24830, 25349, 25867, 26386, 26905, 27424, 27943, 28462, 28980, 29499, 30018, 30537, 31056, 31574, 32093, 32613, 33131, 33650, 34169, 34688, 35207, 35725, 36244, 36763, 37282, 37801, 38320, 38838, 39357, 39876, 40395, 40914]]
    #藤蔓多段攻击物理攻击力：<data1>%
    data1 = [(i*1.203) for i in [0, 1910, 2104, 2298, 2491, 2685, 2879, 3073, 3266, 3461, 3654, 3848, 4042, 4236, 4429, 4624, 4817, 5011, 5205, 5399, 5592, 5787, 5980, 6175, 6368, 6561, 6756, 6949, 7143, 7337, 7531, 7724, 7919, 8112, 8306, 8500, 8694, 8887, 9082, 9275, 9469, 9663, 9857, 10050, 10245, 10438, 10632, 10826, 11019, 11213, 11407, 11601, 11794, 11989, 12182, 12376, 12570, 12764, 12958, 13152, 13345, 13540, 13733, 13927, 14121, 14315, 14508, 14703, 14896, 15089, 15284]]
    攻击次数2 = 6
    #藤蔓爆炸物理攻击力：<data2>%
    data2 = [(i*1.203) for i in [0, 12755, 14050, 15344, 16638, 17933, 19226, 20521, 21814, 23109, 24403, 25697, 26991, 28285, 29579, 30873, 32168, 33462, 34756, 36050, 37344, 38638, 39933, 41226, 42521, 43814, 45109, 46402, 47697, 48992, 50285, 51580, 52873, 54168, 55462, 56756, 58050, 59344, 60638, 61932, 63226, 64521, 65814, 67109, 68403, 69697, 70992, 72285, 73580, 74873, 76168, 77461, 78756, 80050, 81344, 82638, 83932, 85227, 86521, 87815, 89109, 90403, 91697, 92991, 94285, 95580, 96873, 98168, 99461, 100756, 102050]]
    攻击次数3 =1
    CD = 45
    # 攻击倍率 = 1.203
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.data0 = [(i*2.98) for i in self.data0]
            # self.倍率 *= 1.3452212

# 二觉    3+1+5 hit
class 技能24(职业主动技能):
    名称 = '暮光之灵黄昏独角兽'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 76675
    # 成长 = 23148.2
    #突击物理攻击力：<data0>%
    data0 = [(i*1.231) for i in [0, 5989, 7378, 8767, 10156, 11545, 12934, 14322, 15711, 17100, 18489, 19878, 21267, 22656, 24045, 25434, 26822, 28211, 29600, 30989, 32378, 33767, 35156, 36545, 37934, 39323, 40711, 42100, 43489, 44878, 46267, 47656, 49045, 50434, 51823, 53211, 54600, 55989, 57378, 58767, 60156, 61545, 62934, 64323, 65711, 67100, 68489, 69878, 71267, 72656, 74045, 75434, 76823, 78211, 79600, 80989, 82378, 83767, 85156, 86545, 87934, 89323, 90711, 92100, 93489, 94878, 96267, 97656, 99045, 100434, 101823]]
    攻击次数 = 3
    #最后一击物理攻击力：<data1>%
    data1 = [(i*1.231) for i in [0, 71875, 88541, 105208, 121875, 138541, 155208, 171875, 188542, 205208, 221875, 238542, 255208, 271875, 288542, 305208, 321875, 338542, 355209, 371875, 388542, 405209, 421875, 438542, 455209, 471876, 488542, 505209, 521876, 538542, 555209, 571876, 588542, 605209, 621876, 638543, 655209, 671876, 688543, 705209, 721876, 738543, 755209, 771876, 788543, 805210, 821876, 838543, 855210, 871876, 888543, 905210, 921876, 938543, 955210, 971877, 988543, 1005210, 1021877, 1038543, 1055210, 1071877, 1088543, 1105210, 1121877, 1138544, 1155210, 1171877, 1188544, 1205210, 1221877]]
    攻击次数2 = 1
    #星光多段攻击物理攻击力：<data2>%
    data2 = [(i*1.231) for i in [0, 1996, 2459, 2922, 3385, 3848, 4311, 4774, 5237, 5700, 6163, 6626, 7089, 7552, 8015, 8478, 8940, 9403, 9866, 10329, 10792, 11255, 11718, 12181, 12644, 13107, 13570, 14033, 14496, 14959, 15422, 15885, 16348, 16811, 17274, 17737, 18200, 18663, 19126, 19589, 20052, 20515, 20978, 21441, 21903, 22366, 22829, 23292, 23755, 24218, 24681, 25144, 25607, 26070, 26533, 26996, 27459, 27922, 28385, 28848, 29311, 29774, 30237, 30700, 31163, 31626, 32089, 32552, 33015, 33478, 33941]]
    攻击次数3 = 5
    # 攻击倍率 = 1.231
    CD = 180

class 技能25(被动技能):
    名称 = '生命的恩宠'
    所在等级 = 95
    等级上限 = 40
    等级精通 = 30
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能26(职业主动技能):
    名称 = '荆棘之城'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    CD = 60.0
    基础 = 5310.4
    成长 = 599.6
    攻击次数 = 1
    基础2 = 47799.2
    成长2 = 5396.8
    攻击次数2 = 1

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)
    

class 技能27(职业主动技能):
    名称 = '生命之律·神木擎天'
    所在等级 = 100
    等级上限 = 40
    等级精通 = 30
    基础等级 = 2
    关联技能 = ['无']
    CD = 290.0
    基础 = 24011.2233708822
    成长 = 7248.77662911778
    攻击次数 = 1
    基础2 = 192094.735204356
    成长2 = 57990.2647956442
    攻击次数2 = 1
    基础3 = 4001.07958064222
    成长3 = 1207.92041935778
    攻击次数3 = 6

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)

技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)

class 职业属性(角色属性):
    实际名称 = '皓曦·精灵骑士'
    角色 = '守护者'
    职业 = '精灵骑士'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '板甲'
    防具精通属性 = ['力量']

    主BUFF = 2.03

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    # def 被动倍率计算(self):
    #     super().被动倍率计算()
    #     # self.技能栏[self.技能序号['天马流星落']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
    #     # self.技能栏[self.技能序号['暮光之灵黄昏独角兽']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
    #     # self.技能栏[self.技能序号['天马流星落']].被动倍率 *= self.技能栏[self.技能序号['自然恩泽']].加成倍率(self.武器类型)
    #     # self.技能栏[self.技能序号['暮光之灵黄昏独角兽']].被动倍率 *= self.技能栏[self.技能序号['自然恩泽']].加成倍率(self.武器类型)
    #     # self.技能栏[self.技能序号['生命之律·神木擎天']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
    #     # self.技能栏[self.技能序号['生命之律·神木擎天']].被动倍率 *= self.技能栏[self.技能序号['自然恩泽']].加成倍率(self.武器类型)
    #     self.技能栏[self.技能序号['剑盾强袭']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
    #     self.技能栏[self.技能序号['剑盾强袭']].被动倍率 *= 0.30 + self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
    #     self.技能栏[self.技能序号['剑盾猛攻']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)


class 皓曦·精灵骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 护石判断(self):
        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '一刀两断':
                sign = 1
        if sign == 1:
            self.先锋斩倍率.setEnabled(True)
            self.先锋斩倍率.setStyleSheet(下拉框样式)
        else:
            self.先锋斩倍率.setEnabled(False)
            self.先锋斩倍率.setStyleSheet(下拉框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())

        self.先锋斩倍率 = MyQComboBox(self.main_frame2)
        for i in range(0,51):
            self.先锋斩倍率.addItem( '先锋斩：'+str(i * 2)+'%' )
        self.先锋斩倍率.setCurrentIndex(0)
        self.先锋斩倍率.resize(105, 20)
        self.先锋斩倍率.move(310, 420)
        self.先锋斩倍率.setToolTip('请按实际情况选择')

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           self.先锋斩倍率.setCurrentIndex(int(setfile[0].replace('\n', '')))

        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(str(self.先锋斩倍率.currentIndex())+'\n')

        except:
            pass

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.先锋斩倍率.isEnabled():
            属性.技能栏[属性.技能序号['一刀两断']].倍率 *= self.先锋斩倍率.currentIndex() / 50 + 1
