import unittest
from test_control_file_directory import control_file_directory
from unittest.mock import patch
from PyQt5.QtWidgets import QFileDialog


def get_file_py_for_source_code():
    """Take Python-based source code to use for V&V process in IM-FIT"""
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setNameFilter(("*.py"))

    if dialog.exec():
        file_name = dialog.selectedFiles()

        control_status = control_file_directory(file_name[0])

        # .py file is choosed by the user
        if file_name[0].endswith(".py") and control_status == True:
            # file_name[0] is directory of file
            with open(file_name[0], mode="r", encoding="utf-8") as json_file:
                source_code_data = json_file.read()
                # Source code directory is added to the text
                self.ui.source_code_directory_text.setPlainText(
                    str(file_name[0])
                )
                # source adds to the UI
                self.ui.source_code_content.setPlainText(source_code_data)

                # IM-FIT DB
                source_code_file_full_directory = file_name[0].split("/")
                source_code_file_name = source_code_file_full_directory[-1]


class TestGetFilePyForSourceCode(unittest.TestCase):
    def test_get_file_py_for_source_code_with_banned_characters(self):
        # Test if the function correctly handles file names with banned characters
        with patch("PyQt5.QtWidgets.QFileDialog.exec") as mock_exec:
            with patch("PyQt5.QtWidgets.QFileDialog.selectedFiles") as mock_selected_files:
                mock_exec.return_value = True
                mock_selected_files.return_value = ["my/file?name.py"]
                get_file_py_for_source_code()
                # Check if the file name is not set to the UI
                self.assertEqual(self.ui.source_code_directory_text.toPlainText(), "")

    def test_get_file_py_for_source_code_without_banned_characters(self):
        # Test if the function correctly handles file names without banned characters
        with patch("PyQt5.QtWidgets.QFileDialog.exec") as mock_exec:
            with patch("PyQt5.QtWidgets.QFileDialog.selectedFiles") as mock_selected_files:
                mock_exec.return_value = True
                mock_selected_files.return_value = ["my_file_name.py"]
                get_file_py_for_source_code()
                # Check if the file name is set to the UI
                self.assertEqual(self.ui.source_code_directory_text.toPlainText(), "my_file_name.py")


if __name__ == '__main__':
    unittest.main()
