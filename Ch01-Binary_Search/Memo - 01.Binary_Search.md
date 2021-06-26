### 先決條件
1. 被搜尋的清單內容必須先經過排序
### 最多搜尋次數
* 2Log N , (剛好整數則需要 +1 )
### 用 Python 實作
1. List / Array

### :memo:範例程式 ( 01_binary_search.py )
    def binary_search(list, item):
        low = 0
        high = len(list)-1
    
        while low <= high:
            mid = (low + high)//2
            guess = list[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
    
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))  # => 1
    ptint(binary_search(my_list, -1)) # => None


### 演算法執行時間
* 簡易搜尋法/傻瓜搜尋法
    - 最大猜測次數與清單的長度一樣
    - 線性時間 (Linear Time)
    - O(n)
* 二元搜尋法
    - 最大猜測次數 為 2Log 清單的長度
    - 對數時間 (Logarithmic Time 或稱為 Log Time) 
    - O(Log n)