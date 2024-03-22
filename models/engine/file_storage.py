#!/usr/bin/python3
#from models.base_model import BaseModel
import json
import os
class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """return dictionary of previously created objects"""
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
            """write json representation of an object to a file"""
            tmp_dict = {}
            for key, value in FileStorage.__objects.items():
                tmp_dict[key] = value.to_dict()
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                json.dump(tmp_dict, f)
    def reload(self):
        """returns the dictionary representation of an object from the file"""
        from models.base_model import BaseModel
        tmp = {}

        if os.path.isfile(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.loads(f.read())
        for key, value in tmp.items():
            tmp_obj = BaseModel(**value)
            self.new(tmp_obj)
