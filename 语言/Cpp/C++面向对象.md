## const

**作用**

1. 修饰变量，说明该变量不可被改变
2. 修饰指针，有两种，一种是指向常量的指针(pointer to const)，另一种是自身是常量的指针(const pointer)
3. 修饰引用，指向常量的引用（reference to const），用于形参类型，及避免拷贝，又避免函数对值进行修改。
4. 修饰成员函数，说明该成员函数不能修改成员变量。

**const的指针和引用**

- 指针
  - 指向常量的指针（pointer to const）
  - 自身是常量的指针（常量指针，const pointer）
- 引用
  - 指向常量的引用（reference to const）
  - 没有 const reference，因为引用本身就是 const pointer

### 修饰变量，指针

| 声明                      | 含义说明                                         |
| ------------------------- | ------------------------------------------------ |
| `double* ptr`             | 普通指针，可改地址，也可改指向的值               |
| `const double* ptr`       | 指向常量，**不能改值**，可以改地址               |
| `double* const ptr`       | 常量指针，**不能改地址**，可以改值               |
| `const double* const ptr` | 指向常量的常量指针，**既不能改值，也不能改地址** |



### 修饰成员函数

```cpp
class A {
public:
    int x;
    int getX() const;  // const 成员函数
};
```

带有 `const` 的成员函数表示：

> **该函数承诺不修改当前对象的成员变量（除了 mutable 修饰的）。**

❗特点

- 可以访问成员变量，但**不能修改**它们。
- **只能调用其他的 const 成员函数**。

### 修饰对象

```cpp
const A obj(10);
```

这个 `obj` 是一个常量对象，意思是：

- **不能修改其成员变量（包括通过成员函数）**。
- **只能调用 const 成员函数**。

|                        | 普通对象 (`A obj`) | 常量对象 (`const A obj`) |
| ---------------------- | ------------------ | ------------------------ |
| 调用 const 成员函数    | ✅ 允许             | ✅ 允许                   |
| 调用 非-const 成员函数 | ✅ 允许             | ❌ 不允许（编译错误）     |

`mutable` 修饰的成员变量可以在 const 成员函数中被修改。



```cpp
const int& getValue() const;  // 返回 const 引用，避免被修改
```

和成员函数是否 `const` 是两回事，`const` 在不同位置有不同含义：

- **函数后面的 const**：修饰的是 this，表示函数不修改成员。
- **返回值前面的 const**：修饰的是返回值本身，不允许修改它。





## 内存分区模型

C++ 在执行时将内存大方向划分为四个区域：

### 程序执行前

#### 代码区

- 存放 CPU 执行的机器指令，由操作系统进行管理。
- 代码区是共享的，可以被反复执行。
- 代码区是只读的，防止程序意外修改指令。

#### 全局区（静态存储区） -> 

- 存放全局变量和静态变量（函数体外的变量是全局变量）。
- 包含常量区，字符串常量和其他常量（包括 `const` 修饰的变量）。
- 该区域的数据在程序结束后由操作系统释放。

### 程序执行后

#### 栈区
- 由编译器自动分配和释放，存放函数的参数值、局部变量等。
- **注意**：不要在函数内部返回局部变量的地址，栈区开辟的数据由编译器自动释放。

#### 堆区

- 由程序员分配和释放，若程序员不释放，程序结束时由操作系统回收。
- 意义：不同区域存放的数据，赋予不同的生命周期，给我们更大的灵活性。
- 利用 `new` 关键字可以将数据开辟到堆区：
  ```cpp
  int* p = new int(10);  // 用指针保存位置  新创建的对象是一个指针，指针本质也是局部变量，存放在栈区，而指针所指向的数据存放在堆区。

### malloc

在c当中，malloc/free函数的底层是通过`mmap` , `munmap`以及`sbrk`函数来进行内存的分配和释放的。

当malloc小于128k的内存时，会使用sbrk来分配内存，这个128k是可以由用户设置的。其中sbrk函数通过将内核的brk指针增加来扩展和收缩堆。

并且如果brk指针内已经有足够大小的已释放空间，则可以直接使用这片内存空间而不用重新分配。

当malloc大于128k的内存时，会使用mmap在堆和栈之间寻找一块空闲的内存来进行分配，并且通常会分配一个比用户申请内存空间更大，目的是为了减少后续申请中向操作系统申请内存的次数。并且用mmap分配的内存都会直接与物理地址建立映射，**会发生大量的缺页中断**。

malloc是由c函数库实现的，跟os无关。sbrk和mmap是系统调用**由此会带来内存碎片的问题**



###  `new` 操作符

new申请内存时无需指定内存块大小，编译器会根据类型信息计算，而malloc需要显示指定大小

- 利用 `delete` 释放内存。
  - 创建语法：
    ```cpp
    int* p = new int(10);
    ```
    `new` 返回的数据类型是指针，不会自动释放内存。
  - 释放语法：
    ```cpp
    delete p;
    ```
    释放后再次访问即为非法操作。

- 在堆区利用 `new` 开辟数组：
  - 语法：
    ```cpp
    int* p = new int[10];
    ```
  - 释放：
    ```cpp
    delete[] p;  // 数组时要加上中括号
    ```

##  引用&

### 引用的本质
- 引用是给变量起别名，通过不同的变量名来操作同一块内存（两个变量的地址相同）。引用本质上是一个指针常量。
- 语法：
  ```cpp
  数据类型& 别名 = 原名;
  ```

### 引用的注意事项
1. 引用必须初始化，不能先创建后引用。
2. 引用一旦初始化后不能更改。

### 引用传递
- 引用作为函数参数，利用引用使形参修饰实参，简化指针修改实参：
  ```cpp
  int swap(int &a, int &b) {
      // 交换操作
  }
  ```

### 引用作为函数返回值
```cpp
int& func() {
    static int a = 10;
    return a;
}
int &b = func();  // 直接使用引用作为返回值
```
- 函数调用可以作为左值：
  ```cpp
  func() = 100;  // 直接给函数返回值赋值
  ```

### 常量引用

- 使用 `const` 修饰形参，防止误操作。加入 `const` 后，编译器将代码修改为：
  ```cpp
  int temp = 10;
  const int& a = temp;  // 引用了一块临时的空间
  ```

## 函数function

###  函数默认参数

- 函数形参可以有默认值，调用时如果不传值则使用默认值。
- 注意：
  - 如果某个位置有了默认值，从此位置开始从左到右的所有参数都必须有默认值。
  - 如果函数声明有默认参数，函数的实现中不能再有默认值。
  

###  函数占位参数

- 只写数据类型，不写形参变量名，占位参数可以有默认值。

### 函数重载

- 函数名可以相同，增加代码复用性，依据参数`类型`、`个数`或`顺序`的不同，调用不同的函数。
- 注意：
  1. 引用作为重载的条件：`int&` 和 `const int&` 是不同类型。
  2. 函数重载可能会遇到二义性，避免重载函数中包含默认参数。

## 类和对象

C++ 面向对象的三大特性：封装、继承、多态。

### 封装

- 将属性和行为作为一个整体，并对其进行权限控制：
  1. **公共权限** (`public`)：类内外都可以访问。
  2. **保护权限** (`protected`)：类内可以访问，类外不可以访问，子类可以访问父类内容。
  3. **私有权限** (`private`)：类内可以访问，类外不可以访问，子类无法访问父类的私有成员。

```cpp
class Circle {
public:
    int m_r;
    double zhouchang() {
        return 2 * 3.14 * m_r;
    }
private:
    // 私有成员
};
```

#### `struct` 和 `class` 的区别
- `struct` 默认权限是公共 (`public`)，`class` 默认权限是私有 (`private`)。

#### 类外调用类内对象时要表明作用域。



### 对象的初始化和清理

#### 构造函数

- 主要作用是创建对象时为对象的成员属性赋值。
- 无返回值，不写 `void`。
- 构造函数名称与类名相同。
- 可以重载，有参构造、无参构造和拷贝构造。
-  程序在调用对象时候由编译器自动调用，无需手动调用。

构造函数的分类：无参构造（默认构造）；有参构造；

有参构造可以使用初始化列表来构造

> 对于 const、引用 或类成员对象，必须用初始化列表。

```cpp
class ClassName {
    int x;
    const int y;
    int& ref;

public:
    ClassName(int a, int b, int& r) : x(a), y(b), ref(r) {
        // 构造函数体（可以为空）
    }
};

```



#### 普通构造

拷贝构造用引用的方式传入函数，将传入的人身上的所有属性拷贝到我身上。

**调用方法**

#####  括号法  （比较常用）

> 类名 类变量名；   //默认构造

> 类名 类变量名（函数参数）//有参构造函数

> 类名 类变量名（要拷贝的类变量名） //拷贝构造函数

注意：调用默认构造函数时 不要加（），因为编译器会认为这是函数声明。

#####  显示法

> 类名 类变量名 = 类名（参数）； //有参构造函数，右侧是一个匿名对象，操作结束后系统自动回收。

> 类名 类变量名 = 类名（要拷贝的类变量名）； //拷贝构造函数

注意：不要利用拷贝构造函数，来初始化匿名对象。编译器会认为这是一个对象声明，`person （p3）`等价于 ` person p3`;

#####  **隐式转换法**

> 类名 类变量名 = 参数；  //有参构造函数

> 类名 类变量名 = 要拷贝的类变量名；  //拷贝构造函数

省略了类名

 **拷贝构造函数的调用时机**

使用一个已经创建的对象来初始化一个新对象

值传递的方式给函数参数传值

以值方式返回局部变量

创建方法：

> 类名 （const 类名&变量名）{函数体；}





#### 析构函数

 对象销毁前系统自动调用，执行一些清理工作。

> ~类名（）{ }

1. 没有返回值也不写void。

2. 函数名称与类名相同，在名称前加上~  

3. 析构函数不可以有参数，因此不可以发生重载

4. 自行调用，而且只会调用一次

作用：将堆区开辟的数据做释放操作。如果用new在堆区开辟内存，则要在析构函数中用delete手动释放内存。

#### 深拷贝与浅拷贝

- **浅拷贝**：简单的赋值拷贝，编译器默认的。如果浅拷贝可能会造成堆区内存重复释放，
- **深拷贝**：通过手动实现拷贝构造函数，避免浅拷贝造成内存泄漏。在堆区重新申请空间，进行拷贝操作,通过自己实现拷贝构造函数，来进行深拷贝 

#### 初始化列表

- 传统初始化：在构造函数体内进行。

- 初始化列表：构造函数初始化时通过列表直接初始化类成员。

- 语法：

  > 构造函数（数据类型 值1，数据类型 值2……）：类变量1（值1），类变量2（值2）……{ }

  注意冒号的位置



#### 初始化列表的类对象

1. `const`修饰的成员变量：

   ​	如果在类中直接定义const成员变量，会报错。

   ```cpp
   class Myclass{
   public:
       const int value = 10; //错误：不能直接初始化，要在构造函数中进行初始化
   };
   ```

   

2. `引用`成员变量

   ​	引用成员变量必须在对象创建时绑定到一个有效的对象上，并且不能重复绑定

   ```cpp
   class Myclass{
       public:
       int& ref;
       
       Myclass(int& r) : ref(r) {}
   };
   ```

   

3. 动态分配的资源

   ```cpp
   #includ
   class Mycalss{
     public:
       
   };
   ```

   

### **类对象作为类成员**

类中的成员可以是另外一个类的对象，该对象为对象成员

当出现这种情况时，构造时先构造对象，再构造类本身。

析构的顺序和构造的顺序相反

### 静态成员static

1. 修饰普通变量，修改变量的存储区域和生命周期，变量存储在静态区，在main函数运行时就已经分配了空间，如果有初始值就用初始值初始化，如果没有则用默认值初始化。

2. 修饰普通函数，表明函数的作用范围，仅在定义该函数的文件内才能使用。在多人开发项目时为了防止与他人命名空间里的函数重名，可以将函数定义成static。
3. 修饰成员变量，该类的所有对象实例只保存一个该变量，而且不需要生成对象就可以访问该成员。
4. 修饰成员函数，使得不需要生成对象就可以访问该函数，在静态成员函数中只能访问静态成员变量。

#### 静态成员变量

在成员函数和成员变量前加上关键字`static`，称为静态成员

- 所有对象共享同一份数据，在编译阶段分配内存。
- **类内声明，类外初始化。**（不能在类内初始化，也不能在类的构造函数中初始化）

``` cpp
class person{
    public:
        static int m_a;  //类内声明
}

int person：：m_a = 10； //类外初始化
```

静态成员变量不属于某个对象，所有对象共享同一份数据。

访问方式：person::m_a  通过类名访问

Ø 静态成员变量和静态成员函数也是有访问权限的。



#### static的初始化顺序

在类外的static变量的初始化顺序是根据其在编译单元（.cpp）中声明的顺序初始化的，但是不同编译单元之间的静态变量的初始化顺序是不确定的。

可以通过延迟初始化的方式来控制静态变量的初始化顺序。

类内部的static成员变量的初始化顺序根据其**初始化语句的先后顺序**确定，而不是根据声明的顺序确定。



#### 静态成员函数

- 所有对象共享同一个函数，只能访问静态成员变量。

  

###  对象模型和 `this` 指针

#### 类内的成员变量和成员函数分开存储

- C++ 中，类的成员变量和成员函数分别存储。成员变量通常存储在对象的内存中，而成员函数存储在程序的代码区中（即共享内存区域）。
- 只有非静态成员变量才属于类的对象上（即每个对象都会有自己的成员变量副本）。静态成员变量属于类本身，而不是某个特定对象。

#### 空对象占用的字节

- 空对象占用 1 字节，因为 C++ 编译器会给每个空对象分配一个字节的空间，以区分空对象在内存中的位置。即使对象没有成员变量，仍然会占用最少的内存空间。
- 可以通过 `sizeof()` 来计算对象所占用的内存空间。`sizeof()` 计算的是对象的总大小，包括成员变量、内存对齐等。

 示例：

```cpp
class Empty {
    // 没有成员变量
};

int main() {
    Empty e;
    cout << sizeof(e) << endl;  // 输出 1
    return 0;
}
```

#### `this` 指针

- `this` 指针是 C++ 中的一个特殊指针，它指向调用成员函数的对象。
- 每个对象在调用成员函数时，编译器会自动将该对象的地址作为 `this` 指针传递给成员函数。`this` 是一个常量指针，不能修改它指向的对象。
- 友元函数没有 `this` 指针，因为它们不是类的成员函数。

 `this` 指针的用途

1. **解决成员变量与函数参数名称冲突**：可以通过 `this->` 来区分成员变量和函数参数。
2. **返回对象本身**：通过 `*this` 解引用返回当前对象的引用，通常用于实现链式调用。

 示例：

```cpp
class Person {
public:
    int age;

    // 通过返回 *this 来支持链式调用
    Person& addAge(int years) {
        this->age += years;
        return *this;  // 返回对象本身
    }
};

int main() {
    Person p;
    p.age = 20;
    p.addAge(5).addAge(3);  // 链式调用
    cout << p.age << endl;  // 输出 28
    return 0;
}
```

#### 空指针调用成员函数

- 空指针（`NULL` 或 `nullptr`）可以调用成员函数，但在访问成员函数时，程序会崩溃。
- 为了避免空指针引用错误，可以在成员函数内部添加空指针检查。

 示例：

```cpp
class Person {
public:
    int age;

    void printAge() {
        if (this == nullptr) {
            return;  // 防止空指针调用
        }
        cout << "Age: " << age << endl;
    }
};

int main() {
    Person* p = nullptr;
    p->printAge();  // 安全处理，避免崩溃
    return 0;
}
```

#### `const` 修饰成员函数

- **常函数**（`const` 成员函数）：在成员函数的后面加上 `const`，表明该函数不会修改类的成员变量。
- 在常函数中，不能修改成员变量，但可以访问 `mutable` 修饰的成员变量。

 示例：

```cpp
class Person {
public:
    mutable int age;

    void setAge(int a) const {  // 常函数
        age = a;  // `mutable` 允许修改成员
    }
};

int main() {
    const Person p;
    p.setAge(25);  // 调用常函数
    cout << p.age << endl;  // 输出 25
    return 0;
}
```

###  友元

#### 友元函数

- 通过 `friend` 关键词，可以让类外的函数访问类的私有成员。通常用于访问类的内部数据，尤其是操作类对象时。
- 友元函数不会被继承，因为友元函数不是目标类的函数

##### 示例：全局函数作友元

```cpp
class Building {
    friend void printBedroom(Building& b);  // 友元函数声明
private:
    string m_Bedroom;
public:
    Building() : m_Bedroom("Master Bedroom") {}
};

void printBedroom(Building& b) {
    cout << "Bedroom: " << b.m_Bedroom << endl;
}

int main() {
    Building b;
    printBedroom(b);  // 通过友元函数访问私有成员
    return 0;
}
```

#### 友元类

- 可以将一个类声明为另一个类的友元类，使得友元类能够访问该类的私有成员。

##### 示例：类作友元

```cpp
class Building {
    friend class GoodFriend;  // 友元类声明
private:
    string m_Bedroom;
public:
    Building() : m_Bedroom("Master Bedroom") {}
};

class GoodFriend {
public:
    void showBedroom(Building& b) {
        cout << "Bedroom: " << b.m_Bedroom << endl;
    }
};

int main() {
    Building b;
    GoodFriend gf;
    gf.showBedroom(b);  // 通过友元类访问私有成员
    return 0;
}
```

#### 友元函数作为成员函数

- 可以指定某个类的成员函数作为另一个类的友元函数，使得该函数可以访问类的私有成员。

##### 示例：成员函数作友元

```cpp
class Building {
    friend void GoodFriend::visit(Building& b);  // 友元函数声明
private:
    string m_Bedroom;
public:
    Building() : m_Bedroom("Master Bedroom") {}
};

class GoodFriend {
public:
    void visit(Building& b) {
        cout << "Visiting Bedroom: " << b.m_Bedroom << endl;
    }
};

int main() {
    Building b;
    GoodFriend gf;
    gf.visit(b);  // 通过友元函数访问私有成员
    return 0;
}
```

###  运算符重载

运算符重载允许我们为已有的运算符定义新的行为，使其适应新的数据类型。这样可以使代码更加简洁和易于理解。

#### 常见的运算符重载

1. **算术运算符**：`+`, `-`, `*`, `/`, `%`
2. **关系运算符**：`==`, `!=`, `<`, `>`, `<=`, `>=`
3. **逻辑运算符**：`&&`, `||`, `!`
4. **自增自减运算符**：`++`, `--`
5. **赋值运算符**：`=`, `+=`, `-=`
6. **输入输出运算符**：`<<`, `>>`

#### 1. 重载 `+` 运算符

通过运算符重载，可以简化对象之间的加法操作。

##### 示例：成员函数重载 `+` 运算符

```cpp
class Person {
public:
    int age;
    Person operator+ (const Person& p) {  // 运算符重载
        Person temp;
        temp.age = this->age + p.age;
        return temp;
    }
};

int main() {
    Person p1, p2, p3;
    p1.age = 10;
    p2.age = 20;
    p3 = p1 + p2;  // 使用重载的 + 运算符
    cout << p3.age << endl;  // 输出 30
    return 0;
}
```

##### 示例：全局函数重载 `+` 运算符

```cpp
class Person {
public:
    int age;
};

Person operator+ (const Person& p1, const Person& p2) {
    Person temp;
    temp.age = p1.age + p2.age;
    return temp;
}

int main() {
    Person p1, p2, p3;
    p1.age = 10;
    p2.age = 20;
    p3 = p1 + p2;  // 使用重载的 + 运算符
    cout << p3.age << endl;  // 输出 30
    return 0;
}
```

#### 2. 重载输入输出运算符 (`<<`, `>>`)

- 通过重载 `<<` 运算符，可以自定义输出类型的方式，使得可以使用 `cout` 输出自定义类的对象。
- 通过重载 `>>` 运算符，可以自定义输入类型的方式，使得可以使用 `cin` 输入自定义类的对象。

##### 示例：重载 `<<` 运算符

```cpp
class Person {
public:
    int age;
    friend ostream& operator<<(ostream& os, const Person& p) {
        os << "Age: " << p.age;
        return os;
    }
};

int main() {
    Person p;
    p.age = 25;
    cout << p << endl;  // 输出
    return 0;
}
```

#### 3. 重载自增运算符 (`++`)

- 重载自增运算符可以是前置自增或后置自增。前置自增返回对象本身，后置自增返回对象的副本。

##### 示例：重载自增运算符

```cpp
class MyInteger {
public:
    int num;

    MyInteger() : num(0) {}

    MyInteger& operator++() {  // 前置自增
        num++;
        return *this;
    }

    MyInteger operator++(int) {  // 后置自增
        MyInteger temp = *this;
        num++;
        return temp;
    }
};

int main() {
    MyInteger m;
    ++m;  // 前置自增
    cout << m.num << endl;  // 输出 1

    m++;  // 后置自增
    cout << m.num << endl;  // 输出 2

    return 0;
}
```

#### 4. 重载赋值运算符 (`=`)

- 默认情况下，编译器提供浅拷贝的赋值运算符，适用于简单类型。但对于涉及动态内存管理的类，需要手动重载赋值运算符进行深拷贝。

##### 示例：重载赋值运算符

```cpp
class Person {
public:
    int* age;

    Person(int a) {
        age = new int(a);
    }

    // 赋值运算符重载（深拷贝）
    Person& operator=(const Person& p) {
        if (this == &p) return *this;  // 防止自赋值

        delete age;  // 释放原有内存
        age = new int(*p.age);  // 进行深拷贝
        return *this;
    }

    ~Person() {
        delete age;  // 释放内存
    }
};

int main() {
    Person p1(25);
    Person p2(30);
    p2 = p1;  // 使用重载的赋值运算符进行深拷贝
    cout << *p2.age << endl;  // 输出 25
    return 0;
}
```

#### 运算符重载的注意事项：

- 重载运算符时需要保持运算符的语义一致性。
- 不要滥用运算符重载，尤其是对于内置数据类型的运算符，避免混淆程序的逻辑。







## 继承

### **继承的概念**

**继承**是面向对象编程的三大核心特性之一（封装、继承、多态），允许子类（派生类）继承父类（基类）的成员变量和成员函数，实现代码复用和扩展。

#### 核心概念：

- **基类（Base Class）**：被继承的类。
- **派生类（Derived Class）**：继承基类的类。
- **继承类型**：`public`、`protected`、`private`，决定基类成员在派生类中的访问权限。

| 成员类型                      | 是否被继承       | 说明                                                     |
| ----------------------------- | ---------------- | -------------------------------------------------------- |
| **构造函数 (Constructor)**    | ❌ 否             | 不会自动继承，但可用 `using Base::Base;` 显式引入        |
| **析构函数 (Destructor)**     | ✅ 是             | 会继承，用于支持多态删除，建议定义为虚函数               |
| **拷贝构造函数**              | ❌ 否             | 不继承，需派生类自行定义                                 |
| **赋值运算符函数**            | ❌ 否             | 不继承，需派生类自行定义                                 |
| **普通成员函数**              | ✅ 是             | 会继承，若有重名会被覆盖                                 |
| **虚函数 (virtual function)** | ✅ 是             | 支持多态，派生类可 override                              |
| **const 成员函数**            | ✅ 是             | 是成员函数的一种修饰形式，会继承                         |
| **静态成员函数**              | ✅ 是             | 属于类范围，也会被派生类访问到                           |
| **数据成员 (成员变量)**       | ✅ 是             | 会继承，但若为 `private` 无法直接访问                    |
| **静态成员变量**              | ✅ 是             | 属于类，不随对象复制，可通过类名或对象访问               |
| **友元函数 (friend)**         | ❌ 否             | 不是成员函数，不能继承，且不会自动拥有对派生类的访问权限 |
| **私有成员 (private)**        | ✅ 是（不可访问） | 虽然被继承，但在派生类中不能访问                         |
| **保护成员 (protected)**      | ✅ 是             | 被继承，派生类中可以访问                                 |
| **公有成员 (public)**         | ✅ 是             | 被继承，派生类中可以访问                                 |
| **运算符重载函数**            | ✅ 是             | 若为成员函数，也会被继承（但需注意是否被重载）           |
| **模板成员函数**              | ✅ 是             | 作为普通成员函数模板，亦会被继承                         |
| **类型别名 (typedef/using)**  | ✅ 是             | 可被继承和访问                                           |

---

### **继承类型**

####  **公有继承（public）**

- **规则**：
  
  - 基类的 `public` 成员 → 派生类的 `public` 成员。
  - 基类的 `protected` 成员 → 派生类的 `protected` 成员。
  - 基类的 `private` 成员 → **不可直接访问**（需通过基类的公有/保护方法）。
- **语法**：
  ```cpp
  class Derived : public Base {
      // ...
  };
  ```

#### **保护继承（protected）**

- **规则**：
  - 基类的 `public` 和 `protected` 成员 → 派生类的 `protected` 成员。
  - 基类的 `private` 成员 → **不可直接访问**。
- **语法**：
  ```cpp
  class Derived : protected Base {
      // ...
  };
  ```

####  **私有继承（private）**

- **规则**：
  - 基类的 `public` 和 `protected` 成员 → 派生类的 `private` 成员。
  - 基类的 `private` 成员 → **不可直接访问**。
- **语法**：
  ```cpp
  class Derived : private Base {
      // ...
  };
  ```

#### 4. **访问权限表**
| 基类成员访问权限 | 公有继承     | 保护继承     | 私有继承     |
| ---------------- | ------------ | ------------ | ------------ |
| `public`         | `public`     | `protected`  | `private`    |
| `protected`      | `protected`  | `protected`  | `private`    |
| `private`        | 不可直接访问 | 不可直接访问 | 不可直接访问 |

---

### **继承方式**

####  **单继承**

- 一个派生类只继承一个基类。
- **示例**：
  ```cpp
  class Animal {
  public:
      void eat() { cout << "Eating..." << endl; }
  };
  
  class Dog : public Animal {
  public:
      void bark() { cout << "Barking..." << endl; }
  };
  
  Dog dog;
  dog.eat();   // 继承自 Animal
  dog.bark();
  ```

####  **多重继承**

- 一个派生类继承多个基类。
- **语法**：
  ```cpp
  class Derived : public Base1, protected Base2, private Base3 {
      // ...
  };
  ```
- **示例**：
  ```cpp
  class Student {
  public:
      void study() { /* ... */ }
  };
  
  class Employee {
  public:
      void work() { /* ... */ }
  };
  
  class TeachingAssistant : public Student, public Employee {
      // 可以访问 study() 和 work()
  };
  ```

####  **菱形继承（钻石问题）**

- 问题描述：多个派生类继承同一个基类，最终派生类包含重复的基类成员。
- **解决方法**：使用**虚继承**（Virtual Inheritance）。
- **示例**：
  
  ```cpp
  class Person {
  public:
      string name;
  };
  
  class Student : virtual public Person {};
  class Employee : virtual public Person {};
  
  class TeachingAssistant : public Student, public Employee {};
  ```
  - `TeachingAssistant` 中只有一个 `Person` 子对象。

---

### **构造函数与析构函数**

####  **构造函数调用顺序**

1. 基类构造函数（按继承顺序）。
2. 成员对象的构造函数（按声明顺序）。
3. 派生类构造函数。

####  **析构函数调用顺序**

1. 派生类析构函数。
2. 成员对象的析构函数。
3. 基类析构函数（按继承逆序）。

####  **显式调用基类构造函数**

- 在派生类构造函数初始化列表中调用基类构造函数。
  ```cpp
  class Base {
  public:
      Base(int x) { /* ... */ }
  };
  
  class Derived : public Base {
  public:
      Derived(int x, int y) : Base(x) { /* ... */ }
  };
  ```

---

### **覆盖与隐藏**

####  **函数覆盖（Override）**

- 派生类重写基类的虚函数（需使用 `virtual` 关键字）。
  ```cpp
  class Base {
  public:
      virtual void print() { cout << "Base" << endl; }
  };
  
  class Derived : public Base {
  public:
      void print() override { cout << "Derived" << endl; }
  };
  ```

#### **函数隐藏**

- 派生类定义与基类同名但参数不同的函数，导致基类函数被隐藏。
  ```cpp
  class Base {
  public:
      void func(int x) { /* ... */ }
  };
  
  class Derived : public Base {
  public:
      void func(double x) { /* ... */ } // 隐藏 Base::func(int)
  };
  ```

---

### **虚继承（Virtual Inheritance）**

- **目的**：解决多重继承中的菱形问题，确保基类只被继承一次。
- **语法**：
  ```cpp
  class Base { /* ... */ };
  class Derived1 : virtual public Base { /* ... */ };
  class Derived2 : virtual public Base { /* ... */ };
  class Final : public Derived1, public Derived2 { /* ... */ };
  ```

---

### **使用注意事项**

1. 优先使用公有继承（符合“is-a”关系）。
2. 谨慎使用多重继承，优先用组合代替。
3. 使用 `override` 关键字明确函数覆盖。
4. 避免在基类中使用非虚析构函数（可能导致资源泄漏）。



## 类对象之间转换

| 转换类型                              | 合法性                         | 说明/示例                                                |
| ------------------------------------- | ------------------------------ | -------------------------------------------------------- |
| 派生类指针 → 基类指针                 | 合法                           | `Base* b = d;`                                           |
| 派生类引用 → 基类引用                 | 合法                           | `Base& b = d;`                                           |
| 基类指针 → 派生类指针（dynamic_cast） | 合法（运行时需实际类型匹配）   | `Derived* d = dynamic_cast<Derived*>(b);`                |
| 基类指针 → 派生类指针（static_cast）  | 不安全（行为未定义）           | `Derived* d = static_cast<Derived*>(b);`                 |
| 无继承关系类指针转换                  | 非法                           | `B* b = (B*)a; // A与B无继承关系`                        |
| 派生类对象赋值给基类对象              | 合法（发生对象切片）           | `Base b = d;`                                            |
| 基类对象赋值给派生类对象              | 非法（类型不兼容）             | `Derived d = b; // 错误`                                 |
| 对象指针 void* ↔ 任意类型指针         | 合法（需谨慎）                 | `void* vp = d; Derived* d2 = static_cast<Derived*>(vp);` |
| const_cast（去除const）               | 合法（但修改原数据行为未定义） | `int* q = const_cast<int*>(p);`                          |
| reinterpret_cast（强制位级转换）      | 合法（极不安全）               | `int* p = reinterpret_cast<int*>(0x123456);`             |



## 多态和虚函数

### 动态多态

动态多态是面向对象编程中最重要的特性之一，它允许程序在运行时决定调用哪一个版本的函数。当一个基类的指针或引用指向派生类的对象时，就可以通过虚函数实现多态行为。

### 关键点：

1. **继承关系**：动态多态要求有继承关系，子类需要重写父类的虚函数。
2. **虚函数**：父类中的虚函数必须被子类重写（覆盖），从而允许运行时动态绑定。

### 纯虚函数与抽象类

- **纯虚函数**：在父类中声明为 `= 0`，表示该函数没有实现，必须由派生类实现。
  
  - 纯虚函数使得类变为**抽象类**，抽象类无法直接实例化，只能通过其派生类来使用。
  
  纯虚函数语法：
  
  > virtual 返回值类型 函数名 （参数列表） = 0；
  
  当类里有了纯虚函数，这个类也就被称为抽象类。
  
  特点：①无法实例化对象；②子类必须重写抽象类里的纯虚函数否则也是抽象类

### 纯虚函数示例：

```cpp
class Animal {
public:
    virtual void speak() = 0;  // 纯虚函数，必须被派生类重写
};

class Dog : public Animal {
public:
    void speak() override {
        cout << "Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void speak() override {
        cout << "Meow!" << endl;
    }
};

void makeSound(Animal& animal) {
    animal.speak();
}

int main() {
    Dog dog;
    Cat cat;

    makeSound(dog);  // 输出 Woof!
    makeSound(cat);  // 输出 Meow!

    return 0;
}
```

### 虚析构函数

虚析构函数用于确保当通过基类指针删除派生类对象时，派生类的析构函数被正确调用。这是实现多态的一部分，如果没有虚析构函数，程序可能会发生内存泄漏，因为基类析构函数不会自动调用派生类的析构函数。

#### 虚析构函数示例：

```cpp
class Base {
public:
    virtual ~Base() {
        cout << "Base class destructor" << endl;
    }
};

class Derived : public Base {
public:
    ~Derived() override {
        cout << "Derived class destructor" << endl;
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // 删除派生类对象时会先调用派生类的析构函数，再调用基类的析构函数
    return 0;
}
```

## 模板

模板是 C++ 中实现泛型编程的工具，可以让代码更具通用性，减少重复编写。

#### 函数模板

函数模板允许我们编写一个函数模板，之后可以根据传入的类型自动推导出相应类型的函数。

##### 函数模板示例：
```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << add(3, 4) << endl;  // 传入整数
    cout << add(3.5, 4.5) << endl;  // 传入浮点数
    return 0;
}
```

#### 类模板

类模板允许我们编写一个类模板，之后可以使用不同类型实例化该类。

##### 类模板示例：
```cpp
template <typename T>
class Box {
private:
    T value;
public:
    Box(T v) : value(v) {}
    T getValue() { return value; }
};

int main() {
    Box<int> intBox(10);
    Box<double> doubleBox(3.14);

    cout << intBox.getValue() << endl;
    cout << doubleBox.getValue() << endl;

    return 0;
}
```

## 多重继承与虚继承

C++ 允许多重继承，即一个类可以继承多个父类。然而，多重继承有时会导致问题，特别是在父类中有相同成员时，这种情况被称为**菱形继承**。为了解决菱形继承问题，C++ 引入了虚继承。

#### 菱形继承问题

菱形继承指的是一个类继承自两个类，而这两个类又有相同的基类。在没有虚继承的情况下，派生类会有两个基类的副本，导致二义性问题和资源重复管理的问题。

##### 菱形继承示例：
```cpp
class A {
public:
    void show() {
        cout << "Class A" << endl;
    }
};

class B : public A {
public:
    void show() {
        cout << "Class B" << endl;
    }
};

class C : public A {
public:
    void show() {
        cout << "Class C" << endl;
    }
};

class D : public B, public C {
    // D 类从 B 和 C 类继承，且 B 和 C 都继承自 A
};

int main() {
    D d;
    d.show();  // 这里会有二义性，因为 D 类继承了两个 A 类的副本
    return 0;
}
```

#### 虚继承

虚继承解决了菱形继承问题，使得类 `D` 只有一个 `A` 的副本，而不是两个。在虚继承中，父类 `A` 的构造函数只会调用一次，派生类 `B` 和 `C` 不会重复调用 `A` 的构造函数。

##### 虚继承示例：
```cpp
class A {
public:
    A() { cout << "A constructor" << endl; }
    virtual void show() { cout << "Class A" << endl; }
};

class B : virtual public A {
public:
    void show() override { cout << "Class B" << endl; }
};

class C : virtual public A {
public:
    void show() override { cout << "Class C" << endl; }
};

class D : public B, public C {
public:
    void show() override { cout << "Class D" << endl; }
};

int main() {
    D d;
    d.show();  // 输出 "Class D"
    return 0;
}
```

## 智能指针

智能指针是 C++11 引入的，用来管理动态内存的分配和释放，避免手动内存管理导致的内存泄漏问题。常见的智能指针有 `std::unique_ptr`、`std::shared_ptr` 和 `std::weak_ptr`。

#### `std::unique_ptr`

`std::unique_ptr` 是一种独占所有权的智能指针，确保同一时刻只有一个 `unique_ptr` 拥有资源的所有权。

##### `std::unique_ptr` 示例：
```cpp
#include <memory>

class Person {
public:
    Person() { cout << "Person created" << endl; }
    ~Person() { cout << "Person destroyed" << endl; }
};

int main() {
    std::unique_ptr<Person> p1 = std::make_unique<Person>();  // 自动管理内存
    // 不需要手动调用 delete，p1 超出作用域时自动销毁
    return 0;
}
```

#### `std::shared_ptr`

`std::shared_ptr` 允许多个指针共享同一个资源。当所有指向资源的 `shared_ptr` 都被销毁时，资源才会被释放。

##### `std::shared_ptr` 示例：
```cpp
#include <memory>

int main() {
    std::shared_ptr<int> ptr1 = std::make_shared<int>(10);
    std::shared_ptr<int> ptr2 = ptr1;  // ptr1 和 ptr2 共享内存

    cout << *ptr1 << endl;  // 输出 10
    cout << *ptr2 << endl;  // 输出 10

    return 0;
}
```

#### `std::weak_ptr`

`std::weak_ptr` 是用来解决循环引用问题的智能指针，它不会增加引用计数。

## Lambda 表达式

Lambda 表达式是 C++11 引入的一种匿名函数对象，允许我们在代码中直接定义可调用的函数。

#### Lambda 表达式示例：

```cpp
#include <iostream>
using namespace std;

int main() {
    auto add = [](int a, int b) { return a + b; };
    cout << add(3, 4) << endl;  // 输出 7
    return 0;
}
```

