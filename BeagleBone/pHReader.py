"""
 Based on https://github.com/SparkysWidgets/MinipHBFW

 A simple library to support http:#www.sparkyswidgets.com/Projects/MiniPh.aspx
 on BeagleBone Black. Likely compatible with Raspbery Pi (minor changes might
 be required). Requires SciPy and python-smbus.

 Evan Galpin 2015
"""
import smbus as I2C
import pHParams
import time

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
        self.addr = addr
        self.i2c = I2C.SMBus(1)
        self.params = pHParams.pHParams()


    def read(self):
        """Read and assemble the 12-bit reading from the MCP3221 of the MinipH.

        :return : Integer between 0 and 4096 (2^12).
        """
        reading = self.i2c.read_i2c_block_data(self.addr, 0x00, 2)
        return (reading[0] << 8) + reading[1]


    def calc_ph(self, reading):
        """Calculates the pH based on millivolts reading from ADC of MinipH

        :param reading: Raw 12-bit reading from MinipH
        :return : Integer. 0.0 <= return <= 14.0
        """
        reading = reading - self.params.intercept
        return round(reading / self.params.slope, 2)


def main():
    """Test function to ensure that your system is working properly and to
    obtain calibration readings.

    """
    phr = pHReader()
    while True:
        sample = phr.read()
        print sample
        print phr.calc_ph(sample)
        print
        time.sleep(1)


if __name__ == '__main__':
    main()
