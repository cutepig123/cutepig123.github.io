# openproject

它可以使用docker運行，運行完畢，訪問ip:8181端口即可

```bash
mkdir -p ~/openproject/{pgdata,assets} 

sudo docker run -d -p 8081:80 --name openproject2 \
  -e SERVER_HOSTNAME=openproject.example.com \
  -e SECRET_KEY_BASE=secret \
  -v ~/openproject/pgdata:/var/openproject/pgdata \
  -v ~/openproject/assets:/var/openproject/assets \
  openproject/community:12
  
sudo docker exec -it    openproject2 bash

```

大概試了一下，他的ganttchart界面還算不錯。



Cons

* 反應有點慢
* 修改了ganttchart之後如何查看修改記錄啊 - task detail裏面能看到
