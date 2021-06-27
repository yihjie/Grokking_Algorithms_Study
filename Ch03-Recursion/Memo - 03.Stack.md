### Stack ( 堆疊 )
- Stack 是一種資料結構
  - 函式呼叫時會用到堆疊技術
  - 使用遞迴時，也必須理解堆疊的觀念
- 具有順序性的資料結構
  - LIFO ( Last-In-First-Out) : 最晚放入堆疊的資料，會最先被取出
  - FILO ( First-In-Last-Out) : 最早放入堆疊的資料，會最後被取出
- 動作
  - push : 在最上面貼上一張便利貼
  - put  : 讀取並撕掉最上面的便利貼
---
### Call Stack ( 呼叫堆疊 )
- 呼叫函式時，使用堆疊 → Call Stack
- 02_greet.py

      def greet2(name):
          print("how are you, ", name, "?")

      def bye():
          print("ok bye!")

      def greet(name):
          print("hello, ", name, "!")
          greet2(name)
          print("getting ready to say bye...")
          bye()

      greet("maggie")

- 02_greet.py 解說
    1. greet("maggie") # def greet(name)
       1. memory address : greet()
          - variable : name = "maggie"
    2. greet("maggie") + greet2(name) # def greet(name) + def greet2(name)
       1. memory address : greet2()
          - variable : name = "maggie"
       2. memory address : greet()
          - variable : name = "maggie"
    3. greet("maggie") # def greet(name)
       1. memory address : greet()
          - variable : name = "maggie"
    4. greet("maggie") + bye()  # def greet(name) +  def bye()
       1. memory address : bye()
       2. memory address :  greet("maggie")
          - variable : name = "maggie"
    5. NULL
---
### Call Stack and Recursion
-

    
     


