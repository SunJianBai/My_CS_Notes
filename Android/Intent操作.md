`Intent` 是 Android 中非常重要的一个核心类，它的作用是：**在 Android 系统中完成“意图”操作，例如启动活动、传递数据、调用系统功能（如拨号、拍照等）**。

---

## 什么是 Intent？

`Intent` 是 “意图” 的意思，它的作用是告诉系统：“**我要做某件事**”，比如：

- 从一个 Activity 跳转到另一个 Activity
- 打开浏览器
- 发短信、拨电话
- 启动一个服务

---

## Intent 的两种类型

|类型|用途|示例|
|---|---|---|
|**显式 Intent**|明确指定目标组件（Activity、Service）|`Intent(this, OtherActivity::class.java)`|
|**隐式 Intent**|不指定具体组件，通过动作+数据类型让系统查找匹配的组件|`Intent(Intent.ACTION_VIEW).setData(Uri.parse("http://www.baidu.com"))`|

---

## 最常见用途：启动 Activity + 传递数据

###  1. 启动另一个 Activity（**显式 Intent**）：

```kotlin
val intent = Intent(this, OtherActivity::class.java)
startActivity(intent)
```

- `this` 是当前上下文对象（Activity）
    
- `OtherActivity::class.java` 是目标 Activity 类
    

---

###  2. 启动并传递数据（putExtra）

```kotlin
val intent = Intent(this, OtherActivity::class.java)
intent.putExtra("username", "小明")
intent.putExtra("age", 18)
startActivity(intent)
```

在 `OtherActivity` 中接收：

```kotlin
val name = intent.getStringExtra("username")
val age = intent.getIntExtra("age", 0)
```

---

## 隐式 Intent：调用系统功能

###  1. 打开网页

```kotlin
val intent = Intent(Intent.ACTION_VIEW)
intent.data = Uri.parse("https://www.baidu.com")
startActivity(intent)
```

###  2. 打电话

```kotlin
val intent = Intent(Intent.ACTION_DIAL)
intent.data = Uri.parse("tel:10086")
startActivity(intent)
```

> 如果要直接拨出电话，要用 `ACTION_CALL`，但需要加权限。

---

## 使用 `startActivityForResult`（已被废弃，建议用新版 API）

老方法（已废弃）：

```kotlin
startActivityForResult(intent, 1)
```

推荐方法（新 API）：  
使用 `ActivityResultLauncher` 和 `registerForActivityResult` 来实现 “启动另一个 Activity 并获取返回结果”。

---

## Intent 可以携带哪些类型数据？

|方法|支持的数据类型|
|---|---|
|`putExtra`|基本类型（int、String、boolean）|
|`putExtras`|Bundle|
|`putParcelableExtra`|实现了 Parcelable 接口的对象（自定义类）|
|`putSerializableExtra`|实现了 Serializable 接口的对象|

---

## Intent 的常用属性

|方法 / 属性|作用|
|---|---|
|`setClass()`|设置目标组件|
|`setAction()`|设置动作（比如 ACTION_VIEW）|
|`setData()`|设置数据（通常是 URI）|
|`setType()`|设置 MIME 类型（如 "image/*"）|
|`addCategory()`|添加类别（如 CATEGORY_DEFAULT）|

---

##  示例：一个完整流程（跳转 + 传值 + 接收）

**MainActivity.kt**

```kotlin
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "张三")
intent.putExtra("age", 20)
startActivity(intent)
```

**DetailActivity.kt**

```kotlin
val name = intent.getStringExtra("name")
val age = intent.getIntExtra("age", 0)
```

---



> Intent 就是 Android 中组件之间“沟通的媒介”，你可以用它来 **跳转页面、传递数据、调用系统功能**。

---

