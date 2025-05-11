# 中英对照表

| 英文术语                | 中文术语      | 简要说明或举例（如适用）                 |
| ----------------------- | ------------- | ---------------------------------------- |
| object                  | 对象          | 类创建的实例，例如：`MyClass obj;`       |
| class                   | 类            | 用于定义对象的模板                       |
| abstraction             | 抽象          | 提取对象的共性，隐藏细节                 |
| encapsulation           | 封装          | 将数据和方法绑定到一个类中，限制外部访问 |
| inheritance             | 继承          | 子类继承父类的成员                       |
| polymorphism            | 多态性        | 相同接口，不同行为；如虚函数             |
| composition             | 组合          | 一个类中包含另一个类对象                 |
| derivation              | 派生          | 从已有类创建新类，派生类 = 子类          |
| subclass                | 子类          | 派生类（继承自基类）                     |
| superclass / base class | 父类 / 基类   | 被继承的类                               |
| constructor             | 构造函数      | 创建对象时自动调用的函数                 |
| destructor              | 析构函数      | 销毁对象时自动调用，释放资源             |
| initialization          | 初始化        | 给变量赋初始值                           |
| cleanup                 | 清除          | 通常在析构函数中进行资源释放             |
| overloading             | 重载          | 同名函数/运算符，参数不同                |
| overriding              | 重写          | 子类重新定义父类的虚函数                 |
| constants               | 常量          | `const int x = 5;`，不可被修改           |
| constant function       | 常量成员函数  | `int get() const;`，不能修改成员变量     |
| inline                  | 内联          | `inline` 关键字，减少函数调用开销        |
| references              | 引用          | `int& ref = a;`，变量别名                |
| pointer                 | 指针          | `int* p = &a;`，存储地址                 |
| template                | 模板          | 泛型编程，如 `template<typename T>`      |
| variables               | 变量          | 存储数据的命名空间                       |
| assignment              | 赋值          | `a = 5;`                                 |
| array element           | 数组元素      | `arr[0]` 是数组的一个元素                |
| access                  | 访问          | 使用成员或变量，如 `obj.a`               |
| declaration             | 声明          | `static int a;`，说明变量存在            |
| definition              | 定义          | `int a = 5;`，分配内存                   |
| scope                   | 作用域        | 变量或函数的可见范围                     |
| namespace               | 命名空间      | 避免命名冲突，如 `std::cout`             |
| virtual                 | 虚拟          | `virtual void func();`，实现多态         |
| static                  | 静态          | 静态成员属于类而不是对象                 |
| dynamic                 | 动态          | 运行时行为，如动态内存 `new`, 动态多态   |
| multiple inheritance    | 多重继承      | 一个类继承多个基类                       |
| access specifier        | 访问限定符    | `public`, `private`, `protected`         |
| friend function         | 友元函数      | 非成员但能访问类私有数据                 |
| shallow copy            | 浅拷贝        | 仅复制指针地址（共享同一内存）           |
| deep copy               | 深拷贝        | 分配新内存并复制数据                     |
| this pointer            | this 指针     | 指向当前对象的指针                       |
| new/delete              | 动态分配/释放 | `new` 分配，`delete` 释放                |
| operator overloading    | 运算符重载    | 通过函数重载 `+`, `==` 等运算符          |











\1.                                                       
 关于const指针那些事![image-20250508142134671](https://cdn.jsdelivr.net/gh/SunJianBai/pictures@main/img/202505081421828.png)

\2.   面向对象的三个基本特征是封装、继承、和多态

\3.   (A) Inheritance  继承

(B) Polymorphism  多态

(C) overloading  重载

(D) Encapsulation 封装

\4. 类定义是，未声明private和public，默认是private

\5. const和引用都必须在定义的时候赋值

\6. 友元函数是非成员函数，

**友元函数的声明位置首先必须是在类中**，至于是在public,protected,private无所谓,**外界都可以直接调用**

友元函数的实现位置,也就是具体的定义(非声明)所在位置第1种方式(推荐):在宿主类中声明的同时直接提供定义。第二种：将宿主类用一个新的namespace框起来,然后在其他cpp文件中提供友元的定义,但是需要使用类似 myNameSpace::operator<<() 这样的命名空间限定符

\7. Const可修饰：函数参数不变、返回值不变、函数本身不修改类的数据成员

\8. 在以下三种情况下需要使用初始化成员列表：

情况一、需要初始化的数据成员是对象的情况(这里包含了继承情况下，通过显示调用父类的构造函数对父类数据成员进行初始化)；

情况二、需要初始化**const**修饰的类成员；

情况三、需要初始化**引用成员**数据；

9.

1.类里面的任何成员变量在定义时是不能初始化的。

2.一般的数据成员可以在构造函数中初始化。

3.**const****数据成员必须在构造函数的初始化列表中初始化。**

4.**static****要在类的定义外面初始化**。

5.数组成员是不能在初始化列表里初始化的。

6.不能给数组指定明显的初始化。

这6条一起，说明了一个问题：C++里面是不能定义常量数组的！因为3和5的矛盾。这个事情似乎说不过去啊？没有办法，我只好转而求助于静态数据成员。

到此，我的问题解决。但是我还想趁机复习一下C++类的初始化：

1.初始化列表：CSomeClass::CSomeClass() : x(0), y(1){}

2.类外初始化：int CSomeClass::myVar=3;

3.const常量定义必须初始化，C++类里面使用初始化列表;

4.C++类不能定义常量数组。

10.指针和引用的区别：

针和引用都是地址的概念，指针指向一块内存，它的内容是所指内存的地址；引用是某块内存的别名。

l 程序为指针变量分配内存区域，而不为引用分配内存区域。

l 指针使用时要在前加 * ，引用可以直接使用。

l 引用在定义时就被初始化，之后无法改变；指针可以发生改变。 即引用的对象不能改变，指针的对象可以改变。

l 没有空引用，但有空指针。这使得使用引用的代码效率比使用指针的更高。因为在使用引用之前不需要测试它的合法性。相反，指针则应该总是被测试，防止其为空。

l 对引用使用“sizeof”得到的是变量的大小，对指针使用“sizeof”得到的是变量的地址的大小。

l 理论上指针的级数没有限制，但引用只有一级。即不存在引用的引用，但可以有指针的指针。

l int **p //合法

l int &&p //非法

l ++引用与++指针的效果不一样。

l 例如就++操作而言，对引用的操作直接反应到所指向的对象，而不是改变指向；而对指针的操作，会使指针指向下一个对象，而不是改变所指对象的内容。

11.抽象类不可new子类可new（有纯虚函数的是抽象类）

\12. C++用虚函数实现动态多态性

13.所有类共用一个静态数据成员，静态成员函数只能访问静态数据成员

\14. 友元关系不能被继承，基类的友元对派生类没有特殊的访问权限

\15. 不能继承的东西：

​       ①构造函数和析构函数不能被继承

②operator= 也不能被继承，因为它完成类似于构造函数的活动。这就是 说，尽管我们知道如何由等号右边的对象初始化左边的对象的所有成员，但这并不意味着这个初始化在继承后仍有意义。

16.函数决定要素：参数类型表，返回类型，函数名称

17.父类可以引用子类，而子类不可以引用父类

18.虚继承才会有一个子类，否则有多个子类

19.“=”必须是成员函数

20.命名空间：

​       namespace加上作用域：

: : 全局作用域访问符

名字空间名称: : 名字空间作用域访问符

类: : 类作用域访问符

21.友元函数不能用const修饰





#  OOP(Cpp)考前复习

OOP：

- Encapsulation
- Inheritance
- Polymorphism

## Cpp syntax

### Compile

一张图看懂edit, compile, translate和link在从编写代码到程序执行这段时间所起的作用：![image-20250505163647208](https://cdn.jsdelivr.net/gh/SunJianBai/pictures@main/img/202505051636363.png)



**declaration**：向编译器引入变量

**definition**：给变量分配内存

declaration和definition既可以同步进行也可以先declaration再definition

#### Header Files

包含了外部的declaration

#### Linking

==Linker==会收集编译器产出的.obj和外部的libraries然后将其转化为可执行文件

只需告诉Linker .obj的的名字和可执行文件的名字，他就可以工作

<img src="https://cdn.jsdelivr.net/gh/SunJianBai/pictures@main/img/202505051636176.png" alt="image-20250505163658074" style="zoom:33%;" />

### 使用iostream、string、vector类

iostream类图：

<img src="https://cdn.jsdelivr.net/gh/SunJianBai/pictures@main/img/202505051637935.png" alt="image-20250505163706853" style="zoom:33%;" />

### C++中的C语法

函数、运算符、基本数据类型

#### Pointer 指针

指针应当在declaration时初始化它

如果想更改指针所指向的数据类型，要使用显式的类型转换

C++允许将一个`void*`类型的指针指向任意类型的数据，但不允许将任意类型的数据指向`void*`

#### Reference  引用

使用引用可以允许一个函数去修改外部的对象，如同指针那样

引用必须==初始化==，也就是说declaration和definition必须同时进行

初始化==永远不能为null==

##### const与reference

让一个函数参数变为一个const reference会允许这个函数在任何情况可用，比如：

- 若一个函数的参数为`int& a`，那么向这个函数直接传一个Constant是不合法的，只能传入一个变量；比如传入一个1，非法，传入一个const修饰过的变量，也非法
- 若一个函数的参数为`const int& a`，那么传常数和变量都是合法的

#### 指定存储位置

1. Global variables

   对于程序的所有部分都有效

2. Local variables

   自动是`auto`的

   使用`register`关键字可以提升对变量的访问速度，但不能用于全局或静态变量

3. Static variables

   被`static`修饰的变量只会初始化一次，并在多次函数的调用之间保存它的值（相当于Global?）

   比如说一个函数令static的变量i初始化为0，每次调用会使i++，那么得到的结果不会是每次都是1而是会不断增加

   但是static的变量在函数的作用域之外是无效的，也就是说会限制变量的作用域（函数的Global变量？）

4. Extern

   使用`extern`关键字可以告诉编译器一个变量存在，而在哪里definition的需要编译器等下再去找

   使用extern关键字还可以调用其他文件里的变量

   注意，使用extern关键字declaration变量的时候，不能同时definition赋值

5. Constants

   `const`修饰的变量不能被修改，也必须被初始化他的值

6. Volatile

   `volatile`修饰的变量可以在任何时候改变

#### 运算符





#### Dynamic storage allocations

使用`new/new[]`会返回一个指向后面对象类型的指针

使用`delete/delete[]`销毁动态的对象

带`[]`都是用于数组的

### Constants

==const默认与左边结合，如果左边没有东西则与右边结合==，如：

`const int* p`代表着p是指向整型的const指针

`const int * const p`代表着p是指向const整形的const指针

注意，const类型对象的值，不可能通过指向它的指针修改

#### Value substitution

一个常量必须要被初始化，并且不能被重新赋值

#### Pointers

如果一个指针被const修饰，那么不仅不能修改该指针指向的地点，也不能修改该指针指向的变量、数组、对象等等的值或字段

对于const修饰过的变量，必须要用const类型的指针才能拿到地址，且const必须修饰在类型前，比如：

```c++
const float f1 = 5.0;
float *const p1 = &f1; //error!
const float* p2 = &f1; //ok

float f2 = 1.0;
float *const p3 = &f2;//ok
float *const p4 = &f2;//ok
```

#### 函数参数与返回值

1. 如果传递给函数地址，使用const能确保这个地址不会被改变
2. 如果返回一个const类型的对象，那么返回的对象是不能被修改的

如果在函数类型中表明了const，那么既可以传入const值也可以传入非const值；而如果没有标注const，那么就无法传入const值

使用const值能避免client在拿到返回的地址后去修改值

#### Temporaries

在表达式中，compiler可能会创建临时的对象，他们都是const的

#### 成员函数后面加const

这个const修饰的是this指针，意思是这个函数不能修改该对象的任何字段

### Functions

#### 传递参数的方式

1. 值传递

2. 指针传递

3. 引用传递

   被调函数内对形参的操作就是对实参的操作

   如果被调函数只使用==实参的值==，而不改变实参，那么可以在形参前加const修饰

#### Function Pointer

**把函数也当作一个对象**

一旦函数被编译并且将被执行，他就会占据一块内存并且有一个地址

使用函数指针：

- `void (*funcPtr)()`，`funcPtr`是指向一个没有参数并且不返回值函数的==指针==
- `void* funcPtr()`，`funcPtr`是一个会返回`void*`的==函数==

#### Static Fuction

对于包含多个文件的程序，在全局函数前加static修饰可以限制函数的作用域为本文件

#### Inline Function

当一个函数**很短**但是需要被经常调用时，使用Inline Function可以大幅提高效率

内联函数不能包括迭代和switch，不能处理异常，也不能是递归的

所有在类中定义的函数都默认是inline的

如果所有函数都是内联函数，那么整个类都应该被放在头文件里

#### Default arguments

默认参数只能**从右向左**添加，比如：

- `int f(int,int = 0,char* = 0)`这是可以的
- `int g(int = 0,int,char* = 0)`是不可以的

默认参数可以是常量，也可以是表达式

默认参数在同一作用域内只能初始化一次

#### Placeholder arguments

可以不给函数的参数提供identifier，也就是不给他名字，但是这样也没办法用那个参数了

那么这个参数将纯纯用来占位

### Name Control

#### Static elements

1. static storage：static的object会在一片特殊的区域存储而不是在栈中，会等到程序结束时才被释放
2. static 还会控制一个name的visibility

如果一个static的对象没有被初始化，那么compiler会给它赋初值0；但是用户定义的类型必须用constructor初始化

#### Static object destructors

一个全局object的constructor一般在进入main函数之前就被调用

而函数中的static object只有在该函数被调用时constructor才被调用

#### Namespaces





### Template 泛型

从泛型生成一个类或一个函数的过程称为==instatiation==

<img src="imgs/image-20220513135157659.png" alt="image-20220513135157659" style="zoom: 33%;" />

#### 泛型语法

##### 泛型函数

```c++
template <typename T>
T max(T x,T y){
    return (x>y)?x:y;
}
max<int>(1,2);
```

T是type arguments，在函数被调用之前必须要用data类型来代替它

##### 泛型类

```c++
template <typename T>
class name{
    ...
}

name<type> n = name();
```

如果一个函数在template类的外面被定义，那么他也必须被定义为template函数

在创建一个template类的实例时，要规定它的data类型，比如：`name<int,char> n(1,'2');`





## Cpp class

怎么在代码中实现对象呢？使用 abstract data type -- `class`

`class`中包含 data elements 和 functionality分别用来刻画对象的 特征 与 行为`

### class基础

`class`与`struct`最大的区别是`class`的成员默认是`private`而`struct`的成员默认是`public`

`::`用于分析作用域，比如`classname::func()`意思是`func()`这个函数是`classname`类里的方法

==所有成员方法==都暗含了一个参数`this`，`this`是一个`classname*`类型的指针，指向这个对象

Object-Based和Object-oriented的最大区别在于==多态==

#### 存取控制——hiding implementation

1. 把接口与实现分离开
2. 使用public、private和protected关键词
3. 使用`friend`：在类之中==声明==一个friend function，注意friend function==不是成员函数==，但是friend function具有访问类中私有字段的权限。friend function不能被继承

#### 初始化和清除

##### Constructor

Constructor是一个与class名字相同的函数，没有返回值，通过重载来分辨不同的Constructor

在给一个对象分配空间的时候，Constructor被自动调用。也可以手动调用

###### copy constructor

```cpp
int a = 5;
int b = 1;	//copy constructor

X first(1,2,3);
X second = first;  //copy constructor
```

声明初始化：

设类名为X，声明构造函数`X(const X& x)`即为copy constructor

copy constructor在何时被调用？

- 用值传递参数
- 函数返回一个object值
- 使用已有object传递新object
- 使用引用传递参数时==不会调用==

###### 转换构造函数

当构造函数具有一个参数或者从第二个参数开始都具有默认值，那么这个构造函数会自动把第一个参数转换成当前类的类型

###### 初始化列表

形如此的构造函数：

```c++
class Data{
 	int a;
public:
    Data(int ra):a(ra){}
};
```

const数据成员、引用型数据成员、类类型成员的初始化操作必须成员初始化列表中进行

##### Destructor

Destructor是一个名字为"~"加上class名字的函数，没有返回值。destructor不能被重载且没有正式的参数

Destructor会在一个对象被销毁时自动调用

#### class修饰

##### Static Data Members

被static修饰的字段被该类的==所有object所共享==

声明为static的data必须被初始化，但是在初始化时不需要加static关键字

因为consts和引用必须被初始化，所以含有上述两者的类必须要写构造函数

##### Static member funtions

静态成员函数只能访问static data member，不能是virtual函数，也没有this指针

##### Const Member Functions

在函数名和()之后添加const会使函数变为const member function

const member funtion不能修改类的data member，除非这个字段被==mutable==修饰过

##### Const objects

const修饰的对象只能调用const修饰的成员函数，不能调用非const的

##### volatile

#### 指向数据成员或成员函数的指针

使用`::*`定义这些指针

使用`->*`或`.*`来使用这些指针

##### 指向data字段的指针

```cpp
Data d;
Data* dp = &d;
//定义指向Data中a字段的指针pm
int Data::*pm = &Data::a;	//主要看这两行
dp->*pm = 47;
//将pm指向的内容改为b字段
pm = &Data::b;
d.*pm = 48;
```

##### 指向成员函数的指针

```cpp
Widget w;
Widget* wp = &w;
//定义成员函数指针
void (Widget::*pmem)(int) const = &Widget::h;
(w.*pmem)(1);
(wp->*pmem)(2);
```

#### 运算符重载

运算符重载是调用函数的另一种方式

##### 成员函数重载

普通的运算符重载已经比较熟悉，不过多介绍

##### 使用友元的运算符重载

没有隐式的this，所以相比于成员函数，必须要有显式的对象在函数的参数中

##### 选用成员函数还是友元？

1. 如果第一个操作数是一个类的对象，应当使用成员函数；否则使用友元
2. 所有的一元运算符和=,(),[],->,->*,+=,-=,/=,\*=,^=,&=,|=,%=,>>=,<<=都应使用成员函数，其他的用友元

##### 其他注意事项

1. ->运算符的返回值必须是一个指针 
2. 自增(++)和自减(--)运算符都可以用于前缀或者后缀运算符，所以要重载这俩运算符，都需要两个函数Prefix: `type operator++()`     Postfix: `type operator--(int)`
   注意后缀中的int并不是真实的参数，只是用来==占位==以区分前缀和后缀运算符
3. 关于赋值运算符"="：如果在declaration的同时调用=，那么被调用的则是copy constructor；如果是先declaration，后来再赋值，那么调用的是=的重载
4. 当一个类有指针类型的字段时，一定要定义它的copy constructor和=运算符重载，否则可能会出现同一个地址被释放两次等异常状况
5. 类型转换重载：`type operatorT()`，转换类型type到T
6. inserter<<和extractor>>，重载这两个运算符以用于标准化输出，第一个参数是ostream或istream

#### 动态object创建

当一个object被创建时，会发生两件事：

1. 分配存储空间：static storage area, stack, heap(动态内存分配)
2. 调用constructor

如果要动态创建，要用到new和new[]，删除则是delete和delete[]



### Inheritance & Composition

#### syntax

Composition：在一个新的类中创建已有的类的object

继承的基础都比较了解了，不再多说

#### Constructor initializer list

constructor和destructor是不会被继承的，赋值运算符也不会被继承

当创建一个派生类时，下列objects可能被创建：基类、成员类和派生类自己。

一般先创建基类，然后按照构造类中声明的顺序创建成员类，最后创建派生类

#### Name hiding

子类的成员函数名与基类相同，称为`Redefine`

在派生类中的成员函数名字与基类中相同时，会自动隐藏基类的函数

如果redefine了一个static成员函数，那么所有基类中的重载函数都会被隐藏

#### 选择inheritance和composition

如果要使用基类的接口，那就用inheritance；如果只是想用一个类的特性，那用composition

#### Access Control

Access specifier：public, private, protected

不管用什么修饰，派生类都无法直接访问到基类的private成员，private成员只能被同一类的成员函数或友元访问

##### public

基类成员的访问属性在派生类中保持不变

**同名屏蔽**：如果派生类redefine了与基类中同名的函数，那么所有基类的同名函数都会被屏蔽

**向上类型转换**：通过public继承，派生类获得了基类中除构造函数、析构函数、复制韩式以外的所有成员，这样公有派生类就具备了基类的功能，在需要基类的地方可以用派生类代替

##### private

基类成员的访问属性在派生类中全部变为private

##### protected

基类成员的访问属性在派生类中全部变为private

#### Constructor&Destructor

派生类的构造函数要在==初始化列表==中对基类数据成员初始化

==顺序==为：先按继承顺序调用基类的构造函数，再按照成员在派生类中声明的顺序进行初始化

析构的顺序与上面相反

#### 继承中的运算符重载

除了赋值操作符，运算符全都会自动被派生类继承

#### Multiple inheritance

一个派生类可以有多个直接的基类

#### Incremental development（增量开发）

增量开放可以让我们加入新的代码但是不造成bug

#### Ambiguity

一个类可能作为派生类的基类不止一次；不同的基类可能有相同的成员函数名

解决方法：

1. 使用`::`限定作用域或者定义一个新函数
2. 直接在派生类中定义一个新的成员函数
3. 在继承时使用`virtual`修饰基类



### Polymorphism & Virtual Functions

#### Upcasting

当使用==引用或者指针==操纵object时，派生类的object能表现出基类的特性，也就是说派生类是基类的一种。这点在多态中十分重要

如果没有用引用或者指针而是直接用了派生类object的值，就会出现object slicing

#### Virtual Functions

```c++
virtual type func(arguments);
```

虚函数是==nonstatic==的成员函数，且`virtual`只许在声明处写

如果一个函数在基类中就被声明为虚函数，那么他在所有派生类中都是虚函数

constructor不能是虚函数，destructor可以是虚函数并且往往是虚函数

对于虚函数的redefinition被称为overriding

如果在派生类中，基类的虚函数没有被重写，那么就会调用“最近”的函数

要实现多态，需要：

1. 派生类public继承基类
2. 被调用的成员函数必须是虚函数
3. 通过**引用或指针**操纵object

#### Abstract base classes & Pure virtual functions

Abstract base class至少要有一个pure virtual function

一个pure abstract base class只有pure virtual function

抽象类不能实例化，也就是不能创建它的对象

pure virtual function要在函数声明后面加'=0'，如：`virtual void func()=0;`，纯虚函数没有函数体

所有的pure virtual function在子类都应该被重写

#### Object slicing

如果没有用引用或者指针而是直接用了派生类object的值，就会出现object slicing：意思就是会把一个派生类的对象“切成”基类对象，只留下与基类object相同的部分
