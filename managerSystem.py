from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据
        self.student_list = list()

    # 1. 程序入口函数
    def run(self):
        # 1. 加载文件中的学员数据
        self.load_student()
        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3. 用户输入目标功能序号
            menu_num = int(input("请输入您要执行的功能序号："))
            # 4. 根据用户输入的序号执行不同的功能
            if menu_num == 1:
                # 1. 添加学员信息
                self.add_student()
            elif menu_num == 2:
                # 2. 删除
                self.del_student()
            elif menu_num == 3:
                # 3. 修改
                self.modify_student()
            elif menu_num == 4:
                # 4. 查询
                self.search_student()
            elif menu_num == 5:
                # 5. 查询所有
                self.show_all_students()
            elif menu_num == 6:
                # 6. 保存
                self.save_student()
            elif menu_num == 7:
                # 7. 退出
                break
            else:
                print("输入有误，请重新输入功能序号！！！")

    # 2. 系统功能函数
    # 2.1 显示功能菜单 -- 打印 -- 使用静态方法
    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1:添加学员")
        print("2:删除学员")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所有学员信息")
        print("6:保存学员信息")
        print("7:退出系统")

    # 2.2 添加学员信息
    def add_student(self):
        # 1. 输入姓名、性别、手机号
        name = input("请输入学员姓名：")
        gender = input("请输入学员性别：")
        tel = input("请输入学员手机号：")
        # 2. 创建学员对象
        student_info = Student(name, gender, tel)
        # 3. 将学员对象添加到学员数据列表
        self.student_list.append(student_info)

    # 2.3 删除学员信息
    def del_student(self):
        # 1. 用户输入目标学员姓名
        del_name = input("请输入要删除的学员姓名：")
        # 2. 遍历学员列表
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                print("%s 学员已删除" % del_name)
                break
        else:
            print("查无此人")

    # 2.4 修改学员信息
    def modify_student(self):
        mo_student = input("请输入要修改的学员姓名：")
        for i in self.student_list:
            if i.name == mo_student:
                print("1:姓名")
                print("2:性别")
                print("3:手机号")
                mo_num = int(input("请选择修改的学员信息编号:"))
                if mo_num == 1:
                    mo_name = input("请输入修改后的名称：")
                    i.name = mo_name
                elif mo_num == 2:
                    mo_sex = input("请输入修改后的性别：")
                    i.gender = mo_sex
                else:
                    mo_tel = input("请输入修改后的手机号：")
                    i.tel = mo_tel
                print(f"修改学员信息成功, 姓名:{i.name}, 性别:{i.gender}, 手机号:{i.tel}")
                break
        else:
            print("查无此人")

    # 2.5 查询学员信息
    def search_student(self):
        search_name = input("请输入需要查询的学员姓名：")
        for i in self.student_list:
            if i.name == search_name:
                print(f"姓名 {i.name}, 性别 {i.gender}, 手机号 {i.tel}")
                break
        else:
            print("查无此人")

    # 2.6 显示所有学员信息
    def show_all_students(self):
        print("姓名\t性别\t手机号")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    # 2.7 保存学员信息
    def save_student(self):
        # 1. 打开文件
        f = open("student_data", "w")

        # 2. 写入要保存的学员信息
        # 注意：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        new_list = list()
        # 2.1 [学员对象]转换成[字典]
        for i in self.student_list:
            new_list.append(i.__dict__)
        print(new_list)
        # 2.2 写入字符串
        f.write(str(new_list))
        # 3. 关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # 1. 打开文件
        try:
            f = open("student_data", "r")
        except:
            f = open("student_data", "w")
        else:
            data = f.read()
            read_list = eval(data)
            print(read_list)
            for i in read_list:
                student_object = Student(i['name'], i['gender'], i['tel'])
                self.student_list = [student_object]
        finally:
            # 3. 关闭文件
            f.close()
