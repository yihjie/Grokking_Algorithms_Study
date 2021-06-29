## Hash Table ( 雜湊表 )
  - 非常實用的資料結構
  - 核心
    - 實作 ( Implementation )
    - 碰撞 ( Collision )
    - 雜湊函式 ( Hash Function )
---
### 假設在雜貨店工作，顧客買東西，得從價目表查詢商品的價格才能結帳
  1. 價目表沒有排序，逐一查價
     - 簡易搜尋法 ( Simple Search )
     - 執行時間 : O(n)
  2. 價目表有排序
     - 二元搜尋法 ( Binary Search )
     - 執行時間： O(Log n)
  3. 品名、價格對應表
     - 雜湊表 ( Hash Table )
     - 執行時間： O(1)
---
### Hash Function ( 雜湊函式 )
  - 一種將輸入的字串輸出成數字的格式
    - 字串：以連續 Byte 表示的任何類型資料
  - **雜湊函式會將字串對應到數字**
    - 規則
      1. 必須有一致性
      2. 不同的字串要對應到不同的數字
  - Hash Function 是一個函數，必須和資料結構 ( 例如：陣列 ) 搭配，才能用來存放或查找資料

### Hash Table ( 雜湊表 )
  - 將雜湊函式與陣列組合在一起
    - 陣列 ( array ) 和串列 ( linked list ) 會直接對應到記憶體位址
    - Hash Table 巧妙使用 Hash Function 來指定元素的存放位置
  - 又稱為
    - Hash Map ( 雜湊地圖 )
    - Map ( 地圖 )
    - Dictionary ( 字典 )
    - Associative Array ( 關聯式陣列 )
  - 有 key ( 鍵 )、value ( 值 ) 之分
    - key -- 品名
    - value -- 價格
---
#### 建立 Hash Table
  - Python - dict
  
        book = dict()

