

Gradle 是一个现代化的构建工具，广泛应用于 **Java、Kotlin、Android** 等项目的构建、依赖管理和自动化任务。它结合了 **Maven** 和 **Ant** 的优点，提供了高性能、灵活的构建能力。

------

## 1. Gradle 的作用

Gradle 主要用于：

- **自动化构建**（编译、打包、测试、发布）
- **依赖管理**（类似于 Maven）
- **多模块项目管理**（适用于大型项目）
- **自定义任务**（灵活配置各种构建任务）

------

## 2. Gradle 与 Maven 的区别

| 对比项   | Gradle                                                     | Maven                    |
| -------- | ---------------------------------------------------------- | ------------------------ |
| 配置文件 | `build.gradle` (Groovy) 或 `build.gradle.kts` (Kotlin DSL) | `pom.xml` (XML)          |
| 语法     | 基于 Groovy/Kotlin 的 DSL                                  | XML 配置                 |
| 依赖管理 | 支持 `mavenCentral()`、`google()` 等                       | 使用 `<dependency>` 标签 |
| 扩展性   | 高度可扩展（可以自定义 Task）                              | 扩展性较弱               |
| 性能     | **增量构建**（只编译修改的部分）更快                       | 需要全量编译             |

------

## 3. Gradle 的基本结构

Gradle 的核心概念：

- **Project**（项目）：代表一个构建单元，可以是单模块或多模块。
- **Task**（任务）：Gradle 的最小执行单元，比如 `compileJava`、`test` 等。
- **依赖管理**：Gradle 可以使用 Maven 仓库或本地文件进行依赖管理。

### 目录结构（以 Java 项目为例）

```
my-project/
 ├── build.gradle        # Gradle 构建脚本（Groovy DSL）
 ├── settings.gradle     # 配置项目的基本信息（如多模块）
 ├── gradle/            # Gradle 相关文件
 ├── src/
 │   ├── main/java/      # 主要的 Java 代码
 │   ├── main/resources/ # 资源文件
 │   ├── test/java/      # 测试代码
```

------

## 4. 基本的 `build.gradle` 配置

```gradle
plugins {
    id 'java'  // 使用 Java 插件
}

repositories {
    mavenCentral()  // 使用 Maven 中央仓库
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.0.2'
    testImplementation 'junit:junit:4.13.2'
}

tasks.register('hello') {
    doLast {
        println 'Hello, Gradle!'
    }
}
```

- **`plugins`**：声明使用的插件（如 Java、Kotlin、Android）
- **`repositories`**：指定依赖仓库
- **`dependencies`**：声明项目的依赖
- **`tasks.register('hello')`**：自定义一个 `hello` 任务

------

## 5. 常用 Gradle 命令

| 命令                  | 作用                                          |
| --------------------- | --------------------------------------------- |
| `gradle build`        | 构建项目（编译、测试、打包）                  |
| `gradle clean`        | 清理 `build/` 目录                            |
| `gradle run`          | 运行 Java 应用（如果使用 `application` 插件） |
| `gradle test`         | 运行测试                                      |
| `gradle dependencies` | 查看依赖关系                                  |
| `gradle tasks`        | 查看所有可用任务                              |
| `gradle -q hello`     | 运行 `hello` 任务                             |

------

## 6. Gradle 在 Android 开发中的作用

在 Android Studio 中，Gradle 主要负责：

- **管理依赖**（如 `implementation 'com.android.support:appcompat-v7:28.0.0'`）
- **编译和打包 APK**（自动执行 `assembleDebug` 或 `assembleRelease`）
- **多渠道打包**（如 `productFlavors`）
- **代码混淆和优化**（ProGuard / R8）

### Android 项目的 `build.gradle` 示例：

```gradle
android {
    compileSdk 33

    defaultConfig {
        applicationId "com.example.myapp"
        minSdk 21
        targetSdk 33
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.9.0'
}
```

------

## 7. Gradle Wrapper（推荐使用）

Gradle 提供了 **Wrapper**（包装器），保证所有开发者使用相同版本的 Gradle。

### 生成 Wrapper

```sh
gradle wrapper
```

生成的文件：

```
gradlew       # Linux/Mac 运行 Gradle
gradlew.bat   # Windows 运行 Gradle
gradle/wrapper/
 ├── gradle-wrapper.jar
 ├── gradle-wrapper.properties
```

### 使用 Wrapper

```sh
./gradlew build  # Mac/Linux
gradlew.bat build  # Windows
```

⚠️ **优点**：

- 统一 Gradle 版本，避免开发环境不一致
- 运行 `gradlew` 自动下载 Gradle，无需手动安装

------

## 8. Groovy DSL vs Kotlin DSL

Gradle 支持 **Groovy DSL**（`build.gradle`）和 **Kotlin DSL**（`build.gradle.kts`）。

### Groovy DSL（默认）

```gradle
plugins {
    id 'java'
}

repositories {
    mavenCentral()
}
```

### Kotlin DSL（推荐）

```kotlin
plugins {
    id("java")
}

repositories {
    mavenCentral()
}
```

**Kotlin DSL 的优势**：

- 提供 **类型安全**（避免拼写错误）
- 更好的 **代码补全**（IDE 支持更强）

------

## 9. Gradle 多模块项目

适用于 **大型项目**，多个模块可以共享代码和依赖。

### 目录结构：

```
multi-module-project/
 ├── settings.gradle
 ├── build.gradle
 ├── app/ (主应用)
 │   ├── build.gradle
 ├── library/ (公共库)
 │   ├── build.gradle
```

### `settings.gradle` 配置：

```gradle
rootProject.name = 'multi-module-project'
include 'app', 'library'
```

### `app/build.gradle`：

```gradle
dependencies {
    implementation project(':library')
}
```

------

