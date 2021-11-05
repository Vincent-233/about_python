"""
parse the subtile ass file (English and mandarin)
解析 ass 格式的中英双语字幕文件，输出为更易阅读的中英对照形式
"""
import re

class Ass_Parse:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_to_file(self, output_file):
        with open(self.file_path,'r',encoding='utf16') as f:
            with open(output_file,'w',encoding='utf8') as w:
                for line in f:
                    if line.startswith('Dialogue:'):
                        pattern = r"Dialogue: 0,(\d:\d{2}:\d{2}.\d{2}).*,,(.*)\\N.*\}(.*)"
                        result = re.search(pattern,line)
                        if result:
                            script = [x for x in result.group(1,3,2)]
                            w.write("{}: {:80}{}\n".format(*script))

if __name__ == '__main__':
    ass_path = r'C:\xxxx.ass.ass'
    ass = Ass_Parse(ass_path)
    ass.parse_to_file('E:\xxxx\Temp\output.txt')


