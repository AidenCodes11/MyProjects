import os
import sys
import tempfile
import shutil
import re

_NO_BACKUP = 0xFFFFFFFF

@property
def NO_BACKUP():
    return _NO_BACKUP

backups = {}
last_backup = tuple()

# Notice: Please be careful with this function. It will create sub folders in the folder you give it, and the sub folders'
# names will be every file extension (like the file extension of hello.txt is txt) of all the files in the folder you
# originaly gave it. And then it will move all the files with the matching file extension into those folders. If you are
# unpleased with the organization, do not panic and please delete the organize call and replace it with:
# restore_backup()
# without the "#" and recover your files from there.

# Please do not turn off warnings and backup unless needed
# Please do not delete any backup files
def organize(folder_path: str, warn: bool = True, backup_path: str | None = None, supress_backup: int = 0) -> None:
    global backups, last_backup
    folder_path = os.path.abspath(folder_path)

    if (backup_path is None or (not os.path.exists(str(backup_path)))) and NO_BACKUP is not supress_backup:
        backup_path = os.path.join(tempfile.gettempdir(), os.path.basename(folder_path) + "_BACKUP")
        while os.path.exists(backup_path):
            backup_path += "_"
        backup_path = os.path.join(backup_path, os.path.basename(folder_path))
        os.makedirs(backup_path, exist_ok=True)

    if backup_path:
        backup_path = os.path.abspath(backup_path)
        backups[folder_path] = backup_path
        last_backup = (folder_path, backup_path)
        shutil.copytree(folder_path, backup_path, dirs_exist_ok=True)

    if warn:
        continue_ = input("Do you want to continue? Doing this on some folders may have unintended consequences (default n, y or n)! ").lower() == "y"
        if not continue_:
            print('a')
            return
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        raise TypeError("path is not a folder.")

    forbidden_patterns = [
        r"^/$",  # Root on Unix
        r"^/bin(/.*)?$",
        r"^/boot(/.*)?$",
        r"^/dev(/.*)?$",
        r"^/etc(/.*)?$",
        r"^/lib(/.*)?$",
        r"^/proc(/.*)?$",
        r"^/root(/.*)?$",
        r"^/sbin(/.*)?$",
        r"^/sys(/.*)?$",
        r"^/usr(/.*)?$",
        r"^/var(/.*)?$",
        r"^/lib64(/.*)?$",
        r"^/opt(/.*)?$",
        r"^/home?$",
        r"^C:\\$",  # Root on Windows
        r"^C:\\Windows(\\.*)?$",  # Windows and subpaths
        r"^C:\\System Volume Information(\\.*)?$",
        r"^C:\\\$Recycle\.Bin(\\.*)?$",
        r"^C:\\Program Files(\\.*)?$",
        r"^C:\\Program Files \(x86\)(\\.*)?$",
        r"^C:\\ProgramData(\\.*)?$",
        r"^C:\\Recovery(\\.*)?$",
        r"^C:\\Users?$"
    ]

    compiled_patterns = [re.compile(p, re.IGNORECASE) for p in forbidden_patterns]

    def is_forbidden(path: str) -> bool:
        normalized = os.path.abspath(path).rstrip("\\/")
        return any(p.fullmatch(normalized) for p in compiled_patterns)

    if is_forbidden(folder_path): raise PermissionError("This is a critical system path")

    temp_path = os.path.join(tempfile.gettempdir(), f"_tmp_{os.path.basename(folder_path)}_")
    while os.path.exists(temp_path):
        temp_path += "_"
    shutil.copytree(folder_path, temp_path)

    extension_set = set()
    empty_folders = []

    for root, dirs, files_ in os.walk(folder_path):
        for file in files_:
            if sys.platform == "win32" and os.path.basename(file) == "desktop.ini":
                continue
            full_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1] or "no_extension"
            extension_set.add(ext)

            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)

            shutil.move(full_path, os.path.join(ext_folder, file))

        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            if not os.listdir(dir_path):
                empty_folders.append(dir_path)

    empty_folder_dest = os.path.join(folder_path, "Empty Folders")
    os.makedirs(empty_folder_dest, exist_ok=True)

    for empty in empty_folders:
        try:
            shutil.move(empty, empty_folder_dest)
        except Exception as e:
            print(f"Could not move {empty}: {e}")

    shutil.rmtree(temp_path)

def restore_backup(folder_path: str = None, del_after: bool = True):
    global backups, last_backup
    if folder_path is None:
        folder, backup = last_backup
    else:
        folder = folder_path
        backup = backups[folder]
    to_copy = os.path.dirname(backup)
    if not os.path.exists(to_copy):
        print("Error: backup host folder got deleted")
        return
    if not os.path.exists(backup):
        print("Error: backup folder got deleted")
        return
    if os.path.exists(folder):
        shutil.rmtree(folder)
    shutil.copytree(to_copy, os.path.dirname(folder), dirs_exist_ok=True)
    if del_after:
        shutil.rmtree(to_copy)


#organize(r"C:\Users\angel\PycharmProjects\PYTHON\docs\NUKE")
#import time
#time.sleep(10)
#restore_backup()