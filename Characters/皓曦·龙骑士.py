from math import *
from PublicReference.base import *


class 技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['龙人剑术','普通攻击（一轮）']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.463 + 0.089 * self.等级, 5)


class 技能1(主动技能):
    名称 = '龙人剑术'
    备注 = '(TP为基础精通)'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 1159.00 * 1.05
    成长 = 0
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 5


class 技能2(主动技能):
    名称 = '火焰吐息'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [(i*1.116) for i in [0, 785, 864, 944, 1023, 1103, 1183, 1262, 1342, 1422, 1501, 1581, 1661, 1740, 1820, 1900, 1979, 2059, 2138,
           2218, 2298, 2377, 2457, 2537, 2616, 2696, 2776, 2855, 2935, 3014, 3094, 3174, 3253, 3333, 3413, 3492, 3572,
           3652, 3731, 3811, 3891, 3970, 4050, 4129, 4209, 4289, 4368, 4448, 4528, 4607, 4687, 4767, 4846, 4926, 5006,
           5085, 5165, 5244, 5324, 5404, 5483]]
    攻击次数1 = 3
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '龙翼突袭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [(i*1.12) for i in [0, 1545, 1702, 1859, 2016, 2172, 2329, 2486, 2643, 2800, 2957, 3113, 3270, 3427, 3584, 3741, 3897, 4054,
           4211,
           4368, 4525, 4681, 4838, 4995, 5152, 5309, 5465, 5622, 5779, 5936, 6093, 6250, 6406, 6563, 6720, 6877, 7034,
           7190, 7347, 7504, 7661, 7818, 7974, 8131, 8288, 8445, 8602, 8759, 8915, 9072, 9229, 9386, 9543, 9699, 9856,
           10013, 10170, 10327, 10483, 10640, 10797, 10954, 11111, 11267, 11424, 11581, 11738, 11895, 12052, 12208,
           12365]]
    攻击次数1 = 1
    数据2 = [(i*1.12) for i in [0, 1399, 1541, 1683, 1825, 1967, 2109, 2251, 2393, 2535, 2677, 2819, 2961, 3103, 3245, 3387, 3529, 3671,
           3813, 3955, 4097, 4239, 4381, 4523, 4665, 4807, 4949, 5091, 5233, 5375, 5517, 5659, 5801, 5943, 6085, 6227,
           6369, 6511, 6653, 6795, 6937, 7079, 7221, 7363, 7505, 7647, 7789, 7931, 8073, 8215, 8357, 8499, 8641, 8783,
           8925, 9067, 9209, 9351, 9493, 9635, 9777, 9919, 10061, 10203, 10345, 10487, 10629, 10771, 10913, 11055,
           11197]]
    攻击次数2 = 1
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(主动技能):
    名称 = '龙语召唤：阿斯特拉'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    数据1 = [(i*1.101) for i in [0, 2712, 3145, 3577, 4009, 4442, 4874, 5307, 5739, 6172, 6604, 7037, 7469, 7901, 8334, 8766, 9199, 9631,
           10064, 10496, 10929, 11361, 11793, 12226, 12658, 13091, 13523, 13956, 14388, 14821, 15253]]
    攻击次数1 = 1
    CD = 7.0
    关联技能 = ['所有']

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)

    def 独立攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '爆破龙角'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [(i*1.12) for i in [0, 1531, 1686, 1841, 1997, 2152, 2307, 2462, 2618, 2773, 2928, 3084, 3239, 3394, 3550, 3705, 3860, 4016,
           4171,
           4326, 4482, 4637, 4792, 4948, 5103, 5258, 5414, 5569, 5724, 5880, 6035, 6190, 6346, 6501, 6656, 6812, 6967,
           7122, 7277, 7433, 7588, 7743, 7899, 8054, 8209, 8365, 8520, 8675, 8831, 8986, 9141, 9297, 9452, 9607, 9763,
           9918, 10073, 10229, 10384, 10539, 10695]]
    攻击次数1 = 1
    数据2 = [(i*1.12) for i in [0, 3572, 3934, 4297, 4659, 5022, 5384, 5746, 6109, 6471, 6834, 7196, 7559, 7921, 8283, 8646, 9008, 9371,
           9733, 10095, 10458, 10820, 11183, 11545, 11908, 12270, 12632, 12995, 13357, 13720, 14082, 14445, 14807,
           15169, 15532, 15894, 16257, 16619, 16981, 17344, 17706, 18069, 18431, 18794, 19156, 19518, 19881, 20243,
           20606, 20968, 21330, 21693, 22055, 22418, 22780, 23143, 23505, 23867, 24230, 24592, 24955]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(主动技能):
    名称 = '龙拳(地面释放)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [(i*1.105) for i in [0, 1838, 2025, 2211, 2398, 2584, 2771, 2957, 3144, 3330, 3517, 3703, 3890, 4076, 4263, 4449, 4636, 4822,
           5009, 5195, 5382, 5568, 5755, 5941, 6128, 6315, 6501, 6688, 6874, 7061, 7247, 7434, 7620, 7807, 7993, 8180,
           8366, 8553, 8739, 8926, 9112, 9299, 9485, 9672, 9858, 10045, 10231, 10418, 10605, 10791, 10978, 11164,
           11351, 11537, 11724, 11910, 12097, 12283, 12470, 12656, 12843]]
    攻击次数1 = 1
    数据2 = [(i*1.105) for i in [0, 2757, 3037, 3317, 3597, 3876, 4156, 4436, 4716, 4996, 5275, 5555, 5835, 6115, 6394, 6674, 6954, 7234,
           7514, 7793, 8073, 8353, 8633, 8912, 9192, 9472, 9752, 10032, 10311, 10591, 10871, 11151, 11431, 11710,
           11990, 12270, 12550, 12829, 13109, 13389, 13669, 13949, 14228, 14508, 14788, 15068, 15347, 15627, 15907,
           16187, 16467, 16746, 17026, 17306, 17586, 17865, 18145, 18425, 18705, 18985, 19264]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '龙拳(空中释放)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [(i*1.105) for i in [0, 489, 539, 589, 639, 688, 738, 788, 837, 887, 937, 986, 1036, 1086, 1136, 1185, 1235, 1285, 1334, 1384,
           1434, 1483, 1533, 1583, 1633, 1682, 1732, 1782, 1831, 1881, 1931, 1980, 2030, 2080, 2130, 2179, 2229, 2279,
           2328, 2378, 2428, 2478, 2527, 2577, 2627, 2676, 2726, 2776, 2825, 2875, 2925, 2975, 3024, 3074, 3124, 3173,
           3223, 3273, 3322, 3372, 3422]]
    攻击次数1 = 1
    数据2 = [(i*1.105) for i in [0, 4409, 4856, 5303, 5751, 6198, 6645, 7093, 7540, 7987, 8435, 8882, 9329, 9777, 10224, 10671, 11119,
           11566, 12013, 12461, 12908, 13355, 13803, 14250, 14697, 15145, 15592, 16039, 16486, 16934, 17381, 17828,
           18276, 18723, 19170, 19618, 20065, 20512, 20960, 21407, 21854, 22302, 22749, 23196, 23644, 24091, 24538,
           24986, 25433, 25880, 26328, 26775, 27222, 27669, 28117, 28564, 29011, 29459, 29906, 30353, 30801]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = '龙之撕咬'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [(i*1.101) for i in [0, 904, 996, 1087, 1179, 1271, 1363, 1454, 1546, 1638, 1730, 1821, 1913, 2005, 2097, 2188, 2280, 2372, 2464,
           2555, 2647, 2739, 2831, 2922, 3014, 3106, 3197, 3289, 3381, 3473, 3564, 3656, 3748, 3840, 3931, 4023, 4115,
           4207, 4298, 4390, 4482, 4574, 4665, 4757, 4849, 4941, 5032, 5124, 5216, 5308, 5399, 5491, 5583, 5675, 5766,
           5858, 5950, 6042, 6133, 6225, 6317]]
    攻击次数1 = 6
    CD = 10
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能9(主动技能):
    名称 = '龙翼穿刺(2hit+踢击)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [(i*1.12) for i in [0, 106, 116, 127, 138, 149, 159, 170, 181, 192, 202, 213, 224, 235, 246, 256, 267, 278, 289, 299, 310,
           321, 332, 342, 353, 364, 375, 385, 396, 407, 418, 428, 439, 450, 461, 472, 482, 493, 504, 515, 525, 536,
           547, 558, 568, 579, 590, 601, 611, 622, 633, 644, 655, 665, 676, 687, 698, 708, 719, 730, 741]]
    攻击次数1 = 2
    数据2 = [(i*1.12) for i in [0, 6490, 7148, 7807, 8465, 9123, 9782, 10440, 11099, 11757, 12416, 13074, 13732, 14391, 15049, 15708,
           16366, 17024, 17683, 18341, 19000, 19658, 20317, 20975, 21633, 22292, 22950, 23609, 24267, 24926, 25584,
           26242, 26901, 27559, 28218, 28876, 29535, 30193, 30851, 31510, 32168, 32827, 33485, 34144, 34802, 35460,
           36119, 36777, 37436, 38094, 38752, 39411, 40069, 40728, 41386, 42045, 42703, 43361, 44020, 44678, 45337]]
    攻击次数2 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '龙翼穿刺(撕咬附着)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [(i*1.12) for i in [0, 7109, 7825, 8548, 9271, 9993, 10710, 11432, 12156, 12878, 13595, 14317, 15040, 15763, 16486, 17203, 17925,
           18648, 19371, 20087, 20810, 21533, 22256, 22972, 23694, 24418, 25140, 25857, 26579, 27303, 28025, 28741,
           29464, 30187, 30910, 31633, 32350, 33072, 33795, 34518, 35234, 35957, 36680, 37403, 38119, 38841, 39565,
           40287, 41004, 41726, 42449, 43172, 43895, 44611, 45334, 46057, 46780, 47496, 48219, 48942, 49665]]
    攻击次数1 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能11(主动技能):
    名称 = '飞龙斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [(i*1.12) for i in [0, 2003, 2206, 2409, 2612, 2815, 3019, 3222, 3425, 3628, 3832, 4035, 4238, 4441, 4644, 4848, 5051, 5254,
           5457, 5660, 5864, 6067, 6270, 6473, 6677, 6880, 7083, 7286, 7489, 7693, 7896, 8099, 8302, 8505, 8709,
           8912, 9115, 9318, 9522, 9725, 9928, 10131, 10334, 10538, 10741, 10944, 11147, 11350, 11554, 11757, 11960,
           12163, 12367, 12570, 12773, 12976, 13179, 13383, 13586, 13789, 13992]]
    攻击次数1 = 2
    数据2 = [(i*1.12) for i in [0, 5883, 6479, 7076, 7673, 8270, 8867, 9464, 10061, 10657, 11254, 11851, 12448, 13045, 13642, 14238,
           14835, 15432, 16029, 16626, 17223, 17819, 18416, 19013, 19610, 20207, 20804, 21400, 21997, 22594, 23191,
           23788, 24385, 24982, 25578, 26175, 26772, 27369, 27966, 28563, 29159, 29756, 30353, 30950, 31547, 32144,
           32740, 33337, 33934, 34531, 35128, 35725, 36321, 36918, 37515, 38112, 38709, 39306, 39903, 40499, 41096]]
    攻击次数2 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 3.25
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 3.7
            self.CD *= 0.9
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(被动技能):
    名称 = '大胃王'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.0 + 0.01 * self.等级, 5)
        else:
            return round(0.9 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '龙刃无双'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [(i*1.05) for i in [0, 14507, 15979, 17451, 18923, 20395, 21867, 23338, 24810, 26282, 27754, 29226, 30698, 32169, 33641, 35113,
           36585, 38057, 39529, 41000, 42472, 43944, 45416, 46888, 48359, 49831, 51303, 52775, 54247, 55719, 57190,
           58662, 60134, 61606, 63078, 64550, 66021, 67493, 68965, 70437, 71909, 73380, 74852, 76324, 77796, 79268,
           80740, 82211, 83683, 85155, 86627, 88099, 89571, 91042, 92514, 93986, 95458, 96930, 98401, 99873, 101345]]
    攻击次数1 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
        elif x == 1:
            self.倍率 *= 1.37

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(主动技能):
    名称 = '魔龙之息(脱手)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [(i * 1.113) for i in
           [0, 1533, 1688, 1844, 1999, 2155, 2310, 2466, 2622, 2777, 2933, 3088, 3244, 3399, 3555, 3710, 3866, 4021,
            4177, 4333, 4488, 4644, 4799, 4955, 5110, 5266, 5421, 5577, 5733, 5888, 6044, 6199, 6355, 6510, 6666, 6821,
            6977, 7132, 7288, 7444, 7599, 7755, 7910, 8066, 8221, 8377, 8532, 8688, 8843, 8999, 9155, 9310, 9466, 9621,
            9777, 9932, 10088, 10243, 10399, 10554, 10710]]
    攻击次数1 = 13
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.30
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率



class 技能15(主动技能):
    名称 = '魔龙之息(骑乘)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [(i*1.113) for i in [0, 1015, 1118, 1221, 1324, 1427, 1530, 1633, 1736, 1839, 1942, 2045, 2148, 2251, 2354, 2457, 2560, 2663, 2766, 2869, 2972, 3075, 3178, 3280, 3383, 3486, 3589, 3692, 3795, 3898, 4001, 4104, 4207, 4310, 4413, 4516, 4619, 4722, 4825, 4928, 5031, 5134, 5237, 5340, 5443, 5546, 5649, 5752, 5855, 5958, 6061, 6164, 6267, 6370, 6473, 6576, 6679, 6782, 6885, 6988, 7091]]
    攻击次数1 = 23
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    护石CD缩减 = 0

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数1 = 25
            self.护石CD缩减 = 4
        elif x == 1:
            self.倍率 *= 1.07
            self.CD *= 0.9
            self.攻击次数1 = 25
            self.护石CD缩减 = 4
        
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return round((self.CD * 武器冷却惩罚(武器类型,输出类型,self.版本)-self.护石CD缩减)/ self.恢复, 1)

class 技能16(被动技能):
    名称 = '魔龙之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能17(主动技能):
    名称 = '魔龙之力(火球)'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    数据1 = [(i*1) for i in [0, 935, 1084, 1233, 1383, 1532, 1681, 1830, 1979, 2128, 2278, 2427, 2576, 2725, 2874, 3023, 3172, 3322, 3471,
           3620,
           3769, 3918, 4067, 4217, 4366, 4515, 4664, 4813, 4962, 5112, 5261, 5410, 5559, 5708, 5857, 6006, 6156, 6305,
           6454,
           6603, 6752]]
    攻击次数1 = 1
    CD = 3.0
    TP上限 = 0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能18(主动技能):
    名称 = '雷光嘶吼'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [(i*1.122) for i in [0, 2210, 2722, 3235, 3747, 4260, 4772, 5285, 5797, 6310, 6823, 7335, 7848, 8360, 8873, 9385, 9898, 10410,
           10923, 11435, 11948, 12460, 12973, 13485, 13998, 14510, 15023, 15535, 16048, 16561, 17073, 17586, 18098,
           18611, 19123, 19636, 20148, 20661, 21173, 21686, 22198]]
    攻击次数1 = 8
    数据2 = [(i*1.122) for i in [0, 39297, 48409, 57522, 66634, 75747, 84859, 93972, 103084, 112197, 121309, 130422, 139534, 148647, 157759,
           166871, 175984, 185096, 194209, 203321, 212434, 221546, 230659, 239771, 248884, 257996, 267109, 276221,
           285333, 294446, 303558, 312671, 321783, 330896, 340008, 349121, 358233, 367346, 376458, 385571, 394683]]
    攻击次数2 = 1
    CD = 145

    def 等效百分比(self, 武器类型):
        if self.等级 <= 8:
            return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率
        else:
            return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * 1.1) * self.倍率


class 技能19(主动技能):
    名称 = '龙皇制裁'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [(i*1.12) for i in [0, 20666, 22763, 24859, 26956, 29052, 31149, 33246, 35342, 37439, 39535, 41632, 43729, 45825, 47922, 50018,
           52115, 54212, 56308, 58405, 60501, 62598, 64694, 66791, 68888, 70984, 73081, 75177, 77274, 79371, 81467,
           83564, 85660, 87757, 89854, 91950, 94047, 96143, 98240, 100337, 102433, 104530, 106626, 108723, 110820,
           112916, 115013, 117109, 119206, 121303, 123399, 125496, 127592, 129689, 131786, 133882, 135979, 138075,
           140172, 142269, 144365]]
    攻击次数1 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能20(主动技能):
    名称 = '魔龙天翔(脱手)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [(i*1.113) for i in [0, 29663, 32672, 35681, 38690, 41701, 44710, 47719, 50729, 53738, 56747, 59757, 62766, 65775, 68784, 71794,
           74803, 77812, 80822, 83831, 86840, 89850, 92859, 95868, 98877, 101887, 104896, 107905, 110915, 113924,
           116933, 119943, 122952, 125961, 128970, 131980, 134990, 137999, 141009, 144018, 147027]]
    攻击次数1 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.18
        elif x == 1:
            self.倍率 *= 1.26

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能21(主动技能):
    名称 = '魔龙天翔(骑乘)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [(i*1.113) for i in [0, 10901, 12008, 13114, 14219, 15326, 16432, 17537, 18644, 19750, 20855, 21962, 23068, 24173, 25280,
           26385, 27491, 28598, 29703, 30809, 31916, 33021, 34127, 35234, 36339, 37445, 38552, 39657, 40763, 41870,
           42975, 44081, 45188, 46293, 47399, 48506, 49611, 50717, 51824, 52929, 54035]]
    攻击次数1 = 1
    数据2 = [(i*1.113) for i in [0, 8479, 9339, 10199, 11060, 11920, 12780, 13640, 14500, 15361, 16221, 17081, 17941, 18801, 19661,
           20522, 21382, 22242, 23102, 23962, 24822, 25683, 26544, 27404, 28264, 29124, 29985, 30845, 31705,
           32565, 33425, 34286, 35146, 36006, 36866, 37726, 38586, 39447, 40307, 41167, 42027]]
    攻击次数2 = 3
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能22(被动技能):
    名称 = '龙神血脉'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.02 * self.等级, 5)


class 技能23(主动技能):
    名称 = '魔龙星落'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [(i*1.12) for i in [0, 3698, 4073, 4449, 4824, 5199, 5574, 5949, 6325, 6700, 7075, 7450, 7826, 8201, 8576, 8951, 9326, 9702,
           10077, 10452, 10827, 11203, 11578, 11953, 12328, 12703, 13079, 13454, 13829, 14204, 14579, 14955, 15330,
           15705, 16080, 16456, 16831, 17206, 17581, 17956, 18332, 18707, 19082, 19457, 19833, 20208, 20583, 20958,
           21333, 21709, 22084, 22459, 22834, 23210, 23585, 23960, 24335, 24710, 25086, 25461, 25836]]
    攻击次数1 = 9
    数据2 = [(i*1.12) for i in [0, 22191, 24442, 26694, 28945, 31196, 33448, 35699, 37950, 40202, 42453, 44704, 46956, 49207, 51458,
           53710, 55961, 58212, 60464, 62715, 64966, 67218, 69469, 71720, 73971, 76223, 78474, 80725, 82977,
           85228, 87479, 89731, 91982, 94233, 96485, 98736, 100987, 103239, 105490, 107741, 109993, 112244,
           114495, 116747, 118998, 121249, 123501, 125752, 128003, 130254, 132506, 134757, 137008, 139260,
           141511, 143762, 146014, 148265, 150516, 152768, 155019]]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1
    
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.37

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能24(主动技能):
    名称 = '征战无双'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [(i*1.114) for i in [0, 25530, 28120, 30709, 33300, 35890, 38480, 41070, 43660, 46249, 48840, 51430, 54020, 56610, 59199, 61790,
           64380, 66970, 69560, 72149, 74739, 77330, 79920, 82510, 85100, 87689, 90279, 92870, 95460, 98050, 100639,
           103229, 105819, 108410, 111000, 113589, 116179, 118769, 121360, 123950, 126540, 129129, 131719, 134309,
           136900, 139490, 142079, 144669, 147259, 149849, 152440, 155030, 157619, 160209, 162799, 165390, 167980,
           170569, 173159, 175749, 178339]]
    攻击次数1 = 1
    数据2 = [(i*1.114) for i in [0, 36765, 40495, 44225, 47954, 51684, 55414, 59144, 62874, 66604, 70333, 74063, 77793, 81523, 85253, 88982,
           92712, 96442, 100172, 103902, 107632, 111361, 115091, 118821, 122551, 126281, 130011, 133740, 137470, 141200,
           144930, 148660, 152390, 156119, 159849, 163579, 167309, 171039, 174768, 178498, 182228, 185958, 189688,
           193418, 197147, 200877, 204607, 208337, 212067, 215797, 219526, 223256, 226986, 230716, 234446, 238175,
           241905, 245635, 249365, 253095, 256825]]
    攻击次数2 = 1
    CD = 50.0
    是否有护石 = 1
    
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 1.23
            self.倍率 = 1.16
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能25(主动技能):
    名称 = '龙神裁决：终末之光'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [(i*1.161) for i in [0, 149640, 184340, 219039, 253739, 288438, 323137, 357837, 392536, 427235, 461935, 496634, 531333, 566033,
           600732, 635431, 670131, 704830, 739529, 774229, 808928, 843628, 878327, 913026, 947726, 982425, 1017124,
           1051824, 1086523, 1121222, 1155922, 1190621, 1225320, 1260020, 1294719, 1329418, 1364118, 1398817, 1433516,
           1468216, 1502915, 1537615, 1572314, 1607013, 1641713, 1676412, 1711111, 1745811, 1780510, 1815209, 1849909,
           1884608, 1919307, 1954007, 1988706, 2023405, 2058105, 2092804, 2127504, 2162203, 2196902, 2231602, 2266301,
           2301000, 2335700, 2370399, 2405098, 2439798, 2474497, 2509196, 2543896]]
    攻击次数1 = 1
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能26(被动技能):
    名称 = '龙血誓约'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能27(主动技能):
    名称 = '龙咆雷鸣'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 121579.681
    成长 = 13727.4
    CD = 60.0


class 技能28(主动技能):
    名称 = '龙神君临·虚空烬灭'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 336533.014
    成长 = 101585.4
    CD = 290.0
    def 加成倍率(self, 武器类型):
         return 0.0

class 技能29(主动技能):
    名称 = '普通攻击（一轮）'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    基础 = 1114.6981
    成长 = 0
    CD = 1

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
    temp = i
    if i.是否有伤害 == 1 and i.是否有护石 == 1 and i.所在等级 != 45 and i.所在等级 != 70:
        护石选项.append(i.名称)
护石选项.append('魔龙之息')
护石选项.append('魔龙天翔')

符文选项 = ['无']
for i in 技能列表:
    temp = i
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.所在等级 != 48 and i.是否有伤害 == 1 and i.所在等级 != 45 and i.所在等级 != 70:
        符文选项.append(i.名称)
符文选项.append('魔龙之息')
符文选项.append('魔龙天翔')


class 职业角色属性(角色属性):
    实际名称 = '皓曦·龙骑士'
    角色 = '守护者'
    职业 = '龙骑士'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    类型选择 = ['物理固伤']

    类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.850

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[17].等级 = self.技能栏[16].等级

        if self.装备检查('守护的抉择'):
            if self.护石第一栏 == '魔龙之息':
                self.技能栏[self.技能序号['魔龙之息(脱手)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙之息(脱手)']].倍率 *= 1.55
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].倍率 *= 1.55
            if self.护石第二栏 =='魔龙之息':
                self.技能栏[self.技能序号['魔龙之息(脱手)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙之息(脱手)']].倍率 *= 1.45
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].倍率 *= 1.45
            if self.护石第一栏 == '魔龙天翔':
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].倍率 *= 1.55
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].倍率 *= 1.55
            if self.护石第二栏 =='魔龙天翔':
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].倍率 *= 1.45
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].倍率 *= 1.45

class 皓曦·龙骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业角色属性()
        self.角色属性A = 职业角色属性()
        self.角色属性B = 职业角色属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentText() != '无':
            if self.护石栏[x].currentText() not in ['魔龙天翔', '魔龙之息']:
                try:
                    self.护石类型选项[x].addItems(self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石选项)
                except:
                    self.护石类型选项[x].addItem('魔界')
                    self.护石栏[x].setCurrentIndex(0)
            elif self.护石栏[x].currentText() in ['魔龙天翔', '魔龙之息']:
                self.护石类型选项[x].addItem('魔界')
                self.护石类型选项[x].addItem('圣痕')
        else:
            self.护石类型选项[x].addItem('魔界')

    def 加载护石(self,属性):
        for k in range(3):
            if self.护石栏[k].currentText() != '无' and self.护石栏[k].currentText()!= '魔龙之息' and self.护石栏[k].currentText()!= '魔龙天翔':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(self.护石类型选项[k].currentIndex())
            elif self.护石栏[k].currentText()== '魔龙之息':
                if self.护石类型选项[k].currentText() == '魔界':
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].装备护石(0)
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].装备护石(0)
                elif self.护石类型选项[k].currentText() == '圣痕':
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].装备护石(1)
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].装备护石(1)
            elif self.护石栏[k].currentText()== '魔龙天翔':
                if self.护石类型选项[k].currentText() == '魔界':
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].装备护石(0)
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].装备护石(0)
                elif self.护石类型选项[k].currentText() == '圣痕':
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].装备护石(1)
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].装备护石(1)

        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()

        for i in range(0, 9):
            if self.符文[i].currentText() != '无' and self.符文效果[i].currentText() != '无' and self.符文[i].currentText() != '魔龙之息' and self.符文[i].currentText() != '魔龙天翔':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
            elif self.符文[i].currentText() == '魔龙之息':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].倍率 *= 1 + int(j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].倍率 *= 1 + int(j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].CD *= 1 + int(j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].CD *= 1 + int(j.replace('CD', '').replace('%', '')) / 100
            elif self.符文[i].currentText() == '魔龙天翔':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].倍率 *= 1 + int(j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].倍率 *= 1 + int(j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].CD *= 1 + int(j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].CD *= 1 + int(j.replace('CD', '').replace('%', '')) / 100       





