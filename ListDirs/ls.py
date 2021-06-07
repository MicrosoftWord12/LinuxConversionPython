import os


class ListDirs(object):
    def lsHandler(self, s: str):
        if s.find("ls -la"):
            self._lsAddon()
        elif s.find("ls"):
            self._listDirs()

    def _listDirs(self):
        if os.name.startswith("!,.\\?"):
            pass
        else:
            print(os.curdir)

    def _lsAddon(self):
        if os.name.startswith("!,.\\?"):
            print(os.curdir)
