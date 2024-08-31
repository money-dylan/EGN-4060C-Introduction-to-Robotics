#!/usr/bin/python

import sys
import time
import math

sys.path.append('../lib/python/amd64')
import robot_interface as sdk


if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL  = 0xff

    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.161", 8082)
    state = sdk.HighState()
    cmd = sdk.HighCmd()
    udp.InitCmdData(cmd)

    motiontime = 0
    while True:
        time.sleep(0.002)
        motiontime = motiontime + 1

        udp.Recv()
        udp.GetRecv(state)

        cmd.mode = 0      # 0:idle, default stand      1:forced stand     2:walk continuously
        cmd.gaitType = 0
        cmd.speedLevel = 0
        cmd.footRaiseHeight = 0
        cmd.bodyHeight = 0
        cmd.euler = [0, 0, 0]
        cmd.velocity = [0, 0]
        cmd.yawSpeed = 0.0
        cmd.reserve = 0
        if(motiontime > 1000 and motiontime < 4500):
            cmd.mode = 2
            cmd.gaitType = 1
            cmd.velocity = [0.4, 0] # -1  ~ +1
            cmd.yawSpeed = 0.4
            cmd.footRaiseHeight = 0.1
            print("circle\n")
            print(motiontime)
        elif(motiontime > 4500 and motiontime < 8000):
            cmd.mode = 12    # 0:idle, default stand      1:forced stand     2:walk continuously
            # cmd.gaitType = 0
            # cmd.speedLevel = 0
            # cmd.footRaiseHeight = 0
            # cmd.bodyHeight = 0
            # cmd.euler = [0, 0, 0]
            # cmd.velocity = [0, 0]
            # cmd.yawSpeed = 0.0
            # cmd.reserve = 0
            print("dance 1\n")
            print(motiontime)
        elif(motiontime > 8000 and motiontime < 12000):
            cmd.mode = 13      # 0:idle, default stand      1:forced stand     2:walk continuously
            # cmd.gaitType = 0
            # cmd.speedLevel = 0
            # cmd.footRaiseHeight = 0
            # cmd.bodyHeight = 0
            # cmd.euler = [0, 0, 0]
            # cmd.velocity = [0, 0]
            # cmd.yawSpeed = 0.0
            # cmd.reserve = 0
            print("dance 2\n")
            print(motiontime)
        # elif(motiontime > 12000):
        #     cmd.mode = 0      # 0:idle, default stand      1:forced stand     2:walk continuously
        #     cmd.gaitType = 0
        #     cmd.speedLevel = 0
        #     cmd.footRaiseHeight = 0
        #     cmd.bodyHeight = 0
        #     cmd.euler = [0, 0, 0]
        #     cmd.velocity = [0, 0]
        #     cmd.yawSpeed = 0.0
        #     cmd.reserve = 0
        #     print("idle\n")
        #     print(motiontime)
            

        udp.SetSend(cmd)
        udp.Send()