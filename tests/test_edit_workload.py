import unittest


# Workload Edit Checkbox on START PAGE
def edit_workload():
    if self.ui.checkBox_5.isChecked() is True:
        self.ui.textEdit_3.setReadOnly(False)
    else:
        self.ui.textEdit_3.setReadOnly(True)


class TestEditWorkload(unittest.TestCase):
    def test_edit_workload_with_checkbox_selected(self):
        # Test if the function correctly handles the checkbox being selected
        self.ui.checkBox_5.setChecked(True)
        edit_workload()
        # Check if the textbox is set to be editable
        self.assertFalse(self.ui.textEdit_3.isReadOnly())

    def test_edit_workload_with_checkbox_not_selected(self):
        # Test if the function correctly handles the checkbox not being selected
        self.ui.checkBox_5.setChecked(False)
        edit_workload()
        # Check if the textbox is set to be not editable
        self.assertTrue(self.ui.textEdit_3.isReadOnly())
