# 目的

研究一下有什么功能

# 软件

linux + python3 + docker

# 使用步骤

```bash
# method 1
# use pip3
pip3 install homeassistant
# 报错 ERROR: Could not build wheels for cryptography
hass


# method2
# use docker
docker pull homeassistant/home-assistant

mkdir my-home-assistant-config
docker run -d --name="home-assistant" -v ~/my-home-assistant-config:/config -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/home-assistant

open http://192.168.75.128:8123/onboarding.html in chrome
```



How to solve ERROR: Could not build wheels for cryptography

```bash
# https://community.home-assistant.io/t/error-failed-building-wheel-for-cryptography/352020/4
sudo apt install cargo
export CRYPTOGRAPHY_DONT_BUILD_RUST=1

# error: command 'i686-linux-gnu-gcc' failed with exit status 1
sudo apt install libssl-dev

pip3 install --upgrade homeassistant

#  No module named 'aiohttp_cors'
pip3 install aiohttp_cors
```





# 我的家

![image-20210925160440554](../images/2021-09-25-home-assistent/image-20210925160440554.png)



![image-20210925160455772](../images/2021-09-25-home-assistent/image-20210925160455772.png)



# Ref

https://home-assistant.cc/installation/docker/

