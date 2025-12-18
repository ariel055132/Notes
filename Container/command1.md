# docker container run [參數] {image 名稱} [CMD]

# 觀察以下指令的執行過程與結果
docker container run alpine echo "Hello, Docker"
## echo "hello world" 是啟動這個 container 的 process
##  舊版指令: docker run alpine echo "hello world" 

# 練習基本指令
docker container ls # 為什麼看不到上一行指令建立的 container?
docker container ls -a
## 舊版指令:
## docker ps 
## docker ps -a

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