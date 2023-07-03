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