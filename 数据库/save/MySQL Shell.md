## 📌 一、MySQL Shell 简介

MySQL Shell（`mysqlsh`）是 MySQL 官方提供的新一代命令行工具，支持多种语言（SQL、JavaScript、Python）和更现代化的交互方式。相比传统的 `mysql` 客户端，MySQL Shell 功能更强大，特别适合开发者和管理员。

------

## 🚀 二、启动和连接

### 1. 启动 MySQL Shell

```bash
mysqlsh
```

启动后会进入交互式命令行界面（默认 JS 模式）。

### 2. 连接 MySQL 实例

#### 方法一：命令行直接连接

```bash
mysqlsh [用户名]@[主机地址]:[端口]
```

示例：

```bash
mysqlsh root@localhost:3306
```

连接后会提示输入密码。

#### 方法二：使用命令连接

在 MySQL Shell 启动后输入：

```js
\connect root@localhost:3306
```

### 3. 使用密码连接

```bash
mysqlsh --uri root@localhost:3306
# 会自动提示输入密码
```

或

```bash
mysqlsh --uri root:password@localhost:3306
# 直接提供密码（不安全，不推荐）
```

------

## 🗂 三、基本操作命令

### 1. 查看当前连接信息

```js
\status
```

### 2. 查看所有数据库

```sql
SHOW DATABASES;
```

或：

```js
\sql
SHOW DATABASES;
```

### 3. 切换数据库

```sql
USE 数据库名;
```

例子：

```sql
USE mysql;
```

------

## 🔄 四、语言模式切换（SQL / JavaScript / Python）

MySQL Shell 支持三种语言模式：

- SQL 模式：标准 SQL
- JavaScript 模式：默认模式，命令以 JS 风格写法为主
- Python 模式：可使用 Py 风格编程操作数据库对象

### 切换命令：

```bash
\sql      # 切换到 SQL 模式
\js       # 切换到 JavaScript 模式
\py       # 切换到 Python 模式
```

### 当前语言查看：

```bash
\status
```

------

## 📚 五、常用命令速查表

| 命令                 | 说明                             |
| -------------------- | -------------------------------- |
| `\connect`           | 连接到数据库                     |
| `\sql`, `\js`, `\py` | 切换语言模式                     |
| `\status`            | 显示连接信息和当前模式           |
| `\quit` 或 `\exit`   | 退出 MySQL Shell                 |
| `\help` 或 `\?`      | 显示所有可用命令                 |
| `\show`              | 显示当前连接的数据库、模式等状态 |
| `\use <database>`    | 切换数据库（JS/Py 模式下）       |
| `\history`           | 查看历史命令记录                 |
| `\edit`              | 编辑长命令                       |
| `\source file.sql`   | 执行 SQL 脚本文件                |

------

## 🛠 六、MySQL Shell 支持的高级功能

### 1. 执行脚本

在 shell 启动参数中直接执行脚本：

```bash
mysqlsh --uri root@localhost:3306 --file script.sql
```

### 2. 使用 Python/JavaScript 操作数据库对象（对象模型）

```js
\js
var session = shell.getSession()
var myDb = session.getSchema("test")
var myTable = myDb.getTable("users")
var result = myTable.select(["id", "name"]).execute()
print(result.fetchAll())
```

------

## 🧪 七、实用小技巧

### 1. 多行输入

以 `\` 结尾表示继续下一行：

```sql
SELECT *
FROM users \
WHERE id > 100;
```

### 2. 配置文件路径

默认配置路径：

- Linux/macOS: `~/.mysqlsh`
- Windows: `C:\Users\你的用户名\AppData\Roaming\MySQL\mysqlsh`

可以在里面设置登录别名、启动参数等。

------

## 📤 八、退出 MySQL Shell

```bash
\quit
```

或

```bash
\exit
```

------

## 📖 九、参考资料

- [MySQL Shell 官方文档](https://dev.mysql.com/doc/mysql-shell/8.0/en/)
- `mysqlsh --help` 获取本地帮助信息

