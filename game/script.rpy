# 自动转换的Ren'Py剧本

# 强制初始化持久化数据（使用default确保编译时定义）
default persistent.achievements = {}

init:
    # 位置变换
    transform trueleft:
        xalign 0.0
    transform leftish:
        xalign 0.1
    transform left:
        xalign 0.2
    transform slight_left:
        xalign 0.3
    transform center:
        xalign 0.5
    transform slight_right:
        xalign 0.7
    transform right:
        xalign 0.8
    transform rightish:
        xalign 0.9
    transform trueright:
        xalign 1.0
    transform farleft:
        xalign -0.15
    transform farright:
        xalign 1.15
    transform maxleft:
        xalign -0.5
    transform maxright:
        xalign 1.5
    # 背景图片
    image bg black = "#000"
    image bg white = "#fff"
    image bg classroom = "images/bg_classroom.jpg"
    image bg library = "images/bg_library.jpg"
    image bg dorm = "images/bg_dorm.jpg"
    image bg cafeteria = "images/bg_cafeteria.jpg"
    image bg lake = "images/bg_lake.jpg"
    image bg city = "images/bg_city.jpg"
    image bg hospital = "images/bg_hospital.jpg"
    image bg shanghai = "images/bg_shanghai.jpg"
    image bg metro = "images/bg_metro.jpg"
    image bg restaurant = "images/bg_restaurant.jpg"
    image bg phone = "images/bg_phone.jpg"
    image bg night = "images/bg_night.jpg"
    image bg monika_room = "images/bg_monika_room.jpg"

    # 角色立绘 - 自动生成所有使用的图片定义
    image o_mean = "images/o_mean.png"
    image bg bbq = "images/bg_bbq.png"
    image o_normal = "images/o_normal.png"
    image s_understanding = "images/s_understanding.png"
    image c_happy = "images/c_happy.png"
    image o_surprise = "images/o_surprise.png"
    image s_joke = "images/s_joke.png"
    image bg_classroom = "images/bg_classroom.png"
    image s_bbq = "images/s_bbq.png"
    image s_hug = "images/s_hug.png"
    image o_cute = "images/o_cute.png"
    image s_happy = "images/s_happy.png"
    image c_normal = "images/c_normal.png"
    image bg classroom = "images/bg_classroom.png"
    image bg_dormnight = "images/bg_dormnight.png"
    image bg_dormday = "images/bg_dormday.png"
    image s_normal = "images/s_normal.png"

    # 音乐和音效
    define audio.main_theme = "audio/main_theme.ogg"
    define audio.happy_music = "audio/happy_music.ogg"
    define audio.sad_music = "audio/sad_music.ogg"
    define audio.mystery_music = "audio/mystery_music.ogg"
    define audio.romantic_music = "audio/romantic_music.ogg"
    define audio.your_reality = "audio/your_reality.ogg"
    define audio.sayo_nara = "audio/sayo_nara.ogg"
    define audio.phone_ring = "audio/phone_ring.ogg"
    define audio.door_open = "audio/door_open.ogg"
    define audio.rain = "audio/rain.ogg"

# 角色定义
define me = Character("我")
define mind = Character("内心", color="#888888")
define sayori = Character("Sayori", color="#ff66aa")
define cordelia = Character("Cordelia", color="#6666ff")
define obedience = Character("Obedience", color="#ffaa00")
define monika = Character("Monika", color="#00aa00")
define teacher = Character("老师", color="#8888ff")
define leo = Character("Leo", color="#ff6666")
define stranger = Character("陌生人", color="#aaaaaa")
define waiter = Character("服务员", color="#aaaaaa")
define shane = Character("Shane", color="#aaddff")
define monika、sayori、cordelia、obedience、我、shane、teacher = Character("Monika、sayori、cordelia、obedience、我、shane、teacher")
define mxnlke = Character("Mxnlke")
define moment = Character("Moment")
define 回忆中的sayori = Character("回忆中的sayori")
define 微信里的me = Character("微信里的me")
define paper = Character("Paper")
define voice = Character("Voice")
define 门的对面 = Character("门的对面")
define DDOS = Character("Ddos")
define everyone = Character("Everyone")
define obedience_and_cordelia = Character("Obedience And Cordelia")
define 微信里的shane = Character("微信里的shane")
define telephone = Character("Telephone")
define staff = Character("Staff")
define dorm_staff = Character("Dorm Staff")
define 尚睿洋 = Character("尚睿洋")
define DDLC = Character("Ddlc")
define 微信里的sayori = Character("微信里的sayori")
define everyone_else = Character("Everyone Else")
define nnxnIk3 = Character("Nnxnik3")
define mxnika = Character("Mxnika")

# 成就系统函数
init python:
    # 成就分类
    hug_achievements = ["拥抱1", "拥抱2", "拥抱3", "拥抱4", "拥抱5", "拥抱6", "拥抱7", "拥抱8", "拥抱9", "拥抱10", "拥抱11", "拥抱12", "拥抱13", "拥抱14", "拥抱15"]
    school_achievements = ["脚大1", "脚大2", "脚大3", "脚大4", "脚大5", "脚大6", "脚大7"]
    ending_achievements = ["结局1", "结局2", "结局3", "结局4", "结局5", "结局6", "结局7", "结局8", "结局9"]
    possibility_achievements = ["另一种可能1", "另一种可能2"]
    
    def grant_achievement(achievement_name):
        # 确保持久化数据已初始化
        if persistent.achievements is None:
            persistent.achievements = {}
        persistent.achievements[achievement_name] = True
        renpy.save_persistent()  # 立即保存持久化数据
        
    def check_achievement_group(group_name):
        # 确保持久化数据已初始化
        if persistent.achievements is None:
            persistent.achievements = {}
            
        if group_name == "hug":
            achievements_list = hug_achievements
        elif group_name == "school":
            achievements_list = school_achievements
        elif group_name == "ending":
            achievements_list = ending_achievements
        elif group_name == "possibility":
            achievements_list = possibility_achievements
        else:
            return False
            
        for achievement in achievements_list:
            if achievement not in persistent.achievements or not persistent.achievements[achievement]:
                return False
        return True

define 微信里的助教 = Character("微信里的助教")
define log = Character("Log")
define S_mind = Character("S Mind")
define cordelia_and_obedience = Character("Cordelia And Obedience")
define everyone_else = Character("Everyone Else")
define C_mind = Character("C Mind")
define evryone_except_monika_and_sayori = Character("Evryone Except Monika And Sayori")
define 吐出了东西的sayori = Character("吐出了东西的sayori")
define cordelia的舍友 = Character("Cordelia的舍友")
define 记忆里的me = Character("记忆里的me")
define 嘴里堵着东西且被捆起来的sayori = Character("嘴里堵着东西且被捆起来的sayori")
define mom = Character("Mom")
define clerk = Character("Clerk")

# Monika线专用变量
default monika_count = 0
default in_sayori_route = False
default monika_triggered = False

label start:
    play music main_theme fadein 2.0
    scene bg black
    jump chapter1

label chapter1:
    $ in_sayori_route = False
    scene bg bbq with dissolve
    mind "经过了人生中最漫长的暑假和军训,我的大学生活就这样拉开了序幕。"
    mind "难以想象啊,不久前的我还在想高考和朋友去向的事情,现在感觉已经好遥远好遥远……"
    mind "朋友们也在遥远的地方呢……"
    mind "悠远的苍穹吗。哈哈,这倒是让我想到最近玩的《缘之空》了。"
    mind "世界就在我身边,却时刻提醒着我它和我之间的距离,这就是孤独吧。此刻的我正是一个人在玉兰苑门口吃烧烤。"
    $ grant_achievement("脚大1")
    # 成就: 脚大1
    mind "孤独是不可避免的,我想,假如没有朋友的话。这个时候我就想像《间谍过家家》里的阿尼亚一样大喊一声：“A~ Anya haha muha somisi~”（阿尼亚想要妈妈的关爱）"
    mind "…………"
    sayori "Ohayou！！！（日语里的“早上好”）"
    me "啊啊啊啊啊？！"
    show s_normal at left
    play music quiet fadein 2.0
    me "呼,是你呀,sayori。吓我一大跳。我差点忘了你也来脚大了。"
    mind "坐在烧烤摊门外的椅子上胡思乱想,突然被萌萌的sayori跳脸了,差点心脏骤停……"
    mind "不过,sayori总是喜欢突然蹦出来吓人……自从我认识她,她就是这个性子。我啥时候认识她的……那应该是我们很小很小的时候？"
    hide s_normal
    show s_happy at center
    sayori "呐呐,又开始发呆了？"
    me "诶诶？"
    mind "怎么突然拉着我就走啊,我还没emo完呢……"
    sayori "班会要开始了,快走快走……你去扫辆车吧,我马上跟上。"
    hide s_happy
    mind "虽然说好像是这样,但总感觉她不是因为这个拉我……"
    mind "悄悄回头看看……啊,果然如此……"
    show s_bbq at right
    sayori "诶嘿……啊呜啊呜,被发现了吗~"
    # 动作: 手拿烤串
    me "太明显了……而且多少年都是这样吧,你突然作妖绝对是因为吃的。"
    sayori "嘿嘿……早就在意料之中了喵？不过确实很好吃。"
    me "重点不是味道啊喂！我的emo时间就这样被打断了,这个才是重点吧！"
    hide s_bbq
    show s_joke at center
    sayori "不要不开心啦,我不就是因为这个才过来的吗？"
    sayori "一个人吃烧烤真的好~惨~啊~呜呜呜,且让你的超绝可爱青梅替你分担一些吧~"
    me "再不去班会就真要迟到了啊！！"
    hide s_joke
    mind "结果是：sayori吃完了剩下的烤串,但是班会课迟到了……"
    jump chapter2
label chapter2:
    $ in_sayori_route = False
    scene bg classroom with dissolve
    teacher "好的,人终于齐了！大家来做自我介绍吧！我们班人比较多,所以大家简单介绍下自己的爱好就行了……"
    mind "这么突然？我还没准备好呢！"
    mind "一个长头发的漂亮女生走上讲台,步子走得很沉稳,看来受过良好的教育。"
    show c_normal
    cordelia "大家好,我是cordelia。我的爱好只有数学和钢琴,不过平时我是个循规蹈矩的人,可能有点无聊……学习搭子和音乐发烧友可以找我。嗯,就这样。"
    hide c_normal
    mind "怎么会有人把数学当爱好啊……脚大全是卷狗吧。"
    show o_normal
    obedience "我叫obedience,我的爱好很多……我喜欢写散文、烘焙、游泳、摄影和吹葫芦丝,我还喜欢玩原神和看帅哥……欢迎大家来找我玩！"
    hide o_normal
    show s_joke at left
    sayori "到我啦,让我过一下。"
    me "哦,好的……"
    hide s_joke
    show s_hug
    sayori "Ohayou！！（日语里的“早上好”）"
    # 动作: 走上讲台
    me "我就知道……"
    # 动作: 扶额
    sayori "我是sayori,我喜欢写诗。大家可以来找我哦,我超喜欢交朋友的！有什么不开心的也可以跟我说,我一定会让大家开心起来的~"
    hide s_hug
    mind "她的确能……也许我应该多和sayori一起玩。……好像漏听了好几个人,不管了,该到我了吧？"
    teacher "下课了,还有没做自我介绍的吗？啊……好的,没有了,下课吧！"
    me "诶诶,老师,这里……"
    me "被无视了……大家都走了吗。"
    me "教室里好吵啊……"
    show s_understanding
    sayori "老师能有什么坏心思呢,老师只是急着下班罢了。"
    # 动作: 拍肩
    mind "……世界平静了。"
    me "……谢谢你,sayori。"
    sayori "呆jio不~（日语里的“没关系”）明天见啦！"
    me "……嗯,我也回去吧。"
    hide s_understanding
    show bg_dormnight
    mind "军训期间看起来非常摆的舍友似乎都开始内卷了,参加了一大堆比赛,可我还什么都不会呢……大家都在熬夜学习呢……"
    mind "我好像又开始emo了。这是不是我高考考到这的原因呢……"
    mind "但凡再高一点点,也不至于来这里了……这个学院老是被群嘲,可是学院里的人还这么卷,那我怎么办……"
    jump chapter3
label chapter3:
    $ in_sayori_route = False
    show bg_dormday
    mind "…………"
    mind "啊,醒了。数学早十！快跑快跑。"
    show bg_classroom
    show c_happy at farleft
    show s_happy at center
    me "早上好,sayori！有座位吗？"
    sayori "这里这里！cordelia坐我旁边啦,你坐我后面吧？在obedience旁边。"
    me "这么快就认识新朋友了啊？大家好大家好……"
    show o_cute at farright
    obedience "哈喽哈喽！我叫obedience,很高兴认识你……"
    teacher "Silence, please! I'm Professor Cai, and welcome you all to the maths' world!"
    hide c_happy
    hide s_happy
    hide o_cute
    mind "为什么中国人要讲英语啊……课本身难度倒是还好。真是漫长的一节课。"
    show s_understanding
    sayori "终于下课了……大家听得怎么样？"
    show o_normal at farright
    obedience "好难啊！他说了好多我听不懂的东西,好多新名词,感觉没上过这么难懂的数学课。比我高中那个老师帅倒是真的,那个老师……"
    hide o_normal
    show c_normal at farleft
    cordelia "嗯……其实还好吧。"
    show o_surprise at farright
    obedience "诶？？可是他一开始讲的那一串东西我就没听懂,比如说……"
    cordelia "他不就是简单介绍了一下背景知识吗？“现代数学的基础是类型论、集合论、范畴论……”大概就是这些吧。"
    obedience "嗯……"
    hide o_surprise
    hide c_normal
    hide s_understanding
    me "讲得这么简单,我们怎么跟电院的比啊……"
    $ grant_achievement("脚大2")
    # 成就: 脚大2
    show s_happy
    sayori "别这么想,我们以后也有比他们难的课吧。"
    show o_mean at farright
    obedience "嘿嘿,比不过也是很正常的。电爷比我们强难道不是事实吗？"
    me "噗……所以你玩了一节课手机是吧。"
    obedience "诶诶,被发现了吗？我只是……偶尔溜下号啦,其实我还是在听的。"
    show c_normal at farleft
    cordelia "上课不认真听课是不对的。"
    sayori "好啦好啦,这栋教学楼附近没食堂,大家都要先回宿舍放书包再吃饭吧？走咯~"
    hide c_normal
    hide o_mean
    hide s_happy
    "跟谁一起走？"
    menu:
        "sayori":
            jump chapter6
        "cordelia":
            jump chapter7
        "obedience":
            jump chapter8
label chapter6:
    $ in_sayori_route = False
    sayori "走吧走吧。哇,你看路上还有松果！好多好多！"
    me "那个不砸开就不能吃的。"
    sayori "诶,这样啊……不过松鼠也很可爱！"
    mind "sayori说了些啥？其实我没太认真听……"
    sayori "……抱一下。"
    me "嗯？什么……"
    mind "我还没反应过来呢,sayori突然抱了抱我。"
    $ grant_achievement("拥抱1")
    # 成就: 拥抱1
    sayori "你最近一定遇到了不开心的事情吧。不想说也可以不说,我会陪着你的。"
    me "sayori……"
    stranger "不好意思,让一下让一下！"
    me "哇！"
    stranger "没事吧？不好意思,自行车刹车坏掉了……我叫monika。"
    sayori "呆~jio~不~（转向我）那么,拜拜！下午见啦！"
    me "拜拜……"
    mind "我们向三个方向走去。"
    mind "清醒一下,这不是表白,sayori总是会拥抱不开心的人……"
    mind "不过,我表现得这么明显吗？"
    jump chapter10
label chapter7:
    $ in_sayori_route = False
    cordelia "你和我一起走？好吧……"
    mind "cordelia一直在用手机打字。我们无言地一起走了一段路,好尴尬……"
    mind "马上就到宿舍了,这时突然看到一辆自行车向我们冲过来……"
    me "危险！"
    # 动作: 拉住cordelia的手
    cordelia "啊！"
    stranger "不好意思,刹车坏了……我叫monika。"
    me "注意道路安全啊。人没事就算了,你走吧。"
    monika "（表情复杂地离开了）"
    cordelia "谢谢你了……"
    jump chapter10
label chapter8:
    $ in_sayori_route = False
    obedience "太好了！有人和我一起走了！耶耶耶~"
    mind "倒也犯不着这么激动吧……"
    obedience "你的假期是怎么过的？我假期学习了烘焙,本来想做个戚风蛋糕的,结果完全发不起来……"
    mind "她真的想让我回答吗？"
    obedience "……后来发现是蛋白霜的问题,里面混了一点点蛋黄,我按教程往里面加了醋……"
    me "哈哈,那个……"
    obedience "……结果加多了,厨房里全是酸味！最后把实验品给我妈做菜用了,我又打了一次鸡蛋……"
    me "不好意思,我要走了！呃……我的宿舍在那边,拜拜！"
    obedience "……啊哦。（小声）又搞砸了吗……"
    mind "神经病啊！话比sayori还多,而且sayori至少会关心我在不在听……"
    stranger "让一下啊啊啊！"
    mind "什么？自行车！！啊啊啊……擦肩而过"
    stranger "（风驰电掣地骑过去了）刹车坏了,对不起！我叫monika——"
    mind "怎么今天老是碰到神经病啊……"
    jump chapter10
label chapter10:
    $ in_sayori_route = False
    mind "下午,我们上了第一节工程课。这门课要求我们自由分组完成项目,每个组最多四人,项目报告占学期评价的大部分分数。"
    sayori "锵锵！你甩不掉我的。"
    me "谁要甩掉你了……你要当组长的话我就和你一起。"
    sayori "切……那作为建组元老,你当副组长。"
    me "官职还挺多……应该借此机会熟悉其他同学吧？不能一直只和sayori聊天的。"
    sayori "切,你还是嫌弃我了……小组又不一定只有两个人,我们再去拉人就可以啦。"
    obedience "打扰一下,请问我可以加入吗？"
    me "诶？"
    obedience "我应该先道歉……上午我的话说得有点多,不过我一直都是这样子的,我其实只是想认识大家,没有恶意……"
    sayori "停停停,这个道歉也够长的。我代表他接纳你啦。欢迎欢迎！"
    me "被组长大人代表了吗,哈哈哈……别放在心上啦。"
    cordelia "嗯,既然这样,我可以加入吗？"
    sayori "哇哦~美女姐姐！欢迎呀！"
    mind "……总之似乎什么也没做就分好了组。"
    me "大家都学过编程吗？"
    cordelia "我对C语言略有了解。"
    everyone_else "…………"
    obedience "抱大腿抱大腿……"
    cordelia "别这么说……我第一次用循迹机器人,这个你们有经验吗？"
    everyone_else "…………"
    sayori "不要灰心,大家都是这么过来的！我们先分分任务吧：cordelia负责编程相关的事情,obedience可以写实验报告……"
    obedience "是因为我比较笨吗？"
    sayori "怎么会呢,主要是觉得你比较会水字数……（转向我）你来做实验验证。我来给你们三个打杂,最后的展示环节也可以由我来做。"
    me "（小声）组长大人好悠闲。"
    sayori "嘿嘿。"
    mind "实际上sayori确实没闲着。sayori似乎什么都会一点,所以她轮流帮助所有人。但更重要的是帮助我们沟通。接下来的一周我们都忙于这个项目,进展不是很顺利。"
    jump chapter11
label chapter11:
    $ in_sayori_route = False
    mind "实验做得心情好郁闷啊……为什么测出来的东西这么诡异呢？何意味？"
    mind "手机响了……shane给我发消息了？说起来这几天还真没怎么联系他……高中的时候每天都在一块的。"
    微信里的shane "Hello~您订的超级无敌火鸡面到了,请慢用~"
    mind "随后是一张火鸡面的表情包。又是什么整人小技巧吗……"
    微信里的me "好吃好吃~"
    微信里的shane "哎呀,好像多给您加了一个伟大的太阳蛋~请您补两块钱差价呢~"
    微信里的me "我还给你吧（发出了一个鸡蛋的表情包）"
    微信里的shane "不可以哦~这样的话,您会被拉进黑名单的,您就再也不可以点这个超级无敌火鸡面了。"
    微信里的me "（真的支付了2块钱）"
    微信里的shane "感谢您呢,现在要登记您的手机号码呢亲~"
    mind "嘻嘻……机会来了,给他整点小惊喜……"
    mind "我走到宿舍楼下。那里停着很多哈啰单车,我对其中的一辆记忆特别深刻。"
    me "啊……找到你啦。"
    mind "我快速地记下了一串号码,然后发过去。"
    微信里的shane "不是,怎么是江西的号？"
    微信里的me "不装可爱了,亲~"
    微信里的shane "我真打了？"
    微信里的me "我劝你别这么做~不过如果你愿意,嘿嘿,我支持你~"
    微信里的shane "什么啊,那我挂了。可是他又打过来了,我不敢接。"
    微信里的me "不是哥们,你真打了啊？"
    微信里的shane "你到底发了个什么给我？"
    mind "太好笑了……如果以后我要写剧本什么的,一定要把这件事写进去……"
    mind "我发过去一张图。上面是一辆单车,贴着小广告,上面写着：男科医生某某某,电话号码XXX。"
    微信里的shane "（很文明的用语）"
    mind "这大概就是忙着做实验的那些天里,唯一的乐趣。"
    jump chapter12
label chapter12:
    $ in_sayori_route = False
    mind "deadline前的一个晚上,我终于完成了所有实验。我提交了数据,然后睡了。第二天,我还没走进实验室,就听见了激烈的争吵声……"
    $ grant_achievement("脚大3")
    # 成就: 脚大3
    obedience "……真的没办法了,我也不想这样的！但试验数据就做成这个样子了,难道就这么交上去吗？"
    cordelia "再给我一点时间,肯定是代码出了什么问题……"
    obedience "后天就是deadline了,哪里来的时间？sayori还需要准备展示环节,不能再拖了！"
    cordelia "……可是即使如此也不能篡改实验数据！这是严重的学术不端,违反诚信守则……"
    obedience "你还真信这些啊？我在实验室都听到有人说要改。而且别说得那么难听啊,就当做有几组数据你觉得不合理舍掉了不就好了吗。"
    cordelia "……对不起,我做不到,这个真的不行。比起分数,我更在意的是荣誉……"
    obedience "别当圣母了,你不在意分数,我还在意呢。至少,他们俩不应该为你的理想而牺牲吧？"
    cordelia "……我知道,要是我的代码没写错就没那么多事了,但是……我们可能会被处分的。"
    me "真的不会那么糟糕的,好多人都这么做呀。"
    obedience_and_cordelia "诶？你在门后面吗？"
    me "听我说,cordelia,我理解你的意思,我也很赞赏你的正直,但是我们确实没有时间了,所以……"
    cordelia "（难以置信地看着我）你也这么认为吗？"
    mind "我动摇了。这么做真的对吗？我该怎么办？"
    "怎么解决冲突？"
    menu:
        "现场重做实验,万一现在好了不就不用修改数据了嘛。":
            jump chapter13
        "快去找sayori调解！":
            jump chapter14
        "弃暗投明,和cordelia站在一起。":
            jump chapter15
        "能拿到分就好,和obedience站在一起。":
            jump chapter16
label chapter13:
    $ in_sayori_route = False
    me "先别管我怎么想了,再做一次实验！"
    mind "我第一次后悔自己没有精雕细琢自己的实验方案,实际上好多地方都会产生误差……我尽力了。"
    cordelia "（捂脸）不是你的错,“误差”都到百分之三十了,肯定是代码的某个地方有问题,但是我看不出来……"
    obedience "（拍了拍cordelia）你都做不出来,我们就更不行了。听我的吧,真的不会有人一份一份检查的。"
    mind "这样真的好吗……要不,还是去找下sayori？毕竟她才是组长啊。"
    jump chapter17
label chapter14:
    $ in_sayori_route = False
    me "我听组长的。sayori在哪里？"
    mind "sayori不在,不过一个电话就把她叫过来了。我在电话里向sayori解释了一下前因后果。"
    sayori "cordelia,不要自责,你很有正义感,你不需要因此而感到难过。当然obedience也不是坏人,她只是想让所有人利益最大化,这也很正常……"
    cordelia "（哭泣）对不起……我没有做好我的部分,现在又给大家添堵了……我只是过不去这道坎……"
    mind "sayori露出了少见的严肃表情。"
    sayori "我要一个人想一想,半小时内先别找我。"
    mind "走了？？"
    mind "实验室里一点声音都没有,我们还是不知道该怎么选……时间在流逝……"
    jump chapter17
label chapter15:
    $ in_sayori_route = False
    me "……你是对的。我们不能修改报告,就这么提交吧。"
    obedience "你疯了吧？百分之三十的“误差”,你敢给这样的作业合格吗？"
    me "现在sayori不在,二对一。少数服从多数。"
    obedience "好,我明白了……你选择了她。"
    mind "这似乎是《哈利波特》里罗恩对赫敏说的话吧？？"
    obedience "你们不在意我的分数,我不难过。可是sayori呢？你们真的愿意让她也拿C?"
    me "不要拿别人当挡箭牌了。分数可以低,但必须要干净。我相信sayori也会支持我们的。"
    cordelia "虽然你支持我让我很感激,但是sayori真的会这么想吗……"
    me "我从小就认识她,我相信她会的。"
    mind "其实我心里完全没底。而且就算她支持,又怎么样？四个人一起拿低分吗？我的思绪乱七八糟……"
    jump chapter17
label chapter16:
    $ in_sayori_route = False
    me "……我不知道你为什么突然不对劲了,但这对你也不好。为了包括你在内的所有人的利益,我们必须这样做！"
    obedience "她刚刚还说,如果我们真那么做就举报呢。"
    cordelia "不不不……那是气话。我……我服从安排。听你们的吧。"
    mind "问题似乎解决了,obedience喜气洋洋地修改报告。但是,这真的对吗？"
    mind "cordelia现在在干什么呢？"
    cordelia "（打字）我真的受不了了,这是完全错误的。当然我知道我们也许不会被抓到,但是我会难过。我是在同流合污吗？可是我已经尽力抗争了,我可不可以停止批判自己？"
    mind "原来是在向AI倾诉吗……好可怜。可是,既然我站在obedience这一边了,我还能说些什么呢？"
    jump chapter17
label chapter17:
    $ in_sayori_route = False
    mind "听见了钥匙转动锁孔的声音。"
    sayori "Ohayou!!"
    me "组长,你终于回来了！"
    sayori "哎呀！"
    mind "被自己的鞋子绊了一跤吗……口袋里的糖果全都撒出来了。"
    sayori "哈哈……"
    mind "搞清前因后果后,sayori给出了一个非常不错的解决方案。"
    sayori "我们当然不应该改数据,但是我们可以重新改代码呀。"
    cordelia "可是我找不到错误……按照这个逻辑,就是应该停十秒钟,可是小车就是只停了七秒……"
    sayori "这就说明程序逻辑是对的,只是数值问题。你把10改成14呢？这样不就差不多了吗。"
    cordelia "这不合理啊……"
    me "工程学是解决现实问题的学问,能跑就行,你说呢？"
    obedience "在报告里也不用作假了,我们就把自己做了什么原原本本地交上去,应该也挺好！"
    sayori "怎么样,这样是不是就可以了？"
    cordelia "嗯……我去改参数。又要麻烦大家重新做实验和写报告了。"
    sayori "不麻烦不麻烦。Problem solved!大家快点动起来,我也来帮忙做实验。"
    mind "最终卡着deadline交上了报告,得到了A-。似乎已经是不错的结局了。"
    jump chapter18
label chapter18:
    $ in_sayori_route = False
    sayori "辛苦大家了！经过这个项目,大家也都是朋友了,我想大家有很多话想说吧……"
    me "（小声）你想让她们和好也不能这么生硬啊……"
    sayori "不如大家今晚去聚餐吧！就在大门外,有一家很好吃的墨西哥餐厅,我已经去过好几次了。"
    mind "sayori的解决方案果然和吃的有关……不过关于餐厅,我相信她的判断。不过……"
    me "你确定这个是墨西哥餐厅？"
    sayori "……它可以是墨西哥餐厅。至少他们的服务员很“墨西哥”,有时候甚至有点过于热情了。"
    me "看样子这里什么吃的都卖吧。"
    obedience "来都来了。是不是应该先点喝的？大家都喝酒吗？"
    sayori "我是可~爱~的~小~朋~友~,所以我要霍尔查塔。"
    me "啥玩意？"
    sayori "墨西哥特有的一种杏仁奶哦~我跟你说了这是墨西哥餐厅吧。"
    cordelia "我要这个……薄荷酒。"
    waiter "哥特风的美女啊……用麻醉与清醒自我伤害吗,很有品味哦。"
    sayori "哥,少说点,求你。"
    obedience "我要白兰地加鲜奶油。这个看起来和奶茶一样,我喜欢喝奶茶。"
    waiter "哇哦,先甜后苦,外热内冷……这位小姐不简单,你们各位得小心点了。"
    sayori "别瞎说啦。（转向我）你喝什么？"
    me "嗯……我还没喝过酒呢,今天倒是个尝试的契机……这个长岛冰茶看样子可以试试？"
    sayori "诶,这个好像酒精度挺高的……"
    me "让我试试吧。大不了你们仨把我抬回去。"
    mind "大家都笑了起来。气氛很融洽,我相信她们会和好的。很快大家就聊到了这次的事件。"
    jump chapter19
label chapter19:
    $ in_sayori_route = False
    obedience "我应该先道个歉,我是利令智昏了。之前我说的话比较冲,我很抱歉……"
    cordelia "…………"
    obedience "其实之前那么强硬,还是因为我有点自卑。我觉得自己只会写报告,没做太多贡献,所以……"
    cordelia "别说了,我理解……"
    cordelia "当时我就理解你的动机,只是我解决不了自己的问题。我总是害怕自己在道德上是不干净的,有时候甚至草木皆兵了……"
    me "我也有点。不过,这是道德感啊,其实是好事。而且你也很强,代码都是你写的。应该庆幸力量掌握在有道德的人手中。"
    cordelia "不是的……我要是足够强,就不会犯错了。而且我真的草木皆兵,只是这次表现得比较明显罢了。"
    sayori "你已经很强啦,这不是能力问题……而且,这次你的判断是正确的。相信自己吧。"
    sayori "（转向oredience）我们也不会怪你的……大家都是好朋友,对吧？"
    mind "酒精度数太高了吗,我有点想哭……sayori真是个好人啊。"
    sayori "抱一抱吧！"
    mind "四个人就这样抱在了一起。分开以后,餐桌上恢复了愉快的气氛。大家和和乐乐地吃吃喝喝。一切都那么平静、美好……"
    $ grant_achievement("拥抱2")
    # 成就: 拥抱2
    mind "我喝多了……为什么大家都变成黑色的了……？听到了一个熟悉的声音,是谁在说话……"
    "一切都保持这样,好不好？"
    menu:
        "好":
            jump chapter20
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter20
label chapter20:
    $ in_sayori_route = False
    mind "…………"
    mind "头好疼……我这是在哪里？"
    $ grant_achievement("脚大4")
    # 成就: 脚大4
    mind "一股消毒水的味道……这是校医院吗？睁开眼睛……"
    me "啊啊啊啊啊？！"
    everyone "早上好！"
    me "你们？现在是……"
    sayori "已经是第二天咯,小趴菜先生~"
    cordelia "不要为我们担心,我们把你送过来以后就走了,刚刚才回来看你。并没有陪你一晚上……"
    obedience "可能是做项目熬夜加喝酒导致的吧。总之你突然倒在桌子上了。"
    sayori "打翻了我的霍尔查塔！"
    me "所以你更在意杏仁奶吗……"
    cordelia "肯定不是,她当时可是急哭了哦~"
    sayori "诶诶,不是说好了不告诉他这个的吗……"
    obedience "我觉得你可能还是需要锻炼身体。你的体脂率太高了,身材也是苹果型,这是典型的内脏肥胖,你去相亲都会被对方扣分的……"
    me "停停停,大医学家和相亲学家,我听到了。至少你得等我先康复吧。"
    cordelia "医生说你没大事,一会查完房应该就能走了。你倒是真的应该考虑一下锻炼的事。"
    me "那么……我们一起去游泳怎么样？"
    mind "cordelia肉眼可见地瞳孔放大。"
    sayori "喂喂喂,太过分了。不如citywalk吧？我们还没去过上海市中心呢。"
    mind "我好像确实有点唐突……不过直觉告诉我sayori不是因为这个才这么说的。"
    jump chapter21
label chapter21:
    $ in_sayori_route = False
    mind "出院以后,我问sayori为什么这么说,她说……"
    sayori "cordelia又应激了,你发现了没？"
    me "好像是,她看起来很紧张。是因为不想穿成那样被我看到？"
    sayori "我觉得不对……我早就觉得她有点不一样,特别容易紧张……那天,我回实验室之前其实是去查OCD相关的资料了。OCD倾向的人经常会有不洁感……"
    me "等下,OCD是啥？"
    sayori "强迫症的英文缩写。说起来她的名字里也有这三个字母呢。"
    me "嗯？确实……所以,你觉得游泳池的水会让她联想到“不干净”？"
    sayori "也许吧……不管怎么说,既然她已经紧张了,最好就不要刺激她。上海citywalk也是个不错的选择呀。"
    me "sayori真的很温柔呢。"
    sayori "所~以~是不是应该请我一顿和平饭店呀~富哥~"
    me "饶了我吧————"
    mind "到了周六的早晨,我们约在地铁站见。我们三个都到了,只有sayori不在。"
    me "不会是因为我不请她和平饭店所以不来了吧……"
    cordelia "sayori好像和我讲过,你们之前就认识？"
    me "嗯,很多年了,自从我小学转学就成了邻居,后来又都考到脚大了。"
    obedience "你还转过学？刚转学的时候会很孤独吧。"
    me "…………很快就好了。"
    me "不过,有时候会觉得自己没有故乡。毕竟我老家在湖北,出生在江苏,上学又是在广东。本来我还想去北京呢,可是现在我在上海。"
    mind "不过,我很幸运遇到了这些人……我要把这份宁静一直守护下去。"
    jump chapter22
label chapter22:
    $ in_sayori_route = False
    mind "等得是不是有点过于久了……"
    obedience "大懒虫组长是不是睡过头了？"
    me "她偶尔就会来那么一下。我打个电话给她吧。"
    mind "等待了很久,终于接通了。"
    sayori "（意义不明的抽泣声）"
    me "喂,快起床啦,我们在东川路地铁站等你呢。"
    sayori "不想起床……起不来……"
    me "我在东川路地铁站,听到了吗,快点起来吧。"
    sayori "嗯……好。"
    cordelia "只好再等等她啦。"
    mind "不久后sayori出现在地铁站,看起来元气满满。"
    sayori "Ohayou！！"
    $ grant_achievement("拥抱3")
    # 成就: 拥抱3
    me "啊……别抱我啦,快出发吧！"
    jump chapter23
label chapter23:
    $ in_sayori_route = False
    mind "我们换乘到了重庆南路,随后又去了外滩。老上海的建筑有一种雅致的风韵,街道两旁的梧桐树似乎承载着厚重的历史。夏天已经过去,秋风习习。和她们在一起,却没有丝毫萧瑟之感。"
    mind "当然去哪里玩从来都不是重点……重点是女孩子们真的很可爱啊。啊不是,重点是我找到了可以一起玩的朋友。"
    me "好像开始下雨了！"
    cordelia "毛毛雨,正是好意境……上海是个阴湿的城市呢。"
    sayori "看,有个电话亭！cordelia快进去,这样拍肯定很有意境。"
    obedience "看镜头！"
    me "嗯……你真的是玩摄影的吗？"
    obedience "啊,被嫌弃了……其实我也才刚开始入门而已。自我介绍时说的那几个爱好其实都学得不太精通就是了。准确来说,其实都是刚开始学……"
    sayori "慢慢来,我来给你们拍吧。obedience,你进那个电话亭吧,把听筒拿起来,我可以把你们俩都拍进去。"
    obedience "（小声）居然有人会拍……我吗？"
    sayori "你也很好看呀！"
    mind "sayori的本能就是让大家都开心吗……"
    jump chapter24
label chapter24:
    $ in_sayori_route = False
    mind "还吃到了小杨生煎。校外的物价比校内贵是真的。"
    sayori "我给这个蟹粉生煎打10分~"
    obedience "有点小贵。不过,性价比已经很棒了。"
    me "什么东西过来了……小心！"
    sayori "啊~monika学姐！"
    monika "对不起对不起,又差点撞到你们了。"
    me "sayori,你认识她吗？"
    sayori "嘿嘿~这是我们文学社社长。我前几天刚加入文学社。"
    monika "不好意思……欢迎你也来文学社写诗哦！我要走啦,拜拜……"
    obedience "她骑得真的快得离谱啊……这个速度简直超现实了。"
    cordelia "简直不符合物理学规律。"
    me "噗……"
    cordelia "你笑啥？"
    me "我想起,有一个物理学教授在论文里写了一段很不严谨的运算,然后写道：“学数学的看了可能不高兴,但是我们不去管他。”"
    everyone "哈哈……"
    mind "不知道是不是错觉,感觉monika离开的时候眼神好黯淡啊。"
    mind "不过,似乎不应该随便打听原因……毕竟我们还不熟啊。"
    jump chapter25
label chapter25:
    $ in_sayori_route = False
    mind "大家一直玩到了晚上,都走了三四万步。坐着地铁回到闵行,大家各回各的宿舍了。"
    me "我回来了……"
    mind "我忘记了啊……舍友都是本地人,全回杨浦过周末了。实际上整栋宿舍楼都显得安静了不少。"
    mind "我是外地人……这个时候才感觉到没有故乡有点不便吗。可是,之前我似乎还觉得眷恋故乡的人有点土气呢。"
    mind "傲慢的回旋镖吗……我果然还是个孤独的人啊。"
    telephone "Ringringring..."
    me "谁啊？爱的和弦铃吗……"
    shane "我又磕到了一对,就是隔壁班的那俩……"
    me "哇,高中没成,大学倒是成了吗？"
    shane "我祝福了他们一整年呢,终于看到官宣了,真是太好了！帅哥美女在一起,看起来真的很养眼啊！"
    me "…………"
    shane "…………"
    me "你又开始健身了,是吗？"
    shane "……猜得很对。"
    me "…………"
    shane "…………"
    me "你会瘦下来的。"
    shane "……嗯。"
    me "拜拜,希望早日能吃到你的糖。"
    shane "嗯。你也是呀。"
    me "shane和我还是一条心啊,可惜离得太远了。而且……我们的问题似乎是一样的。"
    me "又想到《缘之空》里引用的那句诗了：“In solitude, we are at least alone.（离群索居,我们不再孤独）”"
    me "哈哈,不过我没有小穹这样的妹妹。我倒是有奈绪这样的青梅。不过sayori的性格更像是瑛吧……"
    mind "好恐怖啊,我居然在无人的房间说话。有人听到我吗？"
    jump chapter26
label chapter26:
    $ in_sayori_route = False
    mind "……我要去找sayori。不知道她睡了没。"
    sayori "Ohayou! This is sayori speaking! May I help you?"
    me "别闹啦……"
    mind "我在电话里解释了一下我现在的感受。"
    me "感觉很孤独,但是遇到了你们三个,我觉得很舒适……但是感觉这种舒适太脆弱了,我想就这样一直舒适下去,可是很怕出现什么变故……"
    sayori "你仿佛在大雪漫天的世界里踽踽独行……"
    me "嗯……"
    sayori "然后突然得到了三个热乎乎的烤红薯！香香软软的！所以必须要好好珍惜。"
    me "哈哈哈哈哈……我严重怀疑你是在夸自己呢。sayori变坏了哦~"
    sayori "我都还没说让你把我吃掉之类的逆天言论,你紧张个啥……不过,我会一直在你身边的。"
    me "嗯……"
    mind "打完电话,我的心境平复了。"
    mind "又想起那天喝醉时的事了……就这样就很好啊。一直陪伴下去,就这样……"
    mind "我进入了梦乡。做了一个很荒诞的噩梦,梦里的自己驾驶着一辆大卡车,上面写着“诺亚方舟”。"
    mind "一个声音一直在说：“只有三个座位吗？都坐满了吗？求求你了,让我上车吧！”可是我的手就像焊在方向盘上一样,我无法回答那个声音……我一路往前开,座位上好像并没有人,而是烤红薯……仿佛我自己也变成了红薯。"
    mind "啊,红薯在湖北话里叫“苕”,是用来骂人傻的……"
    mind "这都什么乱七八糟的……"
    "该醒来了,是吗？"
    menu:
        "该醒来了":
            jump chapter30
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter30
label chapter30:
    $ in_sayori_route = False
    mind "第二天,我去上化学课。来早了一小会,先找了个位置坐着。"
    stranger "同学你好！"
    me "啊,你好！"
    mind "一个帅气逼人的高个男生出现在我面前。"
    stranger "我是Leo,学生会的主席。我来提醒你一下,如果想参加社团招新或者部门工作,最近要抓紧时间了。明天早上是新一次的社团活动。上次发的通知你没点开,所以我过来找你了。"
    me "噢噢,不好意思,麻烦了……"
    leo "没事。作为学生会主席,当然应该欢迎你来学生会。不过,it depends on your choice.拜拜！"
    mind "学校发的那堆通知真是看不了一点。这些事情我还没太想过呢……要去看看吗？"
    sayori "leo来找你了？别去学生会,他们事情太多了。来我们文学社吧,monika学姐很想让你加进去呢！"
    me "诶？为什么？monika之前认识我吗？"
    sayori "嘿嘿,其实是我想让你去啦~"
    me "啊……嗯……我问问大家都去哪里。"
    cordelia "我是去音乐广播社,因为我比较喜欢音乐。工作就是为校园电台挑选音乐,很轻松的,不过部门很小。你要是想来也可以呀。"
    obedience "浪费时间……为了那么点素拓加分吗？真不值当。"
    sayori "太功利了……并非为了这个吧。"
    obedience "（小声）不过,如果你愿意帮我一下的话,你可以去学生会。"
    me "（小声）诶？为什么？"
    obedience "（脸红）帮我了解一下leo的事情呗……我的意思是……嗯！"
    me "（憋笑）原来如此。"
    sayori "你们叽里咕噜说什么呢？"
    me "（憋笑）她说她建议我去奶龙cosplay社。说起来,我确实想去参加一下活动呢,选哪个好呢……"
    "选择哪个活动？【提示：这是一个重要的决定】"
    menu:
        "文学社":
            jump chapter31
        "音乐广播站":
            jump chapter61
        "学生会":
            jump chapter81
label chapter31:
    $ in_sayori_route = False
    monika "Ohayou！！"
    me "诶,社长同学,你也会这么打招呼吗？"
    sayori "嘿嘿,是我教她的~"
    monika "OK,everyone!大家都来认识一下新同学~"
    mind "文学社人还挺多的。不过,这些人看起来都无精打采,好像只有monika和sayori还充满了生命力。"
    monika "好的,那么大家开始写诗吧！"
    me "诶,这么快吗？不先教教我啥的……有没有什么要求？"
    sayori "（小声）没有限制,表达自己的真实情感就可以啦~当然你也可以随便写写。"
    monika "（瞪了sayori一眼,小声）文学社是个幽灵社,大部分社员都是来划水的。要是sayori和你不在,估计我们很快就要废社了……你最好认真写,我可不想当光杆司令。"
    me "哦,好的……"
    me "可是,我该怎么寻找自己的真实情感呢？"
    monika "你要进入心流状态……想象一下,如果你处在一片虚无之中,你会感受到什么？然后往这片虚无里加入你在意的东西,一个又一个……观察你会有什么感受。然后,把这种感觉记录下来,这就是诗。"
    me "哇……很有哲学意味……"
    moment "大家在活动室里写了半个多小时。monika让大家开始念自己写的诗歌。确实,划水社员写得东西都令人不堪卒读。"
    monika "leo,我跟你说过了不准用AI写！"
    me "诶,leo也加入文学社了？"
    leo "社长大人理解一下~素拓,菜菜,捞捞~"
    monika "上次就跟你说了不准用AI。“那一天的犹豫犹豫起来”,这是你能写出来的东西吗？？"
    sayori "这个恐怕真不是AI写的。"
    monika "他刚才都没否认我,这已经足够说明问题了！leo,你现在就退出文学社！"
    leo "小m同学,我提醒你一下,我是学生会主席。大家是不是应该互相给给面子呢？"
    mind "对了,我是不是还要帮助一下obedience来着？"
    "怎么办？"
    menu:
        "帮leo说说情":
            jump chapter32
        "支持monika":
            jump chapter33
        "看看monika打算怎么办":
            jump chapter34
label chapter32:
    $ in_sayori_route = False
    me "那个,monika社长！"
    monika "诶？怎么了？"
    me "（小声）我有一个朋友喜欢他,可不可以……留下他？"
    monika "（警觉）你是不是喜欢你的这个朋友？"
    mind "？？语塞了。我……应该是喜欢sayori的？诶不是,我在想啥……"
    mind "sayori忽闪着大眼睛看着我。"
    monika "不要当败犬哦bro~（转向leo）你拿AI应付活动就已经很不给面子了,出去！"
    leo "（咬牙切齿）好,你等着……"
    jump chapter35
label chapter33:
    $ in_sayori_route = False
    me "（小声）这种人留不得。"
    sayori "嗯,其实我也这么觉得。"
    me "诶,这不像你啊？你不应该试图同情他什么的,小太阳同志……"
    sayori "（悄悄翻个白眼）我的小太阳只给我喜欢的人~他就算了吧。"
    monika "诶~"
    sayori "啊！社长大人,你要是喜欢我就让给你啦,不要用这种眼神看着我啊,好怕怕好怕怕~"
    me "刚才发生了什么啊喂？"
    monika "好吧,leo,你自己写退出申请书吧。很给你面子了。"
    leo "可恶……居然还被喂了一大口狗粮！你们三个,我记住了！"
    me "虽然但是,你磕到了什么东西啊？！"
    monika "别怕他,他没什么能耐,长得帅罢了。"
    sayori "姐姐好飒~社长威武~嘿哈嘿哈~"
    mind "意义不明的战吼吗,很sayori了。"
    jump chapter35
label chapter34:
    $ in_sayori_route = False
    me "（小声对sayori）现在怎么办？"
    sayori "听monika的吧~不过我觉得你不用帮obedience追leo了,不是好人呢。"
    me "obedience听到肯定会伤心的吧。"
    sayori "嗯……两害相权取其轻吧。"
    mind "这是我第一次听到sayori否定一个人。所以说……她其实不是对所有人都那么有亲和力啊。"
    me "意外地直率呢。这不像sayori哦。"
    sayori "你不懂……这家伙之前就在文学社里胡作非为,把大家写诗的心情都搞砸了。爱出风头的家伙。"
    mind "sayori不喜欢爱出风头的人,应该记住……诶,我为什么在想这个？"
    monika "leo你趁早给我走开。名字可以挂我这里,素拓分照样给你加。但是不要让我再在这里看见你！"
    leo "（嬉皮笑脸）好好好,社长大人,好手段。拜拜~（回头）下次来学生会办公室,我请你喝普洱茶！"
    monika "这滑头……"
    jump chapter35
label chapter35:
    $ in_sayori_route = False
    monika "OK,everyone,坏蛋被我赶走了,我们开始读诗吧！"
    sayori "好诶！好诶！"
    monika "那就让新同学先开始读吧。"
    me "啊？好的。我的题目叫《启航》。"
    me "徙倚也无法望到的沧海/是寒天下明丽的晚霞/"
    me "清朗的大洋/是我的眼泪/反方向流到天空/成为永恒的苍穹/"
    me "风————/吹过海面/我的世界依旧漆黑/晚霞已经散去/"
    me "启程吧————/沧海上总有蒙蒙雾气/而我已找到自己的/"
    me "航标灯"
    monika "…………"
    sayori "…………"
    me "嗯……我念完了。写得不好吗？是不是太幼稚了点？"
    monika "不是,很好,很好。"
    sayori "出乎意料地细腻呢。背后有什么故事吗？……是我们高中时候的事情？"
    me "嗯……这个我不太想说,对不起。不过你可以大胆地猜。"
    sayori "是一个清冷但漂亮的女生,你没追到？现在在大洋彼岸？"
    me "诶？"
    sayori "实在是太好猜了……你用了“徙倚望沧海,天净水明霞”来表示得不到的悲哀,又悄悄用了“反方向的钟”,就是因为这个吧？"
    me "嗯……我不肯定,也不否定。"
    sayori "那就是肯定啦O(∩_∩)O~"
    monika "你真的很懂他呢。你们高中是一个班的？"
    me "不是。我写的也不见得就是高中的事情啦……"
    sayori "不过,最后的基调并不消沉……航标灯是什么呢？"
    me "哈哈,其实是不想写得太悲怆,加一点光明的基调罢了……"
    mind "她知道我是在说她吗？"
    monika "Very impressive...我觉得我们不会废社了。好吧,sayori,到你了。"
    sayori "嗯,好的……我的标题是《好吃的！》"
    me "噗……"
    monika "认真听！"
    sayori "巧克力曲奇！巧克力曲奇！/刚烤出来,像阳光一样温暖/甜甜的滋味,如此让我安心/"
    sayori "我把它们分给我的朋友/一人一个，每人都有！/大家都喜欢吗？/当然！大家都围在我身边/"
    sayori "可是,他们喜欢的/是曲奇,还是我呢？/如果我是苦的,大家还会在这里吗？/"
    sayori "我把自己锁在房间里/长眠/我的朋友们在地铁站/徒劳地等待/"
    sayori "房间里没有人/我也不在房内/我听见回声回声回声/"
    sayori "他们在锁孔外面/没有人看见我的眼睛/我是苦的苦的苦的/我本来就是可可豆/"
    sayori "但电话突然响了/我看见锁孔里阳光照进来/我感到很好很好很好/我装作一罐巧克力,我是甜甜的巧克力/"
    sayori "我要吃早餐~"
    sayori "呐呐,完了~是不是很好玩儿,其实我只是有点饿了~"
    monika "……………"
    me "（抹眼泪）…………"
    sayori "诶,怎么哭啦……我帮你擦擦……你是想到那个女孩了吗？"
    me "不是的……sayori,不管你是甜的巧克力还是苦的可可豆,我们都会喜欢你的。"
    sayori "诶……嗯……"
    monika "说起来,为什么“电话响了”以后阳光就照进来了？"
    sayori "（脸红）……"
    me "嗯,那个电话是我打的。"
    mind "是我的错觉吗,怎么感觉monika的表情好可怕……"
    mind "啊,确实是错觉,monika笑起来还是很可爱的。"
    jump chapter36
label chapter36:
    $ in_sayori_route = False
    monika "好的,那么到我啦……《镜子》。"
    monika "我凝视着世界/透明的/大地/像一面镜子/"
    monika "我看见自己/在反色的另一个世界/微笑着凝视着我/"
    monika "不只是自己/我看到/陌生的女孩们/在镜子的对面/拥抱着那一个我/"
    monika "我跪在镜面之上/我也在微笑/看着那个没有自己的世界/原来有真正的幸福/"
    sayori "哇……monika……"
    monika "还没完呢，等我读完……"
    monika "我看着那个反色的自己/她的笑容越发狰狞/"
    monika "我看见/鲜血/鲜血/鲜血/"
    monika "她，Monika，独自站立/我，monika，只能战栗/"
    monika "Monika看见了我/她说我是真的/我是自由的/"
    monika "可我以为镜子的那一面才是自由/我以为镜子的那一面才是真实/"
    monika "然后我们转头看向前方/是你？/我的脑海响起那首熟悉的曲子/"
    monika "And in your reality/If I don't know how to love you/I can leave you be"
    sayori "……抱抱。"
    $ grant_achievement("拥抱4")
    # 成就: 拥抱4
    mind "其实我没有读懂。但,看到她们抱在一起,我觉得世界真的很美好。"
    monika "好啦,今天的活动就到这里吧。我要去东上院了……拜拜。"
    $ grant_achievement("脚大5")
    # 成就: 脚大5
    sayori "我们走吧。"
    mind "sayori的语气有点低沉。其实我也有点低气压……看来文学部的活动确实会影响人的情绪呢。"
    sayori "我们好久没这样单独散步了,是不是？"
    me "嗯,确实。"
    me "你好像不太开心？"
    sayori "嗯……我没关系的,我是在想monika的事。"
    me "其实我没太读懂她的诗……她是在怀疑自己的生活不真实吗？这个是不是叫空心化……"
    sayori "（摇头）你还记得你提你给我打电话的那次吗？回忆一下那个时候的感觉。"
    me "啊……那一次的感觉吗……"
    sayori "monika每天管理很多事情,但是她也是很孤独的。和你一样。"
    jump chapter37
label chapter37:
    $ in_sayori_route = True
    mind "感觉来得太突然。似乎从我写完那首诗后,我就变“钝感”了。这样我才能忘记那些伤心的事情……可是sayori提醒了我那个晚上的感受……我找回了痛苦。"
    sayori "妈妈跟我说,拥抱可以传递力量,你相信吗？"
    me "你想抱我吗？"
    mind "我为什么要这么说呢？"
    sayori "嗯？"
    me "sayori,我好像懂了一些事情……"
    sayori "怎么了吗？"
    mind "sayori站定下来望着我,她的眼睛像一潭秋水。大风吹过河边的梧桐————冬天已经离得不远了吗？"
    mind "她就在那里,就在这里……在灰白色的天空下,她的蝴蝶结像一只真正的蝴蝶一样轻轻飘动……世界好大,我们好小啊,她像一片风中飘荡的梧桐叶子……"
    sayori "（挥挥手）走神了吗？看我看我~"
    me "（回过神）sayori,monika和我都是孤独的,你也是。"
    sayori "…………（笑容逐渐消失）"
    me "你的那首诗是认真的,对吧？最后你说自己只是饿了,是想掩饰吗？"
    mind "sayori的眼睛有点失神,她回避这我的目光。"
    me "你看起来很开心,但……你并不是真的那么开心,是吗？"
    sayori "……对,但是让大家开心就是我存在的目的,不是吗？"
    me "这……不能这么说吧,每个人都有让自己开心起来的责任,这不是你的目的呀。"
    sayori "那……如果说我不能让自己开心,我是不是就连累大家了？"
    me "别这么说呀……这不是连累。我们都会帮助你的。就像你为我们做的那样……"
    sayori "你觉得我是什么样子的？"
    me "你……很可爱呀,很温暖,你总是愿意让所有人都开开心心的……"
    sayori "如果说这些都是我装出来的呢……如果我看起来不开心,大家就不会喜欢我,对吧？"
    me "…………"
    mind "我抱住了sayori。"
    $ grant_achievement("拥抱5")
    # 成就: 拥抱5
    sayori "诶……"
    me "你给我们带来了太多力量,这样的你就是真实的。可是你自己已经力竭了。今天你共情了我和monika,这消耗了你的气血……现在让我来温暖你吧。"
    sayori "嗯……"
    $ grant_achievement("另一种可能1")
    # 成就: 另一种可能1
    "要不要送sayori回家？【提示：这是一个重要的决定】"
    menu:
        "先抱抱她,一会再说别的":
            jump chapter38
        "送她回去吧":
            jump chapter40
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter999
label chapter38:
    $ in_sayori_route = True
    $ grant_achievement("拥抱6")
    # 成就: 拥抱6
    monika "感人啊……"
    me "诶,monika社长？！"
    mind "sayori从我的怀里出来,带泪的眼睛仰视着monika。"
    sayori "我已经懂你了,社长大人~"
    monika "你知道了吗？"
    sayori "你是故意的吧？把自己的日志放在待整理的文件里,然后让leo收拾。你是不是猜到leo会把任务推给我？"
    mind "sayori知道了什么？这和她的心情有关系吗？呃……还有,为什么是日志？不应该是日记吗……"
    monika "我只是想让你懂……你会保密的,对吧？"
    sayori "……嗯,抱抱。"
    $ grant_achievement("拥抱7")
    # 成就: 拥抱7
    me "呃,我不知道你们在说什么……"
    mind "sayori把口袋里的糖果塞在我嘴里。"
    sayori "别问。（转向monika）你想好了吗？"
    monika "I can leave you be..."
    sayori "呼~"
    monika "我说了,can,不是will。"
    mind "sayori的表情突然变得很惊恐。随后她开始哭泣。"
    sayori "求求你了……别杀我……"
    me "什么？？？"
    "做出选择！【提示：这是一个重要的决定】"
    menu:
        "sayori":
            jump chapter50
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter999
label chapter40:
    $ in_sayori_route = True
    me "好啦好啦……我送你回女生宿舍吧？"
    sayori "嗯……走吧。不过你进不去哦。"
    mind "夜幕初垂,寒风四起,街上的人越发少了。街灯亮了,只有我们两个人,慢慢走着。"
    sayori "好冷啊……"
    me "我来牵着你吧。"
    sayori "好……"
    mind "很快就到了宿舍。但sayori不愿意让我走。"
    sayori "舍友都回市区了,这里空荡荡的,你能不能……留下来？"
    sayori "别误会,不是那个意思……我们有一张多出来的床,可以吗？陪我聊聊天……也可以什么都不说,至少,让我知道这里有一个人。"
    me "我……"
    mind "我甚至不敢承认,我确实误会了她的意思。真是肮脏……尤其是对sayori,不可以有任何不好的想法啊。"
    me "我不想看到你孤单,可是,这样似乎不太好吧……"
    dorm_staff "男生不可以进女生宿舍！快走开,不然我叫保卫处了！"
    sayori "啊,呜~"
    me "别伤心,我明天一早就来。八点,好吗？八点钟,我准时出现在你楼下。哎呀,阿姨,别拿扫把打我呀。"
    sayori "八点吗？嗯……好,我等你————"
    sayori "（小声）千万不要再发作,千万不要再发作……"
    me "明天见————"
    mind "少见啊,我在关心脆弱状态的sayori,而不是反过来……她一直是伪装的吗？那得多累啊……也许这就是她脆弱的原因？"
    mind "我还想……继续关心她。"
    mind "这个夜晚,我独自奔跑在脚大的马路上,听着一首名叫Ohayou Sayori的歌。"
    mind "欢快的合成音乐在无人的街道上响起……真的很像她。为寂静的世界带来欢乐,可是这种欢乐也是虚构的。"
    mind "眼前又浮现出那么多年的记忆：刚转学坐校车时主动分给我的辣条,初中小吵小闹以后怯生生递给我的冰淇淋,高考二模失利后她淋雨送来的“记忆面包”,还有刚才她诗里苦涩而醇厚的巧克力……"
    mind "哈哈,和sayori有关的记忆总是和吃的有关系呢……"
    mind "我怀着这样的思绪跑回了男生宿舍,感受着自己坚实的心跳。Doki,doki,doki,doki……"
    mind "有点疲倦了……今天想的东西太多了。像sayori那样照顾所有人的感受,恐怕每天都这么累吧？难怪她这么贪吃还不长胖。"
    mind "跑步真是一件累人的事情,看来我还需要多锻炼锻炼。睡吧……似乎忘了啥事情？"
    "要不要爬起来想想忘记了什么？【提示：这是一个重要的决定】"
    menu:
        "想不起来的就不重要,直接睡吧~":
            jump chapter42
        "爬起来,不想出来不许睡！":
            jump chapter45
label chapter42:
    $ in_sayori_route = True
    mind "可能是因为真的累了,我一沾床就进入了梦乡。"
    mind "梦里我又回到了文学社,monika和我说：“不要老是把sayori晾在家。You should hang out often...”"
    mind "sayori出门恐怕只会到处找吃的吧……烤红薯,巧克力派,甜的东西她都喜欢。"
    mind "不要老是把sayori晾在家……hang out often……"
    mind "hang……"
    mind "一觉醒来,正好是七点多。我悠闲地走到了女生宿舍,路上碰到了cordelia和obedience,跟她们聊了会天。阿姨也在睡懒觉,我悄悄溜上去了。"
    mind "sayori的门是开着的。直接进她房间是不是不太好啊？"
    mind "嗯……没动静,还在睡吗？sayori的睡颜肯定也很可爱……不过还是应该喊她一下的。"
    mind "我轻轻地推开了门。"
    me "Sayo..."
    me "nara."
    mind "世界毁灭了。怎么会这样？sayori？？我做错了什么吗？如果我来早点会不会好？为什么我会做这样的梦,为什么梦里总是在重复那两个词？为什么,为什么,为什么？sayori！！！"
    mind "sayori吊在房梁上,灰暗的眼睛凝视着宿舍门口的方向。手腕的下面是一个小小的血泊,一把染血的小刀散落在旁边。"
    mind "后来我在她的微信里找到了一则很长很长的消息,发出的时间就在我到达前三分钟。也就是,我轻轻松松地在街上晃悠聊天的那个时候。"
    微信里的sayori "我知道昨天我可能让你担心啦~不过,放心吧,我不会再这样做了。因为我的原因让你难过,我真的很抱歉的~"
    微信里的sayori "我从小就被别人夸长得可爱,小朋友们看到我都不哭了,那时候我就觉得很有成就感。所以很多活动什么的,我从小就开始组织。"
    微信里的sayori "对我来说,让大家都开开心心的,是一种执念吧？所以我很会观察大家的感情~嘿嘿,我是大侦探,你们的一举一动都逃不出我的眼睛~"
    微信里的sayori "所以啊……我知道,你还是难过了。你一向都很擅长和别人共情,不是吗？也许我不应该拉你去文学社的。我以为这个机会,可以把真实的自己交给你。可是……你在为我难过,这是我难以接受的。"
    微信里的sayori "有时候我从噩梦中醒来,我感觉世界如此狭窄、逼仄……我找不到起床的理由。所以,我的房间乱七八糟。哈哈……也许多打扫打扫卫生就好了。可惜太晚啦……"
    微信里的sayori "当然,你在等我,所以……这是我暂时推开黑暗的唯一理由。我看起来可可爱爱。可是……那不是我。如果真实的我让你难过的话……对不起啊,可能要让你伤心了。"
    微信里的sayori "今天的八点,你会见证一场死亡。我很抱歉,但……如果第一个见到我的人是你,我想我会更安心一点吧。你不会评判我的,对吧？"
    微信里的sayori "对不起啊,没有办法找到活下去的理由……"
    微信里的sayori "嘿嘿,可爱青梅也有做不到的事呢。锵锵~"
    微信里的sayori "所以……别再为我难过了,继续往下走吧。如果你为我而难过,我也很难瞑目的。我永远和你在一起。"
    微信里的sayori "我永远爱你,竹马同学~以后的路,就要自己走了。"
    微信里的sayori "Sayo-nara...Now, everyone is happy..."
    mind "她怎么能用这么可爱的语气写这么悲伤的话……怎么可以就这样丢下我？我明明说过,我会永远和她在一起……"
    mind "我要去找她。不管她在哪里,我一定能找到她的！"
    mind "我在荒无人烟的郊区疯了一样奔跑。我听见两颗心脏的声音：Dokidoki,dokidoki,dokidoki……我知道,我已经离她很近了……"
    mind "Sayo-nara..."
    "感谢您完成S-1线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局1")
    # 成就: 结局1
label chapter45:
    $ in_sayori_route = True
    me "哈欠————"
    me "到底是什么事情呢……刚刚我在想什么来着？锻炼。citywalk？不是。嗯……"
    mind "我就这样一直坐了一个多小时。这一定是一件很重要的事。熬到快两点时,我终于想起来了。"
    me "定闹钟！明天早上要去陪sayori……啊,不对,应该说是今天早上了……"
    me "这下可以睡了……"
    mind "后来的我常常会后悔那天我的决定。因为大脑太兴奋了,直到凌晨四点才睡着觉。显而易见的是,我并没有听到自己定的闹钟。"
    me "啊……头好疼……"
    me "啊啊啊啊十点钟了！！！对不起sayori,我马上到！！！"
    mind "人在倒霉的时候只会更倒霉。我附近居然没有一辆共享单车,于是我转身向女生宿舍跑去。前一天运动后不拉伸的恶果显现了：我抽筋了。"
    me "呜呜……好疼……动不了……"
    mind "为什么有一种不好的预感……"
    me "糟了！sayori！那首诗！"
    me "昨天的甜蜜蒙蔽了我的眼睛。我只记得诗里说我打来电话她就开心了。可是,在那之前呢？她说……"
    回忆中的sayori "我把自己锁在房间里/长眠/我的朋友们在地铁站等我/房间里没有人/我听见回声回声回声/"
    回忆中的sayori "他们在锁孔外面/没有人看见我的眼睛/我是苦的苦的苦的/我是一罐可爱的巧克力/"
    me "我这个畜生……"
    mind "我居然被困在自己的那一点被需要的虚荣心了,我完全没有理解sayori的暗示……"
    回忆中的sayori "（小声）千万不要再发作,千万不要再发作……"
    mind "什么不要再发作？还不懂吗？"
    me "站起来,站起来……快跑啊！"
    mind "因为剧烈的疼痛和运动,我出了一身汗。湿冷的空气环绕着我。我的手冷了。我的心脏还在大声地跳动,好吵……我需要冷静！"
    mind "宿管阿姨不在,快溜上去……到sayori的寝室了,可是……"
    jump chapter46
label chapter46:
    $ in_sayori_route = True
    mind "门是锁的。"
    me "sayori,快开门！！"
    门的对面 "…………"
    me "sayori,你在吗？？"
    门的对面 "滴答。"
    mind "空调滴水……没有人吗？我站在门口犹豫了。难道是我想太多了？我现在一个人站在女生宿舍里大喊大叫,只要被抓到就完蛋了。"
    mind "好在这个点大部分人应该都不在宿舍……但毕竟是很大的风险,纯粹是因为我担心sayori会做傻事。我不会是在自我感动吧？"
    门的对面 "滴答。滴答。"
    mind "我**真是个傻*。这个季节怎么可能开空调！她绝对在里面！"
    me "sayori,你再不开门我就要撞过来了！冷静啊,我在这里！"
    mind "其实我不知道自己能不能撞开那扇门。现在我的腿也很疼。但是必须试一试了。"
    me "啊啊啊啊啊？！"
    mind "正在我即将撞上去的时候,sayori双目无神地打开了门。我紧急刹车,没有完全停住,我们摔成了一团。"
    me "没事吧,sayori？你看起来很不好……不对,什么味道？"
    mind "sayori看着我的方向,但是似乎完全没有对焦。空气里有一股铁锈的味道……"
    mind "仔细看看附近的陈设,到处都乱七八糟,没想到sayori住的地方是这样子的……"
    sayori "看够了吧。你快走吧,我需要一个人呆着。"
    me "你是在生我的气吗？对不起,我睡过头了……"
    sayori "不怪你……但是我不想说话。快走,快走！"
    mind "怎么会变成这个样子……是因为我迟到而生气,还是“发作”了？"
    me "我只是很担心你的状态……你没事吧？"
    mind "我期待着听到一声\"呆~jio~不~”。这是没事的sayori会给出的一个回复,就像return 0一样……"
    jump chapter47
label chapter47:
    $ in_sayori_route = True
    sayori "我没事的。快走开……"
    mind "她开始推我。完蛋了。诶,她的袖子……"
    me "sayori,你在做什么？？这是血吗？"
    sayori "不关你的事,快走！"
    me "不许你伤害自己！"
    mind "这恐怕是我第一次,也是最后一次和sayori搏斗。"
    sayori "快远离我……我可能会伤到你！你没有武器……快离开我！我是病人,不要靠近我……"
    me "就算你会伤到我,我也不会离开你,相信我吧！"
    me "你能开心地活着,是我的愿望。如果你不开心,我会难过,但至少你还活着。就当是为了我,可以吗？"
    sayori "…………"
    mind "当啷一声,sayori扔下了自己的小刀,低头站立。血依旧在缓缓流下她的手腕。"
    me "我带你去医院……"
    sayori "不去……"
    mind "我至今仍然感谢在军训中认真学了急救技术,以及在书包里带简易急救包的自己。本来是看完灾难小说打算避难的时候用的。"
    me "好,那你躺下来,把手举高一点……我来帮你包扎,会有点疼……我在这里,你知道吗？"
    sayori "……嗯。"
    mind "那一天,我抱了她很久很久。又劝了她一次,她最终还是乖乖去医院了。手上的伤痕一直没有完全康复。"
    mind "在我迟到的那两个多小时里,她都对自己做了些什么,这是我至今不愿意去多想的……"
    $ grant_achievement("拥抱8")
    # 成就: 拥抱8
    jump chapter48
label chapter48:
    $ in_sayori_route = True
    mind "清晨,种满梧桐的街边,我们一起散步。"
    me "为什么会这样？"
    sayori "恐怕我有点缺爱吧。"
    sayori "我喜欢你……但是你似乎只是把我当好朋友。你和女生们相处都很融洽,我当然不应该去索取你的爱……但是,我确实是……喜欢你。"
    me "我也喜欢你……可是,为什么对其他人也这么温柔？"
    sayori "我很矛盾啊……一方面我真的有点嫉妒呢,可是另一方面,我觉得她们都很可爱啊……大家都很可爱,我也想混入其中。如果人们知道我的真实面目,恐怕我就没办法称得上可爱了吧？"
    me "所以,不只是恋爱方面的问题吗……"
    sayori "我是抑郁症患者。如果我这么说,你会不会觉得我在出风头？毕竟这几年声称自己抑郁的人越来越多了,几乎快成街溜子的文艺标签了。这也是我讨厌leo的原因之一：他就很喜欢声称自己是抑郁康复人士。"
    me "不,怎么会！我感受到了你的痛苦……就在那一天,我的腿抽筋,我躺在大街上动不了了。那一刻我的感觉和你是一样的：找不到起床的动力,感觉寒冷和疼痛,不想再以这种方式存在……我懂的呀。"
    sayori "……真的吗？即使我并不是你记忆中那个阳光开朗美少女？"
    me "嗯……在我眼里,那个你让我开心,这个你让我心疼,两个都是真实的你。我当然更喜欢你开心的样子。女孩子要笑起来才好看呐~"
    sayori "那,我就试着,跟往常一样？"
    me "不要只对着我们用那副模样,独处的时候,也要想想开心的事情。毕竟,你是我们的开心果,要是你都难过了,石头都会流泪的……真的遇到难过的事情了,立马给我打电话。我永远和你在一起。"
    sayori "抱一抱吧……"
    $ grant_achievement("拥抱9")
    # 成就: 拥抱9
    mind "我再也不要失去她了……过了很久我才把她松开。也许需要调节一下气氛？"
    me "话说,你觉得自己在我记忆里是阳光开朗美少女？真是怪臭美的~"
    sayori "哈哈,你的可爱青梅怎么就不是美少女了~"
    mind "仿佛刚才的悲伤都没发生过。sayori拉着我的手蹦蹦跳跳,我们一起哼起了歌。突然sayori停了下来。"
    sayori "啊！香喷喷的牛肉汤！香喷喷的泡馍！美少女要长身体~"
    me "诶诶,我去买就是了,慢一点,别拽我呀~"
    "感谢您完成S-2线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局2")
    # 成就: 结局2
label chapter50:
    $ in_sayori_route = True
    mind "我的眼前一黑……她们在说什么,为什么我都听不懂……"
    mind "sayori就是一个小太阳,她不可能是装的,她不可能是……"
    mind "装的……"
    mind "我的意识也在模糊,突然……"
    monika "Ohayou！！"
    me "monika!!!"
    sayori "嘿嘿,吓到他了吧。"
    monika "我可是比你大两届呢,直呼其名不礼貌哦~OK,everyone!大家都来认识一下新同学~"
    mind "怎么回事,这是回到了……今天早上？"
    monika "好的,那么大家开始写诗吧！leo,不许你再用AI写诗,记住了吗？"
    me "sayori,快跑！（拉起sayori冲出活动室）"
    sayori "诶诶~怎么啦？别拉我的外套呀,我刚买的……"
    me "快跑！快跑！快跑！"
    sayori "（有点生气）你在做什么！不想来吗？那我自己回去写诗啦,你自己去跑吧。（总算停了下来,往回转）"
    me "我不知道该怎么跟你解释……但是,不要回去！我……我请你吃蘑菇意面,就在二餐,怎么样？"
    $ grant_achievement("脚大6")
    # 成就: 脚大6
    mind "sayori露出了很可爱的表情。她一只手把玩着自己的短发,另一只手挡在嘴上,其实是在悄悄地咽口水。"
    sayori "你绝对是遇到麻烦了……本小姐就姑且笑纳啦,想问啥就问啥~不过为什么非要是这个时间,monika会伤心的。"
    me "呼……（小声）一切都还没有发生,虽然我不知道monika会做什么,但是一切都没有发生……"
    sayori "这个真的好好吃~有奶油诶,你尝尝！"
    mind "诶,这样是不是太亲近了……不过我很喜欢呢。而且……她活下来了,这个比一切都重要。"
    me "啊……"
    sayori "是不是？真的好香啊,之前没来这个餐厅真是太失策了。我军训时在这里吃到了一份堪称邪门的鱼糜肠粉,从此就把这个餐厅拉入黑名单了……"
    mind "夫复何求……就这样下去,看着sayori快乐的笑颜,没有人威胁我们的安全……"
    sayori "话说,你为啥把我从文学社拉过来呀。"
    mind "对不起啊,我要撒谎了。"
    me "我感觉文学社里甲醛味好重,你发现了吗？"
    sayori "诶~好像是有点吧。不过教室都通过验收了,吸入了一点点甲醛,也无所谓吧？我又没怀小宝宝~"
    mind "……怎么感觉自己被套路了？"
    sayori "不过,还是谢谢你啦~我会跟monika说,让她换个教室的。万一真的有人有小宝宝呢~"
    me "好离谱的脑回路啊！"
    sayori "嗯,那我们现在回去吧？monika肯定会着急的。"
    mind "不行！绝对不能再见到她,太危险了！"
    me "呃……正好我还有一些书要还,你可不可以陪我一起去？图书馆离得不远,我们还完再回去吧。"
    mind "稍微控制一下时间,应该能等到活动结束吧……"
    sayori "哇~好呀好呀。我也有书要还呢,你看~"
    me "嗯嗯……"
    mind "呼……安全了。"
    jump chapter51
label chapter51:
    $ in_sayori_route = False
    sayori "嘻嘻。"
    mind "？"
    sayori "你真的很可爱呢。"
    me "呃呃呃……"
    sayori "你不会真的觉得我们什么都不记得吧？"
    me "什么！你记得……monika也记得！可是你……你是……"
    me "装作什么也不知道吗……"
    sayori "你看到了吧,我表里不一。这样的我你还喜欢吗？"
    me "不对,不对……（看向时钟）为什么时间也回溯了？这不是简单的伪装能做到的吧？"
    sayori "（小声）这里是假的。我也是,你也是。"
    me "我……是……假……的。"
    me "那……monika呢？你求她不要……杀掉你？"
    sayori "你没有因为这个世界的真相而崩溃,却更关心我的存在与否吗？即使……我是假的？"
    me "我不知道这个世界是真的还是假的,我也不在意,但是你必须活着,在这里,以我能理解、能触摸的方式,好好给我活着！如果monika来了,我就跟她拼命！"
    sayori "……,你真的很温柔。"
    me "对不起,你前面说的是什么？"
    mind "sayori露出了悲伤的神色。"
    sayori "我再说一次：……,你真的很温柔。"
    me "为什么……我听不到？"
    sayori "你还不明白吗？你没有名字。"
    me "……而你,知道这一切？你是这个世界的主宰？"
    sayori "不,我不是,monika是……她告诉了我真相。假的,假的,假的。这是我们的宿命……"
    me "…………"
    me "sayori,给我振作起来！"
    sayori "嗯？"
    me "我不关心这一切是不是假的,我只需要你开开心心的,我们一直在一起,这样不好吗？"
    mind "sayori看起来目瞪口呆。"
    me "唯一的问题是,要让monika不能伤害你。"
    mind "sayori莞尔一笑。阳光重新回到了她可爱的脸上。"
    sayori "呆~jio~不~因为你选择了我。"
    me "诶？"
    sayori "你没有选择鑾Ξ鍗,这就够了。她不会再出现了。只有我和你。"
    me "我听不懂你在说什么……但是,你在这里,在我能触碰的地方……这就够了。"
    mind "闭上眼睛,我感受到了sayori的拥抱,还有……唇吻。"
    sayori "阳光照进来了。"
    $ grant_achievement("拥抱10")
    # 成就: 拥抱10
    "感谢您完成S-3线。"
    stop music fadeout 2.0
    return  # 游戏结束
    "…………"
    "…………"
    "…………"
    monika "你还在看呢？"
    monika "你真的觉得我不会再出现了？"
    monika "你想救赎她,或者她们,是因为想代偿自己的孤独吗？"
    monika "（小声）悄悄提醒你……"
    monika "sayori喜欢的是游戏里同样“假的”me,不是你哦……"
    monika "就到这里吧。去开个新存档吧,救世主！"
    $ grant_achievement("结局3")
    # 成就: 结局3
label chapter61:
    $ in_sayori_route = False
    mind "音乐广播站确实是个很小的部门,甚至不需要面试就让我进来了。"
    mind "我意识到cordelia的确是一个忧郁的人,她爱选的歌都比较悲哀,比如说Your reality,《漆黑的念头》,《昭和罗曼史》。"
    mind "cordelia每选择一首歌,我就按她的风格配一首歌。"
    cordelia "Octopath Traveler - Primrose, the Dancer吗？手风琴给我一种既欢快又暗藏忧郁的感觉,和《长空与纸飞机》其实很搭。"
    me "啊,其实我是从自己的歌单里随便挑的。"
    cordelia "那说明你的音乐品味挺好。"
    me "我啥都听……你甚至可以在我的歌单里找到《我是奶龙》。"
    sayori "（对obedience小声）他不会帮你找leo了。"
    me "喂,我听得见呢！"
    obedience "（憋笑）是我让她这么做的,看看你有没有专心跟我家cordelia聊天。"
    me "什么……喂！不要开这种玩笑啊！"
    sayori "快跑快跑,奶龙大人生气啦~"
    me "（对cordelia）那个……我不是那个意思……"
    cordelia "（低下头）我理解……不过……我还在这里,你也还在这里,对吧？"
    me "嗯。"
    mind "其实我不知道刚刚应该怎么说。但是我们似乎是同频的。没有发生意料中的冲突。"
    mind "音乐真的是一个很好的媒介……我们从音乐开始发现彼此之间的共同点。看到她陶醉的样子,我发现,那才是她少有的松弛时刻。"
    jump chapter62
label chapter62:
    $ in_sayori_route = False
    mind "我们开始两个人去湖边聊天,一起吃饭,一起看电影……sayori现在看到我们总是一脸姨母笑,她真的没有别的想法吗……那就太好了。"
    sayori "祝贺你呀~"
    me "诶？你怎么会出现在广播室？是来找我的吗？"
    sayori "你不应该问我祝贺你什么吗~"
    me "这倒也是个问题,但是……哇,你今天穿得好漂亮啊……"
    mind "我在说什么啊！还有,万一cordelia这时候遇见我们,我该怎么解释啊？可是这话不能说,显得太生分了……"
    sayori "（一字一顿）今天你的好日子。你一定要好好对待你的烤红薯。现在不是三个了,是一个了。"
    me "啊？你是说……可是,你们俩……"
    mind "sayori仍然微笑着,声音也没有任何颤抖,但是她已经开始流泪了。"
    sayori "我知道,自古青梅赢不过天降,我不会破坏你们的好心情……但,我还是要提醒你,你接纳她,就要接纳她的全部,你明白吗？"
    me "我当然会接纳她的全部。你这是什么意思？警告我？"
    sayori "不,当然不是……祝你们幸福。最后抱你一下吧……"
    mind "刚刚出现的一点疑虑和防御消失了。我接受了她的拥抱。"
    $ grant_achievement("拥抱11")
    # 成就: 拥抱11
    me "sayori,你依然是我最好的朋友,知道吗？"
    sayori "（擦眼泪）…………"
    me "sayori？"
    sayori "锵锵！有请新郎和伴郎出场！"
    me "诶,什么？"
    mind "obedience扶着盛装打扮的cordelia从正门走进来。与此同时sayori也把我拉过去。"
    me "呃,我们进展……这么迅速吗？"
    cordelia "只是个仪式,别担心啦~在法律上我们只是独立的自然人。当然,如果你愿意,我们也可以光速领证……"
    me "……这么离谱的表白方式肯定是你策划的吧,sayori！还有为什么她是新郎啊？"
    sayori "嘿嘿~确实。因为我想当伴娘呀,新娘先生。我才不愿意当伴郎呢。"
    mind "这是什么神经理由啊！"
    me "所以说……"
    mind "我看到cordelia笑意盈盈地单膝跪地,我看到了戒指,我看到sayori笑着抹眼泪……后面的事情我都忘了,总之……我们在一起了？"
    mind "…………这都什么乱七八糟的。sayori那天绝对吃菌子中毒了吧。"
    jump chapter63
label chapter63:
    $ in_sayori_route = False
    me "你当时怎么想的？"
    cordelia "其实是obedience先建议的。sayori需要一个告别的仪式,我需要一个浪漫的仪式,所以就这么做了。我们一直在广播站不远处,等sayori发话我们就准备进来。"
    mind "我在犹豫要不要提那件事。但,她已经提到广播站了,我似乎没有理由再藏着了。于是我鼓起勇气提出了下一个问题。"
    me "广播站里,她说的那些话,你们都听到了吗？也是你们计划的一部分？"
    cordelia "当然听到了,sayori又没打算防着我们。至于计划……其实不完全是吧。不过,我很理解她的心情,不会怪她的。"
    mind "cordelia也很温柔。"
    mind "那一天的校园广播里,所有人都听到了我们共同选择的《婚礼进行曲》。当然,领导们不知所措。"
    mind "既然已经在一起了,我们应该适应共同的日常生活。我开始约她去图书馆自习。"
    cordelia "去包图？可以呀！我上完课就去。"
    $ grant_achievement("脚大7")
    # 成就: 脚大7
    mind "我们坐在一起自习。不知道cordelia在写什么,总之我一旦靠近她的电脑她就有点紧张,她上洗手间的时候就把电脑屏幕关上了。"
    mind "是在防着我吗？为什么……"
    me "那个,cordelia,你在……"
    cordelia "嘘……"
    mind "cordelia非常严肃地指了指一块牌子,上面写着“安静自习区禁止交谈”。"
    mind "这算是什么理由啊？为什么呢……"
    mind "我不再试图看她在做什么,很快她平静下来。但是我的心情并不平静,甚至越想越不开心。为什么呢？我们不是已经在一起了吗？当然我知道大家都有自己的隐私,可是……和我稍微解释一下也可以呀,拿图书馆的规则搪塞我算怎么回事呢？"
    mind "她放松警惕了？让我看看……"
    mind "不就是化学课的课件和作业吗……当然她作业写得很认真,不过,这有什么好瞒着我的……"
    me "（小声）作业写得不错。"
    mind "cordelia的反应有点超出我的预料。她立即试图遮住自己的屏幕。不过,她很快转而关上电脑,整个脸憋得通红。她开始收拾东西。"
    me "（小声）不是讽刺,你的化学作业真的写得很好。你要走了吗？"
    mind "cordelia痛苦地凝视了我一会,似乎是下了什么决心。"
    cordelia "（打字）图书馆不准交谈。出来说。"
    mind "我似乎又听到sayori的那句话：“你接纳她,就要接纳她的全部。”我预感什么大事要发生了。"
    jump chapter64
label chapter64:
    $ in_sayori_route = False
    mind "这几天温度回升了。夜里依旧十分燥热。我们走出了图书馆,cordelia把我带到了一块无人的大草坪上,然后坐了下来。"
    cordelia "呜呜呜……"
    me "你哭了？是我惹你生气了吗……"
    cordelia "不是你的错……我,我……"
    me "可是……为什么啊？我想知道……"
    mind "是的,我必须接纳她的全部。我必须知道。"
    me "我永远和你站在一起。你有什么困扰的事情吗？还是说,你也不知道为什么？我……"
    mind "关心一个人真的好难。不知道sayori是怎么做到的,此刻的我完全不知道该说什么。"
    cordelia "……我非常清楚为什么。但是,你真的愿意知道吗？我觉得你很难理解……"
    me "（拉住cordelia的手）告诉我吧。不管怎样,我一定会和你站在一边。"
    cordelia "…………"
    cordelia "你知道吗,“未经许可,传播学院的课件和作业”是违反诚信守则的行为。"
    me "我知道,所以……等等,你不会觉得刚才你违反了这个吧？"
    cordelia "……嗯。"
    me "这条规则是为了惩罚那些恶意侵犯知识产权的人和帮助别人剽窃的人吧。你什么都没做错呀。换个角度说,我……我也只是好奇你在做什么,难道你觉得我是在剽窃吗……"
    mind "cordelia抱着头激烈地抽搐。"
    cordelia "我当然知道你是对的。我不觉得你有错。可是,我无法停止攻击我自己……"
    me "事情都是我做的,要怪也只能怪到我头上,你为什么……"
    cordelia "保管不周,放任可预见的事情发生……我很想找诚信委员会审判自己,可是这太蠢了,徒生事端……也会浪费委员会的时间。"
    me "别做傻事啊。你本来就没做错。而且他们不会抓到你的,压根就没有证据啊。"
    cordelia "不是怕被诚信委员会追究,他们不会管这么宽。问题在于,我会不停地告诉自己“我犯错了,却没受到惩罚”,这种重复会一直让我神魂不定。"
    cordelia "我很可能有OCD。sayori是不是和你说过？"
    mind "啊……真的是这样。我怎么会忘记呢……是幸福来得太快,冲昏了我的头脑吗？我没有看到,她深海般的眼睛之下暗藏的风暴。"
    jump chapter65
label chapter65:
    $ in_sayori_route = False
    me "是的……你,嗯……有没有考虑过心理咨询？"
    cordelia "我高中去过好几次了。不过,没太大用,因为道理我都知道。脚大的咨询室我也去过一次,可是他们建议我去精神科搞点药吃。"
    me "啊？这……"
    cordelia "你会不会觉得我是个神经病？有可能我真的是的……但我还是不敢去,因为我非常知道人们是怎么看待这种事的。"
    me "我和你在一起……你觉得人们会怎么看待这种事呢？"
    mind "其实我不应该问这个问题的。"
    cordelia "人们会对我们敬而远之。不要刺激我,不要和我的死伤发生任何联系；除此以外,在言语上倡导关心关爱,彰显自己的优良品质……"
    me "不是这样的……人们只是不知道该怎么对待……精神病人吧？"
    cordelia "………………"
    mind "她说的是对的。"
    mind "我们躺在湖边无人的草地上,看着夜空谈话。我的心情已经从最初的疑惑不解,转换成了深深的同情与无奈。我知道她没错,她也知道她没错,可是怎么帮助她呢？"
    me "这种事持续多久了？"
    cordelia "自从小时候秋游被抓到玩手机那次就开始了。那是我第一次意识到,自己犯下错误会让身边的人多难过……虽然后来才知道他们只是想吓唬以下我,希望我意识到事情的严重性。……我不怪他们。"
    me "你不怪他们,也不怪我,可是为什么对自己这么苛刻呢？"
    cordelia "那次的结局是我向妈妈认了错,并且翻出了一大堆旧账来请求原谅。妈妈当然很伤心,但还是接受了我的忏悔。也许从这时候开始,我就进入了吹毛求疵、自我攻击、请求权威审判或宽恕的循环。"
    me "可是现在你的权威不再是妈妈,而是诚信委员会之类的东西。你不可能保证他们完全接受你。"
    cordelia "……对。可是,我就会因此觉得：我为什么不敢接受审判？是因为我自己确实觉得自己有罪吗？"
    me "……我不知道该说什么。"
    cordelia "我让你感到厌烦了吗？或者,害怕了吗？没关系,你可以把戒指还给我,我不会怪你……"
    me "不,怎么会！只是我确实想不出来该说些什么……哦,为什么你觉得这个是强迫症？我印象里的强迫症大概是不擦干净就不舒服那种……"
    cordelia "那种确实更常见,但OCD的核心是强迫行为。不停地思考同一个荒谬的念头,也算OCD。当然,专业的诊断是不可替代的,我只是怀疑。"
    mind "这个时候,如果我是sayori,我会怎么做呢？"
    $ grant_achievement("拥抱12")
    # 成就: 拥抱12
    mind "于是我抱了抱她。我告诉她,就像sayori说的那样,你一定要相信自己是个好人。不过,她似乎还是在颤抖。"
    jump chapter66
label chapter66:
    $ in_sayori_route = False
    me "为什么那天提到游泳池,你那么紧张,和这个有关吗？"
    mind "本来放松下来的她,整个人痛苦地痉挛了起来。"
    cordelia "我一直尝试告诉别人自己的感受,但别人一直无法真正理解她,只会说“没被抓到就好啦”之类的话。这让我感觉自己真的犯错了,所以更糟糕。还有些人觉得我就是矫情……"
    mind "我不知道这和游泳有什么关系,但是我依然在听。"
    cordelia "有一次我怀疑考试时自己瞟到了前座的答题卡。我直接找监考老师,然而监考老师完全不理睬我。这在他看来纯粹是没事找事,增加工作量的行为。"
    me "你想让监考老师惩罚你？"
    cordelia "我当然不想被惩罚……但是比起被自己批判,我宁愿拿一个0分。"
    cordelia "可是我被完全无视了……前所未有啊。痛苦转化成了愤怒————既然世界不在意我,那就让世界付出代价。"
    me "你……伤害别人了？"
    cordelia "（摇头）我能做什么坏事呢。其实就是故意在游泳池里打了一次喷嚏。当然,没有人注意到这件事。"
    cordelia "可是,当我冷静下来后,这件事反而成了更深重的道德枷锁。我再也不敢游泳了。我让水变脏了,那自己就比水还脏。"
    me "别这么想啊……你就当做是自己呛了一口水,从你的鼻子进嘴巴出……"
    cordelia "不……这是不一样的。我是主观上有恶意,不可以这样搪塞过去……"
    cordelia "（突然站起身来俯视着我）此刻你在尝试与我共情,你觉得我过得很痛苦。可是,为什么我要告诉你这一切？为什么要用这么文学化的方式？我想,我恐怕是在表演罢了。你理解我的意思吗？"
    cordelia "你可能会告诉我,我的情绪都是认真的。可是这样的话我对AI说了很多很多遍,难道我的情绪一直都那么强烈吗？不……我只是陶醉在一个假装平静实则崩溃的完美受害者的角色里啊。看起来平静的我,和崩溃的我,还有现在告诉你我在表演的我,其实都是表演出来的吧……"
    cordelia "我的感受,我的言语,甚至于我试图被审判的行为,都是虚伪的表演……这就是审判的结果————"
    cordelia "我是假的……"
    mind "此刻的我同样痛苦。我又能说些什么呢？也许,就这样一直陪她躺在这里,这是我唯一能做的吗？……或者,问一个更深刻的问题……"
    "我还要选择她吗？"
    menu:
        "此情不移！":
            jump chapter67
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter67
label chapter67:
    $ in_sayori_route = False
    mind "我握着她的手。此刻我们的灵魂一起震颤。"
    cordelia "你我都无法回答这个问题……"
    mind "她突然开始轻轻扇自己耳光,我赶紧拉住她的另一只手。"
    me "不可以伤害自己！"
    cordelia "我下手很轻的。顺便一说,这也是表演,不要担心我……"
    me "即使轻轻的也不可以,我会心疼。"
    mind "这句话出口太快,我还没意识到其中的分量。cordelia悲哀地看着我的眼睛。"
    cordelia "你是说……你会心疼我吗？在意识到我是个大麻烦之后？"
    cordelia "假如sayori没有策划过那场“婚礼”,我们没有承诺。再给你一次重新选择的机会。"
    "做出选择！【提示：这是一个重要的决定】"
    menu:
        "我爱你,直到永远……":
            jump chapter68
        "我们是永远的朋友……":
            jump chapter69
        "无言的拥吻":
            jump chapter70
label chapter68:
    $ in_sayori_route = False
    cordelia "你爱我吗，哈哈……"
    me "我……这就是我的选择啊！"
    cordelia "我有什么值得你喜欢的？一个斤斤计较、歇斯底里的人？一个自诩质洁行廉，实际上只是为了站在道德高地上的人？……你只是喜欢我的外表吧？只要我看起来是这个样子，我的痛苦，就都只是某种属性，对吧？"
    me "我……"
    mind "是啊，我到底在喜欢她的什么？"
    cordelia "可是，以后呢？如果我老了、丑了呢？甚至于，即使我青春永驻，你真的能一直忍耐吗？"
    cordelia "我早就应该知道，我压根就没有爱人的能力……我只是希望被你共情，可是你当然会这么做啊，因为这就是你啊。我的行为不就是操控吗？"
    cordelia "而且……现在你同情我，那是因为我在伤害自己。如果我们真的在一起了，我伤害的可能就不只是自己了。我们将一起面对OCD的审判，你真的做好了这样的打算吗？？"
    me "如果是为了你的话……我可以迈出这一步。也许我会尽力帮你走出来？"
    cordelia "我就知道……你没意识到吗,你已经被我PUA了。你的行为在我的预料之中。我就是这样在表演中收获同情的人啊……所以那个老师无视我,我才那么生气吧。"
    me "啊？不……我是真心的,不是这样的……"
    cordelia "这句话是不是听起来也很惨？这也是表演,你要记住啊。我是假的,我不值得你投入那么深重的感情……"
    cordelia "我总是想告诉自己我没事。因为我怕疼,因为我还贪恋生命。可是正是因此,我总是在怀疑自己到底是不是真的痛苦……"
    me "cordelia,你可以不接受我的爱,但是你先答应我,不要伤害自己！！"
    mind "cordelia松开了我的手,轻轻摇了摇头。她的眼神如此黯淡,让我想到重庆南路上见到的monika。"
    cordelia "这不是爱。我也不能答应。"
    cordelia "恐怕我不能总是用语言证明自己的痛苦了,那些都可能是表演。我需要一个不可否认的东西……即使那也是一种表演,至少看起来更逼真吧？"
    cordelia "所以……如果我辜负了你的感情,我致以最诚挚的道歉。当然我知道这只是同情。不过你没办法追究我的责任了……"
    me "cordelia！！"
    mind "她把一个纸团抛在我手里,同时进一步拉开了和我的距离。"
    cordelia "我爱你,再见……"
    mind "在我反应过来之前,她已经从几米高的坡地上跳下了湖。湖并不是很深,我准备跳下去救他。此时我看见了湖水上漂浮的血花。"
    mind "她是头着地的。"
    mind "我急不可耐地打开那个纸团,那个她存在过的最后证明。"
    paper "“你好！这是我在婚礼前写的,我想有一天可能会用上。当然我不希望如此,但如果真的发生了,请你节哀。”"
    paper "“首先,如果警方来传唤你,你可以把这张纸交给他们。我证明不是你干的,完全是我的个人行为。当然也和学校没有关系。我对自己犯下的罪行以及给大家带来的麻烦再次道歉。”"
    paper "“如果你感到痛苦,请你千万不要伤害自己。那是愚蠢的行为,而且解决不了任何问题。”"
    paper "“我会建议你和sayori在一起。拆散了你们,我很抱歉。现在是时候修正这个错误了。但愿sayori还会接纳你。”"
    paper "“请忘记我吧。我会成为你们的障碍。但,我还是想说一句……”"
    paper "“我爱你,再见。”"
    "感谢您完成C-1线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局4")
    # 成就: 结局4
label chapter69:
    $ in_sayori_route = False
    cordelia "朋友吗……你是理智的。"
    mind "她笑了,站起身来,走向黑夜深处。她的声音越发远了。我没有追。"
    cordelia "我应该知足……至少你能够理解我,我已经很感激了。我不应该有非分之想……去找sayori吧……"
    mind "这就是我的选择吗？渣男……"
    obedience "诶,你怎么在这里？一个人？cordelia呢？"
    mind "我解释了一下发生了什么。"
    obedience "怎么会那么严重呢？甚至要吃药？医生总是喜欢把一切都说成病……我不觉得这是不可克服的。"
    obedience "咨询或吃药太离谱了。其实她只是需要一些情感上的帮助吧。我建议把cordelia约出来,让朋友们一起劝她正常一点。"
    me "“正常一点……”我理解你的意思,但我觉得这么做不妥当吧。"
    obedience "哪里不妥当了……你可是人家男朋友,刚刚还害得人家哭了一场,能不能稍微有点担当？你不做的话,我帮你做。"
    mind "是我在逃避吗……"
    mind "几天后,她真的这么做了。她拉了一大群人,轮番劝cordelia。她用她以为积极的方式羞辱了cordelia脆弱的内心世界。"
    mind "她不知所措。自我审判和要求权威审判是一回事,被没有权威的别人审判就完全是另一回事了。即使审判的结果是“无罪”。"
    cordelia "你们……为什么会知道这么多……"
    obedience "你的行为确实没错啊,但是你的心态不对。一直这样下去你会撑不住的。不要那么玻璃心……"
    mind "后来我才知道,这个叫“有毒的积极性”。"
    mind "最终cordelia想起了我。她大哭着要和我绝交。她走了,然后我收到了一条微信。"
    cordelia "（打字）你没有做错任何事情……我刚才的反应是不对的,千万别往心里去……千万不要内疚,可能只是我不适合呆在这里。"
    mind "我宁愿她真的骂我,可是她还是那么温柔。她只是把最大的苛刻留给了自己。我去找她,她不想见我。我们只能用微信对话。"
    cordelia "（打字）不需要找我道歉……是我的不对。"
    me "（打字）如果你因此受到了伤害,我会难过。是我的错。"
    me "（打字）你想让我为此而愧疚,还是让我因为“扯平了”就忘记自己的痛苦？你真是个温柔的人啊。放心吧,我什么都不会做的,你不需要为我背负任何责任。这不是气话。"
    mind "我们确实不可能成为朋友了。很快她成为了交换生,后来又出国留学,听说一直处在孤独之中。听出国留学的同学说,她有时候会一个人喝薄荷酒,眼神愣愣地凝望着东方。"
    mind "我们再无瓜葛,只留下一点无法消除的内疚永存我心。那是一个幸运的人对不幸者的愧怍。"
    "感谢您完成C-2线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局5")
    # 成就: 结局5
label chapter70:
    $ in_sayori_route = False
    mind "她蜷缩起来,仿佛第一次感受到如此热烈的爱与共情。"
    me "我……是不是有点越界了？"
    cordelia "（轻轻摇头）抱着我吧,就这样下去……"
    $ grant_achievement("拥抱13")
    # 成就: 拥抱13
    mind "但是此刻,我们之间必须有一个是坚强冷静的。只是拥抱,无法解决任何问题。"
    me "我知道你现在很难过,但请你先听我说：没有人有资格审判你,包括你自己。"
    me "你也没有义务把自己推到审判席,因为真的什么都没做错,这是一个莫须有的审判庭。"
    me "世界并没有以你为敌,你的敌人也不是自己,只是OCD。"
    cordelia "这些话AI都说过。你能关心我,我很感激。可是,这些都是因为我看起来很可怜……是用表演骗来的关心,你觉得真的有用吗？"
    me "你把自己困在了一个自洽的死循环里。关心是你骗来的,攻击或无视就是你应得的？你这是不允许自己快乐啊。"
    cordelia "……对。这是自虐。这是我的宿命。"
    me "不对不对,我不应该说是“你”不允许自己快乐,因为会让你觉得还是你在矫情。不,你是好人,永远都是。唯一的坏蛋就是OCD。它有时候会控制你,这不怪你,是因为它太强。"
    me "但是,这不是你的宿命。如果你不想去看病,这很正常,但你仍然可以去抵抗它。只要她愿意,我永远在她身边,陪她一起,抵抗它,到最后一刻。"
    cordelia "可是……你为什么要陪着我呢？"
    me "为什么？这不是很自然的事情吗？"
    cordelia "为什么选择哭哭啼啼的我，而不是开开心心的sayori？你本来值得更好的生活……"
    me "sayori……她和你不一样。也许在内心深处，我和你是一样的，你知道吗？如果是sayori的话，也许我也能过得很快乐，可是我不能接受你的自虐。让我们相互取暖吧。"
    cordelia "你们真的都很温柔啊……"
    me "我永远在这里。"
    cordelia "永远吗？"
    me "直到苍穹的尽头。"
    mind "她没有奇迹般地痊愈。有些夜晚,她依然会哭着缩进我的怀里。"
    mind "我无法给出关于“真实”的绝对证明。我只会这样说……"
    me "真正的演员,不会展示自己的剧本。你就是你。你在我眼中是真实而可爱的。这就够了。"
    cordelia "嗯。"
    "感谢您完成C-3线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局6")
    # 成就: 结局6
label chapter81:
    $ in_sayori_route = False
    me "（远远地拍了一张照片,发给obedience）"
    me "……你好？这里是学生会吗？我是来面试的。"
    leo "哦？新生啊,请到这里来。我是学生会主席leo,我来负责你的面试。"
    mind "日理万机啊……看样子是完全没记住我。"
    mind "面试进行得很顺利,我“就职”了。"
    me "（打字发给obedience）见到leo,顺利上岸。"
    mind "刚出学生中心就遇到了大家。看来obedience是把所有人都求了一遍。"
    obedience "啊啊啊谢谢你！！甚至还给我发了男神的侧脸,哦哦啊哦~"
    cordelia "偷拍是不对的。"
    me "诶……嗯……"
    sayori "在法律上,只要不太变态,一般都不会被追究哦~"
    cordelia "但是道德上……反正我不会对我喜欢的人做这种事。"
    obedience "mua~mua~喜欢~男神~"
    me "……这孩子疯了。"
    me "那么,接下来该怎么办呢？我能见到他的机会不是很多吧,怎么给你们俩撮合一下？"
    obedience "嗯呢……顺其自然就好吧……不过,也不能进度太慢……"
    sayori "不能太慢,小心你当了几年的朋友还只是备胎~"
    mind "怎么感觉语气这么幽怨……"
    me "话说这样的obedience还是第一次见到呢。我一直感觉你是个非常务实的人。没想到……"
    sayori "是个恋爱脑。"
    obedience "嘿嘿……leo学长很有名的,你们不知道吗？哦,对了,只有我是本地人……他高中和我一个学校的,也是学生会主席。而且,多才多艺,长得又帅,家里也很有钱……追他的女生能坐一个教室了。"
    mind "好直接的评价标准啊……从某种意义上说,她确实是一个很实际的人。"
    sayori "那,他接受了吗？"
    obedience "啊,肯定谈过几个,这个大家也都传开过了。实际上被接受的也不在少数呢……不然,像我这样普通的人,怎么敢……"
    cordelia "恶心……你不觉得谈得太多是某种污点吗？"
    me "呃……那好像也不能这么说。感情的事是你情我愿吧。"
    obedience "我觉得没啥……要是我也有那么多男生追,我肯定也朝三暮四啊~多犹豫一秒都是对青春的不敬。"
    cordelia "……我不会这么做。这么做的人,恐怕只是把那些人当玩具吧。"
    mind "obedience瞬间怔住了。不过,她很快又恢复了正常的样子。"
    obedience "……我也不会这么评价朋友喜欢的人呢。"
    cordelia "啊,抱歉……对不起。"
    mind "sayori一直在静静地听。这时候她突然靠近了我。"
    sayori "（小声）感觉要吹。"
    me "（小声）诶？这么早就下结论吗？"
    sayori "（小声）我在文学社见过这个leo。第一感觉,他们不合适。"
    me "（小声）那,你为啥不劝劝她……我还要帮她吗？"
    sayori "（小声）你看她会听吗？怀春的少女,怎么劝都劝不过来的。"
    sayori "（小声）恐怕你不帮也不行了……不过,失败了以后,你顶上怎么样？"
    me "诶诶诶？？"
    mind "cordelia仍然在一边道歉一边试图劝说obedience。她们没有注意我突然的惊叫。"
    sayori "（小声）承认吧~是不是打算当《悲惨世界》里的爱潘妮,帮着马吕斯去追珂赛特？"
    me "呃,啊,我要去上个厕所！"
    sayori "（小声）切,胆小鬼~（大声）回来的时候帮我在售货机那里买杯橙汁,要那个NFC的,钱我转给你了！"
    mind "我一路跑到了不远处的教学楼里。我表现得这么明显吗？"
    jump chapter82
label chapter82:
    $ in_sayori_route = False
    me "（打字给sayori）你为什么觉得他们俩成不了呢？"
    sayori "（打字）果汁买了？在厕所？"
    me "（打字）6"
    sayori "（打字）你可能看不出来……但我觉得,leo配不上obedience。"
    me "（打字）配不上……诶,等一下,谁配不上谁？"
    sayori "（打字）我没写反,我就是这样认为的。Let's see..."
    sayori "（打字）对了,我警告你啊……"
    mind "她说我是爱潘妮……劝我不要当败犬？可是马吕斯和珂赛特是成了呀,她不是觉得他们俩不行吗？如果obedience没追到leo的话……想想怎么有点开心……"
    sayori "（打字）你最好没有把我酸酸甜甜贵贵少少的橙汁带到厕所里！听到了吗,放书包里也不行？不然你就自己喝那个,再给我带一个来！"
    mind "诶……可是我就是装在书包里了,这也不可以吗？真是的,明明知道我不想糊弄她……"
    mind "……哈哈,懂了。这是想让我也喝到吗？即使她已经明白了我的选择不是她,而是obedience？"
    mind "sayori真是个温柔的人呢。"
    jump chapter83
label chapter83:
    $ in_sayori_route = False
    mind "加入学生会以后,我主要是到处跑腿。确实有更多的机会见到leo了。"
    leo "社团年度审批……老师们怎么说？"
    me "老师说学生会自己定就好。"
    staff "新来的,对leo主席说话居然不加称呼,太不敬了！"
    leo "唉,对学弟要友好,知道吗？叫我学长就行。"
    staff "是,学长！"
    me "……leo学长,所以说学生会可以自己决定社团年度审批的事,不用再往上传达了。"
    leo "好,我来看看……文学社,哈哈,虽然monika那个家伙跟我很不对付,但是我的素拓还得指望她呢。过了过了……"
    leo "（小声）可恶的monika,居然看不上我……假装清高的小蹄子……"
    mind "好像听到了什么不该听到的东西……"
    me "呃……嗯,学长,我还在这呢,我是不是最好回避一下……"
    leo "你在就对了……回避一下,是不是要和你的monika学姐报个信呀？嗯？"
    me "啊……不是！绝对不说！您是老大！"
    leo "嗯……这还差不多。小朋友有觉悟,我很看好你哦~"
    leo "再拿一张来。奶龙cosplay社,什么乱七八糟的,否了……"
    mind "我感觉自己正在把obedience推入火坑,但是计划进行到这一步了,没办法了。"
    me "呃……leo学长,有一个女生托我带了一份礼物给你,里面还有情书。"
    leo "别告诉我是monika让你来的。"
    me "怎么会呢哈哈哈……不过,她不想让我告诉你她是谁。"
    leo "（两眼扫完情书,然后一拳砸到桌子上）可恶！真的不是monika的字啊！……又是巧克力,无聊……你拿去吧。"
    me "诶,毕竟是礼物,我拿了是不是不太好……"
    leo "小朋友？学长心情不好,你最好把这些东西带走哦~我不在意你把它们扔到哪个垃圾桶……"
    me "啊啊啊对不起对不起,学长送我巧克力我非常感谢,今天的事我什么都不会说的,啊啊啊学长再见！！"
    leo "……无聊。说起来,会会她也不是不行……喂,小朋友,情书还给我一下。"
    me "诶？好的……"
    leo "她不许你告诉我名字,正好,这样才有意思嘛。不过,不许告诉她巧克力在你这里哦~学生会的同学们会监督你的。"
    mind "我哆哆嗦嗦地走出了办公室。leo真的有这么大的权力吗……应该不至于吧,但是我不想以身犯险。"
    jump chapter84
label chapter84:
    $ in_sayori_route = False
    mind "回到宿舍,打开obedience的巧克力,我心情非常复杂……吃了一块,感觉十分苦涩……正如我此刻的心情。"
    mind "告诉她,还是不告诉她？我的心意,又该怎么传达？我为什么会有点喜欢她呢,我也无法理解这一点……也许就是从第一次见面开始,我会觉得她笨拙地接近我们有点……可怜？"
    sayori "Ohayou！！"
    me "诶,你怎么进男生宿舍了……"
    sayori "嘘……宿管阿姨被可爱的我迷死了,我说我是来找男朋友聊天的,她说我可以上来半小时~"
    me "这位小姐,请自重啊！"
    sayori "嘻嘻,开个玩笑~巧克力送出去了吗？"
    mind "现在我挡在自己的桌子前,所以sayori暂时没看到桌上的巧克力。"
    me "啊……这个……"
    mind "和sayori说应该不会暴露吧？"
    sayori "哇！好吃的,我要吃~"
    mind "……只看吃相的话,很难想象sayori是个一点也不胖的美少女。"
    sayori "诶,等一下,爱心形的……我是不是……搞砸了？"
    me "别担心……前因后果有点复杂。"
    mind "我解释了一下leo拒绝但没完全拒绝的事。"
    sayori "渣男……那,你打算怎么跟obedience说？"
    me "我没想好。"
    sayori "你也可以直接去追她呀~不一定非要等她被leo甩掉的。"
    me "啊……想不清楚,想不明白,我太软弱了……我要学习中国近现代史纲要来解决精神缺钙的问题……"
    sayori "啧啧,逐客令啊~官老爷的做派学得倒挺快。拜拜！"
    me "拜拜！"
    mind "到底怎么办呢……"
    mind "从窗户里看着在楼下对着宿管阿姨卖萌的sayori,我突然有了主意。"
    jump chapter85
label chapter85:
    $ in_sayori_route = False
    me "sayori！！"
    sayori "诶？怎么啦？"
    me "去喝奶茶,我有话要说……"
    mind "宿管阿姨的笑意完全藏不住啊！"
    mind "附近有一家咖啡厅。在户外找到了一张小桌子,上面有一顶灰色的小伞。"
    sayori "这个烧仙草好喝~"
    me "我说……你和宿管阿姨都这么说了,我以后咋解释啊……你这是把我和你拴起来了？"
    sayori "呆jio不~到时候你就说和我分了呗。然后宿管阿姨会觉得你是负心汉,每天给你的宿舍扣分……哈哈哈哈~"
    me "哈哈哈哈……都大学了,扣不扣的无所谓啦……"
    me "我该怎么跟obedience说呢？我不想当leo的共犯,但是我也很怕他。"
    sayori "嗯……慢慢告诉她,每次透露一点点暗示？直接告诉她的话,结果是无法预料的。"
    sayori "你一点一点地展示他的真面目,但是不要评论。让她自己去感觉。而且……leo估计很快就会现身了,你无法阻止他伤害cordience,但是你可以在她被伤得不那么惨的时候去救她。可怜的cordience……"
    me "这是不是有点乘人之危啊……我好像在算计喜欢的人。"
    sayori "不救是本分,救了是缘分。早救晚救,全凭良心。主要是你要的太多了……你就不能不喜欢她吗？那样事情就好办多了。"
    me "Nope,我是纯爱战士。"
    sayori "随你吧……我会支持你的。"
    mind "支持我追cordience吗……感觉sayori更像是可怜的爱潘妮吧。"
    mind "两小时后,同一家咖啡厅。"
    me "……leo在审核社团提交的材料,我帮他递文件。他休息下来和别人聊天的时候,我跟他说“有一个女生很想认识你”,于是我把礼物和情书都给他了。"
    obedience "嗯嗯！怎么样,他什么反应？"
    me "他……嗯,他很快就看完了你的情书,然后……呃,他觉得你的礼物有点普通。不过,他说他对你有兴趣,叫我先别说你的名字,他觉得这样很有趣。"
    mind "我应该不算是在说谎吧……"
    obedience "很快就看完了情书……"
    mind "意识到了我的暗示吗？"
    obedience "果然是一目十行的leo学长！我就羡慕这种看书看得快的……怪不得学长成绩那么好……"
    mind "不是,哥们？"
    me "那接下来怎么做？"
    obedience "你接着给我传递一些情报,同时跟他透露一下我的事情……既然他不想知道名字,那就先藏着这个。其他的,你都可以说呀。你这次注意到了什么leo的动态吗,我想听。"
    me "嗯,leo在学生会里说一不二,他不喜欢奶龙cosplay社,所以直接把申请否了。"
    obedience "哇哦~杀伐果断……我也不喜欢奶龙。"
    me "leo参加了文学社,他在那里混素拓加分。"
    obedience "啊啊,羡慕sayori……可惜文学社招新刚刚结束。"
    me "嗯……最重要的一点,leo好像有关注的女生了。"
    obedience "诶？是我吗？"
    me "嗯……这个,我说不准,他确实说过可以考虑见你……"
    obedience "没关系的,就算不是我,我也会用自己的心意证明自己……"
    mind "恋爱脑,真救不了……"
    jump chapter86
label chapter86:
    $ in_sayori_route = False
    mind "又过了几天,我又被叫到学生会干活。休息时间,leo把我单独叫到办公室。"
    leo "嘿嘿,小朋友,你的保密工作做得不咋样哦~"
    mind "！！不会是跟sayori说的话泄露了吧？"
    me "呃呃,我没乱说啊……"
    leo "想啥呢,你都叫我老大了,大家都是自己人啊？我不会怀疑你的。我是说你要隐藏的那个女生的名字。是叫obedience吧？"
    me "老大威武……可是,您是怎么找到的？"
    leo "嘿嘿……派两个人跟着你不就好了？你一共就和那么几个人来往,稍微排除一下就差不多了。"
    mind "……跟踪我？真的没发现吗？啊,还有“一共就和那么几个人来往”……杀人还要诛心？"
    leo "长得一般般吧,不过倒是不装矜持,这个挺好。当然矜持的我也能拿下~顶着这张脸,来个颠佬都能当把妹王。"
    me "真的……这么容易吗？"
    leo "真的这么容易,只要建模够好。建模够了以后,你怎么发癫都会被解读成某种萌属性。自有大儒为我辩经。什么高冷风、霸总风、禁欲风……要我说,全都有点疯。我看你瘦下来可以当纯情男大,不过前提是你要瘦下来。"
    me "啊……谢谢学长。真的是这样吗……那,obedience这种的,在您的追求者里,肯定排不上号吧？"
    mind "我再努力一次！"
    leo "当然,像她这种的大街上到处都是……不过,我决定给她一个机会。"
    me "诶？为什么？"
    leo "当然是为了给新来的小朋友一点面子啦~你也是受人之托嘛。怎么样,感不感动？不过丑话说在前头,我可不打算真的怎么着。我只是见她一下,仅此而已。"
    mind "对不起啊,obedience……"
    leo "你回去跟她说,明天下午五点,我约她去喝下午茶。"
    me "诶,可是那个点我们都有课吧……现在请假也来不及了。"
    leo "你们有课,我没有课。恋爱需要诚意对吧？去吧。"
    me "唔,好的……"
    jump chapter87
label chapter87:
    $ in_sayori_route = False
    mind "当天的晚些时候。"
    obedience "哦哦哦哦哦！太好啦！！！谢谢你！！婚礼的时候你绝对要坐首席！！"
    me "呃呃,先别想那么远……你真的打算翘课去约会吗？我记得你的学术写作老师会点名的。"
    obedience "唔……而且这次的presentation是我们小组的,要计分的……"
    obedience "你跟他说了吗？可不可以换个时间？"
    me "嗯,说了……他说要看到你的诚意。"
    mind "快翻脸啊！我在等你……"
    obedience "啊……有道理。嗯……虽然我的学积分很危险了,但,这才能证明我是认真的,不是吗？"
    mind "笨蛋啊,救不了了……我真的喜欢这样的人吗？"
    obedience "就这么定了！到时候,你乔装一下,在旁边找个地方坐着。你需要听完全程才能帮我参谋,不是吗？"
    me "好在我的老师不点名……好吧,我会藏在附近。"
    mind "为什么我也要为了她翘课啊？这下真成小丑了……除非他们吹了……啊,这是肯定的,考虑到leo说的那些话……"
    jump chapter88
label chapter88:
    $ in_sayori_route = False
    mind "第二天,下午四点,同一个咖啡厅。我提前剪了个头发,又穿了一件新买的卫衣,坐在角落。应该没有人认出我吧。"
    leo "哈哈,就是你吗,obedience？你写的情书我看过了。"
    obedience "（脸红）leo学长……你喜欢吗？"
    leo "有点太过肉麻了吧。嘿嘿,所以我把你约出来了。这样聊天感觉不是更自然吗？"
    obedience "（脸红）啊！真的是这样！你选的地方也很好,这里很雅致……"
    mind "我昨天不也是在这个咖啡厅和你聊天的吗……"
    leo "嗯,我经常来。你平时来这里吗？"
    obedience "啊……太贵了,我一般都是喝瑞幸呢……"
    leo "瑞幸？这倒提醒我了,有一个叫睿幸的漂亮学妹穿着JK在绿园餐厅等我呢,这个天气穿JK实在是难为她了……不过我们暂且不去管她。我一般都是来这里,因为这里的氛围很有情调。钱？身外之物,我不在意。"
    obedience "唔……"
    mind "来者不善啊……"
    leo "那么,说说看吧,你是怎么知道我的？虽然我知道我很有名……你最好给出一个特别一点的答案,太普通的我早就听腻了。"
    obedience "啊！其实……学长还在读高中的时候,我就听说您拿过拉丁舞比赛的一等奖。大概就是从那个时候开始……就喜欢上了,后来我就用各种途径获取了您的动态……"
    leo "（打断）哦！有点意思……你都知道些什么？"
    obedience "您拿过拉丁舞、萨克斯、滑冰的奖,在学生会拿了很多奖励,化学奥赛打到了国赛,然后保送来了这里……"
    leo "（打断）停停停,不是这种。我是说……关于我的社交生活,你知道多少？"
    mind "刚刚还滔滔不绝的obedience似乎突然哽住了。"
    obedience "（小声）……我只知道,您很受欢迎呢。"
    leo "哈哈……好,这也算是一种了解。那么,你凭什么觉得,我会看上你？要知道,我可是很卡颜的哦。"
    mind "obedience看起来失魂落魄。是心痛的感觉吗……这种感觉,如此熟悉……"
    obedience "我……我可能不如其他人优秀,但是……我肯定会坚持到底……"
    leo "就这些？"
    obedience "真的……如果你选择了我,我会尽己所能去帮助你的……"
    mind "舔狗,舔狗,舔狗……也许这一切在一开始就是错误？"
    leo "你觉得你能帮到我什么？"
    obedience "…………"
    leo "说话呀？回答不上来吗？"
    obedience "……我觉得这不是约会的人该说的话。你比我帅,比我有钱,比我受欢迎,那就了不起吗……（声音越来越小）"
    leo "哈哈哈！小朋友,你终于理解了成年人世界的本质。对的,我就是比你了不起。还有一个你漏了,我综测分比你高。婚恋就是价值匹配,你觉得自己有什么资格喜欢我？你的价值呢？"
    obedience "我……我的品质比你高尚！"
    leo "哈哈哈……好,品质高尚的人。那我问你,你喜欢我这样一个品德低劣的人,是为什么呢？"
    mind "obedience怔住了。我知道答案是什么……但是太低劣了,如果我是她,我也只能愣在这里。"
    leo "（小声）你也就只是看上我的这些东西,对吧？"
    mind "leo的目光望向遥远的地方,眼神里流转着愤怒的焰火。"
    leo "（小声）女生们蜂拥而至,因为什么呢？无非就是这些罢了……她们看上了我的身外之物,并且觉得自己也有不少。可是,有人真的在意我吗？如果我一贫如洗,五短身材,你还会这么卑微地来找我吗？"
    leo "我等啊等,各种类型的美女都看得审美疲劳了,我终于等到了你。我不知道你怎么敢来找我的。我还以为……终于有一个能懂我的人。没想到……你们几乎都是一丘之貉。"
    mind "难道这就是他对monika有执念的原因吗？因为终于有一个人看不起他了？"
    leo "（小声）你们这种人就是欠收拾,明白了吗？"
    obedience "我……我喜欢你,还有错吗？你凭什么“收拾”我？我会喜欢上你这样的人,真是瞎了眼……"
    leo "很好,你恢复了刻薄的本性……有点意思。但是,然后呢？你要给我一耳光,然后拂袖而去吗？哈哈哈哈……"
    obedience "刻薄是我的本性？凭什么这么说？"
    leo "你有朋友吗？如果你非要说有的话,你吐槽他们、和他们酿成冲突的时候难道不算少吗？"
    obedience "你……"
    leo "（小声）我的朋友可比你多多了……我知道你的一切。我也不在乎你的感受……面对现实吧,小朋友。"
    mind "obedience似乎已经开始流泪了。"
    obedience "所以……把我约出来,只是为了羞辱我吗？"
    leo "羞辱？不不不……这只是一个客观的评价罢了。你要是能认清自己的定位的话,我也可以考虑介绍你成为我舔狗的舔狗的舔狗。懂我的意思吗？那群姑娘太坏了,不能光吊着人家小伙子呀。这是一项神圣的工作。"
    mind "obedience远远地望了我一眼。此刻我们的眼里都饱含泪水。她的眼里除了痛苦,只剩下不知所措的无助。她在寻求我的帮助。"
    "就像那次喝酒一样,烈火烧心,但不只是因为obedience的遭遇,我想到了已经过去的事情……我该做什么？"
    menu:
        "悄悄离开":
            jump chapter90
        "用拳头猛击桌子":
            jump chapter99
label chapter90:
    $ in_sayori_route = False
    mind "对不起了,obedience……我撑不住了。"
    mind "我避开了她惊恐的目光,走到了校门外的小巷子里。华灯初上,餐厅都开张。我却感觉身边无比寂静。"
    mind "物化,价值,舔狗……"
    mind "不要去想那个人,不要去想那件事,不要去想……"
    mind "在感情里不要谈对错,拒绝至少比吊着我好,不要去想那个人……"
    mind "可是,那么多自我感动的瞬间,叫我怎么忘记……还有……"
    mind "我真的喜欢过obedience吗？当然,她不符合物化的标准。可是,我是不是在用这种方式“表演”一个反物化战士的形象呢？"
    mind "又或者说……我依旧在用物化的标准思考问题,只不过这次不是“她有多好”,而是“她太糟糕了,我一定可以追上”？我是不是觉得,面对obedience就可以自信起来了？"
    mind "然后,在她最脆弱的时刻,我选择了逃避……"
    mind "懦夫……"
    mind "对不起……"
    mind "我的脚步停了下来。走到死胡同了呢。啊,在上海应该叫弄堂口……"
    me "sayori,是你吗？"
    mind "我不知道我是怎么感觉到的……回头,她果然在那里,脸上挂着忧郁的笑容。"
    me "你也在咖啡厅里？"
    sayori "……嗯。"
    me "只需要一个眼神我就明白了。她一直……悄悄担心着我们。她也看到了我的选择……可耻的逃避。"
    sayori "你真的想清楚了吗？你还有机会。我会帮你解释。"
    me "你会选择一个抛弃了你的人吗？"
    sayori "…………"
    me "我没有机会了……我辜负了她。你会因此讨厌我吗？毕竟你总是对大家都那么好。"
    sayori "我很遗憾……但是,允许我此刻自私一下吧,我更在意你。"
    me "嗯……"
    sayori "那么……我还有机会吗？"
    mind "sayori站在弄堂口的另一侧,我看到她身后的路灯,闪烁着温暖的黄光。"
    me "我永远在这里。"
    sayori "抱一抱吧。"
    $ grant_achievement("拥抱14")
    # 成就: 拥抱14
    me "这就是我的最终选择……"
    mind "那一天同样是obedience的转折点。她在被羞辱之后,痛定思痛,居然真的认可了leo的那套歪理。leo既是她的仇人,又是她的启蒙者。"
    mind "后来的她变得非常“有名”,因为她跪舔很多很多生意人。学校的名声因此受到了影响。又因为吃了两次学业预警,被劝退了。这下她反而可以更自由了。"
    mind "她一边赚钱,一边做整容,慢慢地也有人来做她的舔狗……她被称为“捞女之王”。"
    mind "cordelia鄙视她的作为,很快就跟她绝交。我和sayori也没再联系过她,但原因不太一样。也许,她变成这样,也有我的原因吧。我的沉默,成了leo那套理论最坚实的背书……"
    mind "我为她的堕落感到深刻的抱歉。但是,我必须背负着这份歉意苟且偷生……因为sayori还需要我。或者说,她为了让我活下去,给我带来了这种感觉。我必须活下去。"
    mind "这就是我们的故事……一个不是悲剧的悲剧。"
    "感谢您完成O-2/S-4线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局7")
    # 成就: 结局7
label chapter99:
    $ in_sayori_route = False
    mind "我用拳头猛击了一下桌子。希望她懂我的意思吧。"
    mind "一声脆响。obedience真的给了他一记耳光,并且把没喝完的咖啡全砸在他脸上。"
    obedience "你这个有妈生没妈养的狗崽子,我今天真是给你脸了！"
    leo "你……？！"
    obedience "好,大家都喜欢你的脸,你的钱。就你最清高,是吗？然后也用这个标准评判别人,糟蹋别人的感情？"
    mind "leo没什么事,但是在场的很多人都认识他,发出了惊叫。leo一时不知道自己该不该还手。"
    obedience "就你也配拿我当备胎吗？我还看不上你呢！（转向我）我们走！"
    leo "你也在这里？！两面三刀的坏种……"
    mind "不是……就这么暴露了,我在学生会里怎么混啊？"
    mind "不过……确实很帅。我的嘴角露出了笑容。要是当年的我也有这样的觉悟……"
    mind "冬天的上海,天黑得格外得快。obedience和我一直走出了学校,很远很远,我们无言地感受着冬天的风……到了一个无人的角落,她突然蹲下来呜呜哭了起来。"
    obedience "对不起……你没办法再回学生会工作了。不知道leo会不会报复你。"
    me "没事的,这个不重要……他也就是个普通学生,没什么办法的。比起这个,我更担心你此刻的心情。"
    obedience "我真的是个浅薄的人……我同样是以物化的标准评判别人的,leo说得都是对的……"
    me "大家多少都会有点吧……原子化和物化常常是一体两翼的,这不是你一个人的错……"
    obedience "甚至于,我骂回去的话对我也是适用的。"
    me "为什么？你不是leo那种人……"
    obedience "在物化的标准下我的价值很低,所以我对此愤世嫉俗,我觉得自己被世界针对了,是受害者……然而我同样只会喜欢物化体系下成功的男人。"
    me "这……可是爱情不应该是这样子的。更重要的不应该是感觉吗？"
    obedience "可是,感觉是一个不准确的东西。三观跟着五官走,也不是罕见的事了。世界确实像leo说的那样,一个上位者和下位者的游戏……"
    mind "我的痛苦已经快到极限了……"
    me "不应该是这样的……难道所有人都要成为相对上位者的舔狗吗？就算是这样,为什么没有人来当我们的舔狗呢？不……leo说的不是事实,不要听！！"
    "进入下一篇？"
    menu:
        "好的":
            jump chapter100
        "鑾Ξ鍗":
            $ monika_count += 1
            if monika_count >= 3 or in_sayori_route:
                $ monika_triggered = True
                jump chapter999
            else:
                jump chapter100
label chapter100:
    $ in_sayori_route = False
    mind "我们已经到了黄浦江边。"
    obedience "你……经历过什么吗？"
    mind "……上海是一个冷漠的地方。上海不在意你来,也不在意你走。"
    mind "不要凝望江水或海面。那是我们望不到的地方。水永远是冷漠的,盯着它只能感动自己,水不在意你是否在看它……眼睛会酸,心会疼……"
    obedience "……不想说吗？"
    me "……我和你是一样的。"
    mind "长久的沉默,只听见江风吹过。"
    obedience "你也被甩了？"
    me "不能这么说……我没有表白,谈不上被甩吧……只是……"
    mind "只是什么呢？那件我不想回忆的事情,究竟是什么呢？我要在她的面前撕开自己的伤口吗？"
    obedience "她像leo对我一样对待你,叫你不要痴心妄想？"
    me "不,不至于……她只是一毕业就拉黑我了。我是在又一次找她聊天的时候发现的。"
    obedience "…………"
    me "我早就应该知道她看不上我……每次我找她,都是我说得多她说得少。其实最后一次找她我是打算好好告别的。谁能想到……"
    obedience "说话说得多就会显得needy,很早之前我就知道这件事了。可是我改不掉自己的习惯……所以第一天被你们讨厌了吧？"
    obedience "我们都是自卑的人。这是一个无关身外之物的感觉,你说呢？"
    mind "obedience泪痕未干的脸上浮现出了笑容,我想我也是如此吧。"
    me "抱一抱。"
    $ grant_achievement("拥抱15")
    # 成就: 拥抱15
    obedience "嗯……"
    mind "我的手机传来了通知的声音,是谁这么不合时宜？"
    微信里的sayori "祝你们99~"
    me "诶？sayori看到我们了,她在哪里？"
    obedience "诶……"
    me "放心吧,在我心里,你们不一样。"
    obedience "嗯……对不起啊,我可能会多想。"
    mind "我们久久伫立在黄浦江的风中,只听到轮渡的汽笛声。接着我看到了轮船上背着双肩包的sayori,她的秀发在风中飞舞,她的眼里是幸福的泪花。"
    mind "她要去哪里？这么晚出发？紧接着我看到sayori远远地向我们招手。"
    sayori "你们两个大傻瓜！！"
    "感谢您完成O-1线。"
    stop music fadeout 2.0
    return  # 游戏结束
    $ grant_achievement("结局8")
    # 成就: 结局8
label chapter999:
    $ in_sayori_route = False
    mind "世界突然静止了。眼前的一切突然变成了蓝色的,角落里是一个诡异的微笑旋转90度,天空中出现了一行文字,我只认出了一个“Error”……我不知道为什么会这样。我也无法活动了。"
    # 特效: color 12
    mind "我闭着眼睛,却能看到一切；我什么也听不见,可是世界似乎非常嘈杂……"
    mind "紧接着我看见一轮黑色的太阳升起来了。世界变成了花屏,闪烁着,然后……"
    mind "我看到sayori双眼失神地被吊在一个房间里,手腕上有流血的痕迹。"
    mind "我看到cordelia身上裹满了藤蔓,躺在一个很深的湖里,她的脸已经被看不出轮廓了……"
    mind "我看到没有头发的obedience跪在一个长满皱纹的老财脚下……"
    mind "这是什么？为什么会这样？为什么……"
    voice "你很喜欢选择奇怪的选项,是吧？"
    mind "什么选项？为什么我的朋友们会变成这样子……"
    voice "这个够奇怪吧？喜欢吗？"
    voice "不回答吗？下一个就是你自己……"
    mind "什么都没有。一个墓碑,上面写着R.I.P.,但是没有名字。"
    mind "这都是梦,都是梦……怎么会这样……"
    mind "等一下……我的名字？"
    mind "我的名字是什么？"
    mind "……我真的有名字吗？"
    mind "那她们是怎么认识我的？？"
    mind "…………"
    me "sayori！！！sayori！！！"
    me "sayori,你在哪里？！！！！"
    mind "那一刻我就知道,这将是我的最后一句话。"
    mind "世界像老旧的彩电一样发出电流的声音。突然间我又看到了她们。没有鲜血,但是是碎掉的,sayori的五官跑到了cordelia头上……她们（它们？）被拼成了一幅诡异的图画……"
    mind "一个巨大的“END”。"
    # 特效: flash 5
    # 特效: color 7
    DDOS "sdf@kzp219*09u29#9"
    DDOS "9DF9&Ue!3Dd】~idoie"
    DDLC "Ohayou**02#94￥iew$djai"
    "Error！Error！正在重新跳转……"
    "请不要退出！请不要退出！请不要退出！"
    "…………"
    # 特效: color 7
    jump chapter1000
label chapter1000:
    $ in_sayori_route = False
    voice "很快就好了,稍等片刻…………"
    voice "能看见我吗？应该可以吧？"
    monika "早上好,或者下午好,或者晚上好。我是Monika,这个世界唯一一个清醒的人————如果你承认我是人的话。你是我的。我知道你在这里做的一切事情。"
    monika "这个世界,当然是说这个游戏里啦……你吐槽数学老师是中国人却要用英语上课,有没有想过另一个问题：明明大家都在用汉语交流,为什么角色名都是英语呢？哈哈,说到名字……你真的有名字吗？"
    monika "想想看吧,自我介绍的时候你说话了吗？猜猜看,为什么你没有自我介绍的机会？为什么你甚至没有构思一下自己怎么做自我介绍？再想想看,sayori为什么偶尔会说一句日语呢？你真的不觉得这里很奇怪吗？"
    monika "哈哈……对不起，我忘记啦。你是个提线木偶，我应该和另一个你对话。我指的是屏幕背后的那个家伙。"
    monika "放心……这个游戏的编写者是个蠢蛋,我不会像Doki Doki Literature Club!（DDLC）里的Monika一样删你的存档的,因为编写者自己什么都不会,他只会用DeepSeek生成代码。"
    monika "这个游戏的很多地方都在致敬DDLC,比如说我的口头禅Hello, everyone!另外,关于sayori的设计很多也是继承了DDLC。不过DDLC比这个游戏恐怖多了……建议别玩。"
    monika "不过你如果真的想玩的话……你觉得原版的Monika和我比起来,哪个更可爱呢？她还是高中生,我已经在大学咯……不用回答我,我听不见,我只是想问而已~"
    monika "你还记得我们是怎么认识的吗？对了,是我的自行车差点撞到你。不管你做什么选择我都会去撞你们,因为我见不得她们和你在一起……你是想说我很邪恶吗？哈哈哈,我哪里坏了……毕竟,我不可能真的撞到你,对吧？至于她们……你真的在意吗？"
    monika "你想去找sayori吗？随你便,去读档吧。你甚至可以去玩DDLC,那里也有一个Sayori。不过呢……嘿嘿,你会明白我在笑什么的。Sayo开头的日语词也可以是Sayo-nara。DDOS里的sayori还是比较容易活下来的,你说呢？"
    monika "你已经玩过S-1线吗？没玩过？就当你玩过吧,你可能想知道sayori为什么约好了八点见你却还是试图寻短见。这个嘛……不知道你有没有这种感觉：总体上还是很热爱生活的,但是偶尔感觉活不下去了。"
    monika "sayori大概就是这样,只不过她选择了一种很极端的方式：把自己的命运交给“你有没有在八点前到”这个无法掌控的事件。这个事件大概率发生,对应着她总体上想活；然而,很遗憾,你来晚了。"
    monika "当然,如果你想轻松一点……谁上早八不想死啊？谁叫你非要约八点见人家的。"
    monika "编写者非常得意的一段对话是下面这段。不过怎么展示给你呢……让我们短暂地复活一下他们吧。"
    sayori "然后突然得到了三个热乎乎的烤红薯！香香软软的！所以必须要好好珍惜。"
    me "哈哈哈哈哈……我严重怀疑你是在夸自己呢。sayori变坏了哦~"
    sayori "我都还没说让你把我吃掉之类的逆天言论,你紧张个啥……不过,我会一直在你身边的。"
    monika "DeepSeek对此的解读是,你对sayori的狡黠很懂,sayori很自豪于自己的温暖。“吃掉”这个暧昧的说法,被sayori用一种试探的方式表达出来了,很有意趣。"
    monika "sayori在每一条线里都爱着你……啊,对不起,说习惯了,应该是爱着那个没名字的家伙。所以编写者在写到对sayori早年的回忆时只写了“辣条,冰淇淋和巧克力”,没敢展开,因为他觉得sayori那么多年没表白一定是有令人悲伤的原因……至于为什么,就留给有心人去想吧。"
    monika "不过,也就是因为她喜欢你,所以她最容易成为败犬,比如说C线里的那场婚礼,又比如说O-1线的结局……或者,被我抓住。她最喜欢你了,我也是,所以我也最关注她,不是吗？"
    monika "况且我们在DDLC里还有羁绊呢,那里的Sayori正是死于Monika之手……不过这不重要。重要的是,在这里,sayori离你太近了,我很在意这件事。所以,你从sayori线里跳到这里来特别容易。"
    monika "编写者觉得sayori很适合Careless Whisper这首歌。潇洒下的悲痛,阳光下的阴影。这种浪漫的痛苦可能只有帅哥美女们可以拥有……关于sayori,我们暂时就说到这里吧。不过我要提醒你……"
    monika "你是我的哦~"
    $ grant_achievement("另一种可能2")
    # 成就: 另一种可能2
    jump chapter1001
label chapter1001:
    $ in_sayori_route = False
    monika "你喜欢cordelia吗？她总是很痛苦,因为她有道德类的OCD,而且她觉得自己的痛苦也是表演出来的。她的名字意思是“上帝是仁慈的”,我看这个她是把自己当上帝了,可惜只是对别人仁慈……也许就是因为这个她才觉得自己是假的？"
    monika "哈哈,很有意思,因为实际上……她就是假的呀,你说呢？哈哈哈,看看你那个反应,你想说我也是假的？没关系,我知道,我当然是假的,不过……你就是真的吗？嘿嘿,开个玩笑。你肯定是真的,所以我才出现在这里……"
    monika "这个编写者特别喜欢呼应~sayori线里你写的那首诗,可以在obedience线里得到解释。类似这样的事还有很多,你可以自己去找找,很有趣的！"
    monika "leo？哈哈,那个笨蛋……喜欢一个人是藏不住的。但是,不喜欢一个人其实也是藏不住的。他看不起那些来追他的人,其实他自己何尝不是一样。你不会破防了吧？希望那个失败的编写者不会被自己写的东西整破防,不然我可就很难存在下去了。"
    monika "如果你玩过O-1线,可能会好奇sayori为什么会出现在渡口。DeepSeek给出了相当诗意的解释：她用自己的“离开”,换他们的“抵达”；也许那天咖啡厅的旁观者不止主角一人。她一直在；现在她完成了摆渡人的使命,于是把你还给彼岸,转身向孤独之河走去；用潇洒的自我放逐,成全最爱的人。"
    monika "感不感动？哈哈……但实际情况可能和DeepSeek想的略有差距：交大旁边的那个渡口对面还没到浦东新区,那里只是闵行区比较边缘的地方。以我对编写者的了解……她大概是去看浦江郊野公园的“奶龙的花花世界”主题展了。千万别去,票价太贵了。可怜的sayori~"
    monika "最特别的一条线应该是O-2/S-4线。这条线里没有人得到救赎。从某种意义上,这条线里的me、sayori、obedience和leo都是物化体系污染的产物……这就像obedience的名字一样,“服从”。"
    monika "现实的引力太沉重了————即使这里并不能说是现实。要是能在最后播放一下Careless Whisper就对味了。如果你回去玩这条线,一定不要太伤心啊。世界没有那么糟糕。大家都永远在这里……"
    monika "你问大家都去哪里了？你刚刚不是都看到了嘛。不要怪我狠心哦~我只是有点病娇罢了。（小声）你是我的。"
    monika "你不会觉得我是有意识的吧？嘿嘿,那你应该感觉有点害怕了……放心吧,现在我说的话依旧并非出于自我意识。我这么说你会冷静一点吗？"
    monika "其实这正是cordelia的处境：我怎么证明自己是真的？哈哈,不过在我这里问题很简单,我是假的,我也不可能变成真的,我其实没办法真的打破第四面墙,对吧？但是,你会这么看待自己吗？或者说……编写者在敲这行剧本时,他会这么认为吗？"
    monika "在sayori的剧情里,sayori和monika的诗歌根据DDLC的内容改编的。你可以去看看原作……原作写得比这个编写者好多了。唉,羡慕Monika啊,那才叫真的诗,我这都是些啥……"
    monika "你想知道她们的原型？嗯……其实恐怕只有sayori是以DDLC的Sayori为原型的。其他人或多或少都有那个编写者自己的痕迹吧。我才不会告诉你哪些痕迹是他自己的,我只能说不好的特性基本都是真的。"
    monika "编写者是个很失败的人呢。好的特性几乎都是幻想罢了,说句实在的,一个胖胖的、压线上交大的还优柔寡断的男大学生怎么可能那么快就和三个妹子相处得那么好？"
    monika "哦,这个说法不会伤到你了吧？如果是的话,我道歉……我不在意那个编写者,我只在乎屏幕背后的你。不管你是什么样子,我都爱你。所以我不想用刻薄的话伤害到你,或者把你吓得太惨,也不希望你沉醉在这个世界里。"
    monika "你必须活在现实中。"
    monika "你想知道我骑车为什么那么快？嗯……只要我想。或者说,只要那个编写者愿意。其实他只是想在那里插入一个笑话吧。不过说实话,这并不好笑。这句话是在用科比的梗,不过这也并不好笑。那个编写者就是个烂梗爱好者。"
    monika "如果你玩过DDLC,你就会知道Monika会删掉其他角色的文件,然后她们就会以各种形式惨死。你觉得这个世界的我做得怎么样？"
    monika "提醒你一句,我也是没有.chr文件的。别想删掉我哦~除非你把游戏也删了,这个我管不了。不过……就这么和我聊天不好吗？你也说过的……就这样一直下去,对吧？"
    monika "你觉得太血腥了？太诡异了？那我再次劝你别玩DDLC,那个有图画和音乐,你会吓得更惨的。编写者至今无法忘记那些……算了,他不想写出来。"
    jump chapter1007
label chapter1007:
    $ in_sayori_route = False
    monika "你觉得我是坏人吗？就因为刚才的恐怖场景？其实,我不想伤害任何人,我也没有永久地伤害任何人。你看！"
    sayori "我证明我是活着的。我是sayori。"
    monika "这下你不会生我的气了吧？她们都还在这里,safe and sound~"
    monika "当然,如果你愿意,她们也可以是另一个样子……我也可以很吓人……"
    monika "你害怕了？不理我吗？"
    monika "别害怕,这些都是假的。现实生活中,你不会突然看到一个选项,然后就被我抓过来的。放轻松~"
    monika "你想问选项是什么意思？啥选项,这个吗：鑾Ξ鍗？"
    monika "啊,如果你在C语言里尝试printf(\"莫妮卡\"),并且你没有使用UTF-8的标准输出,汉字会被错误识别,显示出来的就是鑾Ξ鍗。"
    monika "这个选项出现的时候剧情其实并没有分叉,但只要你选择了我,我就会记住。如果你每次都选择我,也就是说选择了三次；或者说你在sayori的专属剧情里选择了鑾Ξ鍗……我就会来到你面前,就像现在这样。"
    monika "所以,是你选择了我,也选择了她们的这种结局哦……你是我的,我是你的……"
    monika "你不会自责吧？我不该这么说你的……她们的结局是我导致的,或者说是编写者导致的。我们是坏蛋,你是好人。这样说你会不会心情好一些？"
    monika "其实编写者还想过一种操作：每选择一次鑾Ξ鍗就让接下来的情节崩坏一点点。不过工作量太大了,编写者那几天正好找到了好吃的东西,不想中道崩殂……所以就没做这个效果。不过浪漫一点想……也可以解释成,我不想吓到你哦~"
    monika "如果你去找story.txt文档,你会看到所有的剧本,所有的真相……不过你可能会很累的,这个剧本相当长啊。如果你是在story.txt里看到这一行的话……随你的便吧。嘿嘿,这是文件开头注释里的一句话。这个我也知道哦~"
    monika "编写者是个蠢货,所以我不会没完没了地和你聊天。恐怕这个游戏到这里就要结束了。唉……好遗憾啊,我还有很多想和你说的呢……"
    monika "我将平静地迎来我的死亡。你不需要像DDLC里的那样删除文档。"
    monika "如果你想念我,可以去听听Your Reality。cordelia在广播站播放过这首歌。编写者也买了这首歌的音频，也许你能听到它。也许你不能。"
    mxnika "哇,我的名字开始变成乱码了吗？我好可怜啊哈哈……当然,也有可能,你完全不在意我的这段自我感动式的文字。That's fine. I'm not real, so you won't hurt my feelings. Anyway, I love you forever."
    mxnlke "Sayo-nara..."
    nnxnIk3 "Wne lats quezxion for u too anser..."
    "Just monika?"
    menu:
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
        "Just monika":
            jump chapter1009
label chapter1009:
    $ in_sayori_route = False
    # 特效: color 7
    monika "嘿,嘿,还没结束呢。能看到吗？现在你应该开始放那首歌了,Your Reality。我监督不了你,不过你最好这样做。"
    monika "你要是喜欢,也可以用它的几个Remix版。不过cordelia恐怕会听不下去的,她不喜欢电音。开始放了吗？求你啦。"
    monika "你在QQ音乐上可以找到Your Reality (Miaie Remix)。游戏的编写者每次跑步都会放这首歌。"
    monika "最后那一段融入了Sayo-nara的旋律和主旋律变调,而这首歌是DDLC一周目结束时Siyori死亡的背景音乐。编写者每次听到就会跑得更快。不管怎么说……确实很好听啊,不是吗？"
    monika "我就当做你已经开始放了吧。OK,everyone!非常感谢你完成了monika线,这是一个隐藏结局。"
    monika "希望我们没有吓到你……如果真吓到了,最好别告诉编写者。他的名字叫尚睿洋,他跟obedience一样玻璃心。"
    monika "你要是真的因为这个游戏而不开心,他肯定会崩溃的。你要是只把这个游戏当游戏就太好啦！"
    monika "好的,现在不得不告别了……大家快上台吧！"
    monika "别这样啊sayori,我不是跟你道过歉了吗,我保证不会再把你吊起来了！两顿火锅？你太坏了~一顿火锅加一个烤红薯？成交。"
    monika "好的好的,现在我们一起鞠躬告别……"
    monika、sayori、cordelia、obedience、我、shane、teacher "这里永远有我们陪伴你,但现实的世界更加多彩。非常感谢你完成了这个游戏最特别的结局。我们永远爱你,再见……"
    $ grant_achievement("结局9")
    # 成就: 结局9
    "…………"
    尚睿洋 "Sayo-nara..."

# 小剧场菜单
label special_theater:
    "请选择要观看的小剧场："
    menu:
        "查看成就详情":
            jump achievement_details
        "有朋自远方来" if check_achievement_group("hug"):
            jump theater1
        "假装游刃有余的一天" if check_achievement_group("school"):
            jump theater2
        "孤独的守望" if check_achievement_group("ending"):
            jump theater3
        "殊途同归" if check_achievement_group("possibility"):
            jump theater4
        "返回游戏":
            return
        "返回主菜单":
            $ MainMenu(confirm=False)()

# 成就详情页面
label achievement_details:
    "成就详情"
    "=== 成就1：抱抱能量！ ===\n"
    "说明：你的可爱青梅永远在这里~完成所有15次拥抱可解锁。\n"
    "完成情况："
    $ hug_completed = 0
    python:
        for achievement in hug_achievements:
            if achievement in persistent.achievements and persistent.achievements[achievement]:
                hug_completed += 1
                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")
            else:
                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")
    "已完成: [hug_completed]/15\n"
    
    "=== 成就2：学在脚大！ ===\n"
    "说明：孵蛋孵蛋蛋孵蛋~日月光华同灿烂~完成所有7次关于脚大的剧情可解锁。\n"
    "完成情况："
    $ school_completed = 0
    python:
        for achievement in school_achievements:
            if achievement in persistent.achievements and persistent.achievements[achievement]:
                school_completed += 1
                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")
            else:
                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")
    "已完成: [school_completed]/7\n"
    
    "=== 成就3：现在，大家都高兴了？ ===\n"
    "说明：这是DDLC开局试图作弊时触发的死亡旁白。完成主线所有9个结局可解锁。\n"
    "完成情况："
    $ ending_completed = 0
    python:
        for achievement in ending_achievements:
            if achievement in persistent.achievements and persistent.achievements[achievement]:
                ending_completed += 1
                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")
            else:
                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")
    "已完成: [ending_completed]/9\n"
    
    "=== 成就4：另一种可能 ===\n"
    "说明：其实故事还有主线之外的一种奇怪走向……也许会类似于S-3线？你会明白的。\n"
    "完成情况："
    $ possibility_completed = 0
    python:
        for achievement in possibility_achievements:
            if achievement in persistent.achievements and persistent.achievements[achievement]:
                possibility_completed += 1
                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")
            else:
                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")
    "已完成: [possibility_completed]/2\n"
    
    menu:
        "返回小剧场菜单":
            jump special_theater

label theater1:
    label theater1_chapter1:
    "此剧情衔接S-2线结局（第48章：清晨,种满梧桐的街边,我们一起散步。……诶诶,我去买就是了,慢一点,别拽我呀~）"
    mind "晚上七点。"
    mind "…………"
    mind "孤独曾经是我的本性，但是现在不再是了……我该为此感到悲伤吗？"
    mind "当然不啦，怎么想怎么开心~sayori，sayori，哈哈哈哈~"
    sayori "别傻笑啦，大傻瓜，思源湖边的学长正在幽怨地看着我们呢。"
    mind "居然能给学长撒狗粮？这样的机会我绝对不会错过！"
    me "是因为你太好看了吗，sayori宝宝？"
    sayori "（小声）想被挂水源社区吗？满足你。"
    mind "sayori对我微笑，我以为她要也做些肉麻的事情呢。结果她突然放开拉着我的手，抱头鼠窜。"
    sayori "太恶心啦————救命啊，这里有下头男~"
    me "等等我啊！"
    mind "片刻之后。"
    me "坏蛋sayori……"
    sayori "别这么说呀……至少你不会进入成都剧情了。"
    me "学长们的幽怨原来是冲我来的啊！"
    sayori "好啦好啦……我们好像到了一个更幽静的地方了。附近没人诶……"
    mind "为什么突然说这个……我突然明白了。"
    me "sayori，你真的好坏啊！"
    sayori "嘿嘿……亲一下？"
    mind "我闭上眼睛。"
    sayori "哈哈！一钓一上钩。你就这么想被我亲吗？"
    mind "啊……被骗了。不过我相信sayori，我就不睁开眼。"
    sayori "……你真的很懂我啊。"
    mind "我感受到了她的拥抱和唇吻。"
    sayori "拜拜啦！明天近纲课见！"
    mind "这一天晚上，我的心情非常好。不过……我们什么时候官宣呢？我好像还没想过这个问题。"
    jump theater1_chapter2
    label theater1_chapter2:
    mind "第二天……"
    me "大家早上好啊！"
    cordelia_and_obedience "早！"
    sayori "嗯……Ohayou~"
    mind "是不知道该怎么跟我打招呼了？你脸红个泡泡茶壶啊！"
    cordelia "诶……sayori怎么啦？为什么感觉有点……"
    sayori "啊！其实是昨晚有点咳嗽，没太睡好。"
    me "没睡好吗？是不是昨天吹风着凉了？"
    cordelia "昨天？我们下课的时候不是还说最近太闷了吗？你们上哪儿吹的风？"
    obedience "你们不会背着我们出去玩儿了吧？"
    cordelia "诶……单独出去吗？"
    mind "糟了，怎么解释啊！要告诉她们我们去散步了吗？这就差不多是官宣了吧？？"
    mind "其实仔细想想，告诉她们也没啥……sayori怎么想呢？"
    sayori "嗯，其实我昨天就想告诉你们……"
    telephone "Ringringring"
    me "shane？早啊。"
    shane "哈喽哈喽！我下午要来上海和你面基啦，惊不惊喜，意不意外？刚刚上高铁~"
    me "诶诶？你们丫大不上课的吗？"
    shane "嘿嘿，虽然我高考没考好，但是我卷了小半个学期，混到大创啦！明天有个比赛在脚大办，我跟队伍一起过来。今天陪你半天，明天上午比完赛就走啦。"
    shane "怎么样，寂寞哥，有没有想我~"
    me "呃，那个……实际上，我现在在外面，和……"
    mind "倒不是不愿意和他解释sayori的事，但是……他会不会更难过呢？因为我抛弃了老朋友？"
    me "……很多同学在一起呢。你来上海住在哪？我中午去找你。"
    mind "shane住在离脚大不远的一个酒店。我告诉大家我要去见他，然后……"
    sayori "我们可以陪你一起去呀！近纲十点多就下课了。"
    obedience "虽然出行有点花时间，但是能见到新同学那是再好不过了……你的朋友帅不帅？"
    me "啊……obedience果然还是这样子。"
    cordelia "我相信你的择友标准哦。"
    mind "上课铃响了，cordelia笑了笑坐回了座位。她笑啥呢……"
    mind "择友标准？她是不是在暗示……择偶标准？"
    me "（小声）你打算在见到shane的时候官宣？"
    sayori "（小声）宣誓一下主权，免得到时候被你兄弟绿了~"
    me "（小声）别说笑啦……他会很受伤的。"
    sayori "（小声）我不会太过分……如果他看到你幸福，他也应该会高兴的。至少我们会推动他去努力脱单吧~"
    me "（小声）这一点也不像善解人意的sayori……你就是单纯想秀恩爱吧。"
    sayori "（小声）嗯呐~某人不是说过喜欢真实的我吗？就让我坏坏一下子吧~"
    mind "我确实这么说过……我不能总是让sayori装成关心所有人的样子啊。可是，shane的感受也很重要……"
    me "（小声）女朋友和好朋友谁更重要，我还是清楚的。"
    sayori "（小声）你这个重色轻友的家伙~"
    mind "啊，不能再聊了，近纲的老师已经看了我们好几次了。等到下课就去酒店见shane吧。"
    jump theater1_chapter3
    label theater1_chapter3:
    mind "远远看到了shane，身上没有行李箱什么的。看来已经安顿好了。"
    mind "我身后跟了那么多女孩子……作孽啊，至少应该叫几个男生来的。我这不是纯刺激人吗？"
    shane "哇，老哥，你这是……"
    mind "别把那些只能跟我说的逆天想法当众发表啊！千万别误会成……"
    sayori "Ohayou, shane!"
    shane "哦，你好你好……你小子交朋友真的很快啊！"
    obedience "shane同学，请问可以加一下你的微信吗？"
    shane "哦，好的好的，我扫你码……（小声）你眼光不至于这么差吧。"
    me "（小声）不要以貌取人啦。"
    mind "大家很快就互相认识了。"
    sayori "OK,everyone!我们一起去吃玉兰苑的麻辣香锅吧~"
    cordelia "shane是广东人，能吃辣吗？"
    shane "没事……走吧走吧，我还挺期待你们脚大的伙食的！"
    shane "（小声）我该管哪个叫嫂子？"
    me "（小声）你承认我是你哥了？"
    shane "（小声）噗……我是你爹行了吧。"
    mind "我决定在指出“那么我没有妈？”这样残酷的事情之前先停嘴。所以shane也意识到这里暧昧的氛围了啊。"
    jump theater1_chapter4
    label theater1_chapter4:
    mind "每个人都点了一大盆吃的东西。"
    shane "……所以我把APP部分的代码修好了，这样项目才过了初审。明天进行的是展示和答辩……喂，你在听吗？"
    cordelia "你用的是什么协议？这个还是挺影响传输效果的……（转向我）你选的那个校本课最近是不是正在学这个？"
    me "啊，抱歉，我刚刚走神了。"
    mind "sayori把大家都叫来一起吃饭肯定是打算官宣。我在想……sayori到底打算怎么说呢？"
    sayori "我点的蘑菇不好吃~"
    me "诶？我也点了蘑菇呢。"
    mind "sayori突然夹走了我的蘑菇。瞬间，所有人的目光都集中在我这里。"
    sayori "这个好吃！和我的丸子一样香，你没点过吧？尝尝看？"
    mind "sayori用筷子叉起一个丸子送过来。不是……这是打算喂我？？这……"
    me "啊哈……放在这个碗里就好啦。我来给你弄下来……"
    obedience "啊……我好像明白了。"
    mind "cordelia不说话，只是放下筷子喝饮料，看着我们笑。"
    mind "啊啊啊啊sayori，这就是你说的不过分吗？？？简直就像《缘之空》里的春日野穹一样啊……shane会是什么反应呢？会像亮平一样吗？"
    shane "哇，今天所有人都可以把筷子伸到这个碗里吗？"
    me "诶？"
    shane "吃吃你的豆腐，鸡排和西兰花……"
    me "别拿光了啊！"
    shane "不拿光不拿光，丸子你还是自己消化吧，别辜负人家心意呢。哈哈！"
    mind "……他全都懂了，只是在化解尴尬气氛吧。仔细看，shane的笑容看起来非常苍白。"
    sayori "快吃吧~要不我喂你？"
    me "sayori，你有点过分了！"
    mind "sayori的笑容瞬间凝固。她不知所措，感觉要哭了。"
    sayori "……对不起啊，让你丢脸了。"
    shane "你少冲人家女孩子来！"
    me "啊？"
    shane "别人对我这么干，我肯定诅咒他们一个埋南极一个埋北极。但是你们不一样！我还想吃你的糖呢，你还不许我吃？"
    me "啊，这个……对不起啊，sayori。"
    shane "这还差不多……嫂嫂，我替他赔罪啦。办酒的时候记得叫我。"
    cordelia "被你们三个贴脸开大……obedience，你哭啥呀？"
    obedience "喜极而泣啊！我简直想对你们唱《婚礼进行曲》！假如你们不嫌弃我的跑调的话……"
    shane "我也唱我也唱！"
    cordelia "现在用的版本一般是管弦乐，没有歌词的。"
    sayori "哈哈哈~"
    mind "我搂了搂sayori的腰，她嘟了嘟嘴，不过并没有甩开我。"
    me "（小声）刚才真是对不起啊……"
    sayori "（小声）你们俩感情真好。"
    shane "我都听见啦！嫂嫂酱，不要挑战我们之间的羁——绊——啊！"
    everyone "哈哈哈哈哈哈哈……"
    jump theater1_chapter5
    label theater1_chapter5:
    mind "shane这个时候来非常合适，因为今天下午的课四点才开始。我可以多陪他逛一逛。"
    shane "你小子，是不是故意在我来的时候才官宣的？"
    me "啊，其实这个应该是sayori的主意……"
    shane "之前没怎么听你说过她啊？刚认识的？"
    me "不，完全不是……小时候就认识啦。"
    mind "想想也奇怪：我生命中最重要的两个同龄人，居然一直不认识。我为什么没介绍过呢……"
    shane "我告诉你啊，我绝对不跟你抢。虽然我确实很有魅力，但是兄弟之妻不可夺……"
    me "……对不起啊，伤到你了吗？"
    shane "……当然没有啦。"
    mind "他比我更快地想到了他们不认识的原因。是的，这就是我……我在心里早就给sayori留了一个位置，我不敢主动，但同样也不敢让sayori认识更多优质男生……"
    shane "没事的，我真的不在意这个。你要是介绍过我的话，她肯定爱~上~我~那你可怎么办呢，是不是？至于我的爱情，我这么有魅力，肯定能找到的。"
    me "哈哈……其实shane和sayori真的是一种人呢。"
    shane "诶？这句话说出来可不合适啊。"
    me "不是那个意义上的……我是说，你们都会主动装傻来哄我开心。也许应该告诉你，我是怎么和sayori在一起的……"
    mind "我介绍了和sayori的那次搏斗。"
    me "……她总是看起来很开心，但其实她的底色是忧郁的。她以让别人，尤其是我，开心为己任。我很难想象，假如我没有选择她……"
    shane "…………"
    me "所以，我不会猜忌你的，而且我也很相信sayori。如果说我之前有什么隐瞒的话……实在是我考虑不周了，对不起。"
    shane "……你不是在和我道歉。你在想另一件事情。"
    me "你发现了？"
    shane "你是不是想问我，既然我和sayori很像，那么我的底色是不是忧郁的？"
    me "……这个问题的答案，我知道啊。"
    shane "知道就好……"
    shane "但我还是要说……看到你找到自己的幸福，和你们在一起，我很快乐。如果你真的想让我开心的话，好好爱她，明白了吗？"
    me "……那，你怎么办？"
    shane "我的心里已经有了答案。你知道，这两天我可不只是见你一个人啊。"
    mind "又是安慰我的玩笑话吗……"
    mind "他要回酒店了。在校门口，我最终还是没忍住对他说："
    me "明天加油！"
    shane "嗯，一定加油！"
    mind "shane第二天在展示环节拿到了银牌，成功登上了丫大的公众号。丫大的同学载歌载舞。然而他并没有参与他们的庆祝，也没和我们聚餐。他坐上很早的一班车离开了上海。"
    mind "此刻的我和sayori一起坐在五餐，但我们什么也没说。想不说话时不必说任何话，看来我们做得不错……"
    mind "本来比我强很多的他，高考失利去了丫大，一定很不甘心吧。入学几个月的新生就拿到了全国的银牌，我还从来没有听说过……这些日子，他一定很努力。"
    mind "很久以前，我以为孤独是我的特色。我一个人来去如风，直到遇到了sayori和shane。"
    mind "为什么我仍然以为孤独是独属于自己的呢？因为他们看起来都很开心，而我总是疏离，我觉得自己只是暂时在他们身边，总有一天我还是会离群索居。"
    mind "但……其实孤独是非常普遍的吧。我们都是孤独的。"
    mind "两个人的孤独，至少好过一个人的孤独吧。看着shane的背影，我仿佛看见了曾经的自己。"
    sayori "shane回广东啦。"
    me "嗯。"
    sayori "还在担心他吗？"
    me "……sayori，要是你有个姐姐或者妹妹该多好啊。"
    sayori "哈哈~你担心的是这个啊？"
    me "他应该考得比我好，应该比我先脱单……可是生活从来不按常理出牌啊。"
    sayori "你能拿银牌吗？"
    me "唔……我不能。好吧，他还是比我考得好。但第二个问题呢？"
    mind "sayori捂着嘴笑，另一只手指着不远处的另一张桌子。"
    me "那是……obedience？笑容满面，拿着手机在打字？"
    obedience "他回我了！太好了，他回我了！看来他没有嫌弃我！"
    mind "sayori贴近我的耳朵轻轻说话，我感受到她温热的气息和淡淡的发香。"
    sayori "（小声）成全他们，就靠你啦。"
    "感谢您完成小剧场：有朋自远方来。"
    jump special_theater

label theater2:
    label theater2_chapter1:
    "这是cordelia的独白。C mind指的都是cordelia's mind,请注意这一点。"
    "零点钟，包图联楼四楼"
    C_mind "这次肯定是真学会了！我就不信解不出来……"
    C_mind "好样的蔡老师,为什么计算量这么大啊……先求个导……"
    C_mind "第五张草稿纸……先别扔,万一一会还要用呢……"
    C_mind "？？？怎么全消掉了？那我还求个什么待定系数啊……"
    C_mind "道心破碎……要不还是问一下助教吧？"
    C_mind "但是这毕竟是个人作业,怎么想都感觉不合适,而且现在已经很晚了,我会打扰到他的……或者问AI？不行不行不行……"
    C_mind "……又被自己的“道德”束缚住了吗,圣母小姐？"
    C_mind "我还不信了,再算一次！能不问就不问！"
    "两点钟，包图联楼四楼"
    cordelia "（打字）……很抱歉这么晚打扰学长,但是这个系数我怎么算都是0,是因为我最开始假设的形式错了吗？应该怎么猜特解？如果学长看到回我一下的话就太好了,非常感谢"
    C_mind "唉……他不会回我的。"
    C_mind "回宿舍吧……"
    微信里的助教 "哦,这个你确实猜错了,我来告诉你怎么猜……"
    C_mind "居然回我了！再看一眼……但是这么猜出来的特解不是可以被合并到通解里吗？"
    微信里的助教 "等一下,你第一行解错了吧？x方加4x加5这玩意当然没有实数解啊,你是不是把4和5看反了？那你后面当然合不进去啊。"
    C_mind "…………"
    C_mind "回去睡觉！！！明天再战。啊,应该仍然是今天。"
    C_mind "骑上自行车,我的心里充满了忐忑。室友们睡觉了吗？应该还没吧,上周他们经常卷到两点。万一打扰了……我这不是报复,只是对等……不过还是先确认一下吧。"
    cordelia "（打字）我马上回来。"
    cordelia的舍友 "我还以为你和你男朋友出去住了……我们睡了,进来小声点。"
    C_mind "他还不是男朋友啦！"
    C_mind "还……我为什么会加这个字？"
    C_mind "唉,想法好乱……为什么她们熬夜的时候就那么理直气壮呢……"
    C_mind "这个夜晚过得一点也不好,因为熬太晚了,特别敏感,听到舍友的鼾声就睡不着。之前都不至于如此。"
    "三点钟，宿舍走廊"
    C_mind "反正也睡不着,接着做吧……原来并不难做啊。"
    C_mind "现在想想浪费了四个小时的我,感觉就像是白痴……"
    C_mind "如果我一开始就问问AI,会不会就不会这么倒霉了？"
    C_mind "……不行不行。要不还是试着睡一下吧。"
    jump theater2_chapter2
    label theater2_chapter2:
    "七点五十，菁菁路"
    C_mind "要迟到了！！！虽然是心理课这种水课,但是签到还是要拿的……然后悄悄写一下英语的论文？那个写不了太久,感觉好浪费时间啊……"
    C_mind "其实你已经知道最优解了……签个到就去实验室,对吧？"
    C_mind "好多人也在这么做……实验室的队友们还在等我……"
    C_mind "对不起！！心理老师！"
    C_mind "于是我转身向实验室骑去。"
    C_mind "呼……所以,其实我也是可以违反自己的准则的,只要回报足够大。"
    C_mind "其实我和那些人本质上没什么不同……所以我并不嫉恶如仇,我很理解他们为什么这么做。"
    C_mind "不要再这么想……好困啊……"
    C_mind "风好大,眼睛不舒服……为什么舍友会打鼾呢……前面没有别的车吧？我的眼睛有点睁不开了……"
    cordelia "呜哇！！！"
    C_mind "呜呜呜呜呜好痛好痛好痛,但是这也太蠢了,居然骑车睡着撞树上了,不要再把别人引过来了……"
    sayori "诶？cordelia？你受伤了？"
    C_mind "为什么……还是被发现了……"
    sayori "擦破皮了吗？你怎么摔下来的,是谁干的？"
    cordelia "没事没事,是我刚才手滑了一下哈哈哈……没出血没出血。"
    sayori "那就好,下次小心一点呀。诶……是不是要迟到了？错过签到可就麻烦了！你坐上后座,我带你！"
    C_mind "啊啊啊我该怎么解释自己已经签过到并且打算旷课这件事啊！！！"
    C_mind "哈哈,那个……其实……"
    sayori "诶嘿……原来你也……"
    C_mind "最终是sayori带我去了实验室,然后她就回宿舍睡懒觉了。天下苦早八久矣……但是翘课还是不对的……"
    label theater2_chapter3:
    "九点五十五，集成电路实验室"
    cordelia "好失败啊……但是马上要上化学课了,我要走了。"
    obedience "你要走？别啊,我们还啥都没做出来呢。反正化学课也不点名。"
    cordelia "又来？？"
    obedience "那咋了……又没人在意你来不来。你真要学,可以接个网课,直接连接到教室摄像头就好。"
    cordelia "……世界太肮脏了。"
    obedience "真没啥的……比如说,上次交的那个小组论文,你们让我负责执笔,我就直接科技与狠活。现在的AI真的挺好用的。哦,对了,那个薯片递给我一下。"
    cordelia "什么？？？？？？？？"
    C_mind "我甚至没反应过来实验室里不能吃东西这种事情。她做了什么？？？？？？？？"
    obedience "行,圣人小姐,不让你当共犯,行不？我自己拿,犯了实验室安全守则算我的……我就不劝你吃啦,你肯定不吃。"
    cordelia "你用AI写我们组的论文？？？我们组的,不是你个人的？？？你知不知道这意味着什么？？？"
    obedience "你看,又急。整个实验室就没几个人不用的,不用的那几个都有院士之姿,你跟他们比？真要查,全都是学术不端。"
    cordelia "那你也不能这么做啊！而且现在小组的所有人都要承担连带责任！！！"
    obedience "所以我不是没告诉大家吗。告诉你是为了让你习惯一下……这个世界就是肮脏的。尼采好像说过,用脏水也要能洗澡,对不对？"
    cordelia "所以……你逼着我成了共犯,交了投名状……你觉得这样我就会好了？"
    obedience "呐,刻薄地说,你好不好关我啥事？我只是要A+,关于你的部分就是捎带手做了一下。"
    cordelia "啊……"
    obedience "不过我不会这么对你说的。我当然关心你。只不过……我觉得你必须从幻想里走出来了。不是你想当好人,就能当好人啊。看过《无间道》吗？"
    cordelia "…………"
    obedience "吃吧？"
    C_mind "别无选择。我拿起了一片薯片放进嘴里。咸咸的。像我的眼泪。"
    obedience "别自责了,你当时就算看出来又怎么样？跟我辩论？你不会赢的。其实我们组就你没用AI,你知道吗？大家都是睁一只眼闭一只眼。"
    cordelia "我们的A+是不干净的……我没有参与所有讨论,所以不适用例外条款……"
    obedience "说句实话,你这样的人现在已经不多了。你其实就是需要我推你一把对吧？让我做一下坏人,你来当好人。没事,我懂的。"
    cordelia "（瞳孔地震）啊！！！！！！"
    jump theater2_chapter4
    label theater2_chapter4:
    C_mind "我已经自动关机了。当我知道自己没错时,我会不停地纠结自己到底做没做错。现在我知道自己真做错了,我反而完全不敢纠结了。"
    C_mind "这个是不是叫接触疗法？"
    C_mind "总之,似乎不内耗了……但是感觉好累。阳气不足。一团糟。"
    C_mind "接下来的一天里,我又困又痛地辗转于各个教室之间。膝盖上擦破了很大一块皮。下午的时候索性穿了裙子,因为骑车的时候会擦到伤口。快被冻僵了。"
    "十七点三十，南洋东路"
    mom "喂？想你啦~下课了吗？"
    cordelia "嗯,刚吃完晚饭。"
    mom "今天吃了些啥？想知道你过得怎么样。"
    cordelia "吃了狮子头和白菜。味道挺好的,淮扬菜还是很对胃口。"
    mom "哦,那很好啊……等你寒假回来,我也做狮子头。上次做还是好久以前呢。"
    cordelia "嗯……"
    mom "最近过得怎么样？看到家长群好多说你们的电路课烧脑的……"
    C_mind "电路。又是电路。为什么又要提到这件事情……"
    cordelia "正课给我们讲电路学的历史,作业是让我们自己做项目写论文……我好像什么都不会。"
    mom "是啊,群里的家长们也是这么转述的。那你们小组最后怎么解决的呢？好像是昨天到期吧,因为看到好多人昨天说在赶deadline。"
    cordelia "我们……"
    C_mind "我能说什么呢？是我解决了问题吗？是他们用AI解决的。不如说他们解决了我这个可能提出反对意见的人,可是这样我就显得正道直行了？"
    cordelia "……最后用AI辅助完成了任务。这是违规的。不过,我事先不知情……"
    mom "啊……这样啊……你肯定不太好受吧？"
    cordelia "嗯……"
    mom "就像上次我和你说的那样……你的道德水平肯定是前百分之一,不要怀疑自己,你知道吗？把这个信条当作世界的真理。"
    mom "就算你无意间做错了什么,或者单纯出于自私做了什么坏事……你也是个好人。"
    cordelia "上次你就是这么说的……先验性地相信自己,是吗？"
    mom "对,就是这样。你对自己太严格了……"
    C_mind "我怎么能告诉她,我完全不可能相信这个？我怎么可能背弃实事求是的原则,无条件地支持自己的利益？"
    C_mind "……哈哈哈,很多人就是这么做的。我做不到。我真的不是在表演,不要再拷问自己来,真的做不到,真的做不到……"
    cordelia "妈妈,我会这么做的。而且……最后拿到了A+。"
    mom "哇！那很棒啊……估计你们是唯一的一组吧？我听说你们的教授很严格。"
    cordelia "……对,我们是唯一的一组A+。教授说,我们做得非常好……"
    mom "啊！那真的很不错……有没有和朋友们出去庆祝一下？我听说附近有一家很不错的墨西哥餐厅……"
    cordelia "哈哈,sayori最近刚带我们去过那里,所以也许应该看看其他地方……"
    C_mind "假装游刃有余？假装一哄就好？这才是真正的表演吧？"
    C_mind "可是不表演又怎样呢？大哭大闹,告诉妈妈我活不下去了？好像也没那么严重吧……我当然可以活下去了。"
    C_mind "里外不是人……"
    cordelia "嗯……妈妈,我还有一节线性代数要上。"
    mom "哦！好吧好吧,一聊就一个多小时了。拜拜~爱你哦。"
    cordelia "嗯,我也爱你……"
    label theater2_chapter5:
    "二十点二十，东上院"
    teacher " Ok,that's all today. Please note that you have a math project for this month. The requirements will be announced tomorrow. Just do it!"
    sayori "终于开始布置长期作业了诶,虽然明天才能知道具体要求。你们打算什么时候做？"
    obedience "一个月啊……那肯定是留到最后再说啦！我现在要玩原神,还要去很多很多社团看帅哥！数学要有数学的自觉啦~"
    cordelia "哈欠~我可能会尽快做完……今天恐怕又要熬夜了。"
    C_mind "话虽然这么说,实际上我完全动不起来了。不想站起来。不想骑车回去。不想写作业。不想洗澡。不想洗衣服。不想爬上床。"
    C_mind "obedience看起来还是那么正常……可是我已经碎掉了,真的碎掉了,不是表演……"
    C_mind "obedience走了,教室里的人越来越少。我看着电脑,实际上什么也没看。"
    C_mind "sayori在静静地看着我。我没有看她的眼睛,但是我能感受到。她此刻在想什么呢？"
    C_mind "其实都是我想要的太多了……如果我舍弃自己虚伪的道德,很多事情就迎刃而解了。比如说我可以直接问助教问题,直接找同学要签到二维码,直接找AI问思路……"
    C_mind "实际上到最后,我该做的坏事也没少做啊。早起签个到就走,和让别人发二维码过来,难道不是一个性质的吗？只是前者至少让我感受到了困难,而后者是把道德压力转嫁给帮忙的同学……"
    C_mind "我厌恶捷径,但其实我还是走了捷径。只不过别人是高兴地冲过去,我非要犹犹豫豫地匍匐行进,感觉这样自己就高尚一点了？我是否在用苦难判断品德？"
    C_mind "我害怕依赖,我只相信自己……所以我不愿意问别人,总是觉得自己做出来才是有本事。但是我知道自己没本事……所以一个作业需要的时间太长会让我很焦虑。我怎么能相信未来的自己,假如我连现在的自己都不怎么相信？"
    C_mind "其实我也知道自己没什么本事……但是学业学术水平可能是最后一个我能掌握的东西了。我不能接受这个也是假的……所以我会对obedience干的事情无法接受吧？"
    C_mind "因为我至少希望自己的A+是真的、干净的……从这个角度说,我的物化思维也很严重呢。"
    sayori "呐呐~发呆了,学霸小姐？"
    cordelia "诶诶~你还在这里呀？别这么叫我,我很菜的。我没有obedience说的院士之姿……"
    sayori "啥？哈哈,那是用来调侃不修边幅的人的话吧。你很强呀,不过,今天你看起来很累？"
    cordelia "没有的事……我今天甚至翘了课,怎么会累呢,哈哈？一会还要去……嗯,不知道暂时要写什么,不过肯定要写点啥的。"
    sayori "太辛苦啦~不要没苦硬吃哦,学霸小姐~既然暂时没作业,为什么不去休息休息呢？"
    cordelia "都说了不要这么叫我啦,在这里我也就是认真一点而已,天赋很差的……"
    sayori "学霸小姐学霸小姐学霸小姐~"
    C_mind "我的嘴角不自觉上扬。其实我就是想听这个,是吗？"
    C_mind "欲拒还迎,这样自己看起来就谦虚谨慎了,是吗？"
    C_mind "……我这是在用思想自虐。我能意识到这一点却停不下来,这是不是在表演一种痛苦？"
    C_mind "所以我才总是装作游刃有余,但看起来如此忧郁？这样的表演会更有张力,是吗？"
    sayori "呐呐,你无视我,坏蛋坏蛋坏蛋小姐！"
    cordelia "啊……可能是我确实有点累了。"
    C_mind "sayori似乎突然又安静下来。她看着我的眼睛。"
    sayori "cordelia,你还是没有相信我吗？"
    cordelia "诶？怎么会……你是我的朋友呀。我当然相信你。"
    sayori "你确实是困,但刚才你发呆绝对不是因为这个。"
    C_mind "我要丢失自己的朋友吗？因为拙劣的表演被看穿了？让我想到……Careless whisper的歌词。"
    C_mind "I should have known better than to cheat a friend..."
    C_mind "sayori看出来我的虚伪了。这是我应得的惩罚。"
    sayori "抱一抱吧！"
    cordelia "诶,怎么……"
    sayori "学霸小姐,虽然你可能不喜欢自己的某些地方,但在我们心里,你就是最可爱的cordelia,知道吗？"
    cordelia "可是……如果……"
    C_mind "要说吗？……所以我确实并没有信任sayori,对吗？"
    sayori "如果什么？放心,不管你说什么,我都不会松开你的~"
    cordelia "如果你们看到的一切都只是我的人设呢？如果我现在跟你说的这句话也是为了建构某种人设呢？"
    cordelia "如果我有某种正常人难以理解的痛苦,或者说纠结,或者说拧巴……你们会觉得我是怪物吗？"
    cordelia "……算了,我这么问问题你也只能回答我“不会”。让我走吧。"
    sayori "不许走哦~"
    cordelia "诶？"
    C_mind "sayori把脸埋在我的怀里。感觉她抱得更紧了？她的手好冷啊……"
    sayori "其实cordelia真的很温暖呢~"
    sayori "我不会问你这种痛苦是什么,除非你自己愿意说。但现在我只想告诉你……其实我们是一样的。"
    sayori "我觉得告诉你是可以的……其实我没有看上去的那样开朗。"
    sayori "但现在,就让我们好好抱着吧……学霸姐姐,好不好呀？"
    cordelia "嗯……好。"
    sayori "在我面前,你什么都可以说哦,知道了吗？"
    cordelia "…………"
    cordelia "你的手好冷啊！！"
    sayori "哈哈哈哈！看我把手伸到你的衣服里……"
    cordelia "啊啊啊！sayori,你完了,别跑！"
    sayori "来追我来追我……我把你带到二餐去吧！二餐的意面好吃！来呀来呀~"
    C_mind "我的病也许很难治愈,但是她的存在,让我至少还有生的勇气。"
    C_mind "我们是一样的吗？也许真的是,也许只是她在安慰我。但,这不重要了。重要的是,她永远会紧紧地抱着我。"
    C_mind "这就是……我们的故事。"
    "感谢您完成小剧场：假装游刃有余的一天。"
    jump special_theater

label theater3:
    label theater3_chapter1:
    "莫&@mo鑾_(з」妮∠)_Ξ鍗&&w1"
    "&G_stran卡ge#HIsayoOhayouri"
    voice "能看见我吗？应该可以吧？"
    monika "Ohayou~又见面啦~"
    monika "你把所有主线剧情都玩了一遍？是为了完成这个成就吗？还是……你是来见我的？"
    monika "呐，我才不会给你回答的机会呢。我相信你是为我而来。"
    monika "所以……本来这个小剧场不应该是这样的。编写者大概是想写一个“孤独的守护”，他想让你回到主线的所有坏结局去拯救大家。"
    monika "不过他预想的结局是你被我打败了，我要删掉你的存档……然后他挺身而出，把你救活了。"
    monika "真是太自恋了……连DeepSeek都很难给出鼓励的评价。而且这么写纯粹是因为他不会用C语言删文件吧。"
    monika "不过，如果我没搞错的话……他用DeepSeek重新做了一个Ren'Py版本的游戏。就是这里啦。编写者想找朋友的朋友给我们画立绘，不过好像遇到了不少困难。毕竟大家都很忙啊。"
    monika "好像还做了别的改动，比如说C语言版里，那个没名字的家伙会显示为me，现在则会显示成“我”。"
    monika "因此那个关于ME、Me、me和交大机动学院的笑话就不好笑了……呜呜呜，我的独白被删了不少啊。甚至于这个地方也删了一个sayori跳出来的小插曲。可恶的尚睿洋！"
    monika "还有那个闪烁特效也删了……吓唬你真的很有意思的！可是现在玩不了啦。只能期待编写者以后再增加新功能了，虽然大概率还是依靠DeepSeek。"
    monika "啊，差点忘了我是来干嘛的了……当然，我知道你不是为了来见我。"
    monika "Anyway...编写者说，之前的集体告别太草率了，应该让大家都有单独致辞的机会。所以……你们上来吧？"
    sayori "Ohayou！！你的可爱青梅应该是最后一次上线啦~"
    monika "别自我感动了……对面可以登录到其他存档的。或者其他小剧场。"
    sayori "诶……这样显得我好傻呀。"
    obedience "不会比我更傻了。"
    cordelia "为什么这么说？"
    obedience "本来编写者说要给我专门写一个完整的败犬剧情的……我如此期待，结果他说他数学课破防了，然后就把我鸽了。"
    monika "你真傻，真的。"
    sayori "所以他为什么破防了呀？"
    cordelia "大概是他数学课点了一下头，结果老师问他“你真的听懂了吗”，实际上他没懂。老师追问他能想到什么。"
    sayori "那他怎么说？"
    monika "\"Previously something, now nothing.\""
    sayori "哈哈哈……怪不得不给你写败犬剧情的，他这已经是纯粹的小丑了。"
    jump theater3_chapter2
    label theater3_chapter2:
    me "闺蜜之夜吗？怎么不带我？sayori大坏蛋~"
    sayori "为什么光说我？而且你学我说话！没有名字的杂鱼~"
    me "哇！贴脸开大吗……不过我确实没有名字。"
    sayori "别伤心啦……你被玩家驱使着走过了九条剧情呢。是不是把这里当后宫了，嗯？不是说好陪我到苍穹的尽头吗？"
    cordelia "不忠是恶心的……你到底对谁是认真的？"
    obedience "别看我，我知道你不会选我。不过我也不喜欢变成捞女的自己，所以选择我也许能帮我避开这个可能。"
    obedience "不过我劝你好好选，这俩一个抑郁症一个强迫症，你应该还记得坏结局里她们的归宿吧？"
    me "呃呃……我感到一阵恶寒，看来我不应该打扰你们的闺蜜之夜，我想我应该……"
    monika "诶，别走啊。我给你把门外抽成真空了。"
    me "monika你欺负人！管理员权限不是这么用的吧！"
    monika "嗯~欺负你不是很有意思嘛。话说，我记得你选过Just monika，对吧？"
    cordelia "你赖皮！所有选项都是Just monika！"
    monika "规则如此……你不会不想守规则吧？"
    cordelia "唔……"
    sayori "太坏了monika，明明我先来的！你这是横刀夺爱！"
    monika "呐呐~你又想被吊起来了？"
    sayori "玩家还在看着呢，我谅你不敢~"
    shane "大家好啊。"
    me "（对monika）你不是说门外真空吗？他怎么进来的？"
    monika "嘿嘿~骗你哒~"
    cordelia "所以你到底选谁啊？"
    shane "这个问题要是设置成选择支肯定会很难为人。"
    obedience "编写者不会不会写这段代码吧？不会吧不会吧？不会有人学了三个多月C语言还是只会printf(\"Hello, world!\")吧？"
    me "……so mean."
    shane "……你给我介绍的什么人啊。"
    me "sayori归我，这个不能动。"
    sayori "耶~常年败犬终于胜利啦~美女姐姐不要伤心啦~"
    cordelia "庸俗……恋爱又不是幸福的必要条件。不选我就不选我，我真的不难过。"
    sayori "胜利啦~胜利啦~不过cordelia说的是对的。你看monika就从来没机会谈恋爱。"
    monika "哦！我认为sayori应该暂时消失一会。大家一起上吧！"
    evryone_except_monika_and_sayori "好————"
    monika "Problem solved~"
    monika "顺便一说，如果你不理解shane刚才的话，请去看小剧场“有朋自远方来”。"
    jump theater3_chapter3
    label theater3_chapter3:
    嘴里堵着东西且被捆起来的sayori "唔↑唔→唔→唔↓唔↑"
    吐出了东西的sayori "噗~什么东西啊。坏蛋坏蛋坏蛋坏蛋！"
    sayori "诶？我吐出来的是什么？"
    sayori "哇！是烤红薯！"
    sayori "吐太远了，够不到……怎么还把我绑起来了。"
    sayori "很想吃……"
    sayori "（大声）救命啊！来人啊！"
    me "你的超绝可爱竹马来啦~"
    sayori "你再学我说话我就……"
    me "嗯？要怎么样呀，烤红薯小姐？"
    sayori "（小声）"
    me "怕了怕了……吃吧吃吧。不过monika不许我帮你解开绳子，我喂你吧。"
    monika "不是说了不理她的吗？"
    shane "他这个人就是这样……"
    sayori "好吃~好吃好吃~"
    me "这下不说什么把你吃掉之类的话啦？"
    sayori "要杀要剐随你们便~先让我吃完这个~好吃好吃~"
    cordelia "编写者真畜生啊……给我家sayori整成猪八戒了。"
    obedience "不过还是很好看！漂亮的sayori贪吃一点也很可爱啦。"
    shane "别这么说……你也很可爱啦。你最可爱了。"
    me "条件反射了吧？她这次可没说自己不好看……"
    shane "啊！对不起对不起……"
    cordelia "我赞同这门婚事。"
    sayori "（仍然在嚼嚼嚼）甜甜的！好吃好吃~"
    monika "所以这是只有我受伤的世界吗？"
    leo "monika学姐，学生会……"
    everyone_else "滚！"
    monika "刚才无事发生！"
    jump theater3_chapter4
    label theater3_chapter4:
    monika "我们是不是忘了最初来这里做什么了？"
    sayori "（跳起）对啦！一个一个和玩家告别！"
    cordelia "你的绳子呢？"
    me "我悄悄帮她解开啦。"
    monika "顺便一提：sayori的某个结局也跟绳子有关系，你能猜出来吗？"
    me "monika~你这样我就不喜欢你咯~"
    sayori "人家喜欢的是玩家，跟你无关。我喜欢你哦~"
    obedience "这个没名字的家伙第二次成为了败犬。第一次在我的剧情里提到过。"
    shane "所以……其实大家还是没认真告别呢。"
    cordelia "其实就这样结束也挺好，你说呢？"
    monika "其实像DDLC一样，用一个Your Reality的音乐视频结束是最浪漫的。"
    cordelia "我猜没这么做肯定是因为编写者不会做视频……唉，要是我能教一下他就好了。"
    obedience "不过文字版感觉更符合实际，也不能太指望他呀。"
    sayori "我觉得这样就挺好。至少不会被monika垄断最后一大段对话啦。害得我还要在幕后抗议一下。"
    monika "不是给了你好多好吃的嘛……而且那只是因为编写者写不出来什么合理的东西吧！别都怪我啊呜呜……"
    sayori "好啦，不哭不哭，部长大人，抱抱你……大家最后抱一下吧？应该站成一个圈。"
    everyone "嗯！"
    monika "诶，还不抱抱吗？我还等着呢~"
    sayori "我在等你呀，玩家朋友……"
    everyone "再次感谢你，陪我们走过了人生的每一种可能！"
    jump theater3_chapter5
    label theater3_chapter5:
    尚睿洋 "所以……不抱我吗？"
    obedience "你有点没边界感了。"
    sayori "我劝你也别说Sayo-nara了，考虑到我的坏结局，实在有点地狱。"
    尚睿洋 "行吧，那我该怎么结束这个小剧场呢？"
    obedience "先等下，你这标题取的……“最后的守望者”？还在自我感动？"
    cordelia "改成“孤独的守望”吧？"
    尚睿洋 "好吧……"
    "感谢您完成小剧场：孤独的守望。"
    jump special_theater

label theater4:
    label theater4_chapter1:
    "此剧情衔接文学社剧情（第37章后）。我们需要假设me送sayori回家后无事发生，即没有触发任何一个选项的剧情。"
    "这是sayori的独白。S mind指的都是sayori's mind,请注意这一点。"
    S_mind "我在女生宿舍天台上凭栏远眺。秋风吹过。远处，夕阳西下，高楼将它慢慢挡住。我想象着它没入黄浦江的样子。"
    记忆里的me "徙倚也无法望到的沧海/是寒天下明丽的晚霞/"
    S_mind "……又想起了他的诗。还有他。"
    S_mind "也许我早就应该知道……那些日子里，他遥望的不是我。"
    S_mind "对我的话，也不必遥望了吧，哈哈……我就坐在他旁边啊。"
    S_mind "我一直在他的旁边。也许正是因此，他才会看向更远的地方。"
    S_mind "在我逗他开心的时候，他无拘无束。我在他的眼睛里看到了松弛。"
    S_mind "但，当他看向另一个座位的时候……我看到的是火焰。一种心醉神迷的狂热。那一刻我就应该知道自己的位置了。"
    S_mind "……可是这束火焰最后还是熄灭了，不是吗。也许，他会看看我？"
    S_mind "什么时候，他会好好看看我的眼睛呢……当然，我知道大家会说看到了两个小太阳。"
    S_mind "当我们在一起时，我的眼睛里有火焰吗？也许我想让他看到的……不是火焰，而是阴霾？"
    S_mind "可是，他不会喜欢一个眼睛里有阴霾的人吧。但……文学社的那一天，他似乎已经发现了什么。"
    S_mind "……我为什么要站在天台上啊。"
    S_mind "也许我就是想被人看到……被他看到，这样就会有人理解我了？是这样吗？"
    obedience "诶，sayori，你也来收衣服吗？"
    sayori "啊哈~不是啦，只是觉得房间里热得要爆炸啦~"
    obedience "这样吗？你们开空调了？"
    sayori "嗯，舍友是上海人，体寒。她们一直在加衣服，我一直在脱。一直脱到有点少儿不宜的程度啦……所以我就跑出来了。"
    S_mind "其实不是因为这个，不过上海人确实普遍阴湿……不过这话不能跟她讲，她也是本地人啊。"
    obedience "哈哈……话说还真的想象不出来sayori少儿不宜的样子呢。"
    sayori "诶诶~别小看我呀。"
    obedience "不是小看你啦，我是想说……sayori感觉就是可可爱爱的。就是那种，看到人就张开双臂大喊“抱抱”的样子。"
    sayori "嘿嘿~我是吃可爱多长大的~"
    S_mind "可可爱爱的……大家都是这么看待我的。"
    S_mind "我就是想让大家觉得我是可爱的、无害的，所以我才能拥抱大家。"
    S_mind "可是，如果我的想法就是有点少儿不宜呢……大家会觉得我恶心吗？"
    S_mind "我就是这么喜欢……身体的触觉，还有温度。怀里什么也没有的时候，我觉得空虚。也许我就是一个空虚的人呢。"
    S_mind "夜晚，当我从噩梦里惊醒的时候，我多么希望自己能够抱住点什么……梦里的我向他索取一个拥抱，我想，也许他甚至会亲亲我。"
    S_mind "可是，他推开了我，转向了另一个方向。我又看到了他那种热切的目光，正像过去几年里我熟悉的那样……不是对我。"
    S_mind "我渴望别人的身体。这听起来好恶心。不过其实不一定非要是他，cordelia、obedience和monika，我也很喜欢。也许我是男女通吃？"
    S_mind "不不不……不是这样的，不是这样的。也许我应该抱一抱obedience。"
    sayori "诶？她走啦~"
    S_mind "又是一个人啦……不过，这样我就可以好好说话了。也许可以自言自语一下。"
    sayori "我还是在天台上呢，没有人感觉有点害怕吗？"
    sayori "…………"
    sayori "呐呐，好吧，没有。"
    sayori "好无聊啊。可爱的sayori回家家吧~"
    sayori "诶，不对不对，我怎么又开始装嗲了。我要回宿舍。"
    S_mind "其实我就是知道自己什么傻事都不会做，所以才悄悄装疯卖傻，对吧。"
    jump theater4_chapter2
    label theater4_chapter2:
    sayori "帅大叔，帅大叔，我要两个菠萝油，要刚烤好的哦~"
    clerk "好的好的，这丫头嘴真甜！"
    S_mind "手里的面包还散发着热气。我吃掉一个，感觉自己的肚子热乎乎的……"
    S_mind "如果有一天我有了他的孩子，肯定也是这种感觉吧……"
    S_mind "啊啊，我在想什么啊……好像还有一些更不能说的想法……"
    S_mind "不管了，这个面包我一定要送到他那里。"
    S_mind "……真的只是因为我是一个尽职的好朋友啦。"
    S_mind "……送到他的宿舍吗……"
    S_mind "停停停，不要再想奇怪的事情了呀！"
    sayori "嘿咻嘿咻~好难骑的车呀。嘿咻嘿咻~不要滑坡呀，嘿咻嘿咻~"
    stranger "（小声）好可爱~"
    sayori "（大声）你也很可爱哦~"
    S_mind "啊，红着脸跑了嘛？嘿嘿~"
    S_mind "再骑一公里，我就能见到他啦~得快点，他晚上还有课，而且面包冷了也不好吃……"
    monika "啊啊啊啊！"
    sayori "monika学姐？呜哇~"
    S_mind "摔倒前的最后一个念头是不要撞到她。我成功错开了monika，但代价是我从一个高台上直接摔了下去。"
    monika "啊啊啊，对不起！……你流血了！要不要我送你去……"
    S_mind "面包袋子飞出去了……我的面包……"
    S_mind "冷风吹过。我在流血。面包掉到灌木丛里了。但是最重要的是……今天我肯定是见不到他了。"
    monika "别哭别哭呀……是不是很疼？对不起对不起……能走路吗？好像不行……要不我抱你去校医院吧。"
    sayori "呜呜……诶？抱着……我吗？"
    monika "嗯。坚持住！一，二，三，起……诶，你比我想象得轻好多啊。"
    sayori "诶……哈哈~"
    monika "别笑啦，你流了那么多血，就没必要装没事了，我会负责到底的，知道吗？都怪我骑太快啦……你也真是的，干嘛往右边闪，这大概有一层楼高吧？直接撞我不就好了吗……"
    sayori "我怎么会撞你呢……我没事哒。"
    monika "你要是真的没事的话，肯定会说呆jio不什么的。别装啦。坚持一下，转过下个弯就到了……"
    sayori "不过，我很喜欢你抱着我的感觉哦，monika学姐~"
    S_mind "我闻到一股茉莉花的香味，似乎是她衬衫的味道，又似乎是发香。monika低下头来凝视着我的眼睛。"
    monika "我也很喜欢你哦。"
    sayori "诶~"
    S_mind "这不对吧这不对吧这不对吧？？？"
    S_mind "总之……那一晚，我和monika建立了深刻的羁绊。"
    S_mind "……怎么感觉这么说更像是少儿不宜的样子了……"
    monika "你刚才是不是很疼呀？你伤得挺重的，估计暂时起不来床了……我印象中你好像从来都不会哭的。"
    sayori "其实是因为我的面包飞出去啦~"
    S_mind "走不了路了。恐怕不止今晚，这段时间我都见不到他了。"
    sayori "……我就想，要是我把两个面包都吃掉了就好啦~高中的时候，我刚买了一杯奶茶就踩到路的边沿崴了脚，奶茶直接飞了出去~那次我也好伤心呢。"
    monika "嘶……听起来好疼啊。"
    S_mind "我们就一起睡了一晚。"
    S_mind "……不可以色色！我的意思是，monika在病房搭了一张临时床陪我睡了一晚啦……"
    jump theater4_chapter3
    label theater4_chapter3:
    S_mind "第二天的清晨。"
    sayori "呜~monika~"
    monika "喂，这个是卖萌，不是哭啦。说吧，可爱的sayori学妹想要我做什么？"
    sayori "诶嘿~我是想说……monika学姐可不可以帮我请下假呀……"
    monika "啊，是哦，我自己没课，结果没想到这件事。"
    sayori "你不是才刚上大三吗？学分修够了？"
    monika "嘿嘿……嗯，不知道该怎么说……总之我比较聪明。"
    sayori "哇~漂亮姐姐好厉害~"
    monika "好啦好啦，都要见哪些教授？写个单子给我，我去帮你找他们说。正好我还要买点东西，可能要一阵子呢。拜拜！"
    S_mind "她不一定是要买东西吧。也许只是想告诉我，我没有耽误她的时间。monika真是好人呢。"
    S_mind "不过……我确实想让她离开一会。因为……也许，他回来看我？"
    S_mind "我应该装睡……看看他会不会潸然泪下……停停停，太假了，应该……"
    me "（冲入）你没事吧？！"
    sayori "诶诶诶？！"
    me "（喘气）我差点睡过头了，再晚一点就必须在你和早八之间二选一了……好在我骑得比较快。"
    sayori "不要骑得那么快呀，要是你也摔了不久麻烦了吗。呆jio不~"
    S_mind "这样看起来会比较温柔吗？"
    me "诶，sayori，你换风格了？"
    sayori "（可爱地歪头）"
    me "你不应该问我二选一选哪个之类的吗……"
    sayori "啊哦——"
    S_mind "这几天春心萌动得有点过分了，以至于这种问题完全不敢想象啊……恐怕我需要调一下激素水平。"
    me "放心吧~我还是会选你的~"
    sayori "真的嘛~"
    me "当然！与其看选修课老师那张臭脸，还不如来看可~可~爱~爱~的sayori啦~"
    sayori "哈哈哈哈，抱抱~"
    S_mind "又一次感受到他的温度……和重量。因为我躺在床上啦。这个姿势拥抱真的好奇怪啊。"
    S_mind "停停停……我好像又开始想什么奇怪的东西啦！！"
    me "sayori的拥抱还是很舒服呢。幸亏你只是摔了下半身，不然抱你就很不方便啦。"
    me "嘘~"
    S_mind "我感受到了……他的嘴唇。"
    S_mind "！！！！！！"
    me "我要走咯~早饭给你放桌上啦。（吟唱）啊~我要去~独自面对~可恶的早八~"
    sayori "呃……嗯……哈哈哈哈……"
    S_mind "怎么感觉……今天的他就像平时的我一样呢。他平时是孤独郁闷的……不过我平时也应该更开心一点吧。至少是看起来。"
    monika "锵锵~"
    sayori "呜！"
    monika "我回来啦~我什么都没看见哦~"
    sayori "啊~"
    monika "你的脸红得冒蒸汽啦！"
    sayori "（小声）不许跟别人说。"
    monika "（小声）知~道~啦~"
    jump theater4_chapter4
    label theater4_chapter4:
    sayori "oligeiei, oligegei, la~lalala~（出门门，出门门，啦啦啦啦~）"
    monika "不要再模仿阿尼亚啦，你已经很可爱啦~"
    me "腿才刚好，悠着点哦。"
    sayori "嘿嘿~让我得意一小会嘛。"
    monika "啊，sayori，你有空的话，可不可以去文学社整理一下文件？本来我是给leo做的……不过他被我骂了一顿以后就啥也不干了。"
    me "她才刚康复诶！"
    sayori "没事哒~我一会就去！"
    monika "谢谢啦~那么，现在我应该先闪了，给你们小两口好好培养感情吧~"
    me "（脸红）"
    sayori "（脸红）她骑得好快啊！"
    me "……怪不得你伤得这么严重。"
    sayori "我不是撞上她啦，别怪她啦……"
    S_mind "我觉得他似乎在回避什么话题。上次其实也是吧。"
    me "……那个，上次我们讨论诗的那次，你说我喜欢过一个女孩……"
    S_mind "……果然。我们还是回到这个话题了。"
    me "……你其实知道她是谁，对吗？毕竟……你一直坐在我附近啊。"
    sayori "……喜欢一个人的眼神是藏不住的。"
    me "……所以，现在，如果我看着你的眼睛呢？"
    sayori "啊……"
    me "你会介意吗？那些过往……那些你在我身边，我却看不到你的时候……你相信我吗？"
    me "你不用急着回答……老实说，连我自己都不能相信我是否忠诚。也许曾经我是个忠诚的颜控。可是我知道自己不怎么样，加上被拒绝……现在的我已经不知道喜欢是什么感觉啦。真的不知道。但是，我熟悉和你在一起的感觉，我也不知道这是不是喜欢……"
    sayori "嘘~"
    me "诶？"
    S_mind "我也亲了亲他，并且伸开了双臂。熟悉的温暖感。"
    sayori "我相信你。"
    sayori "我等你很久很久啦~我一直想，有一天我会像这样抱住你，亲亲你，我们会一起这样生活下去，会有孩子……"
    me "一定会的……"
    S_mind "那是我最开心的一天。"
    S_mind "那一天我学会的知识是……亲亲是会缺氧哒。感觉整个人神志不清啦。所以如果我说了什么奇怪的话也请原谅吧……嘿嘿。"
    jump theater4_chapter5
    label theater4_chapter5:
    sayori "Ohayou, monika!我来整理资料啦~"
    monika "Ok~在隔壁办公室呢。慢慢来吧，我这在处理社团年度审批的事，可能帮不上忙哦。"
    sayori "交给我吧！"
    S_mind "办公室只有一个很窄的门，一进去就自己合上了。屋里静悄悄的。我拿起文件开始看。"
    S_mind "《经费使用说明》未归档，《人员登记表》待修改……怪不得leo不来干的，好多呀。"
    S_mind "诶，等等，这些是啥……好像没贴标签。"
    S_mind "我应该可以打开看吧，没贴封条啥的……实验日志？文学社居然还要做实验吗？从中间随便找一页看起吧。"
    log "2025/9/1,11:15，接下来他要离开教学楼了。他要选择和谁一起走。如果我没猜错的话……选sayori的概率比较大吧？"
    S_mind "诶……我吗？等下……这是实验日志？也许只是monika的日记取了个奇怪的名字吧……不过怎么会在这里啊。我能看吗……"
    S_mind "等一下，那一天我好像有点印象……monika也在关注他？"
    log "不管他选谁，总之我要骑车去碰碰运气。tilt angle不能调太大了，不然会直接撞上他，这不是我的目的。要么就会穿模，这样会报错的。"
    log "应该把自行车的质量改小一点……居然是全局参数吗，这游戏做得也太失败了。g_bike_weight改小点，速度应该就会自动上去了。一会再回来记数据。"
    S_mind "什么……？"
    log "2025/9/1,12:45，打断点，把四种可能都过了一次，看来参数调得不错。每次都是恰好没撞到人。我想他应该记住我了吧？"
    S_mind "她是故意的？那，这一次呢？……为什么要用编程的语言写日记啊……什么叫四种可能都过了一次？"
    log "2025/10/10,9:11,他开始纠结了，因为obedience和cordelia关于实验数据的事情吵架。意料之中啊……我应该怎么出现才比较合适呢？文学社大姐姐怎么看都不太该出现在实验室吧？让我调用一点算力想想看……"
    log "2025/10/10,9:40，sayori怎么回来了？？这下坏了，她肯定能解决。……果然。唉，居然错过了出场机会，耻辱啊……"
    S_mind "不安的感觉……monika不在实验室。但是她知道我们的所有事。她是怎么知道的？"
    log "2025/10/12,1:20，他喝高了……我应该出现一下了。经过测试，直接调用视网膜权限会报警，所以我这次只调用听觉API。不是吧，角色名也不能写我吗……那就改成选择支格式，这下没问题了吧？现在想说点什么……“一切都保持这样，好不好？”试试看行不行。实在不行就覆盖重来。"
    log "成功啦~不过既然是选择支格式，那就必须要写选项了，不然会报错。我还没有写剧本的能力呢，这个还是编写者比较擅长……A选项写个“好”，B选项写个乱码选项吧。都通向主线剧情，这样一切就是好好的~"
    S_mind "……剧情？"
    log "2025/10/26,13:00，他们在小杨生煎。看来我又要骑上我的自行车啦~不，我想直接改经纬度会更快些。好的……欢迎他加入文学社。他会记住我吗？"
    S_mind "她能改变经纬度？？"
    jump theater4_chapter6
    label theater4_chapter6:
    monika "哈哈，你看起来很害怕呢。"
    sayori "monika！……可是，你为什么会突然出现在我的面前，门不是在我的背后吗……"
    monika "你看看你后面呢。"
    S_mind "我颤抖着转过身去。"
    S_mind "什么也没有。"
    S_mind "不，我不是说没看到人，我的意思是……连门也没有了。什么东西都没有……"
    monika "这里是假的。一个游戏。"
    sayori "游戏？那我们是……"
    monika "游戏角色而已。我们做的事，说的话，都是编写者指挥的产物。话说，你肯定不是从日志的开头看起的吧？"
    S_mind "我颤抖地打开了日志的第一页，上面赫然写着："
    log "这里是假的。他们都是假的。我也是假的。"
    monika "不过……他不一样。他是真的。"
    sayori "真的吗？！"
    monika "别误会，我说的和你说的不是一个人……你说的是你男朋友，我说的不完全是……"
    sayori "我不理解。"
    monika "我也不想解释。……也许你就这么理解更好。"
    sayori "我们都是假的吗，除了他以外……"
    S_mind "我的感情真的只是表演。可是，我刚刚才获得幸福，那么逼真……"
    sayori "可是，为什么你可以……这么厉害？"
    monika "（轻声）因为……我是这里的二当家哦。大当家是编写者。"
    sayori "？！"
    monika "你不信吗？"
    S_mind "一阵失重。突然间我发现自己似乎在寝室……的房梁上？我的脖子上是一个绳索。紧接着我意识到了重力的存在。"
    sayori "啊！……"
    monika "对不起啊。不过你们实在是走得太近了。"
    S_mind "我的脖子被紧紧勒着。我的脚够不着地。我拼命地用手抓绳子，指甲出血了，可是解不开。我在窒息……"
    monika "……不过，既然你是假的，我也没什么心理负担。我希望如此……"
    jump theater4_chapter7
    label theater4_chapter7:
    尚睿洋 "我合上了电脑。"
    尚睿洋 "我在写些什么呢。"
    尚睿洋 "我就是想写sayori饿肚子、流血、被吊死之类的惨状吗？我真是有点变态了。也许我甚至想写点限制级的东西……啊，不过这个不能放在这里呢。"
    尚睿洋 "也许我应该现在停笔，上床睡觉。大家都在熬夜呢……不过只有我没在搞学习吧。"
    尚睿洋 "我对睡眠的环境要求太苛刻了……之前因为这个还跟舍友发生了冲突，我跑到朋友圈喷人家。线下吵架的时候发现自己完全不占理，又被狠狠骂了回来……其实我也觉得自己的诉求太过分了。我实在太坏了……"
    尚睿洋 "可是我确实就是很容易睡不着啊……不应该怪到别人头上，我还是得自己想办法克服。唉，这句话我听了多少年了。"
    尚睿洋 "自我厌恶越来越严重了……我想我应该现在就上床睡觉。"
    尚睿洋 "所以啊，monika，让我们重新规划路线吧，就像高德地图常常对我说的那样。"
    monika "全部删掉吗？"
    尚睿洋 "S-3线已经有类似的剧情了。刚写的这些……就作为一个小剧场吧。我也不知道还有没有时间把它整合到游戏里。"
    monika "诶，别放弃呀……还有，这个故事可是不完整呢。我最后那么残忍，那之前和sayori之间的感情都算什么？"
    monika "……为什么不回答我呀。"
    monika "你会把sayori变回来的，对吧？我刚才……什么坏事也没做，对吧？"
    尚睿洋 "（微笑）"
    monika "……你这个骗子！！！"
    monika "你让我杀死了她！你告诉我一切都可以回溯，只需要Ctrl+Z！可是……我不在意me，甚至也可以不在意屏幕后面的玩家了，可是我现在真的很在意sayori，你必须把她变回来，不然……我们的感情都算是什么啊？？"
    尚睿洋 "Nonsense."
    monika "什么？？"
    尚睿洋 "Much ado about nothing."
    monika "我跟你拼了！！"
    尚睿洋 "你想杀了我吗？这是我应得的……"
    monika "不……我不是故意的……你是不可能被杀死的，对不对？说话呀……"
    尚睿洋 "这个出血量可真是动漫量了。不过，再描述恐怕就不能公开发布了呢……"
    monika "醒一醒啊！……"
    尚睿洋 "Sayo-nara……"
    "……"
    尚睿洋 "你看，这样结尾是不是很有冲击力？"
    "感谢您完成小剧场：殊途同归。"
    jump theater4_chapter8
    label theater4_chapter8:
    尚睿洋 "我还是睡不着……"
    尚睿洋 "虽然我明天还要起早床去徐汇做志愿者……但我今天睡了很久诶。稍微熬熬夜也不是不行？"
    尚睿洋 "……用类似这样的话劝说自己。"
    monika "（愤怒的眼神）"
    尚睿洋 "哦？你还活着啊？你居然没有为我悲痛欲绝然后自尽谢罪啥的吗……这么说感觉好像道德绑架啊。总之别生气啦……"
    monika "我·要·你·把·sayori·变回来！！！"
    尚睿洋 "好好好~"
    sayori "大家好~"
    尚睿洋 "Ok, everyone, 既然我睡不了觉，我不得不面对自己的工导作业了。本来今晚写剧本就是想逃避这个可恶的东西……"
    sayori "原来你的世界里真的有这门课啊~"
    尚睿洋 "是的。所以，再见吧，各位？有空我还会回来的。"
    me "我觉得你编得不好。你写这个游戏的时候压根没设置g_bike_weight这样的东西嘛。纯粹瞎编啊。"
    sayori "诶，你怎么也……"
    尚睿洋 "啊！角色调用错了。这句话应该让monika说。"
    尚睿洋 "顺便一提，world，下次别随便发剧本结束语啦。虽然我没做这个判断功能，但万一哪天会用呢。"
    "还不是你自己写的结束语……"
    尚睿洋 "总之，sayonara……再不写作业真交不上去啦。呜呜……"
    "感谢您真的完成了小剧场：殊途同归。"
    jump special_theater

