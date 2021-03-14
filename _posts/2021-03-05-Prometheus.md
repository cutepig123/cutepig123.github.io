---
categories: networking tool Prometheus
---
Prometheus

# 系统架构

![img](Prometheus.assets/e3daea22834a551c630c566c82451290.png)

# 基本入门

运行windows exporter，他会在端口9182监听。用telnet测试端口是否打开

配置G:\sw\prometheus-2.21.0-rc.0.windows-amd64\prometheus.yml,加入

```yaml
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  - job_name: 'jaeger'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:14269']

  - job_name: 'windows'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9182']    
```



运行G:\sw\prometheus-2.21.0-rc.0.windows-amd64\prometheus.exe

用chrome打开http://localhost:9090/

# 如何搭配grafana打造高逼格监控平台(done)

https://blog.51cto.com/youerning/2050543

访问grafana, http://<服务器IP>:3000
默认用户名密码:admin/admin

为grafana添加Prometheus数据源

https://www.jianshu.com/p/8d2c020313f0

安装并启动Grafana后，浏览器输入 IP:3000 来访问Grafana，管理员账号密码默认是admin/admin。首次登陆会让你修改管理员密码，然后就可以登录查看了。

在界面左边是一竖排选项，选择设置图标中的Data Source，添加Prometheus的数据源，URL就填上面你给Prometheus Server设置的ip+端口号就行了，如果没改过且在本机运行的话，那就是localhost:9090。

此时可以添加dashboard，也就是监控面板了，在刚配好的Prometheus Data Source的设置中有一个标签就是dashboard，我们导入Prometheus 2.0 Stats这个面板，就能看到我们Prometheus的一些基本监控情况了，这其实就是导入了一个别人写好的面板配置，并且连接我们自己Prometheus的监控数据做展示。

还记得我们上面还运行了一个node exporter吧，现在我们展现一下这个监控信息，左边竖排点击加号图标中的Import，来导入其他别人写好的面板。在[Grafana的官方面板页面](https://grafana.com/dashboards)其实可以看到很多别人配置好的面板，我们找到自己想要的面板，比如这个node exporter的：

![img](Prometheus.assets/9075967-4de16503230115e3.webp)

复制右边那个面板ID，然后在Import界面输入ID，Load后配置好数据源为我们的Prometheus，就可以出现我们自己机器的状态监控面板了，很炫酷吧。

这个面板需要安装一个饼图的插件（页面上有说明），安装Grafana插件的方法为：



```shell
// 进入Grafana/bin目录
./grafana-cli plugins install [插件名]
// 安装成功后重启Grafana
```

# 用promethus+wmi-exporter监控windows系统(done)

https://www.jianshu.com/p/8d2c020313f0

## 一、安装wmi-exporter

首先在需要监控的Windows机器上安装wmi_exporter。wmi_exporter下载地址：https://github.com/martinlindhe/wmi_exporter/releases

![img](Prometheus.assets/1323857-20191101145445097-825587686.png)

 

 下载后，双击即可完成安装。

完成安装后，会自动创建一个开机自启的服务

![img](Prometheus.assets/1323857-20191101145612968-448777749.png)

 

 ![img](Prometheus.assets/1323857-20191101145810771-595061180.png)

 

验证服务是否启动，默认wmi-exporter端口为9182

浏览器访问 http://192.168.56.1:9182/metrics （Windows系统IP地址：9182端口），显示数据，则服务开启成功。

![img](Prometheus.assets/1323857-20191101150254169-1138580051.png)

 

##  二、修改Prometheus配置

进入Prometheus的安装文件夹，打开Prometheus配置文件

```
#  cd /usr/local/prometheus
#  vim prometheus.yml
```

在scrape_configs标签下，添加以下内容，配置监控

```
- job_name: 'Windows'
    static_configs:
    - targets: ['192.168.56.1:9182']
      labels:
        instance: Windows
```

以下是Prometheus.yml 文件全部内容

[![复制代码](Prometheus.assets/copycode.gif)](javascript:void(0);)

```
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  - job_name: 'Linux'
    static_configs:
    - targets: ['192.168.56.201:9100']
      labels:
        instance: Linux

  - job_name: 'Windows'
    static_configs:
    - targets: ['192.168.56.1:9182']
      labels:
        instance: Windows
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

保存退出，重启Prometheus服务

```
#  systemctl restart prometheus
```

浏览器访问 http://192.168.56.200:9090/targets 查看监控信息

![img](Prometheus.assets/1323857-20191101150812380-1654750515.png)

 

 可以看到，Windows机器已经加入进来。

## 三、配置Grafana

添加dashboard

Grafana官方为我们提供了很多dashboard页面，可直接下载使用。浏览器访问 https://grafana.com/grafana/dashboards 下载所需要的dashboard页面

此处我们使用Windows 监控的dashboard，dashboard Id为：10467

![img](Prometheus.assets/1323857-20191101151238581-132000887.png)

 

 然后打开我们的Grafana监控页面，打开dashboard的管理页面

 

 ![img](Prometheus.assets/1323857-20191101151253998-187872000.png)

 

 点击【import】按钮

![img](Prometheus.assets/1323857-20191101151308560-58521440.png)

 

 然后将我们刚才的dashboard Id （10467） 复制进去

![img](Prometheus.assets/1323857-20191101151333991-1287896704.png)

 

 Grafana会自动识别dashboard Id 。

然后点击【change】按钮，生成一个随机的UID，然后点击下方输入框，选择我们之前创建的数据源Prometheus，最后点击【Import】按钮，即可完成导入。

![img](Prometheus.assets/1323857-20191101151621997-1862727626.png)

 

 导入成功后，会自动打开该Dashboard，即可看到我们刚才设置好的Windows监控

![img](Prometheus.assets/1323857-20191101151713084-2146447021.png)

 

 至此Prometheus监控Windows机器，配置完成。

# 如何设置alert？

