import json


person = {
    "name": "RothJie",
    "age": 25,
    "tel":["18313632919","19211696278"],
    "isonly":True,
    "iskong":None
}

# 从python对象转化为Json对象。
print(person,type(person))
jsonStr = json.dumps(person)  #将python类型的数据加载为Json格式的数据
# jsonStr = json.dumps(person,indent=4,sort_keys=True) # indent格式化输出的缩进，sort_keys=Ture是为了输出按字母排序
print(jsonStr,type(jsonStr))

with open('person_info.json','w') as f:
    json.dump(person,fp=f)  # 写入文件 (将python类型的数据转化为Json类型的数据并存入文件)



# 将Json类型的字符串转为Python对象  load,loads
josnString = """
{
    "age": 25,
    "iskong": null,
    "isonly": true,
    "name": "RothJie",
    "tel": [
        "18313632919",
        "19211696278"
    ]
}
"""
pythonObject = json.loads(josnString) # 将Json类型字符串转化为python可识别的对象
print(pythonObject,type(pythonObject))

with open('package.json','r',encoding='utf-8') as f1:
    pythonObj = json.load(f1)  # 加载从文件中读取出来的对象，使之能够被python识别（使之成为python可识别的类型）
    print(pythonObj,type(pythonObj))

