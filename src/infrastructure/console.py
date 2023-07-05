import rich
import os
from rich.console import Console

class elftools_console:
    def __init__(self, filename: str):
        self._filename: str = filename
        self.__init_console()
        self.__start_console()
        self._main_loop: any = None

    def __init_console(self):
        self._console: any = Console()
        self.__init_footer()
        pass

    def __init_footer(self):
        self._console.print(self._filename)
        pass

    def __start_console(self):
        self.update()

    def update(self):
        pass
