下面是整理后的《MySQL Python 连接与使用》笔记，已去除冗余小标题如“实例”，统一了格式，并补充了部分缺失内容（如常用查询语句示例、异常处理建议、数据类型映射等）：

------

# MySQL Python 连接与使用

MySQL 是最流行的开源关系型数据库之一，而 Python 是当今最受欢迎的编程语言之一。将 Python 与 MySQL 结合使用，可以让我们轻松地开发数据库驱动的应用程序。

本文将介绍如何使用 Python 连接和操作 MySQL 数据库，内容包括：

- 安装 Python MySQL 驱动
- 建立和关闭数据库连接
- 执行 SQL 查询
- 事务管理与错误处理
- 最佳实践与性能建议

------

## 准备工作

### 安装必要的软件

请确保已安装：

- Python（推荐 3.6 或以上）
- MySQL Server（可选社区版）
- Python MySQL 驱动（推荐官方：`mysql-connector-python`，或第三方 `pymysql`）

### 安装驱动

使用 pip 安装驱动：

```bash
pip install mysql-connector-python
# 或
pip install pymysql
```

------

## 连接 MySQL 数据库

### 使用 mysql-connector-python

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

print("数据库连接成功")
```

### 使用 PyMySQL

```python
import pymysql

db = pymysql.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

print("数据库连接成功")
```

### 连接参数说明

- `host`: 主机名（本地为 `"localhost"`）
- `user`: 数据库用户名
- `password`: 登录密码
- `database`: 数据库名称（可选）

------

## 执行 SQL 查询

### 创建游标对象

```python
cursor = db.cursor()
```

### SELECT 查询

```python
cursor.execute("SELECT * FROM your_table")
results = cursor.fetchall()
for row in results:
    print(row)
```

### INSERT、UPDATE、DELETE 操作

```python
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("张三", 25)
cursor.execute(sql, values)
db.commit()
print(cursor.rowcount, "条记录插入成功")
```

批量插入

```python
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = [
    ("张三", 25),
    ("李四", 30),
    ("王五", 22)
]
cursor.executemany(sql, values)
```



### 使用参数化查询（防止 SQL 注入）

```python
sql = "SELECT * FROM users WHERE name = %s"
name = ("张三",)
cursor.execute(sql, name)
results = cursor.fetchall()
```

```python
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
params = ("李四", 28)
cursor.execute(sql, params)
```





## 事务管理

### 使用事务

```python
try:
    cursor.execute("START TRANSACTION")
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    db.commit()
    print("事务执行成功")
except Exception as e:
    db.rollback()
    print("事务执行失败:", e)
```

------

## 错误处理

### 捕获数据库错误

对于 `mysql-connector-python`：

```python
import mysql.connector

try:
    cursor.execute("SELECT * FROM non_existent_table")
except mysql.connector.Error as err:
    print("数据库错误:", err)
```

对于 `pymysql`：

```python
import pymysql

try:
    cursor.execute("SELECT * FROM non_existent_table")
except pymysql.MySQLError as err:
    print("数据库错误:", err)
```

### 常见错误码

| 错误码 | 含义说明                      |
| ------ | ----------------------------- |
| 1045   | 访问被拒绝（用户名/密码错误） |
| 1049   | 未知数据库                    |
| 1146   | 表不存在                      |
| 1062   | 重复键值（如主键冲突）        |

------

## 关闭连接

### 手动关闭连接

```python
cursor.close()
db.close()
print("数据库连接已关闭")
```

### 使用 with 语句自动关闭连接

```python
import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
) as db:
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
```

------

## 最佳实践

### 使用连接池

适用于高并发场景：

```python
from mysql.connector import pooling

db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

db = db_pool.get_connection()
cursor = db.cursor()
```

### 使用 ORM 框架

如使用 SQLAlchemy：

```python
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://user:password@localhost/dbname")
```

或使用 Django ORM，适合 Web 项目。

------

## 常用扩展内容（补充）

### Python 类型与 MySQL 类型映射（部分）

| Python 类型 | MySQL 类型        |
| ----------- | ----------------- |
| `str`       | `VARCHAR`, `TEXT` |
| `int`       | `INT`, `BIGINT`   |
| `float`     | `FLOAT`, `DOUBLE` |
| `datetime`  | `DATETIME`        |
| `bool`      | `TINYINT(1)`      |

### 建议结构化封装

可将连接、查询封装为类或工具函数，提高代码复用性。
