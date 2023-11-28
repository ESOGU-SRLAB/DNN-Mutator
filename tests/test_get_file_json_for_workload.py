import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QFileDialog

from tests.test_control_file_directory import control_file_directory


def get_file_json_for_workload():
    """Take JSON-based workload files to use for V&V process in IM-FIT"""
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setNameFilter(("*.json"))

    if dialog.exec():
        file_name = dialog.selectedFiles()

        control_status = control_file_directory(file_name[0])

        if file_name[0].endswith(".json") and control_status == True:
            with open(file_name[0], mode="r", encoding="utf-8") as file:
                data = file.read()
                self.ui.textEdit_3.setPlainText(data)


class TestGetFileJsonForWorkload(unittest.TestCase):
    def test_get_file_json_for_workload_with_banned_characters(self):
        # Test if the function correctly handles file names with banned characters
        with patch("PyQt5.QtWidgets.QFileDialog.exec") as mock_exec:
            with patch("PyQt5.QtWidgets.QFileDialog.selectedFiles") as mock_selected_files:
                mock_exec.return_value = True
                mock_selected_files.return_value = ["my/file?name.json"]
                get_file_json_for_workload()
                # Check if the file content is not set to the UI
                self.assertEqual(self.ui.textEdit_3.toPlainText(), "")