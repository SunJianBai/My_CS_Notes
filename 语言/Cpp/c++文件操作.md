下面是整理后的文章，并加上了适当的补充内容：

---

# C++ 文件操作

在 C++ 中，文件操作需要包含头文件 `<fstream>`。文件操作时，通常不建议使用 `std::string` 类型，建议使用字符数组（如 `char buf[64]`）来处理文件内容。

C++ 中的文件类型分为两种：

1. **文本文件** - 文件以 ASCII 码形式存储，易于编辑和查看。
2. **二进制文件** - 文件以二进制格式存储，内容不可直接查看，适用于存储结构化数据。

C++ 中操作文件的三大类：

- **`ofstream`**：用于写操作。
- **`ifstream`**：用于读操作。
- **`fstream`**：用于读写操作。

## 文本文件操作

### 一、写文件

1. **包含头文件**
   ```cpp
   #include <fstream>
   ```

2. **创建文件流对象**
   ```cpp
   std::ofstream ofs;
   ```

3. **打开文件**
   ```cpp
   ofs.open("文件路径", 打开方式);
   ```

4. **写数据**
   ```cpp
   ofs << "写入的数据";
   ```

5. **关闭文件**
   ```cpp
   ofs.close();
   ```

#### 文件打开方式

- `ios::app`：追加模式。所有写入都追加到文件末尾。
- `ios::ate`：文件打开后定位到文件末尾。
- `ios::in`：打开文件用于读取。
- `ios::out`：打开文件用于写入。
- `ios::trunc`：如果文件已存在，打开时内容会被清空。
- `ios::binary`：二进制方式。

可以组合使用文件打开方式，用 `|` 隔开，如 `ios::out | ios::app`。

### 二、读文件

1. **包含头文件**
   ```cpp
   #include <fstream>
   ```

2. **创建流对象**
   ```cpp
   std::ifstream ifs;
   ```

3. **打开文件并判断文件是否成功打开**
   ```cpp
   ifs.open("文件路径", 打开方式);
   if (!ifs.is_open()) {
       std::cerr << "文件打开失败!" << std::endl;
       return;
   }
   ```

4. **读取数据**
   - 直接读取，用字符数组接收：
     ```cpp
     char buf[1024] = { 0 }; // 初始化字符数组
     while (ifs >> buf) { // 逐个接收字符，直到文件末尾
         std::cout << buf;
     }
     ```
   - 逐行读取，用字符数组接收：
     ```cpp
     char buf[1024] = { 0 };
     while (ifs.getline(buf, sizeof(buf))) {
         std::cout << buf << std::endl;
     }
     ```
   - 读取到 `std::string` 中：
     ```cpp
     std::string buf;
     while (getline(ifs, buf)) {
         std::cout << buf << std::endl;
     }
     ```
   - 逐个字符读取：
     ```cpp
     char c;
     while ((c = ifs.get()) != EOF) { // EOF 表示文件末尾
         std::cout << c;
     }
     ```

5. **关闭文件**
   ```cpp
   ifs.close();
   ```

#### 示例：读取文件并跳过第一行

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main() {
    std::ifstream input("data.txt");
    std::string line;

    // 跳过第一行
    std::getline(input, line);

    while (std::getline(input, line)) {
        std::istringstream iss(line);
        int studentId;
        std::string name, className;
        double score;

        // 解析每一行数据
        iss >> studentId >> name >> className >> score;

        std::cout << "学号：" << studentId << ", 姓名：" << name << ", 班级：" << className << ", 成绩：" << score << std::endl;
    }

    input.close();

    return 0;
}
```

## 读写二进制文件

### 写入二进制文件

```cpp
std::ofstream ofs("t.txt", std::ios::out | std::ios::binary);

struct Person {
    char name[64];
    int age;
};

Person p = { "张三", 18 };

ofs.write(reinterpret_cast<const char*>(&p), sizeof(Person)); // 强转为 const char* 类型，写入指定字节数
ofs.close();
```

### 读取二进制文件

```cpp
std::ifstream ifs("t.txt", std::ios::in | std::ios::binary);

Person p;
ifs.read(reinterpret_cast<char*>(&p), sizeof(Person)); // 读取指定字节数
std::cout << "姓名：" << p.name << ", 年龄：" << p.age << std::endl;
ifs.close();
```

## C语言文件操作（补充）

### 数据流与缓冲区

1. **数据流**：文件操作中，数据的传输是以流的形式进行的。数据从程序移入和移出时，都通过流进行。流是字节的连续移动。
   
2. **缓冲区**：操作系统提供的额外内存，用于临时存放即将执行的文件数据。缓冲区的目的是提高文件存取效率，因为内存访问速度远快于硬盘。

### 文件类型

- **文本文件**：以字符编码（如 ASCII）保存，内容可由人类阅读。
- **二进制文件**：以二进制格式保存数据，通常用于保存非文本数据，如图像、音频等，存取速度较快，占用空间小。

### 文件存取方式

- **顺序存取**：按照文件的字节顺序读取数据。常用于文本文件。
- **随机存取**：按需读取文件中的任意部分，常用于二进制文件，适用于存储结构化数据。

### C 语言文件操作函数

1. **`fopen`**：打开文件。
   ```cpp
   FILE *fopen(const char *filename, const char *mode);
   ```

2. **`fclose`**：关闭文件。
   ```cpp
   int fclose(FILE *stream);
   ```

3. **`fread` / `fwrite`**：读取或写入二进制数据。
   ```cpp
   size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
   size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
   ```

4. **`fseek` / `ftell`**：移动文件指针和获取当前文件指针位置。
   ```cpp
   int fseek(FILE *stream, long int offset, int origin);
   long int ftell(FILE *stream);
   ```

5. **`feof`**：判断文件是否读取到末尾。
   ```cpp
   int feof(FILE *stream);
   ```

6. **`rename`**：重命名文件。
   ```cpp
   int rename(const char *oldname, const char *newname);
   ```

7. **`remove`**：删除文件。
   ```cpp
   int remove(const char *filename);
   ```

### 示例：读取二进制文件

```cpp
#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp = fopen("file.txt", "w+");
    char str[] = "Hello, World!";

    // 写入数据
    fwrite(str, sizeof(char), strlen(str), fp);

    // 重置文件指针
    fseek(fp, 0, SEEK_SET);

    // 读取数据
    char buffer[50];
    fread(buffer, sizeof(char), strlen(str), fp);
    buffer[strlen(str)] = '\0'; // 确保字符串终结

    printf("读取的内容: %s\n", buffer);
    fclose(fp);

    return 0;
}
```

## 其他文件操作相关函数

1. **`fseek`**：移动文件指针。
   
   > int fseek ( FILE * stream, long int offset, int from);
   
   - stream：流
   - offset：相对应 origin 位置处的偏移量，单位为字节，8bit 为负数时是往回取
   
   由于是long型来代替字节，所以要在数字后面加L
   
   - from：指针当前的位置
   
     > ​    \#define SEEK_CUR 1 // 当前位置
     > ​     \#define SEEK_END 2 // 末尾
     > ​     \#define SEEK_SET 0 // 开头
   
   ```cpp
   fseek(fp, 6L, SEEK_SET);  // 将指针移动到文件开头的第6个字节
   fseek(fp, -6L, SEEK_END); // 从文件末尾向前移动6个字节
   ```
   
2. **`ftell `**:获取指针位置
   
   读取当前指针指向的位置，返回的数字是相对文件开头的字节数。
   
   函数出错时返回-1
   
    
   
   拓展方法：获取文件字符个数
   
   ```cpp
   long n;
   fseek(pf,0,SEEK_END);
   n=ftell(pf);
   ```
   
   
   
2. **`rewind`**：将文件指针重置到文件开头。
   
   ```cpp
   rewind(fp);
   ```
   
3. **`clearerr`**：清除文件流的错误标志。
   ```cpp
   clearerr(fp);
   ```

4. **`ferror`**：检查文件流是否发生错误。
   ```cpp
   if (ferror(fp)) {
       std::cerr << "文件操作出错！" << std::endl;
   }
   ```

5. **`feof`**：检测文件是否读取到末尾。
   
   ```cpp
   if (feof(fp)) {
       std::cout << "到达文件末尾" << std::endl

7. **`rename `**：重命名文件

   > int rename ( const char * oldname, const char * newname );

> rename(“原名.txt” , “新名字.txt”); 

 

8. **`remove `**：删除文件

   > 函数声明：int remove ( const char * filename );

- filename：文件的路径

  > emove（“data.txt”）