from typing import List

def read_log_files(files : List[str]) -> List[str]:
    """Read Data from a list of file and load them into 1 List of Dictionary 

    Args:
        files (List[str]) : list of file path (str)

    Returns:
        List : List of content based on files.
    """
    contents = []
    for file_path in files:
        with open(file_path, "r") as file:
            content = file.read()
            contents.append(content)

    return contents
