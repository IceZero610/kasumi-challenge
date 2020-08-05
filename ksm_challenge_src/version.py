log_file = [
    {
        "version": "Alpha 0.0.7",
        "log": """
极大的平衡性调整：
法术构筑现在有更多样的叠加法术倍率的选择；
lv3中的沉默技能不再会为boss增加上百点防御
角色基础生命窃取从60%降低至40%
角色基础暴击率从16%降低至11%
角色基础暴击倍率从175%降低至160%
Huntars种族的暴击伤害倍率加成从100%下调至75%
角色基础闪避值有轻微的下调
被动中的暴击伤害倍率从40%下调至30%
被动中的基础生命加成从50下调至30
被动中的法术倍率增加从8%上调至9%
"终极射手"组技能的攻击提高量从期望90下调至期望30
由这些变动，重新设计了四个boss的属性
其中黑帮老大现在会拥有更高的防御力和更少的生命，以让法术构筑有更好的表现
增加了更新日志的功能
错误修复：
修复了敏捷和感知增加的被动技能异常地提高属性值的问题
修复了可能过高的减甲可能会导致伤害变为1的问题
"""
    }, {
        "version": "Alpha 0.0.8",
        "log": """
游戏开始时玩家就会获得一定的MP，有机会在第一个回合使用技能
增加log向前查询的功能
错误修复：
修复了发起boss战可能会提前结束的错误
"""
    }, {
        "version": "Alpha 0.0.9",
        "log": """
lv2技能组的单体治疗目标从自身变为生命值最低的队友
【远距瞄准】技能增加一个期望40的攻击提升效果
若干涉及法术伤害提升的技能效果增加约50%左右的数值
"""
    }, {
        "version": "Alpha 0.0.10",
        "log": """
lv1增加"向阳"组效果，可以强化玩家的恢复强度。
lv3中的"净化"组技能，现在额外拥有一个降低目标恢复强度的效果
lv3中的"自然祝福"组技能，现在会为目标额外增加恢复强度
lv3中的"法力涌动"组技能，现在会为自身额外增加恢复强度
错误修复：
修复了多次攻击削弱buff导致攻击变为负数的情况，现在攻击最低为1
"""
    }, {
        "version": "Alpha 0.0.11",
        "log": """
【天使降临】组的治疗量从400下调至300，增加效果："使目标获得200点护盾并且在2回合内提升2点防御"
【强化治疗法术】组的治疗量从360上调到440
错误修复：
修复了lv3自然祝福恢复强度选择器错误的错误
"""
    }, {
        "version": "Alpha 0.1.0",
        "log": """
——战斗系统更新——
由生命值减少而增加的MP量从100%下调至75%
回合基础MP恢复从75上调至90
回合额外MP恢复范围从70上调至80
现在，所有的技能也会像普通攻击一样拥有一个效果数值的范围随机波动
——技能组更新——
lv3中[沉默]技能的持续时间从2c3下调至固定2回合
必杀技中的[终极射手]攻击提升效果从期望30上调至期望60，持续时间从1c2上调至固定2回合
增加了有关MP增加的技能效果，现在你可以在新建立的角色中选到这些技能
——Boss更新——
【黑帮老大】的基础攻击力期望从53.5上调至66
【黑帮老大】的[高爆手雷]技能伤害期望从220下调至200
【血色之鹰】的基础攻击力期望从185上调至215
【幽灵忍者】的攻击选择器从"RAND"变为"RAND_SAFE"，在仅有一个目标时不再多次攻击
添加了新的Boss【堕落教师】。和【幽灵忍者】一样，它是一个机制非常有趣，也有一点恶心的Boss，希望你们战斗愉快~
——用户系统更新——
现在Boss的强度参考值将会更加科学
现在转生的间隔由24小时减为12小时
在若干处增加了展示帮助的指令信息，方便新人熟悉系统
——系统更新——
现在玩家的状态效果使用了更好的管理机制，未来可能会推出分别针对增益效果和减益效果的技能
——错误修正——
当玩家在第30回合击败Boss时，系统会正常结算，不再会提示超时
"""
    }, {
        "version": "Alpha 0.1.1",
        "log": """
——Boss更新——
【堕落教师】的[偷换概念辩论]技能动态概率由10%上调至30%，移到2技能
【堕落教师】的[布置课堂作业]移到3技能
——错误修正——
Boss的强度参考值不再高到离谱
"""
    }, {
        "version": "Alpha 0.1.2",
        "log": """
——平衡更新——
修改了属性对应关系，现在：
敏捷将会影响防御和暴击倍率
力量只会影响生命上限
敏捷和力量共同影响攻击伤害
用户手册中的相关条目也对应地修改了
——错误修正——
修复了闪避不生效的错误

"""
    }, {
        "version": "Alpha 0.1.3",
        "log": """
——平衡更新——
【堕落教师】的生命窃取倍率从40%上调至90%，以平衡在沉默状态下战斗力过弱的问题
lv1中群体回复效果期望从25提升至38
lv1中自我治疗效果期望从70提升至80
lv1中自我护盾添加量从期望90上调至100
"""
    }, {
        "version": "Alpha 0.1.4",
        "log": """
——平衡更新——
【堕落教师】的基础攻击期望从195上调至210
【堕落教师】的基础防御期望从2.65下调至1.65
【堕落教师】的生命基础值期望从455下调至435
【堕落教师】的恢复强度期望从108%下调至102%
【堕落教师】的法术强度期望从105%下调至95%
【堕落教师】的生命窃取倍率从90%下调至70%
【堕落教师】的[错题审判]生命回复期望从530下调至330
【堕落教师】的[布置课堂作业]法术伤害期望从70上调至170
【堕落教师】的[自我否定误导]更名为[点名批评]，法术伤害期望从365上调至440，额外增加一个生命恢复效果
"""
    }, {
        "version": "Alpha 0.1.5",
        "log": """
——平衡更新——
技能组中效果为百分比攻击提升技能现在拥有更高的倍率和更长的持续时间
lv3中造成魔法伤害并提升法术倍率的技能伤害期望从110下调至100，法术倍率提高期望从12.5%上调至20.5%，持续时间由8c10下调至6c8
lv3中提升法术倍率并提升恢复强度的技能法术倍率提高期望从29.5%上调至42%
增加了[迅猛冲拳]组技能，在当回合提升自身攻击并进行一次普通攻击
[天使降临]技能的治疗量期望从300下调至260
[守护天使]技能的护盾量期望从200下调至160
[魔力过载]技能的法术倍率提高期望从99%上调至120%，额外为自己添加期望170的护盾
"""
    }, {
        "version": "Alpha 0.1.6",
        "log": """
——【黑帮老大】平衡性调整——
攻击力由期望66下调至53
[机枪扫射]由6次攻击上调至7次
防御基础值由期望3.75下调至3.05
增益幅度由120%下调至110%
暴击伤害倍率由150%上调至210%
暴击率由12%上调至14%
[高爆手雷]伤害由期望200下调至190
[高精度瞄准镜]暴击率提高从期望16%上调至55%
[寻找掩体]闪避提升由15%提升至50%，额外为自己添加一个期望220的护盾
——技能组调整——
lv1中的MP增加技能由期望47.5上调至90
lv2中群体MP增加技能由期望47.5上调至65
lv3中伤害队友并增加MP的技能，MP增加期望由160上调至230
"""
    }, {
        "version": "Alpha 0.1.7",
        "log": """
——系统更新——
现在，所有的技能冷却时间不会在本回合结束时立即减少，这意味着1回合冷却的技能将会隔1个回合才会发动
——平衡性调整——
【堕落教师】的[错题审判]冷却时间由2降低为1以适应新的冷却机制
lv3的[奥术强化攻击]组法术伤害提升效果由期望20.5%提升至25.5%，但是持续时间由6c8下调至3回合
lv3的[强力一击]攻击提升效果期望由50%下调至38%
"""
    }, {
        "version": "Alpha 0.1.8",
        "log": """
——平衡性调整——
现在，天赋中每个属性的天赋每级的属性提升由1.5下调至0.75
天赋中每个属性成长的天赋每级成长的属性由0.03上调至0.05
Human种族的额外生命基础加成由20上调至27
Shadoul种族的闪避加成由25%下调至21%，生命值减少量由20%下调至15%
Eledrin种族的力量减少量由6下调至4，敏捷和感知的增加量由9下调至8
"""
    }, {
        "version": "Alpha 0.2.0",
        "log": """
——重大更新——
必杀技增加了一个新的技能组：[嗜血渴望]，短时间内小幅度提高自己的攻击，并大幅度提高自己的生命窃取倍率。
增加了一个新的Boss【食尸恶灵】。和【堕落教师】一样，它同样也是一个机制有趣，也有一点点恶心的Boss，运气不好的话，也许会和它鏖战到超时……？希望每个人都能找到乐趣！
增加了游戏更新日志的推送功能，群管理员可以使用"ksmgame-autolog"指令在开启和关闭间切换
——平衡调整——
lv1和lv2中的攻击百分比提升效果将会更强
[远距瞄准]组技能的攻击提升期望由36%下调至30%，持续时间由4c5下调至3回合
[衰弱巫术]组技能的攻击降低由期望40%下调至27%，持续时间由3上调至4回合
必杀技中
[死亡射线]组技能伤害期望由280上调至310
[毁灭之雨]组技能伤害期望由150上调至168
[狂怒战神]组技能攻击提升期望由260下调至200
[强化治疗法术]组技能的治疗量由190上调至205
[守护天使]组技能的护盾量由160上调至170
[残废]组技能持续时间由3下调至2回合
[沉默的猎杀者]组技能攻击提高由期望60下调至42
——错误修正——
修正了回复量减少的状态效果减少量小于预期的错误
修正了百分比攻击提高的攻击提升效果还会额外受到增益幅度加成的影响
"""
    }, {
        "version": "Alpha 0.2.1",
        "log": """
——用户界面更新——
沉默与净化的提示更简练
——系统更新——
现在维护bot前后会有提示
转生频率限制降低到5小时
🎉本项目已于GitHub开源，如果你对项目开发、Boss设计、游戏平衡等方面有任何建议，欢迎给开发者发送Issue或者PR。
项目地址：https://github.com/rMuchan/kasumi-challenge
"""
    }, {
        "version": "Alpha 0.3.0",
        "log": """
——Boss更新——
【食尸恶灵】重做。由于平衡幅度比较大，已经接近于重做了所以这里就偷懒不写更新日志了(
【黑帮老大】的[机枪扫射]不再会平均地选择目标。
【堕落教师】的[点名批评]不再为自己回复生命，取而代之的是一个护盾.
高等级的Boss现在会有更强的战斗力。
——平衡更新——
主技能的MP消耗量减少由12加强至30
lv3中[攻击削弱]组技能现在效果变为对敌方全体，但是削减量减半。
重新平衡了必杀技的各项数值。
——系统更新——
现在当护甲衰减至最低时，会使普通攻击伤害提高至250%
攻击衰弱效果现在会拥有更小的波动
——错误修正——
修正了攻击倍率没有如期影响实际攻击力的错误
修正了敏捷没有如期影响实际暴击率的错误
"""
    }, {
        "version": "Alpha 0.3.1",
        "log": """
——系统更新——
重写了用户手册，你可以使用"ksmgame-help"看看重写后的用户手册！
创建角色时，被动加成的选择移到技能选择完毕之后。
加入了更多的提示以帮助新人上手。
——错误修正——
修复了bot被口球时游戏不能正确结束的bug。
修正lv3中[攻击削弱]组技能描述的typo。
修正天赋描述的格式。
"""
    }, {
        "version": "Alpha 0.3.2",
        "log": """
——平衡更新——
现在，绝大多数的状态效果的效果数值将会拥有更小的波动。
——错误修正——
改正了【堕落教师】简介中的文字错误
修复了降低攻击的技能效果得到施法者本身的增益幅度加成，使得在高加成的情况下目标攻击降至0的情况。
"""
    }, {
        "version": "Alpha 0.3.3",
        "log": """
——系统更新——
现在，玩家创建新的角色时，新角色的属性值将会更加稳定一些。这意味着玩家将更不容易获得高到极端或是低到极端的属性。
攻击百分比下降的技能不再以加法叠加的方式生效，而是变为乘法叠加。这意味着，多个攻击衰减的效果不再会轻易地让目标的攻击力降到0以下，相对的在有攻击力提升的情况下，攻击衰减的效果将会更加显著。
——Boss更新——
为了削弱【食尸恶灵】在[猎杀形态]下过于强大的表现，它的生命窃取倍率从36%下调至21%，为了平衡其在其他状态下的作战表现，它的[饕餮盛宴]生命窃取倍率从期望79%上调至94%，[肢体重构]的治疗量由期望241.5上调至251.5。
玩家们实在是太优秀了！【幽灵忍者】的恢复强度期望由105%上调至110%，暴击率由75%上调至79%。
——错误修正——
我惊讶地发现我错误地将【幽灵忍者】[遁入暗影]技能的治疗量填写到了错误的变量中，现在，[遁入暗影]的治疗量将会变得正常。
"""
    }, {
        "version": "Alpha 0.3.4",
        "log": """
我更新了一系列文档和《Boss设计手册》，欢迎所有玩家一起设计Boss。
手册地址：https://github.com/rMuchan/kasumi-challenge/blob/master/doc/Kasumi%20Challenge%20Boss%E8%AE%BE%E8%AE%A1%E6%89%8B%E5%86%8C.md
——系统更新——
现在，每个玩家同时只能参与一场战斗。请好好享受和朋友们一起嘲笑不停叠Buff和叠了Buff又Miss的大兄弟的过程，不要为了刷而刷！
"""
    }, {
        "version": "Alpha 0.4.0",
        "log": """
被动与种族加成重做：
现在，种族对角色的影响将会更小，取而代之的是玩家将会拥有更多且更强被动的选择。
开发者评论：设计种族的初衷是希望不同的玩家可以根据自身不同的种族选择更合适的构筑，以此来避免构筑过于单一化的问题。现在的平衡性已经令玩家们有了更多的选择，许多玩家也表示不希望被种族所束缚。所以我做出了这样的修改，希望新的构筑方法也能令你们感到开心~
一些和物理构筑相关的技能将会有更高的出现概率。
"""
    }, {
        "version": "Alpha 0.4.1",
        "log": """
——错误修正——
现在，所有的Buff的持续时间将会在每一轮结束之后统一结算，以避免出现为自己先行动的目标添加Buff之后持续回合比预期长1回合的问题。
"""
    }
]
