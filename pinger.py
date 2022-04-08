from subprocess import Popen
from subprocess import PIPE
import time


class device(Popen):
    def __init__(self,deviceip,devicetype,kd,status=True):
        self.deviceip=deviceip
        self.devicetype = devicetype
        self.kd = kd
        self.status=status
        super().__init__('ping -n 2 '+deviceip,stdout=PIPE)
    def checkitout(self):
        if self.poll()==self.status:
            if self.poll():
                self.status= False
                print(self)
            else:
                self.status= True
                print(self)
    # def wait(self, timeout: float | None = ...) -> int:
    #     return super().wait(timeout)
    def betterwait(self)->None:
        super().wait()
        self.checkitout()
    #     if self.poll():
    #         self.setstatus(False)
    #     else:
    #         self.setstatus(True)
    # def setstatus(self,newstatus):
    #     if self.status != newstatus:
    #         self.status=newstatus
    #         print(self)
    def __str__(self):
        return f'{self.deviceip} {self.status} {self.poll()}'
goodip = ['127.0.0.1','sigint','10']
badip = ['199.167.6.57','shiran','40']
numberofdevices = 100
subs = []
# for i in range(numberofdevices):
#     subs.append(subprocess.Popen(args='ping '+goodip,stdout=subprocess.PIPE))
# for i in subs:
#     i.wait()
#     x = i.poll()
#     print(x)
# for i in range(numberofdevices//2):
#     subs.append(device(*goodip))
for i in range(numberofdevices):
    subs.append(device(*badip))
    # time.sleep(1)
for i in range(numberofdevices):
    subs.append(device(*goodip))
loopcount = 0
timer = time.time()
while True:
    [i.betterwait() for i in subs]
    # print([str(i) for i in subs])
    print(f'loopcount : {loopcount}\nlooptime : {time.time()-timer}')
    timer=time.time()
    loopcount+=1
    subs = [device(x.deviceip,x.devicetype,x.kd,x.status) for x in subs]