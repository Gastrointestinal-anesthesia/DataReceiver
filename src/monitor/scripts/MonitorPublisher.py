import rospy
from monitor.msg import Anesthesia

def ShutDownAction():
    print("A monitor publisher is turned off")

# todo: class不能多开,因为topic的名字没有指定下标
class MonitorPublisher:

    monitorIndex = 0

    def __init__(self):
        self.dataReady = False
        self.msgBuffer = Anesthesia()

        # auto counter
        self.index = MonitorPublisher.monitorIndex
        MonitorPublisher.monitorIndex += 1
        print("Creating Monitor publisher %d" % self.index)

        # Init ROS communication
        # ROS节点初始化,anonymous=False
        rospy.init_node("anesthesia_publisher%d" % self.index)
        # 创建一个Publisher,发布名是/anesthesia_info的topic，消息类型是Anesthesia.msg,队列长度为1
        self.pub = rospy.Publisher("/anesthesia_info", Anesthesia, queue_size=1)
        # 设置循环的频率
        self.rate = rospy.Rate(10)

        # Shutdown callback
        # rospy.on_shutdown(MonitorPublisher.shutDownAction)

    def AddMsg(self, hl7data):  # Lateral should be a dict
        # Message generation

        # Enable data publishing
        self.dataReady = True

    def LoopSending(self):
        while not rospy.is_shutdown():
            if self.dataReady:
                self.pub.publish(self.msgBuffer)
                self.dataReady = False

                rospy.loginfo("publish anesthesia message")

            # self.rate.sleep()

    def __del__(self):
        print("Deconstructing Monitor publisher %d" % self.index)
