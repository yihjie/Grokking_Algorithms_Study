### 選擇排序法 ( Selection Sort )
   - 概念
     - 假如電腦裡有一份記錄每位歌手播放次數的記錄表，想依播放次數的高低來排序
     - 做法：
       1. 建立一個新的表格
       2. 從原本表格中搜尋所有資料，找出播放次數最多的歌手
       3. 將該歌手搬到新的表格中
       4. 重複步驟 2. 及步驟 3. 依序找出次高的歌手
     - 計算 Big O
       1. O(n) x n = O(n^2) 
     - 日常應用
       1. 排序電話簿裡的姓名
       2. 依日期排序旅遊時間
       3. 依日期排序電子郵件 ( 由新到舊 )
---
### :memo:範例程式 ( 01_selection_search.py )
    def find_smallest_index(arr):
        smallest = arr[0]
        smallest_index = 0

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest_index = i
                smallest = arr[i]
        
        return smallest_index

    def selection_sort(arr):
        new_arr = []

        for i in range(len(arr)):
            smallest = find_smallest_index(arr)
            new_arr.append(arr.pop(smallest))

        return new_arr

    print(selection_sort([5, 3, 6, 2, 10]))

可以到 http://pythontutor.com 去執行本程式