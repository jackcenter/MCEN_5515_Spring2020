import smbus
import time
bus = smbus.SMBus(1)        # 1 is for custom, non-shield

# I2C address of Arduino Slave
address = 0x07

LEDst = [0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01, 0x01]
for s in LEDst:
    bus.write_byte(address, s)
    time.sleep(5)
