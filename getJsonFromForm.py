from flask import request, Flask
import json

# 1. 接收网页端form表单数据，并转dict
form = request.form.to_dict()
json_dict = json.loads(form['data'])   # 提取json数字， data为前端定义的接收字段

# 2. 接收前端上传的文件或图片
file = request.files['image']   # image为前端定义的上传文件字段

# 3. 获取上传文件的文件名
obj = request.files.get('image')
filename = obj.filename

# 4. 文件保存本地保存
file_path = f'data/{filename}'
# 绝对路径 base_path = os.path.dirname(__file__)
file.save(file_path)
