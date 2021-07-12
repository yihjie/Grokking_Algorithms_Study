由於大部分的程式語言都有內建 Hash Table，使用者不需要自己撰寫
本章節不深入探討 Hash Table 的實作細節，<font color="red">得注意 Hash Table 的效能 </font>
### Collision ( 碰撞)
- 兩個鍵 ( Key ) 被分配到同一個位置 ( Slot ) 的情況
- 避免 Collision --> 建立鏈結串列 ( Linked List )
**重點**
1. 雜湊函式非常重要
2. 鍵結串列太長會拖類雜湊表的效能