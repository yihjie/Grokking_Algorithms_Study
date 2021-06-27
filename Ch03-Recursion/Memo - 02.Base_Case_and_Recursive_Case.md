## 遞迴函式會呼叫自己，所以一不小心就會寫出無限循環的函式
#### 01_coundown_a.py
    def countdown(i):
        print(i)
        countdown ( i - 1)
    
    countdown(3)

### 設定何時停止遞迴
- 撰寫遞迴函式時，必須設定何時停止遞迴
- 遞迴函式的組成
    1. Base Case ( 基本情況 )
       - 函式不在呼叫自己的情況
    2. Recursive Case ( 遞迴情況 )
       - 函式呼叫自己的情況
#### 01_coundown_b.py
    def countdown(i):
        # Base Case
        print(i)
        if i <= 1:
            return
        
        # Recursive Case
        else:
            countdown( i - 1)

    countdown(5)
