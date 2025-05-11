以下是使用 **MySQL Shell 的 JavaScript 模式**操作 MySQL 数据库的详细指南，涵盖连接数据库、执行 SQL、处理结果、事务管理以及高级功能的使用。通过示例代码和分步说明，帮助你快速上手。

---

### **一、安装与启动 MySQL Shell**

1. **安装 MySQL Shell**  
   - 从 [MySQL 官网](https://dev.mysql.com/downloads/shell/) 下载对应系统的安装包。
   - 或通过包管理器安装（如 Ubuntu）：
     ```bash
     sudo apt-get install mysql-shell
     ```

2. **启动 MySQL Shell**  
   在终端输入以下命令：
   ```bash
   mysqlsh
   ```
   - 默认进入 **JavaScript 模式**，提示符为 `MySQL JS>`。

---

### **二、连接数据库**
#### 1. 基础连接方式
```javascript
// 连接到本地 MySQL 服务器（用户 root，密码 123456）
shell.connect('root@localhost:3306', '123456');
```

#### 2. 指定更多参数
```javascript
// 显式指定协议、主机、端口、用户和密码
const session = mysqlx.getSession({
  host: 'localhost',
  port: 3306,
  user: 'root',
  password: '123456'
});

// 验证连接是否成功
session.sql("SELECT 'Connected!' AS status").execute()
  .then(result => console.log(result.fetchOne()))
  .catch(err => console.error("连接失败:", err));
```

---

### **三、执行 SQL 查询**
#### 1. 直接执行 SQL 语句
```javascript
// 执行 SELECT 查询
session.sql("SELECT * FROM sakila.actor LIMIT 5")
  .execute()
  .then(result => {
    const rows = result.fetchAll();
    console.log("查询结果:", rows);
  });
```

#### 2. 执行 DML 操作（INSERT/UPDATE/DELETE）
```javascript
// 插入数据
session.sql(`
  INSERT INTO sakila.actor (first_name, last_name)
  VALUES ('John', 'Doe')
`).execute()
  .then(() => console.log("插入成功！"))
  .catch(err => console.error("插入失败:", err));
```

#### 3. 使用预处理语句（防止 SQL 注入）
```javascript
// 使用占位符 ? 传递参数
const query = "INSERT INTO sakila.actor (first_name, last_name) VALUES (?, ?)";
const params = ['Jane', 'Smith'];

session.sql(query)
  .bind(params)
  .execute()
  .then(() => console.log("预处理插入成功！"));
```

---

### **四、处理查询结果**
#### 1. 获取结果集
```javascript
session.sql("SELECT actor_id, first_name FROM sakila.actor")
  .execute()
  .then(result => {
    // 逐行读取
    let row;
    while ((row = result.fetchOne())) {
      console.log(`ID: ${row[0]}, Name: ${row[1]}`);
    }

    // 或一次性获取全部结果
    const allRows = result.fetchAll();
    console.log("全部数据:", allRows);
  });
```

#### 2. 获取元数据（列信息）
```javascript
result.getColumns().forEach(column => {
  console.log(`列名: ${column.getColumnName()}, 类型: ${column.getType()}`);
});
```

---

### **五、事务管理**
```javascript
// 开启事务
session.startTransaction();

try {
  // 执行多个操作
  await session.sql("UPDATE account SET balance = balance - 100 WHERE id = 1").execute();
  await session.sql("UPDATE account SET balance = balance + 100 WHERE id = 2").execute();

  // 提交事务
  await session.commit();
  console.log("事务提交成功！");
} catch (err) {
  // 回滚事务
  await session.rollback();
  console.error("事务回滚:", err);
}
```

---

### **六、使用 X DevAPI 操作文档存储（NoSQL）**
MySQL Shell 支持通过 JavaScript 直接操作 JSON 文档（需使用 MySQL 的 `X DevAPI`）。

#### 1. 访问文档集合
```javascript
// 获取或创建集合（类似表）
const schema = session.getSchema('test');
const collection = schema.createCollection('users');

// 插入文档
collection.add({ name: 'Alice', age: 30, email: 'alice@example.com' }).execute();
```

#### 2. 查询文档
```javascript
// 查找所有年龄大于 25 的用户
collection.find('age > :ageParam')
  .bind('ageParam', 25)
  .execute()
  .then(result => {
    result.forEach(doc => console.log("用户:", doc));
  });
```

---

### **七、实用技巧**
#### 1. 切换模式
```javascript
// 临时切换到 SQL 模式执行命令
\sql
SELECT * FROM sakila.actor;
\js  // 切换回 JavaScript 模式
```

#### 2. 脚本化操作
将操作保存为 `.js` 文件（如 `script.js`），通过 Shell 执行：
```bash
mysqlsh --js -f script.js
```

#### 3. 断开连接
```javascript
session.close();  // 关闭当前会话
shell.disconnect(); // 断开所有连接
```

---

### **八、注意事项**
1. **模式兼容性**：确保 MySQL 服务器版本支持 X DevAPI（MySQL 5.7+ 支持基础功能，8.0+ 功能更完整）。  
2. **错误处理**：始终使用 `try/catch` 或 `.catch()` 处理异步操作中的错误。  
3. **性能优化**：批量操作时使用事务或预处理语句提升效率。

---

### **九、常见问题**
#### Q1：JavaScript 模式下如何执行多行 SQL？
用反引号 `` ` `` 包裹多行 SQL：
```javascript
session.sql(`
  CREATE TABLE IF NOT EXISTS test.books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100)
  )
`).execute();
```

#### Q2：如何导入外部 JavaScript 模块？
在 MySQL Shell 中：
```javascript
// 加载外部模块
const fs = require('fs');
const data = fs.readFileSync('data.json');
```

#### Q3：如何调试代码？
使用 `print()` 或 `console.log()` 输出变量：
```javascript
const result = await session.sql("SELECT NOW()").execute();
console.log("当前时间:", result.fetchOne());
```

---

### **总结**
通过 MySQL Shell 的 JavaScript 模式，你可以：
- **直接执行 SQL**（需用 `session.sql()` 包裹语句）。
- **操作 JSON 文档**（利用 X DevAPI）。
- **编写脚本自动化管理数据库**。

如果需要更复杂的逻辑（如循环、条件判断），可以结合 JavaScript 的完整语法实现灵活控制！ 😊