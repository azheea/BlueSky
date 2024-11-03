import os

def extract_response_content(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    response_index = content.find('//Response')
                    if response_index != -1:
                        response_content = content[response_index + len('//Response'):].strip()
                        
                        new_content = response_content
                        
                        with open(file_path, 'w', encoding='utf-8') as output_file:
                            output_file.write(new_content)


# 调用函数，替换为你的文件夹路径
extract_response_content('./vars copy')