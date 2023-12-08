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
        elif mutate_selected_parameters == "layers.AvgPool1D()":
            change_parameter_with = "tf.keras.layers.AvgPool1D()"
            layer_name = "AvgPool1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AvgPool2D()":
            change_parameter_with = "tf.keras.layers.AvgPool2D()"
            layer_name = "AvgPool2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AvgPool3D()":
            change_parameter_with = "tf.keras.layers.AvgPool3D()"
            layer_name = "AvgPool3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.BatchNormalization()":
            change_parameter_with = "tf.keras.layers.BatchNormalization()"
            layer_name = "BatchNormalization"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Bidirectional()":
            change_parameter_with = "tf.keras.layers.Bidirectional()"
            layer_name = "Bidirectional"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.CategoryEncoding()":
            change_parameter_with = "tf.keras.layers.CategoryEncoding()"
            layer_name = "CategoryEncoding"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.CenterCrop()":
            change_parameter_with = "tf.keras.layers.CenterCrop()"
            layer_name = "CenterCrop"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Concatenate()":
            change_parameter_with = "tf.keras.layers.Concatenate()"
            layer_name = "Concatenate"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv1D()":
            change_parameter_with = "tf.keras.layers.Conv1D()"
            layer_name = "Conv1D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv1DTranspose()":
            change_parameter_with = "tf.keras.layers.Conv1DTranspose()"
            layer_name = "Conv1DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv2D()":
            change_parameter_with = "tf.keras.layers.Conv2D()"
            layer_name = "Conv2D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv2DTranspose()":
            change_parameter_with = "tf.keras.layers.Conv2DTranspose()"
            layer_name = "Conv2DTranspose"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv3D()":
            change_parameter_with = "tf.keras.layers.Conv3D()"
            layer_name = "Conv3D"
            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv3DTranspose()":
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
            
            #losses

            mutated_line = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.BinaryCrossentropy()":
            change_parameter_with = " tf.keras.losses.BinaryCrossentropy()"
            layer_name = "BinaryCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.BinaryFocalCrossentropy()":
            change_parameter_with = "tf.keras.losses.BinaryFocalCrossentropy()"
            layer_name = "BinaryFocalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalCrossentropy()":
            change_parameter_with = "tf.keras.losses.CategoricalCrossentropy()"
            layer_name = "CategoricalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalFocalCrossentropy()":
            change_parameter_with = "tf.keras.losses.CategoricalFocalCrossentropy()"
            layer_name = "CategoricalFocalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalHinge()":
            change_parameter_with = "tf.keras.losses.CategoricalHinge()"
            layer_name = "CategoricalHinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CosineSimilarity()":
            change_parameter_with = "tf.keras.losses.CosineSimilarity()"
            layer_name = "CosineSimilarity"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Hinge()":
            change_parameter_with = "tf.keras.losses.Hinge()"
            layer_name = "Hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Huber()":
            change_parameter_with = "tf.keras.losses.Huber()"
            layer_name = "Huber"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLD()":
            change_parameter_with = "tf.keras.losses.KLD()"
            layer_name = "KLD"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLDivergence()":
            change_parameter_with = "tf.keras.losses.KLDivergence()"
            layer_name = "KLDivergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.LogCosh()":
            change_parameter_with = "tf.keras.losses.LogCosh()"
            layer_name = "LogCosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Loss()":
            change_parameter_with = "tf.keras.losses.Loss()"
            layer_name = "Loss"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAE()":
            change_parameter_with = "tf.keras.losses.MAE()"
            layer_name = "MAE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAPE()":
            change_parameter_with = "tf.keras.losses.MAPE()"
            layer_name = "MAPE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSE()":
            change_parameter_with = "tf.keras.losses.MSE()"
            layer_name = "MSE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSLE()":
            change_parameter_with = "tf.keras.losses.MSLE()"
            layer_name = "MSLE"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanAbsoluteError()":
            change_parameter_with = "tf.keras.losses.MeanAbsoluteError()"
            layer_name = "MeanAbsoluteError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanAbsolutePercentageError()":
            change_parameter_with = "tf.keras.losses.MeanAbsolutePercentageError()"
            layer_name = "MeanAbsolutePercentageError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredError()":
            change_parameter_with = "tf.keras.losses.MeanSquaredError()"
            layer_name = "MeanSquaredError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredLogarithmicError()":
            change_parameter_with = "tf.keras.losses.MeanSquaredLogarithmicError()"
            layer_name = "MeanSquaredLogarithmicError"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Poisson()":
            change_parameter_with = "tf.keras.losses.Poisson()"
            layer_name = "Poisson"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Reduction()":
            change_parameter_with = "tf.keras.losses.Reduction()"
            layer_name = "Reduction"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SparseCategoricalCrossentropy()":
            change_parameter_with = "tf.keras.losses.SparseCategoricalCrossentropy()"
            layer_name = "SparseCategoricalCrossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SquaredHinge()":
            change_parameter_with = "tf.keras.losses.SquaredHinge()"
            layer_name = "SquaredHinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.binary_crossentropy()":
            change_parameter_with = "tf.keras.losses.binary_crossentropy()"
            layer_name = "binary_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.binary_focal_crossentropy()":
            change_parameter_with = "tf.keras.losses.binary_focal_crossentropy()"
            layer_name = "binary_focal_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_crossentropy()":
            change_parameter_with = "tf.keras.losses.categorical_crossentropy()"
            layer_name = "categorical_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_focal_crossentropy()":
            change_parameter_with = "tf.keras.losses.categorical_focal_crossentropy()"
            layer_name = "categorical_focal_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.categorical_hinge()":
            change_parameter_with = "tf.keras.losses.categorical_hinge()"
            layer_name = "categorical_hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.cosine_similarity()":
            change_parameter_with = "tf.keras.losses.cosine_similarity()"
            layer_name = "cosine_similarity"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.deserialize()":
            change_parameter_with = "tf.keras.losses.deserialize()"
            layer_name = "deserialize"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.get()":
            change_parameter_with = "tf.keras.losses.get()"
            layer_name = "get"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.hinge()":
            change_parameter_with = "tf.keras.losses.hinge()"
            layer_name = "hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.huber()":
            change_parameter_with = "tf.keras.losses.huber()"
            layer_name = "huber"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kl_divergence()":
            change_parameter_with = "tf.keras.losses.kl_divergence()"
            layer_name = "kl_divergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kld()":
            change_parameter_with = "tf.keras.losses.kld()"
            layer_name = "kld"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kullback_leibler_divergence()":
            change_parameter_with = "tf.keras.losses.kullback_leibler_divergence()"
            layer_name = "kullback_leibler_divergence"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.log_cosh()":
            change_parameter_with = "tf.keras.losses.log_cosh()"
            layer_name = "log_cosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.logcosh()":
            change_parameter_with = "tf.keras.losses.logcosh()"
            layer_name = "logcosh"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mae()":
            change_parameter_with = "tf.keras.losses.mae()"
            layer_name = "mae"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mape()":
            change_parameter_with = "tf.keras.losses.mape()"
            layer_name = "mape"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_error()":
            change_parameter_with = "tf.keras.losses.mean_absolute_error()"
            layer_name = "mean_absolute_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_percentage_error()":
            change_parameter_with = "tf.keras.losses.mean_absolute_percentage_error()"
            layer_name = "mean_absolute_percentage_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_error()":
            change_parameter_with = "tf.keras.losses.mean_squared_error()"
            layer_name = "mean_squared_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_logarithmic_error()":
            change_parameter_with = "tf.keras.losses.mean_squared_logarithmic_error()"
            layer_name = "mean_squared_logarithmic_error"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mse()":
            change_parameter_with = "tf.keras.losses.mse()"
            layer_name = "mse"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.msle()":
            change_parameter_with = "tf.keras.losses.msle()"
            layer_name = "msle"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.poisson()":
            change_parameter_with = "tf.keras.losses.poisson()"
            layer_name = "poisson"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.serialize()":
            change_parameter_with = "tf.keras.losses.serialize()"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.sparse_categorical_crossentropy()":
            change_parameter_with = "tf.keras.losses.sparse_categorical_crossentropy()"
            layer_name = "sparse_categorical_crossentropy"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.squared_hinge()":
            change_parameter_with = "tf.keras.losses.squared_hinge()"
            layer_name = "squared_hinge"
            mutated_line = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        # optimizers

        elif mutate_selected_parameters == "optimizers.Adadelta()":
            change_parameter_with = "tf.keras.optimizers.Adadelta()"
            optimizer_name = "Adadelta"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adafactor()":
            change_parameter_with = "tf.keras.optimizers.Adafactor()"
            optimizer_name = "Adafactor"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adagrad()":
            change_parameter_with = "tf.keras.optimizers.Adagrad()"
            optimizer_name = "Adagrad"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adam()":
            change_parameter_with = "tf.keras.optimizers.Adam()"
            optimizer_name = "Adam"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adamax()":
            change_parameter_with = "tf.keras.optimizers.Adamax()"
            optimizer_name = "Adamax"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Ftrl()":
            change_parameter_with = "tf.keras.optimizers.Ftrl()"
            optimizer_name = "Ftrl"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Nadam()":
            change_parameter_with = "tf.keras.optimizers.Nadam()"
            optimizer_name = "Nadam"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.RMSprop()":
            change_parameter_with = "tf.keras.optimizers.RMSprop()"
            optimizer_name = "RMSprop"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.SGD()":
            change_parameter_with = "tf.keras.optimizers.SGD()"
            optimizer_name = "SGD"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.deserialize()":
            change_parameter_with = "tf.optimizers.deserialize()"
            optimizer_name = "deserialize"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)         
        elif mutate_selected_parameters == "optimizers.get()":
            change_parameter_with = "tf.optimizers.get()"
            optimizer_name = "get"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)         

        elif mutate_selected_parameters == "optimizers.legacy.Adadelta()":
            change_parameter_with = "tf.keras.optimizers.legacy.Adadelta()"
            optimizer_name = "Adadelta"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adagrad()":
            change_parameter_with = "tf.keras.optimizers.legacy.Adagrad()"
            optimizer_name = "Adagrad"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adam()":
            change_parameter_with = "tf.keras.optimizers.legacy.Adam()"
            optimizer_name = "Adam"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adamax()":
            change_parameter_with = "tf.keras.optimizers.legacy.Adamax()"
            optimizer_name = "Adamax"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Ftrl()":
            change_parameter_with = "tf.keras.optimizers.legacy.Ftrl()"
            optimizer_name = "Ftrl"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Nadam()":
            change_parameter_with = "tf.keras.optimizers.legacy.Nadam()"
            optimizer_name = "Nadam"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.RMSprop()":
            change_parameter_with = "tf.keras.optimizers.legacy.RMSprop()"
            optimizer_name = "RMSprop"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.SGD()":
            change_parameter_with = "tf.keras.optimizers.legacy.SGD()"
            optimizer_name = "SGD"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.CosineDecay()":
            change_parameter_with = "tf.keras.optimizers.schedules.CosineDecay()"
            optimizer_name = "CosineDecay"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.ExponentialDecay()":
            change_parameter_with = "tf.keras.optimizers.schedules.ExponentialDecay()"
            optimizer_name = "ExponentialDecay"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.PolynomialDecay()":
            change_parameter_with = "tf.keras.optimizers.schedules.PolynomialDecay()"
            optimizer_name = "schedules.PolynomialDecay"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.deserialize()":
            change_parameter_with = "tf.keras.optimizers.schedules.deserialize()"
            optimizer_name = "schedules.deserialize"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)       
        elif mutate_selected_parameters == "optimizers.schedules.serialize()":
            change_parameter_with = "tf.keras.optimizers.schedules.serialize()"
            optimizer_name = "schedules.serialize"
            mutated_line = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)   
        
        #tf.nn 


        elif mutate_selected_parameters == "nn.RNNCellDeviceWrapper":
            change_parameter_with = "tf.nn.RNNCellDeviceWrapper()"
            function_name = "RNNCellDeviceWrapper"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.RNNCellDropoutWrapper":
            change_parameter_with = "tf.nn.RNNCellDropoutWrapper()"
            function_name = "RNNCellDropoutWrapper"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.RNNCellResidualWrapper":
            change_parameter_with = "tf.nn.RNNCellResidualWrapper()"
            function_name = "RNNCellResidualWrapper"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.all_candidate_sampler":
            change_parameter_with = "tf.nn.all_candidate_sampler()"
            function_name = "all_candidate_sampler"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.approx_max_k":
            change_parameter_with = "tf.nn.approx_max_k()"
            function_name = "approx_max_k"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.approx_min_k":
            change_parameter_with = "tf.nn.approx_min_k()"
            function_name = "approx_min_k"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.atrous_conv2d":
            change_parameter_with = "tf.nn.atrous_conv2d()"
            function_name = "atrous_conv2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.atrous_conv2d_transpose":
            change_parameter_with = "tf.nn.atrous_conv2d_transpose()"
            function_name = "atrous_conv2d_transpose"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool":
            change_parameter_with = "tf.nn.avg_pool()"
            function_name = "avg_pool"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool1d":
            change_parameter_with = "tf.nn.avg_pool1d()"
            function_name = "avg_pool1d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool2d":
            change_parameter_with = "tf.nn.avg_pool2d()"
            function_name = "avg_pool2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool3d":
            change_parameter_with = "tf.nn.avg_pool3d()"
            function_name = "avg_pool3d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.batch_norm_with_global_normalization":
            change_parameter_with = "tf.nn.batch_norm_with_global_normalization()"
            function_name = "batch_norm_with_global_normalization"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.batch_normalization":
            change_parameter_with = "tf.nn.batch_normalization()"
            function_name = "batch_normalization"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.bias_add":
            change_parameter_with = "tf.nn.bias_add()"
            function_name = "bias_add"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.collapse_repeated":
            change_parameter_with = "tf.nn.collapse_repeated()"
            function_name = "collapse_repeated"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.compute_accidental_hits":
            change_parameter_with = "tf.nn.compute_accidental_hits()"
            function_name = "compute_accidental_hits"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.compute_average_loss":
            change_parameter_with = "tf.nn.compute_average_loss()"
            function_name = "compute_average_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv1d":
            change_parameter_with = "tf.nn.conv1d()"
            function_name = "conv1d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv1d_transpose":
            change_parameter_with = "tf.nn.conv1d_transpose()"
            function_name = "conv1d_transpose"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)


        elif mutate_selected_parameters == "nn.conv2d":
            change_parameter_with = "tf.nn.conv2d()"
            function_name = "conv2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv2d_transpose":
            change_parameter_with = "tf.nn.conv2d_transpose()"
            function_name = "conv2d_transpose"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv3d":
            change_parameter_with = "tf.nn.conv3d()"
            function_name = "conv3d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv3d_transpose":
            change_parameter_with = "tf.nn.conv3d_transpose()"
            function_name = "conv3d_transpose"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv_transpose":
            change_parameter_with = "tf.nn.conv_transpose()"
            function_name = "conv_transpose"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.convolution":
            change_parameter_with = "tf.nn.convolution()"
            function_name = "convolution"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.crelu":
            change_parameter_with = "tf.nn.crelu()"
            function_name = "crelu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_beam_search_decoder":
            change_parameter_with = "tf.nn.ctc_beam_search_decoder()"
            function_name = "ctc_beam_search_decoder"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_greedy_decoder":
            change_parameter_with = "tf.nn.ctc_greedy_decoder()"
            function_name = "ctc_greedy_decoder"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_loss":
            change_parameter_with = "tf.nn.ctc_loss()"
            function_name = "ctc_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_unique_labels":
            change_parameter_with = "tf.nn.ctc_unique_labels()"
            function_name = "ctc_unique_labels"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depth_to_space":
            change_parameter_with = "tf.nn.depth_to_space()"
            function_name = "depth_to_space"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d":
            change_parameter_with = "tf.nn.depthwise_conv2d()"
            function_name = "depthwise_conv2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d_backprop_filter":
            change_parameter_with = "tf.nn.depthwise_conv2d_backprop_filter()"
            function_name = "depthwise_conv2d_backprop_filter"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d_backprop_input":
            change_parameter_with = "tf.nn.depthwise_conv2d_backprop_input()"
            function_name = "depthwise_conv2d_backprop_input"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.dilation2d":
            change_parameter_with = "tf.nn.dilation2d()"
            function_name = "dilation2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.dropout":
            change_parameter_with = "tf.nn.dropout()"
            function_name = "dropout"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.elu":
            change_parameter_with = "tf.nn.elu()"
            function_name = "elu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.embedding_lookup":
            change_parameter_with = "tf.nn.embedding_lookup()"
            function_name = "embedding_lookup"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.embedding_lookup_sparse":
            change_parameter_with = "tf.nn.embedding_lookup_sparse()"
            function_name = "embedding_lookup_sparse"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.erosion2d":
            change_parameter_with = "tf.nn.erosion2d()"
            function_name = "erosion2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.fixed_unigram_candidate_sampler":
            change_parameter_with = "tf.nn.fixed_unigram_candidate_sampler()"
            function_name = "fixed_unigram_candidate_sampler"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
# ...

        elif mutate_selected_parameters == "nn.fractional_avg_pool":
            change_parameter_with = "tf.nn.fractional_avg_pool()"
            function_name = "fractional_avg_pool"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.fractional_max_pool":
            change_parameter_with = "tf.nn.fractional_max_pool()"
            function_name = "fractional_max_pool"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.gelu":
            change_parameter_with = "tf.nn.gelu()"
            function_name = "gelu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.in_top_k":
            change_parameter_with = "tf.nn.in_top_k()"
            function_name = "in_top_k"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.isotonic_regression":
            change_parameter_with = "tf.nn.isotonic_regression()"
            function_name = "isotonic_regression"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.l2_loss":
            change_parameter_with = "tf.nn.l2_loss()"
            function_name = "l2_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.l2_normalize":
            change_parameter_with = "tf.nn.l2_normalize()"
            function_name = "l2_normalize"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.leaky_relu":
            change_parameter_with = "tf.nn.leaky_relu()"
            function_name = "leaky_relu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.learned_unigram_candidate_sampler":
            change_parameter_with = "tf.nn.learned_unigram_candidate_sampler()"
            function_name = "learned_unigram_candidate_sampler"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.local_response_normalization":
            change_parameter_with = "tf.nn.local_response_normalization()"
            function_name = "local_response_normalization"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.log_poisson_loss":
            change_parameter_with = "tf.nn.log_poisson_loss()"
            function_name = "log_poisson_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.log_softmax":
            change_parameter_with = "tf.nn.log_softmax()"
            function_name = "log_softmax"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.lrn":
            change_parameter_with = "tf.nn.lrn()"
            function_name = "lrn"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool":
            change_parameter_with = "tf.nn.max_pool()"
            function_name = "max_pool"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool1d":
            change_parameter_with = "tf.nn.max_pool1d()"
            function_name = "max_pool1d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool2d":
            change_parameter_with = "tf.nn.max_pool2d()"
            function_name = "max_pool2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)

        elif mutate_selected_parameters == "nn.max_pool3d":
            change_parameter_with = "tf.nn.max_pool3d()"
            function_name = "max_pool3d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool_with_argmax":
            change_parameter_with = "tf.nn.max_pool_with_argmax()"
            function_name = "max_pool_with_argmax"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.moments":
            change_parameter_with = "tf.nn.moments()"
            function_name = "moments"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.nce_loss":
            change_parameter_with = "tf.nn.nce_loss()"
            function_name = "nce_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.normalize_moments":
            change_parameter_with = "tf.nn.normalize_moments()"
            function_name = "normalize_moments"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.pool":
            change_parameter_with = "tf.nn.pool()"
            function_name = "pool"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.relu":
            change_parameter_with = "tf.nn.relu()"
            function_name = "relu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.relu6":
            change_parameter_with = "tf.nn.relu6()"
            function_name = "relu6"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.safe_embedding_lookup_sparse":
            change_parameter_with = "tf.nn.safe_embedding_lookup_sparse()"
            function_name = "safe_embedding_lookup_sparse"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sampled_softmax_loss":
            change_parameter_with = "tf.nn.sampled_softmax_loss()"
            function_name = "sampled_softmax_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.scale_regularization_loss":
            change_parameter_with = "tf.nn.scale_regularization_loss()"
            function_name = "scale_regularization_loss"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.selu":
            change_parameter_with = "tf.nn.selu()"
            function_name = "selu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.separable_conv2d":
            change_parameter_with = "tf.nn.separable_conv2d()"
            function_name = "separable_conv2d"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sigmoid":
            change_parameter_with = "tf.nn.sigmoid()"
            function_name = "sigmoid"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sigmoid_cross_entropy_with_logits":
            change_parameter_with = "tf.nn.sigmoid_cross_entropy_with_logits()"
            function_name = "sigmoid_cross_entropy_with_logits"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.silu":
            change_parameter_with = "tf.nn.silu()"
            function_name = "silu"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softmax":
            change_parameter_with = "tf.nn.softmax()"
            function_name = "softmax"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softmax_cross_entropy_with_logits":
            change_parameter_with = "tf.nn.softmax_cross_entropy_with_logits()"
            function_name = "softmax_cross_entropy_with_logits"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softplus":
            change_parameter_with = "tf.nn.softplus()"
            function_name = "softplus"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softsign":
            change_parameter_with = "tf.nn.softsign()"
            function_name = "softsign"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.space_to_batch":
            change_parameter_with = "tf.nn.space_to_batch()"
            function_name = "space_to_batch"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.space_to_depth":
            change_parameter_with = "tf.nn.space_to_depth()"
            function_name = "space_to_depth"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sparse_softmax_cross_entropy_with_logits":
            change_parameter_with = "tf.nn.sparse_softmax_cross_entropy_with_logits()"
            function_name = "sparse_softmax_cross_entropy_with_logits"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sufficient_statistics":
            change_parameter_with = "tf.nn.sufficient_statistics()"
            function_name = "sufficient_statistics"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.swish":
            change_parameter_with = "tf.nn.swish()"
            function_name = "swish"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.tanh":
            change_parameter_with = "tf.nn.tanh()"
            function_name = "tanh"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.top_k":
            change_parameter_with = "tf.nn.top_k()"
            function_name = "top_k"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.weighted_cross_entropy_with_logits":
            change_parameter_with = "tf.nn.weighted_cross_entropy_with_logits()"
            function_name = "weighted_cross_entropy_with_logits"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.weighted_moments":
            change_parameter_with = "tf.nn.weighted_moments()"
            function_name = "weighted_moments"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.with_space_to_batch":
            change_parameter_with = "tf.nn.with_space_to_batch()"
            function_name = "with_space_to_batch"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.zero_fraction":
            change_parameter_with = "tf.nn.zero_fraction()"
            function_name = "zero_fraction"
            mutated_line = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)


        #raw_ops

        elif mutate_selected_parameters == "raw_ops.BlockLSTM":
            change_parameter_with = "tf.raw_ops.BlockLSTM()"
            function_name = "BlockLSTM"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMGrad":
            change_parameter_with = "tf.raw_ops.BlockLSTMGrad()"
            function_name = "BlockLSTMGrad"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMGradV2":
            change_parameter_with = "tf.raw_ops.BlockLSTMGradV2()"
            function_name = "BlockLSTMGradV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMV2":
            change_parameter_with = "tf.raw_ops.BlockLSTMV2()"
            function_name = "BlockLSTMV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BoostedTreesTrainingPredict":
            change_parameter_with = "tf.raw_ops.BoostedTreesTrainingPredict()"
            function_name = "BoostedTreesTrainingPredict"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CSRSparseMatrixToDense":
            change_parameter_with = "tf.raw_ops.CSRSparseMatrixToDense()"
            function_name = "CSRSparseMatrixToDense"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CTCLoss":
            change_parameter_with = "tf.raw_ops.CTCLoss()"
            function_name = "CTCLoss"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CTCLossV2":
            change_parameter_with = "tf.raw_ops.CTCLossV2()"
            function_name = "CTCLossV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv":
            change_parameter_with = "tf.raw_ops.Conv()"
            function_name = "Conv"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2D":
            change_parameter_with = "tf.raw_ops.Conv2D()"
            function_name = "Conv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropFilter":
            change_parameter_with = "tf.raw_ops.Conv2DBackpropFilter()"
            function_name = "Conv2DBackpropFilter"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropFilterV2":
            change_parameter_with = "tf.raw_ops.Conv2DBackpropFilterV2()"
            function_name = "Conv2DBackpropFilterV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropInput":
            change_parameter_with = "tf.raw_ops.Conv2DBackpropInput()"
            function_name = "Conv2DBackpropInput"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropInputV2":
            change_parameter_with = "tf.raw_ops.Conv2DBackpropInputV2()"
            function_name = "Conv2DBackpropInputV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3D":
            change_parameter_with = "tf.raw_ops.Conv3D()"
            function_name = "Conv3D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropFilter":
            change_parameter_with = "tf.raw_ops.Conv3DBackpropFilter()"
            function_name = "Conv3DBackpropFilter"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropFilterV2":
            change_parameter_with = "tf.raw_ops.Conv3DBackpropFilterV2()"
            function_name = "Conv3DBackpropFilterV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropInput":
            change_parameter_with = "tf.raw_ops.Conv3DBackpropInput()"
            function_name = "Conv3DBackpropInput"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropInputV2":
            change_parameter_with = "tf.raw_ops.Conv3DBackpropInputV2()"
            function_name = "Conv3DBackpropInputV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)

        elif mutate_selected_parameters == "raw_ops.CudnnRNN":
            change_parameter_with = "tf.raw_ops.CudnnRNN()"
            function_name = "CudnnRNN"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackprop":
            change_parameter_with = "tf.raw_ops.CudnnRNNBackprop()"
            function_name = "CudnnRNNBackprop"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackpropV2":
            change_parameter_with = "tf.raw_ops.CudnnRNNBackpropV2()"
            function_name = "CudnnRNNBackpropV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackpropV3":
            change_parameter_with = "tf.raw_ops.CudnnRNNBackpropV3()"
            function_name = "CudnnRNNBackpropV3"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNCanonicalToParams":
            change_parameter_with = "tf.raw_ops.CudnnRNNCanonicalToParams()"
            function_name = "CudnnRNNCanonicalToParams"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNCanonicalToParamsV2":
            change_parameter_with = "tf.raw_ops.CudnnRNNCanonicalToParamsV2()"
            function_name = "CudnnRNNCanonicalToParamsV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsSize":
            change_parameter_with = "tf.raw_ops.CudnnRNNParamsSize()"
            function_name = "CudnnRNNParamsSize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsToCanonical":
            change_parameter_with = "tf.raw_ops.CudnnRNNParamsToCanonical()"
            function_name = "CudnnRNNParamsToCanonical"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsToCanonicalV2":
            change_parameter_with = "tf.raw_ops.CudnnRNNParamsToCanonicalV2()"
            function_name = "CudnnRNNParamsToCanonicalV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNV2":
            change_parameter_with = "tf.raw_ops.CudnnRNNV2()"
            function_name = "CudnnRNNV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNV3":
            change_parameter_with = "tf.raw_ops.CudnnRNNV3()"
            function_name = "CudnnRNNV3"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseBincount":
            change_parameter_with = "tf.raw_ops.DenseBincount()"
            function_name = "DenseBincount"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseCountSparseOutput":
            change_parameter_with = "tf.raw_ops.DenseCountSparseOutput()"
            function_name = "DenseCountSparseOutput"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToCSRSparseMatrix":
            change_parameter_with = "tf.raw_ops.DenseToCSRSparseMatrix()"
            function_name = "DenseToCSRSparseMatrix"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToDenseSetOperation":
            change_parameter_with = "tf.raw_ops.DenseToDenseSetOperation()"
            function_name = "DenseToDenseSetOperation"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToSparseBatchDataset":
            change_parameter_with = "tf.raw_ops.DenseToSparseBatchDataset()"
            function_name = "DenseToSparseBatchDataset"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToSparseSetOperation":
            change_parameter_with = "tf.raw_ops.DenseToSparseSetOperation()"
            function_name = "DenseToSparseSetOperation"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNative":
            change_parameter_with = "tf.raw_ops.DepthwiseConv2dNative()"
            function_name = "DepthwiseConv2dNative"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNativeBackpropFilter":
            change_parameter_with = "tf.raw_ops.DepthwiseConv2dNativeBackpropFilter()"
            function_name = "DepthwiseConv2dNativeBackpropFilter"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNativeBackpropInput":
            change_parameter_with = "tf.raw_ops.DepthwiseConv2dNativeBackpropInput()"
            function_name = "DepthwiseConv2dNativeBackpropInput"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.FusedPadConv2D":
            change_parameter_with = "tf.raw_ops.FusedPadConv2D()"
            function_name = "FusedPadConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.FusedResizeAndPadConv2D":
            change_parameter_with = "tf.raw_ops.FusedResizeAndPadConv2D()"
            function_name = "FusedResizeAndPadConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        # ...

        elif mutate_selected_parameters == "raw_ops.GRUBlockCell":
            change_parameter_with = "tf.raw_ops.GRUBlockCell()"
            function_name = "GRUBlockCell"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.GRUBlockCellGrad":
            change_parameter_with = "tf.raw_ops.GRUBlockCellGrad()"
            function_name = "GRUBlockCellGrad"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.L2Loss":
            change_parameter_with = "tf.raw_ops.L2Loss()"
            function_name = "L2Loss"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCell":
            change_parameter_with = "tf.raw_ops.LSTMBlockCell()"
            function_name = "LSTMBlockCell"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCellGrad":
            change_parameter_with = "tf.raw_ops.LSTMBlockCellGrad()"
            function_name = "LSTMBlockCellGrad"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2D":
            change_parameter_with = "tf.raw_ops.QuantizedConv2D()"
            function_name = "QuantizedConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndRelu()"
            function_name = "QuantizedConv2DAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndReluAndRequantize()"
            function_name = "QuantizedConv2DAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndRequantize()"
            function_name = "QuantizedConv2DAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DPerChannel":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DPerChannel()"
            function_name = "QuantizedConv2DPerChannel"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBias":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBias()"
            function_name = "QuantizedConv2DWithBias"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndRelu()"
            function_name = "QuantizedConv2DWithBiasAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndRequantize()"
            function_name = "QuantizedConv2DWithBiasAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasSignedSumAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSumAndRelu()"
            function_name = "QuantizedConv2DWithBiasSumAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasSumAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2D":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2D()"
            function_name = "QuantizedDepthwiseConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBias":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBias()"
            function_name = "QuantizedDepthwiseConv2DWithBias"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu()"
            function_name = "QuantizedDepthwiseConv2DWithBiasAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize()"
            function_name = "QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.RecvTPUEmbeddingActivations":
            change_parameter_with = "tf.raw_ops.RecvTPUEmbeddingActivations()"
            function_name = "RecvTPUEmbeddingActivations"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizer":
            change_parameter_with = "tf.raw_ops.SdcaOptimizer()"
            function_name = "SdcaOptimizer"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizerV2":
            change_parameter_with = "tf.raw_ops.SdcaOptimizerV2()"
            function_name = "SdcaOptimizerV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseAdd":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseAdd()"
            function_name = "SparseDenseCwiseAdd"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseDiv":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseDiv()"
            function_name = "SparseDenseCwiseDiv"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseMul":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseMul()"
            function_name = "SparseDenseCwiseMul"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)


            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseAdd":
            change_parameter_with = "tf.raw_ops.SparseTensorDenseAdd()"
            function_name = "SparseTensorDenseAdd"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseMatMul":
            change_parameter_with = "tf.raw_ops.SparseTensorDenseMatMul()"
            function_name = "SparseTensorDenseMatMul"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseToDense":
            change_parameter_with = "tf.raw_ops.SparseToDense()"
            function_name = "SparseToDense"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.TPUEmbeddingActivations":
            change_parameter_with = "tf.raw_ops.TPUEmbeddingActivations()"
            function_name = "TPUEmbeddingActivations"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolution":
            change_parameter_with = "tf.raw_ops.UniformQuantizedConvolution()"
            function_name = "UniformQuantizedConvolution"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolutionHybrid":
            change_parameter_with = "tf.raw_ops.UniformQuantizedConvolutionHybrid()"
            function_name = "UniformQuantizedConvolutionHybrid"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.RecvTPUEmbeddingActivations":
            change_parameter_with = "tf.raw_ops.RecvTPUEmbeddingActivations()"
            function_name = "RecvTPUEmbeddingActivations"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizer":
            change_parameter_with = "tf.raw_ops.SdcaOptimizer()"
            function_name = "SdcaOptimizer"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizerV2":
            change_parameter_with = "tf.raw_ops.SdcaOptimizerV2()"
            function_name = "SdcaOptimizerV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.L2Loss":
            change_parameter_with = "tf.raw_ops.L2Loss()"
            function_name = "L2Loss"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCell":
            change_parameter_with = "tf.raw_ops.LSTMBlockCell()"
            function_name = "LSTMBlockCell"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCellGrad":
            change_parameter_with = "tf.raw_ops.LSTMBlockCellGrad()"
            function_name = "LSTMBlockCellGrad"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2D":
            change_parameter_with = "tf.raw_ops.QuantizedConv2D()"
            function_name = "QuantizedConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndRelu()"
            function_name = "QuantizedConv2DAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndReluAndRequantize()"
            function_name = "QuantizedConv2DAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DAndRequantize()"
            function_name = "QuantizedConv2DAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DPerChannel":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DPerChannel()"
            function_name = "QuantizedConv2DPerChannel"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBias":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBias()"
            function_name = "QuantizedConv2DWithBias"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndRelu()"
            function_name = "QuantizedConv2DWithBiasAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasAndRequantize()"
            function_name = "QuantizedConv2DWithBiasAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasSignedSumAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSumAndRelu()"
            function_name = "QuantizedConv2DWithBiasSumAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize()"
            function_name = "QuantizedConv2DWithBiasSumAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2D":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2D()"
            function_name = "QuantizedDepthwiseConv2D"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)


# ...

        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBias":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBias()"
            function_name = "QuantizedDepthwiseConv2DWithBias"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu()"
            function_name = "QuantizedDepthwiseConv2DWithBiasAndRelu"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = "tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize()"
            function_name = "QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.RecvTPUEmbeddingActivations":
            change_parameter_with = "tf.raw_ops.RecvTPUEmbeddingActivations()"
            function_name = "RecvTPUEmbeddingActivations"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizer":
            change_parameter_with = "tf.raw_ops.SdcaOptimizer()"
            function_name = "SdcaOptimizer"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizerV2":
            change_parameter_with = "tf.raw_ops.SdcaOptimizerV2()"
            function_name = "SdcaOptimizerV2"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseAdd":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseAdd()"
            function_name = "SparseDenseCwiseAdd"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseDiv":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseDiv()"
            function_name = "SparseDenseCwiseDiv"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseMul":
            change_parameter_with = "tf.raw_ops.SparseDenseCwiseMul()"
            function_name = "SparseDenseCwiseMul"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseAdd":
            change_parameter_with = "tf.raw_ops.SparseTensorDenseAdd()"
            function_name = "SparseTensorDenseAdd"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseMatMul":
            change_parameter_with = "tf.raw_ops.SparseTensorDenseMatMul()"
            function_name = "SparseTensorDenseMatMul"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseToDense":
            change_parameter_with = "tf.raw_ops.SparseToDense()"
            function_name = "SparseToDense"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.TPUEmbeddingActivations":
            change_parameter_with = "tf.raw_ops.TPUEmbeddingActivations()"
            function_name = "TPUEmbeddingActivations"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolution":
            change_parameter_with = "tf.raw_ops.UniformQuantizedConvolution()"
            function_name = "UniformQuantizedConvolution"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolutionHybrid":
            change_parameter_with = "tf.raw_ops.UniformQuantizedConvolutionHybrid()"
            function_name = "UniformQuantizedConvolutionHybrid"
            mutated_line = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)

        #train
        elif mutate_selected_parameters == "train.BytesList":
            change_parameter_with = "tf.train.BytesList()"
            class_name = "BytesList"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Checkpoint":
            change_parameter_with = "tf.train.Checkpoint()"
            class_name = "Checkpoint"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointManager":
            change_parameter_with = "tf.train.CheckpointManager()"
            class_name = "CheckpointManager"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointOptions":
            change_parameter_with = "tf.train.CheckpointOptions()"
            class_name = "CheckpointOptions"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointView":
            change_parameter_with = "tf.train.CheckpointView()"
            class_name = "CheckpointView"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ClusterDef":
            change_parameter_with = "tf.train.ClusterDef()"
            class_name = "ClusterDef"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ClusterSpec":
            change_parameter_with = "tf.train.ClusterSpec()"
            class_name = "ClusterSpec"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Coordinator":
            change_parameter_with = "tf.train.Coordinator()"
            class_name = "Coordinator"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Example":
            change_parameter_with = "tf.train.Example()"
            class_name = "Example"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ExponentialMovingAverage":
            change_parameter_with = "tf.train.ExponentialMovingAverage()"
            class_name = "ExponentialMovingAverage"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Feature":
            change_parameter_with = "tf.train.Feature()"
            class_name = "Feature"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.FeatureList":
            change_parameter_with = "tf.train.FeatureList()"
            class_name = "FeatureList"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.FeatureLists":
            change_parameter_with = "tf.train.FeatureLists()"
            class_name = "FeatureLists"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Features":
            change_parameter_with = "tf.train.Features()"
            class_name = "Features"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.FloatList":
            change_parameter_with = "tf.train.FloatList()"
            class_name = "FloatList"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Int64List":
            change_parameter_with = "tf.train.Int64List()"
            class_name = "Int64List"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.JobDef":
            change_parameter_with = "tf.train.JobDef()"
            class_name = "JobDef"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.SequenceExample":
            change_parameter_with = "tf.train.SequenceExample()"
            class_name = "SequenceExample"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ServerDef":
            change_parameter_with = "tf.train.ServerDef()"
            class_name = "ServerDef"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.TrackableView":
            change_parameter_with = "tf.train.TrackableView()"
            class_name = "TrackableView"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.checkpoints_iterator":
            change_parameter_with = "tf.train.checkpoints_iterator()"
            function_name = "checkpoints_iterator"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.experimental":
            change_parameter_with = "tf.train.experimental()"
            class_name = "experimental"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.experimental.PythonState":
            change_parameter_with = "tf.train.experimental.PythonState()"
            class_name = "experimental.PythonState"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.get_checkpoint_state":
            change_parameter_with = "tf.train.get_checkpoint_state()"
            function_name = "get_checkpoint_state"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.latest_checkpoint":
            change_parameter_with = "tf.train.latest_checkpoint()"
            function_name = "latest_checkpoint"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.list_variables":
            change_parameter_with = "tf.train.list_variables()"
            function_name = "list_variables"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.load_checkpoint":
            change_parameter_with = "tf.train.load_checkpoint()"
            function_name = "load_checkpoint"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.load_variable":
            change_parameter_with = "tf.train.load_variable()"
            function_name = "load_variable"
            mutated_line = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        # ... ve böyle devam eder. Diğer tf.train sınıf ve fonksiyonları için de benzer bloklar eklenebilir.
        


        return mutated_line