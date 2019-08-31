import unittest
from logger import Logger   # imports the class "Logger" from file "logger.py"

logger_target_stub = ""     # This is a global variable that will simulate the logger's target. It starts as an empty string, and
                            # it will be populated with whatever message that gets passed over to either the "info" or "error" methods
                            # under the "Logger" class

def logger_target_stub_function(input_text):        # This is a "stub" target function I defined, that will be passed into the constructor
    global logger_target_stub                       # method of the "Logger" class. This stub function will later be used through the "info"
    logger_target_stub = input_text                 # or the "error" methods to log messages to the target (and not to console). In my
                                                    # implementation, this stub function will just be logging the message into the global
                                                    # variable "logger_target_stub" which will be simulating the logger's target.

class loggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
    
    def test_info(self):
        ''' Tests the info function to see if it logs the correct message to the target '''
        # Arrange
        sampleLog = Logger(logger_target_stub_function)     # Instantiating the "Logger" Class Object, and setting its "_target" function
                                                            # as the stub function I defined. This means that the messages will be logged
                                                            # to "target" (whatever it might be), and not to console.
        # Act
        sampleLog.info("some important info message")
        # Assert
        self.assertEqual(logger_target_stub, '[INFO] some important info message', "The info function failed to log the correct message to target.")
    
    def test_error(self):
        ''' Tests the error function to see if it logs the correct message to the target '''
        # Arrange
        sampleLog = Logger(logger_target_stub_function)     # Instantiating the "Logger" Class Object, and setting its "_target" function
                                                            # as the stub function I defined. This means that the messages will be logged
                                                            # to "target" (whatever it might be), and not to console.
        # Act
        sampleLog.error("some important error message")
        # Assert
        self.assertEqual(logger_target_stub, '[WARNING] some important error message', "The error function failed to log the correct message to target.")
    