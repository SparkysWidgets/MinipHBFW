from Adafruit_I2C import Adafruit_I2C as I2C
import pHParams
import time
#define ADDRESS 0x4D # MCP3221 A5 in Dec 77 A0 = 72 A7 = 79)
                     # A0 = x48, A1 = x49, A2 = x4A, A3 = x4B, 
                     # A4 = x4C, A5 = x4D, A6 = x4E, A7 = x4F

class pHReader(object):
    """Reads values from the pH probe + MinipH and converts to pH
    """
    def __init__(self, addr=0x4D, busnum=-1):
        """Creates an pH Reader with a given address and on a specific I2C bus
        (if provided). If no bus number is provided, the default Adafruit_I2C
        bus will be selected (I2C2).

        :param addr: The address of the device on the I2C bus. This is the
        address of the MCP3221 of the MinipH. Use i2cdetect -y -r 0 and
        i2cdetect -y -r 1 to probe for connected devices. See
        https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/i2c
        for details and installation instructions.

        :param busnum: Optional. The I2C bus number that the probe is on.
        Default Adafruit_I2C bus (I2C2) used if not specified.
        """
        self.i2c = I2C(addr, busnum)
        self.params = pHParams.pHParams()


    def read(self):
        """Read and assemble the 12-bit reading from the MCP3221 of the MinipH.

        :return : Integer between 0 and 4096 (2^12).
        """
        return (self.i2c.readU8(0x00) * 256) + self.i2c.readU8(0x01)


    def calc_ph(self, reading):
        """Calculates the pH based on millivolts reading from ADC of MinipH

        :param reading: Raw 12-bit reading from MinipH
        :return : Integer. 0.0 <= return <= 14.0
        """
        reading = reading - self.params.interceptcept
        return round(reading / self.params.slope, 2)


def main():
    """Test function
    """
    phr = pHReader()
    while True:
        print phr.read()
        time.sleep(0.5)


if __name__ == '__main__':
    main()