## Quicksort ( 快速排序法 )
- 一種排序演算法
- 執行速度比 Selection Sort ( 選擇排序法 ) 快上許多
- C : qsort()
  
### 空陣列或只有 1 個元素的陣列
    def quicksort(array):
        if len(array) < 2:
            return array
- 不需要排序的陣列 : Base Case
  - [] : 空陣列
  - [20] : 只有 1 個元素的陣列

### 2 個元素的陣列
    def quicksort(array):
        if len(array) == 2:
            if array[0] < array[1]:
                 return array
            else:
                new_array = []
                new_array.append(array[1])
                new_array.append(array[0])
                return new_array

### 3 個元素以上的陣列
- 挑選基準值 ( Pivot )
- 分割 ( partitioning ) : 找出「比基準值小的元素」、「比基準值大的元素」
  1. 所有小於基準值的子陣列 -- **尚未排序**
  2. 基準值
  3. 所有大於基準值的子陣列 -- **尚未排序**
- #### 子陣列的排序
  - quicksort(less) + pivot + quicksort(greater)

## 完整的 Quicksort 程式碼： 02_quicksort.py
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:]] if i <= pivot]
            greater = [i for i in array[1:]] if i > pivot

            return quicksort(less) + [pivot] + quicksort(greater)
    
    print(quicksort([10, 5, 2, 3]))