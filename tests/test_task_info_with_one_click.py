from PyQt5.QtTest import QTest


# Select Task with One Click on Workload Page
def task_info_with_one_click():
    clicked_item_text = self.ui.listWidget_21.currentItem().text()
    self.ui.textEdit_14.clear()

    json_type_task = self.ui.plainTextEdit.toPlainText()
    tasks_list_json = json.loads(json_type_task)

    for i in range(0, len(tasks_list_json["Tasks"])):
        task_name = str(tasks_list_json["Tasks"][i]["Task"]["Task_ID"])
        if task_name == clicked_item_text:
            task_detail = str(tasks_list_json["Tasks"][i]["Task"])
            for j in task_detail:
                self.ui.textEdit_14.setPlainText(
                    self.ui.textEdit_14.toPlainText() + j
                )

def test_task_info_with_one_click(self):
    # Test that the correct task information is displayed when a task is clicked
    self.ui.listWidget_21.addItem("Task 1")
    self.ui.listWidget_21.addItem("Task 2")
    self.ui.plainTextEdit.setPlainText('{"Tasks": [{"Task": {"Task_ID": "Task 1", "Description": "This is task 1"}}, '
                                       '{"Task": {"Task_ID": "Task 2", "Description": "This is task 2"}}]}')
    QTest.mouseClick(self.ui.listWidget_21.viewport(), Qt.LeftButton)
    self.assertEqual(self.ui.textEdit_14.toPlainText(), '{\n  "Task_ID": "Task 1", \n  "Description": "This is task 1"\n}')

