import os
import datetime


class Logger:
    def __init__(self, testName):
        self.testName = testName
        logdir = f'{os.getcwd()}\\Artifacts\\Logs\\'
        if not os.path.isdir(logdir):
            os.mkdir(logdir)

        self.logfilename = f'{logdir}{testName}_{datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}'
        print(self.logfilename)
        file = open(self.logfilename, "w")
        file.close()
        if not os.path.isfile(self.logfilename):
            print("Unable to create log file!")
            return False

    def info(self, message):
        f = open(self.logfilename, "a")
        f.write(f"{datetime.datetime.now()} - {self.testName} - info - {message}\n")
        f.close()
        return message

    def error(self, message):
        f = open(self.logfilename, "a")
        f.write(f"{datetime.datetime.now()} - {self.testName} - error - {message}\n")
        f.close()
        return message