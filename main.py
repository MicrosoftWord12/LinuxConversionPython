import cmd
from cmd import Cmd
import os

# My Classes
from ListDirs import ls
from ChangeDirs import cd


class Prompt(Cmd):
    prompt = f"<{os.getlogin()}> "

    @staticmethod
    def do_ls(s):
        ls.ListDirs().lsHandler(s)

    @staticmethod
    def do_cd(s: str):
        cd.ChangeDirs().cdHandler(s)

    @staticmethod
    def do_test(s):
        print("testing Console")


Prompt().cmdloop()
