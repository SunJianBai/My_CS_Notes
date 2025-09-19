[toc]

# 基础

![image-20250413160312331](https://cdn.jsdelivr.net/gh/SunJianBai/pictures/img/202504131605018.png)

![image-20250413160936531](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504131609578.png)



模式定义了数据如何存储、存储什么样的数据以及数据如何分解等信息，数据库和表都有模式。



## SQL模式

现代关系数据库管理系统提供了一个 层次化的数
据库对象命名机制

- 一个关系数据库管理系统的实例（ Instance ）中可以
  建立多个数据库
- 一个数据库中可以建立多个 模式（ Schema）
- 一个模式下通常包括多个表、视图和索引等数据库对象
  ![image-20250326155601462](SQL.assets/image-20250326155601462.png)

## SQL 表

SQL 的 表 分为两种： **基本表** 和 **视图**

- 基本表（ Base Table Table ）

  - 独立存在的表

  - 一个关系模式对应一个基本表

- 视图（ View ）
  
    - 是从一个或多个基本表中导出的表，仅有逻辑上的定义，不实际存储数据，是一种虚表。
    - 视图的定义存储在数据字典中，在使用的时候，根据定义从基本表中导出数据供用户使用。
    - 视图可以象基本表一样进行查询和 某些更新 操作。

## SQL语言特点

SQL 语句**不区分大小写**，但是数据库表名、列名和值是否区分依赖于具体的 DBMS 以及配置。

SQL 支持以下三种注释：

```sql
# 注释
SELECT *
FROM mytable; -- 注释
/* 注释1
   注释2 */
```

数据库创建与使用：

```sql
CREATE DATABASE test;
USE test;
```

## SQL常用数据类型

```sql
SMALLINT 短整数
INTEGER 或 INT 长整数
REAL 浮点数
DOUBLE PRECISION 双精度浮点数
FLOAT n 浮点数 , 精度为 n 位
NUMBER p[,q] 定点数，共 p 位，其中小数点后有 q 位
CHAR n 长度为 n 的定长字符串
VARCHAR n 最大长度为 n 的变长字符串
BIT n 长度为 n 的二进制位串
BIT VARCHAR n 最大长度为 n 的二进制位串
DATE 日期型，格式为 YYYY MM DD
TIME 时间型，格式为 HH MM SS
TIMESTAMP 日期加时间
```

在 SQL2 中增加了 定义域的语句 ，可以 用域名代替指定列的数据类型 。

如果有一个或多个表的属性的域是相同的，通过对域的修改可以很容易地改变属性的数据类型。
域定义语句的格式为：
CREATE DOMAIN <域名 > 数据类型

- 例:
  CREATE DOMAIN Sdept_TYPE CHAR(12);
  域 Sdept_TYPE 创建后，定义学生表时，对列 Sdept 的
  类型定义可以用域名代替： Sdept Sdept_TYPE 。





# 创建表

![image-20250413161027051](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504131610091.png)

```sql
CREATE TABLE <表名>
(<列名 > 数据类型 >[ 列级完整性约束条件 >
[, 列名 > 数据类型 >[ 列级完整性约束条件 > ]
 …
[,<表级完整性约束条件>]);

<表名>：所要定义的基本表的名字

<列名>：组成该表的各个属性 (列)

<列级完整性约束条件>：涉及相应属性列的完整性约束条件

<表级完整性约束条件>：涉及一个或多个属性列的完整性约束条件
 
 );
```



```sql
CREATE TABLE mytable (
  # int 类型，不为空，自增
  id INT NOT NULL AUTO_INCREMENT,
    
  # int 类型，不可为空，默认值为 1，不为空
  col1 INT NOT NULL DEFAULT 1,
    
  # 变长字符串类型，最长为 45 个字符，可以为空
  col2 VARCHAR(45) NULL,
    
  # 日期类型，可为空
  col3 DATE NULL,
    
  # char类型，最长为2个字符 
  Ssex CHAR(2),
    
  # 约束名为 C1 
  CONSTRAINT C1 CHECK (Ssex IN('男', '女')),
    
  # 设置主键为 id
  PRIMARY KEY (`id`));
```

# 约束

约束是指对表中**数据**的一种约束，用于保证数据库中数据的**正确性和有效性**。



CONSTRAINT 子句定义列级或表级约束，格式为
CONSTRAINT < 约束名 > 约束

**常见的 CONSTRAINT 类型**

| 约束类型        | 作用                                     | 示例                                         |
| :-------------- | :--------------------------------------- | :------------------------------------------- |
| **PRIMARY KEY** | 唯一标识一行数据，不允许 NULL 和重复值   | `PRIMARY KEY (id)`                           |
| **FOREIGN KEY** | 确保字段值引用其他表的主键，维护表间关系 | `FOREIGN KEY (user_id) REFERENCES users(id)` |
| **UNIQUE**      | 确保字段值唯一（但允许 NULL）            | `UNIQUE (email)`                             |
| **CHECK**       | 限制字段值必须满足指定条件               | `CHECK (age >= 18)`                          |
| **NOT NULL**    | 禁止字段为 NULL                          | `name VARCHAR(50) NOT NULL`                  |
| **DEFAULT**     | 未提供值时使用默认值                     | `status INT DEFAULT 1`                       |

**列级约束**（直接写在字段定义后）

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,                  -- 主键约束
    email VARCHAR(100) UNIQUE,           -- 唯一约束
    age INT CHECK (age >= 18),           -- 检查约束
    name VARCHAR(50) NOT NULL,           -- 非空约束
    status INT DEFAULT 1                 -- 默认值约束
);
```

**表级约束**（单独定义，可命名）

```sql
CREATE TABLE users (
    id INT,
    email VARCHAR(100),
    age INT,
    name VARCHAR(50),
    status INT,
    
    -- 命名约束（推荐，便于管理）
    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT uk_email UNIQUE (email),
    CONSTRAINT ck_age CHECK (age >= 18),
    CONSTRAINT fk_status FOREIGN KEY (status) REFERENCES status_codes(id)
);
```

 **约束的命名（`CONSTRAINT 约束名`）**

- 约束可以命名（如 `CONSTRAINT ck_age CHECK (age >= 18)`），便于后续管理：
  - **修改约束**：`ALTER TABLE ... DROP CONSTRAINT 约束名`
  - **查看约束**：`SHOW CREATE TABLE 表名`
- 如果不命名，数据库会自动生成一个随机名称（如 `check_1234`），不利于维护。

MySQL主要支持以下6种约束：

- **主键约束**

表的一个特殊字段，该字段能唯一标识表中的每条信息。**一个表中只能有一个。**

- **外键约束**

通常与主键约束一起使用，保证数据的一致性。

例如，一个水果摊，只有苹果、桃子、李子、西瓜 4 种水果，那么，你来到水果摊要买水果只能选择苹果、桃子、李子和西瓜，不能购买其它的水果。

- **唯一约束**

唯一约束和主键约束相似的，能够确保列的唯一性。但是唯一约束在一个表中**可以有多个**，并且设置唯一约束的列是**允许有空值**的，这个空值最多**只能有一个**。

- **检查约束**

检查数据表中，**字段值是否有效**。如负数校验等

- **非空约束**

约束表中的字段不能为空

- **默认值约束**

默认值约束用来约束当数据表中某个字段不输入值时，自动为其添加一个已经设置好的值。

### 主键约束 PRIMARY KEY

主键的值不允许修改，也不允许复用（不能将已经删除的主键值赋给新数据行的主键）。

主键分为**单字段主键**和**多字段联合主键**，本节将分别讲解这两种主键约束的创建、修改和删除。

使用主键应注意以下几点：

- 每个表只能定义**一个主键**。
- 主键值必须唯一标识表中的每一行，且**不能为 NULL**，即表中不可能存在有相同主键值的两行数据。这是**唯一性原则**。
- 一个字段名只能在联合主键字段表中出现一次。
- 联合主键**不能包含不必要的多余字段**。当把联合主键的某一字段删除后，如果剩下的字段构成的主键仍然满足唯一性原则，那么这个联合主键是不正确的。这是**最小化原则**。

**在创建表时设置主键约束**

**设置单字段主键**

在 CREATE TABLE 语句中，通过 PRIMARY KEY 关键字来指定主键。

```mysql
<字段名> <数据类型> PRIMARY KEY [默认值]
 
mysql> CREATE TABLE tb_emp3
  -> (
  -> id INT(11) PRIMARY KEY,
  -> name VARCHAR(25),
  -> deptId INT(11),
  -> salary FLOAT
  -> );
```

或者是在定义完所有字段之后指定主键，语法格式如下：

```mysql
[CONSTRAINT <约束名>] PRIMARY KEY [字段名]
 
mysql> CREATE TABLE tb_emp4
  -> (
  -> id INT(11),
  -> name VARCHAR(25),
  -> deptId INT(11),
  -> salary FLOAT,
  -> PRIMARY KEY(id)
  -> );
```

**设置联合主键**

比如，设置学生选课数据表时，使用学生编号做主键还是用课程编号做主键呢？如果用学生编号做主键，那么一个学生就只能选择一门课程。如果用课程编号做主键，那么一门课程只能有一个学生来选。显然，这两种情况都是不符合实际情况的。

实际上设计学生选课表，**要限定的是一个学生只能选择同一课程一次**。因此，学生编号和课程编号可以放在一起共同作为主键，这也就是联合主键了。

```mysql
PRIMARY KEY [字段1，字段2，…,字段n]
 
mysql> CREATE TABLE tb_emp5
  -> (
  -> name VARCHAR(25),
  -> deptId INT(11),
  -> salary FLOAT,
  -> PRIMARY KEY(name,deptId)
  -> );
```

**在修改表时添加主键约束**

```mysql
ALTER TABLE <数据表名> ADD PRIMARY KEY(<字段名>);
 
mysql> ALTER TABLE tb_emp2
  -> ADD PRIMARY KEY(id);
```

**删除主键约束**

```mysql
ALTER TABLE <数据表名> DROP PRIMARY KEY;
 
mysql> ALTER TABLE tb_emp2
  -> DROP PRIMARY KEY;
```

### 主键自增长 AUTO_INCREMENT

```mysql
字段名 数据类型 AUTO_INCREMENT
mysql> CREATE TABLE tb_student(
  -> id INT(4) PRIMARY KEY AUTO_INCREMENT,
  -> name VARCHAR(25) NOT NULL
  -> );
```

- 默认情况下，AUTO_INCREMENT 的**初始值是** **1**，每新增一条记录，字段值自动加 1。
- 一个表中只能有一个字段使用 AUTO_INCREMENT 约束，且该字段**必须有唯一索引**，以避免序号重复（即为主键或主键的一部分）。
- AUTO_INCREMENT 约束的字段必须具备 **NOT NULL** 属性。
- AUTO_INCREMENT 约束的字段只能是**整数类型**（TINYINT、SMALLINT、INT、BIGINT 等）。
- AUTO_INCREMENT 约束字段的最大值受该字段的**数据类型约束**，如果达到上限，AUTO_INCREMENT 就会失效。

**指定自增字段初始值**

```mysql
mysql> CREATE TABLE tb_student2 (
  -> id INT NOT NULL AUTO_INCREMENT,
  -> name VARCHAR(20) NOT NULL,
  -> PRIMARY KEY(ID)
  -> )AUTO_INCREMENT=100;
```

### 外键约束 FOREIGN KEY

MySQL 外键约束（FOREIGN KEY）是表的一个特殊字段，经常与主键约束一起使用。对于两个具有关联关系的表而言，相关联字段中主键所在的表就是**主表（父表）**，外键所在的表就是**从表（子表）**。

主表删除某条记录时，从表中与之对应的记录也必须有相应的改变。一个表可以**有一个或多个外键**，外键可以为空值，若不为空值，则**每一个外键的值必须等于主表中主键的某个值。**

定义外键时，需要遵守下列规则：

- 主表必须**已经存在**于数据库中，或者是**当前正在创建的表**。如果是后一种情况，则主表与从表是**同一个表**，这样的表称为**自参照表**，这种结构称为**自参照完整性**。
- 必须**为主表定义主键**。
- **主键不能包含空值**，但允许在外键中出现空值。也就是说，只要外键的每个非空值出现在指定的主键中，这个外键的内容就是正确的。
- 在主表的表名后面指定列名或列名的组合。这个列或列的组合必须是主表的主键或候选键。
- 外键中**列的数目必须和主表的主键中列的数目**相同。
- 外键中**列的数据类型必须和主表主键中对应列的数据类型**相同。

**语法**

```mysql
[CONSTRAINT <外键名>] FOREIGN KEY 字段名 [，字段名2，…]
REFERENCES <主表名> 主键列1 [，主键列2，…]
```

```mysql
# 创建一个部门表tb_dept1，结构如下
CREATE TABLE tb_dept1
(
id INT(11) PRIMARY KEY,
name VARCHAR(22) NOT NULL,
location VARCHAR(50) 
);

# 创建数据表tb_emp6，并在表中创建外键约束。将它的键deptId作为外键关联到表tb_dept1的主键id

CREATE TABLE tb_emp6
(
id INT(11) PRIMARY KEY,
name VARCHAR(25),
deptId INT(11),
salary FLOAT,
CONSTRAINT fk_emp_dept1
FOREIGN KEY(deptId) REFERENCES tb_dept1(id)
);
```



**在修改表时添加外键约束**

外键约束也可以在修改表时添加，但是添加外键约束的前提是：**从表中外键列中的数据必须与主表中主键列中的数据一致或者是没有数据**。

```mysql
ALTER TABLE <数据表名> ADD CONSTRAINT <外键名>
FOREIGN KEY(<列名>) REFERENCES <主表名> (<列名>);
 
ALTER TABLE tb_emp2 ADD CONSTRANT fk_tb_dept1 FOREIGN KEY(deptId) REFERENCES tb_dept1(id);
```

 

**删除外键约束**

```mysql
ALTER TABLE <表名> DROP FOREIGN KEY <外键约束名>;
 
ALTER TABLE tb_emp2 DROP FOREIGN KEY fk_tb_dept1;
```



### 唯一约束 UNIQUE

MySQL 唯一约束（Unique Key）是指所有记录中字段的值不能重复出现。

唯一约束在一个表中**可有多个**，并且设置唯一约束的列**允许有空值**，但是**只能有一个空值。**



**创建表时设置唯一约束**

```mysql
<字段名> <数据类型> UNIQUE
 
CREATE TABLE tb_dept2
(
id INT(11) PRIMARY KEY,
name VARCHAR(22) UNIQUE,
location VARCHAR(50)
);
```



**修改表时设置唯一约束**

```mysql
ALTER TABLE <table name> ADD CONSTRAINT <unique name> UNIQUE(<column name>)
 
ALTER TABLE tb_dept1 ADD CONSTRAINT unique_name UNIQUE(name);
```



**删除唯一约束**

```mysql
ALTER TABLE <表名> DROP INDEX <唯一约束名>;
 
ALTER TABLE tb_dept1 DROP INDEX unique_name;
```

### 检查约束 CHECK

MySQL 检查约束（CHECK）是用来**检查数据表中字段值有效性**的一种手段

包括**基于列**的CHECK约束和**基于表**的CHECK约束

注意：若将 CHECK 约束子句置于所有列的定义以及主键约束和外键定义之后，则这种约束也称为基于表的 CHECK 约束。该约束可以同时对表中多个列设置限定条件。

 

**在创建表时设置检查约束**

```mysql
mysql> CREATE TABLE tb_emp7
  -> (
  -> id INT(11) PRIMARY KEY,
  -> name VARCHAR(25),
  -> deptId INT(11),
  -> salary FLOAT,
  -> CHECK(salary>0 AND salary<100),
  -> FOREIGN KEY(deptId) REFERENCES tb_dept1(id)
  -> );
Query OK, 0 rows affected (0.37 sec)
```

 

**在修改表时添加检查约束**

```mysql
ALTER TABLE tb_emp7 ADD CONSTRAINT <检查约束名> CHECK(<检查约束>)
 
ALTER TABLE tb_emp7 ADD CONSTRAINT check_id CHECK(id>0);
```

 

**删除检查约束**

```mysql
ALTER TABLE <数据表名> DROP CONSTRAINT <检查约束名>;
 
ALTER TABLE tb_emp7 DROP CONSTRAINT check_id;
```

### 默认值约束DEFAULT

默认值约束通常用在已经设置了非空约束的列，这样能够防止数据表在录入数据时出现错误。

**在创建表时设置默认值约束**

```mysql
<字段名> <数据类型> DEFAULT <默认值>;
 
CREATE TABLE tb_dept3
(
id INT(11) PRIMARY KEY,
name VARCHAR(22),
location VARCHAR(50) DEFAULT 'Beijing'
);
```

**在修改表时添加默认值约束**

```mysql
ALTER TABLE <数据表名> CHANGE COLUMN <字段名> <数据类型> DEFAULT <默认值>;
 
ALTER TABLE tb_dept3 CHANGE COLUMN location VARCHAR(50) DEFAULT 'Shanghai';
```

**删除默认值约束**

```mysql
ALTER TABLE <数据表名>
CHANGE COLUMN <字段名> <字段名> <数据类型> DEFAULT NULL;
ALTER TABLE tb_dept3 CHANGE COLUMN location VARCHAR(50) DEFAULT NULL;
```



### 非空约束 NOT NULL

MySQL 非空约束（NOT NULL）指字段的值不能为空。

**在创建表时设置非空约束**

```mysql
<字段名> <数据类型> NOT NULL;
CREATE TABLE tb_dept4
(
id INT(11) PRIMARY KEY,
name VARCHAR(22) NOT NULL,
location VARCHAR(50)
);
```

**在修改表时添加非空约束**

```mysql
ALTER TABLE <数据表名>
CHANGE COLUMN <字段名>
<字段名> <数据类型> NOT NULL;
 
 ALTER TABLE tb_dept4 CHANGE COLUMN location VARCHAR(50) NOT NULL;
```

**删除非空约束**

```mysql
ALTER TABLE <数据表名>
CHANGE COLUMN <字段名> <字段名> <数据类型> NULL;
 
ALTER TABLE tb_dept4 CHANGE COLUMN location VARCHAR(50) NULL;
```





# 索引

索引是数据库表中一列或多列的值进行排序的一种结构，使用索引可以快速访问数据库表中的特定信息。

**作用**

- 大大提高数据检索速度
- 加速表与表之间的连接
- 减少查询中分组和排序的时间
- 通过使用索引，可以在查询中使用优化器，提高系统性能

索引的更新和维护是由 DBMS 自动完成 的
系统在存取数据时会自动选择是否使用索引 或者是以合适的索引作为存取路径，用户不必也不能选择索引

有些 DBMS 能自动在某些特殊属性列上建立索引

- PRIMARY KEY
  UNIQUE

## 索引的类型

### 普通索引

最基本的索引类型，没有任何限制。

```sql
CREATE INDEX index_name ON table_name (column_name);
```

### 唯一值索引

索引列的值必须唯一，但允许有空值。

对于已含重复值的属性列不能建 `UNIQUE` 索引

对某个列建立 UNIQUE 索引后，插入新记录时 `DBMS `会自动检查新记录在该列上是否取了重复值。这相当于增加了一个 `UNIQUE `约束。

```sql
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

**例:**

```sql
CREATE UNIQUE INDEX SnoIdx ON Student(Sno);
CREATE UNIQUE INDEX CnoIdx ON Course(Cno);
CREATE UNIQUE INDEX SCno ON
SC(Sno ASC, Cno DESC);
```

### 聚集索引

索引次序与基本表中元组的**物理次序一致**的索引；建立聚集索引后 基表中数据也需要按指定的聚集属性值的升序或降序存放 

即：聚集索引的索引项顺序与表中记录的物理顺序一致

```sql
CREATE CLUSTER INDEX Stusname
		ON Student(Sname);
```

在Student 表的 Sname( 姓名 列上建立一个聚集索引，而且Student 表中的记录将按照 Sname 值的升序存放



### 主键索引

特殊的唯一索引，不允许有空值。

```sql
ALTER TABLE table_name ADD PRIMARY KEY (column_name);
```

## 索引的创建与管理

```sql
-- 基本语法
CREATE [UNIQUE|FULLTEXT|SPATIAL][CLUSTER] INDEX <索引名>
ON <表名> (column_name [(length)] [ASC|DESC], ...)
[USING index_type]
```

<表名>指定要建索引的基本表名字
索引可以建立在该表的 一列或多列 上 各列名之间用逗号分隔
<次序>指定索引值的排列次序，升序`ASC,`  降序`DESC`。缺省默认值：``ASC`

`UNIQUE`   表明此索引的每一个索引值只对应唯一的数据记录（唯一值索引）
`CLUSTER`  表示要建立的索引是聚集索引（ Cluster Index ）





### **修改索引**

```sql
-- MySQL中没有直接修改索引的命令，需要先删除再创建
DROP INDEX index_name ON table_name;
CREATE INDEX new_index_name ON table_name (column_name);
```

**删除索引**

```sql
DROP INDEX index_name ON table_name;
-- 或
ALTER TABLE table_name DROP INDEX index_name;
```

**查看索引**

```sql
SHOW INDEX FROM table_name;
```



#  修改表

```sql
ALTER TABLE <表名>
	[ADD <列名> <数据类型> [<完整性约束>]]
	[DROP <列名> [CASCADE | RESTRICT]]
	[ALTER <列名> <数据类型> ];
```

## **添加列**

ADD 子句 用于增加新列 包括列名 、 数据类型和列级完整性约束

```sql
ALTER TABLE mytable
	ADD col CHAR(20);
```

不论基本表中原来是否已有数据 新增加的列一律为空值；不能在其上指定 NOT NULL

## **删除列**

```sql
DROP TABLE <表名> [RESTRICT|CASCADE];
```

DROP 子句 用于删除指定的列名

- CASCADE 表示删除列时自动删除引用该列的视图和约束

- RECTRICT(默认） 表示没有视图和约束引用时才能删除该列 否则将拒绝删除操

    若选择RESTRICT，则删除的基本表不能被其他表的约束所引用（如CHECK,FOREIGN KEY等约束），不能有视图，不能有触发器，不能有存储过程或函数等。如果存在这些依赖该表的对象，则此表不能被删除。

```sql
DROP TABLE mytable;
```

## **删除表**

ALTER 子句 用于修改列的定义 如修改列的数据类型或修改列的宽度等

```sql
ALTER TABLE mytable
DROP COLUMN col;
```

## 截断表

```sql
TRUNCATE TABLE table_name
```

功能

- 删除表中所有行（与不带 WHERE 子句的 DELETE 语句相同），但不记录单个行删除操作
- 比 DELETE 速度快，使用的系统和事务日志资源少
  - DELETE 语句每次删除一行，并在事务日志中为所删除的每行
    记录一项。
  - TRUNCATE TABLE 通过释放存储表数据所用的数据页来删除
    数据，并且只在事务日志中记录页的释放。
- 操作不能回滚， 但 DELETE 可以回滚



# 修改数据

## 更新

```sql
UPDATE<表名>
	SET 列名1=<表达式1>[,列名2=<表达式2>]...
	[WHERE<条件表达式>];
```

功能：修改指定表中满足WHERE子句条件的元组的指定列的内容

**SET**子句，指定修改方式

- 要修改的列
- 修改后取值

**WHERE**子句，指定要修改的元组

- 缺省表示要修改表中的所有元组

**修改一个或多个元组的值**

> 【例】将数据库课的学分修改为4。

```sql
UPDATE Course
	SET Ccredit=4
	WHERE Cname='数据库';
```



> 【例】将所有学生的年龄增加1岁

```sql
UPDATE Student SET Sage=Sage+1;
```



> 【例】将所有选修了数据库课的学生的成绩清空

```sql
UPDATE SC SET Grade=NULL
	WHERE Cno IN
	(SELECT Cno
		FROM Course
		WHERE Cname='数据库');
```



> 【例 】 将计算机系全体学生的成绩置零 。

```sql
UPDATE SC
	SET Grade=0
		WHERE'cs'=
			(SELETE Sdept
				FROM Student
					WHERE Student.Sno = SC.Sno);
```

```sql
Update SC set Grade=0
	From SC, Student
	where SC.Sno=Student.Sno and Sdept= 'CS'
```





# 插入

### 普通插入

```sql
INSERT INTO<表名>[(<属性列1>[,<属性列2>..)]
	VALUES（<常量1>[，<常量2>］);
```

**INTO 子句**

- 指定要插入数据的表名及属性列

- 属性列的顺序可以与表定义中的顺序不一致

- 没有指定属性列 ：表示要插入的是一条完整的元组且属性列属性与表定义中的顺序一致

- 指定部分属性列：插入的元组在其余属性列上取空值或者是默认值

**VALUES 子句**

- 提供的值必须与 INTO 子句匹配：个数、顺序和值的类型



**例：**在学生表中插入一个学生元组，其学号为101215 ，姓名为李斌，男 19 岁，是计算机系的学生。

```sql
INSERT INTO Student
	VALUES('101215'，'李斌','男',19,'计算机');

INSERT INTO Student (Sno, Sname, Sdept, Sage, Ssex)
	VALUES('101215','李斌','计算机',19,'男');
```

如果表的定义说明某列为`NOT NULL`，则插入时不能取空值。



### 插入子查询结果

将子查询结果插入指定表中

```sql
INSERT INTO <表名>[(<列名1>[,<列名2>，...])]
	<SELECT语句>;/*子查询*/;
```

**INTO 子句**

- 指定要插入数据的表名及属性列
- 属性列的顺序可与表定义中的顺序不一致
  - 没有指定属性列，则表示插入一条完整的元组
  - 指定部分属性列，则在其余属性列上取空值

**子查询**

- SELECT 子句目标列必须与 INTO 子句匹配：个数、顺序和值的类型



> **【例】** 计算计算机系每个学生的平均成绩，并保存在 CS AVG 表中。
>
> 1. 生成学生的平均成绩表 CS AVG
> 2. 在 CS AVG 中插入计算机系学生的平均成绩

```sql
CREATE TABLE CS-AVG
	(Sno CHAR(6)NOT NULL,
	Grade NUMBER(4,1));
```

```sql
INSERT INTO CS-AVG (Sno, Grade)
	SELECT Sno, AVG(Grade) FROM SC
		WHERE Sno IN(
			SELECT Sno FROM Student
			WHERE Sdept='CS')
		GROUP BY Sno ;
```





### 将一个表的内容插入到一个新表

```sql
CREATE TABLE newtable AS
SELECT * FROM mytable;
```



# 删除

```sql
DELETE FROM<表名>
	[WHERE<条件>];
```

功能

- 删除指定表中满足WHERE子句条件的元组

WHERE子句

- 指定要删除的元组
- 缺省表示要修改表中的所有元组



**DBMS 在执行 删除语句时**
检查所删元组是否破坏表上已定义的完整性规则 (参照完整性；如果破坏，则

1. 不允许删除
2. 级联删除



### 删除一个或多个元组
> 【例】删除学号为201225的学生记录

```sql
DELETE FROM StudentWHERE Sn0='201225';
```

> 【例】删除所有的学生选课记录

```sql
DELETE FROM SC;
```

### 带子查询的删除
> 【例】删除所有选修数据库课学生的选课信息

```sql
DELETE FROM SC
	WHERE Cno IN
		(SELECT Cno FROM Course
			WHERE Cname='数据库');
```

```sql
DELETE FROM mytable
WHERE id = 1;
```

**TRUNCATE TABLE**   可以清空表，也就是删除所有行。

```sql
TRUNCATE TABLE mytable;
```

使用更新和删除操作时一定要用 WHERE 子句，不然会把整张表的数据都破坏。可以先用 SELECT 语句进行测试，防止错误删除。

# 查询

## 查询基本语法

```sql
SELECT[ALL|DISTINCT] <目标列表达式>[,<目标列表达式>]
	FROM <表名或视图名>[,<表名或视图名>]
	[WHERE <条件表达式 1>]
	[GROUP BY <列名 1> [HAVING <条件表达式 2>]
	[ORDER BY <列名 2> [ASC|DESC]];
```

- SELECT 子句 ：指定要显示的属性列
- FROM 子句 ：指定查询对象 基本表或视图
- WHERE 子句 ：指定查询条件
- GROUP BY 子句 ：对查询结果按指定列的值分组 该属性列值相等的元组为一个组 。 通常会在每组中使用`聚集函数` 。
- HAVING 短语 ：筛选出满足指定条件的组
- ORDER BY 子句 ：对查询结果表按指定列值的升序或降序排序
- DISTINCT 表示去掉重复元组， ALL 则容许 重复元组

### 结构

```sql
Select A1, A2, ..., An
	From R1, R2, ..., Rm
	Where P
```

<img src="https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504281401228.png" alt="image-20250402162605364" style="zoom:67%;" />

## 单表查询

查询仅涉及一个表，是一种最简单的查询操作

- 选择表中的若干列
- 选择表中的若干元组
- 对查询结果排序
- 使用聚集函数
- 对查询结果分组

SELECT 子句的 目标列表达式 不仅可以是表中的属性列，也可以是

- 表达式
- 算术表达式
- 字符串常量
- 函数
- 列别名

## 例子

示例数据库：学生－课程数据库

**学生表：**
	`Student(Sno, Sname, Sage, Ssex, Sdept)`
**课程表：**
	`Course(Cno, Cname, Ccredit, Cpno)`
**学生选课表：**
	`SC(Sno, Cno, Grade)`

> 【例】查询学生的学号和姓名、

```sql
SELECT Sno, Sname 
	FROM Student;
```

> 【例】查询计算机系学生的学号和姓名

```sql
SELECT Sno, Sname
	FROM Student
	WHERE Sdept='计算机';
```

> 【例】查询年龄在18到25岁之间的学生信息

```sql
SELECT *
	FROM Student
	WHERE Sage BETWEEN 18 AND 25;
```

> 【 例 】 查全体学生的姓名及其出生年份

```sql
SELECT Sname,2000-Sage
	FROM Student;
```

> 【 例 】 查询已经选修了课程的学生学号，并按学号升序排列。

```sql
SELECT DISTINCT Sno
	FROM SC
	ORDER BY Sno;
```

> 【 例 】 查询每门课的选修数。

```sql
SELECT Cno,COUNT(*)
	FROM SC
	GROUP BY Cno;
```

> 【例】 查询平均成绩在 85 分以上的学生的学号和平均成绩

```sql
SELECT Sno, AVG(Grade)
	FROM SC
	GROUP BY Sno
	HAVING AVG(Grade)>85;
```

> 【例】 查询成绩在 75~85 分之间的学生的学号和成绩

```sql
SELECT Sno, Grade
	FROM SC
	WHERE Grade>=75 AND Grade<=85;
```

> 【例】 查询年龄为 19 岁的所有姓李的学生姓名。

```sql
SELECT Sname
	FROM Student
	WHERE Sname LIKE '李%' AND Sage=19;
```

> 【例】 查询缺考学生的学号和课程号。

```sql
SELECT Sno, Cno
    FROM SC
    WHERE Grade IS NULL;
```



## DISTINCT

使用 DISTINCT 短语消除取值重复的行

相同值只会出现一次。它作用于所有列，也就是说所有列的值都相同才算相同。

```sql
SELECT DISTINCT Sno
	FROM SC;
```

注意 DISTINCT 短语的作用范围是所有目标列

在DISTINCT 语句后面可以加多个列

## LIMIT

限制返回的行数。可以有两个参数，第一个参数为起始行，从 0 开始；第二个参数为返回的总行数。

返回前 5 行：

```sql
SELECT *
FROM mytable
LIMIT 5;
```

```sql
SELECT *
FROM mytable
LIMIT 0, 5;
```

返回第 3 \~ 5 行：

```sql
SELECT *
FROM mytable
LIMIT 2, 3;
```



## 子查询

子查询中只能返回一个字段的数据。

可以将子查询的结果作为 WHRER 语句的过滤条件：

```sql
SELECT *
FROM mytable1
WHERE col1 IN (SELECT col2
               FROM mytable2);
```

下面的语句可以检索出客户的订单数量，子查询语句会对第一个查询检索出的每个客户执行一次：

```sql
SELECT cust_name, (SELECT COUNT(*)
                   FROM Orders
                   WHERE Orders.cust_id = Customers.cust_id)
                   AS orders_num
FROM Customers
ORDER BY cust_name;
```



## 组合查询

使用   **UNION**   来组合两个查询，如果第一个查询返回 M 行，第二个查询返回 N 行，那么组合查询的结果一般为 M+N 行。

每个查询必须包含相同的列、表达式和聚集函数。

默认会去除相同行，如果需要保留相同行，使用 UNION ALL。

只能包含一个 ORDER BY 子句，并且必须位于语句的最后。

```sql
SELECT col
    FROM mytable
    WHERE col = 1
UNION
SELECT col
    FROM mytable
    WHERE col =2;
```



## 连接查询

同时涉及两个或两个以上表的查询称为连接查询

# 过滤

不进行过滤的数据非常大，导致通过网络传输了多余的数据，从而浪费了网络带宽。因此尽量使用 SQL 语句来过滤不必要的数据，而不是传输所有的数据到客户端中然后由客户端进行过滤。

```sql
SELECT *
FROM mytable
WHERE col IS NULL;
```

在WHERE子句后面添加查询条件

| **表达式类型** | **语法结构**                                                 | **解释**                                                     | **例子**                                                     |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **比较表达式** | `<列名1> 比较算符 <列名2（或常量）>`<br>比较算符：`=、>、>=、<、<=、<>（或! =）` | 用于比较两个值（列或常量），返回布尔值（真或假）。常见于 `WHERE` 子句中，用于过滤数据。 | `age > 18`：筛选年龄大于 18 的记录。或者 `NOT age <= 18`     |
| **逻辑表达式** | `<条件表达式1> 逻辑算符 <条件表达式2>`<br>逻辑算符：`AND、OR、NOT` | 用于组合多个条件，返回布尔值。`AND` 表示所有条件都为真时返回真；`OR` 表示至少一个条件为真时返回真；`NOT` 表示取反。 | `age > 18 AND salary < 5000`：筛选年龄大于 18 且工资小于 5000 的记录。 |
| **BETWEEN**    | `<列名1> (NOT) BETWEEN <常量1或列名2> AND <常量2或列名3>`    | 用于检查某个值是否在指定范围内（包括边界值）。`NOT BETWEEN` 表示不在范围内。 | `price BETWEEN 100 AND 200`：筛选价格在 100 到 200 之间的记录。 |
| **IN**         | `<列名> (NOT) IN (常量表列 或 SELECT 语句)`                  | 用于检查某个值是否在指定的列表或子查询结果中。`NOT IN` 表示不在列表中。 | `country IN ('USA', 'China', 'Japan')`：筛选国家为美国、中国或日本的记录。 |
| **LIKE**       | `<列名> (NOT) LIKE '匹配字符串'`<br>匹配符：`_`（单字符），`%`（任意字符） | 用于模式匹配，`LIKE` 表示符合模式，`NOT LIKE` 表示不符合模式。`_` 匹配单个字符，`%` 匹配任意长度的字符。 | `name LIKE 'A%'`：筛选以字母 A 开头的名字。                  |
| **NULL**       | `<列名> IS (NOT) NULL`                                       | 用于检查某个列是否为 `NULL`（空值）。`IS NULL` 表示值为空，`IS NOT NULL` 表示值不为空。 | `email IS NULL`：筛选邮箱为空的记录。                        |
| **EXISTS**     | `(NOT) EXISTS (SELECT 语句)`                                 | 用于检查子查询是否返回至少一行数据。`EXISTS` 表示子查询有结果，`NOT EXISTS` 表示子查询无结果。 | `EXISTS (SELECT * FROM orders WHERE customer_id = 1001)`：检查客户 1001 是否有订单。 |

## **比较表达式**  

- 用于基本的数值或字符串比较。

- 常见于 `WHERE` 子句中，用于过滤数据。

- 

  |   操作符    |   说明   |
  | :---------: | :------: |
  |      =      |   等于   |
  |    &lt;     |   小于   |
  |    &gt;     |   大于   |
  | &lt;&gt; != |  不等于  |
  | &lt;= !&gt; | 小于等于 |
  | &gt;= !&lt; | 大于等于 |

  

## **逻辑表达式**

**AND 和 OR**   用于连接多个过滤条件。优先处理 AND，当一个过滤表达式涉及到多个 AND 和 OR 时，可以使用 () 来决定优先级，使得优先级关系更清晰。

**IN**   操作符用于匹配一组值，其后也可以接一个 SELECT 子句，从而匹配子查询得到的一组值。

**NOT**   操作符用于否定一个条件。

## **BETWEEN**  

- 包含边界值（即范围的上下限）。
- 适用于数值、日期或字符串的范围比较。

## **IN**  

- 用于列出多个可能的值。
- 子查询返回的结果可以作为 `IN` 的参数。

## **LIKE**  + 通配符

- 当匹配模板为固定字符串时 可用 运算符取代 LIKE 谓词 用 或 运算符取代 NOT LIKE

- 用于字符串模式匹配。

  

通配符只能用于文本字段。

-   **%**   匹配 \>=0 个任意字符；

-   **\_**   匹配 ==1 个任意字符；

-   **[ ]**   可以匹配集合内的字符，例如 [ab] 将匹配字符 a 或者 b。用脱字符 ^ 可以对其进行否定，也就是不匹配集合内的字符。

使用 Like 来进行通配符匹配。

```sql
SELECT * FROM mytable
    WHERE col LIKE '[^AB]%'; -- 不以 A 和 B 开头的任意文本
    WHERE col LIKE 'a%b';   -- 以 a 开头，以 b 结尾的任意长度的字符串
    WHERE col LIKE 'a_b';  -- 以 a 开头，以 b 结尾的长度为 3 的任意字符串
```

不要滥用通配符，通配符位于开头处匹配会非常慢。

## **NULL**  

- `NULL` 表示空值，不是零或空字符串。
- `IS NULL` 和 `IS NOT NULL` 是专门用于检查空值的运算符。

## **EXISTS**  

- 通常与子查询结合使用。
- `EXISTS` 本身不返回数据，只返回布尔值（真或假）。



# 排序

使用 ORDER BY 子句，可以按一个或多个属性列排序

-   **ASC**  ：升序（默认）
-   **DESC**  ：降序

可以按多个列进行排序，并且为每个列指定不同的排序方式：

> 【例】查询选修了 3 号课程的学生的学号及其成绩，查询结果按分数降序排列。

```sql
SELECT Sno, Grade
    FROM SC
    WHERE Cno= ' 3 '
    ORDER BY Grade DESC;
```



# 计算字段

在数据库服务器上完成数据的转换和格式化的工作往往比客户端上快得多，并且转换和格式化后的数据量更少的话可以减少网络通信量。

计算字段通常需要使用   **AS**   来取别名，否则输出的时候字段名为计算表达式。

```sql
SELECT col1 * col2 AS alias
FROM mytable;
```

**CONCAT()**   用于连接两个字段。许多数据库会使用空格把一个值填充为列宽，因此连接的结果会出现一些不必要的空格，使用 **TRIM()** 可以去除首尾空格。

```sql
SELECT CONCAT(TRIM(col1), '(', TRIM(col2), ')') AS concat_col
FROM mytable;
```

# 函数

各个 DBMS 的函数都是不相同的，因此不可移植，以下主要是 MySQL 的函数。

## 聚集函数

SQL 提供了许多聚集函数 用来实现统计查询

|函 数 |说 明|
| :---: | :---: |
| AVG() | 求平均值 |
| COUNT() | 计数 |
| MAX() | 求最大值 |
| MIN() | 求最小值 |
| SUM() |求和 |

AVG() 会忽略 NULL 行。

使用 DISTINCT 表示在计算时要取消 指定列 中的重复值； ALL 表示不取消重复值； 默认为 ALL 。

```sql
SELECT AVG(DISTINCT col1) AS avg_col
	FROM mytable;
```



> 【例】查询学生总人数

```sql
SELECT COUNT(*) FROM Student;
```

> 【例】查询选修了课程的学生人数。

```sql
SELECT COUNT(DISTINCT Sno)
	FROM SC ;
```

> 【例】计算 1 号课程的学生平均成绩。

```sql
SELECT AVG(Grade) FROM SC
	WHERE Cno= ' 1 ' ;
```

> 【例】查询 1 号课程的最高分数。

```sql
SELECT MAX(Grade) FROM SC
	WHERE Cno= ' 1 ' ;
```



## 文本处理

| 函数  | 说明  |
| :---: | :---: |
|  LEFT() |  左边的字符 |
| RIGHT() | 右边的字符 |
| LOWER() | 转换为小写字符 |
| UPPER() | 转换为大写字符 |
| LTRIM() | 去除左边的空格 |
| RTRIM() | 去除右边的空格 |
| LENGTH() | 长度 |
| SOUNDEX() | 转换为语音值 |

其中，  **SOUNDEX()**   可以将一个字符串转换为描述其语音表示的字母数字模式。

```sql
SELECT *
FROM mytable
WHERE SOUNDEX(col1) = SOUNDEX('apple')
```

## 日期和时间处理


- 日期格式：YYYY-MM-DD
- 时间格式：HH:\<zero-width space\>MM:SS

|函 数 | 说 明|
| :---: | :---: |
| ADDDATE() | 增加一个日期（天、周等）|
| ADDTIME() | 增加一个时间（时、分等）|
| CURDATE() | 返回当前日期 |
| CURTIME() | 返回当前时间 |
| DATE() |返回日期时间的日期部分|
| DATEDIFF() |计算两个日期之差|
| DATE_ADD() |高度灵活的日期运算函数|
| DATE_FORMAT() |返回一个格式化的日期或时间串|
| DAY()| 返回一个日期的天数部分|
| DAYOFWEEK() |对于一个日期，返回对应的星期几|
| HOUR() |返回一个时间的小时部分|
| MINUTE() |返回一个时间的分钟部分|
| MONTH() |返回一个日期的月份部分|
| NOW() |返回当前日期和时间|
| SECOND() |返回一个时间的秒部分|
| TIME() |返回一个日期时间的时间部分|
| YEAR() |返回一个日期的年份部分|

```sql
mysql> SELECT NOW();
```

```
2018-4-14 20:25:11
```

## 数值处理

| 函数 | 说明 |
| :---: | :---: |
| SIN() | 正弦 |
| COS() | 余弦 |
| TAN() | 正切 |
| ABS() | 绝对值 |
| SQRT() | 平方根 |
| MOD() | 余数 |
| EXP() | 指数 |
| PI() | 圆周率 |
| RAND() | 随机数 |

# 分组

把具有相同的数据值的行放在同一组中。使用 GROUP BY 子句分组

- 细化聚集函数的作用对象
  - 未对查询结果分组 聚集函数将作用于整个查询结果
  - 对查询结果分组后，聚集函数将分别作用于每个组

可以对同一分组数据使用汇总函数进行处理，例如求分组数据的平均值等。

### 分组方法

​	按指定的一列或多列值分组， **值相等的为一组**



- 使用 GROUP BY 子句后， SELECT 子句的列名列表中只能出现分组属性和聚集函数

- GROUP BY 子句的作用对象是查询的中间结果表
- 使用 HAVING 短语筛选最终输出结果
  只有满足 HAVING 短语指定条件的组才输出

指定的分组字段除了能按该字段进行分组，也会自动按该字段进行排序。

> 【例】求各个课程号及相应的选课人数。

```sql
SELECT Cno COUNT(*)  -- COUNT(Sno)
    FROM SC
    GROUP BY Cno
```

> 【例】查询选修了 3 门以上课程的学生学号

```sql
SELECT Sno
    FROM SC
    GROUP BY Sno
    HAVING COUNT(*) >3
```

> 【例 】 查询平均成绩大于等于 90 分的学生学号和平均成绩

```sql
SELECT Sno, AVG Grade
    FROM SC
    GROUP BY Sno
    HAVING AVG
    Grade AVG(Grade)>=90
```



GROUP BY 自动按分组字段进行排序，ORDER BY 也可以按汇总字段来进行排序。

```sql
SELECT col, COUNT(*) AS num
FROM mytable
GROUP BY col
ORDER BY num;
```



## `WHERE`和`HAVING`的区别

WHERE 过滤行，HAVING 过滤分组后的数据

行过滤应当先于分组过滤。

```sql
SELECT col, COUNT(*) AS num
    FROM mytable
    WHERE col > 2
        GROUP BY col
        HAVING num >= 2;
```

WHERE 子句中不能使用聚集函数；而 HAVING 短语中可以使用聚集函数

分组规定：

- GROUP BY 子句出现在 WHERE 子句之后，ORDER BY 子句之前；

- 除了汇总字段外，SELECT 语句中的每一字段都必须在 GROUP BY 子句中给出；

- NULL 的行会单独分为一组；

- 大多数 SQL 实现不支持 GROUP BY 列具有可变长度的数据类型。

  

# 连接

- 用来连接两个表的条件称为连接条件或连接谓词
- 连接谓词中的列名称为连接字段

连接条件中各 `连接字段` 的类型必须是` 可比的` ，但不必是相同的

连接用于连接多个表，使用 JOIN 关键字，并且条件语句使用 ON 而不是WHERE。

连接可以替换子查询，并且比子查询的效率一般会更快。

可以用 AS 给列名、计算字段和表名取别名，给表名取别名是为了简化 SQL 语句以及连接相同表。



## 内连接

### 连接条件的一般格式

```sql
[表名 1>.]< 列名 1> <比较运算符> [表名 2>.]<列名 2>
其中比较运算符为： =、 >、 <、 >=、 <=、 !=
```

包括相等连接和自然连接

内连接使用 INNER JOIN 关键字。

```sql
SELECT A.value, B.value
FROM tablea AS A INNER JOIN tableb AS B
ON A.key = B.key;
```





### 等值连接

可以不明确使用 INNER JOIN，而使用普通查询并在 WHERE 中将两个表中要连接的列用等值方法连接起来。

```sql
SELECT A.value, B.value
FROM tablea AS A, tableb AS B
WHERE A.key = B.key;
```

任何子句中引用表 1 和表 2 中同名属性时，都必须加`表名前缀`。 引用唯一属性名时可以省略表名 。

> 【例】查询每个学生及其选修课程的情况。

```sql
SELECT Student.* , SC.*
    FROM Student , SC
    WHERE Student.Sno = SC.Sno
```

![image-20250416155726158](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504161557349.png)



### 自然连接

自然连接是把同名列通过等值测试连接起来的，同名列可以有多个。

内连接和自然连接的区别：内连接提供连接的列，而自然连接自动连接所有同名列。

```sql
SELECT A.value, B.value
	FROM tablea AS A NATURAL JOIN tableb AS B;
```

```sql
SELECT Student.Sno, Sname, Ssex, Sage,Sdept, Cno, Grade
    FROM Student , SC
    WHERE Student.Sno = SC.Sno
```



### 自连接

自连接可以看成内连接的一种，只是连接的表是自身而已。

需要给表起别名以示区别
由于所有属性名都是同名属性，因此必须使用别名前缀

> 一张员工表，包含员工姓名和员工所属部门，要找出与 Jim 处在同一部门的所有员工姓名。

**子查询版本**

```sql
SELECT name
FROM employee
WHERE department = (
      SELECT department
      FROM employee
      WHERE name = "Jim");
```

**自连接版本**

```sql
SELECT e1.name
FROM employee AS e1 INNER JOIN employee AS e2
ON e1.department = e2.department
      AND e2.name = "Jim";
      
```

> 【例 】 查询每一门课的间接先修课 即先修课的先修课

```sql
SELECT FIRST.Cno, SECOND.Cpno
    FROM Course AS FIRST Course AS SECOND
    WHERE FIRST.Cpno = SECOND.Cno
```

![image-20250416162031456](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504161620541.png)



## 外连接

外连接保留了没有关联的那些行。分为左外连接，右外连接以及全外连接，左外连接就是保留左表没有关联的行。

检索所有顾客的订单信息，包括还没有订单信息的顾客。

```sql
SELECT Customers.cust_id, Customer.cust_name, Orders.order_id
FROM Customers LEFT OUTER JOIN Orders
ON Customers.cust_id = Orders.cust_id;
```

customers 表：

| cust_id | cust_name |
| :---: | :---: |
| 1 | a |
| 2 | b |
| 3 | c |

orders 表：

| order_id | cust_id |
| :---: | :---: |
|1    | 1 |
|2    | 1 |
|3    | 3 |
|4    | 3 |

结果：

| cust_id | cust_name | order_id |
| :---: | :---: | :---: |
| 1 | a | 1 |
| 1 | a | 2 |
| 3 | c | 3 |
| 3 | c | 4 |
| 2 | b | Null |

# 视图

视图是`虚拟的表`，本身不包含数据，也就不能对其进行索引操作。是从一个或几个基本表（或 **视图** 导出的`虚表`)

对视图的操作和对普通表的操作一样。

视图的定义是递归的，**可以定义基于该视图的新视图**

对视图的操作意味着对基表进行相对应的操作；但对视图的`更新 插入数据、删除、修改 `有一些限制

> DBMS 只存放视图的定义，不存放视图的数据，不会出现数据冗余

视图具有如下好处：

- 简化复杂的 SQL 操作，比如复杂的连接；
- 只使用实际表的一部分数据；
- 通过只给用户访问视图的权限，保证数据的安全性；
- 更改数据格式和表示。
- 基表中的数据发生变化 从视图中查询出的数据也改变

## 语句格式

```sql
create view <视图名> [(<列名1>[,<列名2>]…)] as <select语句>
	[with check option]
```

DBMS 执行 `CREATE VIEW` 语句时只是把视图的定义存入数据字典，并不执行其中的 `SELECT` 语句。在对视图进行操作时才按照视图定义生成数据，供用户使用。

>**SELECT** 语句 表示子查询，视图的属性列和数据都是由该子查询决定的。

### 视图列名

选项 `[(<列名1>[,<列名2>]…)]` 用来定义视图的列名。

组成视图的属性列名可以 **全部省略** 或 **全部指定**

> 省略 :
> 	由 `SELECT` 查询结果的目标列名组成

> 以下情况**必须明确指定**视图的所有列名
> 	(1)目标列中包含**聚集函数**或**表达式**
> 	(2)视图中包含出现在多个表中的**相同列名**
> 	(3)需要在视图中为某个列启用新的**更合适的名字**

### 视图约束

`WITH CHECK OPTION` 选项的作用
通过视图插入、删除或修改元组时，检查元组是否满足视图定义中的条件（即 **子查询中的条件表达式** ），如果不满足将拒绝执行这些操作。
如果视图定义中含有条件，建议选择 `WITH CHECK OPTION` 选项，以**约束更新的数据**。

## 创建视图（例子）

>【例 】 建立年龄小于 23 岁的学生视图，并要求数据更新时进行检查。

```sql
create view Sage_23 as select * from Student
	where Sage < 23
	with check option;
```

当通过视图更新学生元组时，系统将检查所更新的学生年龄是否小于 23 岁，不满足条件时系统将拒绝执行更新操作

> 【例 】 按系建立学生平均年龄的视图。

```sql
create view D-Sage(Sdept,Avgage)
	as select Sdept,AVG(Sage)
		from Student
		group by Sdept
```

因在 `SELECT` 目标表中有聚集函数 `AVG` ，视图定义中 **必须含有列名选项** 。

**视图的列名与 SELECT 后的列名相对应**，即使有与基本表相同的列名也不能省略。



>【例 】 建立计算机系选修了 C2 课的学生姓名和成绩的视图。

```sql
create view CS_SC(Sno,Sname,Grage)
	as select Student.Sno,Sname,Grade
		from Student,SC
		where Sdept='计算机' and 
			Student.Sno=SC.Sno and SC.Cno='C2'
```



> 基于视图的视图
>
> 【例 】 建立计算机系选修了 C2 课且成绩在 90 分以上的学生视图。

```sql
create view CS_90
	as select Sno,Sname,Grage
		From CS_SC
			where Grade>=90;
```



## 删除视图

```sql
DROP VIEW < 视图名 >;
```

该语句从数据字典中删除指定的视图定义

删除基表时，由该基表导出的所有视图定义都**必须显式删除**。



> 【 例 】 删除学生视图 CS_90

```sql
drop view CS_90
```

## 视图查询

从用户角度：查询视图与查询基本表相同

DBMS 实现视图查询的方法

实体化视图（ View Materialization）

1. 有效性检查：检查所查询的视图是否存在
2. 执行视图定义，将视图临时实体化，生成临时表
3. 查询视图转换为查询临时表
4. 查询完毕删除被实体化的视图 临时表



### 视图消解法

视图消解法（View Resolution）是一种数据库查询优化技术，主要用于处理查询中涉及视图的情况。

当用户执行一个查询时，这个查询可能会涉及一个或多个视图。由于视图本质上是一个虚拟表，它并不存储数据，而是通过存储的查询定义动态生成数据。

因此，当查询涉及视图时，**需要将视图的定义“消解”成一个直接的基本表查询**，以便执行。

1. **有效性检查**

   - 在查询中，如果涉及视图，首先需要检查这些视图是否有效。有效性检查的内容包括：检查**查询中的表和视图**是否存在。
   - 如果视图存在，数据库会从 **数据字典** 中查找视图的定义。**数据字典是存储数据库结构和元数据的地方**，其中记录了视图的创建语句（即视图的查询定义）。
2. **将视图定义与用户查询结合**

   - 一旦确定视图存在，下一步是将视图定义与用户的查询结合起来。这一步是核心操作，也就是 **视图消解**。
   - 具体来说，如果用户的查询中涉及视图，数据库会将**视图中的子查询**替换为**它在数据字典中的定义**。换句话说，视图定义的查询被“拉平”，`变成对实际的基本表的查询`。
   - 这通常涉及到将视图的查询语句作为一个子查询插入到用户查询的合适位置，替换掉视图的引用。通过这种方式，查询就变成了一个直接操作基本表的查询。
3. **执行修正后的查询**

   - 一旦完成视图消解，得到的查询就变成了标准的 SQL 查询。这个查询已经不再涉及视图，而是直接操作底层的基本表。


> 【 例 】 查询专业系，要求学生平均年龄小于 21 岁。
>
> ```sql
> CREATE VIEW D-Sage (Sdept, Avgage)
> AS SELECT Sdept, AVG(Sage)
> 	FROM Student
> 	GROUP BY Sdept;
> ```
>
> 

```sql
SELECT Sdept
	FROM D-Sage
	WHERE Avgage<21;
```

会被转化为：

```sql
SELECT Sdept
	FROM Student
	GROUP BY Sdept
	HAVING AVG(Sage)<21;
```

## 视图更新

对视图的数据插入、删除、修改最终转换为对基表的操作来进行

不过从用户角度：**更新视图与更新基本表相同**

指定 `WITH CHECK OPTION` 子句后， DBMS 在更新视图时会进行检查，防止用户通过视图对 **不属于视图范围内** 的基本表数据进行更新

`有些视图是不可更新的`
因为对这些视图的更新 **不能唯一地有意义地转换** 成对相应基本表的更新。**只有简单视图**能自由更新.

> 【 例 】 通过视图 Sage_23 插入学生刘敏的信息
> （（'20041' 刘敏 ' 女 数学 ''）。

```sql
INSERT INTO Sage_23
	VALUES ('20041' ,'刘敏','女','数学');
	
--被转换成-->

INSERT INTO Student
	VALUES ('20041' ,'刘敏','女','数学');


--视图定义语句--
CREATE VIEW Sage_23
	AS SELECT * FROM Student
		WHERE Sage < 23
	WITH CHECK OPTION;
```

> 【 例 】 通过视图 Sage_23 删除学生王茵的记录。

```sql
DELETE FROM Sage_23
	WHERE Sname='王茵';
	
--被转换成-->

DELETE FROM Student
	WHERE Sname='王茵' AND Sage < 23;
	
--视图定义语句--
CREATE VIEW Sage_23
	AS SELECT * FROM Student
		WHERE Sage < 23
	WITH CHECK OPTION;
```



>【 例 】 通过视图 Sage_23 修改学生王茵的年龄为
>22 岁。

```sql
UPDATE Sage_23
	SET Sage=22
	WHERE Sname='王茵';
	
--被转换成-->

UPDATE Student
	SET Sage=22
	WHERE Sname='王茵';
	
--视图定义语句--
CREATE VIEW Sage_23
	AS SELECT * FROM Student
		WHERE Sage < 23
	WITH CHECK OPTION;
```

因修改后学生年龄小于 23 岁，该操作可直接对表Student 修改。

### 更新限制

**视图中有聚合函数**（比如 `SUM()`、`AVG()`、`COUNT()` 等）

- ✖️ 不能更新，因为聚合后的数据不是一行一行基础表直接对应的。

**视图中有分组（GROUP BY）或分区（HAVING）**

- ✖️ 不能更新，因为一组数据聚合成一条记录了，无法追溯到原始行。

**视图是多表连接（JOIN）而成的**

- 由两个以上基本表导出的视图不允许更新。

- ❗ 更新有限制：
  - 如果只改单一基础表的字段，还可以（条件复杂）
  - 如果改多个表的字段，**一般禁止**，因为系统搞不清到底要更新哪个表。

**视图中有 DISTINCT**

- ✖️ 不能更新，因为去重后，视图中的一行可能对应原表的多行，无法确定更新谁。

**视图中有计算列（比如 a+b 这样的表达式）**

- ✖️ 不能直接更新，因为计算列没法直接映射到基础表里的字段。

**视图中缺少主键或基础表关键列**

- ✖️ 不能更新，因为数据库不能确定唯一定位要修改哪条记录。

**视图用了子查询（尤其是复杂的嵌套子查询）**

- ✖️ 通常不能更新，子查询结果只是临时生成的，不能映射回去。

**视图用了 UNION / UNION ALL**

- ✖️ 不能更新，因为是两个（或多个）表集合在一起的，更新方向不明确。

**视图的字段来自字段表达式或常数**

若视图的字段来自字段表达式或常数，则不允许对此视图执行 `INSERT` 和` UPDATE` 操作，但允许执行 DELETE操作。



## 视图的作用

视图 `在一定程度上` 保证了数据的逻辑独立性

> ?使用户外模式保持不变，用户应用程序通过视图仍然能够查找数据。

简化了用户 视图

- 视图使用户把注意力集中在自己所关系的数据上，简化
  了用户的数据结构；
- 定义视图能够简化用户的操作 适当的利用视图可以更清晰的表达查询
  - 基于多张表连接形成的视图
  - 基于复杂嵌套查询的视图
  - 含导出属性的视图

视图使用户以不同 角度 看待相同的数

视图提供了安全保护功能,对不同用户定义不同视图，使每个用户只能看到他有权看到的数据，实现对机密数据的保护。

可以通过 WITH CHECK OPTION 对关键数据定义操作限制，比如 操作时间的限制 。

# 存储过程

存储过程可以看成是对一系列 SQL 操作的批处理。

使用存储过程的好处：

- 代码封装，保证了一定的安全性；
- 代码复用；
- 由于是预先编译，因此具有很高的性能。

命令行中创建存储过程需要自定义分隔符，因为命令行是以 ; 为结束符，而存储过程中也包含了分号，因此会错误把这部分分号当成是结束符，造成语法错误。

包含 in、out 和 inout 三种参数。

给变量赋值都需要用 select into 语句。

每次只能给一个变量赋值，不支持集合的操作。

```sql
delimiter //

create procedure myprocedure( out ret int )
    begin
        declare y int;
        select sum(col1)
        from mytable
        into y;
        select y*y into ret;
    end //

delimiter ;
```

```sql
call myprocedure(@ret);
select @ret;
```

# 游标

在存储过程中使用游标可以对一个结果集进行移动遍历。

游标主要用于交互式应用，其中用户需要对数据集中的任意行进行浏览和修改。

使用游标的四个步骤：

1. 声明游标，这个过程没有实际检索出数据；
2. 打开游标；
3. 取出数据；
4. 关闭游标；

```sql
delimiter //
create procedure myprocedure(out ret int)
    begin
        declare done boolean default 0;

        declare mycursor cursor for
        select col1 from mytable;
        # 定义了一个 continue handler，当 sqlstate '02000' 这个条件出现时，会执行 set done = 1
        declare continue handler for sqlstate '02000' set done = 1;

        open mycursor;

        repeat
            fetch mycursor into ret;
            select ret;
        until done end repeat;

        close mycursor;
    end //
 delimiter ;
```

# 触发器（Trigger）

**触发器** 是一种由数据库自动执行的程序，用于在特定事件（如插入、删除、更新）发生时，自动执行一些指定的操作。常用于：

- 自动检查约束（如你前面的问题）
- 自动记录日志
- 实现复杂的业务规则



触发器会在某个表执行以下语句时而自动执行：DELETE、INSERT、UPDATE。

触发器必须指定在语句执行之前还是之后自动执行，之前执行使用 BEFORE 关键字，之后执行使用 AFTER 关键字。BEFORE 用于数据验证和净化，AFTER 用于审计跟踪，将修改记录到另外一张表中。

INSERT 触发器包含一个名为 NEW 的虚拟表。

```sql
CREATE TRIGGER mytrigger AFTER INSERT ON mytable
FOR EACH ROW SELECT NEW.col into @result;

SELECT @result; -- 获取结果
```

DELETE 触发器包含一个名为 OLD 的虚拟表，并且是只读的。

UPDATE 触发器包含一个名为 NEW 和一个名为 OLD 的虚拟表，其中 NEW 是可以被修改的，而 OLD 是只读的。

MySQL 不允许在触发器中使用 CALL 语句，也就是不能调用存储过程。



```sql
CREATE TRIGGER <触发器名>
 {BEFORE|AFTER} <触发事件(INSERT|DELETE|UPDATE)> ON <表名>
 FOR EACH {ROW | STATEMENT}
 [WHEN <触发条件>]
BEGIN
    -- 触发器执行的 SQL 语句块
END;
```

### ✅ 关键字解释：

| 关键词                 | 作用说明                                           |
| ---------------------- | -------------------------------------------------- |
| `CREATE TRIGGER`       | 创建触发器                                         |
| `trigger_name`         | 触发器名称（一个数据库中唯一）                     |
| `BEFORE` 或 `AFTER`    | 指明是在操作 **之前** 还是 **之后** 执行           |
| `INSERT/UPDATE/DELETE` | 指明要响应哪种类型的操作                           |
| `ON table_name`        | 指定在哪个表上定义该触发器                         |
| `FOR EACH ROW`         | 表示每插入/更新/删除一行记录，就执行一次触发器代码 |
| `BEGIN...END`          | 包含触发器要执行的 SQL 语句块                      |

------

## 三、访问新旧数据

在 `UPDATE` 或 `INSERT` 时，触发器中可以使用如下关键字访问行数据：

| 关键字            | 含义                   |
| ----------------- | ---------------------- |
| `NEW.column_name` | 表示新插入或更新后的值 |
| `OLD.column_name` | 表示被删除或更新前的值 |

### 示例：

```sql
-- 更新工资时记录日志
CREATE TRIGGER log_salary_change
AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
    INSERT INTO salary_log(emp_id, old_salary, new_salary, change_date)
    VALUES (OLD.id, OLD.salary, NEW.salary, NOW());
END;
```

------

## 四、触发器使用举例

### 1. 插入前检查约束

```sql
CREATE TRIGGER check_age
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.age < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '年龄不能为负数';
    END IF;
END;
```

### 2. 自动记录删除操作

```sql
CREATE TRIGGER log_delete
AFTER DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO deleted_orders_log(order_id, delete_time)
    VALUES (OLD.id, NOW());
END;
```

------

## 五、注意事项

### 1. 不能使用事务控制语句

触发器中 **不能使用 `COMMIT`、`ROLLBACK`、`SAVEPOINT`** 等语句。

### 2. 每个表最多定义 6 个触发器（MySQL 中）：

- BEFORE INSERT
- AFTER INSERT
- BEFORE UPDATE
- AFTER UPDATE
- BEFORE DELETE
- AFTER DELETE

### 3. `SIGNAL SQLSTATE` 用于触发错误并阻止操作（MySQL 5.5+）：

```sql
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = '错误信息';
```

------

## 六、小结

| 类型          | 说明                                         |
| ------------- | -------------------------------------------- |
| BEFORE INSERT | 插入之前自动执行，常用于数据校验或默认值处理 |
| AFTER INSERT  | 插入之后自动执行，常用于写日志等             |
| BEFORE UPDATE | 更新之前执行，可检查或限制数据               |
| AFTER UPDATE  | 更新后执行，常用于写日志、历史记录           |
| BEFORE DELETE | 删除前检查                                   |
| AFTER DELETE  | 删除后记录日志                               |

------

是否需要我给你写一个“完整的触发器模板”和带注释的示例？















# 事务管理

基本术语：

- 事务（transaction）指一组 SQL 语句；
- 回退（rollback）指撤销指定 SQL 语句的过程；
- 提交（commit）指将未存储的 SQL 语句结果写入数据库表；
- 保留点（savepoint）指事务处理中设置的临时占位符（placeholder），你可以对它发布回退（与回退整个事务处理不同）。

不能回退 SELECT 语句，回退 SELECT 语句也没意义；也不能回退 CREATE 和 DROP 语句。

MySQL 的事务提交默认是隐式提交，每执行一条语句就把这条语句当成一个事务然后进行提交。当出现 START TRANSACTION 语句时，会关闭隐式提交；当 COMMIT 或 ROLLBACK 语句执行后，事务会自动关闭，重新恢复隐式提交。

设置 autocommit 为 0 可以取消自动提交；autocommit 标记是针对每个连接而不是针对服务器的。

如果没有设置保留点，ROLLBACK 会回退到 START TRANSACTION 语句处；如果设置了保留点，并且在 ROLLBACK 中指定该保留点，则会回退到该保留点。

```sql
START TRANSACTION
// ...
SAVEPOINT delete1
// ...
ROLLBACK TO delete1
// ...
COMMIT
```

# 字符集

基本术语：

- 字符集为字母和符号的集合；
- 编码为某个字符集成员的内部表示；
- 校对字符指定如何比较，主要用于排序和分组。

除了给表指定字符集和校对外，也可以给列指定：

```sql
CREATE TABLE mytable
(col VARCHAR(10) CHARACTER SET latin COLLATE latin1_general_ci )
DEFAULT CHARACTER SET hebrew COLLATE hebrew_general_ci;
```

可以在排序、分组时指定校对：

```sql
SELECT *
FROM mytable
ORDER BY col COLLATE latin1_general_ci;
```

# 权限管理

## 权限类型

SQL中的权限大致分为两类：

| 类别                     | 说明                                   | 举例                                     |
| :----------------------- | :------------------------------------- | :--------------------------------------- |
| **系统权限（全局权限）** | 对整个数据库服务器有效的权限           | 创建数据库、创建用户、关机、备份服务器等 |
| **对象权限（局部权限）** | 对某张表、某个视图、某个过程的操作权限 | 查询某表、更新某视图、执行某存储过程等   |



不同的数据对象有不同的操作权限：

| 模式（架构） | CREATE TABLE                                 |
| ------------ | -------------------------------------------- |
| 表           | SELECT, INSERT, DELETE, UPDATE，ALTER, INDEX |
| 属性列       | SELECT, INSERT, DELETE, UPDATE               |
| 视图         | SELECT, INSERT, DELETE, UPDATE               |



每种操作的作用（以表操作为例）：

| 权限           | 作用               |
| :------------- | :----------------- |
| **SELECT**     | 查询表中的数据     |
| **INSERT**     | 向表中插入数据     |
| **UPDATE**     | 更新表中已有数据   |
| **DELETE**     | 删除表中已有数据   |
| **ALTER**      | 修改表结构         |
| **INDEX**      | 创建和删除表的索引 |
| **REFERENCES** | 创建引用该表的外键 |

除了表，视图、存储过程、函数等也有各自类似的权限。



## 授权和收回权限

SQL中有两个关键词特别重要：

- `GRANT`（授权）
- `REVOKE`（收回权限）

### 授权（GRANT）

```sql
GRANT 权限列表
	ON 对象名
	TO 用户名
	[WITH GRANT OPTION];
```

- `WITH GRANT OPTION`：允许被授权的用户继续把权限授给别人（可转授权）。

**例子：**

```sql
GRANT SELECT, INSERT
	ON student
	TO user1;
```

 给 `user1` 用户授予对 `student` 表的查询（SELECT）和插入（INSERT）权限。

如果加上 `WITH GRANT OPTION`：

```sql
GRANT SELECT
	ON student
	TO user1
	WITH GRANT OPTION;
```

允许 `user1` 再把 SELECT 权限授予其他人

**例子：**

```sql
GRANT ALL PRIVILIGES
	on table student,teacher
	to user1,user2;
```







------

### 收回（REVOKE）

**语法：**

```
sql复制编辑REVOKE 权限列表
ON 对象名
FROM 用户名;
```

**例子：**

```
sql复制编辑REVOKE SELECT
ON student
FROM user1;
```

👉 收回 `user1` 对 `student` 表的查询权限。

注意：

- 如果权限是带 `WITH GRANT OPTION` 授的，收回的时候会**连带收回被他转授出去的权限**，很严格。



## 用户管理

一般用**管理员账号**（比如root，dba账号）来创建、管理用户：

| 动作     | 命令                                        |
| -------- | ------------------------------------------- |
| 创建用户 | `CREATE USER 用户名 IDENTIFIED BY '密码';`  |
| 删除用户 | `DROP USER 用户名;`                         |
| 修改密码 | `ALTER USER 用户名 IDENTIFIED BY '新密码';` |



MySQL 的账户信息保存在 mysql 这个数据库中。

```sql
USE mysql;
SELECT user FROM user;
```

**创建账户**  

新创建的账户没有任何权限。

```sql
CREATE USER myuser IDENTIFIED BY 'mypassword';
```

**修改账户名**  

```sql
RENAME USER myuser TO newuser;
```

**删除账户**  

```sql
DROP USER myuser;
```

**查看权限**  

```sql
SHOW GRANTS FOR myuser;
```

**授予权限**  

账户用 username@host 的形式定义，username@% 使用的是默认主机名。

```sql
GRANT SELECT, INSERT ON mydatabase.* TO myuser;
```

**删除权限**  

GRANT 和 REVOKE 可在几个层次上控制访问权限：

- 整个服务器，使用 GRANT ALL 和 REVOKE ALL；
- 整个数据库，使用 ON database.\*；
- 特定的表，使用 ON database.table；
- 特定的列；
- 特定的存储过程。

```sql
REVOKE SELECT, INSERT ON mydatabase.* FROM myuser;
```

**更改密码**  

必须使用 Password() 函数进行加密。

```sql
SET PASSWROD FOR myuser = Password('new_password');
```

# 参考资料

- BenForta. SQL 必知必会 [M]. 人民邮电出版社, 2013.
