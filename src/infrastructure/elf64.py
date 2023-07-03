#define	ET_NONE 0
#define	ET_REL 1
#define	ET_EXEC 2
#define	ET_DYN 3
#define	ET_CORE 4

#define PT_LOAD 1
#define PT_DYNAMIC 2
#define PT_INTERP 3
#define PT_NOTE 4
#define PT_SHLIB 5
#define PT_PHDR 6
#define PT_TLS 7
from ctypes import *

class elf64_header(Structure):
    _fields_ = (
        ('identifier', c_char * 16), 
        ('type', c_uint16), 
        ('machine', c_uint16), 
        ('version', c_uint32), 
        ('entry_point_address', c_uint64), 
        ('program_header_offset', c_uint64), 
        ('section_header_offset', c_uint64), 
        ('flags', c_uint32), 
        ('size', c_uint16), 
        ('program_header_size', c_uint16), 
        ('program_header_number', c_uint16), 
        ('section_header_size', c_uint16), 
        ('section_header_number', c_uint16), 
        ('section_header_table_string_index', c_uint16)
        )

class elf64_program_header(Structure):
    _fields_ = (
        ('type', c_uint32), 
        ('flags', c_uint32), 
        ('offset', c_uint64), 
        ('virtual_address', c_uint64), 
        ('physical_address', c_uint64), 
        ('file_size', c_uint64), 
        ('memory_size', c_uint64), 
        ('alignment', c_uint64)
    )

class elf64_section_header(Structure):
    _fields_ = (
        ('name', c_uint32), 
        ('type', c_uint32), 
        ('flags', c_uint64), 
        ('address', c_uint64), 
        ('offset', c_uint64), 
        ('size', c_uint64), 
        ('link', c_uint32), 
        ('info', c_uint32), 
        ('address_alignment', c_uint64), 
        ('entry_size', c_uint64)
    )
