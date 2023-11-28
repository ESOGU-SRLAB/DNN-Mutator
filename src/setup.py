#!/usr/bin/env python

from http.server import executable
from ssl import Options
import sys
import os
from cx_Freeze import setup, Executable

files = [
    "code_snippets.json",
    "customFaults.json",
    "customSnippets.json",
    "faultLibrary.json",
    "faultPlans.json",
    "metricList.json",
    "resources_rc.py",
    "resources.qrc",
    "main.ui",
    "ui_main.py",
    "images/",
    "modules/",
    "theme/",
    "widgets/",
    "icon.ico"
]
target = Executable(
    script="main.py",
    icon = "icon.ico"
)

setup(
    name = "IM-FIT",
    version = "1.0",
    options = {'build.exe':{"include_files":files}},
    executables = [target]
)