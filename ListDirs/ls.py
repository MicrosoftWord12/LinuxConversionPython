import os

#  make Array with the letter starting with for example
# badStuff from _listDirs
# array = ["!", "'", "."]
# Its for hiding files etc

class ListDirs(object):
    def lsHandler(self, s: str):
        if s == "-la":
            self._lsAddon()
        else:
            self._listDirs()

    def _listDirs(self):
        for e in os.listdir():
            if e.startswith(".") or e.startswith("!"):
                pass
            else:
                print(e)

    def _lsAddon(self):
        for e in os.listdir():
            print(e)



