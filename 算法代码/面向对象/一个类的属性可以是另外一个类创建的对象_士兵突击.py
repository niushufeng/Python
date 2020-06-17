# 哪个类被使用到先开发哪个类
# 开火和发射是动词，动词是用方法来实现
class Gun:

    def __init__(self,model):

        # 1.枪的型号
        self.model = model

        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self,count):  # 添加子弹
        
        self.bullet_count += count

    def shoot(self):  # 枪要发射子弹应该需要几步

        # 1.判断字弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.model)

            return

        # 2.发射子弹 -1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s] 突突突...[%d]" % (self.model,self.bullet_count))


class Soldier:

    def __init__(self,name):

        # 1.姓名
        self.name = name

        # 2.枪-新兵没有枪
        self.gun = None
    def fire(self):

        # 1.判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:  # is身份判断符与“==”不一样  is 判断内存地址，“==”判断值相等  None建议用is
            print("[%s]还没有枪..." % self.name)

            return

        # 2.高喊口号
        print("冲啊...[%s]" % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(50)  # 调用另一个类创建的对象

        # 4.让枪发射子弹
        self.gun.shoot()

# 1.创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()

# 2.创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)
