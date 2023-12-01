import mutator
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

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6 import QtGui

from PySide6 import *

from modules import *

from widgets import *

from ui_main import Ui_MainWindow

    
def layer_select_mutate(mutate_selected_parameters,source_code ):
        mutated_code =""
        mutated_line =""
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
        elif mutate_selected_parameters == "AvgPool1D":
            change_parameter_with = "tf.keras.layers.AvgPool1D()"
            layer_name = "AvgPool1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "AvgPool2D":
            change_parameter_with = "tf.keras.layers.AvgPool2D()"
            layer_name = "AvgPool2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "AvgPool3D":
            change_parameter_with = "tf.keras.layers.AvgPool3D()"
            layer_name = "AvgPool3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "BatchNormalization":
            change_parameter_with = "tf.keras.layers.BatchNormalization()"
            layer_name = "BatchNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Bidirectional":
            change_parameter_with = "tf.keras.layers.Bidirectional()"
            layer_name = "Bidirectional"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "CategoryEncoding":
            change_parameter_with = "tf.keras.layers.CategoryEncoding()"
            layer_name = "CategoryEncoding"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "CenterCrop":
            change_parameter_with = "tf.keras.layers.CenterCrop()"
            layer_name = "CenterCrop"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Concatenate":
            change_parameter_with = "tf.keras.layers.Concatenate()"
            layer_name = "Concatenate"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv1D":
            change_parameter_with = "tf.keras.layers.Conv1D()"
            layer_name = "Conv1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv1DTranspose":
            change_parameter_with = "tf.keras.layers.Conv1DTranspose()"
            layer_name = "Conv1DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv2D":
            change_parameter_with = "tf.keras.layers.Conv2D()"
            layer_name = "Conv2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv2DTranspose":
            change_parameter_with = "tf.keras.layers.Conv2DTranspose()"
            layer_name = "Conv2DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv3D":
            change_parameter_with = "tf.keras.layers.Conv3D()"
            layer_name = "Conv3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Conv3DTranspose":
            change_parameter_with = "tf.keras.layers.Conv3DTranspose()"
            layer_name = "Conv3DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)                
        elif mutate_selected_parameters == "ConvLSTM1D":
            change_parameter_with = "tf.keras.layers.ConvLSTM1D()"
            layer_name = "ConvLSTM1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ConvLSTM2D":
            change_parameter_with = "tf.keras.layers.ConvLSTM2D()"
            layer_name = "ConvLSTM2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ConvLSTM3D":
            change_parameter_with = "tf.keras.layers.ConvLSTM3D()"
            layer_name = "ConvLSTM3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution1D":
            change_parameter_with = "tf.keras.layers.Convolution1D()"
            layer_name = "Convolution1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution1DTranspose":
            change_parameter_with = "tf.keras.layers.Convolution1DTranspose()"
            layer_name = "Convolution1DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution2D":
            change_parameter_with = "tf.keras.layers.Convolution2D()"
            layer_name = "Convolution2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution2DTranspose":
            change_parameter_with = "tf.keras.layers.Convolution2DTranspose()"
            layer_name = "Convolution2DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution3D":
            change_parameter_with = "tf.keras.layers.Convolution3D()"
            layer_name = "Convolution3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Convolution3DTranspose":
            change_parameter_with = "tf.keras.layers.Convolution3DTranspose()"
            layer_name = "Convolution3DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Cropping1D":
            change_parameter_with = "tf.keras.layers.Cropping1D()"
            layer_name = "Cropping1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Cropping2D":
            change_parameter_with = "tf.keras.layers.Cropping2D()"
            layer_name = "Cropping2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Cropping3D":
            change_parameter_with = "tf.keras.layers.Cropping3D()"
            layer_name = "Cropping3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "SpectralNormalization":
            change_parameter_with = "tf.keras.layers.SpectralNormalization()"
            layer_name = "SpectralNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "StackedRNNCells":
            change_parameter_with = "tf.keras.layers.StackedRNNCells()"
            layer_name = "StackedRNNCells"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "StringLookup":
            change_parameter_with = "tf.keras.layers.StringLookup()"
            layer_name = "StringLookup"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Subtract":
            change_parameter_with = "tf.keras.layers.Subtract()"
            layer_name = "Subtract"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "TextVectorization":
            change_parameter_with = "tf.keras.layers.TextVectorization()"
            layer_name = "TextVectorization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ThresholdedReLU":
            change_parameter_with = "tf.keras.layers.ThresholdedReLU()"
            layer_name = "ThresholdedReLU"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "TimeDistributed":
            change_parameter_with = "tf.keras.layers.TimeDistributed()"
            layer_name = "TimeDistributed"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "UnitNormalization":
            change_parameter_with = "tf.keras.layers.UnitNormalization()"
            layer_name = "UnitNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "UpSampling1D":
            change_parameter_with = "tf.keras.layers.UpSampling1D()"
            layer_name = "UpSampling1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "UpSampling2D":
            change_parameter_with = "tf.keras.layers.UpSampling2D()"
            layer_name = "UpSampling2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "UpSampling3D":
            change_parameter_with = "tf.keras.layers.UpSampling3D()"
            layer_name = "UpSampling3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "Wrapper":
            change_parameter_with = "tf.keras.layers.Wrapper()"
            layer_name = "Wrapper"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ZeroPadding1D":
            change_parameter_with = "tf.keras.layers.ZeroPadding1D()"
            layer_name = "ZeroPadding1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ZeroPadding2D":
            change_parameter_with = "tf.keras.layers.ZeroPadding2D()"
            layer_name = "ZeroPadding2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "ZeroPadding3D":
            change_parameter_with = "tf.keras.layers.ZeroPadding3D()"
            layer_name = "ZeroPadding3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)

        return mutated_line