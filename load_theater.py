# load_theaters_with_characters.py
import re

def collect_characters_from_theater(theater_file):
    """从小剧场文件中收集所有角色"""
    characters = set()
    try:
        with open(theater_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            parts = line.split(',', 2)
            if len(parts) < 3:
                continue
                
            chapter, speaker, content = parts
            
            # 跳过非对话行
            if speaker in ['jump', 'choice', 'option', 'end', 'achievement', 'effect', 'world', 'image', 'music', 'sound', 'stop_music', 'hide']:
                continue
                
            # 处理带括号的角色名
            speaker_clean = speaker
            if '（' in speaker:
                speaker_clean = speaker.split('（')[0]
            
            characters.add(speaker_clean)
            
    except FileNotFoundError:
        print(f"警告：找不到小剧场文件 {theater_file}")
    
    return characters

def add_character_definitions(script_file, characters):
    """将新角色定义添加到脚本文件中"""
    # 读取现有脚本
    with open(script_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找角色定义部分的位置
    char_section_end = content.find("# Monika线专用变量")
    if char_section_end == -1:
        char_section_end = content.find("label start:")
    
    if char_section_end == -1:
        print("警告：找不到角色定义部分的位置")
        return
    
    # 获取已定义的角色
    defined_chars = set()
    char_pattern = r'define\s+(\w+)\s*='
    matches = re.findall(char_pattern, content[:char_section_end])
    defined_chars.update(matches)
    
    # 添加新角色定义
    new_definitions = ""
    for char_name in characters:
        if char_name not in defined_chars:
            # 处理角色名中的空格和特殊字符
            var_name = char_name.replace(' ', '_').replace('-', '_')
            if ' ' in char_name or char_name in ['everyone', 'obedience and cordelia']:
                display_name = char_name.title()
            else:
                display_name = char_name.capitalize()
            
            new_definitions += f"define {var_name} = Character(\"{display_name}\")\n"
    
    if new_definitions:
        # 在角色定义部分后添加新定义
        content = content[:char_section_end] + new_definitions + "\n" + content[char_section_end:]
        
        # 写回文件
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"添加了 {len(new_definitions.splitlines())} 个新角色定义")

def convert_theater_content(theater_file, theater_label):
    """完整转换小剧场内容，包括跳转和选项"""
    try:
        with open(theater_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        renpy_code = f"label {theater_label}:\n"
        
        current_chapter = None
        in_choice = False
        choice_text = ""
        options = []
        
        for line in lines:
            line = line.strip()
            
            # 跳过注释和空行
            if not line or line.startswith('#'):
                continue
                
            # 解析为"章节号,角色,内容"格式
            parts = line.split(',', 2)
            if len(parts) < 3:
                continue
                
            chapter, speaker, content = parts
            
            # 处理章节标签
            if chapter != current_chapter:
                if current_chapter is not None and not in_choice:
                    pass
                
                renpy_code += f"    label {theater_label}_chapter{chapter}:\n"
                current_chapter = chapter
            
            # 处理不同类型的行
            if speaker == 'jump':
                renpy_code += f"    jump {theater_label}_chapter{content}\n"
                
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
                    renpy_code += f'    "{choice_text}"\n'
                    renpy_code += '    menu:\n'
                    for option_text, target in options:
                        renpy_code += f'        "{option_text}":\n'
                        renpy_code += f'            jump {theater_label}_chapter{target}\n'
                    in_choice = False
                    options = []
                    
            elif speaker == 'achievement':
                renpy_code += f'    # 成就: {content}\n'
                
            elif speaker == 'effect':
                renpy_code += f'    # 特效: {content}\n'
                
            elif speaker == 'world':
                content_clean = content.replace('"', '\\"')
                renpy_code += f'    "{content_clean}"\n'
                
            elif speaker == 'image':
                # 处理图片显示
                if content.startswith('bg '):
                    # 背景图片
                    bg_name = content[3:]
                    renpy_code += f'    scene bg {bg_name} with dissolve\n'
                elif ' at ' in content:
                    # 角色立绘带位置
                    char_part, position = content.split(' at ', 1)
                    renpy_code += f'    show {char_part} at {position} with dissolve\n'
                else:
                    # 直接显示图片
                    renpy_code += f'    show {content} with dissolve\n'
                    
            elif speaker == 'hide':
                # 隐藏立绘
                renpy_code += f'    hide {content} with dissolve\n'
                    
            elif speaker == 'music':
                if content == 'stop':
                    renpy_code += '    stop music fadeout 2.0\n'
                else:
                    renpy_code += f'    play music {content} fadein 2.0\n'
                    
            elif speaker == 'sound':
                renpy_code += f'    play sound {content}\n'
                
            elif speaker == 'stop_music':
                renpy_code += '    stop music fadeout 2.0\n'
                
            else:
                # 普通对话行
                speaker_clean = speaker
                action = None
                
                if '（' in speaker:
                    char_parts = speaker.split('（', 1)
                    speaker_clean = char_parts[0]
                    action = char_parts[1].rstrip('）')
                
                # 处理角色名中的空格和特殊字符
                speaker_var = speaker_clean.replace(' ', '_').replace('-', '_')
                content_clean = content.replace('"', '\\"')
                
                renpy_code += f'    {speaker_var} "{content_clean}"\n'
                
                if action:
                    renpy_code += f'    # 动作: {action}\n'
        
        # 小剧场结束时返回小剧场菜单
        renpy_code += '    jump special_theater\n\n'
        return renpy_code
        
    except FileNotFoundError:
        print(f"警告：找不到小剧场文件 {theater_file}")
        return f"label {theater_label}:\n    \"小剧场文件未找到\"\n    jump special_theater\n\n"

def add_theaters_to_script(script_file):
    """将小剧场内容添加到主脚本中"""
    theaters = [
        ("theater1.txt", "theater1"),
        ("theater2.txt", "theater2"), 
        ("theater3.txt", "theater3"),
        ("theater4.txt", "theater4")
    ]
    
    # 首先收集所有小剧场中的角色
    all_characters = set()
    for theater_file, label_name in theaters:
        characters = collect_characters_from_theater(theater_file)
        all_characters.update(characters)
    
    # 添加新角色定义到脚本
    add_character_definitions(script_file, all_characters)
    
    # 然后添加小剧场内容
    with open(script_file, 'a', encoding='utf-8') as f:
        for theater_file, label_name in theaters:
            theater_content = convert_theater_content(theater_file, label_name)
            f.write(theater_content)

if __name__ == "__main__":
    add_theaters_to_script('game/script.rpy')
    print("小剧场加载完成！")