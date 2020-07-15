import data

numerical = data.numerical


# 以下到类声明之前的所有函数都会用于战斗直接相关的属性的生成，在类中无需记录基础三属性 ----


# 属性计算
def attr_calc(attr_base, attr_grow, lv):
    current = attr_base
    for _ in range(lv - 1):
        current = current * (numerical['attr_rate']) + attr_grow
    return current


# 攻击计算
def atk_calc(int_cur):
    return int_cur * numerical['atk_rate']


# 血量计算  -  modify基本上就是给Shadoul用的了(
def hp_calc(str_cur, life_base, life_grow, lv, modify):
    current = str_cur
    for _ in range(lv - 1):
        current = current * numerical['hp_lv_rate'] + life_grow
    hp = life_base + current
    hp *= numerical['hp_rate'] * modify
    return hp


# 防御计算
def def_calc(str_cur, int_cur, defense_str_rate, def_base, extra):
    adj = str_cur * defense_str_rate + int_cur * (1 - defense_str_rate)
    return adj * numerical['def_adj_rate'] + def_base + extra


# 暴击率增益计算
def crit_rate_calc(str_cur, int_cur, defense_str_rate, def_base, extra):
    adj = str_cur * defense_str_rate + int_cur * (1 - defense_str_rate)
    return adj * numerical['def_adj_rate'] + def_base + extra


# 下面会有三个基于属性的技能强化率的计算会用到这个函数
def attr_based_enhance(attr):
    return numerical['enhance_constant'] * (attr ** numerical['enhance_exponent'])


# 护盾与治疗倍率
def recover_rate_calc(per_cur, str_cur, health_per_rate):
    return attr_based_enhance(per_cur * health_per_rate + str_cur * (1 - health_per_rate))


# 魔法伤害增强 - 对于Magecian种族，mage_rate会有更高的数值
def spell_rate_calc(int_cur, per_cur, magic_int_rate, extra):
    return attr_based_enhance(int_cur * magic_int_rate + per_cur * (1 - magic_int_rate)) * extra


# 增益类技能效果增强
def buff_rate_calc(per_cur):
    return attr_based_enhance(per_cur)


# 闪避
def dodge_calc(per_cur, extra):
    return numerical['dodge_base'] + extra + per_cur * numerical['dodge_rate']


chara = dict(str_cur=50,
             int_cur=50,
             per_cur=50,
             defense_str_rate=0.5,
             magic_int_rate=0.5,
             health_per_rate=0.5,
             life_base=200,
             life_grow=5,
             HP=200,
             defence=3,
             attack=80
             )