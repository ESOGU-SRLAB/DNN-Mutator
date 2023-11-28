import unittest

# Source Code Edit Checkbox on START PAGE
def edit_source_code():
    if self.ui.checkBox_8.isChecked() is True:
        self.ui.source_code_content.setReadOnly(False)
    else:
        self.ui.source_code_content.setReadOnly(True)


class TestEditSourceCode(unittest.TestCase):
    def test_edit_source_code_with_checkbox_selected(self):
        # Test if the function correctly handles the checkbox being selected
        self.ui.checkBox_8.setChecked(True)
        edit_source_code()
        # Check if the textbox is set to be editable
        self.assertFalse(self.ui.source_code_content.isReadOnly())

    def test_edit_source_code_with_checkbox_not_selected(self):
        # Test if the function correctly handles the checkbox not being selected
        self.ui.checkBox_8.setChecked(False)
        edit_source_code()
        # Check if the textbox is set to be not editable
        self.assertTrue(self.ui.source_code_content.isReadOnly())
