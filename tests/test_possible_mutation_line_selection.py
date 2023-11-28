import unittest

def possible_mutation_line_selection():
    """Select Line For Mutation on FI Plan Page"""
    possible_mutation_line = self.ui.listWidget.currentItem().text()
    self.ui.textEdit_13.setPlainText(possible_mutation_line)


def test_possible_mutation_line_selection(self):
    # Test if the function correctly selects and displays the selected line
    self.ui.listWidget.addItem("test line")
    self.ui.listWidget.setCurrentRow(0)
    self.assertEqual(self.ui.textEdit_13.toPlainText(), "test line")
