import unittest

# Select Task on Create on Workload Page
def task_selection():
    selected_row = self.ui.listWidget_21.currentItem().text()
    row = selected_row.split("\n")
    self.ui.listWidget_22.addItems(row)


class TestTaskSelection(unittest.TestCase):
    def test_task_selection_with_valid_input(self):
        # Test if the function correctly adds the selected task to the list with valid input
        self.ui.listWidget_21.addItem("My Task")
        self.ui.listWidget_21.setCurrentRow(0)
        task_selection()
        # Check if the selected task is added to the list
        self.assertEqual(self.ui.listWidget_22.item(0).text(), "My Task")

    def test_task_selection_with_invalid_input(self):
        # Test if the function does not add anything to the list with invalid input (no task selected)
        self.ui.listWidget_21.addItem("My Task")
        task_selection()
        # Check if the list is empty
        self.assertEqual(self.ui.listWidget_22.count(), 0)
