#### 目录

*   [知识点 / 算法模板整理](#_1)
*   *   [一、Python 基础](#Python_6)
    *   *   [1. 输入输出高效处理](#1__8)
        *   [2. 数据类型进阶](#2__26)
        *   [3. 函数式编程](#3__45)
    *   [二、核心数据结构深度解析](#_55)
    *   *   [1. 特殊数据结构](#1__57)
        *   [2. 树结构实现](#2__75)
        *   [3. 图表示方法](#3__88)
    *   [三、算法模板大全](#_105)
    *   *   [1. 搜索算法](#1__107)
        *   [2. 动态规划经典模型](#2__137)
        *   [3. 数论算法](#3__161)
    *   [四、蓝桥杯特色题型突破](#_184)
    *   *   [1. 日期处理](#1__186)
        *   [2. 全排列应用](#2__197)
        *   [3. 贪心策略](#3__209)
    *   [五、竞赛技巧与优化](#_225)
    *   *   [1. 时间优化](#1__227)
        *   [2. 空间优化](#2__240)
        *   [3. 调试技巧](#3__250)
    *   [六、备赛路线图](#_260)
    *   [七、资源推荐](#_272)
    *   [八、注意事项](#_281)
    *   [蓝桥杯备赛](#_289)

知识点 / 算法模板整理
------------

> 这篇笔记给大家系统整理了[蓝桥杯 python](https://so.csdn.net/so/search?q=%E8%93%9D%E6%A1%A5%E6%9D%AFpython&spm=1001.2101.3001.7020) 组竞赛所需的【核心知识点】，涵盖从基础语法到高级算法的各个方面，希望帮助大家高效备赛。包括输入输出处理、数据结构应用、算法模板、数学知识等。

### 一、Python 基础

#### 1. [输入输出](https://so.csdn.net/so/search?q=%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA&spm=1001.2101.3001.7020)高效处理

*   **快速输入**：

```
import sys
input = sys.stdin.read  # 整块读取
data = input().split()  # 分割处理
```

*   **输出优化**：

```
print(' '.join(map(str, result)))  # 减少IO次数
```

#### 2. 数据类型进阶

*   **集合操作**：

```
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 | s2)  # 并集
print(s1 & s2)  # 交集


```

*   **字典排序**：

```
sorted(dict.items(), key=lambda x: (-x[1], x[0]))


```

#### 3. 函数式编程

*   **Lambda 高阶用法**：

```
from functools import reduce
reduce(lambda x,y: x*y, range(1,6))  # 5!计算


```

### 二、核心[数据结构](https://so.csdn.net/so/search?q=%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84&spm=1001.2101.3001.7020)深度解析

#### 1. 特殊数据结构

*   **双向队列**：

```
from collections import deque
dq = deque(maxlen=5)  # 固定长度队列


```

*   **有序字典**：

```
from collections import OrderedDict
od = OrderedDict()  # 保持插入顺序


```

#### 2. 树结构实现

*   **二叉树节点**：

```
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


```

#### 3. 图表示方法

*   **邻接矩阵**：

```
    graph = [[0]*n for _ in range(n)]
    

```

*   **边列表**：

```
    edges = [(u1,v1,w1), (u2,v2,w2)...]
    

```

### 三、算法模板大全

#### 1. 搜索算法

*   **DFS 模板**：

```
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)
    

```

*   **BFS 模板**：

```
    def bfs(start):
        queue = deque([start])
        visited = set([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    

```

#### 2. 动态规划经典模型

*   **背包问题**：

```
    dp = [0]*(V+1)
    for i in range(N):
        for j in range(V, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    

```

*   **LIS 问题**：

```
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    

```

#### 3. 数论算法

*   **GCD/LCM**：

```
    import math
    math.gcd(a, b)
    a*b//math.gcd(a, b)  # LCM
    

```

*   **素数判定**：

```
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

```

### 四、蓝桥杯特色题型突破

#### 1. 日期处理

*   **闰年判断**：

```
    def is_leap(year):
        return year%400==0 or (year%100!=0 and year%4==0)
    

```

#### 2. 全排列应用

*   **生成排列**：

```
    from itertools import permutations
    for p in permutations('ABC', 2):
        print(''.join(p))
    

```

#### 3. 贪心策略

*   **区间调度**：

```
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = -float('inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    

```

### 五、竞赛技巧与优化

#### 1. 时间优化

*   **预处理技巧**：

```
    # 预处理阶乘模数
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i % MOD
    

```

#### 2. 空间优化

*   **滚动数组**：

```
    dp = [[0]*(W+1) for _ in range(2)]  # 交替使用
    

```

#### 3. 调试技巧

*   **断言检查**：

```
    assert len(nums) > 0, "输入不能为空"
    

```

### 六、备赛路线图

1.  **基础阶段**：
    *   完成 Python 语法强化
    *   掌握基本数据结构实现
2.  **强化阶段**：
    *   刷经典算法题（每日 3-5 题）
    *   参加每周模拟赛
3.  **冲刺阶段**：
    *   重点突破动态规划和图论
    *   研究历年真题

### 七、资源推荐

*   **在线题库**：
    *   蓝桥杯官方练习系统
    *   LeetCode 精选题目
*   **参考书籍**：
    *   《算法竞赛入门经典》
    *   《Python 算法教程》

### 八、注意事项

1.  比赛环境为 Python 3.8.x
2.  禁止使用 numpy 等第三方库
3.  注意题目中的时间限制（通常 1s 对应 1e8 次操作）

### 蓝桥杯备赛

1.  **基础优先**：确保熟练掌握所有基础语法和数据结构
2.  **模板记忆**：熟记常用算法模板，如排序、搜索、DP 等
3.  **真题训练**：至少完成近 3 年的真题，理解出题思路
4.  **时间管理**：练习时注意时间分配，简单题快速解决
5.  **调试技巧**：学会使用打印调试和边界条件测试

**推荐练习顺序**：

1.  基础语法和输入输出
2.  字符串处理和数学问题
3.  数据结构应用
4.  动态规划和图论算法
5.  综合真题模拟

💡

通过系统性地学习和练习这些知识点，再加上适量的真题训练，建议每天保持 3-5 小时的专注练习时间，省一等奖乃至国奖都还是非常有希望的。