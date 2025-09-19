# Activity 生命周期

## 生命周期

![](http://gityuan.com/images/lifecycle/activity.png)

- 从创建到显示到前台再到后台再到销毁，Activity会经历一个复杂的生命周期。
- 在Activity生命周期的各个阶段，Android会“回调（call back）”特定的生命周期方法。

在Android 中，Activity 的生命周期交给操作系统统一管理。

在android.app.Activity 类中，Android 定义了一系列与生命周期相关的方法，这些方法将被系统在合适的时机回调，我们可以根据需要“覆盖（或重写，override）”特定的方法。

```java
public class Activity {
    protected void onCreate(Bundle savedInstanceState);
    protected void onStart();
    protected void onResume();
    protected void onPause();
    protected void onStop();
    protected void onDestroy();
}
```

![image-20250330101147888](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201922212.png)

不同的生命周期方法，通常承担不同的任务，如果把特定的任务分派给了不合适的生命周期方法，可能会引入隐藏的BUG。

![image-20250330101218078](Android%E7%9F%A5%E8%AF%86%E7%82%B9%E6%B1%87%E6%80%BB.assets/image-20250330101218078.png)

![image-20250330101256657](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201922239.png)

- Activity A 启动另一个Activity B，回调如下:  
  Activity A 的onPause() 

  → Activity B 的onCreate() → onStart() → onResume()

  → Activity A的onStop()；

  如果B是透明主题又或则是个DialogActivity，则不会回调A的onStop；

可以在MainActivity.kt中写一个这样的类来通过 `Log.i(TAG, "...")` 记录日志，你可以观察 **Activity 的状态变化**。

```kotlin
val TAG = "ActivityLifecycle"

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val btnShowOther: Button =findViewById(R.id.btnShowOther)

        btnShowOther.setOnClickListener {
            val intent = Intent(this, OtherActivity::class.java)
            startActivity(intent)
        }


    }

    override fun onDestroy() {
        super.onDestroy()
        Log.i(TAG, "MainActivity onDestroy")
    }

    override fun onPause() {
        super.onPause()
        Log.i(TAG, "MainActivity onPause")
    }

    override fun onRestart() {
        super.onRestart()
        Log.i(TAG, "MainActivity onRestart")
    }

    override fun onResume() {
        super.onResume()
        Log.i(TAG, "MainActivity onResume")
    }

    override fun onStart() {
        super.onStart()
        Log.i(TAG, "MainActivity onStart")
    }

    override fun onStop() {
        super.onStop()
        Log.i(TAG, "MainActivity onStop")
    }
}
```

另一个activity：

```kotlin
class OtherActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_other)
    }
    override fun onDestroy() {
        super.onDestroy()
        Log.i(TAG, "OtherActivity onDestroy")
    }

    override fun onPause() {
        super.onPause()
        Log.i(TAG, "OtherActivity onPause")
    }

    override fun onRestart() {
        super.onRestart()
        Log.i(TAG, "OtherActivity onRestart")
    }

    override fun onResume() {
        super.onResume()
        Log.i(TAG, "OtherActivity onResume")
    }

    override fun onStart() {
        super.onStart()
        Log.i(TAG, "OtherActivity onStart")
    }

    override fun onStop() {
        super.onStop()
        Log.i(TAG, "OtherActivity onStop")
    }
}
```

App初启时，在Logcat面板中可以看到，onStart方法和onResume方法被先后调用，现在App可以响应用户操作。

![image-20250330170004199](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201922215.png)

此时点击“显示另一个Activity”按钮，新的Activity（OtherActivity）出现在屏幕上，这时，在Logcat中可以看到以下输出：

![image-20250330165958257](Android%E7%9F%A5%E8%AF%86%E7%82%B9%E6%B1%87%E6%80%BB.assets/image-20250330165958257.png)

- 主动销毁Activity

  调用Activity的finish()方法可以通知Android销毁Activity对象并将它从Back Stack（回退堆栈）中移除，这时，onDestory()方法会被调用，可以在此方法中“清理必要的资源”。

对于单Activity实例的App，调用它的finish()方法会因为唯一的Activity被销毁而导致Android结束整个进程，但如果这一App中包容多个Activity实例，必须要等到所有的Activity实例都被销毁，进程才退出。
如果希望立即终止整个进程，可以调用exitProcess(0)方法，这一方法是Kotlin标准库所提供的。



- 使用onSaveInstanceState（）保存简单，轻量级的UI状态

```java
lateinit var textView: TextView
var gameState: String? = null

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    gameState = savedInstanceState?.getString(GAME_STATE_KEY)
    setContentView(R.layout.activity_main)
    textView = findViewById(R.id.text_view)
}

override fun onRestoreInstanceState(savedInstanceState: Bundle?) {
    textView.text = savedInstanceState?.getString(TEXT_VIEW_KEY)
}

override fun onSaveInstanceState(outState: Bundle?) {
    outState?.run {
        putString(GAME_STATE_KEY, gameState)
        putString(TEXT_VIEW_KEY, textView.text.toString())
    }
    super.onSaveInstanceState(outState)
}
```

## 启动模式

| LaunchMode               | 说明                                                         |
| ------------------------ | ------------------------------------------------------------ |
| standard                 | 系统在启动它的任务中创建 activity 的新实例                   |
| singleTop                | 如果activity的实例已存在于当前任务的顶部，则系统通过调用其onNewIntent()，否则会创建新实例 |
| singleTask               | 系统创建新 task 并在 task 的根目录下实例化 activity。但如果 activity 的实例已存在于单独的任务中，则调用其 onNewIntent() 方法，其上面的实例会被移除栈。一次只能存在一个 activity 实例 |
| singleInstance           | 相同 singleTask，activity始终是其task的唯一成员; 任何由此开始的activity 都在一个单独的 task 中打开 |
| &nbsp;                   |                                                              |
| 使用Intent标志           | 说明                                                         |
| ----------               | -----                                                        |
| FLAG_ACTIVITY_NEW_TASK   | 同 singleTask                                                |
| FLAG_ACTIVITY_SINGLE_TOP | 同 singleTop                                                 |
| FLAG_ACTIVITY_CLEAR_TOP  | 如果正在启动的 activity 已在当前 task中 运行，则不会启动该activity 的新实例，而是销毁其上的 activity，并调用其 onNewIntent() |

## 启动过程

![](https://img-blog.csdn.net/20180427173504903)

``ActivityThread.java``

```java
private Activity performLaunchActivity(ActivityClientRecord r, Intent customIntent) {
    ...
    ActivityInfo aInfo = r.activityInfo;
    if (r.packageInfo == null) {
        //step 1: 创建LoadedApk对象
        r.packageInfo = getPackageInfo(aInfo.applicationInfo, r.compatInfo,
                Context.CONTEXT_INCLUDE_CODE);
    }
    ... //component初始化过程

    java.lang.ClassLoader cl = r.packageInfo.getClassLoader();
    //step 2: 创建Activity对象
    Activity activity = mInstrumentation.newActivity(cl, component.getClassName(), r.intent);
    ...

    //step 3: 创建Application对象
    Application app = r.packageInfo.makeApplication(false, mInstrumentation);

    if (activity != null) {
        //step 4: 创建ContextImpl对象
        Context appContext = createBaseContextForActivity(r, activity);
        CharSequence title = r.activityInfo.loadLabel(appContext.getPackageManager());
        Configuration config = new Configuration(mCompatConfiguration);
        //step5: 将Application/ContextImpl都attach到Activity对象
        activity.attach(appContext, this, getInstrumentation(), r.token,
                r.ident, app, r.intent, r.activityInfo, title, r.parent,
                r.embeddedID, r.lastNonConfigurationInstances, config,
                r.referrer, r.voiceInteractor);

        ...
        int theme = r.activityInfo.getThemeResource();
        if (theme != 0) {
            activity.setTheme(theme);
        }

        activity.mCalled = false;
        if (r.isPersistable()) {
            //step 6: 执行回调onCreate
            mInstrumentation.callActivityOnCreate(activity, r.state, r.persistentState);
        } else {
            mInstrumentation.callActivityOnCreate(activity, r.state);
        }

        r.activity = activity;
        r.stopped = true;
        if (!r.activity.mFinished) {
            activity.performStart(); //执行回调onStart
            r.stopped = false;
        }
        if (!r.activity.mFinished) {
            //执行回调onRestoreInstanceState
            if (r.isPersistable()) {
                if (r.state != null || r.persistentState != null) {
                    mInstrumentation.callActivityOnRestoreInstanceState(activity, r.state,
                            r.persistentState);
                }
            } else if (r.state != null) {
                mInstrumentation.callActivityOnRestoreInstanceState(activity, r.state);
            }
        }
        ...
        r.paused = true;
        mActivities.put(r.token, r);
    }

    return activity;
}

```

# 多activity开发



## 创建新Activity

### 创建布局文件![image-20250418233744884](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504182337049.png)

### 创建Activity类

创建一个新类，派生自Activity，重写其onCreate方法：![image-20250420192709248](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201927320.png)

注意一下，为了实现兼容性，自定义Activity的基类是AppCompatActivity，它拥有复杂的继承体系，其中在“很远”的地方，你可以找到一个名为“Activity”的“祖先”。

Activity被实例化时，onCreate()方法被回调，在此方法中将Activity与布局文件关联起来。

### 注册Activity

修改AndroidManifest.xml，注册这个刚创建的Activity类

![image-20250420192952225](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201929293.png)

> 所有的Activity，必须在清单文件中注册。

### 启动并显示一个 Activity

1. 创建一个Intent，指明要启动哪个Activity，它还可以携带特定的信息（以Name-Value形式保存）
2. 将Intent作为实际参数传给startActivity()方法



修改主Activity界面，给其添加一个按钮![image-20250420193359906](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202504201933973.png)

↑这是典型的启动 Acitivity 的代码
在 `btnStartSecendAcitvity` 的事件监听器被触发时，创建一个 `SecendAcitvity ` 类的 Intent(意图)，并用 startActivity 来运行这个意图，启动第二个activity

### 步骤总结

1. 为新 Activity 创建一个布局文件，设计好其布局。
2. 创建一个 Activity 类，并且在 Activity 的 onCreate ()方法中将布局文件与 Activity 关联起来。
3. 在 App 的清单文件中注册这个 Activity。
4. 创建一个 Intent 实例，调用 startActivity (intent)方法，即可启动并显示这个 Activity。

![image.png](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052122989.png)

Android Studio 提供了相应的模板（Empty Activity），可以把前面的过程自动化。

## 多入口的 Android App

Android App 是“多入口点”的，同一应用中的每个 Activity 都可能被单独访问，为此，Android 要求所有 Activity 都需要在清单文件中注册。

用户点击 App 图标启动时显示的第一个 Activity 称为“启动 Activity”，它必须定义有以下<intent-filter>，如果有多个 Activity 都有这个<intentfilter>，则第一个 Activity 被当成是启动 Activity。

![image.png](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052123526.png)

##  Activity 之间的信息传递

![image-20250505212656533](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052126592.png)

### 可以保存到Bundle中的信息

如果是离散的基础数据类型（比如Int和String）信息，直接用putXXX系列方法存入：

![image-20250505212754784](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052127825.png)

如果是一个对象，需要进行特殊的处理，让其实现Parcelable接口，并附加@Parcelize注解……

<img src="https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052128437.png" alt="image-20250505212815405" style="zoom: 80%;" />                 <img src="https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505052128478.png" alt="image-20250505212820417" style="zoom: 80%;" />



### 使用Intent 对象传输

Activity之间的数据传送由Intent对象负责，它提供了putXXX系列方法实现信息的传送：![image-20250506143554313](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505061435374.png)



在新Activity接收外界传入的数据
![image-20250506161851840](https://raw.githubusercontent.com/SunJianBai/pictures/main/img/202505061618950.png)

>putXXX(): 放数据
>getXXX()：取数据

