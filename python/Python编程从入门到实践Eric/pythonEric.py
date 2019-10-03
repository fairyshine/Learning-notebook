# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:31:00 2019

@author: 吴孟松
"""
#《Python编程：从入门到实践》学习笔记说明
#分隔用 # In[]
#    或 #%%

# In[]
#第1章 起步
# In[1.1.2]
print("Hello Python interpreter!")
# In[1.1.3]
print("Hello world!")
# In[]
#第2章 变量和简单数据类型
# In[2.2]
message="Hello Python World!"
print(message)
message="Hello Python Crash Course World!"  #可随时修改变量的值
print(message)
# In[2.3]
name="ada lovelace"
print(name.title()) #titile方法修改字符串大小写
print(name.upper())#全部大写
print(name.lower())#全部小写
# In[2.3.2] 合并（拼接）字符串
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print("Hello,"+full_name.title()+"!")
# In[2.3.3]  制表符\t 换行符\n
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# In[2.3.4] 删除空白
favourite_language='python '
favourite_language
favourite_language.rstrip() #使用rstrip方法删除字符串结尾多余的空白
                            #仅临时删除
favourite_language          #使用IDLE查看效果
favourite_language=favourite_language.rstrip()
                            #此处为永久删除空白
favourite_language=" python "
favourite_language.rstrip() #right 仅删除结尾空白
favourite_language.lstrip() #left  仅删除开头空白
favourite_language.strip()  #  删除两侧空白
# In[2.4]
2+3
3-2
2*3
3/2
3**2 #乘方运算
2+3*4
(2+3)*4
# In[2.4.2]
0.2+0.1 #浮点数计算时的问题，语言通病
# In[2.4.3]
age=23
message="Happy "+age+"rd Birthday!"  #变量类型不统一，会报错
print(message)
# In[2.4.3]
age=23
message="Happy "+str(age)+"rd Birthday!"  #将数值(整数、浮点数)转化为字符串
print(message)
# In[2.6]
import this #Python之禅
# In[]
#第3章 列表简介
# In[3.1] #列表是什么，使用方括号来表示
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
# In[3.1.1] #访问列表元素
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
# In[3.1.2]
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[1]) #索引从0而不是1开始
print(bicycles[3])
print(bicycles[-1]) #索引指定为-1，可访问最后一个列表元素
# In[3.1.3] #可像使用其他变量一样使用列表中的各个值
bicycles=['trek','cannondale','redline','specialized']
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)
# In[3.2]
#修改、添加和删除元素
# In[3.2.1]
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'  #修改列表元素
print(motorcycles)
# In[3.2.2]
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')  #append方法添加元素至列表末尾
print(motorcycles)
###
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
###
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati') #insert方法在列表任意位置添加元素，确定索引
print(motorcycles)
# In[3.2.3]
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]  #del语句删除某位置的元素，要知道索引
print(motorcycles)
###
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
###
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0) #pop方法弹出列表中某未知的元素，不再在列表中
print('The first motorcycle I owned was a '+first_owned.title()+'.')
print(motorcycles)
###
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati') #remove方法根据值来删除元素，只删除第一个，若有多个相同值，用循环来判断，见第7章
print(motorcycles)
# In[3.2.3]
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
# In[3.3]
#组织列表
# In[3.3.1]
cars=['bmw','audi','toyota','subaru']
cars.sort() #sort方法按字母顺序排序，永久修改
print(cars)
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True) #sort方法的reverse参数，反序排序
print(cars)
# In[3.3.2]
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))  #sorted函数临时排序
print("\nHere is the original list again:")
print(cars)
# In[3.3.3]
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse() #reverse方法将列表顺序颠倒，永久修改
print(cars)
# In[3.3.4]
cars=['bmw','audi','toyota','subaru']
len(cars)  #len函数返回列表的长度
# In[]
#第4章 操作列表
# In[4.1]
#遍历整个列表
magicians=['alice','david','carolina']
for magician in magicians:  #for循环语句，maigician作为变量使用
    print(magician)
# In[4.1.2]
magicians=['alice','david','carolina']
for magician in magicians:  #别遗漏了for语句的冒号
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")
# In[4.1.3]
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")
print("Thank you,everyone.That was a great show!")  #是否缩进-->是否在循环内
# In[4.3]
#创造数值列表   for 变量 in 范围
# In[4.3.1]
for value in range(1,5): #用range函数生成一系列数字，注意打印的是数字1~4
    print(value)
# In[4.3.2]
numbers=list(range(1,6))
print(numbers)
###
even_numbers=list(range(2,11,2)) #range可以指定步长
print(even_numbers)
###
squares=[]
for value in range(1,11): #有通项公式，range函数能创建几乎任何需要的数字集
    square=value**2
    squares.append(square)
print(squares)
# In[4.3.3] 对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits)) #min函数找出列表最小值
print(max(digits)) #max函数找出列表最大值
print(sum(digits)) #sum函数对数字列表求和
# In[4.3.4] 列表解析
squares=[value**2 for value in range(1,11)] #squares.py的精简版本
print(squares)
# In[4.4]
#使用列表的一部分
# In[4.4.1] 切片  [起始:最终:步长（默认为1）]
players=['charles','martina','michael','florence','eli']
print(players[0:3]) #实际显示索引为0、1、2的元素
print(players[1:4])
print(players[:4]) #不指定第一个索引，自动从列表的开头开始
print(players[2:])
print(players[-3:])#无论列表多长，选取最后三个元素
# In[4.4.2] 遍历切片
players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# In[4.4.3] 复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)
# In[4.4.3] 复制列表2
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)
# In[4.4.3] 复制列表3
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

#这行不通
friend_foods=my_foods  #这样会使两个变量名关联到同一个列表

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)
# In[4.5]
#元组        #列表用[],元组用()
# In[4.5.1]
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#禁止修改元组，运行会报错 dimensions[0]=250
# In[4.5.2] 遍历元组中的所有值
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)
# In[4.5.3] 修改元祖变量
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)    #没有修改元组，修改的是变量名对应的元组
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# In[]
#第5章 if语句
# In[5.1]
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if cars == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# In[5.2] 条件测试
#检查是否相等时区分大小写
#可以用lower方法统一，临时改变字符串
#检查相等 ==    检查不相等 !=
# In[5.2.3]
requested_topping='mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# In[5.2.4]
answer=17
if answer != 42:
    print("That is not the correct answer.Please try agian!")
# In[5.2.5] 检查多个条件
# and 必须同时满足
# or  至少一个满足即可
# In[5.2.6] 检查特定值是否包含在列表中
requested_toppings=['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings  #语句返回布尔值
# In[5.2.7] 检查特定值是否不包含在列表中
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
# In[5.2.8] 布尔表达式
# In[5.3]
# if语句
# In[5.3.1] 简单的if语句
#   if conditional_test:
#       do something
age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# In[5.3.2] if-else语句
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# In[5.3.3] if-elif-else语句
age=12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# In[5.3.4] 使用多个elif语句
age=12
if age < 4:
    price=0
elif age <18:
    price=5
elif age < 65:
    price=10
else:
    price=5
print("Your admission cost is $"+str(price)+".")
# In[5.3.5] 省略else代码块
age=12
if age < 4:
    price=0
elif age <18:
    price=5
elif age < 65:
    price=10
elif age >= 65:
    price=5
print("Your admission cost is $"+str(price)+".")
# In[5.3.6] 测试多个条件
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# In[5.3.6] 错例
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:  #用if-elif-else结构，有一个条件通过，就会跳过余下的测试
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# In[5.4]
# 使用if语句处理列表
# In[5.4.1] 检查特殊元素
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding"+requested_topping+".")
print("\nFinished making your pizza!")
# In[5.4.2] 确定列表不是空的
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")
# In[5.4.3] 使用多个列表
available_toppings=['mushrooms','olives','green peppers',
                    'pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza!")
# In[]
#第6章 字典
# In[6.1]
#一个简单的字典
alien_0={'color':'green','points':5}  #字典名={键（key）：值（value）}
print(alien_0['color'])
print(alien_0['points'])
# In[6.2]
#使用字典
# In[6.2.1] 访问字典中的值
alien_0={'color':'green','points':5}
new_points=alien_0["points"]
print("You just earned "+str(new_points)+" points!")
# In[6.2.2] 添加键-值对
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
# In[6.2.3] 先创建一个空字典
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
# In[6.2.4] 修改字典中的值
alien_0={'color':'green'}
print("The alien is "+alien_0['color']+".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+'.')
# In[6.2.4] 
alien_0={'x_position':0,'y_position':25,'speed':'meium'}
print("Original x-position: "+str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快
    x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position:"+str(alien_0['x_position']))
# In[6.2.5] 删除键-值对
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
# In[6.2.6] 由类似对象组成的字典
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
print("Sarah's favourite language is "+
      favourite_languages['sarah'].title()+
      ".")
# In[6.3]
#遍历字典
# In[6.3.1] 遍历所有键-值对
user_0={
        'username':'efermi',
        'first':'enrico',
        'last':'fermi',
        }
for key,value in user_0.items():  #字典的items方法，返回一个键-值对列表。变量可以任意定，k，v
    print("\nKey: "+key)
    print("Value: "+value)
# In[6.3.1]
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
for name,language in favourite_languages.items():
    print(name.title()+"'s favourite language is "+language.title()+".")
# In[6.3.2] 遍历字典中的所有键
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
friends=['phil','sarah']
for name in favourite_languages.keys():
    print(name.title())    
    if name in friends:
        print(" Hi "+name.title()+
              ", I see your favourite language is"+
              favourite_languages[name].title()+"!")
# In[6.3.2]
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")
# In[6.3.3] 按顺序遍历字典中的所有值
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
for name in sorted(favourite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")  
# In[6.3.4] 遍历字典中的所有值
favourite_languages={
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
        }
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()): #为避免重复，使用set（集合），类似于列表
    print(language.title())
# In[6.4]
#嵌套
# In[6.4.1] 字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#详例见P94，略
# In[6.4.2] 在字典中存储列表
#存储所有点披萨的信息
pizza={
       'curst':'thick',
       'toppings':['mushrooms','extra cheese'],
       }
#概述所点的披萨
print("You ordered a "+pizza['curst']+"-curst pizza "+
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
# In[6.4.2]
favourite_languages={
        'jen':['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','gp'],
        'phil':['python','haskell'],
        }  
for name,languages in favourite_languages.items():
    print("\n"+name.title()+"'s favourite languages are:")
    for language in languages:
        print("\t"+language.title())
# In[6.4.3] 在字典中存储字典
users={
       'aeinstein':{
               'first':'albert',
               'last':'einstein',
               'location':'princeton',
               },
        'mcurie':{
                'first':'marie',
                'last':'curie',
                'location':'paris',
                },
        }
for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name=user_info['first']+' '+user_info['last']
    location=user_info['location']
    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
# In[]
#第7章 用户输入和while循环
# In[7.1] 函数input()的工作原理
message=input("Tell me something, and I will repeat it back to you: ")
print(message)
# In[7.1.1] 编写清晰的程序
name=input("Please tell me your name: ")
print("Hello, "+name+"!")
# In[7.1.1] 提示文字储存在变量中
prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print("Hello, "+name+"!")
# In[7.1.2] 使用int()来获取数值输入
age=input("How old are you?")
age=int(age)  #int函数，将字符串转化为数值
age>=18
# In[7.1.2]
height=input("How old are you, in inches?")
height=int(height)
if height>=36:
    print("\nYou're tall enough o ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# In[7.1.3] 求模运算符
number=input("Enter a number, and I'll tell you if it's even or odd: ")
number=int(number)
if number%2==0:
    print("\nThe number "+str(number)+" is even.") #偶数
else:
    print("\nThe number "+str(number)+" is odd.") #奇数
# In[7.2]
# while循环简介
# In[7.2.1] 使用while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
# In[7.2.2]
prompt="\nTell me something, and I will repeat it back to you."
prompt+="\nEnter 'quit' to end the program."
message=""
while message!='quit':
    message=input(prompt)
    if message!="quit":
        print(message)
# In[7.2.3] 使用标志
prompt="\nTell me something, and I will repeat it back to you."
prompt+="\nEnter 'quit' to end the program."
active=True  #active作为标志使用，判断程序是否应继续运行
while active:
    message = input(prompt)
    if message == 'quit':
        active=False
    else:
        print(message)
# In[7.2.4] 使用break退出循环
prompt="\nPlease enter the name of a city you have visited."
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
    city=input(prompt)       
    if city == 'quit':
        break #任何循环中都可以使用break语句来退出
    else:
        print("I'd love to go to "+city.title()+"!")
# In[7.2.5] 在循环中使用continue
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue  #跳过本次循环，至下次循环的开头
    print(current_number)
# In[7.3]
#使用while循环来处理列表和字典
# In[7.3.1] 在列表之间移动元素
#首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users=['alice','brain','candace']
confirmed_users=[]
#验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# In[7.3.2] 删除包含特定值的所有列表元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']        
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)       
# In[7.3.3] 使用用户输入来填充字典       
responses={}       
# 设置一个标志，指出调查是否继续
polling_active=True
while polling_active:
    # 提示输入被调查者的名字和回答
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")    
    #将答案存储在字典中
    responses[name]=response
    #看看是否还有人参与调查
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
#调查结束，显示结果
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+".")       
# In[]
#第8章 函数
# In[8.1] 定义函数
def greet_user():   #def，函数定义
    """显示简单的问候语"""
    print("Hello!")
greet_user()
# In[8.1.1] 向函数传递信息
def greet_user(username):                       #username为形参
    """显示简单的问候语"""
    print("Hello, "+username.title()+"!")
greet_user('jesse')                            #jeese为实参
# In[8.2]
# 传递实参
# In[8.2.1] 位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
# In[8.2.1] 1.调用函数多次
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')       
# In[8.2.1] 2.位置实参顺序很重要
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('harry','hamster')
# In[8.2.2] 关键字实参，避免了顺序问题
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster',pet_name='harry')  # 形参名 = 实参
# In[8.2.3] 默认值
def describe_pet(pet_name,animal_type='dog'): #若不给出，则使用此默认值。有默认值的要靠后放，否则报错
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='willie')  
# In[8.3]
#返回值
# In[8.3.1] 返回简单值
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
# In[8.3.2] 让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=""):
    """返回整洁的姓名"""
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','hooker','lee')
print(musician)
# In[8.3.3] 返回字典
def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)
# In[8.3.4] 结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name=input("First name:")
    if f_name=='q':
        break
    l_name=input("Last name:")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")
# In[8.4] 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)
# In[8.4.1] 在函数中修改列表  不使用函数的代码
#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
#模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design=unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: "+current_design)
    completed_models.append(current_design)
#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
# In[8.4.1] 使用函数的代码
def print_models(unprinted_designs,complted_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['iphone case','robot pendant','dadecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
# In[8.4.2] 禁止函数修改列表
#function_name(list_name[:]) 使用切片传递列表的副本
# In[8.5] 传递任意数量的实参
def make_pizza(*toppings):   #建立名为toppings的空元组,任意数量的实参都可以装入
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# In[8.5]
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# In[8.5.1] 结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a "+str(size)+
          "-inch pizza with the following toppings")
    for topping in toppings:
        print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
# In[8.5.2] 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',
                           location='princeton',  #注意此处字典的赋值
                           field="physics")
print(user_profile)
# In[8.6]
#将函数存储在模块中
# In[8.6.1] 导入整个模块 pizza.py
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a "+str(size)+
          "-inch pizza with the following toppings")
    for topping in toppings:
        print("- "+topping)
# In[8.6.1]  making_pizzas.py
#import sys
#sys.path.append("D:\\pizza.py")
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')    
# In[8.6.2] 导入特定的函数
# from module_name import function_name
# from module_name import function_0,function_1,function_2
from pizza import make_pizza
make_pizza(16,'pepperoni')   #直接导入函数，就不用使用句点了
make_pizza(12,'mushrooms','green peppers','extra cheese')   
# In[8.6.3] 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')    
# from module_name import function_name as fn
# In[8.6.4] 使用as给模块指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')    
# import module_name as mn
# In[8.6.5] 导入模块中的所有函数
from pizza import * #*运算符可导入全部
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')    
# from module_name import *
# In[]
# 第9章 类
# In[9.1]
# 创建和使用类
# In[9.1.1] 创建Dog类  dog.py
class Dog():     #类中的函数称为方法
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):  #创建新实例时，会自动调用init，self形参必不可少
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+' is now sitting.')
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+' rolled over!')
# In[9.1.2] 根据类创建实例
class Dog():     #类中的函数称为方法
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):  
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+' is now sitting.')
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+' rolled over!')    
        
my_dog= Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()
your_dog=Dog('lucy',3)
# In[9.2]
#使用类和实例
# In[9.2.1] Car类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
# In[9.2.2] 给属性指定默认值
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# In[9.2.3] 修改属性的值  1.直接修改
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23 #此处直接修改
my_new_car.read_odometer()
# In[9.2.3] 修改属性的值 2.通过方法修改
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
#    def update_odometer(self,mileage):  #新方法
#        """将里程表读数设置为指定的值"""
#        self.odometer_reading=mileage
    def update_odometer(self,mileage):
        """
        将里程表读书设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23) #使用方法修改
my_new_car.read_odometer()
# In[9.2.3] 3.通过方法对属性的值进行递增
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表的读数增加指定的量"""
        self.odometer_reading+=miles
my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# In[9.3]
# 继承
# In[9.3.1] 子类的方法 __init__()
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)  #特殊函数super，将父子类结合，父类（superclass）
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name()) 
# In[9.3.3] 给子类定义属性和方法
 class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())      
my_tesla.describe_battery()
# In[9.3.4]  重写父类的方法
#直接在子类里写就行
# In[9.3.5]  将实例用作属性
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())      
my_tesla.battery.describe_battery()
# In[9.3.5]  将实例用作属性 补
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message = "This car can go approximately "+str(range)
        message+=' miles on a full charge.'
        print(message)
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
        self.battery=Battery()
        
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())      
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# In[9.4]
# 导入类
# In[9.4.1] 导入单个类 car.py
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
# In[9.4.1] my_car.py
from car import Car
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
# In[9.4.2] 在一个模块中存储多个类 car.py
"""
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message = "This car can go approximately "+str(range)
        message+=' miles on a full charge.'
        print(message)
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
        self.battery=Battery()
"""
#my_cars.py
from car import ElectricCar
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())      
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# In[9.4.3] 从一个模块中导入多个类
from car import Car,ElectricCar
my_beetle=Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
# In[9.4.4] 导入整个模块
import car
my_beetle=car.Car('volkswagen','beetle',2016) #注意此处变化
print(my_beetle.get_descriptive_name())
my_tesla=car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())'
# In[9.4.5] 导入模块中的所有类
from module_name import *
# In[9.4.6] 从一个模块中导入另一个模块
from 模块 import 类
# In[9.5] Python标准库
from collections import OrderedDict  #调用该类创建了有序字典
favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'                
favorite_languages['phil']='python'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+
          language.title()+".")
# In[9.6] 类编码分格
类名 驼峰命名法  首字母大写，不加下划线
实例，模块名 小写，下划线
# In[]
# 第10章 文件和异常
# In[10.1]
# 从文件中读取数据
# In[10.1.1] 读取整个文件 file_reader.py
with open('data\pi_digits.txt') as file_object:  #open函数  with,文件在不调用时自动关闭
    contents=file_object.read()
    print(contents.rstrip())  #去除结尾返回的空字符串
# In[10.1.2] 文件路径
with open('text_files\filename.txt') as file_object:
file_path='c:\....'
with open(file_path) as file_object:
# In[10.1.3] 逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:  #line非特殊词
        print(line.rstrip())
# In[10.1.4] 创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines() #readlines方法从文件中读取每一行，存在列表中
for line in lines:
    print(line.rstrip())
# In[10.1.5] 使用文件的内容
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
# In[10.2]
# 写入文件
# In[10.2.1] 写入空文件
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
# In[10.2.2] 写入多行
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# In[10.2.3] 附加到文件
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")   
# In[10.2]
# 异常
# In[10.3.1] 处理ZeroDivisionError异常
print(5/0)
# In[10.3.2] 使用try-except 代码块  如果没问题，就跳过except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# In[10.3.8]失败时一声不吭
try:
    except:
        pass  #什么都不做，跳过
# In[10.4] 
#存储数据
# In[10.4.1] 使用json.dump()和json.load()
#模块json
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
# In[10.4.1]
import json
filename='numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)
# In[10.4.2] 保存和读取用户生成的数据
import json
filename='username.json'
try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+'!')
else:
    print("Welcome back, "+username+"!")
# In[10.4.3] 重构
#函数清晰具体化
# In[]
# 第11章 测试代码
# unittest模块









