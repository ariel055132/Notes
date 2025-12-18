# Command 練習 
* 指令格式：docker container run [參數] {image 名稱} [CMD]

# 觀察以下指令的執行過程與結果
* docker container run alpine echo "Hello, Docker"
* 顯示 Hello, Docker

# 練習基本指令
## 顯示目前 Docker Container
* docker container ls 
* 為什麼看不到上一行指令建立的 container?
* 因為該 Container  
docker container ls -a

# 移除 container
docker container rm {container name or id}
## 舊版指令: docker rm {container id or hash id}

# 移除所有停止運行的 container
docker container prune

# 啟動時指定名字
docker container run --name my-container alpine

# 查看一個 container
docker container inspect my-container

# 觀察以下兩個指令執行後的差異
docker container run alpine echo "hello world"
docker container run --rm alpine echo "hello rm"
# 怎麼觀察？
docker container ls # 看得到哪些 containers?
docker container ls -a # 看得到哪些 containers?
# 差異是什麼？