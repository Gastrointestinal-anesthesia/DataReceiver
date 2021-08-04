# DataReceiver

## 使用方法
### 环境配置

* 清除devel，build等文件夹
* 在/DataReceiver下执行catkin_make，为Python提供消息类型Anesthesia.msg的信息

### 运行

* 在/DataReceiver下执行source devel/setup.bash
* 在同一Terminal下执行rosrun monitor main.py

## 基本信息

### 设备信息

​	迈瑞BeneVision N15

### Python版本

​	测试环境Python3.8

### Python包依赖

* HL7Process
* socket

### 文件结构

| 文件名称（.py)   | 描述                                        |
| ---------------- | ------------------------------------------- |
| main             | 执行入口                                    |
| MonitorSocket    | 与监测仪建立TCP/IP连接，并进行数据传输      |
| HL7Process       | 处理收到的字符串，根据HL7协议将其转化为字典 |
| MonitorPublisher | 将解析后的字典以ROS topic的形式发布         |

## PyCharm配置

​	为了使PyCharm可以用于ROS的调试，需要进行以下配置

* File -> Settings -> Project:scripts -> Python Interpreter
* 点击上方Python Interpreter，选择Show all
* 点击上方Show paths for the selected interpreter(5个选项中最右侧一个)
* 添加/opt/ros/noetic/lib/python3/dist-packages、仓库路径（例如/home/lab129/DataReceiver) /devel/lib/python3/dist-packages