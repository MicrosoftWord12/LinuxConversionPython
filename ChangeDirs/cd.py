import os
import sys

class ChangeDirs(object):
    def cdHandler(self, s: str):
        os.system("cd")
        for e in os.listdir():
            print(e)

        if s.lower() == " ..":
            os.system("cd ..")
            for e in os.listdir():
                print(e)


