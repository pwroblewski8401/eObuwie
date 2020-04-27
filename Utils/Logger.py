import os
import datetime


class Logger:
    def __init__(self, testName):
        dir_artifact = f'{os.getcwd()}\\Artifacts\\'
        if not os.path.isdir(dir_artifact):
            os.mkdir(dir_artifact)
        self.testName = testName
        logdir = f'{os.getcwd()}\\Artifacts\\Logs\\'
        print(logdir)
        if not os.path.isdir(logdir):
            os.mkdir(logdir)

        self.logfile_name = f'{logdir}{testName[:15]}_{datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}'
        print(self.logfile_name)
        file = open(self.logfile_name, "w")
        file.close()
        if not os.path.isfile(self.logfile_name):
            print("Unable to create log file!")
            return False

    def info(self, message):
        f = open(self.logfile_name, "a")
        f.write(f"{datetime.datetime.now()} - {self.testName} - info - {message}\n")
        f.close()
        return message

    def error(self, message):
        f = open(self.logfile_name, "a")
        f.write(f"{datetime.datetime.now()} - {self.testName} - error - {message}\n")
        f.close()
        return message

