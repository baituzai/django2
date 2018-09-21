<<<<<<< HEAD
# django2
学生信息表
=======
# django2
学生信息表
>>>>>>> student infoo

第一课要介绍一种设计模式 —— MVC
MVC 是 Model View Controller 的缩写，也就是模型、视图、控制器三者协同工作的一种设计模式
初级课程中我们是通过 Django 做了一个留言板
其中主要的代码是 models.py, views.py, urls.py 这三部分
先看一下 models.py这个文件用了一个 Python 的类来描述表，我们管这个叫模型(Model) 我们可以通过这个类，使用简单的 Python 代码对数据进行创建、修改、更新等操作
这个文件包含了页面的业务逻辑，其中函数的返回就是视图(View) 视图是应用程序中处理数据显示的部分，通常视图是依据模型数据创建的
这个文件指出了某个 URL 调用的是哪个视图在我们的例子中，我们输入 http://127.0.0.1:8000/mesboard 这个地址就会调用 index 这个函数
这是本地的测试，实际开发中代码会放在服务器上，如果你的域名是 www.google.com，那么你访问 www.google.com/mesboard 就会看到留言板的页面
这就是 MVC 的设计模式，它把定义和访问数据的方法(模型)与处理用户交互的部分(控制器)，还要展示出的界面(视图)分离开来
降低了程序的耦合性，提高的代码的复用性
视图层和业务层分离，使得修改起来更方便，若需求改变，只需修改对应的模型部分即可
然后根据模型数据对视图做相应修改，这样也就更容易协作开发，不同的人做不同的部分，也提升了开发效率

我们就做一个学生的信息表，用 Django 编写一个接口，然后通过 HTML、JS 来调用，完成这个项目
一步一步来，我们先用 Django 创建一个新项目，并创建用户名和密码
django-admin startproject UserTable .

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
admin  admin1234

python manage.py startapp UserTable
CommandError: 'UserTable' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.
PS G:\django2> python manage.py startapp UserInfo

找到 settings.py 在 INSTALLED_APPS 中加入你创建的名字，比如UserInfo




We’ve detected the file has mixed line endings. When you commit changes we will normalize them to Windows-style (CRLF).
