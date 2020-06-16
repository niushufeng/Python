# coding = utf-8   ## 中文包

class Cat: # 类的命名，大驼峰法

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

# 创建对象 是主程序
tom = Cat()  # 先执行等号右侧代码，在等号右侧执行是在内存中创建一个变量， 等号左侧 tom负责引用变量

tom.eat()
tom.drink()

print(tom)  # 输出tom内存地址，是16进制

addr1 = id(tom)  # id查询tom在内存中的地址
print("%x" % addr1)  # %x输出16进制 ，%d打印10进制

# 再创建一个猫对象
lazy_cat = Cat()  

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)  # 输出lazy_cat内存地址，是16进制

addr2 = id(lazy_cat)  # id查询lazy_cat在内存中的地址
print("%x" % addr2)  # %x输出16进制 ，%d打印10进制
