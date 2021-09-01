# ourMemory906

环境要求:
```
python == 3.7.4

django == 3.1
```

运行服务：
```shell
# 进入目录
cd blogs

# 开启服务
python manage.py runserver
```

设置超级管理员账户:
```shell
cd blogs

# 创建用户
python manage.py createsuperuser 
```

开启服务后，浏览器访问127.0.0.1:8000/admin
使用管理员用户账户登陆，进行文章编辑



