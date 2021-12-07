# 开发时间：2021/12/7 13:41
# 学习者：漫画人

class Animal:

    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print("这里是父类会叫的方法")

    def run(self):
        print("这里是父类会跑的方法")

class Cat(Animal):

    def __init__(self,name,color,age,gender,hair):
        self.hair = "短毛"
        super().__init__(name,color,age,gender)

    def huizhuolaoshu(self):
        print("这里是子类猫会捉老鼠的方法")
        print(f"猫猫的姓名：{self.name}，颜色：{self.color}，年龄：{self.age}，性别：{self.gender}，毛发：{self.hair}，{self.name}捉到了老鼠")

    def run(self):
        print("这里是子类猫会叫，会喵喵叫的方法")

class Dog(Animal):

    def __init__(self,name,color,age,gender,hair):
        self.hair = "长毛"
        super(Dog, self).__init__(name,color,age,gender)

    def huikanjia(self):
        print("这里是子类狗会看家的方法")
        print(f"狗狗的姓名：{self.name}，颜色：{self.color}，年龄：{self.age}，性别：{self.gender}，毛发：{self.hair}")

    def run(self):
        print("这里是子类狗会叫，会汪汪叫的方法")

if __name__ == '__main__':
    cat1 = Cat("Lily","orange",2,"公猫","")
    cat1.huizhuolaoshu()

    dog1 = Dog("Tom","black",3,"公狗","")
    dog1.huikanjia()
