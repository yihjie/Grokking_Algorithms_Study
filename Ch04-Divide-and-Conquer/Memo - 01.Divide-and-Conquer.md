### Divide-and-Conquer ( D&C )
- 概念：將一個複雜的問題拆解成多個子問題，再利用遞迴求出子問題的答案，最後將子問題的答案合併在一起，即可得到原本複雜問題的答案
- 很多演算法都會用到 D&C 的技巧：
  - Binary Search ( 二元搜尋法 )
  - Mergesort ( 合併排序法 )
  - Quicksort ( 快速排序法 )
- 執行步驟或思路：
  1. 找出 Base Case ( 基本情況 )，而且要用最單純的 Base Case
  2. 拆解或是縮減問題，直到變成 Base Case ( 基本情況 ) -- **<font color="white" style="background-color:red" size="5">不再遞迴</font>**
---
#### Euclid's Algorithm ( 歐幾里德演算法 )

#### 回傳陣列內所有數字的加總 : 01_loop_sum.py

    def sum(arr):
        total = 0
        for x in arr:
            total += x
        return total
    
    print(sum([2, 4, 6]))
---
### Functional Programming ( 函數式程式設計 )

 - Haskell : 沒有迴圈，只能用遞迴方式來撰寫函式

       Sum [ ] = 0 <-- Base Case
       Sum (x:xs) = x + (sum xs) <-- Recursive Case
   Or

       sum arr = if arr == []
                    then 0
                    else ( head arr) + (sum ( tail arr ))

