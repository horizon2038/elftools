from infrastructure.elf_reader import elf_reader
from infrastructure.elf import elf64_header

def main():
    file_path: str = "/Users/horizon/Documents/Program/A9N/Build/x86_64/A9NRun/kernel/kernel.elf"
    _elf_reader: elf_reader = elf_reader(file_path)
    _elf64_header: elf64_header = _elf_reader.read_elf_header()
    print("entry_point_address: {}".format(hex(_elf64_header.entry_point_address)))
    pass

if __name__ == "__main__":
    main()

