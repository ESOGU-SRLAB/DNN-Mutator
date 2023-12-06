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
        elif mutate_selected_parameters == "layers.ConvLSTM1D()":
            change_parameter_with = "tf.keras.layers.ConvLSTM1D()"
            layer_name = "ConvLSTM1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ConvLSTM2D()":
            change_parameter_with = "tf.keras.layers.ConvLSTM2D()"
            layer_name = "ConvLSTM2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ConvLSTM3D()":
            change_parameter_with = "tf.keras.layers.ConvLSTM3D()"
            layer_name = "ConvLSTM3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution1D()":
            change_parameter_with = "tf.keras.layers.Convolution1D()"
            layer_name = "Convolution1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution1DTranspose()":
            change_parameter_with = "tf.keras.layers.Convolution1DTranspose()"
            layer_name = "Convolution1DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution2D()":
            change_parameter_with = "tf.keras.layers.Convolution2D()"
            layer_name = "Convolution2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution2DTranspose()":
            change_parameter_with = "tf.keras.layers.Convolution2DTranspose()"
            layer_name = "Convolution2DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution3D()":
            change_parameter_with = "tf.keras.layers.Convolution3D()"
            layer_name = "Convolution3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution3DTranspose()":
            change_parameter_with = "tf.keras.layers.Convolution3DTranspose()"
            layer_name = "Convolution3DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping1D()":
            change_parameter_with = "tf.keras.layers.Cropping1D()"
            layer_name = "Cropping1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping2D()":
            change_parameter_with = "tf.keras.layers.Cropping2D()"
            layer_name = "Cropping2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping3D()":
            change_parameter_with = "tf.keras.layers.Cropping3D()"
            layer_name = "Cropping3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.SpectralNormalization()":
            change_parameter_with = "tf.keras.layers.SpectralNormalization()"
            layer_name = "SpectralNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.StackedRNNCells()":
            change_parameter_with = "tf.keras.layers.StackedRNNCells()"
            layer_name = "StackedRNNCells"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.StringLookup()":
            change_parameter_with = "tf.keras.layers.StringLookup()"
            layer_name = "StringLookup"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Subtract()":
            change_parameter_with = "tf.keras.layers.Subtract()"
            layer_name = "Subtract"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.TextVectorization()":
            change_parameter_with = "tf.keras.layers.TextVectorization()"
            layer_name = "TextVectorization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ThresholdedReLU()":
            change_parameter_with = "tf.keras.layers.ThresholdedReLU()"
            layer_name = "ThresholdedReLU"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.TimeDistributed()":
            change_parameter_with = "tf.keras.layers.TimeDistributed()"
            layer_name = "TimeDistributed"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UnitNormalization()":
            change_parameter_with = "tf.keras.layers.UnitNormalization()"
            layer_name = "UnitNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UpSampling1D()":
            change_parameter_with = "tf.keras.layers.UpSampling1D()"
            layer_name = "UpSampling1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UpSampling2D()":
            change_parameter_with = "tf.keras.layers.UpSampling2D()"
            layer_name = "UpSampling2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UpSampling3D()":
            change_parameter_with = "tf.keras.layers.UpSampling3D()"
            layer_name = "UpSampling3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Wrapper()":
            change_parameter_with = "tf.keras.layers.Wrapper()"
            layer_name = "Wrapper"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding1D()":
            change_parameter_with = "tf.keras.layers.ZeroPadding1D()"
            layer_name = "ZeroPadding1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding2D()":
            change_parameter_with = "tf.keras.layers.ZeroPadding2D()"
            layer_name = "ZeroPadding2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding3D()":
            change_parameter_with = "tf.keras.layers.ZeroPadding3D()"
            layer_name = "ZeroPadding3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.add()":
            change_parameter_with = "tf.keras.layers.add()"
            layer_name = "add"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.average()":
            change_parameter_with = "tf.keras.layers.average()"
            layer_name = "average"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.concatenate()":
            change_parameter_with = "tf.keras.layers.concatenate()"
            layer_name = "concatenate"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.deserialize()":
            change_parameter_with = "tf.keras.layers.deserialize()"
            layer_name = "deserialize"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.dot()":
            change_parameter_with = "tf.keras.layers.dot()"
            layer_name = "dot"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.maximum()":
            change_parameter_with = "tf.keras.layers.maximum()"
            layer_name = "maximum"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.minimum()":
            change_parameter_with = "tf.keras.layers.minimum()"
            layer_name = "minimum"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.multiply()":
            change_parameter_with = "tf.keras.layers.multiply()"
            layer_name = "multiply"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.serialize()":
            change_parameter_with = "tf.keras.layers.serialize()"
            layer_name = "serialize"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.subtract()":
            change_parameter_with = "tf.keras.layers.subtract()"
            layer_name = "subtract"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.BinaryCrossentropy()":
            change_parameter_with = " tf.keras.losses.BinaryCrossentropy()"
            layer_name = "BinaryCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.BinaryFocalCrossentropy()":
            change_parameter_with = "tf.losses.BinaryFocalCrossentropy()"
            layer_name = "BinaryFocalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalCrossentropy()":
            change_parameter_with = "tf.losses.CategoricalCrossentropy()"
            layer_name = "CategoricalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalFocalCrossentropy()":
            change_parameter_with = "tf.losses.CategoricalFocalCrossentropy()"
            layer_name = "CategoricalFocalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalHinge()":
            change_parameter_with = "tf.losses.CategoricalHinge()"
            layer_name = "CategoricalHinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CosineSimilarity()":
            change_parameter_with = "tf.losses.CosineSimilarity()"
            layer_name = "CosineSimilarity"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Hinge()":
            change_parameter_with = "tf.losses.Hinge()"
            layer_name = "Hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Huber()":
            change_parameter_with = "tf.losses.Huber()"
            layer_name = "Huber"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLD()":
            change_parameter_with = "tf.losses.KLD()"
            layer_name = "KLD"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLDivergence()":
            change_parameter_with = "tf.losses.KLDivergence()"
            layer_name = "KLDivergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.LogCosh()":
            change_parameter_with = "tf.losses.LogCosh()"
            layer_name = "LogCosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Loss()":
            change_parameter_with = "tf.losses.Loss()"
            layer_name = "Loss"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAE()":
            change_parameter_with = "tf.losses.MAE()"
            layer_name = "MAE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAPE()":
            change_parameter_with = "tf.losses.MAPE()"
            layer_name = "MAPE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSE()":
            change_parameter_with = "tf.losses.MSE()"
            layer_name = "MSE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSLE()":
            change_parameter_with = "tf.losses.MSLE()"
            layer_name = "MSLE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        # ... (Diğer kayıp fonksiyonları için benzer bloklar eklenecek)
        elif mutate_selected_parameters == "losses.MeanAbsoluteError()":
            change_parameter_with = "tf.losses.MeanAbsoluteError()"
            layer_name = "MeanAbsoluteError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanAbsolutePercentageError()":
            change_parameter_with = "tf.losses.MeanAbsolutePercentageError()"
            layer_name = "MeanAbsolutePercentageError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredError()":
            change_parameter_with = "tf.losses.MeanSquaredError()"
            layer_name = "MeanSquaredError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredLogarithmicError()":
            change_parameter_with = "tf.losses.MeanSquaredLogarithmicError()"
            layer_name = "MeanSquaredLogarithmicError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Poisson()":
            change_parameter_with = "tf.losses.Poisson()"
            layer_name = "Poisson"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Reduction()":
            change_parameter_with = "tf.losses.Reduction()"
            layer_name = "Reduction"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SparseCategoricalCrossentropy()":
            change_parameter_with = "tf.losses.SparseCategoricalCrossentropy()"
            layer_name = "SparseCategoricalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SquaredHinge()":
            change_parameter_with = "tf.losses.SquaredHinge()"
            layer_name = "SquaredHinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.binary_crossentropy()":
            change_parameter_with = "tf.losses.binary_crossentropy()"
            layer_name = "binary_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.binary_focal_crossentropy()":
            change_parameter_with = "tf.losses.binary_focal_crossentropy()"
            layer_name = "binary_focal_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_crossentropy()":
            change_parameter_with = "tf.losses.categorical_crossentropy()"
            layer_name = "categorical_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_focal_crossentropy()":
            change_parameter_with = "tf.losses.categorical_focal_crossentropy()"
            layer_name = "categorical_focal_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_hinge()":
            change_parameter_with = "tf.losses.categorical_hinge()"
            layer_name = "categorical_hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.cosine_similarity()":
            change_parameter_with = "tf.losses.cosine_similarity()"
            layer_name = "cosine_similarity"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.deserialize()":
            change_parameter_with = "tf.losses.deserialize()"
            layer_name = "deserialize"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.get()":
            change_parameter_with = "tf.losses.get()"
            layer_name = "get"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.hinge()":
            change_parameter_with = "tf.losses.hinge()"
            layer_name = "hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.huber()":
            change_parameter_with = "tf.losses.huber()"
            layer_name = "huber"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kl_divergence()":
            change_parameter_with = "tf.losses.kl_divergence()"
            layer_name = "kl_divergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kld()":
            change_parameter_with = "tf.losses.kld()"
            layer_name = "kld"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kullback_leibler_divergence()":
            change_parameter_with = "tf.losses.kullback_leibler_divergence()"
            layer_name = "kullback_leibler_divergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.log_cosh()":
            change_parameter_with = "tf.losses.log_cosh()"
            layer_name = "log_cosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.logcosh()":
            change_parameter_with = "tf.losses.logcosh()"
            layer_name = "logcosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mae()":
            change_parameter_with = "tf.losses.mae()"
            layer_name = "mae"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mape()":
            change_parameter_with = "tf.losses.mape()"
            layer_name = "mape"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_error()":
            change_parameter_with = "tf.losses.mean_absolute_error()"
            layer_name = "mean_absolute_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_percentage_error()":
            change_parameter_with = "tf.losses.mean_absolute_percentage_error()"
            layer_name = "mean_absolute_percentage_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_error()":
            change_parameter_with = "tf.losses.mean_squared_error()"
            layer_name = "mean_squared_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_logarithmic_error()":
            change_parameter_with = "tf.losses.mean_squared_logarithmic_error()"
            layer_name = "mean_squared_logarithmic_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mse()":
            change_parameter_with = "tf.losses.mse()"
            layer_name = "mse"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.msle()":
            change_parameter_with = "tf.losses.msle()"
            layer_name = "msle"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.poisson()":
            change_parameter_with = "tf.losses.poisson()"
            layer_name = "poisson"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.serialize()":
            change_parameter_with = "tf.losses.serialize()"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.sparse_categorical_crossentropy()":
            change_parameter_with = "tf.losses.sparse_categorical_crossentropy()"
            layer_name = "sparse_categorical_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.squared_hinge()":
            change_parameter_with = "tf.losses.squared_hinge()"
            layer_name = "squared_hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        


        return mutated_line