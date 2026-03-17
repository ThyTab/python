from pathlib import Path
import json

#存储数据   JSON
#JSON格式存储的数据便于共享
numbers = [2,7,4,1,9]
path = Path('numbers.json')   #若没有，会自动创建json格式文件
contents = json.dumps(numbers)   #使用此函数生成字符串,为对应数据的JSON表示形式
path.write_text(contents)
contents2 = path.read_text()   #此处的contents2为json字符串格式
numbers2 = json.loads(contents)   #将一个JSON格式字符串作为参数，返回一个python对象（此处为列表）
print(numbers2)
