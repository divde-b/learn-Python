#b站项目，林粒粒（三小时python快速入门）
#one
print("Dad!")
print("妈！")

#two
print("hellow" + "这是一句代码")
print("let\'s go!")
print("我是第一行\n我是第二行")
print("""《定风波.莫听穿林打叶声》
三月七日，沙湖道中遇雨，雨具先去，同行皆狼狈，余独不觉。已而遂晴，故作此(词)。
莫听穿林打叶声，何妨吟啸且徐行。
竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。
料峭春风吹酒醒，微冷，山头斜照却相迎。
回首向来萧瑟处，归去，也无风雨也无晴。""")

#three
greet = "您好，吃了吗"
print(greet,"张三")
print(greet,"罗翔")

#four
UserAge = 17
user_age = 17
User_Age = 17

#five
a,b,c = 1,2,3
number =int(-b + c * a)
print(number)

#six
#这个项目是注释，注释用#号
#这是一行python注释

#seven
s ="ashtray business tender"
print(len(s))
print(s[0])
print(s[21])
print(s[len(s) - 1])
print(s[:])
print(s[3:9])
b1 = True
y = None
print(type(s))
print(type(b1))
print(type(y))

#eight
#小知识：bmi是身体质量指数
weight = float(input("请输入您的体重 (单位:  kg)"))
height = float(input("请输入您的身高 (单位:  m)"))
BMI = weight / height ** 2
print(f"您的bmi值为： {BMI}")

#nine
#if条件语句，判断布尔值ture或false，结合比较运算符使用
messages = int( input("对象的心情指数是： ") )
if messages >= 60:
    print("恭喜，今晚应该可以打游戏，去吧皮卡丘！")
else:#心情指数小于60的时候
    print("为了小命还是别打游戏啦！")

#ten
#一个更完整的bmi计算
weight = float(input("请输入您的体重 (单位:  kg)"))
height = float(input("请输入您的身高 (单位:  m)"))
gender = input("请输入您的性别： ")
BMI = weight / height ** 2
if BMI <= 18.5:
    if gender == "男":
        print("先生您的bmi分类为：偏瘦")
        if gender == "女":
            print("女士您的bmi分类为： 偏瘦")
elif 18.5 < BMI <= 25:
    if gender == "男":
        print("先生您的bmi值为：正常")
        if gender == "女":
            print("女士您的bmi值为： 正常")
elif 25 < BMI <= 30:
    if gender == "男":
        print("先生您的bmi值为：偏胖")
        if gender == "女":
            print("女士您的bmi值为： 偏胖")
else:
    if gender == "男":
        print("先生您的bmi值为：肥胖")
        if gender == "女":
            print("女士您的bmi值为： 肥胖")
print("\nbmi小于18.5为偏瘦\nbmi大于18.5但是小于或等于25为正常\nbmi大于25小于等于30为偏胖\nbmi大于30为肥胖\n")
print(f"请您对照自己的bmi分类: {BMI},来调整您的生活状态，切记一个好的身体比什么都重要")

#eleven
#创建一个购物列表
shopping_list = ["键盘","键帽","音响","电竞椅"]
shopping_list[1] = "硬盘"
print(shopping_list)
print(len(shopping_list))
#创建一个价格列表
price = [799,1024,200,800]
max_price = max(price)
min_price = min(price)
sorted(price)
print(max_price)
print(min_price)

#twelfth
#创建一个成语词典
chinese = {

            "集思广益":"集中众人的指挥和意见，广泛吸取有益的建议，获得更好的效果",
            "浅尝辄止":"稍微尝试一下就停止了",
            "越俎代庖":"超越自己的职责范围，去处理别人应该处理的事",
            "庖丁解牛":"掌握事物内在规律，做事得心应手",
            "饮鸩止渴":"用有害的方法来解决眼前的问题而不顾严重后果",
            "厚积薄发":"要想有所成就就必须静下心来，打好基础进行长期的坚持和积累",
            "捉襟见肘":"处境窘迫，顾此失彼，穷于应付，资源匮乏导致无法从容应对",
            "潜移默化":"受到外来影响在不知不觉中发生变化",
            "春风化雨":"形容教育或感化的力量就如春风拂面，细雨润物，温和持久深渊的影响",
            "触类旁通":"形容人聪明，悟性高，学习能力强善于思考和联想",

}
message = input("请输入您要查询的成语: ")
if message in chinese:
    print(f"您查询的{message}含义如下: ")
    print(chinese[message])
else:
    print("您查询的的成语暂时没有收录")
    print(f"当前词典收录词条数为: ",str(len(chinese)),"条")

#thirteenth
#求平均值的程序while
i = 0
c = 0
user_num = input("请输入数字（完成所有数字输入后，请输入q终止程序）: ")
while user_num != "q":
    number = float(user_num)
    i += number
    c += 1
    user_num = input("请输入数字（完成所有数字输入后，请输入q终止程序）: ")
    if c == 0:
        sums = 0
    else:
        sums = i / c
print(f"您输入的数字平均值为：",str({sums}))

#fourteenth
#定义函数
def Calculate_BMI(weight,height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = "thin"
    elif bmi <= 25:
        category = "normal"
    elif bmi <= 30:
        category = "strong"
    else:
        category = "very_strong"
    print(f"您的bmi分类为：{category}")
    return bmi
result = Calculate_BMI(70,1.8)
print(f"{result}")

#fifteenth
#定义一个学生类
#属性包括姓名，学号，语数英三科的成绩
#能够设置学生某科目的成绩
#能狗打印学生所有科目成绩
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {"chinese":0,"math":0,"english":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grade(self):
        print(f"student:{self.name},(id:{self.id})grades is:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")
chen = Student("chen","10086")
chen.set_grade("chinese",92)
chen.set_grade("math",85)
chen.print_grade()
zeng = Student("zeng","10087")
zeng.set_grade("chinese",90)
zeng.set_grade("english",89)
zeng.print_grade()

#fourteenth
#使用继承
#人力系统，员工分为：全职员工，兼职员工
#全职员工有月薪属性，兼职员工有日薪和每月工作天数
#兼职和全职都有计算月薪方法，计算过程稍显差异

#首先来定义一个员工的父类供全职和兼职员工继承使用
class Employee:
    def __init__(self,name,id):#员工类拥有姓名（name）和员工编号（id）属性
        self.name = name
        self.id = id
#定义一个打印信息的方法
    def print_info(self):
        print("-" * 40  )
        print(f"employee message".center(38))
        print("-" * 40)
        print(f"name：{self.name}")
        print(f"id:   {self.id}")

#定义全职员工（继承父类）
class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):#添加取值员工的月薪属性
        super().__init__(name,id)#super访问父类的方法或属性
        self.monthly_salary = monthly_salary
    def print_info(self):
        super().print_info()
        print(f"monthly_salary: {self.monthly_salary:,.2f} dollar")
        print("-" * 40)
#计算全职员工的月薪的方法
    def calculate_monthly_pay(self):#定义全职员工计算月薪的方法：会返回全职员工的月薪属性
        return self.monthly_salary

#定义兼职员工（继承父类）
class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):#另外添加的属性
        super().__init__(name,id)#接着继承父类的属性
        self.daily_salary = daily_salary
        self.work_days = work_days
    def print_info(self):
        super().print_info()
        print(f"daily_salary: {self.daily_salary}dollar")
        print(f"work_days: {self.work_days}days")
        print(f"monthly_salary: {self.calculate_monthly_pay()} dollar")
#计算兼职员工的月薪方法
    def calculate_monthly_pay(self):#兼职员工的计算月薪的方法，返回日薪*工作天数
        return self.daily_salary * self.work_days

#创建了两个对象一个全职员工一个兼职员工并定义了他们的属性
zhang_lin = FullTimeEmployee("张林","10001",5300)
wang_niu = PartTimeEmployee("王牛","10002",180,16)

#使用父类定义的打印信息的方法
zhang_lin.print_info()
wang_niu.print_info()

print(zhang_lin.calculate_monthly_pay())#不同的类不同的计算方法
print(wang_niu.calculate_monthly_pay())

#fifteenth
#while实现与if相同功能电影票
#这的关键在于try和except关键字
while True:
    mess = input("请输入您的年龄(输入'q'退出)： ")
    if mess == 'q':
        print("程序已经退出")
        break
    try:#try关键字创建一个可能会引发错误的代码块
        age = int(mess)
        if age < 3:
            print(f"您的年龄为: {age},票价为免费")
        elif 3 <= age < 12:
            print(f"您的年龄为： {age},票价为10元")
        elif 12 <= age < 15:
            print(f"您的年龄为： {age},票价为15元")
        else:
            print(f"您的年龄为： {age}，票价为18元")
    except ValueError:#excpet定义错误的类型是值错误，当错误后输出.....
        print("输入无效请输入正确的数字或'q'退出")

#sixteeth