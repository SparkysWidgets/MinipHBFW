Welcome To: MinipH Basic Example Firmware!!
================================

##### Note: This is for the MinipH Hardware Version 1 Branch

This is the base example sketch for using MinipH hardware. The usage is quite straight forward :sunglasses:.
MinipH digitizes the analog voltage from the pH AFE using an I2C ADC.

Adding pH Sensors has never been easier
-------------------------

Using MinipH with any project is extremely easy, the MCP3221 is a very popular ADC which is easy to work with whether you use Arduino or any other method, even BitBanging over a FTDI USB to Serial!

Please see [MinipH's Project page](http://www.sparkyswidgets.com/Projects/MinipH.aspx) for more information!
<http://www.sparkyswidgets.com/Projects/MinipH.aspx>

Whats in the firmware?
-------------------------

Not too Much really! The flow is very straight forward. Set up our I2C (2Wire, Aka "Wire") interface assign the address of our ADC.
Then we can ask it for its MSB and LSBs, put them together to form the 12 bit reading back and bobs your uncle :aus:

Installation Info
-------------------------

The best part of this design and firmware is nothing extra to install. copy paste, clone whatever you method all you need is similar hardware and this code!!

Basic Usage
-------------------------

Usage of MinipH example code is very easy. There are only a few commands, but that doesnt mean you cant augment this further.

####Some of the commands are:
- I : Calibration and general Info dump
- C7 : set pH7 Calibration point
- C4 : set pH7 Calibration point


Hardware: Schematics and Layouts
-------------------------

- Take a look in [MinipH's Hardware Repo](https://github.com/SparkysWidgets/MinipHHW) for the EAGLE files!
- Check out my USB pH interface[LeoPhi](http://www.sparkyswidgets.com/Projects/LeoPhi.aspx) for a powerful and easy to use USB PH Probe interface!


License Info
-------------------------

<p>This is a fully open source project released under the CC BY license</p>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width: 0px;" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">MinipH</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="www.sparkyswidgets.com" property="cc:attributionName" rel="cc:attributionURL">Ryan Edwards, Sparky's Widgets</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br />
Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="/projects/MinipH.aspx" rel="dct:source">http://www.sparkyswidgets.com/projects/MinipH.aspx</a>