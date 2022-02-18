#create a I2C bus
i2c_channel = 1
scl_pin = 19
sda_pin = 18
address = 0x60

class mcp4725:
    def __init__(self, channel, address):
        self.channel = channel
        self.address = address
    
    def mcp4725_setup(self, scl_pin, sda_pin):
        import machine
        self.i2c = machine.I2C(self.channel, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))

    def mcp4725_send(self, value):
        import machine
        buf=bytearray(2)
        buf[0]=(value >> 8) & 0xFF
        buf[1]=value & 0xFF
        self.i2c.writeto(self.address, buf)

test1 = mcp4725(i2c_channel, address)
test1.mcp4725_setup(scl_pin, sda_pin)
