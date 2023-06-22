import os


class FileSystem:
    def __init__(self, directoryPath = None, isDirectory = False, isRoot = False):
        if directoryPath is None or len(directoryPath) < 0:
            raise Exception("Invalid directoryPath given!!")
        
        if not isDirectory and isRoot:
            raise Exception("FileSystem Object can't represent a root directory if isDirectory is False")
        
        head, tail = os.path.split(directoryPath)

        if tail is None or len(tail) < 1:
            raise Exception("Enter a valid directory")
        
        self.__isDirectory = isDirectory
        self.__isRoot = isRoot
        self.__basePath = head
        self.__name = tail

        self.__contents = {
            'directories': {}, 
            'files': {}
        }

        # Automatically set the size if the obj represents a file
        self.__size = os.stat(directoryPath).st_size if not isDirectory else 0

    # Getters
    def getPath(self): return os.path.join(self.__basePath, self.__name)
  
    def getName(self): return self.__name

    def getContents(self): return self.__contents

    def getDirectories(self): return self.__contents['directories']

    def getFiles(self): return self.__contents['files']

    def isDirectory(self): return self.__isDirectory

    def isRoot(self): return self.__isRoot

    def getSize(self): return self.__size

    #Setters
    def updateContents(self, directories = {}, files = {}):
        for k, v in directories.items():
            if self.__contents['directories'].get(k) is None:
                self.__contents['directories'][k] = v
            else: raise Exception(f"Directory {k} already exists")

        for k, v in files.items():
            if self.__contents['files'].get(k) is None:
                self.__contents['files'][k] = v
            else: raise Exception(f"File {k} already exists")

    def updateDirectorySize(self): 
        if not self.__isDirectory:
            raise ("Files cannot update their size")

        for directoryObjects in self.__contents['directories'].values():
            self.__size += directoryObjects.getSize()
        for fileObjects in self.__contents['files'].values():
            self.__size += fileObjects.getSize()
        
