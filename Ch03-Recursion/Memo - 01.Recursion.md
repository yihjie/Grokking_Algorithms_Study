## 從盒子中找出鑰匙
### 方法一：把所有盒子都取出後，再檢查
1. 先將收納箱 ( Main Box ) 內的所有盒子拿出來排成一堆 ( 待檢查區 )
2. 只要待檢查區還有盒子，就從盒子堆裡拿起一個盒子檢查
3. 如果盒子裡面還有盒子，就放到待檢區的盒子堆中
4. **如果找到鑰匙，就完成了!**
5. 不斷回到步驟 2

### 方法二：逐一拿起盒子檢查
1. 逐一拿起盒子檢查
2. 如果盒子裡面還有盒子，就繼續打開檢查
3. **如果找到鑰匙，就完成了**

---
## Pseudo Code ( 虛擬碼 )
### 方法一：把所有盒子都取出後，再檢查
    def look_for_key(main_box):
        pile = main_box.make_a_pile_to_look_through()
        # 將 main_box 中的小盒子拿出來放在待檢區 ( pile)

        while pile is not empty:
            box = pile.grab_a_box()
            for item in box:
                if item.is_a_box():
                    pile.append(item)
                elif item.is_a_key():
                    print("找到鑰匙了!")

### 方法二：逐一拿起盒子檢查
    def look_for_key(box):
        for item in box:
            if item.is_a_box():
                look_for_key(item)
            elif item.is_a_key():
                print("找到鑰匙了!")

---
## 使用遞迴 ( Recursion ) 的目的就是想讓解決的方法更明確
- Leigh Caldwell ( 李‧考德威爾) : <font color="blue">迴圈可能會提升程式的效能，但遞迴可能會提升程式設計師的效益</font>
1. 採用遞迴並不會提升效能
2. 有時候用迴圈還比較快