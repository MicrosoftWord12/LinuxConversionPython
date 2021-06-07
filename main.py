import cmd
from cmd import Cmd
import os

# My Classes
from ListDirs import ls


class Prompt(Cmd):
    prompt = f"<{os.getlogin()}> "

    def do_ls(self, s):
        ls.ListDirs().lsHandler(s)


    def do_test(self, s):
        print("testing Console")


Prompt().cmdloop()
