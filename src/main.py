""" IM-FIT """

#!/usr/bin/env python3

import os
import re
import ast
import sys
import time
import ast
import json
import subprocess
import xml.etree.ElementTree as ET
import random
import astunparse
import platform
import astunparse
import matplotlib.pyplot as plt
import importlib
import mutator
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6 import QtGui

from PySide6 import *

from modules import *

from widgets import *

from ui_main import Ui_MainWindow

import scan_process
import monitoring_process


class MainWindow(QMainWindow):
    """IM-FIT UI Window"""

    global RUN_ORDER_LIST_JUST_PATH
    RUN_ORDER_LIST_JUST_PATH = []

    global ROS_SOURCE_CODE
    ROS_SOURCE_CODE = ""

    global POSSIBLE_MUTANT_LIST
    POSSIBLE_MUTANT_LIST = []

    global ZIPPED_LIST
    ZIPPED_LIST = []

    global ZIPPED_ROS_LIST
    ZIPPED_ROS_LIST = []

    global ROS_SOURCE_MUTANT
    ROS_SOURCE_MUTANT = []

    global SOURCE_AND_MUTANT_CODE
    SOURCE_AND_MUTANT_CODE = []

    global FAULT_NAME_LIST
    FAULT_NAME_LIST = []

    global FIPLAN_DIRECTORY_LIST
    FIPLAN_DIRECTORY_LIST = []

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        #  APP NAME
        title = "IM-FIT"
        description = "IM-FIT"

        self.setWindowTitle(title)
        self.ui.titleRightInfo.setText(description)
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)

        # DATA
        self.code_part_for_mutation = []

        # FUNCTIONS
        # TAKE FILE FUNCTIONS
        def control_file_directory(file_name):
            """Check the file directory for the unwanted characters"""
            banned_characters = ["(", ")", "[", "]", "?", "<", ">", "\\", "|"]
            for i in file_name:
                if i in banned_characters:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Warning)
                    message_box.setText("File directory must be edited!")
                    message_box.setWindowTitle("Warning!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()
                    return False
            return True

        # Take ".py" file for source code
        def get_file_py_for_source_code():
            """Take Python-based source code to use for V&V process in IM-FIT"""
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.py"))
            if dialog.exec():
                file_name = dialog.selectedFiles()
                control_status = control_file_directory(file_name[0])
                # .py file is choosed by the user
                if file_name[0].endswith(".py") and control_status:
                    with open(file_name[0], mode="r", encoding="utf-8") as json_file:
                        source_code_data = json_file.read()
                        # Source code directory is added to the text
                        self.ui.plainTextEdit_10.setPlainText(str(file_name[0]))
                        # source adds to the UI
                        self.ui.plainTextEdit_9.setPlainText(source_code_data)
        def get_dnn_file_py_for_source_code():                                     #Gökhan--------------------------- 
            """Take Python-based source code to use for V&V process in IM-FIT"""
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.py"))
            if dialog.exec():
                file_name_dnn = dialog.selectedFiles()
                control_status = control_file_directory(file_name_dnn[0])
                # .py file is choosed by the user
                if file_name_dnn[0].endswith(".py") and control_status:
                    with open(file_name_dnn[0], mode="r", encoding="utf-8") as json_file:
                        dnn_source_code_data = json_file.read()
                        # Source code directory is added to the text
                        self.ui.plainTextEdit_dnn_source.setPlainText(str(file_name_dnn[0]))
                        # source adds to the UI
                        self.ui.plainTextEdit_53.setPlainText(dnn_source_code_data)     #Gökhan
                        # rapor_dosyasi = "rapor.txt"
                        # self.dnn_parameter = QComboBox(self)
                        # parameter=self.dnn_parameter.currentText()
                        # tensorflow_parametreleri_bul_ve_degistir(source_code_data,parameter,"if",rapor_dosyasi) #Gökhan--------------------------- 

        # Take ".json" file for workload
        def workload_get_file_json():
            """Take JSON-based workload files to use for V&V process in IM-FIT"""
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.json"))
            if dialog.exec():
                file_name = dialog.selectedFiles()
                control_status = control_file_directory(file_name[0])
                if file_name[0].endswith(".json") and control_status is True:
                    with open(file_name[0], mode="r", encoding="utf-8") as file:
                        data = file.read()
                        self.ui.plainTextEdit_13.setPlainText(str(file_name[0]))
                        self.ui.plainTextEdit_14.setPlainText(data)

        # Take ".json" file function
        def fiplan_get_file_json():
            """Take FI Plan to use for V&V process in IM-FIT"""
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.json"))
            if dialog.exec():
                file_name = dialog.selectedFiles()
                control_status = control_file_directory(file_name[0])
                if file_name[0].endswith(".json") and control_status:
                    self.ui.listWidget_11.addItem(str(file_name[0]))

        # EDIT BUTTONS FOR START PAGE

        # Source Code Edit Checkbox on START PAGE
        def edit_source_code():
            if self.ui.checkBox_8.isChecked() is True:
                self.ui.plainTextEdit_9.setReadOnly(False)
            else:
                self.ui.plainTextEdit_9.setReadOnly(True)

        # Workload Edit Checkbox on START PAGE
        def edit_workload():
            if self.ui.checkBox_5.isChecked() is True:
                self.ui.plainTextEdit_14.setReadOnly(False)
            else:
                self.ui.plainTextEdit_14.setReadOnly(True)

        # Select Code Snippets wit One Click
        def code_snippet_select_with_one_clicked():
            try:
                clicked_item_text = self.ui.code_snippet_list.currentItem().text()

                with open(
                    "code_snippets.json", encoding="utf-8"
                ) as code_snippets_from_json:
                    code_snippets_name_list = json.load(code_snippets_from_json)

                    added_snippet_regex_length = len(
                        code_snippets_name_list["code_snippets"]
                    )
                    for i in range(0, added_snippet_regex_length):
                        code_snippet_name = code_snippets_name_list["code_snippets"][i][
                            "Snippets"
                        ]["Snippet_Name"]

                        if clicked_item_text == code_snippet_name:
                            code_snippet_description = code_snippets_name_list[
                                "code_snippets"
                            ][i]["Snippets"]["Process"]
                            self.ui.plainTextEdit_15.setPlainText(
                                code_snippet_description
                            )
            except AttributeError:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Error!")
                message_box.setWindowTitle("Error!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

        #Gökhan----------------------------------------------------------------------Start
        # Select DNN Code Snippets wit One Click
        def dnn_code_snippet_select_with_one_clicked():
            try:
                clicked_item_text = self.ui.dnn_code_snippet_list.currentItem().text()

                with open(
                    "dnn_code_snippets.json", encoding="utf-8"
                ) as dnn_code_snippets_from_json:
                    code_snippets_name_list = json.load(dnn_code_snippets_from_json)

                    added_snippet_regex_length = len(
                        code_snippets_name_list["code_snippets"]
                    )
                    for i in range(0, added_snippet_regex_length):
                        code_snippet_name = code_snippets_name_list["code_snippets"][i][
                            "Snippets"
                        ]["Snippet_Name"]

                        if clicked_item_text == code_snippet_name:
                            code_snippet_description = code_snippets_name_list[
                                "code_snippets"
                            ][i]["Snippets"]["Process"]
                            self.ui.plainTextEdit_code_snippet_details.setPlainText(
                                code_snippet_description
                            )
            except AttributeError:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Error!")
                message_box.setWindowTitle("Error!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()
        #Gökhan----------------------------------------------------------------------End



        # Select Snippet Button on Start Page
        def code_snippet_selection():
            code_snippet_list_is_empty = True
            len_of_selected_code_snippets = self.ui.listWidget_8.count()
            selected_row = self.ui.code_snippet_list.currentItem().text()
            row = selected_row.split("\n")

            # Double Enter Check
            if len_of_selected_code_snippets:
                for i in range(len_of_selected_code_snippets):
                    code_snippet_list_element = self.ui.listWidget_8.item(i).text()
                    if code_snippet_list_element == selected_row:
                        code_snippet_list_is_empty = False
                if code_snippet_list_is_empty is True:
                    self.ui.listWidget_8.addItems(row)
            else:
                self.ui.listWidget_8.addItems(row)

        
        # Select DNN Snippet Button on Start Page /GÖKHAN-------START
        def dnn_code_snippet_selection():
            dnn_code_snippet_list_is_empty = True
            dnn_len_of_selected_code_snippets = self.ui.dnn_selected_snippet.count()
            dnn_selected_row = self.ui.dnn_code_snippet_list.currentItem().text()
            row = dnn_selected_row.split("\n")

            # Double Enter Check
            if dnn_len_of_selected_code_snippets:
                for i in range(dnn_len_of_selected_code_snippets):
                    dnn_code_snippet_list_element = self.ui.dnn_selected_snippet.item(i).text()
                    if dnn_code_snippet_list_element == dnn_selected_row:
                        dnn_code_snippet_list_is_empty = False
                if dnn_code_snippet_list_is_empty is True:
                    self.ui.dnn_selected_snippet.addItems(row)
            else:
                self.ui.dnn_selected_snippet.addItems(row)        
        #/GÖKHAN -----------------------------------------------------------------END
        #Gökhan---------------------------------Start
        def dnn_mutate_parameter_selection():
            dnn_code_mutate_list_is_empty = True
            dnn_len_of_selected_code_parameters = self.ui.listWidget_selected_mutate_parameters.count()
            dnn_selected_row = self.ui.listWidget_mutate_list.currentItem().text()
            row = dnn_selected_row.split("\n")

            # Double Enter Check
            if dnn_len_of_selected_code_parameters:
                for i in range(dnn_len_of_selected_code_parameters):
                    dnn_code_mutate_list_element = self.ui.listWidget_selected_mutate_parameters.item(i).text()
                    if dnn_code_mutate_list_element == dnn_selected_row:
                        dnn_code_mutate_list_is_empty = False
                if dnn_code_mutate_list_is_empty is True:
                    self.ui.listWidget_selected_mutate_parameters.addItems(row)
            else:
                self.ui.listWidget_selected_mutate_parameters.addItems(row)
        #GÖKHAN-----------------------------------End
        def dnn_mutate_parameter_unselection():
            row = self.ui.listWidget_selected_mutate_parameters.currentRow()
            self.ui.listWidget_selected_mutate_parameters.takeItem(row)

        # Select Task on Create on Workload Page
        def task_selection():
            selected_row = self.ui.listWidget_21.currentItem().text()
            row = selected_row.split("\n")
            self.ui.listWidget_22.addItems(row)

        # Select Task with One Click on Workload Page
        def task_info_with_one_click():
            clicked_item_text = self.ui.listWidget_21.currentItem().text()
            self.ui.plainTextEdit_38.clear()
            json_type_task = self.ui.plainTextEdit.toPlainText()
            tasks_list_json = json.loads(json_type_task)
            for i in range(0, len(tasks_list_json["Tasks"])):
                task_name = str(tasks_list_json["Tasks"][i]["Task"]["Task_ID"])
                if task_name == clicked_item_text:
                    task_detail = str(tasks_list_json["Tasks"][i]["Task"])
                    for j in task_detail:
                        self.ui.plainTextEdit_38.setPlainText(
                            self.ui.plainTextEdit_38.toPlainText() + j
                        )

        def possible_mutation_line_selection():
            """Select Line For Mutation on FI Plan Page"""
            possible_mutation_line = self.ui.listWidget.currentItem().text()
            self.ui.plainTextEdit_18.setPlainText(possible_mutation_line)

        def fault_selection_from_library():
            """Select Fault From Fault Library on FI Plan Page"""
            global ZIPPED_LIST
            ZIPPED_LIST = []
            text_check = self.ui.plainTextEdit_18.toPlainText()
            if text_check:
                selected_line = self.ui.plainTextEdit_18.toPlainText()
                selected_fault = self.ui.listWidget_3.currentItem().text()

                text_selected_line_and_fault = (
                    selected_line + " #==># " + selected_fault
                )
                ZIPPED_LIST.append(text_selected_line_and_fault)
                line_and_fault = text_selected_line_and_fault.split("\n")
                self.ui.listWidget_7.addItems(line_and_fault)

        # This Function Shows Fault's Information from Fault Library on FI Plan Page
        def show_fault_info_with_one_click():
            try:
                clicked_item_text = self.ui.listWidget_3.currentItem().text()

                with open("fault_library.json", encoding="utf-8") as file:
                    fault_list = json.load(file)

                fault_list_size = self.ui.listWidget_3.count()

                for i in range(fault_list_size):
                    fault_name = fault_list["all_faults"][i]["fault"]["Fault_Name"]

                    if clicked_item_text == fault_name:
                        fault_description = fault_list["all_faults"][i]["fault"][
                            "Explanation"
                        ]
                        self.ui.plainTextEdit_19.setPlainText(fault_description)
            except:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Error!")
                message_box.setWindowTitle("Error!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

        def nth_replace(string, old, new, replace_num=1):
            """Replace Funtion"""

            left_join = old
            right_join = old
            if not old:
                old = " "
            groups = string.split(old)
            nth_split = [
                left_join.join(groups[:replace_num]),
                right_join.join(groups[replace_num:]),
            ]
            return new.join(nth_split)

        def mutation_process_function(target_text, start_json_value, finish_json_value):
            global SOURCE_AND_MUTANT_CODE
            global FAULT_NAME_LIST

            with open("fault_library.json", encoding="utf-8") as file:
                fault_list = json.load(file)

            for fault_number in range(start_json_value, finish_json_value):
                target_operators_from_library = fault_list["all_faults"][fault_number][
                    "fault"
                ]["Target_to_Change"]
                operators = target_operators_from_library.split(",")

                changed_operators_from_library = fault_list["all_faults"][fault_number][
                    "fault"
                ]["Changed"]
                using_fault_name = fault_list["all_faults"][fault_number]["fault"][
                    "Fault_Name"
                ]
                split_operators = changed_operators_from_library.split(",")
                for k in operators:
                    find_k_in_text = re.findall(k, target_text)
                    if find_k_in_text:
                        found_target = find_k_in_text[0]
                        number_of_pattern = len(find_k_in_text)
                        for changing_number in range(1, number_of_pattern + 1):
                            for changed_line in split_operators:
                                mutated_line = nth_replace(
                                    target_text,
                                    found_target,
                                    changed_line,
                                    replace_num=changing_number,
                                )
                                if mutated_line != target_text:
                                    # Mutated line is added to mutation list on IM-FIT UI
                                    self.ui.listWidget_4.addItem(mutated_line)
                                    # Original source code line and mutated line are added to
                                    # list to use for execution
                                    SOURCE_AND_MUTANT_CODE.append(target_text)
                                    SOURCE_AND_MUTANT_CODE.append(mutated_line)
                                    FAULT_NAME_LIST.append(using_fault_name)

            total_mut = self.ui.listWidget_4.count()
            self.ui.label_17.setText(str(total_mut))

        def fault_lib_size():
            with open("fault_library.json", encoding="utf-8") as file:
                fault_list = json.load(file)
            fault_library_size = len(fault_list["all_faults"])
            return fault_library_size

        def start_mutation():
            self.mutation_process_progress_bar()
            global FAULT_NAME_LIST
            with open("fault_library.json", encoding="utf-8") as file:
                fault_list = json.load(file)
            fault_library_size = fault_lib_size()
            if self.ui.checkBox_4.isChecked() is True:
                self.ui.listWidget_7.clear()
                self.ui.listWidget_7.setEnabled(False)
                len_selected_line_mutation = self.ui.listWidget.count()
                for i in range(0, len_selected_line_mutation):
                    line = self.ui.listWidget.item(i).text()
                    mutation_process_function(line, 0, fault_library_size)
            else:
                len_selected_line_mutation = self.ui.listWidget_7.count()
                for i in range(0, len_selected_line_mutation):
                    hata_ve_line = self.ui.listWidget_7.item(i).text()
                    split_hata_ve_line = hata_ve_line.split(" #==># ")
                    hata_ismi = split_hata_ve_line[1]
                    print(hata_ismi)
                    FAULT_NAME_LIST.append(hata_ismi)
                    line = split_hata_ve_line[0]
                    for fault_number in range(fault_library_size):
                        fault_name_from_library = fault_list["all_faults"][
                            fault_number
                        ]["fault"]["Fault_Name"]
                        if hata_ismi == fault_name_from_library:
                            mutation_process_function(
                                line, fault_number, fault_number + 1
                            )

        def random_hata_bas():
            fault_library_size = fault_lib_size()
            random_fault = random.randint(0, fault_library_size)
            target_text = self.ui.listWidget.currentItem().text()
            mutation_process_function(target_text, random_fault, random_fault + 1)

        def save_execution_plan():
            dialog = QFileDialog()
            path_name = QFileDialog.getExistingDirectory()
            if path_name:
                file_name = self.ui.plainTextEdit_22.toPlainText() + ".json"
                full_path = os.path.join(path_name, file_name)
                split_text = full_path.split("\n")
                self.ui.listWidget_13.addItems(split_text)
            else:
                self.show_information_box("Caution!", "File Name is required!")

        def execution_module_function():
            global ROS_SOURCE_MUTANT
            global ROS_SOURCE_CODE

            global FAULT_NAME_LIST

            killed_mutants_list = []
            survived_mutants_list = []
            equivalent_mutants_list = []

            all_mutant_list = []

            error_code_list = []

            killed_mutants = 0
            survived_mutants = 0
            equivalent_mutants = 0
            execution_timeout_list = []
            original_source_code_output = ""

            operating_system = platform.system()
            execution_fiplan_list_length = self.ui.listWidget_6.count()

            for execution_step in range(0, execution_fiplan_list_length):
                execution_fiplan_directory = self.ui.listWidget_6.item(
                    execution_step
                ).text()
                file_type_keywords = [
                    "_type_python.json",
                    "_type_launch.json",
                    "_type_rospy.json",
                ]
                for file_type_pattern in file_type_keywords:
                    find_file_type = re.findall(
                        file_type_pattern, execution_fiplan_directory
                    )
                    if find_file_type:
                        # ROS-Py execution settings
                        if find_file_type[0] == "_type_rospy.json":

                            killed_counter = 0
                            survived_counter = 0

                            # Length of ROS source mutant list
                            len_ros_source_mutant = len(ROS_SOURCE_MUTANT)
                            ros_working_directory = (
                                self.ui.plainTextEdit_33.toPlainText()
                            )
                            working_package_full_path_split = (
                                ros_working_directory.split("/")
                            )
                            working_package_full_path_split.pop(-1)
                            working_directory = ""

                            for i in working_package_full_path_split:
                                if not i == "":
                                    working_directory += "/" + i

                            for i in range(len_ros_source_mutant):
                                if i % 3 == 2:
                                    new_data = ROS_SOURCE_CODE.replace(
                                        ROS_SOURCE_MUTANT[i - 1], ROS_SOURCE_MUTANT[i]
                                    )
                                    fname = "mutant" + str(int(i / 3)) + ".py"
                                    complete_name = os.path.join(
                                        working_directory, fname
                                    )
                                    with open(
                                        complete_name, mode="w", encoding="utf-8"
                                    ) as file1:
                                        file1.write(new_data)

                                    subprocess.Popen(
                                        ["chmod", "+x", fname], cwd=working_directory
                                    )
                                    print("Mutant:", fname)
                                    try:
                                        roscore_process = subprocess.Popen(["roscore"])
                                        time.sleep(5)
                                        print("fname", fname)
                                        status_output = subprocess.Popen(
                                            [
                                                "rosrun",
                                                working_package_full_path_split[-2],
                                                fname,
                                            ]
                                        )
                                        status_output.wait(timeout=5)
                                    except subprocess.TimeoutExpired:
                                        status_output.terminate()
                                        roscore_process.terminate()
                                        survived_counter += 1
                                        print("#       Survived Mutant        #")
                                        print("\n\n")

                                    else:
                                        status_output.terminate()
                                        roscore_process.terminate()
                                        killed_counter += 1
                                        print("\n\n")
                                        print("#       Killed Mutant          #")
                                        print("\n\n")

                            print("#         Results              #")
                            print("\n\n")
                            print("Total Killed Mutant(s):", killed_counter)
                            print("Total Survived Mutant(s):", survived_counter)
                            print(
                                "\nMutation Score:",
                                (killed_counter / (killed_counter + survived_counter))
                                * 100,
                            )
                            print("-" * 32)
                            print("\n\n")

                        elif find_file_type[0] == "_type_launch.json":
                            killed_counter = 0
                            survived_counter = 0

                            fiplan_directory = self.ui.listWidget_36.item(0).text()
                            with open(fiplan_directory, encoding="utf-8") as json_file:
                                fault_list = json.load(json_file)

                            for i in range(len(fault_list)):
                                directory = fault_list[i]["Fault"]["File_Directory"]
                                split_directory = directory.split("/")
                                folder_name = split_directory[-3]
                                ros_exe_file_name = fault_list[i]["Fault"]["Exe_File"]
                                with open(
                                    directory, mode="r", encoding="utf-8"
                                ) as file:
                                    python_file_content = file.read()
                                source_code = fault_list[i]["Fault"]["Source_Code"]
                                mutant_code = fault_list[i]["Fault"]["Mutate_Code"]
                                mutation_process = python_file_content.replace(
                                    source_code, mutant_code
                                )
                                with open(
                                    directory, mode="w", encoding="utf-8"
                                ) as file:
                                    file.write(mutation_process)
                                print("Mutant:", str(i))

                                try:

                                    status_output = subprocess.Popen(
                                        [
                                            "roslaunch",
                                            folder_name,
                                            ros_exe_file_name,
                                        ]
                                    )
                                    status_output.wait(timeout=60)
                                except subprocess.TimeoutExpired:
                                    status_output.terminate()
                                    survived_counter += 1
                                    print("#      Survived Mutant        #")
                                    print("\n\n")

                                else:
                                    status_output.terminate()
                                    killed_counter += 1
                                    print("#     Killed Mutant           #")
                                    print("\n\n")

                                with open(
                                    directory, mode="w", encoding="utf-8"
                                ) as file:
                                    file.write(python_file_content)

                            print("#      Results            #")
                            print("\n\n")
                            print("Total Killed Mutant(s):", killed_counter)
                            print("Total Survived Mutant(s):", survived_counter)
                            print(
                                "\nMutation Score:",
                                (killed_counter / (killed_counter + survived_counter))
                                * 100,
                            )
                            print("\n\n")
                        else:
                            # Python script type
                            is_empty_dependent = self.ui.plainTextEdit_12.toPlainText()
                            if is_empty_dependent == "":
                                all_created_files = []
                                start_time = time.time()
                                timeout_counter = 0
                                source_code_text = self.ui.plainTextEdit_9.toPlainText()
                                mutant_save_location = (
                                        self.ui.plainTextEdit_24.toPlainText()
                                    )
                                original_source_code_name = "original_code.py"
                                data = source_code_text

                                if mutant_save_location != "":
                                    mutant_save_location_and_mutant_file = (
                                        os.path.join(mutant_save_location, original_source_code_name)
                                    )
                                    with open(
                                        mutant_save_location_and_mutant_file,
                                        mode="w",
                                        encoding="utf-8",
                                    ) as file:
                                        file.write(data)
                                else:
                                    with open(
                                        original_source_code_name, mode="w", encoding="utf-8"
                                    ) as file:
                                        file.write(data)
                                all_created_files.append(original_source_code_name)
                                mutation_list_size = self.ui.listWidget_4.count()
                                time_limit_per_process = (
                                    self.ui.plainTextEdit_25.toPlainText()
                                )
                                if operating_system == "Windows":
                                    subprocess.Popen(
                                        "python original_code.py", shell=True
                                    )
                                if operating_system == "Linux":
                                    subprocess.Popen(
                                        "python3 original_code.py", shell=True
                                    )
                                print("#       Original Code       #")
                                fiplan_directory = self.ui.listWidget_6.item(0).text()
                                with open(
                                    fiplan_directory, encoding="utf-8"
                                ) as json_file:
                                    fault_list = json.load(json_file)
                                file_name = self.ui.plainTextEdit_10.toPlainText()
                                file_name_split = file_name.split("/")
                                file_name_for_creating_mutant_file = file_name_split[-1]

                                for i in range(0, mutation_list_size):
                                    target_line_from_json = fault_list[i]["Fault"][
                                        "Source_Code"
                                    ]
                                    mutated_code_from_json = fault_list[i]["Fault"][
                                        "Mutate_Code"
                                    ]
                                    main_mutation_process = source_code_text.replace(
                                        target_line_from_json, mutated_code_from_json
                                    )
                                    fname = (
                                        "Mutant_no_"
                                        + str(i + 1)
                                        + "_"
                                        + file_name_for_creating_mutant_file
                                    )
                                    all_created_files.append(fname)
                                    data = main_mutation_process

                                    if mutant_save_location != "":
                                        mutant_save_location_and_mutant_file = (
                                            os.path.join(mutant_save_location, fname)
                                        )
                                        with open(
                                            mutant_save_location_and_mutant_file,
                                            mode="w",
                                            encoding="utf-8",
                                        ) as file:
                                            file.write(data)
                                    else:
                                        with open(
                                            fname, mode="w", encoding="utf-8"
                                        ) as file:
                                            file.write(data)
                                    print("\n\nFault Number: ", i)

                                    if operating_system == "Windows":
                                        if mutant_save_location != "":
                                            cmd = ["python", fname]
                                        else:
                                            cmd = ["python", fname]
                                            mutant_save_location = os.getcwd()
                                    if operating_system == "Linux":
                                        if mutant_save_location != "":
                                            cmd = ["python3", fname]
                                        else:
                                            cmd = ["python3", fname]
                                            mutant_save_location = os.getcwd()

                                    all_mutant_list.append(fname)
                                    try:
                                        subprocess.run(
                                            cmd,
                                            cwd=mutant_save_location,
                                            timeout=int(time_limit_per_process),
                                        )
                                    except subprocess.TimeoutExpired:
                                        if operating_system == "Windows":
                                            timeout_counter += 1
                                            killed_mutants += 1
                                            killed_mutants_list.append(
                                                "python " + fname
                                            )
                                            if mutant_save_location != "":
                                                cmd = ["python", fname]
                                            else:
                                                cmd = ["python", fname]
                                            execution_timeout_list.append(
                                                "python " + fname
                                            )
                                            continue
                                        if operating_system == "Linux":
                                            timeout_counter += 1
                                            killed_mutants += 1
                                            killed_mutants_list.append(
                                                "python3 " + fname
                                            )
                                            if mutant_save_location != "":
                                                cmd = ["python3", fname]
                                            else:
                                                cmd = ["python3", fname]
                                            execution_timeout_list.append(
                                                "python3 " + fname
                                            )
                                    else:
                                        os.chdir(mutant_save_location)
                                        if operating_system == "Linux":
                                            mutant_code_execution = "python3 " + fname
                                        if operating_system == "Windows":
                                            mutant_code_execution = "python " + fname

                                        # This subprocess function runs mutant codes
                                        # and takes their output.
                                        subprocess_output_status = (
                                            subprocess.getstatusoutput(
                                                mutant_code_execution
                                            )
                                        )
                                        mutant_code_output = subprocess_output_status[1]
                                        error_code_list.append(mutant_code_output)

                                        if subprocess_output_status[0] != 0:
                                            print(mutant_code_output)
                                            print("#      Killed Mutant         #")
                                            killed_mutants += 1
                                            killed_mutants_list.append(
                                                mutant_code_execution
                                            )
                                            error_code_list.append(mutant_code_output)
                                        else:
                                            if (
                                                mutant_code_output
                                                == original_source_code_output
                                            ):
                                                print(mutant_code_output)
                                                print(
                                                    "#          Equivalent Mutant           #"
                                                )
                                                equivalent_mutants += 1
                                                equivalent_mutants_list.append(
                                                    mutant_code_execution
                                                )
                                            else:
                                                print(mutant_code_output)
                                                print(
                                                    "#       Survived Mutant          #"
                                                )

                                                survived_mutants += 1
                                                survived_mutants_list.append(
                                                    mutant_code_execution
                                                )
                                end_time = time.time()
                                print("\n\n")
                                print(
                                    "#                     RESULTS                        #"
                                )
                                print("\n")
                                print("Process Time: ", end_time - start_time)
                                self.ui.listWidget_9.addItem(
                                    "Process Time:" + str(end_time - start_time)
                                )
                                print("\n")

                                mutation_score = (
                                    killed_mutants / (killed_mutants + survived_mutants)
                                ) * 100

                                print("Mutation Score: %", mutation_score)
                                self.ui.listWidget_9.addItem(
                                    "Mutation Score: %" + str(mutation_score)
                                )
                                print("\n")
                                print(
                                    "Number of Total Mutants:",
                                    killed_mutants
                                    + survived_mutants
                                    + equivalent_mutants,
                                )
                                self.ui.listWidget_9.addItem(
                                    "All Mutants: "
                                    + str(
                                        killed_mutants
                                        + survived_mutants
                                        + equivalent_mutants
                                    )
                                )
                                print("\n")
                                print("Killed Mutants: ", killed_mutants)
                                self.ui.listWidget_9.addItem(
                                    "Killed: " + str(killed_mutants)
                                )
                                print("Survived Mutants: ", survived_mutants)
                                self.ui.listWidget_9.addItem(
                                    "Survived: " + str(survived_mutants)
                                )
                                print("Equivalent Mutants: ", equivalent_mutants)
                                self.ui.listWidget_9.addItem(
                                    "Equivalent: " + str(equivalent_mutants)
                                )
                                print("Timeout: ", timeout_counter)
                                self.ui.listWidget_9.addItem(
                                    "Timeout: " + str(timeout_counter)
                                )
                                # Create graphics about mutation process
                                self.create_bar_chart(
                                    mutation_score,
                                    killed_mutants,
                                    survived_mutants,
                                    equivalent_mutants,
                                )
                                self.create_pie_chart(
                                    killed_mutants, survived_mutants, equivalent_mutants
                                )
                                print("\n")
                                print(
                                    "#                      DETAILS                       #"
                                )
                                print("\n")

                                killed_mutant_list_size = len(killed_mutants_list)
                                print("Killed Mutants List: ")
                                self.ui.listWidget_16.addItem("Killed Mutants List: ")
                                for i in range(killed_mutant_list_size):
                                    print(killed_mutants_list[i])
                                    self.ui.listWidget_16.addItem(
                                        str(killed_mutants_list[i])
                                    )
                                print("\n")
                                print("Survived Mutants List: ")
                                self.ui.listWidget_16.addItem("Survived Mutants List: ")
                                for i in survived_mutants_list:
                                    print(i)
                                    self.ui.listWidget_16.addItem(str(i))
                                print("\n")
                                print("Equivalent Mutants List: ")
                                self.ui.listWidget_16.addItem(
                                    "Equivalent Mutants List: "
                                )
                                for i in equivalent_mutants_list:
                                    print(i)
                                    self.ui.listWidget_16.addItem(str(i))
                                print("Timeout List: ")
                                self.ui.listWidget_16.addItem("Timeout Mutants List: ")
                                for i in execution_timeout_list:
                                    print(i)
                                    self.ui.listWidget_16.addItem(str(i))

                                print("\n")
                                print(
                                    "#             Outputs of Killed Mutants              #"
                                )

                                for i in range(killed_mutant_list_size):
                                    print("\n")

                                    print(killed_mutants_list[i])
                                    self.ui.listWidget_19.addItem(
                                        str(killed_mutants_list[i])
                                    )

                                    error_output = error_code_list[i]
                                    error_output_split = error_output.split("\n")
                                    print(error_output_split[-1])
                                    self.ui.listWidget_19.addItem(
                                        str(error_output_split[-1])
                                    )
                                print("\n")

                                if self.ui.checkBox_7.isChecked() is True:
                                    for created_file in all_created_files:
                                        os.remove(created_file)
                                self.ui.label_10.setText(
                                    "Mutation Score: %" + str(mutation_score)
                                )

                                fault_name_list_size = len(FAULT_NAME_LIST)
                                for i in range(0, fault_name_list_size):
                                    added_line_mutants_faults = (
                                        "Mutant_no_"
                                        + str(i + 1)
                                        + "_"
                                        + file_name_for_creating_mutant_file
                                        + " --> "
                                        + str(FAULT_NAME_LIST[i])
                                    )
                                    self.ui.listWidget_14.addItem(
                                        added_line_mutants_faults
                                    )
                            else:
                                killed_counter = 0
                                survived_counter = 0

                                fiplan_directory = self.ui.listWidget_6.item(0).text()
                                with open(
                                    fiplan_directory, encoding="utf-8"
                                ) as json_file:
                                    fault_list = json.load(json_file)

                                for i in range(len(fault_list)):
                                    directory = fault_list[i]["Fault"]["File_Directory"]

                                    split_directory = directory.split("/")
                                    folder_name = split_directory[-3]

                                    ros_exe_file_name = fault_list[i]["Fault"][
                                        "Exe_File"
                                    ]

                                    with open(
                                        directory, mode="r", encoding="utf-8"
                                    ) as file:
                                        python_file_content = file.read()

                                    source_code = fault_list[i]["Fault"]["Source_Code"]
                                    mutant_code = fault_list[i]["Fault"]["Mutate_Code"]

                                    mutation_process = python_file_content.replace(
                                        source_code, mutant_code
                                    )

                                    with open(
                                        directory, mode="w", encoding="utf-8"
                                    ) as file:
                                        file.write(mutation_process)
                                    print("Mutant:", (str(i)))

                                    try:
                                        status_output = subprocess.Popen(
                                            [
                                                "roslaunch",
                                                folder_name,
                                                ros_exe_file_name,
                                            ]
                                        )
                                        status_output.wait(timeout=60)
                                    except subprocess.TimeoutExpired:
                                        status_output.terminate()
                                        survived_counter += 1
                                        print("#       Survived Mutant        #")
                                        print("\n\n")

                                    else:
                                        status_output.terminate()
                                        killed_counter += 1
                                        print("#     Killed Mutant            #")
                                        print("\n\n")

                                    with open(
                                        directory, mode="w", encoding="utf-8"
                                    ) as file:
                                        file.write(python_file_content)

                                print("\n\n")
                                print("#           Results            #")
                                print("\n\n")
                                print("Total Killed Mutant(s):", killed_counter)
                                print("Total Survived Mutant(s):", survived_counter)
                                print(
                                    "\nMutation Score:",
                                    (
                                        killed_counter
                                        / (killed_counter + survived_counter)
                                    )
                                    * 100,
                                )
                                print("\n\n")

        def metric_info_selection():
            try:
                clicked_item_text = self.ui.listWidget_23.currentItem().text()

                with open("metric_list.json", encoding="utf-8") as file:
                    fault_list = json.load(file)

                metric_list_size = self.ui.listWidget_23.count()

                for i in range(0, metric_list_size):
                    metric_name = fault_list["Metrics"][i]["Metric"]["Name"]

                    if clicked_item_text == metric_name:
                        metric_information = fault_list["Metrics"][i]["Metric"]["Info"]
                        self.ui.plainTextEdit_21.setPlainText(metric_information)
            except:
                IndexError()

        def metric_from_list_selection():
            selected_metric = self.ui.listWidget_23.currentItem().text()
            self.ui.listWidget_24.addItem(selected_metric)

        def show_message(message_box_type, message_box_text, message_box_title):
            message_box = QMessageBox()
            if message_box_type == "Critical":
                message_box.setIcon(QMessageBox.Critical)
            if message_box_type == "Ok":
                message_box.setIcon(QMessageBox.Ok)
            if message_box_type == "Critical":
                message_box.setIcon(QMessageBox.Critical)
            message_box.setText(message_box_text)
            message_box.setWindowTitle(message_box_title)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

        def fi_plan_selection():
            clicked_item_text = self.ui.listWidget_6.currentItem().text()
            self.ui.plainTextEdit_23.setPlainText(clicked_item_text)

        # LIST'S (listWidget's) CLICK CONNECTS
        # Line Selection For Mutation on FI Plan Page
        self.ui.listWidget.itemClicked.connect(possible_mutation_line_selection)

        # Line Selection and Show Information About Fault on FI Plan Page
        self.ui.listWidget_3.itemDoubleClicked.connect(fault_selection_from_library)
        self.ui.listWidget_3.itemClicked.connect(show_fault_info_with_one_click)
        
        # Code Snippet Selection on Start Page
        self.ui.code_snippet_list.itemDoubleClicked.connect(code_snippet_selection)
        self.ui.code_snippet_list.itemClicked.connect(
            code_snippet_select_with_one_clicked
        )
        # DNN Code Snippet Selection on Start Page
        self.ui.dnn_code_snippet_list.itemDoubleClicked.connect(dnn_code_snippet_selection)
        self.ui.listWidget_mutate_list.itemDoubleClicked.connect(dnn_mutate_parameter_selection)
        self.ui.listWidget_selected_mutate_parameters.itemDoubleClicked.connect(dnn_mutate_parameter_unselection)
        self.ui.dnn_code_snippet_list.itemClicked.connect(
            dnn_code_snippet_select_with_one_clicked
        )
         #GÖKHAN
        
        # Select Task and Show Task's Details on Workload Page
        self.ui.listWidget_21.itemClicked.connect(task_info_with_one_click)
        self.ui.listWidget_21.itemDoubleClicked.connect(task_selection)

        # Select Metric
        self.ui.listWidget_23.itemClicked.connect(metric_info_selection)
        self.ui.listWidget_23.itemDoubleClicked.connect(metric_from_list_selection)

        # Select FI Plan from
        self.ui.listWidget_6.itemClicked.connect(fi_plan_selection)

        # BUTTONS CLICK CONNECTS
        # LEFT MENU BUTTON CONNECTS
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_start.clicked.connect(self.buttonClick)
        self.ui.btn_scan.clicked.connect(self.buttonClick)
        self.ui.btn_fiplan.clicked.connect(self.buttonClick)
        self.ui.btn_execution.clicked.connect(self.left_menu_execution_page)
        self.ui.btn_monitoring.clicked.connect(self.buttonClick)
        self.ui.open_ros_page.clicked.connect(self.buttonClick)
        self.ui.btn_dnn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(10))# GÖKHAN
        
        
        
        # GO TO BUTTON CONNECTS
        self.ui.btn_go_start.clicked.connect(self.go_to_start_page)
        self.ui.btn_go_scan.clicked.connect(self.buttonClick)
        self.ui.btn_go_fiplan.clicked.connect(self.buttonClick)
        self.ui.btn_go_exe.clicked.connect(self.buttonClick)
        self.ui.btn_go_monitoring.clicked.connect(self.buttonClick)
        self.ui.btn_new_one.clicked.connect(self.buttonClick)
        self.ui.back_start_page.clicked.connect(self.buttonClick)
        self.ui.go_execution.clicked.connect(self.buttonClick)

        # START PAGE BUTTON CONNECTS
        self.ui.btn_open_folder.clicked.connect(get_file_py_for_source_code)
        self.ui.btn_load_dnn.clicked.connect(get_dnn_file_py_for_source_code)
        self.ui.btn_select_workload.clicked.connect(workload_get_file_json)
        self.ui.btn_create_workload.clicked.connect(self.buttonClick)
        self.ui.checkBox_5.clicked.connect(self.buttonClick)
        self.ui.btn_clear_codes.clicked.connect(self.buttonClick)
        self.ui.btn_clear_workload.clicked.connect(self.buttonClick)
        self.ui.btn_add_custom.clicked.connect(self.buttonClick)
        self.ui.checkBox_8.clicked.connect(edit_source_code)
        self.ui.checkBox_5.clicked.connect(edit_workload)
        self.ui.pushButton_10.clicked.connect(self.buttonClick)
        
        

        # CODE SNIPPET BUTTON CONNECTS
        self.ui.btn_create_code.clicked.connect(self.buttonClick)
        self.ui.btn_select_snippet.clicked.connect(code_snippet_selection)
        self.ui.btn_remove_snip.clicked.connect(self.buttonClick)

        # ROS PAGE BUTTON CONNECTS
        self.ui.rosrun_btn.clicked.connect(self.rospy_run)
        self.ui.add_order_btn.clicked.connect(self.buttonClick)
        self.ui.select_trgt_btn.clicked.connect(self.buttonClick)
        self.ui.scan_ros_btn.clicked.connect(self.buttonClick)
        self.ui.mutate_ros_btn.clicked.connect(self.buttonClick)
        self.ui.remove_order_btn.clicked.connect(self.buttonClick)
        self.ui.add_ros_btn.clicked.connect(self.buttonClick)
        self.ui.remove_ros_btn.clicked.connect(self.buttonClick)
        self.ui.remove_ros_mutant.clicked.connect(self.buttonClick)
        self.ui.ros_slct_fiplan.clicked.connect(self.buttonClick)
        self.ui.ros_fiplan_save.clicked.connect(self.buttonClick)
        self.ui.ros_fiplan_remove.clicked.connect(self.buttonClick)
        self.ui.open_target_ros.clicked.connect(self.buttonClick)

        # SCAN PAGE BUTTON CONNECTS
        self.ui.btn_back_code.clicked.connect(self.buttonClick)
        self.ui.btn_scan_process.clicked.connect(self.start_scan_process)
        
        #DNN SCAN
        self.ui.pushButton_dnn_scan.clicked.connect(self.dnn_start_scan_process)
        self.ui.pushButton_dnn_mutate.clicked.connect(self.dnn_start_mutate_process)
        
        # FI PLAN PAGE BUTTONS
        self.ui.btn_random_fault.clicked.connect(random_hata_bas)
        self.ui.btn_slct_fiplan.clicked.connect(fiplan_get_file_json)
        self.ui.btn_create_custom.clicked.connect(self.buttonClick)
        self.ui.btn_select_fault.clicked.connect(fault_selection_from_library)
        self.ui.btn_remove_fault.clicked.connect(self.buttonClick)
        self.ui.btn_start_mutation.clicked.connect(start_mutation)
        self.ui.btn_save_fiplan.clicked.connect(self.buttonClick)
        self.ui.btn_remove_fiplan.clicked.connect(self.buttonClick)

        # EXECUTION PAGE BUTTONS
        self.ui.btn_new_exe.clicked.connect(self.development_process_info)
        self.ui.btn_remove_exe.clicked.connect(self.development_process_info)
        self.ui.btn_select_metrics.clicked.connect(metric_from_list_selection)
        self.ui.btn_start_exe.clicked.connect(execution_module_function)
        self.ui.pushButton_16.clicked.connect(self.buttonClick)
        self.ui.pushButton_3.clicked.connect(save_execution_plan)
        self.ui.btn_export_fiplan.clicked.connect(self.buttonClick)
        self.ui.btn_remove_fi.clicked.connect(self.buttonClick)
        self.ui.btn_create_mutants.clicked.connect(self.development_process_info)

        # DOCKER SETTINGS BUTTONS
        self.ui.btn_create_container.clicked.connect(
            self.development_process_info
        )
        self.ui.btn_show_di.clicked.connect(self.development_process_info)
        self.ui.btn_show_con.clicked.connect(self.development_process_info)
        self.ui.btn_apply_docker.clicked.connect(self.development_process_info)

        # MONITORING PAGE BUTTONS
        self.ui.btn_create_report.clicked.connect(self.create_v_and_v_report)
        self.ui.bar_chart.clicked.connect(self.show_bar_chart)
        self.ui.pie_chart.clicked.connect(self.show_pie_chart)

        # CREATE WORKLOAD PAGE BUTTONS
        self.ui.btn_changeDir.clicked.connect(self.buttonClick)
        self.ui.btn_workload_save.clicked.connect(self.buttonClick)
        self.ui.btn_take_tasks.clicked.connect(self.buttonClick)
        self.ui.btn_select_task.clicked.connect(self.buttonClick)
        self.ui.btn_remove_task.clicked.connect(self.buttonClick)
        self.ui.btn_save_task.clicked.connect(self.buttonClick)
        self.ui.btn_back_start.clicked.connect(self.buttonClick)

        # CREATE CUSTOM SNIPPET PAGE BUTTONS
        self.ui.btn_create_snip.clicked.connect(self.buttonClick)
        self.ui.btn_save_snip.clicked.connect(self.buttonClick)
        self.ui.back_snip.clicked.connect(self.buttonClick)
        self.ui.btn_delete_snip.clicked.connect(self.buttonClick)

        # CREATE CUSTOM FAULT PAGE
        self.ui.btn_back_fi.clicked.connect(self.buttonClick)
        self.ui.btn_save_fault.clicked.connect(self.buttonClick)
        self.ui.btn_create_fault.clicked.connect(self.buttonClick)
        self.ui.btn_delete_fault.clicked.connect(self.buttonClick)
        self.ui.btn_remove_createdFault.clicked.connect(self.buttonClick)

        # SHOW APP
        self.show()

        # SET HOME PAGE AND SELECT MENU
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(
            UIFunctions.selectMenu(self.ui.btn_home.styleSheet())
        )
                # REFRESH AND RESET BUTTONS
        self.ui.refresh_page.clicked.connect(self.refresh_page)
        self.ui.reset_for_all.clicked.connect(self.reset_all)

    #def install_tensorflow_library(self):
        #try:
            # Tensorflow kütüphanesini içe aktar, eğer yüklü değilse ImportError alırız
           #importlib.import_module('tensorflow')
        
        #except ImportError:
            # Tensorflow yüklü değilse yüklemeye çalış
            #try:
                #import pip
                #pip.main(['install', 'tensorflow'])
            #except Exception as e:
                #print("Tensorflow yüklenirken bir hata oluştu:", e)
        #if 'tensorflow' in sys.modules:
            #from tensorflow.keras.datasets import mnist
            #from tensorflow.keras.models import Sequential
            #from tensorflow.keras.layers import Dense, Flatten
            #from tensorflow.keras.optimizers import Adam
        #else:
            #print("TensorFlow yüklü değil. Lütfen yükleyin veya uygun bir yolla içe aktarın.")
        #print("Tensorflow Yükleme Butonuna Basıldı")
    # TensorFlow ile çalışmaya başlayabilirsiniz

# Şimdi Tensorflow kütüphanesinin yüklü olduğundan emin olabiliriz

    def dnn_start_mutate_process(self):
        self.dnn_mutation_process_progress_bar()

        # Get the selected items from the list widget as a list
        selected_items = []

        for i in range(self.ui.listWidget_selected_mutate_parameters.count()):
            item = self.ui.listWidget_selected_mutate_parameters.item(i)
            selected_items.append(item.text())
            print(selected_items[i])

        # Check if there are selected items
        if not selected_items:
            return  # No selected items, exit the function

        # Initialize a variable to store the mutated code
        mutated_code =""
        mutated_line =""
        # Get the initial source code
        source_code = self.ui.plainTextEdit_53.toPlainText()

        # Iterate through the selected items
        for item in selected_items:
            mutate_selected_parameters = item

            if mutate_selected_parameters == "epochs":
                change_parameter_with = 180
                mutated_line = mutator.modify_code_in_file_epoch(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "activation":
                change_parameter_with = "mutated--"
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "optimizer":
                change_parameter_with = "mutated--"
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "batch_size":
                change_parameter_with = 64
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "dropout_rate":
                change_parameter_with = 0.2
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "regularization":
                change_parameter_with = "l2"
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "loss":
                change_parameter_with = "mae"
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "learning_rate":
                change_parameter_with = "0.001"
                mutated_line = mutator.modify_code_in_file_activation(source_code, mutate_selected_parameters, change_parameter_with)
            elif mutate_selected_parameters == "Conv2D":
                change_parameter_with = "layers.Conv2D(256), (2, 2))"
                mutated_line = mutator.modify_code_in_file_Conv2D(source_code, change_parameter_with)
            elif mutate_selected_parameters == "MaxPooling2D":
                change_parameter_with = "layers.MaxPooling2D((6, 6))"
                mutated_line = mutator.modify_code_in_file_MaxPooling2D(source_code, change_parameter_with)
            elif mutate_selected_parameters == "input_shape":
                change_parameter_with = "input_shape=(64, 64, 3)"
                mutated_line = mutator.modify_code_in_file_MaxPooling2D(source_code, change_parameter_with)
            elif mutate_selected_parameters == "AbstractRNNCell":
                change_parameter_with = "AbstractRNNCell()"
                layer_name="AbstractRNNCell"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "Activation":
                change_parameter_with = "Activation()"
                layer_name="Activation"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "ActivityRegularization":
                change_parameter_with = "ActivityRegularization()"
                layer_name="ActivityRegularization"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "AlphaDropout":
                change_parameter_with = "AlphaDropout()"
                layer_name="AlphaDropout"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "Average":
                change_parameter_with = "Average()"
                layer_name="Average"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "AveragePooling1D":
                change_parameter_with = "AveragePooling1D()"
                layer_name="AveragePooling1D"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)                              
            elif mutate_selected_parameters == "AveragePooling2D":
                change_parameter_with = "AveragePooling2D()"
                layer_name="AveragePooling2D"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
            elif mutate_selected_parameters == "AveragePooling3D":
                change_parameter_with = "AveragePooling3D()"
                layer_name="AveragePooling3D"
                mutated_line = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)                
            # Modify the code using mutator and append it to mutated_code
            
            mutated_code += mutated_line + "\n"


        # Set the mutated code in the plain text edit
        self.ui.plainTextEdit_mutated_code.setPlainText(mutated_code)

            #try:
                # Mutasyona uğratılan kodu çalıştır ve sonucu yakala
                
                #exec(mutated_code)
                
            #except Exception as e:
                    #print("Kod çalıştırılırken bir hata oluştu:", e)
        

   
    def refresh_page(self):
        user_decision_to_refresh = self.refresh_page_decision_box()
        
        if user_decision_to_refresh is False:
            return None

        page_index = self.ui.stackedWidget.currentIndex()
        if page_index == 1:  # Start Page
            self.refresh_start_page()
        elif page_index == 2:  # ROS Page
            self.refresh_ros_page()
        elif page_index == 3:  # Scan Page
            self.refresh_scan_page()
        elif page_index == 4:  # FI Plan Page
            self.refresh_fiplan_page()
        elif page_index == 5:  # Execution Page
            self.refresh_execution_page()
        elif page_index == 6:  # Monitoring Page
            self.refresh_monitoring_page()
        elif page_index == 7:  # Custom Fault Page
            self.refresh_custom_fault_page()
        elif page_index == 8:  # Workload Creation Page
            self.refresh_create_workload_page()
        elif page_index == 9:  # Code Snippet Creation Page
            self.refresh_create_code_snippet_page()
        elif page_index == 10:  # Code Snippet Creation Page
            self.refresh_dnn_mutation_page()
        else:
            self.non_refreshed_page()

    def refresh_page_decision_box(self):
        reply = QMessageBox.question(
            self,
            "Refresh",
            "Are you sure you want to refresh?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            return True
        return False

    def non_refreshed_page(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText("Refreshed!")
        message_box.setWindowTitle("Refreshed!")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()

    def refresh_start_page(self):
        self.ui.plainTextEdit_11.clear()
        self.ui.plainTextEdit_12.clear()
        self.ui.plainTextEdit_10.clear()
        self.ui.plainTextEdit_9.clear()
        self.ui.plainTextEdit_13.clear()
        self.ui.plainTextEdit_14.clear()
        self.ui.plainTextEdit_15.clear()
        self.ui.listWidget_8.clear()

    def refresh_ros_page(self):
        self.ui.plainTextEdit_32.clear()
        self.ui.label_86.clear()
        self.ui.plainTextEdit_33.clear()
        self.ui.listWidget_10.clear()
        self.ui.treeView.reset()
        self.ui.listWidget_26.clear()
        self.ui.listWidget_27.clear()
        self.ui.listWidget_28.clear()
        self.ui.listWidget_29.clear()
        self.ui.listWidget_30.clear()
        self.ui.listWidget_33.clear()
        self.ui.listWidget_35.clear()
        self.ui.listWidget_31.clear()
        self.ui.listWidget_26.clear()
        self.ui.listWidget_31.clear()
        self.ui.plainTextEdit_34.clear()
        self.ui.listWidget_36.clear()

    def refresh_scan_page(self):
        self.ui.plainTextEdit_16.clear()
        self.ui.plainTextEdit_17.clear()
        self.ui.listWidget_17.clear()
        self.ui.listWidget_2.clear()
        self.ui.progressBar_2.setValue(0)

    def refresh_fiplan_page(self):
        self.ui.plainTextEdit_18.clear()
        self.ui.plainTextEdit_19.clear()
        self.ui.listWidget.clear()
        self.ui.listWidget_7.clear()
        self.ui.listWidget_4.clear()
        self.ui.label_17.clear()
        self.ui.plainTextEdit_20.clear()
        self.ui.listWidget_11.clear()
        self.ui.listWidget_7.setEnabled(True)

    def refresh_execution_page(self):
        self.ui.listWidget_6.clear()
        self.ui.plainTextEdit_22.clear()
        self.ui.plainTextEdit_25.setPlainText("1")
        self.ui.plainTextEdit_23.clear()
        self.ui.listWidget_13.clear()

    def refresh_monitoring_page(self):
        self.ui.listWidget_16.clear()
        self.ui.listWidget_19.clear()
        self.ui.listWidget_14.clear()
        self.ui.label_47.clear()
        self.ui.listWidget_9.clear()
        self.ui.label_10.setText("Mutation Score")

    def refresh_custom_fault_page(self):
        self.ui.plainTextEdit_40.clear()
        self.ui.plainTextEdit_41.clear()
        self.ui.plainTextEdit_42.clear()
        self.ui.plainTextEdit_43.clear()
        self.ui.plainTextEdit_45.clear()
        self.ui.listWidget_5.clear()
        self.ui.plainTextEdit_44.clear()

    def refresh_create_workload_page(self):
        self.ui.plainTextEdit_35.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.listWidget_21.clear()
        self.ui.listWidget_22.clear()
        self.ui.plainTextEdit_37.clear()
        self.ui.label_4.setText("NOT SAVE!")
        self.ui.plainTextEdit_38.clear()

    def refresh_create_code_snippet_page(self):
        self.ui.plainTextEdit_47.clear()
        self.ui.plainTextEdit_48.clear()
        self.ui.plainTextEdit_50.clear()
        self.ui.plainTextEdit_49.clear()
        self.ui.plainTextEdit_51.clear()
        self.ui.plainTextEdit_52.clear()
        self.ui.checkBox_6.setChecked(False)
    def refresh_dnn_mutation_page(self):
        self.ui.listWidget_selected_mutate_parameters.clear()
        self.ui.plainTextEdit_53.clear()
        self.ui.plainTextEdit_mutated_code.clear()
        self.ui.listWidget_selected_mutate_parameters.clear()
        self.ui.dnn_selected_snippet.clear()

    def reset_all(self):
        reset_decision = self.reset_all_decision_box()
        if reset_decision is False:
            return None

        # RESET PAGES
        self.refresh_start_page()
        self.refresh_ros_page()
        self.refresh_scan_page()
        self.refresh_fiplan_page()
        self.refresh_execution_page()
        self.refresh_monitoring_page()
        self.refresh_custom_fault_page()
        self.refresh_create_workload_page()
        self.refresh_create_code_snippet_page()
        self.refresh_dnn_mutation_page()
        # RESET VARIABLES
        self.reset_variables()

        information_title = "Completed!"
        information_text = "Reset process is done!"
        self.show_information_box(information_title, information_text)

    def reset_all_decision_box(self):
        reply = QMessageBox.question(
            self,
            "Reset!",
            "Are you sure you want to reset all?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            return True
        return False

    def reset_variables(self):
        global RUN_ORDER_LIST_JUST_PATH
        RUN_ORDER_LIST_JUST_PATH = []

        global ROS_SOURCE_CODE
        ROS_SOURCE_CODE = ""

        global POSSIBLE_MUTANT_LIST
        POSSIBLE_MUTANT_LIST = []

        global ZIPPED_LIST
        ZIPPED_LIST = []

        global ZIPPED_ROS_LIST
        ZIPPED_ROS_LIST = []

        global ROS_SOURCE_MUTANT
        ROS_SOURCE_MUTANT = []

        global SOURCE_AND_MUTANT_CODE
        SOURCE_AND_MUTANT_CODE = []

        global FAULT_NAME_LIST
        FAULT_NAME_LIST = []

        global FIPLAN_DIRECTORY_LIST
        FIPLAN_DIRECTORY_LIST = []

    def show_information_box(self, information_title, information_text):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(information_text)
        message_box.setWindowTitle(information_title)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()

    def left_menu_execution_page(self):
        """Go to execution page from left menu"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.execution)
        UIFunctions.resetStyle(self, self.ui.btn_execution)
        self.sender().setStyleSheet(UIFunctions.selectMenu(self.sender().styleSheet()))
        self.ui.titleRightInfo.setText("EXECUTION")

    def go_to_start_page(self):
        """Go to start page button"""

        self.ui.stackedWidget.setCurrentWidget(self.ui.start)
        UIFunctions.resetStyle(self, self.ui.btn_home.styleSheet())
        self.ui.btn_start.setStyleSheet(
            UIFunctions.selectMenu(self.ui.btn_start.styleSheet())
        )
        self.ui.titleRightInfo.setText("START")

    # Splits source code to scan line by line
    def take_split_source_code(self):
        """The function provides the splitted code to scan line by line"""
        pure_source_code_content = self.ui.plainTextEdit_16.toPlainText()
        split_text = pure_source_code_content.split("\n")
        self.ui.listWidget_2.addItems(split_text)

        return split_text
    #Gökhan-------------------------------------------------------------------start
       # Splits source code to scan line by line
    def dnn_take_split_source_code(self):
        """The function provides the splitted code to scan line by line"""
        pure_source_code_content = self.ui.plainTextEdit_53.toPlainText()
        split_text = pure_source_code_content.split("\n")
        self.ui.listWidget_dnn_selected_snippet.addItems(split_text)

        return split_text
    #Gökhan-------------------------------------------------------------------end
    # Scan Process Main Function
    def start_scan_process(self):
        """The function decides which scan process path to use"""
        check_detected_parts_list = self.ui.listWidget_2.count()

        if check_detected_parts_list:
            self.ui.listWidget_2.clear()

        scan_page_source_code_check = self.ui.plainTextEdit_16.toPlainText()

        if scan_page_source_code_check:
            is_empty_workload = len(self.ui.plainTextEdit_17.toPlainText())
            selected_code_snippet_length = self.ui.listWidget_17.count()

            if is_empty_workload == 0 and selected_code_snippet_length == 0:
                self.start_no_workload_no_code_snippet_process()
            elif is_empty_workload > 0 and selected_code_snippet_length == 0:
                self.start_yes_workload_no_code_snippet_process()
            elif is_empty_workload == 0 and selected_code_snippet_length > 0:
                self.start_no_workload_yes_code_snippet_process()
            else:
                self.start_yes_workload_yes_code_snippet_process()
    
    #GÖKHAN---------------------------------------------------------------------------start
    def dnn_start_scan_process(self):
        """The function decides which scan process path to use"""
        check_detected_parts_list = self.ui.listWidget_dnn_selected_snippet.count()

        if check_detected_parts_list:
            self.ui.listWidget_dnn_selected_snippet.clear()
        self.ui.listWidget_dnn_selected_snippet.clear()
        scan_page_source_code_check = self.ui.plainTextEdit_53.toPlainText()

        if scan_page_source_code_check:
            
            selected_code_snippet_length = self.ui.dnn_selected_snippet.count()


            if  selected_code_snippet_length > 0:
                self.dnn_start_no_workload_yes_code_snippet_process()
            else:
                print("eror")
                
    #GÖKHAN---------------------------------------------------------------------------end
    
    
    # Function starts "Yes Workload, Yes Code Snipet" Scan Process
    def start_yes_workload_yes_code_snippet_process(self):
        """Function manages yes workload, yes code snippet scan process"""
        detected_part_list_size = self.ui.listWidget_2.count()
        selected_code_snippet_length = self.ui.listWidget_17.count()
        code_snippet_regex_code = scan_process.open_code_snip()
        workload_text = self.ui.plainTextEdit_17.toPlainText()
        workload_data = json.loads(workload_text)
        workload_function_name_list = scan_process.take_workload_name_list(
            workload_data
        )
        split_text = self.take_split_source_code()
        painted_lines = scan_process.workload_lines(
            split_text, workload_function_name_list
        )
        (
            added_snippet_regex_length,
            code_snippet_data_list,
        ) = self.find_selected_code_snippet(
            selected_code_snippet_length, code_snippet_regex_code
        )
        patterns = scan_process.find_patterns_yes_wl_yes_cs(
            added_snippet_regex_length, code_snippet_data_list
        )
        source_code_list = self.take_source_code()
        (
            faultable_line_list,
            faultable_line_number_list,
        ) = scan_process.scan_yes_wl_yes_cs(patterns, source_code_list, painted_lines)

        self.scan_process_progress_bar()
        self.paint_workload_lines(painted_lines)
        self.paint_sky_blue(faultable_line_number_list)
        self.add_fi_plan(faultable_line_list)

    # Progress bar on scan page
    def scan_process_progress_bar(self):
        """Progress Bar"""
        for i in range(100):
            time.sleep(0.01)
            self.ui.progressBar_2.setValue(i + 1)

    # Progress bar on fi plan page
    def mutation_process_progress_bar(self):
        """Progress Bar"""
        for i in range(100):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i + 1)
    def dnn_mutation_process_progress_bar(self):
        """Progress Bar"""
        for i in range(100):
            time.sleep(0.01)
            self.ui.progressBar_Mutation.setValue(i + 1)

    # Function takes source code to use on IM-FIT
    def take_source_code(self):
        """Take Source Code from UI"""
        source_code_list = []
        source_code = self.ui.plainTextEdit_16.toPlainText()
        source_code_list = source_code.split("\n")

        return source_code_list

    # Function paints workload covered and
    # selected code snippets lines to show to the user on UI
    def paint_sky_blue(self, faultable_line_number_list):
        """In "Yes Workload, Yes Workload" Process,
        this function paints the detected parts of code as sky blue"""
        for i in faultable_line_number_list:
            self.ui.listWidget_2.item(i).setBackground(
                QtGui.QColor(0, 128, 255)
            )  # Colored as sky blue
    #GÖKHAN-----------------------------------------------------------------START
       # selected code snippets lines to show to the user on UI
    def dnn_paint_sky_blue(self, faultable_line_number_list):
        """In "Yes Workload, Yes Workload" Process,
        this function paints the detected parts of code as sky blue"""
        for i in faultable_line_number_list:
            self.ui.listWidget_dnn_selected_snippet.item(i).setBackground(
                QtGui.QColor(0, 128, 255)
            )  # Colored as sky blue
    #GÖKHAN-----------------------------------------------------------------END

    # Function paints workload covered lines to show to the user on UI
    def paint_workload_lines(self, painted_lines):
        """In "Yes Workload, Yes Workload" Process,
        this function paints the detected parts of workload as purple"""
        for number in painted_lines:
            self.ui.listWidget_2.item(number).setBackground(
                QtGui.QColor(102, 0, 102)
            )  # Colored as purple

    # Function finds selected code snippets by the user in source code
    def find_selected_code_snippet(
        self, selected_code_snippet_length, code_snippet_regex_code
    ):
        """Selected code snippets by the user are finded by IM-FIT"""
        code_snippet_data_list = []
        for i in range(selected_code_snippet_length):
            code_snippet_data = self.ui.listWidget_17.item(i).text()
            code_snippet_data_list.append(code_snippet_data)
            added_snippet_regex_length = len(code_snippet_regex_code["code_snippets"])
        return added_snippet_regex_length, code_snippet_data_list

    # Function adds the faultable lines to FI Plan page
    def add_fi_plan(self, faultable_line_list):
        """Detected fault applicable lines
        add to FI Plan page to apply mutation testing"""
        for painted_line in faultable_line_list:
            strip_painted_line = painted_line.strip()
            self.ui.listWidget.addItem(strip_painted_line)

    # Function starts "No Workload, No Code Snipet" Scan Process
    def start_no_workload_no_code_snippet_process(self):
        """Function manages no workload, no code snippet scan process"""
        code_snippet_regex_code_list = scan_process.take_code_snippet_regex_code_list()
        source_code_list = self.take_source_code()
        (
            faultable_line_number_list,
            faultable_line_list,
        ) = scan_process.no_wl_no_cs_find_target_line(
            source_code_list, code_snippet_regex_code_list
        )
        self.take_split_source_code()
        self.scan_process_progress_bar()
        self.paint_sky_blue(faultable_line_number_list)
        self.add_fi_plan(faultable_line_list)

    # Function starts "Yes Workload, No Code Snippet" Scan Process
    def start_yes_workload_no_code_snippet_process(self):
        """Function manages yes workload, no code snippet scan process"""
        split_text = self.take_split_source_code()
        workload_text = self.ui.plainTextEdit_17.toPlainText()
        workload_data = json.loads(workload_text)
        workload_function_name_list = scan_process.take_workload_name_list(
            workload_data
        )
        painted_lines = scan_process.workload_lines(
            split_text, workload_function_name_list
        )
        patterns = scan_process.take_code_snippet_regex_code_list()
        (
            faultable_line_list,
            faultable_line_number_list,
        ) = scan_process.yes_workload_no_snippet_target_line(
            patterns, painted_lines, split_text
        )
        self.scan_process_progress_bar()
        self.paint_workload_lines(painted_lines)
        self.paint_sky_blue(faultable_line_number_list)
        self.add_fi_plan(faultable_line_list)

    # Method takes code snippet for "No Workload, Yes Code Snippet" Scan Process
    def take_code_snippet_no_workload_yes_code_snippet(self):
        """Code snippets are taken by IM-FIT to use on no workload yes code snippet scan process"""
        selected_code_snippet_length = self.ui.listWidget_17.count()
        code_snippet_data_list = []
        for line_number in range(selected_code_snippet_length):
            line_from_code_snippet_list = self.ui.listWidget_17.item(line_number).text()
            code_snippet_data_list.append(line_from_code_snippet_list)
        return code_snippet_data_list
#Gökhan------------------------------------------------------------------------------------------------------start
  # Method takes code snippet for "No Workload, Yes Code Snippet" Scan Process
    def dnn_take_code_snippet_no_workload_yes_code_snippet(self):
        """Code snippets are taken by IM-FIT to use on no workload yes code snippet scan process"""
        selected_code_snippet_length = self.ui.dnn_selected_snippet.count()
        code_snippet_data_list = []
        for line_number in range(selected_code_snippet_length):
            line_from_code_snippet_list = self.ui.dnn_selected_snippet.item(line_number).text()
            code_snippet_data_list.append(line_from_code_snippet_list)
        return code_snippet_data_list
#Gökhan------------------------------------------------------------------------------------------------------end
    
    
    # Method start "No Workload, Yes Code Snippet" Scan Process
    def start_no_workload_yes_code_snippet_process(self): #gökhanbakılacak
        """Method manages no workload yes code snippet scan process"""
        detected_part_list_size = self.ui.listWidget_2.count()
        code_snippet_data_list = self.take_code_snippet_no_workload_yes_code_snippet()
        patterns = scan_process.define_code_snippet_no_workload_yes_code_snippet(
            code_snippet_data_list
        )
        split_text = self.take_split_source_code()
        (
            faultable_line_list,
            faultable_line_number_list,
        ) = scan_process.find_target_no_workload_yes_code_snippet(split_text, patterns)
        self.scan_process_progress_bar()
        self.paint_sky_blue(faultable_line_number_list)
        self.add_fi_plan(faultable_line_list)



#GÖKHAN*-------------------------------------------------------------------------------------------------start
 # Method start "No Workload, Yes Code Snippet" Scan Process
    def dnn_start_no_workload_yes_code_snippet_process(self): #gökhanbakılacak
        """Method manages no workload yes code snippet scan process"""
        detected_part_list_size = self.ui.listWidget_dnn_selected_snippet.count()
        code_snippet_data_list = self.dnn_take_code_snippet_no_workload_yes_code_snippet()
        patterns = scan_process.dnn_define_code_snippet_no_workload_yes_code_snippet(
            code_snippet_data_list
        )
        split_text = self.dnn_take_split_source_code()
        (
            faultable_line_list,
            faultable_line_number_list,
        ) = scan_process.find_target_no_workload_yes_code_snippet(split_text, patterns)
        self.scan_process_progress_bar()
        self.dnn_paint_sky_blue(faultable_line_number_list)
        self.add_fi_plan(faultable_line_list)
#GÖKHAN*-------------------------------------------------------------------------------------------------end
    def monitoring_report_faults_list(self):
        """Method shows the detected faults
        after execution process in fault list on monitoring page"""
        monitoring_faults_list = []
        monitoring_faults_list_size = self.ui.listWidget_14.count()
        for i in range(0, monitoring_faults_list_size):
            line_of_faults_list = self.ui.listWidget_14.item(i).text()
            monitoring_faults_list.append(line_of_faults_list)
        return monitoring_faults_list

    def monitoring_report_killed_mutants_output_list(self):
        """Outputs of detected killed mutants are added
        to the killed mutants output list by IM-FIT on monitoring page"""
        monitoring_killed_mutants_output_list = []
        monitoring_killed_mutants_output_list_size = self.ui.listWidget_19.count()
        for i in range(0, monitoring_killed_mutants_output_list_size):
            line_of_killed_mutants_output_list = self.ui.listWidget_19.item(i).text()
            monitoring_killed_mutants_output_list.append(
                line_of_killed_mutants_output_list
            )
        return monitoring_killed_mutants_output_list

    def monitoring_report_mutant_list(self):
        """Detected mutants are shown to the user by IM-FIT on monitoring page"""
        monitoring_mutant_list = []
        monitoring_mutant_list_size = self.ui.listWidget_16.count()
        for i in range(0, monitoring_mutant_list_size):
            line_of_mutant_list = self.ui.listWidget_16.item(i).text()
            monitoring_mutant_list.append(line_of_mutant_list)
        return monitoring_mutant_list

    def monitoring_report_metric_list(self):
        """Used metrics for the execution process and
        their results are shown to the user in the list on monitoring page"""
        monitoring_metric_list = []
        monitoring_metric_list_size = self.ui.listWidget_9.count()
        for i in range(0, monitoring_metric_list_size):
            line_of_metric_list = self.ui.listWidget_9.item(i).text()
            monitoring_metric_list.append(line_of_metric_list)
        return monitoring_metric_list

    def create_v_and_v_report(self):
        """Method manages creating a V&V report"""
        monitoring_metric_list = self.monitoring_report_metric_list()
        monitroing_mutant_list = self.monitoring_report_mutant_list()
        monitoring_killed_mutants_output_list = (
            self.monitoring_report_killed_mutants_output_list()
        )
        monitoring_faults_list = self.monitoring_report_faults_list()

        monitoring_process.create_new_v_and_v_report(
            monitoring_metric_list,
            monitroing_mutant_list,
            monitoring_killed_mutants_output_list,
            monitoring_faults_list,
        )
        self.ui.label_77.setText("V&V Report is Created")

    # Mutation Score Graphic Types
    # Creating bar chart function
    def create_bar_chart(
        self,
        mutation_score,
        killed_mutant_number,
        survived_mutant_number,
        equvialent_mutant_number,
    ):
        """Creating bar chart graphic"""
        # Create bars
        plt.clf()
        bar_width = 1
        bars1 = [mutation_score]
        bars2 = [killed_mutant_number]
        bars3 = [survived_mutant_number]
        bars4 = [equvialent_mutant_number]
        bars5 = bars1 + bars2 + bars3 + bars4

        # The X position of bars
        bar_1_x_position = [1]
        bar_2_x_position = [2]
        bar_3_x_position = [3]
        bar_4_x_position = [4]
        bar_5_x_position = (
            bar_1_x_position + bar_2_x_position + bar_3_x_position + bar_4_x_position
        )

        # Create barplot
        plt.bar(
            bar_1_x_position,
            bars1,
            width=bar_width,
            color=(0.3, 0.9, 0.2, 0.6),
            label="Mutation Score",
        )
        plt.bar(
            bar_2_x_position,
            bars2,
            width=bar_width,
            color=(0.3, 0.7, 0.4, 0.6),
            label="Killed Mutants",
        )
        plt.bar(
            bar_3_x_position,
            bars3,
            width=bar_width,
            color=(0.3, 0.5, 0.6, 0.6),
            label="Survived Mutants",
        )
        plt.bar(
            bar_4_x_position,
            bars4,
            width=bar_width,
            color=(0.3, 0.3, 0.8, 0.6),
            label="Equivalent Mutants",
        )

        # Create legend
        plt.legend()

        # Text below each barplot
        plt.xticks(
            [r + bar_width for r in range(len(bar_5_x_position))],
            ["Mutation Score", "Killed", "Survived", "Equivalent"],
        )

        # Text on the top of each bar
        for i, _ in enumerate(bar_5_x_position):
            plt.text(
                x=bar_5_x_position[i],
                y=bars5[i] + 0.1,
                s=str(bars5[i]),
                fontdict=dict(fontsize=12),
                ha="center",
            )

        # Graphic title
        plt.title("Details of V&V Process")
        plt.tight_layout()
        plt.savefig("output1.jpg", dpi=70)

    # Creating Pie Chart Function
    def create_pie_chart(
        self, killed_mutant_number, survived_mutant_number, equvialent_mutant_number
    ):
        """Creating pie chart"""
        plt.clf()
        chart = np.array(
            [
                killed_mutant_number,
                survived_mutant_number,
                equvialent_mutant_number,
            ]
        )
        if killed_mutant_number:
            killed_mutant_graph_string = "Killed: " + str(killed_mutant_number)
        else:
            killed_mutant_graph_string = ""

        if survived_mutant_number:
            survived_mutant_graph_string = "Survived: " + str(survived_mutant_number)
        else:
            survived_mutant_graph_string = ""

        if equvialent_mutant_number:
            equvialent_mutant_graph_string = "Equvialent: " + str(
                equvialent_mutant_number
            )
        else:
            equvialent_mutant_graph_string = ""

        mylabels = [
            killed_mutant_graph_string,
            survived_mutant_graph_string,
            equvialent_mutant_graph_string,
        ]
        plt.title("Details of V&V Process")
        plt.pie(chart, labels=mylabels)
        plt.savefig("output2.jpg", dpi=70)

    def show_bar_chart(self):
        self.ui.label_47.setPixmap(QPixmap("output1.jpg"))

    def show_pie_chart(self):
        self.ui.label_47.setPixmap(QPixmap("output2.jpg"))

    def rospy_run(self):
        """main func"""
        global RUN_ORDER_LIST_JUST_PATH

        if RUN_ORDER_LIST_JUST_PATH:
            len_run_order_list_just_path = len(RUN_ORDER_LIST_JUST_PATH)
            roscore_process = subprocess.Popen(["roscore"])
            time.sleep(5)

            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setText("Roscore is ready!")
            message_box.setWindowTitle("Ready!")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

            for i in range(len_run_order_list_just_path):
                if i % 2 == 0:
                    ros_directory = RUN_ORDER_LIST_JUST_PATH[i]
                    split_rospy_file_name = ros_directory.split("/")
                    package_name = split_rospy_file_name[-3]

                else:
                    rospy_file_name = RUN_ORDER_LIST_JUST_PATH[i]
                    if i == 1:
                        target_ros_process = subprocess.Popen(
                            ["rosrun", package_name, rospy_file_name]
                        )
                    else:
                        ros_subprocess = subprocess.Popen(
                            ["rosrun", package_name, rospy_file_name]
                        )
                        try:
                            print("Running in process", target_ros_process.pid)
                            target_ros_process.wait(timeout=5)
                        except subprocess.TimeoutExpired:
                            rosnode_list = subprocess.getoutput("rosnode list")
                            rostopic_list = subprocess.getoutput("rostopic list")
                            rosparam_list = subprocess.getoutput("rosparam list")
                            rosservice_list = subprocess.getoutput("rosservice list")

                            print("Timed out - killing", target_ros_process.pid)
                            target_ros_process.terminate()
                            ros_subprocess.terminate()
                            roscore_process.terminate()
        else:
            roscore_process = subprocess.Popen(["roscore"])
            time.sleep(5)

            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setText("Roscore is ready!")
            message_box.setWindowTitle("Ready!")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

            one_ros_file_directory_text = self.ui.plainTextEdit_33.toPlainText()
            one_ros_file_directory_split = one_ros_file_directory_text.split("/")
            print("File name:", one_ros_file_directory_split[-1])
            print("Package name:", one_ros_file_directory_split[-3])

            rospy_file_name = one_ros_file_directory_split[-1]
            package_name = one_ros_file_directory_split[-3]

            target_ros_process = subprocess.Popen(
                ["rosrun", package_name, rospy_file_name]
            )
            try:
                print("Running in process", target_ros_process.pid)
                target_ros_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                rosnode_list = subprocess.getoutput("rosnode list")
                rostopic_list = subprocess.getoutput("rostopic list")
                rosparam_list = subprocess.getoutput("rosparam list")
                rosservice_list = subprocess.getoutput("rosservice list")

                print("Timed out - killing", target_ros_process.pid)
                target_ros_process.terminate()
                roscore_process.terminate()

        time.sleep(1)
        print("Process Done")

        rosnodes = rosnode_list.split("\n")
        self.ui.listWidget_27.addItems(rosnodes)

        # ROS TOPIC LIST
        rostopics = rostopic_list.split("\n")
        self.ui.listWidget_28.addItems(rostopics)

        # ROS SERVICE LIST
        rosservices = rosservice_list.split("\n")
        self.ui.listWidget_29.addItems(rosservices)

        # ROS PARAMETER LIST
        rosparams = rosparam_list.split("\n")
        self.ui.listWidget_30.addItems(rosparams)

    def development_process_info(self):
        information_text = "System in the development process!"
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(information_text)
        message_box.setWindowTitle("Information")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()

    # BUTTONS CLICK FUNCTIONS
    def buttonClick(self):
        """Button click function"""
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # DNN
        if btnName == "btn_dnn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.btn_dnn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(10)))# GÖKHAN
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("DNN") # GÖKHAN
        # HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("HOME")

        # START PAGE
        if btnName == "btn_start":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("START")

        # SCAN PAGE
        if btnName == "btn_scan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.scan)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("SCAN")

        # CODE SNIPPETS PAGE
        if btnName == "btn_code":
            self.ui.stackedWidget.setCurrentWidget(self.ui.code)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("CODE SNIPPETS")

        # FIPLAN PAGE
        if btnName == "btn_fiplan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.fiplan)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("FAULT INJECTION PLAN")

        # EXECUTION PAGE
        if btnName == "btn_execution":
            self.ui.stackedWidget.setCurrentWidget(self.ui.execution)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("EXECUTION")

        # MONITORING PAGE
        if btnName == "btn_monitoring":
            self.ui.stackedWidget.setCurrentWidget(self.ui.monitoring)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ui.titleRightInfo.setText("MONITORING")

        # PAGE CHANGE BUTTONS
        if btnName == "btn_go_start":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            UIFunctions.resetStyle(self, self.ui.btn_home.styleSheet())
            self.ui.btn_start.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_start.styleSheet())
            )
            self.ui.titleRightInfo.setText("START")

        if btnName == "btn_go_start_2":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            UIFunctions.resetStyle(self, self.ui.btn_home.styleSheet())
            self.ui.btn_start.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_start.styleSheet())
            )
            self.ui.titleRightInfo.setText("START")

        if btnName == "back_start_page":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            self.ui.titleRightInfo.setText("START")

        if btnName == "btn_go_scan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.scan)
            UIFunctions.resetStyle(self, self.ui.btn_start.styleSheet())
            self.ui.btn_scan.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_scan.styleSheet())
            )
            self.ui.titleRightInfo.setText("SCAN")

            if self.ui.checkBox_3.isChecked() is True:
                self.ui.plainTextEdit_16.setPlainText(
                    self.ui.plainTextEdit_9.toPlainText()
                )
                self.ui.plainTextEdit_17.setPlainText(
                    self.ui.plainTextEdit_14.toPlainText()
                )
                check_selected_code_snippet_list = self.ui.listWidget_8.count()

                if check_selected_code_snippet_list:
                    code_snippet_data_list = []
                    for i in range(0, check_selected_code_snippet_list):
                        code_snippet_data = self.ui.listWidget_8.item(i).text()
                        code_snippet_data_list.append(code_snippet_data)

                    self.ui.listWidget_17.addItems(code_snippet_data_list)

            selected_code_snippets = []
            code_snippet_list_size = self.ui.listWidget_8.count()
            if code_snippet_list_size:
                for selected_code_snippet_line_number in range(
                    0, code_snippet_list_size
                ):
                    selected_line_content = self.ui.listWidget_8.item(
                        selected_code_snippet_line_number
                    ).text()
                    selected_code_snippets.append(selected_line_content)
            #GÖKHAN GÖKHAN 
            dnn_selected_code_snippets = []
            dnn_code_snippet_list_size = self.ui.dnn_selected_snippet.count()
            if dnn_code_snippet_list_size:
                for dnn_selected_code_snippet_line_number in range(
                    0, dnn_code_snippet_list_size
                ):
                    dnn_selected_line_content = self.ui.dnn_selected_snippet.item(
                        dnn_selected_code_snippet_line_number
                    ).text()
                    dnn_selected_code_snippets.append(dnn_selected_line_content)
            #GÖKHAN GÖKHAN
        if btnName == "btn_go_fiplan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.fiplan)
            UIFunctions.resetStyle(self, self.ui.btn_scan.styleSheet())
            self.ui.btn_fiplan.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_fiplan.styleSheet())
            )
            self.ui.titleRightInfo.setText("FAULT INJECTION PLAN")

            for original_line in self.code_part_for_mutation:
                if not isinstance(original_line, int):
                    new_line = original_line.lstrip()
                    self.ui.listWidget.addItem(new_line)

            line_number = self.ui.listWidget.count()

            for number in range(0, line_number):
                if number % 2 == 0:
                    self.ui.listWidget.item(number).setBackground(
                        QtGui.QColor(52, 59, 72)
                    )  # Gray backgound
                else:
                    self.ui.listWidget.item(number).setBackground(
                        QtGui.QColor(40, 44, 52)
                    )  # IM-FIT original backgound color

        if btnName == "btn_go_exe":
            self.ui.stackedWidget.setCurrentWidget(self.ui.execution)
            UIFunctions.resetStyle(self, self.ui.btn_fiplan.styleSheet())
            self.ui.btn_execution.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_execution.styleSheet())
            )
            self.ui.titleRightInfo.setText("EXECUTION")

        if btnName == "btn_go_exe_2":
            self.ui.stackedWidget.setCurrentWidget(self.ui.execution)
            UIFunctions.resetStyle(self, self.ui.btn_fiplan.styleSheet())
            self.ui.btn_execution.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_execution.styleSheet())
            )
            self.ui.titleRightInfo.setText("EXECUTION")

        if btnName == "go_execution":
            self.ui.stackedWidget.setCurrentWidget(self.ui.execution)
            UIFunctions.resetStyle(self, self.ui.btn_start.styleSheet())
            self.ui.btn_execution.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_execution.styleSheet())
            )
            self.ui.titleRightInfo.setText("EXECUTION")

        if btnName == "btn_go_monitoring":
            self.ui.stackedWidget.setCurrentWidget(self.ui.monitoring)
            UIFunctions.resetStyle(self, self.ui.btn_execution.styleSheet())
            self.ui.btn_monitoring.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_monitoring.styleSheet())
            )
            self.ui.titleRightInfo.setText("MONITORING")

        if btnName == "btn_new_one":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            UIFunctions.resetStyle(self, self.ui.btn_monitoring.styleSheet())
            self.ui.btn_start.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_start.styleSheet())
            )
            self.ui.titleRightInfo.setText("START")

        # PAGES

        # START PAGE
        if btnName == "open_ros_page":
            self.ui.stackedWidget.setCurrentWidget(self.ui.ros_page)
            self.ui.titleRightInfo.setText("ROS Mutation Module")
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_create_workload":
            self.ui.stackedWidget.setCurrentWidget(self.ui.cWorkload)
            self.ui.leftMenuBg.hide()
            self.ui.toggleButton.show()
            self.ui.titleRightInfo.setText("START - CREATE WORKLOAD")

        if btnName == "btn_add_custom":
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.json"))

            if dialog.exec():
                file_name = dialog.selectedFiles()

                if file_name[0].endswith(".json"):
                    with open(file_name[0], mode="r", encoding="utf-8") as file:
                        data = file.read()
                        self.ui.plainTextEdit_15.setPlainText(data)
                        code_snippets_list_json = json.loads(data)

                        task_name = str(code_snippets_list_json["Snippet_Name"])
                        self.ui.listWidget_8.addItem(task_name)
                        self.ui.code_snippet_list.addItem(task_name)

        if btnName == "btn_clear_codes":
            self.ui.plainTextEdit_9.clear()

        if btnName == "btn_clear_workload":
            self.ui.plainTextEdit_14.clear()

        if btnName == "pushButton_10":
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("*.py *.launch")

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".py") or file_name[0].endswith(".launch"):

                    with open(file_name[0], mode="r", encoding="utf-8") as file:
                        data = file.read()
                        self.ui.plainTextEdit_11.setPlainText(file_name[0])
                        self.ui.plainTextEdit_12.setPlainText(data)
                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText(
                        "Please be sure to selected .py or .launch file!"
                    )
                    message_box.setWindowTitle("Attention!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

        # CREATE WORKLOAD PAGE FROM START PAGE

        if btnName == "btn_changeDir":
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.json"))

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".json"):  # .json file is choosed by the user
                    with open(
                        file_name[0], mode="r", encoding="utf-8"
                    ) as file:  # file_name[0] is directory of file
                        workload_content_data = file.read()
                        self.ui.plainTextEdit_35.setPlainText(
                            str(file_name[0])
                        )  # Source code directory is added to the text
                        self.ui.plainTextEdit.setPlainText(workload_content_data)
                        self.ui.plainTextEdit_2.setPlainText(workload_content_data)

        if btnName == "btn_workload_save":
            dialog = QFileDialog()
            path_name = QFileDialog.getExistingDirectory()
            text = self.ui.plainTextEdit_36.toPlainText() + ".json"
            full_path = os.path.join(path_name, text)
            created_workload_content = self.ui.plainTextEdit_2.toPlainText()

            with open(full_path, mode="w", encoding="utf-8") as file:
                file.write(created_workload_content)

        if btnName == "btn_take_tasks":
            try:
                all_task_list_size = self.ui.listWidget_21.count()
                json_type_task = self.ui.plainTextEdit.toPlainText()
                json_loaded_task = json.loads(json_type_task)

                if all_task_list_size == 0:

                    for i in range(0, len(json_loaded_task["Tasks"])):
                        workload_task = str(
                            json_loaded_task["Tasks"][i]["Task"]["Task_ID"]
                        )
                        split_workload_task = workload_task.split("\n")
                        self.ui.listWidget_21.addItems(split_workload_task)
                else:
                    self.ui.listWidget_21.clear()

                    for i in range(0, len(json_loaded_task["Tasks"])):
                        workload_task = str(
                            json_loaded_task["Tasks"][i]["Task"]["Task_ID"]
                        )
                        split_workload_task = workload_task.split("\n")
                        self.ui.listWidget_21.addItems(split_workload_task)
            except:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                caution_text = """Please Fix Workload!
                This is the example workload template.
                
                "Task":{
                    "Task_ID": DATA,
                    "Tag": DATA TAG,
                    "Process": DATA PROCESS,
                    "Sayilar": {
                        "Sayi1":XX,
                        "Sayi2":XX
                    }
                }"""
                message_box.setText(caution_text)
                message_box.setWindowTitle("Fix Workload!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

        if btnName == "btn_select_task":
            selected_task_from_list = self.ui.listWidget_21.currentItem().text()
            split_selected_task_from_list = selected_task_from_list.split("\n")
            self.ui.listWidget_22.addItems(split_selected_task_from_list)

        if btnName == "btn_save_task":
            all_selected_snippets = ""

            selected_task_list_size = self.ui.listWidget_22.count()

            json_type_task = self.ui.plainTextEdit.toPlainText()
            tasks_list_json = json.loads(json_type_task)

            if selected_task_list_size:
                dialog = QFileDialog()
                path_name = QFileDialog.getExistingDirectory()

                task_name = self.ui.plainTextEdit_37.toPlainText()

                task_path_and_name = os.path.join(path_name, task_name + ".json")

                for i in range(0, len(tasks_list_json["Tasks"])):
                    task_name = str(tasks_list_json["Tasks"][i]["Task"]["Task_ID"])
                    for j in range(0, self.ui.listWidget_22.count()):
                        list_item = self.ui.listWidget_22.item(j).text()
                        if task_name == list_item:
                            task_detail = str(tasks_list_json["Tasks"][i]["Task"])
                            for i in task_detail:
                                all_selected_snippets += i

                with open(task_path_and_name, mode="w", encoding="utf-8") as json_file:
                    json_file.write(all_selected_snippets)

                self.ui.label_4.setText("SAVED!")

        if btnName == "btn_remove_task":
            row = self.ui.listWidget_22.currentRow()
            self.ui.listWidget_22.takeItem(row)

        if btnName == "btn_back_start":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            self.ui.leftMenuBg.show()
            self.ui.titleRightInfo.setText("START")

        # ROS PAGE on START PAGE
        if btnName == "ros_fiplan_save":
            if self.ui.plainTextEdit_34.toPlainText() != "":
                global ROS_SOURCE_MUTANT

                global FIPLAN_DIRECTORY_LIST

                mut_list = []

                dialog = QFileDialog()
                path_name = QFileDialog.getExistingDirectory()

                directory = self.ui.plainTextEdit_32.toPlainText()

                if path_name != "":
                    if directory:
                        ros_fiplan_name = (
                            self.ui.plainTextEdit_34.toPlainText() + "_type_launch.json"
                        )
                    else:
                        ros_fiplan_name = (
                            self.ui.plainTextEdit_34.toPlainText() + "_type_rospy.json"
                        )

                    len_ros_source_mutant = len(ROS_SOURCE_MUTANT)

                    for i in range(0, len_ros_source_mutant):

                        if i % 3 == 0:
                            file_directory = ROS_SOURCE_MUTANT[i]
                            original_code = ROS_SOURCE_MUTANT[i + 1]
                            mutant_code = ROS_SOURCE_MUTANT[i + 2]
                            if original_code != mutant_code:
                                created_fault = {
                                    "Fault": {
                                        "File_Directory": file_directory,
                                        "Source_Code": original_code,
                                        "Mutate_Code": mutant_code,
                                        "Exe_File": self.ui.label_86.text(),
                                    }
                                }

                                mut_list.append(created_fault)

                                def write_json(new_data, ros_fiplan_name):
                                    desired_dir = path_name
                                    full_path = os.path.join(
                                        desired_dir, ros_fiplan_name
                                    )
                                    with open(
                                        full_path, mode="w+", encoding="utf-8"
                                    ) as file:
                                        json_string = json.dumps(new_data, indent=4)
                                        file.write(json_string)
                                    return full_path

                                ros_fi_plan_path = write_json(mut_list, ros_fiplan_name)
                                # ROS FI Plan Name and Directory Path added to the list
                                FIPLAN_DIRECTORY_LIST.append(ros_fi_plan_path)

                    split_text = str(FIPLAN_DIRECTORY_LIST[-1]).split("\n")
                    self.ui.listWidget_36.addItems(split_text)
                    self.ui.listWidget_6.addItems(split_text)

                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText("Select Directory to Save FI Plan")
                    message_box.setWindowTitle("Warning!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

            else:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Check Mutant Codes and FI Plan Name")
                message_box.setWindowTitle("Caution!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

            def launch_run():
                """main func"""

                roscore_process = subprocess.Popen(["roscore"])
                time.sleep(5)

                message_box.setIcon(QMessageBox.Information)
                message_box.setText("Roscore is ready!")
                message_box.setWindowTitle("Ready!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

                roslaunch_folder_directory_path = self.ui.plainTextEdit_32.toPlainText()
                split_roslaunch_folder_directory_path = (
                    roslaunch_folder_directory_path.split("/")
                )

                folder_name = split_roslaunch_folder_directory_path[-3]

                ros_exe_file_name = self.ui.label_86.text()

                ros_process = subprocess.Popen(
                    [
                        "roslaunch",
                        folder_name,
                        ros_exe_file_name,
                    ]
                )
                try:
                    print("Running in process", ros_process.pid)
                    ros_process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    rosnode_list = subprocess.getoutput("rosnode list")
                    rostopic_list = subprocess.getoutput("rostopic list")
                    rosparam_list = subprocess.getoutput("rosparam list")
                    rosservice_list = subprocess.getoutput("rosservice list")
                    print("Timed out - killing", ros_process.pid)
                    ros_process.terminate()
                    roscore_process.terminate()

                time.sleep(1)
                print("Process Done")

                rosnodes = rosnode_list.split("\n")
                self.ui.listWidget_27.addItems(rosnodes)

                # ROS TOPIC LIST
                rostopics = rostopic_list.split("\n")
                self.ui.listWidget_28.addItems(rostopics)

                # ROS SERVICE LIST
                rosservices = rosservice_list.split("\n")
                self.ui.listWidget_29.addItems(rosservices)

                # ROS PARAMETER LIST
                rosparams = rosparam_list.split("\n")
                self.ui.listWidget_30.addItems(rosparams)

            directory = self.ui.plainTextEdit_32.toPlainText()
            if directory == "":
                directory = self.ui.plainTextEdit_33.toPlainText()
            split_directory = directory.split("/")

            if split_directory[-2] == "launch":
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Information)
                message_box.setText("Process Started. Please Wait!")
                message_box.setWindowTitle("Started!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()
                launch_run()
                message_box.setIcon(QMessageBox.Information)
                message_box.setText("Process Done")
                message_box.setWindowTitle("Done!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

            elif split_directory[-2] == "scripts" or split_directory[-2] == "src":
                if self.ui.checkBox_11.isChecked() is True:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Information)
                    message_box.setText("Process Started. Please Wait!")
                    message_box.setWindowTitle("Started!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()
                    self.rospy_run()
                    message_box.setIcon(QMessageBox.Information)
                    message_box.setText("Process Done")
                    message_box.setWindowTitle("Done!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()
                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Warning)
                    message_box.setText("Be sure to select launch or scripts/src file!")
                    message_box.setWindowTitle("Attention")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()
            else:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setText("Be sure to select launch or scripts/src file!")
                message_box.setWindowTitle("Attention")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

        if btnName == "add_order_btn":
            target_file_path = self.ui.plainTextEdit_32.toPlainText()
            splitted_target_path = target_file_path.split("/")

            try:
                file_from_tree = str(self.ui.treeView.selectedIndexes()[0].data())

                if (
                    splitted_target_path[-2] == "scripts"
                    or splitted_target_path[-2] == "src"
                    and file_from_tree != ""
                ):
                    path = self.ui.plainTextEdit_32.toPlainText()
                    rospy_directory_and_file_name = path + file_from_tree
                    self.ui.listWidget_26.addItem(rospy_directory_and_file_name)
                    RUN_ORDER_LIST_JUST_PATH.append(path)
                    RUN_ORDER_LIST_JUST_PATH.append(file_from_tree)

                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText(
                        "Check the folder and the package!\nPlease be sure to open scripts folder!"
                    )
                    message_box.setWindowTitle("Caution!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

            except:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Please select a file!")
                message_box.setWindowTitle("Warning!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

        if btnName == "select_trgt_btn":
            global ROS_SOURCE_CODE

            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("*.py *.launch")

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".py") or file_name[0].endswith(".launch"):

                    with open(file_name[0], mode="r", encoding="utf-8") as file:
                        data = file.read()

                        directory_split = file_name[0].split("/")
                        ros_file_name = directory_split[-1]

                        self.ui.label_86.setText(ros_file_name)
                        directory_split.pop(-1)

                        ros_launch_directory = ""

                        for i in directory_split:
                            ros_launch_directory += i + "/"

                        self.ui.plainTextEdit_32.setPlainText(ros_launch_directory)
                        ROS_SOURCE_CODE = data
                        splitted_ros_source_codes = ROS_SOURCE_CODE.split("\n")
                        self.ui.listWidget_32.addItems(splitted_ros_source_codes)

                    model = QFileSystemModel()
                    model.setRootPath(ros_launch_directory)

                    self.ui.treeView.setModel(model)
                    self.ui.treeView.setRootIndex(model.index(ros_launch_directory))
                    self.ui.treeView.setSortingEnabled(True)
                    self.ui.treeView.hideColumn(1)
                    self.ui.treeView.hideColumn(2)
                    self.ui.treeView.hideColumn(3)

                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText(
                        "Please be sure to selected .py or .launch file!"
                    )
                    message_box.setWindowTitle("Attention!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

        if btnName == "remove_order_btn":

            def remove_ros():
                row = self.ui.listWidget_26.currentRow()
                self.ui.listWidget_26.takeItem(row)

            remove_ros()

        if btnName == "add_ros_btn":

            def fault_select_ros():
                global ZIPPED_ROS_LIST
                ZIPPED_ROS_LIST = []

                is_text_full = self.ui.plainTextEdit_39.toPlainText()

                if is_text_full:
                    try:
                        selected_line = self.ui.listWidget_33.currentItem().text()
                        selected_fault = self.ui.listWidget_34.currentItem().text()

                        selected_line_text = "Line: " + selected_line
                        selected_fault_text = "\tFault: " + selected_fault

                        ZIPPED_ROS_LIST.append(selected_line)
                        ZIPPED_ROS_LIST.append(selected_fault)

                        selected_line_and_fault = (
                            selected_line_text + selected_fault_text
                        )

                        line_and_fault = selected_line_and_fault.split("\n")

                        self.ui.listWidget_35.addItems(line_and_fault)

                    except AttributeError() or TypeError():
                        message_box = QMessageBox()
                        message_box.setIcon(QMessageBox.Critical)
                        message_box.setText("Error!")
                        message_box.setWindowTitle("Error!")
                        message_box.setStandardButtons(QMessageBox.Ok)
                        message_box.exec()

            fault_select_ros()

        if btnName == "ros_slct_fiplan":
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter(("*.json"))

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".json"):
                    directory = file_name[0]
                    new_file_name = directory.split("/")
                    ros_fi_plan_name = new_file_name[-1]
                    name_and_path = ros_fi_plan_name + "    Directory: " + directory
                    self.ui.listWidget_36.addItem(name_and_path)
                    FIPLAN_DIRECTORY_LIST.append(name_and_path)

        if btnName == "ros_fiplan_remove":

            def ros_fiplan_remove():
                FIPLAN_DIRECTORY_LIST = []

                if FIPLAN_DIRECTORY_LIST:
                    row = self.ui.listWidget_36.currentRow()
                    self.ui.listWidget_36.takeItem(row)
                    FIPLAN_DIRECTORY_LIST.pop(row)

            ros_fiplan_remove()

        # Target ROS file is opened to apply mutation process
        if btnName == "open_target_ros":
            size_target_ros_list = self.ui.listWidget_10.count()

            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("*.py")

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".py"):
                    if size_target_ros_list > 0:
                        self.ui.listWidget_10.clear()

                    with open(file_name[0], mode="r", encoding="utf-8") as file:
                        data = file.read()
                        self.ui.plainTextEdit_33.setPlainText(file_name[0])
                        ROS_SOURCE_CODE = data
                        splitted_ros_source_codes = data.split("\n")
                        self.ui.listWidget_10.addItems(splitted_ros_source_codes)

                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText("Please be sure to selected .py file!")
                    message_box.setWindowTitle("Attention!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

        if btnName == "remove_ros_btn":

            def remove_ros():
                global ZIPPED_ROS_LIST
                ZIPPED_ROS_LIST = []

                row = self.ui.listWidget_35.currentRow()
                self.ui.listWidget_35.takeItem(row)

                for i in range(2):
                    del ZIPPED_ROS_LIST[row]

            remove_ros()

        if btnName == "remove_ros_mutant":

            def remove_ros_mutant():
                global ROS_SOURCE_MUTANT

                row = self.ui.listWidget_31.currentRow()
                row_text = self.ui.listWidget_31.item(row).text()
                self.ui.listWidget_31.takeItem(row)
                self.ui.label_81.setText(str(self.ui.listWidget_31.count()))

                if row > 0:
                    for i in range(len(ROS_SOURCE_MUTANT)):
                        if ROS_SOURCE_MUTANT[i] == row_text:
                            ROS_SOURCE_MUTANT.pop(i)
                            ROS_SOURCE_MUTANT.pop(i - 1)
                            break

            if self.ui.listWidget_31.count() > 0:
                remove_ros_mutant()

        if btnName == "scan_ros_btn":
            total_ros_items = []

            len_node_list = self.ui.listWidget_27.count()
            len_topic_list = self.ui.listWidget_28.count()
            len_service_list = self.ui.listWidget_29.count()
            len_param_list = self.ui.listWidget_30.count()

            for i in range(len_node_list):
                node_list_item = self.ui.listWidget_27.item(i).text()
                node_list_item = node_list_item[1:]
                total_ros_items.append(node_list_item)

            for i in range(len_topic_list):
                topic_list_item = self.ui.listWidget_28.item(i).text()
                topic_list_item = topic_list_item[1:]
                total_ros_items.append(topic_list_item)

            for i in range(len_service_list):
                service_list_item = self.ui.listWidget_29.item(i).text()
                service_list_item = service_list_item[1:]
                total_ros_items.append(service_list_item)

            for i in range(len_node_list):
                param_list_item = self.ui.listWidget_30.item(i).text()
                param_list_item = param_list_item[1:]
                total_ros_items.append(param_list_item)

            len_ros_code = self.ui.listWidget_10.count()

            directory = self.ui.plainTextEdit_32.toPlainText()
            split_directory = directory.split("/")

            if directory:
                if split_directory[-1] == "launch" or split_directory[-2] == "launch":
                    python_files_list = []
                    launch_files_list = []

                    key_list = ["type", "file"]

                    def mutate_all_keys(key_data_list, location, target_file):
                        """Mutation testing applies to  the all possible nodes"""
                        ros_launch_directory_path = (
                            self.ui.plainTextEdit_32.toPlainText()
                        )

                        os.chdir(ros_launch_directory_path)
                        tree = ET.parse(target_file)
                        root = tree.getroot()
                        lenroot = len(root)
                        for i in range(0, lenroot):
                            dictof = root[i].attrib
                            key_list = list(dictof.keys())

                            for target_key in key_list:
                                if target_key == "type":
                                    file_type_info_from_launch = dictof["type"]
                                    find_python_type_info = re.findall(
                                        ".py", file_type_info_from_launch
                                    )
                                    if find_python_type_info:
                                        # The list has Python type files
                                        python_files_list.append(
                                            file_type_info_from_launch
                                        )

                                elif target_key == "file":
                                    # The list has launch type files
                                    launch_files_list.append(dictof["file"])

                    def open_python(location, python_files_list):
                        is_ros_for_mutation_list_empty = self.ui.listWidget_10.count()

                        if is_ros_for_mutation_list_empty > 0:
                            target_ros_py_location = (
                                self.ui.plainTextEdit_33.toPlainText()
                            )
                            target_ros_file_size = self.ui.listWidget_10.count()

                            for line_number in range(0, target_ros_file_size):
                                ros_file_line = self.ui.listWidget_10.item(
                                    line_number
                                ).text()
                                for pattern in total_ros_items:
                                    find_possible_line = re.findall(
                                        pattern, ros_file_line, re.MULTILINE
                                    )
                                    check_rospy = re.findall(
                                        "rospy", ros_file_line, re.MULTILINE
                                    )
                                    if find_possible_line and check_rospy:
                                        self.ui.listWidget_10.item(
                                            line_number
                                        ).setBackground(
                                            QtGui.QColor(102, 0, 102)
                                        )  # Purple color
                                        line_and_location = []
                                        line_and_location = [
                                            ros_file_line.strip(),
                                            " Directory: ",
                                            target_ros_py_location,
                                        ]
                                        str_line_and_location = (
                                            line_and_location[0]
                                            + line_and_location[1]
                                            + line_and_location[2]
                                        )
                                        self.ui.listWidget_33.addItem(
                                            str_line_and_location
                                        )

                        else:
                            for i in python_files_list:
                                with open(
                                    os.path.join(location, i),
                                    mode="r",
                                    encoding="utf-8",
                                ) as x_file:

                                    pure_file_content = x_file.read()

                                split_file_content = pure_file_content.split("\n")

                                lstrip_lines = []

                                for line in split_file_content:
                                    changed_line = line.lstrip()
                                    lstrip_lines.append(changed_line)

                                for ros_code_line in lstrip_lines:
                                    for pattern in total_ros_items:
                                        find_possible_line = re.findall(
                                            pattern, ros_code_line, re.MULTILINE
                                        )
                                        if find_possible_line:
                                            check_rospy = re.findall(
                                                "rospy", ros_code_line, re.MULTILINE
                                            )
                                            if check_rospy:
                                                line_and_location = []
                                                target_ros_py_location = (
                                                    location + "/" + i
                                                )
                                                ros_code_line = ros_code_line.lstrip()
                                                line_and_location = [
                                                    ros_code_line,
                                                    " Directory: ",
                                                    target_ros_py_location,
                                                ]
                                                str_line_and_location = (
                                                    line_and_location[0]
                                                    + line_and_location[1]
                                                    + line_and_location[2]
                                                )
                                                self.ui.listWidget_33.addItem(
                                                    str_line_and_location
                                                )

                    new_location = ""

                    complete_directory_path = self.ui.plainTextEdit_32.toPlainText()

                    split_complete_directory_path = complete_directory_path.split("/")

                    target_file = (
                        self.ui.label_86.text()
                    )

                    for i in range(0, 6):
                        full_location += split_complete_directory_path[i] + "/"

                    mutate_all_keys(key_list, full_location, target_file)

                    if launch_files_list:
                        for i in launch_files_list:
                            split_value = i.split("/")
                            target_file = split_value[-1]
                            mutate_all_keys(key_list, full_location, target_file)

                        for i in range(0, 7):
                            new_location += split_complete_directory_path[i] + "/"

                        selected_location = new_location + "scripts"

                        open_python(selected_location, python_files_list)

            else:
                single_ros__process_folder_name = self.ui.plainTextEdit_33.toPlainText()

                for i in range(0, len_ros_code):
                    ros_code_line = self.ui.listWidget_10.item(i).text()

                    check_rospy = re.findall("rospy", ros_code_line, re.MULTILINE)
                    if check_rospy:
                        complete_name = single_ros__process_folder_name

                        ros_code_line = ros_code_line.lstrip()
                        ros_line_and_directory = (
                            ros_code_line + " Directory: " + complete_name
                        )
                        self.ui.listWidget_33.addItem(ros_line_and_directory)

        if btnName == "mutate_ros_btn":
            global ZIPPED_ROS_LIST

            length_found_lines = self.ui.listWidget_33.count()
            length_mutant_codes_list = self.ui.listWidget_31.count()

            directory = self.ui.plainTextEdit_32.toPlainText()

            if directory:
                split_directory = directory.split("/")
            else:
                directory = self.ui.plainTextEdit_33.toPlainText()
                split_directory = directory.split("/")

            if length_mutant_codes_list:
                self.ui.listWidget_31.clear()
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText("Mutants have already been updated!")
                message_box.setWindowTitle("Warning!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec()

            if length_found_lines:
                node_list = []
                topic_list = []
                service_list = []
                parameter_list = []

                len_node_list = self.ui.listWidget_27.count()
                len_topic_list = self.ui.listWidget_28.count()
                len_service_list = self.ui.listWidget_29.count()
                len_param_list = self.ui.listWidget_30.count()

                for i in range(len_node_list):
                    item = self.ui.listWidget_27.item(i).text()
                    node_list.append(item[1:])

                for i in range(len_topic_list):
                    item = self.ui.listWidget_28.item(i).text()
                    if split_directory[-2] == "scripts" or split_directory[-2] == "src":
                        topic_list.append(item[1:])
                    if split_directory[-2] == "launch":
                        topic_list.append(item)

                for i in range(len_service_list):
                    item = self.ui.listWidget_29.item(i).text()
                    service_list.append(item[1:])

                for i in range(len_param_list):
                    item = self.ui.listWidget_30.item(i).text()
                    parameter_list.append(item[1:])

                def constant_mutate_function(target_line, loc):
                    global ZIPPED_ROS_LIST
                    global POSSIBLE_MUTANT_LIST

                    constant_list = []

                    class ConstantMutator(ast.NodeTransformer):
                        """Constant Mutator Class"""

                        def visit_Constant(self, node):
                            """The visitor function."""
                            if isinstance(node.value, str):
                                constant_target = node.value
                                constant_list.append(constant_target)

                    node = ast.parse(target_line)
                    renamer = ConstantMutator()
                    node2 = renamer.visit(node)

                    all_ros_patterns = [
                        "rospy.Sub",
                        "rospy.Pub",
                        "rospy.Log",
                        "rospy.log",
                        "rospy.Time",
                        "rospy.Dur",
                        "rospy.Rate",
                        "rospy.Par",
                        "rospy.Ser",
                        "rospy.ser",
                        "rospy.init",
                    ]

                    for ros_pattern in all_ros_patterns:
                        ros_result = re.findall(ros_pattern, target)
                        if ros_result:
                            if (
                                ros_result[0] == "rospy.Sub"
                                or ros_result[0] == "rospy.Pub"
                            ):
                                POSSIBLE_MUTANT_LIST = [
                                    self.ui.listWidget_28.item(x).text()
                                    for x in range(self.ui.listWidget_28.count())
                                ]
                            elif (
                                ros_result[0] == "rospy.Log"
                                or ros_result[0] == "rospy.log"
                            ):
                                POSSIBLE_MUTANT_LIST = [
                                    self.ui.listWidget_28.item(x).text()
                                    for x in range(self.ui.listWidget_28.count())
                                ]
                            elif ros_result[0] == "rospy.Par":
                                POSSIBLE_MUTANT_LIST = [
                                    self.ui.listWidget_30.item(x).text()
                                    for x in range(self.ui.listWidget_30.count())
                                ]
                            elif (
                                ros_result[0] == "rospy.Ser"
                                or ros_result[0] == "rospy.ser"
                            ):
                                POSSIBLE_MUTANT_LIST = [
                                    self.ui.listWidget_29.item(x).text()
                                    for x in range(self.ui.listWidget_29.count())
                                ]
                            elif ros_result[0] == "rospy.init":
                                POSSIBLE_MUTANT_LIST = [
                                    self.ui.listWidget_27.item(x).text()
                                    for x in range(self.ui.listWidget_27.count())
                                ]
                            else:
                                POSSIBLE_MUTANT_LIST = [
                                    "mutant_1",
                                    "mutant_2",
                                    "mutant_3",
                                ]

                            for i in constant_list:
                                for j in POSSIBLE_MUTANT_LIST:
                                    x = j[1:].join(target.rsplit(i, 1))
                                    if target_line != x:
                                        self.ui.listWidget_31.addItem(x)
                                        add_location(loc)
                                        ROS_SOURCE_MUTANT.append(loc)
                                        ROS_SOURCE_MUTANT.append(target_line)
                                        ROS_SOURCE_MUTANT.append(x)

                # AST NAME MUTATOR
                # Funciton name is mutated by IM-FIT with using the method
                def function_name_mutator(target_line, loc):
                    """Method applies mutation for function name of ROS source codes"""
                    name_list = []

                    class NameIdMutator(ast.NodeTransformer):
                        """Name ID mutator class"""

                        def VisitName(self, node):
                            """Method applies mutation for Name ID"""
                            target = node.id
                            if (
                                target != "rospy"
                                and target != "String"
                                and target != "args"
                                and target != "kwargs"
                            ):
                                name_list.append(target)

                    node = ast.parse(target_line)
                    renamer = NameIdMutator()
                    node2 = renamer.visit(node)

                    mutant_list = [
                        "representative_mutant_1",
                        "representative_mutant_2",
                        "representative_mutant_3",
                    ]

                    for i in name_list:
                        for j in mutant_list:
                            x = j[1:].join(target.rsplit(i, 1))
                            if target_line != x:
                                self.ui.listWidget_31.addItem(x)
                                add_location(loc)
                                ROS_SOURCE_MUTANT.append(loc)
                                ROS_SOURCE_MUTANT.append(target_line)
                                ROS_SOURCE_MUTANT.append(x)

                ### AST VALUE MUTATOR ###

                def value_mutate_function(target_line, loc):
                    class ConstantMutator(ast.NodeTransformer):
                        """Constant Mutator Class"""

                        global constant_list
                        constant_list = []

                        def visit_Constant(self, node):
                            """The visitor function."""
                            if not isinstance(node.value, str):
                                if isinstance(node.value, bool):
                                    if node.value is True:
                                        node.value = False
                                        self.generic_visit(node)
                                        return node
                                    node.value = True
                                    self.generic_visit(node)
                                    return node
                                value_number = node.value
                                random_number_for_node_value = random.randint(1, 100)
                                if value_number != random_number_for_node_value:
                                    node.value = random.randint(1, 100)
                                    return node
                                else:
                                    node.value = (random.randint(1, 100)) + 1
                                    return node
                            return node

                    node = ast.parse(target_line)
                    renamer = ConstantMutator()
                    node2 = renamer.visit(node)
                    unparsed_code = astunparse.unparse(node2)
                    unparsed_code = unparsed_code.strip()
                    if target_line != unparsed_code:
                        self.ui.listWidget_31.addItem(unparsed_code)
                        add_location(loc)
                        ROS_SOURCE_MUTANT.append(loc)
                        ROS_SOURCE_MUTANT.append(target_line)
                        ROS_SOURCE_MUTANT.append(unparsed_code)

                def add_location(loc):
                    mutant_code_list_size = self.ui.listWidget_31.count()

                    if mutant_code_list_size > 0:
                        line_of_mutant_list = self.ui.listWidget_31.item(
                            mutant_code_list_size - 1
                        ).text()
                        self.ui.listWidget_31.takeItem(mutant_code_list_size - 1)
                        new_line = line_of_mutant_list + "        Directory: " + loc
                        self.ui.listWidget_31.addItem(new_line)

                if (
                    self.ui.checkBox_9.isChecked() is True
                    and self.ui.listWidget_33.count() > 0
                ):
                    list_found_lines = []
                    list_directories = []
                    len_found_lines = self.ui.listWidget_33.count()
                    for i in range(len_found_lines):
                        found_line_and_directory = self.ui.listWidget_33.item(i).text()
                        split_found_line_and_directory = found_line_and_directory.split(
                            " Directory: "
                        )
                        item_found_lines = split_found_line_and_directory[0]
                        item_found_directory = split_found_line_and_directory[1]
                        list_found_lines.append(item_found_lines)
                        list_directories.append(item_found_directory)

                    for target_line, _ in enumerate(list_found_lines):
                        target = list_found_lines[target_line]
                        loc = list_directories[target_line]
                        constant_mutate_function(target, loc)
                        value_mutate_function(target, loc)
                        result = re.findall("rospy.log", target)
                        if result:
                            function_name_mutator(target, loc)

                else:
                    len_zipped_ros_list = len(ZIPPED_ROS_LIST)
                    for i in range(len_zipped_ros_list):
                        if i % 2 == 1:
                            target_line = str(ZIPPED_ROS_LIST[i - 1])
                            selected_fault = str(ZIPPED_ROS_LIST[i])
                            if selected_fault == "ROS Pub-Sub Mutation":
                                find_snip = ["rospy.Sub", "rospy.Pub"]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)
                                    if result:
                                        split_found_line_and_directory = (
                                            target_line.split(" Directory: ")
                                        )
                                        target = split_found_line_and_directory[0]
                                        loc = split_found_line_and_directory[1]

                                        constant_mutate_function(target, loc)
                                        value_mutate_function(target, loc)

                            if selected_fault == "ROS Log Mutation":
                                find_snip = ["rospy.Log", "rospy.log"]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)

                                    if result:
                                        split_found_line_and_directory = (
                                            target_line.split(" Directory: ")
                                        )
                                        target = split_found_line_and_directory[0]
                                        loc = split_found_line_and_directory[1]

                                        function_name_mutator(target, loc)
                                        value_mutate_function(target, loc)

                            if selected_fault == "ROS Time Mutation":
                                find_snip = [
                                    "rospy.Time",
                                    "rospy.Dur",
                                    "rospy.Rate",
                                ]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)
                                    if result:
                                        split_found_line_and_directory = (
                                            target_line.split(" Directory: ")
                                        )
                                        target = split_found_line_and_directory[0]
                                        loc = split_found_line_and_directory[1]

                                        value_mutate_function(target, loc)

                            if selected_fault == "ROS Parameter Mutation":
                                find_snip = ["rospy.Par"]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)
                                    split_found_line_and_directory = target_line.split(
                                        " Directory: "
                                    )
                                    target = split_found_line_and_directory[0]
                                    loc = split_found_line_and_directory[1]
                                    if result:
                                        function_name_mutator(target, loc)
                                        constant_mutate_function(target, loc)
                                        value_mutate_function(target, loc)

                            if selected_fault == "ROS Service Mutation":
                                find_snip = ["rospy.Ser", "rospy.ser"]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)
                                    if result:
                                        split_found_line_and_directory = (
                                            target_line.split(" Directory: ")
                                        )
                                        target = split_found_line_and_directory[0]
                                        loc = split_found_line_and_directory[1]

                                        function_name_mutator(target, loc)
                                        constant_mutate_function(target, loc)
                                        value_mutate_function(target, loc)

                            if selected_fault == "ROS Initializing Node Mutation":
                                find_snip = ["rospy.init"]
                                for snip in find_snip:
                                    result = re.findall(snip, target_line)
                                    if result:
                                        split_found_line_and_directory = (
                                            target_line.split(" Directory: ")
                                        )
                                        target = split_found_line_and_directory[0]
                                        loc = split_found_line_and_directory[1]
                                        constant_mutate_function(target, loc)
                                        value_mutate_function(target, loc)

        #  CODE SNIPPETS FROM START PAGE
        if btnName == "btn_create_code":
            self.ui.stackedWidget.setCurrentWidget(self.ui.cSnippets)
            self.ui.leftMenuBg.hide()
            self.ui.titleRightInfo.setText("CODE SNIPPETS - CREATE CUSTOM SNIPPETS")

        if btnName == "btn_remove_snip":
            row = self.ui.listWidget_8.currentRow()
            self.ui.listWidget_8.takeItem(row)

        # CREATE CUSTOM SNIPPETS FROM START PAGE
        if btnName == "btn_create_snip":
            snippet_name = self.ui.plainTextEdit_47.toPlainText()
            snippet_title = self.ui.plainTextEdit_48.toPlainText()
            snippet_process = self.ui.plainTextEdit_49.toPlainText()
            snippet_regex = self.ui.plainTextEdit_50.toPlainText()

            created_snippet_json = {
                "Snippets": {
                    "Snippet_Name": snippet_name,
                    "Title": snippet_title,
                    "Process": snippet_process,
                    "Regex_Code": snippet_regex,
                }
            }

            json_snippet = json.dumps(created_snippet_json, indent=4)

            self.ui.plainTextEdit_51.setPlainText(json_snippet)

        if btnName == "btn_delete_snip":
            self.ui.plainTextEdit_47.clear()
            self.ui.plainTextEdit_48.clear()
            self.ui.plainTextEdit_49.clear()
            self.ui.plainTextEdit_50.clear()
            self.ui.plainTextEdit_51.clear()
            self.ui.plainTextEdit_52.clear()

        if btnName == "btn_save_snip":

            is_empty_code_snippet = self.ui.plainTextEdit_51.toPlainText()

            if is_empty_code_snippet != "" and self.ui.checkBox_6.isChecked() is True:

                snippet_name = self.ui.plainTextEdit_47.toPlainText()
                snippet_title = self.ui.plainTextEdit_48.toPlainText()
                snippet_process = self.ui.plainTextEdit_49.toPlainText()
                snippet_regex = self.ui.plainTextEdit_50.toPlainText()

                created_snippet = {
                    "Snippets": {
                        "Snippet_Name": snippet_name,
                        "Title": snippet_title,
                        "Process": snippet_process,
                        "Regex_Code": snippet_regex,
                    }
                }

                with open("code_snippets.json", mode="r+", encoding="utf-8") as file:
                    file_data = json.load(file)
                    file_data["code_snippets"].append(created_snippet)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

                code_snippet_file_name = self.ui.plainTextEdit_52.toPlainText()

                dialog = QFileDialog()
                path_name = QFileDialog.getExistingDirectory()

                code_snippet_path_and_name = os.path.join(
                    path_name, code_snippet_file_name + ".json"
                )

                created_code_snippets = self.ui.plainTextEdit_51.toPlainText()

                with open(
                    code_snippet_path_and_name, mode="w", encoding="utf-8"
                ) as file:
                    file.write(created_code_snippets)

                with open("custom_snippets.json", mode="w", encoding="utf-8") as file:
                    file.write(created_code_snippets)

                self.ui.label_60.setText("SAVED!")

                self.ui.code_snippet_list.addItem(snippet_name)

        if btnName == "btn_snip_location":
            dialog = QFileDialog()
            path_name = QFileDialog.getExistingDirectory()
            self.ui.plainTextEdit_51.setPlainText(path_name)

        if btnName == "back_snip":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            self.ui.leftMenuBg.show()
            self.ui.titleRightInfo.setText("START")

        #  SCAN PAGE
        if btnName == "btn_back_code":
            self.ui.stackedWidget.setCurrentWidget(self.ui.start)
            UIFunctions.resetStyle(self, self.ui.btn_scan.styleSheet())
            self.ui.btn_start.setStyleSheet(
                UIFunctions.selectMenu(self.ui.btn_start.styleSheet())
            )

        if btnName == "btn_create_custom":
            self.ui.stackedWidget.setCurrentWidget(self.ui.customFault)
            self.ui.leftMenuBg.hide()
            self.ui.titleRightInfo.setText("FAULT INJECTION PLAN - CREATE CUSTOM FAULT")

        if btnName == "btn_remove_fault":
            global ZIPPED_LIST

            row = self.ui.listWidget_7.currentRow()
            self.ui.listWidget_7.takeItem(row)

            for i in range(2):
                del ZIPPED_LIST[row]

        if btnName == "btn_save_fiplan":
            global SOURCE_AND_MUTANT_CODE

            selected_task_list_size = self.ui.listWidget_4.count()
            created_fault_plan_list = []

            if selected_task_list_size:
                dialog = QFileDialog()
                path_name = QFileDialog.getExistingDirectory()
                if path_name != "":
                    file_name = self.ui.plainTextEdit_20.toPlainText() + ".json"

                mutant_code_list_length = len(SOURCE_AND_MUTANT_CODE)
                source_code_directory = self.ui.plainTextEdit_10.toPlainText()

                for i in range(0, mutant_code_list_length):
                    if i % 2 == 0:
                        original_code = SOURCE_AND_MUTANT_CODE[i]
                    else:
                        mutant_code = SOURCE_AND_MUTANT_CODE[i]

                        created_fault = {
                            "Fault": {
                                "File_Directory": source_code_directory,
                                "Source_Code": original_code,
                                "Mutate_Code": mutant_code,
                            }
                        }
                        created_fault_plan_list.append(created_fault)

                with open("fault_plans.json", mode="w", encoding="utf-8") as file:
                    fault_plan_json_format = json.dumps(
                        created_fault_plan_list, indent=4
                    )
                    file.write(fault_plan_json_format)

                text = self.ui.plainTextEdit_20.toPlainText() + "_type_python.json"
                full_path = os.path.join(path_name, text)

                with open(full_path, mode="w", encoding="utf-8") as file:
                    fault_plan_json_format = json.dumps(
                        created_fault_plan_list, indent=4
                    )
                    file.write(fault_plan_json_format)

                split_text = full_path.split("\n")
                self.ui.listWidget_11.addItems(split_text)
                self.ui.listWidget_6.addItems(split_text)

        if btnName == "btn_remove_fiplan":
            row = self.ui.listWidget_11.currentRow()
            self.ui.listWidget_11.takeItem(row)

        # CREATE CUSTOM FAULT FROM FI PLAN
        if btnName == "btn_back_fi":
            self.ui.stackedWidget.setCurrentWidget(self.ui.fiplan)
            self.ui.leftMenuBg.show()
            self.ui.titleRightInfo.setText("FAULT INJECTION PLAN")

            created_fault_list_size = self.ui.listWidget_5.count()

            if created_fault_list_size:
                for i in range(0, created_fault_list_size):
                    created_fault_list_line = self.ui.listWidget_5.item(i).text()
                    self.ui.listWidget_3.addItem(created_fault_list_line)

        if btnName == "btn_create_fault":
            fault_name = self.ui.plainTextEdit_40.toPlainText()
            target = self.ui.plainTextEdit_41.toPlainText()
            changed = self.ui.plainTextEdit_42.toPlainText()
            explanation = self.ui.plainTextEdit_43.toPlainText()

            created_fault_json = {
                "fault": {
                    "Fault_Name": fault_name,
                    "Target_to_Change": target,
                    "Changed": changed,
                    "Explanation": explanation,
                }
            }

            json_fault = json.dumps(created_fault_json, indent=4)

            self.ui.plainTextEdit_45.setPlainText(json_fault)

        if btnName == "btn_delete_fault":
            self.ui.plainTextEdit_40.clear()
            self.ui.plainTextEdit_41.clear()
            self.ui.plainTextEdit_42.clear()
            self.ui.plainTextEdit_43.clear()
            self.ui.plainTextEdit_45.clear()

        if btnName == "btn_save_fault":
            if (
                self.ui.plainTextEdit_40.toPlainText() != ""
                and self.ui.plainTextEdit_41.toPlainText() != ""
                and self.ui.plainTextEdit_42.toPlainText() != ""
                and self.ui.plainTextEdit_43.toPlainText() != ""
            ):
                fault_name = self.ui.plainTextEdit_40.toPlainText()
                target = self.ui.plainTextEdit_41.toPlainText()
                changed = self.ui.plainTextEdit_42.toPlainText()
                explanation = self.ui.plainTextEdit_43.toPlainText()

                created_fault_json = {
                    "fault": {
                        "Fault_Name": fault_name,
                        "Target_to_Change": target,
                        "Changed": changed,
                        "Explanation": explanation,
                    }
                }

                with open("fault_library.json", mode="r+", encoding="utf-8") as file:
                    file_data = json.load(file)
                    file_data["all_faults"].append(created_fault_json)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

                    json_fault = json.dumps(created_fault_json, indent=4)

                    workload_file_name = self.ui.plainTextEdit_44.toPlainText()

                    dialog = QFileDialog()
                    path_name = QFileDialog.getExistingDirectory()

                    task_path_and_name = os.path.join(
                        path_name, workload_file_name + ".json"
                    )

                    created_fault = self.ui.plainTextEdit_45.toPlainText()

                    with open(
                        task_path_and_name, mode="w", encoding="utf-8"
                    ) as json_file:
                        json_file.write(created_fault)

                    with open("custom_faults.json", mode="w", encoding="utf-8") as file:
                        file.write(created_fault)

                    self.ui.label_61.setText("SAVED!")

                self.ui.listWidget_5.addItem(fault_name)

                self.ui.plainTextEdit_40.clear()
                self.ui.plainTextEdit_41.clear()
                self.ui.plainTextEdit_42.clear()
                self.ui.plainTextEdit_43.clear()
                self.ui.plainTextEdit_45.clear()

            else:
                self.ui.label_61.setText("FAULT DOES NOT EXIST!")

        if btnName == "btn_remove_createdFault":
            row = self.ui.listWidget_5.currentRow()
            self.ui.listWidget_5.takeItem(row)

        # EXECUTION PAGE
        if btnName == "btn_select_metrics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.selectMetrics)
            self.ui.leftMenuBg.hide()
            self.ui.titleRightInfo.setText("EXECUTION - METRICS")

        # SELECT METRICS FROM EXECUTION PAGE
        if btnName == "pushButton_16":
            mutant_folder_directory = QFileDialog.getExistingDirectory(
                self, "Select Folder"
            )
            # mutant folder directory is added on the "target location"
            self.ui.plainTextEdit_24.setPlainText(mutant_folder_directory)
            model = QFileSystemModel()
            model.setRootPath(mutant_folder_directory)
            self.ui.treeView_2.setModel(model)
            self.ui.treeView_2.setRootIndex(model.index(mutant_folder_directory))
            self.ui.treeView_2.setSortingEnabled(True)
            self.ui.treeView_2.hideColumn(1)
            self.ui.treeView_2.hideColumn(2)
            self.ui.treeView_2.hideColumn(3)

        if btnName == "btn_export_fiplan":
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("*.json")

            if dialog.exec():
                file_name = dialog.selectedFiles()
                if file_name[0].endswith(".json"):
                    self.ui.listWidget_6.addItem(file_name[0])
                else:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Critical)
                    message_box.setText("Please be sure to selected FI Plan file!")
                    message_box.setWindowTitle("Attention!")
                    message_box.setStandardButtons(QMessageBox.Ok)
                    message_box.exec()

        if btnName == "btn_remove_fi":
            row = self.ui.listWidget_6.currentRow()
            if row is not None:
                fiplan_list_element = self.ui.listWidget_6.currentItem().text()
                self.ui.listWidget_6.takeItem(row)
                selected_fiplan = self.ui.plainTextEdit_23.toPlainText()
                if fiplan_list_element == selected_fiplan:
                    self.ui.plainTextEdit_23.clear()

    def resizeEvent(self, event):
        """Resize UI window method"""
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        """Mouse press event method for UI"""
        global_position_event = event.globalPosition()
        globalPos = global_position_event.toPoint()
        self.dragPos = globalPos


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())




