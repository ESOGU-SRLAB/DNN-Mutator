import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QFileDialog
from tests.test_control_file_directory import control_file_directory


# Take ".json" file function
def fiplan_get_file_json():
    """Take FI Plan to use for V&V process in IM-FIT"""
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setNameFilter(("*.json"))

    if dialog.exec():
        file_name = dialog.selectedFiles()

        control_status = control_file_directory(file_name[0])

        if file_name[0].endswith(".json") and control_status == True:
            self.ui.listWidget_11.addItem(str(file_name[0]))


class TestFiplanGetFileJson(unittest.TestCase):
    def test_fiplan_get_file_json_with_banned_characters(self):
        # Test if the function correctly handles file names with banned characters
        with patch("PyQt5.QtWidgets.QFileDialog.exec") as mock_exec:
            with patch("PyQt5.QtWidgets.QFileDialog.selectedFiles") as mock_selected_files:
                mock_exec.return_value = True
                mock_selected_files.return_value = ["my/file?name.json"]
                fiplan_get_file_json()
                # Check if the file name is not added to the list
                self.assertEqual(self.ui.listWidget_11.count(), 0)

    def test_fiplan_get_file_json_without_banned_characters(self):
        # Test if the function correctly handles file names without banned characters
        with patch("PyQt5.QtWidgets.QFileDialog.exec") as mock_exec:
            with patch("PyQt5.QtWidgets.QFileDialog.selectedFiles") as mock_selected_files:
                mock_exec.return_value = True
                mock_selected_files.return_value = ["my_file_name.json"]
                fiplan_get_file_json()
                # Check if the file name is added to the list
                self.assertEqual(self.ui.listWidget_11.count(), 1)
