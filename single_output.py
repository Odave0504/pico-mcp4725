import machine

# I2C bus settings
i2c_channel = 1
scl_pin = 19
sda_pin = 18
address = 0x60

class mcp4725:
    def __init__(self, channel, address):
        self.channel = channel
        self.address = address
    
    def mcp4725_init(self, scl_pin, sda_pin):
        self.i2c = machine.I2C(self.channel, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))

    def mcp4725_send(self, value):
        buf=bytearray(2)
        buf[0]=(value >> 8) & 0xFF
        buf[1]=value & 0xFF
        self.i2c.writeto(self.address, buf)


# Output value
voltage0_out = 1.65 # 0~3.3V
dac0_value = int(voltage0_out / 3.3 * 4095) # convert voltage to 12-bit DAC value

# DAC initialization & send value
dac0 = mcp4725(i2c_channel, address)
dac0.mcp4725_init(scl_pin, sda_pin)
dac0.mcp4725_send(dac0_value)
