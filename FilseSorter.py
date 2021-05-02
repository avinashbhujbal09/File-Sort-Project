import os
import shutil

folders = {
    "Videos": ['.mp4', '.mkv'],
    "Music": ['.wav', '.mp3'],
    "Documents": ['.doc', '.xlsx', '.xls', '.pdf', '.csv', '.txt'],
    "Pictures": ['.jpg', '.png'],
    "Zip": ['.zip', '.rar'],
    "App": ['.exe']
}


class sortFile:
    def __init__(self):
        self.dir_loc = ''
        self.other_name = ''
        self.count = 1
        self.other_loc = ''

    def Status(self, file, folder):
        print(f"Total file :{len(os.listdir(self.dir_loc))}| file \"{file}\" move to :\"{folder}\" left "
              f"{len(os.listdir(self.dir_loc)) - self.count}")
        self.count += 1

    def is_exist(self, location):
        if os.path.exists(location):
            return True
        return False

    def create_move(self, ext, file_name, location):
        found = False
        for folder_name in folders:
            if "." + ext in folders[folder_name]:
                if folder_name not in os.listdir(location):
                    os.mkdir(os.path.join(location, folder_name))
                if not self.is_exist(os.path.join(location, folder_name, file_name)):
                    shutil.move(os.path.join(self.dir_loc, file_name), os.path.join(location, folder_name))
                    self.Status(file_name, folder_name)
                else:
                    print(file_name + " This file is already exist in folder " + folder_name)
                found = True
        if not found:
            if "Other" not in os.listdir(location):
                os.mkdir(os.path.join(location, "Other"))
            if not self.is_exist(os.path.join(location, "Other", file_name)):
                shutil.move(os.path.join(self.dir_loc, file_name), os.path.join(location, "Other"))
                self.Status(file_name, "Other")
            else:
                print(file_name + " This file is already exist in folder Other ")

    def rename_folder(self, location):
        for folder in os.listdir(location):
            for folder_name in folders:
                if os.path.isdir(os.path.join(location, folder)):
                    if folder_name.upper() == folder.upper():
                        os.rename(os.path.join(location, folder), os.path.join(location, folder.capitalize()))

    def processing(self, location):
        conf = input("\nWarning ! This process is not reversible do you want to continue ? Y/N :")
        if conf.upper() == 'Y':
            for file in os.listdir(self.dir_loc):
                if os.path.isfile(os.path.join(self.dir_loc, file)):
                    self.create_move(file.split(".")[-1], file, location)

    def is_empty(self):
        if len(os.listdir(self.dir_loc)) == 0:
            print("This folder is empty")
            return False
        return True

    def check_path(self, ):
        pass

    def help(self):
        print("use \n -p --for profile location (C:\\user\\xxx)")
        print("ex: cd:\\user\\xxx\\xxx -p")
        print("-to --for specific location ")
        print("ex: cd:\\user\\xxx\\xxx -to cd:\\user\\xxx\\xxx")
        exit()

    def menu(self):
        try:
            location = ''
            print("type -h for help")
            usr_cmd = input("Sort Location :").strip()
            self.dir_loc = usr_cmd.split("-")[0].strip()

            if '-to' in usr_cmd:
                self.other_loc = usr_cmd.split("-to")[-1].strip()
            elif '-p' in usr_cmd:
                self.other_loc = os.path.expanduser("~")
            elif '-h' in usr_cmd:
                self.help()

            if self.other_loc != '':
                if self.is_exist(self.other_loc) and self.is_exist(self.dir_loc):
                    location = self.other_loc.strip()
                    self.rename_folder(location)
                    print(f"File Location :\"{self.dir_loc}\" sort to the Location :\"{self.other_loc}\"")
                else:
                    print("Path not Found !!")
            else:
                if self.is_exist(self.dir_loc):
                    location = self.dir_loc.strip()
                    self.rename_folder(location)
                    print(f"File Location :\"{self.dir_loc}\" sort to same location")
                else:
                    print(self.dir_loc + " not found !!")
            print(f"The files in the directory {self.dir_loc} are :")
            if self.is_empty():
                for file in os.listdir(self.dir_loc):
                    print(file)
            self.processing(location)
        except FileNotFoundError:
            print("file not found")

sortFile = sortFile()
sortFile.menu()
