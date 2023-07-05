import pathlib

class path_converter:
    def __init__(self):
        pass
    
    def convert_path_absolute(self, target_path: str) -> str:
        path: pathlib.Path = pathlib.Path(target_path)
        if(path.is_absolute()):
            return target_path
        else:
            return path.resolve()
        
    def convert_path_relative(self, target_path: str) -> str:
        path: pathlib.Path = pathlib.Path(target_path)
        if(path.is_absolute()):
            return path.relative_to(path.cwd())
        else:
            return target_path
