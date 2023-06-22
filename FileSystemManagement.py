import json
import os
import shutil
import sys

from FileSystem import FileSystem
import Helpers

class FileSystemManagement:
    def populateFileSystem(fileSystemObject: FileSystem) -> None:
        if not fileSystemObject.isDirectory():
            raise Exception("Cannot populate a file")
        
        fileSystemPath = fileSystemObject.getPath()

        # Scan the directory
        with os.scandir(fileSystemPath) as entries:
            directories, files = {}, {}
            for entry in entries:
                if entry.is_dir():
                    directories[entry.name] = (FileSystem(directoryPath = entry.path, isDirectory = True))
                elif entry.is_file():
                    files[entry.name] = (FileSystem(directoryPath = entry.path))

            fileSystemObject.updateContents(directories, files)

        fsysDirectories = fileSystemObject.getDirectories()
        if len(fsysDirectories) > 0:
            for fsysDirectoryObj in fsysDirectories.values():
                FileSystemManagement.populateFileSystem(fileSystemObject = fsysDirectoryObj)

        fileSystemObject.updateDirectorySize()

    def saveJson(
            fileSystemObject: FileSystem, 
            savePath: str, 
            fileName: str, 
            modifications: list = []
        ) -> None:

        """
        Modifications List Will be applied while recursion
        """


        def _recur(fileSystemObject: FileSystem) -> dict:
            jsonData = {}
            jsonData['name'] = fileSystemObject.getName()
            jsonData['isDirectory'] = fileSystemObject.isDirectory()
            jsonData['size'] = fileSystemObject.getSize()

            jsonData['subDirectories_count'] = len(fileSystemObject.getDirectories())
            jsonData['files_count'] = len(fileSystemObject.getFiles())
            jsonData['path'] = fileSystemObject.getPath()

            jsonData['contents'] = {}
            jsonData['contents']['directories'] = {}
            jsonData['contents']['files'] = {}

            # Rcursive Case
            for name, fsysObj in fileSystemObject.getDirectories().items():
                jsonData['contents']['directories'][name] = _recur(fileSystemObject = fsysObj)
            for name, fsysObj in fileSystemObject.getFiles().items():
                jsonData['contents']['files'][name] = _recur(fileSystemObject = fsysObj) 

            for modification in modifications:
                Helpers.updateJson(jsonData, modification[0], modification[1])

            return jsonData
        
        jsonData = _recur(fileSystemObject)

        with open(os.path.join(savePath, fileName), 'w') as fileHandle:
            json.dump(obj = jsonData, fp = fileHandle)
        





    


    

        