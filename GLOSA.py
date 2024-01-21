#单车辆下不停车通过路口引导，多路口请多次更新distance和time
#目标建模，输入，距离下一个路口的距离(m)，红绿灯时间(s)，最大车速与最小车速，输出推荐车速(km/s)
class GLOSA(object):

    def __init__(self, distance, gtime, rtime, nowtime, maxsp, minsp):
        self.distance = distance
        self.gtime = gtime
        self.rtime = rtime
        self.nowtime = nowtime #nowtime若为绿灯则直接为绿灯时间，若为红灯则为绿灯加红灯时间
        self.maxsp = maxsp  #车流量主要影响速度范围，请外置函数对此处理
        self.minsp = minsp
        self.speed = 0

    def rsc(self):
        if self.nowtime > self.gtime:
            return (self.distance*3.6)/(self.rtime+self.gtime-self.nowtime)
        else:
            return (self.distance*3.6)/(self.gtime-self.nowtime)

    def recommended_speed(self):
        self.speed = self.rsc()
        if self.speed >= self.maxsp:
            self.speed = self.maxsp
        if self.speed <= self.minsp:
            self.speed = self.minsp
        return self.speed
