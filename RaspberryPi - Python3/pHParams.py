"""
 An object to represent the slope of a pH probe using MinipH. This class takes
 care of importing calibrations, exporting calibrations, and calculating the
 slope and intercept of a probe based on the calibrations.

 Calibrations are kept in ph.json by default, but other filenames can be
 provided.  These values should be changed based on your system readings and
 calibration solutions used.  It is recommended that you choose calibration
 points based on the range of pH readings you expect. This library supports
 any number of calibration points 2 or greater, just add them to your
 calibration file as required.

 Evan Galpin 2015, Edited by phpfs 2016

"""
import json
import scipy.stats as scipy


class pHParams(object):
    def __init__(self, calibs=None):
        """Creates a new pHParams object and initializes its calibs dictionary

        :param calibs: Optional. A dictionary of calibrations in the form of
        key,val == phVal,millivolts
        """
        if calibs == None:
            self.calibs = self.read_calibs()
        else:
            self.calibs = calibs
        self.slope, self.intercept = self.calc_ph_slope()


    def set_calib(self, phVal, reading):
        """Assigns a calibration value in the calibration dictionary

        :param phVal: the value on the pH scale being calibrated. Used as the
        key in the calibs dictionary.
        :param reading: the raw probe output for the given pH value. Used as
        the value in calibs dictionary.
        """
        self.calibs[str(phVal)] = int(reading)


    def del_calib(self, phVal):
        """Removes a calibration from the calibs dictionary. If permanent
        deletion is required, don't forget to write_calibs after deleting. An
        error is not raised if the key (phVal) is not found.

        :param phVal: The pH value whose calibration should be removed.
        """
        self.calibs.pop(str(phVal), None)


    def get_calib(self, phVal):
        """Obtains the raw millivolts reading for a given pH value.

        :param phVal: The pH value to obtain the reading for.
        :return : int > 0 on success, -1 on failure.
        """
        phVal = str(phVal)
        if phVal in self.calibs:
            return self.calibs[phVal]
        else:
            return -1


    def read_calibs(self, calibs_file="ph.json"):
        """Reads calibrations from file.

        :param calibs_file: The file to read params from
        :return : dictionary object containing ph,millivolts key/value pairs
        """
        jf = open(calibs_file)
        calibs = json.loads(jf.read())
        jf.close()
        return calibs


    def write_calibs(self, calibs_file="ph.json"):
        """Writes calibrations to file.

        :param calibs_file: The file to write params to
        """
        jf = open(calibs_file, 'w')
        jf.write(json.dumps(self.calibs, indent=4, sort_keys=True))
        jf.close()


    def calc_ph_slope(self):
        """Based on the calibration readings, a line of best fit is calulated.
        This line will be used to calculate the pH step i.e. millivolts to
        pH value.
        """
        xy = [ [float(x), float(y)] for x, y in self.calibs.items() ]
        slope, intercept, r_value, p_value, std_err = scipy.linregress(xy)
        return slope, intercept

