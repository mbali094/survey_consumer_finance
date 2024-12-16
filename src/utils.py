import sys
import shutil
from src.exception import CustomException
from zipfile import ZipFile


def unzipping_file(filepath):

    try:
        
        with ZipFile(filepath, "r") as obj:
            obj.extractall("data")

    except Exception as e:
        raise CustomException(e, sys)