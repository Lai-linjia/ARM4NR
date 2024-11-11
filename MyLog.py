from datetime import datetime

class MyLog:
    
    def getDateTime(self):
        # 获取当前日期和时间
        now = datetime.now()
        # 格式化日期和时间为字符串
        formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"当前时间戳：{formatted_timestamp}")
        return formatted_timestamp
    
    def writeLog(self, obj , path=None):
        file_path = 'log.txt'
        if path is None:
            file_path = 'log.txt'    
        else:
            file_path = path
        # 要追加写入的内容
        content_to_append = getDateTime() + obj +"\n"
        # 以追加模式打开文件并写入内容
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content_to_append)


