from FileSystemManagement import FileSystemManagement as fsm
from FileSystem import FileSystem
import Helpers

import os
import sys

cwd = sys.path[0]

directoryPath = os.path.join(cwd, '..', '..', 'Github', 'becomeCODER-CPP')
fsysObj = FileSystem(directoryPath, isDirectory = True, isRoot = True)

fsm.populateFileSystem(fsysObj)

fsm.saveJson(
    fsysObj, 
    os.path.join(cwd, 'TestFolder'),  
    'Test2_Report.json', 
    modifications = [
        ('size', Helpers.prettifyFileSizes)
    ]
)