
class FilePath:
    txt_file_path = "C:\\Repo\\otus_repo\\test_files"

    def get_file_path(self, file_name):
        return f"{self.txt_file_path}\\{file_name}"

