import os
import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)
        
        a, b = self._generator._file_count(self._generator._root_dir)
        print("The No of files and Directories is: ",a,b)

class _TreeGenerator:
    def __init__(self,root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    def summary(self):
        file, directory = self._file_count(self._root_dir)
        return(file,directory)

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix =""):
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            else:
                self._add_file(entry, prefix, connector)



    def _add_directory(
        self, directory, index, entries_count, prefix, connector
    ):
        self._tree.append(f"{prefix}{connector}" f"\033[1;34;40m {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(
            directory = directory,
            prefix = prefix,
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector}" f"\033[1;32;40m {file.name}")
    

    def _file_count(self, directory, prefix = ""):
        DirCount = 0
        FileCount = 0

        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())

        for index, entry in enumerate(entries):
            if entry.is_dir():
                
                DirCount += 1
            else:
                FileCount += 1
        
        return(FileCount,DirCount)


