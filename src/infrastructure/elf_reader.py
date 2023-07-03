from typing import Protocol

import io
from infrastructure.elf import elf64_header, elf64_program_header

class elf_reader():
    def __init__(self, filename: str):
        self._filename: str = filename
        self._elf64_header: str

    def read_elf_header(self) -> elf64_header:
        self._elf64_header = elf64_header()
        with open(self._filename, "rb") as file:
            file.readinto(self._elf64_header)
        return self._elf64_header