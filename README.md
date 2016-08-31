[![Code Climate](https://codeclimate.com/github/Razer-OSVR/TestRail-Automation/badges/gpa.svg)](https://codeclimate.com/github/Razer-OSVR/TestRail-Automation)

# TestRail-Automation
A set of library plus cli where you can update your TestRail case right after a test is finished.
TestRail-Automation aims to be agnostic of any test implementation, although you can use all classes and methods to extend your Python test coverage; however if you have any software test written in any other computer language, you can use TestRail-Automation cli after parse the output of your test.

## Python dependencies
- urllib2
- json
- base64
- argparse

## How to use?
First of all, you need to define in your TestRail a `Suite of tests` and set a `Test Run` with test cases you want perform.
* Get help? `python main.py -h`
* Example:
  `python main.py --project "OSVR" --suite "TestRailAutomation" --run "Python_API" --case "Check Python Integration" --status "PASSED" --comment "It worked as expected."`
    
