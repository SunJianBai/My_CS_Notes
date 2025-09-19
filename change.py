import os

# 原始和目标字符串
old_str = "cdn.jsdelivr.net/gh/SunJianBai/pictures@main"
new_str = "raw.githubusercontent.com/SunJianBai/pictures/main"

# 遍历当前目录及所有子目录
for root, dirs, files in os.walk('.'):
    for file_name in files:
        if file_name.endswith('.md'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            if old_str in content:
                content = content.replace(old_str, new_str)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"已处理: {file_path}")
            else:
                print(f"无需修改: {file_path}")
