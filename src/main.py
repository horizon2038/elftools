from infrastructure.elf_reader import elf_reader
from infrastructure.elf64 import elf64_header
from infrastructure.elf_common import *
from infrastructure.console import *
from infrastructure.path_converter import path_converter

import sys
import os
import pathlib

def main():
    _path_converter: path_converter = path_converter()

    args: list = sys.argv
    file_path: str = _path_converter.convert_path_absolute(args[1])
    file_path_str: str = "/Users/horizon/Documents/Program/A9N/Build/x86_64/A9NRun/kernel/kernel.elf"
    _elf_reader: elf_reader = elf_reader(file_path_str)
    _elf64_header: elf64_header = _elf_reader.read_elf_header()
    _console: elftools_console = elftools_console(file_path)

    print("type: {}".format(elf_type(_elf64_header.type).name))
    print("machine: {}".format(elf_machine(_elf64_header.machine).name))
    print("version: {}".format(elf_version(_elf64_header.version).name))
    print("entry_point_address: {}".format(hex(_elf64_header.entry_point_address)))
    print("program_header_offset: {}".format(hex(_elf64_header.program_header_offset)))
    print("section_header_offset: {}".format(hex(_elf64_header.section_header_offset)))
    print("flags: {}".format(elf_flags(_elf64_header.flags).name))
    print("size: {}".format(hex(_elf64_header.size)))
    print("program_header_size: {}".format(hex(_elf64_header.program_header_size)))
    print("program_header_number: {}".format(_elf64_header.program_header_number))
    print("section_header_size: {}".format(hex(_elf64_header.section_header_size)))
    print("section_header_number: {}".format(_elf64_header.section_header_number))
    print("section_header_table_string_index: {}".format(_elf64_header.section_header_table_string_index))

if __name__ == "__main__":
    main()

