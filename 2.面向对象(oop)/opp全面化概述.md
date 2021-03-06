- oop-python面向对象
    - python的面向对象编程
       - 面向对象
          - 面向对象概述
          - 类的基本实现和应用
             - anaconda基本使用
             - 类和对象的成员分析
             - self参数
          - 面向对象三大特性
             - 封装
                - 公开，私有，受保护       
             - 继承
                - super
                - 多重继承和单继承
                - 构造函数
                - 钻石继承问题解答
             - 多态,Mixin
          - 类的相关常用函数
          - 类的成员描述符(属性)
          - 类的内置属性
       - 魔法函数
          - 魔法函数概述
          - 构造类魔法函数
          - 运算类魔法函数
       - 类的对象实现的三种方法
          - 实例方法
          - 静态方法
          - 类方法
       - 抽象类
          - 抽象方法
       - 自定义类
          - 使用methodType实现
          - 使用type实现
          - 使用MetaClass(元类)实现


1 . 面向对象概述

- oop面向对象思想：
   - 把一件事情需要做的过程，分割成几个独立的部分，并且链接在一起，在修改某一部分时不影响其他部分的正常工作

- oop名词(装逼用)
   - OO ：面向对象
   - OOA ：面向对象的分析
   - OOD ：面向对象的设计 
   - OOI ：面向对象的实现
   - OOP ：面向对象的编程
   - OOA->OOD->OOI:面向对象功能的实现过程
   
- 类和对象的概念
   - 类：抽象词，代表一个集合，共同使用的事物
   - 对象：具体实现的事物，单个个体
   - 类和对象的关系
      - 类就是一个群体，而对象则是从这个群里里面获取一个个体，所以群体是个抽象的概念，而个体才是实现
      
- 类的内容
   - 代表事物的特征，叫做属性(变量)
   - 表明事物的功能或者需要实现的动作，被称之为成员方法(函数)
 
2 . 类的基本应用与实现

- 类的命名
   - 约定俗称使用大驼峰的命名方式(由一个或者多个单词构成，每个单词首字母大写，单词跟单词之间相连)
   - 尽量避开跟系统定制的类命名相同
   
- 类的创建与实例化使用
   - 案例在 oop类的实现
   - 语法：
      - class 类名():
          - def 函数名(self):
              - pass
   - 注意:
      - 必须使用class来创建类
      - 类只能由属性和方法构成，其他不允许出现(比如调用或者引用函数都只能在成员方法(函数)里面使用)
      - 成员属性定义可以直接使用变量赋值，如果无值，可使用None
   - 实例化使用
      - 语法：
         - 变量名 = 类名() 
         
- 可以使用类的内置函数检查类和对象的所有成员
   - 对象的所有成员检查
     - 对象名.__dict__
   - 类所有的成员检查
     - 类.__dict__

3 . anaconda基本使用

- anaconda概述
  - anaconda是一个虚拟环境管理器，也是一个安装包管理器
  
- anaconda基本语法
  - conda list: 显示anaconda安装的包
  - conda env list 显示anaconda的虚拟环境列表
  - conda create -n xxx python=3.6 ： 创建python版本为3.6的虚拟环境，名称为xxx
    - anaonda这个创建一个版本的虚拟环境，有没有点像类的实例化对象


4 . 类和对象的成员

- 类和对象成员的关系概述（成员意为变量，属性与函数）
  - 类和对象都可以存储成员(变量),成员可以归类所有，也可以归对象所有
  - 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员，那如果对象中有此成员，则优先使用该对象的成员
  - 创建实例化对象时，类中的成员并不会放入对象里面，而是得到一个空的对象，但该对象与类有连接关系，可直接从类中调用成员使用
  - 通过对象对类中的成员重写并不会影响到类中的成员，只会保存到对应的对象中
  
5 . self参数

- self概述
  - self在对象的方法中表示当前对象本身，当一个对象调用一个带有self参数的函数时，就会将调用对象传入被调用的函数里面
  - self并不是关键字，不需要当作参数进行传值，理论上可使用任何变量名称代替，只不过约定俗成使用self而已
  - 在类的函数里带有self形参才能被对象所调用，而不带有self形参的函数只能类进行调用
  - 如果非得使用对象访问不带有self的函数时，可以使用__class__访问
    - __class__语法：
      - 对象名.__class__.函数名

6 . 面向对象三大特性
- 封装
- 继承
- 多态

6 . 1 封装

- 封装概述
  - 封装就是对对象的成员进行访问限制
  
- 封装的三个级别
  - 公开 ： public
  - 受保护的 ： protected
  - 私有的 ： private
  - 注意 public，protected，private都不是关键字
  
- python的下划线约定俗成
  - _变量名 ：受保护的，表示内部使用，无法被import引入
  - 变量名_ ：表示避免和关键字冲突
  - __变量名 ： 私有的，使用了name mangling技术，会自动加上类名前缀，不能被子类或者类外部使用
  - __变量名__ ：魔术方法或用户控制的命名空间，后面会魔法函数详解
  
- 私有private
  - 私有成员属于最高级别的封装，只能在当前类或者对象访问
  - 语法:
    - class Person():
          def siyou(self):
        # __name是私有
              __name = "hahah"
  - python采用的私有变化并不是与java一样真的私有了，而是采用了name mangling改名策略，从效果达到私有
    - 如name mangling一样，python很多编程理论虽然存在，但不像java一样那么规范化，而是通过手段达到了同样的效果
  - 如果真的需要访问私有对象，则可以使用_classname_attributename访问
         
- 受保护protected
  - 受保护的封装时将对象成员进行一定级别的封装，然后在之类或者类中都可条用，但无法进行import引用
  - 语法:
    - class Person():
          def siyou(self):
        # _name是受保护的
               _name = "hahah"
               
- 公开的public 
  - 公开的封装实际对成员没有任何规范，任何地方都可以访问
  - 语法
    - class Person():
          def siyou(self):
        # name是公开的
                name = "hahah"

6 . 2 继承

- 继承基本概述
  - 继承 ： 让一个类去获得另一个类的成员属性和方法
  
- 好处
  - 减少代码，增加代码复用性，同时可以设置类与类之间的关系
  
- 继承与被继承的概念
  - 被继承的类称父类，基类，超类
  - 继承的类称子类，派生类
  - 父类和子类有着Is-A(继承关系)
    - 三种关系
      - Is-A继承关系
        - 继承是一种强耦合的结构，父类改变，子类也应该改变，而子类改变，父类不会跟着改变
      - Has-A合成关系
        - 是关联关系的一种，使用一个私有的变量去代表整体对象用于负责构建和销毁代表部分对象，代表部分的对象不能共享
      - Use-A依赖关系
        - 指类与类(通常为函数的参数)之间的连接，依赖总是单向
        
- 继承的语法
  - class Person():
       def haha(self):
           pass

    class man(Person):
        pass
        
- 继承的特征
  - 所有的类都继承自object类，即所有的类都是object的子类
  - 子类一旦继承父类，则可以使用父类中除私有成员外的所有成员方法和成员属性
  - 子类继承父类后并没有将子类成员完全赋值到子类，而是和对象一样，通过引用关系访问调用，可使用__dict__查看
  - 子类可以自行定义独有的成员属性和方法
  - 在调用时，如调用的成员子类里面有，则优先调用子类成员
  - 子类如果想要扩充父类的某方法，可以在定义新方法的同时访问父类方法来进行方法重写,但重写过后的改变将不影响父类
    - 可以使用 父类名.父类方法 的格式来调用父类成员
      - 父类名语法
        - class Person():
             def haha(self):
                  pass

          class man(Person):
             def haha(self):
                  Person.haha(self)
                  print("asd")
                  
    - 也可以使用super().父类成员的格式调用
      - super语法
        - class D():
             def haha(self):
                  print("Asd")

          class A(D):
             def haha(self):
                  super(A, self).haha()
                  print("asd")
                  
- 继承成员属性与成员函数查找顺序问题
  - 优先查找自己的变量成员，如果找不到则一直寻找父类，直到查找到object还没时就报错
  - 构建函数也一样，优先寻找自己的，没有则寻找父类
  
- super 
  - super不是关键字，而是一个类
  - super的作用是获取MRO(MethodResolustionOrder)列表中的第一个类
  - super并不是代表父类，而是通过super来调用父类
  - super调用时使用的构建函数就是调用父类的构建函数
  
- 单继承与多继承
  - 单继承：每个类只能继承一个类
    - 优点：传承有序，逻辑清晰，语法简单，隐患少
    - 缺点：功能无法无线扩展，只能在唯一的继承链中扩展
  - 多继承：每个类可以继承多个类(也就是java里的接口)
    - 优点：类的功能扩展方便
    - 缺点：继承关系混乱，容易产生调用时不知向那个父类申请调用
    
- 构造函数
  - 构造函数概述
    - 构造函数是一类特殊的函数(魔法函数)，在类实例化之前使用
    - 优先查找子类的构造函数，如果还是查找不到则按照MRO的顺序进行查找
    - 如果查询的是父类的构建函数，那么调用时要注意参数
    
- 钻石继承问题
  - 钻石继承又被称菱形继承，是由多个子类继承同一个父类，而这些子类又被同一个类继承，而继承的关系图就形成了菱形图谱
  - MRO
    - MRO概述
      - MRO就是多继承中，用于保存继承顺序的一个列表
      - python本身采用python3算法来对多重继承进行计算，并返回结果
    - MRO列表的计算原则
      - 子类永远在父类前面
      - 出现多个父类时，将按照继承时的顺序进行排序
      - 如果出现了爷类，孙子类则会选择继承顺序第一的父类进行继承

6 . 3 多态

- 多态的基本概述
  - 多态就是同一个对象在不同情况下以不同状态出现
  - 多态不是语法，而是一种设计思想
  - 多态性：一种调用方法，不同的执行结果
  - 大致思想就是一件事每个人都需要去做，但是不知道每个人做这件事的过程，不同的过程就会产生不同的结果，而父类方法就是定义需要去做的事情，子类则是遇到不同情况则进行重写
  - https://www.cnblogs.com/luchuangao/p/6739557.html（多态性与多态）


- Mixin设计模式
  - 主要采用多继承方式对垒的功能进行扩展
  - https://www.cnblogs.com/aademeng/articles/7262520.html (关于Python的Mixin模式)
  - Mixin的设计思想：将整个机器的功能独立化，这样可以避免当某功能无法使用时，不会影响其他功能的正常工作，让功能与功能之间的依赖性减少
  - 使用Mixin需要注意：
    - 首先Mixin实现的必须是某一单一功能，而不是物品
    - 职务必须单一，如果内含多个功能，也要写多个Mixin
    - Mixin不依赖于子类的实现，自我能运行并传出结果
    - 子类如果没有继承到Mixin类，也不会影响正常运行，只是缺少了某个功能，大幅度减少功能之间的依赖性
  - 优点
    - 使用Mixin可以在不对类进行任何修改的情况下，添加父类进行扩充功能
    - 比起钻石多继承好处在不会在寻找父类功能的时候遇到分叉，因为Mixin每个类的实现只继承唯一一个单一的功能
    - 可以方便的功能的扩展和删除，划分等等操作
    - 可以根据任意调整移动子类继承的功能
    - 避免了钻石继承的遍历混乱
    
7 . 类相关常用函数

- issubclass(class,classinfo)：检测一个类是否是另一个类的子类
- isinstance(object,classinfo)：检测一个对象是否是一个类的实例
  - type和isintance的区别
    - type不会认为子类是一种父类类型，不考虑继承关系
    - isinstance会认为子类是一种父类类型，考虑继承关系
- hasattr(object,name)：检测一个对象是否有成员属性
- getattr(object,name[,default])：get attribute 获取属性
- setattr(object,name,value)：set attribute 设置属性
- delattr(object,name)：del attribute 删除属性
- dir([object])：不带参数时返回当前类的变量，方法和定义的类型列表
  带参数时返回参数的属性，方法列表，如果参数里包含方法__dir__
  该方法被调用，如果参数不包含有__dir__方法，则最大程度收集参数信息
- 案例都在 类相关常用函数.py

8 . 类的成员描述符(属性)
- 类的成员描述符是为了在类中对垒的成员属性进行相关操作而创建的一种方式
  - get：获取属性的操作
  - set：修改或者添加属性操作
  - delete：删除属性的操作

- 类的三大成员描述符
  - 使用类实现描述器
    - 类描述器：一个类实现了__get__,__set__,__delete__，三个方法中的任何一个方法就是描述器，仅仅实现__get__方法就是非数据描述器，同时实现__get__,__set__就是数据描述器
    - https://www.cnblogs.com/52py/p/8662704.html
  - 使用属性描述符
    - 描述符
      - object.__get__(self,instance,owner)
      - object.__set__(self,instance,owner)
      - object.__delete__(self,instance)
      - self代表当前实例对象，instance是owner的实例,owner代表属性所属类
  - 使用property函数
    - property（fget,fset,fdel,doc）
    - @property和函数.setter
  - 案例在类成员描述符.py

- 无论是那种修饰符都只是为了对成员属性进行控制操作而已


9 . 类的内置属性

- __dict__：以字典的方式显示类的成员组成
- __doc__：获取类的文档信息
- __name__：获取类的名称，如果在模块中使用，获取模块的名称
- __bases__：获取某个类的所有父类，以元组的方式显示
  - 案例 类的内置函数.py

10 . 类的常用魔法函数

- 魔法函数概述
  - 魔法函数就是一种不需要人为去进行调用的函数
  - 魔法函数会在特定的时刻自行触发
  - 魔法函数的特征：在函数名前后都有两个下划线包裹

- 操作类：
  - __init__：构造函数，在类被实例化前使用
  - __new__：对象实例化方法，次函数特殊，一般不需要使用
  - __call__：把实例对象当作函数使用时触发
  - __str__：当实例对象被当作字符串使用时触发
  - __repr__：返回字符串
    - __repr__和__str__的区别
      - __repr__：你所需要转化的东西repr是明确的，也会直接进行转化
      - __str__：你所需要转化的东西如果不依靠print进行打印的化，你会发现并没有进行转化，所以str目标没有repr明确，但是他在可读的时会自动帮你转化
        - 容器str用途包含对象repr
      - repr比较面向于程序员，而str面向于客户

- 描述符
  - __set__：设置或者创建一个属性
  - __get__：获取一个属性的值
  - __delete__：删除一个属性
  - 案例在类成员描述符.py

- 属性操作相关
  - __getattr__：访问一个不存在的属性时触发
  - __getattribute__：属性访问拦截器，当某个类的属性被访问，则会自动调用类里面的该方法，经过改变之后再把name的值返回
  - __setattr__：对成员属性进行设置的时触发
  - __setitem__：给对象使用下标赋值时触发
  - __getitem__：在获取被设置下标值的对象的值时触发
  - __delitem__: 在删除下标方式赋值的对象时触发
  - __iter__：在迭送自己定义的对象时触发
  - __del__：这算是个构造器，或者回收器，当对象引用数降到0时执行，但有时候会延迟执行，不推荐执行
    - 注意：在使用成员属性值修改时不能直接进行赋值操作，否则会死循环

- 运算分类相关魔法方法
  - __gt__：进行大于判断时触发
    - 返回值可以为任何值，但是推荐布尔值

- 全部案例除了描述符都在 类的常用魔法函数

11 . 类和对象的三种方法

- 实例方法
  - 需要实例化对象才能使用的方法，使用过程中可能需要截获对象其他子类的方法进行完成

- 静态方法
  - 不需要实例化，直接通过类进行访问，主要用来存放逻辑性的代码，不涉及到类里面的属性和方法，没有像self一样的参数

- 类方法
  - 不需要实例化，直接通过类本身作为对象进行操作，和静态方法的区别在于，不管这个方法是从实例调用还是从类调用，都作为第一个参数传进来

- 案例在 类的三种方法

12 . 抽象类
- 抽象类概述
  - 抽象方法：并没有实现东西，而是为了规范子类的行为
  - 需要借助abc模块进行完成
    - abc模块调用语法
      - import abc
      
- 抽象类使用：
  - 抽象类可以包含抽象方法，也可以包含具体实现方法
  - 抽象类中也可以有成员属性和成员方法
  - 抽象类不允许直接实例化，都是通过子类实现
  - 必须通过继承才能使用，且继承的子类必须实现所有继承来的抽象方法
  - 假如子类没有完全实现抽象类带来的抽象方法，则子类也不能实例化
- 案例在 抽象类使用.py


12 . 自定义类
- 自定义类概述
  - 一个类其实就是各种方法和属性的自由组合
  - 可以定义类和函数，然后自己通过类直接赋值

- 自定义类定义的三种方法：
  - 可以借助MethodType实现
  - 借助type实现
  - 使用元类实现 - MetaClass
    - 元类是类
    - 备用来创造别的类
- 案例在 自定义类实现