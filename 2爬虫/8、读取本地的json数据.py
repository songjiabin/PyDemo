import json

#读取本地的json格式数据  得到的是 字典类型 
path = r"E:\py_project_path\2爬虫\res\localjson.json"

with open(path, "rb") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    pass
