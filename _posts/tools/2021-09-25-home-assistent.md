# 目的

研究一下有什么功能

# 使用步骤

```bash
docker pull homeassistant/home-assistant

mkdir my-home-assistant-config
docker run -d --name="home-assistant" -v ~/my-home-assistant-config:/config -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/home-assistant

open http://192.168.75.128:8123/onboarding.html in chrome
```

# 我的家

![image-20210925160440554](../images/2021-09-25-home-assistent/image-20210925160440554.png)



![image-20210925160455772](../images/2021-09-25-home-assistent/image-20210925160455772.png)



# Ref

https://home-assistant.cc/installation/docker/

