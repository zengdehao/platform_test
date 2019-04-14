import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


class OperationJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = os.path.join(os.path.dirname(current_dir),'dataconfig/user.json')
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.loads(fp)
            return data

    # 根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        return self.data[id]

    # 写入jsons数据
    def write_data(self,data):
        with open(self.file_path) as fp:
            fp.write(json.dumps(data))
