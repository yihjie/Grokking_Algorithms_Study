### 範例 1：建立有對應關係的查詢功能
- 電話簿功能需求：
1. 新增聯絡人姓名及電話號碼
2. 輸入聯絡人姓名時，顯示對應的電話號碼 (**Hash Table**)
3. 將某個元速度應到另一個元素
4. 查詢指定的元素
- 電話簿範例：02_phone_book.py

      phone_book = dict() # phone_book = {}
      phone_book["JENNY"] = 8675309
      phone_book["EMERGENCY"] = 911
      print(phone_book["JENNY"])

- DNS 解析 ( DNS Resolution ) ─將網址轉換成對應的 IP 位址
---
### 範例 2：檢查是否有重複的項目
- 投票所監票人員：
1. 每位投票人只能投一次
- 03_check_voter.py
  
      voted = {}

      def check_voter(name):
          if voted.get(name):
              print("請離開!")
          else:
              voted[name] = True
              print("請投票!")
---
### 範例 3：處理快取 ( Cache )
- 網站 cache 原理：
  1. 首先向網站的伺服器請求 ( request ) 進入
  2. 伺服器會進行一些處理，再將網頁回傳 ( response )
  3. 顯示網頁
- Cache 優點：
  1. 可以更快載入網頁
  2. 減輕網站的工作量
- Pseudo code
  
      cache = {}

      def get_page(url):
          if cache.get(url):
              return cache[url]
          else:
              data = get_data_from_server(url)
              cache[url] = data
              return data

**<font color="red">Hash Table 適用場景</font>**
1. 建立一個元素與另一個元素的對應關係
2. 篩選重複項目
3. 快取或記錄資訊，以減輕伺服器的工作量
