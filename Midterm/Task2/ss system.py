# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = []
STU_FILE = "TODO"


def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    f = open("Stufile.txt", "w")
    f.close()
    print("初始化成功")
    pass


def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    a = int(input("请输入功能："))
    return a

class Student:
    #面向对象的实现
    def __init__(self, name, id):
        self.name = name
        self.id = id


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.保存学生信息")
    print("6.初始化学生信息")
    print("7.分班操作")
    print("0.退出")


def stu_add():
    """此函数用于, 添加学生信息"""
    #stu_init()
    name: str = input("请输入学生姓名")
    id = input('请输入学生ID')
    s = Student(name, id)
    STU_LIST.append(s)
    print("添加成功")


def stu_del():
    """此函数用于, 删除学生信息"""
    a = input("输入想删除的学生姓名：")
    for x in STU_LIST:
        if a == x.name:
            STU_LIST.remove(x)
    pass


def stu_mod():
    """此函数用于, 修改学生信息"""
    a = input("输入想修改的学生姓名：")
    for x in STU_LIST:
        if a == x.name:
            name = input("修改后姓名：")
            id = input("修改后id: ")
            x.name = name
            x.id = id

    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    for x in STU_LIST:
        print(x.name, " ", x.id)
    a = input("请输入查询的学生id")
    for x in STU_LIST:
        if a == x.id:
            print("查找成功")
            print(x.name, " ", x.id)


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    f = open("Stufile.txt", "a")
    for x in STU_LIST:
        f.write(x.name)
        f.write("\t")
        f.write(x.id)
        f.write('\n')
    f.close()
    print("保存成功")


mySET = set()
def stu_set():
    #分班操作
    print("学生分组:")
    mySET.update(STU_LIST)
    a = len(mySET)
    i = 0
    print("第一组")
    for x in mySET:
        print(x.name)
        print(x.id)
        if i == a / 2 and a % 2 == 0:
            print("第二组")
        if i == (a - 1) / 2 and a % 2 != 0:
            print("第二组")
        i += 1

def exec(a):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if a == 1:
        stu_add()
    if a == 2:
        stu_del()
    if a == 3:
        stu_mod()
    if a == 4:
        stu_sel()
    if a == 5:
        stu_save()
    if a == 6:
        stu_init()
    if a == 7:
        stu_set()
def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        exec(user_choice)
        menu()
        user_choice = get_choice()
    pass


if __name__ == '__main__':
    main()