# convert_script_with_media_support.py
import re
import os

def convert_to_renpy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 收集所有角色、成就和使用的图片
    characters = set()
    all_achievements = set()
    used_images = set()  # 收集使用的图片
    
    # 扫描小剧场文件以收集所有使用的图片
    theater_files = ["theater1.txt", "theater2.txt", "theater3.txt", "theater4.txt"]
    
    for theater_file in theater_files:
        if os.path.exists(theater_file):
            with open(theater_file, 'r', encoding='utf-8') as f:
                theater_lines = f.readlines()
            for line in theater_lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(',', 2)
                if len(parts) < 3:
                    continue
                chapter, speaker, content = parts
                if speaker == 'image' and content:
                    # 提取图片标识
                    if ' at ' in content:
                        image_id = content.split(' at ')[0]
                    else:
                        image_id = content
                    used_images.add(image_id)
    
    # 扫描主剧本文件
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(',', 2)
        if len(parts) < 3:
            continue
        chapter, speaker, content = parts
        
        # 收集成就
        if speaker == 'achievement':
            all_achievements.add(content)
        
        # 收集使用的图片
        if speaker == 'image' and content:
            # 提取图片标识
            if ' at ' in content:
                image_id = content.split(' at ')[0]
            else:
                image_id = content
            used_images.add(image_id)
        
        if speaker in ['jump', 'choice', 'option', 'end', 'achievement', 'effect', 'world', 'image', 'music', 'sound', 'stop_music', 'hide']:
            continue
        speaker_clean = speaker
        if '（' in speaker:
            speaker_clean = speaker.split('（')[0]
        characters.add(speaker_clean)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # 在文件最开头添加持久化数据初始化
        f.write('''# 自动转换的Ren'Py剧本

# 强制初始化持久化数据（使用default确保编译时定义）
default persistent.achievements = {}

''')
        
        # 图片和音频资源定义
        f.write("# 图片和音频资源定义\n")
        f.write("init:\n")
        f.write("    # 位置变换\n")
        f.write("    transform left:\n")
        f.write("        xalign 0.2\n")
        f.write("    transform right:\n")
        f.write("        xalign 0.8\n")
        f.write("    transform center:\n")
        f.write("        xalign 0.5\n")
        f.write("    transform slight_left:\n")
        f.write("        xalign 0.3\n")
        f.write("    transform slight_right:\n")
        f.write("        xalign 0.7\n")
        f.write("    \n")
        f.write("    # 背景图片\n")
        f.write('    image bg black = "#000"\n')
        f.write('    image bg white = "#fff"\n')
        f.write('    image bg classroom = "images/bg_classroom.jpg"\n')
        f.write('    image bg library = "images/bg_library.jpg"\n')
        f.write('    image bg dorm = "images/bg_dorm.jpg"\n')
        f.write('    image bg cafeteria = "images/bg_cafeteria.jpg"\n')
        f.write('    image bg lake = "images/bg_lake.jpg"\n')
        f.write('    image bg city = "images/bg_city.jpg"\n')
        f.write('    image bg hospital = "images/bg_hospital.jpg"\n')
        f.write('    image bg shanghai = "images/bg_shanghai.jpg"\n')
        f.write('    image bg metro = "images/bg_metro.jpg"\n')
        f.write('    image bg restaurant = "images/bg_restaurant.jpg"\n')
        f.write('    image bg phone = "images/bg_phone.jpg"\n')
        f.write('    image bg night = "images/bg_night.jpg"\n')
        f.write('    image bg monika_room = "images/bg_monika_room.jpg"\n')
        f.write('\n')
        f.write("    # 角色立绘 - 自动生成所有使用的图片定义\n")
        
        # 角色名称到文件前缀的映射
        char_prefix_map = {
            'sayori': 's',
            'cordelia': 'c', 
            'obedience': 'o',
            'monika': 'm',
            'leo': 'l',
            'teacher': 't'
        }
        
        # 为使用的图片生成定义
        for image_id in used_images:
            if ' ' in image_id:
                # 格式: "角色 表情"
                char_name, expression = image_id.split(' ', 1)
                if char_name in char_prefix_map:
                    prefix = char_prefix_map[char_name]
                    f.write(f'    image {char_name} {expression} = "images/{prefix}_{expression}.png"\n')
                else:
                    # 未知角色，使用角色名作为前缀
                    f.write(f'    image {char_name} {expression} = "images/{char_name}_{expression}.png"\n')
            else:
                # 格式: "文件名" (如 s_bbq)
                # 直接使用文件名作为图片标识
                f.write(f'    image {image_id} = "images/{image_id}.png"\n')
        
        f.write('\n')
        f.write("    # 音乐和音效\n")
        f.write('    define audio.main_theme = "audio/main_theme.ogg"\n')
        f.write('    define audio.happy_music = "audio/happy_music.ogg"\n')
        f.write('    define audio.sad_music = "audio/sad_music.ogg"\n')
        f.write('    define audio.mystery_music = "audio/mystery_music.ogg"\n')
        f.write('    define audio.romantic_music = "audio/romantic_music.ogg"\n')
        f.write('    define audio.your_reality = "audio/your_reality.ogg"\n')
        f.write('    define audio.sayo_nara = "audio/sayo_nara.ogg"\n')
        f.write('    define audio.phone_ring = "audio/phone_ring.ogg"\n')
        f.write('    define audio.door_open = "audio/door_open.ogg"\n')
        f.write('    define audio.rain = "audio/rain.ogg"\n')
        f.write('\n')
        
        # 角色定义
        f.write("# 角色定义\n")
        
        predefined_chars = {
            'me': 'Character("我")',
            'mind': 'Character("内心", color="#888888")',
            'sayori': 'Character("Sayori", color="#ff66aa")',
            'cordelia': 'Character("Cordelia", color="#6666ff")',
            'obedience': 'Character("Obedience", color="#ffaa00")',
            'monika': 'Character("Monika", color="#00aa00")',
            'teacher': 'Character("老师", color="#8888ff")',
            'leo': 'Character("Leo", color="#ff6666")',
            'stranger': 'Character("陌生人", color="#aaaaaa")',
            'waiter': 'Character("服务员", color="#aaaaaa")',
            'shane': 'Character("Shane", color="#aaddff")',
        }
        
        for char_name, char_def in predefined_chars.items():
            f.write(f"define {char_name} = {char_def}\n")
        
        for char_name in characters:
            if char_name not in predefined_chars and char_name not in ['choice', 'option', 'end', 'achievement', 'effect', 'jump', 'world', 'image', 'music', 'sound', 'stop_music', 'hide']:
                if ' ' in char_name or char_name in ['everyone', 'obedience and cordelia']:
                    display_name = char_name.title()
                else:
                    display_name = char_name.capitalize()
                f.write(f"define {char_name.replace(' ', '_').replace('-', '_')} = Character(\"{display_name}\")\n")
        
        # 成就系统函数
        f.write("\n# 成就系统函数\n")
        f.write("init python:\n")
        f.write("    # 成就分类\n")
        f.write("    hug_achievements = [\"拥抱1\", \"拥抱2\", \"拥抱3\", \"拥抱4\", \"拥抱5\", \"拥抱6\", \"拥抱7\", \"拥抱8\", \"拥抱9\", \"拥抱10\", \"拥抱11\", \"拥抱12\", \"拥抱13\", \"拥抱14\", \"拥抱15\"]\n")
        f.write("    school_achievements = [\"脚大1\", \"脚大2\", \"脚大3\", \"脚大4\", \"脚大5\", \"脚大6\", \"脚大7\"]\n")
        f.write("    ending_achievements = [\"结局1\", \"结局2\", \"结局3\", \"结局4\", \"结局5\", \"结局6\", \"结局7\", \"结局8\", \"结局9\"]\n")
        f.write("    possibility_achievements = [\"另一种可能1\", \"另一种可能2\"]\n")
        f.write("    \n")
        f.write("    def grant_achievement(achievement_name):\n")
        f.write("        # 确保持久化数据已初始化\n")
        f.write("        if persistent.achievements is None:\n")
        f.write("            persistent.achievements = {}\n")
        f.write("        persistent.achievements[achievement_name] = True\n")
        f.write("        renpy.save_persistent()  # 立即保存持久化数据\n")
        f.write("        \n")
        f.write("    def check_achievement_group(group_name):\n")
        f.write("        # 确保持久化数据已初始化\n")
        f.write("        if persistent.achievements is None:\n")
        f.write("            persistent.achievements = {}\n")
        f.write("            \n")
        f.write("        if group_name == \"hug\":\n")
        f.write("            achievements_list = hug_achievements\n")
        f.write("        elif group_name == \"school\":\n")
        f.write("            achievements_list = school_achievements\n")
        f.write("        elif group_name == \"ending\":\n")
        f.write("            achievements_list = ending_achievements\n")
        f.write("        elif group_name == \"possibility\":\n")
        f.write("            achievements_list = possibility_achievements\n")
        f.write("        else:\n")
        f.write("            return False\n")
        f.write("            \n")
        f.write("        for achievement in achievements_list:\n")
        f.write("            if achievement not in persistent.achievements or not persistent.achievements[achievement]:\n")
        f.write("                return False\n")
        f.write("        return True\n")
        f.write("\n")
        
        # Monika线专用变量
        f.write("# Monika线专用变量\n")
        f.write("default monika_count = 0\n")
        f.write("default in_sayori_route = False\n")
        f.write("default monika_triggered = False\n\n")
        
        f.write("label start:\n")
        f.write("    play music main_theme fadein 2.0\n")
        f.write("    scene bg black\n")
        f.write("    jump chapter1\n\n")
        
        # 转换逻辑（增加图片和音乐支持）
        current_chapter = None
        in_choice = False
        choice_text = ""
        options = []
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
                
            parts = line.split(',', 2)
            if len(parts) < 3:
                continue
                
            chapter, speaker, content = parts
            
            # 处理章节标签
            if chapter != current_chapter:
                if current_chapter is not None and not in_choice:
                    pass
                
                f.write(f"label chapter{chapter}:\n")
                current_chapter = chapter
                
                # 检测是否进入Sayori专属线路（排除第6章）
                sayori_exclusive_chapters = ['37', '38', '40', '42', '45', '46', '47', '48', '50']
                if chapter in sayori_exclusive_chapters:
                    f.write("    $ in_sayori_route = True\n")
                else:
                    f.write("    $ in_sayori_route = False\n")
            
            # 处理不同类型的行
            if speaker == 'jump':
                f.write(f"    jump chapter{content}\n")
                
            elif speaker == 'choice':
                in_choice = True
                choice_text = content
                options = []
                
            elif speaker == 'option':
                if '->' in content:
                    option_text, target = content.split('->')
                    options.append((option_text.strip(), target.strip()))
                    
            elif speaker == 'end':
                if in_choice:
                    f.write(f'    "{choice_text}"\n')
                    f.write('    menu:\n')
                    for option_text, target in options:
                        # 处理乱码选项 - Monika线触发
                        if option_text == '鑾Ξ鍗':
                            f.write(f'        "{option_text}":\n')
                            f.write('            $ monika_count += 1\n')
                            f.write('            if monika_count >= 3 or in_sayori_route:\n')
                            f.write('                $ monika_triggered = True\n')
                            f.write('                jump chapter999\n')
                            f.write('            else:\n')
                            f.write(f'                jump chapter{target}\n')
                        else:
                            f.write(f'        "{option_text}":\n')
                            f.write(f'            jump chapter{target}\n')
                    in_choice = False
                    options = []
                    
            elif speaker == 'achievement':
                # 成就系统 - 使用持久化数据
                f.write(f'    $ grant_achievement("{content}")\n')
                f.write(f'    # 成就: {content}\n')
                
            elif speaker == 'effect':
                f.write(f'    # 特效: {content}\n')
                
            elif speaker == 'world':
                content_clean = content.replace('"', '\\"')
                f.write(f'    "{content_clean}"\n')
                
                # 检测结局并结束游戏
                if "感谢您完成" in content:
                    f.write('    stop music fadeout 2.0\n')
                    f.write('    return  # 游戏结束\n')
                
            elif speaker == 'image':
                # 处理图片显示
                if content.startswith('bg '):
                    # 背景图片
                    bg_name = content[3:]  # 去掉"bg "前缀
                    f.write(f'    scene bg {bg_name} with dissolve\n')
                elif ' at ' in content:
                    # 角色立绘带位置，格式: "图片标识 at 位置"
                    char_part, position = content.split(' at ', 1)
                    f.write(f'    show {char_part} at {position} with dissolve\n')
                else:
                    # 直接显示图片
                    f.write(f'    show {content} with dissolve\n')
                    
            elif speaker == 'hide':
                # 隐藏立绘
                f.write(f'    hide {content} with dissolve\n')
                    
            elif speaker == 'music':
                # 播放音乐
                if content == 'stop':
                    f.write('    stop music fadeout 2.0\n')
                else:
                    f.write(f'    play music {content} fadein 2.0\n')
                    
            elif speaker == 'sound':
                # 播放音效
                f.write(f'    play sound {content}\n')
                
            elif speaker == 'stop_music':
                # 停止音乐
                f.write('    stop music fadeout 2.0\n')
                
            else:
                # 普通对话行
                speaker_clean = speaker
                action = None
                
                if '（' in speaker:
                    char_parts = speaker.split('（', 1)
                    speaker_clean = char_parts[0]
                    action = char_parts[1].rstrip('）')
                
                speaker_var = speaker_clean.replace(' ', '_').replace('-', '_')
                content_clean = content.replace('"', '\\"')
                
                f.write(f'    {speaker_var} "{content_clean}"\n')
                
                if action:
                    f.write(f'    # 动作: {action}\n')
        
        # 添加小剧场菜单
        f.write("\n# 小剧场菜单\n")
        f.write("label special_theater:\n")
        f.write('    "请选择要观看的小剧场："\n')
        f.write("    menu:\n")
        f.write('        "查看成就详情":\n')
        f.write('            jump achievement_details\n')
        f.write('        "有朋自远方来" if check_achievement_group(\"hug\"):\n')
        f.write('            jump theater1\n')
        f.write('        "假装游刃有余的一天" if check_achievement_group(\"school\"):\n')
        f.write('            jump theater2\n')
        f.write('        "孤独的守望" if check_achievement_group(\"ending\"):\n')
        f.write('            jump theater3\n')
        f.write('        "殊途同归" if check_achievement_group(\"possibility\"):\n')
        f.write('            jump theater4\n')
        f.write('        "返回游戏":\n')
        f.write('            return\n')
        f.write('        "返回主菜单":\n')
        f.write('            $ MainMenu(confirm=False)()\n')
        f.write('\n')
        
        # 添加成就详情页面
        f.write("# 成就详情页面\n")
        f.write("label achievement_details:\n")
        f.write('    "成就详情"\n')
        f.write('    "=== 成就1：抱抱能量！ ===\\n"\n')
        f.write('    "说明：你的可爱青梅永远在这里~完成所有15次拥抱可解锁。\\n"\n')
        f.write('    "完成情况："\n')
        f.write('    $ hug_completed = 0\n')
        f.write('    python:\n')
        f.write('        for achievement in hug_achievements:\n')
        f.write('            if achievement in persistent.achievements and persistent.achievements[achievement]:\n')
        f.write('                hug_completed += 1\n')
        f.write('                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")\n')
        f.write('            else:\n')
        f.write('                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")\n')
        f.write('    "已完成: [hug_completed]/15\\n"\n')
        f.write('    \n')
        f.write('    "=== 成就2：学在脚大！ ===\\n"\n')
        f.write('    "说明：孵蛋孵蛋蛋孵蛋~日月光华同灿烂~完成所有7次关于脚大的剧情可解锁。\\n"\n')
        f.write('    "完成情况："\n')
        f.write('    $ school_completed = 0\n')
        f.write('    python:\n')
        f.write('        for achievement in school_achievements:\n')
        f.write('            if achievement in persistent.achievements and persistent.achievements[achievement]:\n')
        f.write('                school_completed += 1\n')
        f.write('                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")\n')
        f.write('            else:\n')
        f.write('                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")\n')
        f.write('    "已完成: [school_completed]/7\\n"\n')
        f.write('    \n')
        f.write('    "=== 成就3：现在，大家都高兴了？ ===\\n"\n')
        f.write('    "说明：这是DDLC开局试图作弊时触发的死亡旁白。完成主线所有9个结局可解锁。\\n"\n')
        f.write('    "完成情况："\n')
        f.write('    $ ending_completed = 0\n')
        f.write('    python:\n')
        f.write('        for achievement in ending_achievements:\n')
        f.write('            if achievement in persistent.achievements and persistent.achievements[achievement]:\n')
        f.write('                ending_completed += 1\n')
        f.write('                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")\n')
        f.write('            else:\n')
        f.write('                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")\n')
        f.write('    "已完成: [ending_completed]/9\\n"\n')
        f.write('    \n')
        f.write('    "=== 成就4：另一种可能 ===\\n"\n')
        f.write('    "说明：其实故事还有主线之外的一种奇怪走向……也许会类似于S-3线？你会明白的。\\n"\n')
        f.write('    "完成情况："\n')
        f.write('    $ possibility_completed = 0\n')
        f.write('    python:\n')
        f.write('        for achievement in possibility_achievements:\n')
        f.write('            if achievement in persistent.achievements and persistent.achievements[achievement]:\n')
        f.write('                possibility_completed += 1\n')
        f.write('                renpy.say(None, achievement + " {color=#00ff00}✓{/color}")\n')
        f.write('            else:\n')
        f.write('                renpy.say(None, achievement + " {color=#ff0000}✗{/color}")\n')
        f.write('    "已完成: [possibility_completed]/2\\n"\n')
        f.write('    \n')
        f.write('    menu:\n')
        f.write('        "返回小剧场菜单":\n')
        f.write('            jump special_theater\n')
        f.write('\n')

if __name__ == "__main__":
    convert_to_renpy('story.txt', 'game/script.rpy')
    print("转换完成！")