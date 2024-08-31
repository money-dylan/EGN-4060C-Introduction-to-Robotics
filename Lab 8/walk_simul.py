#!/usr/bin/python

import sys
import time
import math

sys.path.append('../lib/python/amd64')
import robot_interface as sdk


if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL  = 0xff

    # Initialize UDP connections for both robots
    udp_robot1 = sdk.UDP(HIGHLEVEL, 8080, "192.168.206.187", 8082)  # IP of the first robot  # 814
    udp_robot2 = sdk.UDP(HIGHLEVEL, 8081, "192.168.206.203", 8082)  # IP of the second robot  # 604

    state_robot1 = sdk.HighState()
    state_robot2 = sdk.HighState()

    cmd_robot1 = sdk.HighCmd()
    cmd_robot2 = sdk.HighCmd()

    udp_robot1.InitCmdData(cmd_robot1)
    udp_robot2.InitCmdData(cmd_robot2)

    motiontime = 0
    while True:
        time.sleep(0.002)
        motiontime += 1

        # Receive state information from both robots
        udp_robot1.Recv()
        udp_robot1.GetRecv(state_robot1)
        udp_robot2.Recv()
        udp_robot2.GetRecv(state_robot2)

        # Set common command parameters for both robots
        for cmd in [cmd_robot1, cmd_robot2]:
            cmd.mode = 0  # 0:idle, default stand      1:forced stand     2:walk continuously
            cmd.gaitType = 0
            cmd.speedLevel = 0
            cmd.footRaiseHeight = 0
            cmd.bodyHeight = 0
            cmd.euler = [0, 0, 0]
            cmd.velocity = [0, 0]
            cmd.yawSpeed = 0.0
            cmd.reserve = 0
            
            if 1000 < motiontime < 3000:
                cmd.mode = 2
                cmd.gaitType = 1
                cmd.velocity = [0.4, 0]  # Range: -1 to +1
                cmd.yawSpeed = 0
                cmd.footRaiseHeight = 0.1
                print("walk\n")

            if 3000 < motiontime < 6000:
                cmd.mode = 12
                cmd.gaitType = 1
                cmd.velocity = [0.0, 0]  # Range: -1 to +1
                cmd.yawSpeed = 0
                cmd.footRaiseHeight = 0.1
                print("dance 1\n")

            if 6000 < motiontime < 9000:
                cmd.mode = 13
                cmd.gaitType = 1
                cmd.velocity = [0.0, 0]  # Range: -1 to +1
                cmd.yawSpeed = 0
                cmd.footRaiseHeight = 0.1
                print("dance 2\n")

            if motiontime > 9000:
                cmd.mode = 0
                cmd.velocity = [0, 0]
                print("idle\n")

        # Send commands to both robots
        udp_robot1.SetSend(cmd_robot1)
        udp_robot1.Send()
        udp_robot2.SetSend(cmd_robot2)
        udp_robot2.Send()
