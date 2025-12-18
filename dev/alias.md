# Alias 
* 字面上的意思是縮寫
* 透過設定來縮寫一些常用的指令，可以使我們在開發上能節省更多的時間
* 例如：如果需要清空 terminal 上的資料，一般打 clear，這樣每次均需要打5個字，但如果設定 alias (e.g alias c='clear')，則每次只需要打 c，即可

## 如何 setting
* bash -> 建立 .bash_profile 和 .bashrc (設定檔)
* zsh -> 建立 .zshrc (設定檔)
1. 直接 vim .zshrc
2. 在 .zshrc 建 alias (alias ll='ls -al')
3. 儲存，並退出
4. 使用 source 指令執行設定檔 (source ~/.zshrc)