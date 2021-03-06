import os
import can


# os.system('sudo ip link set can0 type can bitrate 250000')  # 500k bitrate
# os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel='can0', bustype='socketcan')

for msg in can0:
    msgdata = ','.join(str(i) for i in msg.data)
    print("id is " + str(msg.arbitration_id))
    print(msgdata)

    # DEBUG: send back
    # myId = 0x121
    # can0.send(can.Message(arbitration_id=myId, data=msg.data))

if msg is None:
    print('Timeout occurred, no message.')

# os.system('sudo ifconfig can0 down')
