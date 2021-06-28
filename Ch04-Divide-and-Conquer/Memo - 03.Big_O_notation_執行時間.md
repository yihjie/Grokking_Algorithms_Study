Quicksort 之所以獨特，**在於它的執行時間取決於所選定的基準值 ( Pivot )**

|演算法|Binary Search|Simple Search|Quick Sort|Selection Sort|Traveling Salesperson|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**執行時間**|O(Log n)|O(n)|O(n Log n)|O(n^2)|O(n!)|

### Quicksort 是比較特別的演算法
- 執行時間
  - Worst Case ( 最差情況 ) : O(n^2)
  - Average Case ( 平均情況 ) : O(n Log n)
---

### Merge Sort ( 合併排序法 )
- 做法
  - 分成「分割」、「合併」兩個階段
    - 「分割」
      1. 將想要排序的大陣列先對半分割成兩個小陣列
      2. 分別將兩個小陣列對半分割
      3. 重複步驟 2.，直到每個小陣列都只剩下 1 個元素
    - 「合併」
      1. 將只剩下 1 個元素的陣列進行排序並合併在一起
      2. 重複同樣的操作，直到將全部的陣列組合成一個完成排序的陣列
- 執行時間
  - Worst Case ( 最差情況 ) : O(n Log n)
  - Average Case ( 平均情況 ) : O(n Log n)
---

### Time constant ( 時間常數 ) 的影響
#### 列出 list 中的每個元素，並加入 Time constant
- 03_time_constant_a.py -- 沒有 Time constant
         
      def print_items_a(list):
          for item in list:
              print(item, end = ' ')
            
      a = [2, 4, 6, 8, 10]
      print_items_a(a)

- 03_time_constant_b.py -- 加入 Time constant : sleep(1)
  
      from time import sleep

      def print_items_b(list):
          for item in list:
              sleep(1)
              print(item, end = ' ' )
    
      a = [2, 4, 6, 8, 10]
      print_items_b(a)

- 一般而言， Time constant 會被忽略
- 當兩個演算法的 Big O 執行時間不一樣，那 Time constant 的影響就不大

### 平均情況與最差情況
**Quicksort 的執行時間主要取決於所選定的基準值 ( Pivot )**
1. 假設每次都選擇第一個元素當作基準值，並且用 Quicksort
   1. 一個已經排序過的陣列，Quicksort 並不會先檢查是否已經排序過，所以還是會再次排序
      - a = [1, 2, 3, 4, 5, 6, 7, 8]
        - 最差情況 
          - pivot = 1
          - stack = 8 : O(n)
        - 最佳情況 == 平均情況
          - pivot = 4
          - stack = 4 : O(Log n)
