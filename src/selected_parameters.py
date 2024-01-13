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
import mutation_library
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
        layer_name=""
        matches=[]
        change_parameter_with=[]
        if mutate_selected_parameters == "epochs":
            change_parameter_with = 180
            mutated_line,matches = mutator.modify_code_in_file_epoch(source_code, mutate_selected_parameters, change_parameter_with)
        elif mutate_selected_parameters == "activation":
            change_parameter_with = mutation_library.tf_keras_layers_Activation_Full_List
            mutated_line,matches = mutator.modify_tf_activation_in_code(source_code, mutate_selected_parameters, change_parameter_with)
            layer_name="activation"
        elif mutate_selected_parameters == "optimizer":
            change_parameter_with = mutation_library.tf_optimizers_list
            mutated_line,matches= mutator.replace_optimizer_in_code(source_code, change_parameter_with)
        elif mutate_selected_parameters == "batch_size":
            change_parameter_with = mutation_library.tf_batch_size_list
            mutated_line,matches = mutator.replace_batch_size_in_code(source_code, change_parameter_with)
        elif mutate_selected_parameters == "kernel_regularizer":
            change_parameter_with = mutation_library.tf_kernel_regularizer_configurations
            mutated_line,matches = mutator.kernel_regularizer_in_code(source_code, change_parameter_with)        
        elif mutate_selected_parameters == "loss":
            change_parameter_with = mutation_library.tf_loss_functions_list
            mutated_line,matches = mutator.replace_loss_in_code(source_code, change_parameter_with)
        elif mutate_selected_parameters == "Dense(":
            change_parameter_with = mutation_library.tf_dense_list
            mutated_line,matches = mutator.replace_Dense_in_code(source_code, change_parameter_with)
        elif mutate_selected_parameters == "kernel_initializer":
            change_parameter_with = mutation_library.tf_keras_kernel_initializer_list
            mutated_line,matches= mutator.replace_kernel_initializer(source_code, change_parameter_with)
        elif mutate_selected_parameters == "dropout":
            change_parameter_with = mutation_library.tf_dropout_rate_list
            mutated_line,matches= mutator.modify_tf_dropout_in_code(source_code, change_parameter_with)            
        elif mutate_selected_parameters == "use_bias":
            change_parameter_with = mutation_library.tf_keras_use_bias_list
            mutated_line,matches= mutator.modify_tf_use_bias_in_code(source_code, mutate_selected_parameters, change_parameter_with)
        elif mutate_selected_parameters == "kernel_size":
            change_parameter_with = mutation_library.tf_kernel_size_list
            mutated_line,matches = mutator.replace_kernel_size_in_code(source_code, change_parameter_with)
        elif mutate_selected_parameters == "learning_rate":
            change_parameter_with = mutation_library.tf_learning_rate_list
            mutated_line,matches = mutator.modify_tf_learning_rate_in_code(source_code, mutate_selected_parameters, change_parameter_with)
        elif mutate_selected_parameters == "input_shape":
            change_parameter_with = mutation_library.tf_input_shape_list
            mutated_line,matches = mutator.replace_input_shape(source_code, change_parameter_with)                       
        elif mutate_selected_parameters == "layers.AbstractRNNCell()":
            change_parameter_with = mutation_library.tf_keras_layers_AbstractRNNCell_Mutation_List
            layer_name="AbstractRNNCell"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Activation()":
            change_parameter_with = mutation_library.tf_keras_layers_Activation_Full_List
            layer_name="Activation"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ActivityRegularization()":
            change_parameter_with = mutation_library.tf_keras_layers_ActivityRegularization_Mutation_List
            layer_name="ActivityRegularization"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AlphaDropout()":
            change_parameter_with = mutation_library.tf_keras_layers_AlphaDropout_Mutation_List
            layer_name="AlphaDropout"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Average()":
            change_parameter_with = mutation_library.tf_keras_layers_average_Mutation_List
            layer_name="Average"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AveragePooling1D()":
            change_parameter_with = mutation_library.tf_keras_layers_AveragePooling1D_Mutation_List
            layer_name="AveragePooling1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)                              
        elif mutate_selected_parameters == "layers.AveragePooling2D()":
            change_parameter_with = mutation_library.tf_keras_layers_AveragePooling2D_Mutation_List
            layer_name="AveragePooling2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AveragePooling3D()":
            change_parameter_with = mutation_library.tf_keras_layers_AveragePooling3D_Mutation_List
            layer_name="AveragePooling3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code,layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AvgPool1D()":
            change_parameter_with = mutation_library.tf_keras_layers_AvgPool1D_Mutation_List
            layer_name = "AvgPool1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AvgPool2D()":
            change_parameter_with = mutation_library.tf_keras_layers_AvgPool2D_Mutation_List
            layer_name = "AvgPool2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AvgPool3D()":
            change_parameter_with = mutation_library.tf_keras_layers_AvgPool3D_Mutation_List
            layer_name = "AvgPool3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.BatchNormalization()":
            change_parameter_with = mutation_library.tf_keras_layers_BatchNormalization_Mutation_List
            layer_name = "BatchNormalization"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Bidirectional()":
            change_parameter_with = mutation_library.tf_keras_layers_Bidirectional_Mutation_List
            layer_name = "Bidirectional"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.CategoryEncoding()":
            change_parameter_with = mutation_library.tf_keras_layers_CategoryEncoding_Mutation_List
            layer_name = "CategoryEncoding"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.CenterCrop()":
            change_parameter_with = mutation_library.tf_keras_layers_CenterCrop_Mutation_List
            layer_name = "CenterCrop"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Concatenate()":
            change_parameter_with = mutation_library.tf_keras_layers_Concatenate_Mutation_List
            layer_name = "Concatenate"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv1D()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv1D_Mutation_List
            layer_name = "Conv1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv1DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv1DTranspose_Mutation_List
            layer_name = "Conv1DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv2D()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv2D_Mutation_List
            layer_name = "Conv2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv2DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv2DTranspose_Mutation_List
            layer_name = "Conv2DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv3D()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv3D_Mutation_List
            layer_name = "Conv3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Conv3DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Conv3DTranspose_Mutation_List
            layer_name = "Conv3DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)                
        elif mutate_selected_parameters == "layers.ConvLSTM1D()":
            change_parameter_with = mutation_library.tf_keras_layers_ConvLSTM1D_Mutation_List
            layer_name = "ConvLSTM1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ConvLSTM2D()":
            change_parameter_with = mutation_library.tf_keras_layers_ConvLSTM2D_Mutation_List
            layer_name = "ConvLSTM2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ConvLSTM3D()":
            change_parameter_with = mutation_library.tf_keras_layers_ConvLSTM3D_Mutation_List
            layer_name = "ConvLSTM3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution1D()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution1D_Mutation_List
            layer_name = "Convolution1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution1DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution1DTranspose_Mutation_List
            layer_name = "Convolution1DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution2D()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution2D_Mutation_List
            layer_name = "Convolution2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution2DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution2DTranspose_Mutation_List
            layer_name = "Convolution2DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution3D()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution3D_Mutation_List
            layer_name = "Convolution3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Convolution3DTranspose()":
            change_parameter_with = mutation_library.tf_keras_layers_Convolution3DTranspose_Mutation_List
            layer_name = "Convolution3DTranspose"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping1D()":
            change_parameter_with = mutation_library.tf_keras_layers_Cropping1D_Mutation_List
            layer_name = "Cropping1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping2D()":
            change_parameter_with = mutation_library.tf_keras_layers_Cropping2D_Mutation_List
            layer_name = "Cropping2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Cropping3D()":
            change_parameter_with = mutation_library.tf_keras_layers_Cropping3D_Mutation_List
            layer_name = "Cropping3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.SpectralNormalization()":
            change_parameter_with = mutation_library.tf_keras_layers_SpectralNormalization_Mutation_List
            layer_name = "SpectralNormalization"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.StackedRNNCells()":
            change_parameter_with = mutation_library.tf_keras_layers_StackedRNNCells_Mutation_List
            layer_name = "StackedRNNCells"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.StringLookup()":
            change_parameter_with = mutation_library.tf_keras_layers_StringLookup_Mutation_List
            layer_name = "StringLookup"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Subtract()":
            change_parameter_with = mutation_library.tf_keras_layers_Subtract_Mutation_List
            layer_name = "Subtract"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.TextVectorization()":
            change_parameter_with = mutation_library.tf_keras_layers_TextVectorization_Mutation_List
            layer_name = "TextVectorization"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ThresholdedReLU()":
            change_parameter_with = mutation_library.tf_keras_layers_ThresholdedReLU_Mutation_List
            layer_name = "ThresholdedReLU"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.TimeDistributed()":
            change_parameter_with = mutation_library.tf_keras_layers_TimeDistributed_Mutation_List
            layer_name = "TimeDistributed"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UnitNormalization()":
            change_parameter_with = mutation_library.tf_keras_layers_UnitNormalization_Mutation_List
            layer_name = "UnitNormalization"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "tf.keras.layers.Dense()":
            change_parameter_with = mutation_library.tf_keras_layers_Dense_Mutation_List
            layer_name = "Dense"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)            
        elif mutate_selected_parameters == "layers.UpSampling1D()":
            change_parameter_with = mutation_library.tf_keras_layers_UpSampling1D_Mutation_List
            layer_name = "UpSampling1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UpSampling2D()":
            change_parameter_with = mutation_library.tf_keras_layers_UpSampling2D_Mutation_List
            layer_name = "UpSampling2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.UpSampling3D()":
            change_parameter_with = mutation_library.tf_keras_layers_UpSampling3D_Mutation_List
            layer_name = "UpSampling3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.Wrapper()":
            change_parameter_with = mutation_library.tf_keras_layers_Wrapper_Mutation_List
            layer_name = "Wrapper"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding1D()":
            change_parameter_with = mutation_library.tf_keras_layers_ZeroPadding1D_Mutation_List
            layer_name = "ZeroPadding1D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding2D()":
            change_parameter_with = mutation_library.tf_keras_layers_ZeroPadding2D_Mutation_List
            layer_name = "ZeroPadding2D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.ZeroPadding3D()":
            change_parameter_with = mutation_library.tf_keras_layers_ZeroPadding3D_Mutation_List
            layer_name = "ZeroPadding3D"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.add()":
            change_parameter_with = mutation_library.tf_keras_layers_add_Mutation_List
            layer_name = "add"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.AdditiveAttention()":
            change_parameter_with = mutation_library.tf_keras_layers_AdditiveAttention_Mutation_List
            layer_name = "AdditiveAttention"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.average()":
            change_parameter_with = mutation_library.tf_keras_layers_average_Mutation_List
            layer_name = "average"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.concatenate()":
            change_parameter_with = mutation_library.tf_keras_layers_concatenate_Mutation_List
            layer_name = "concatenate"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.deserialize()":
            change_parameter_with = mutation_library.tf_keras_layers_deserialize_Mutation_List
            layer_name = "deserialize"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.dot()":
            change_parameter_with = mutation_library.tf_keras_layers_deserialize_Mutation_List
            layer_name = "dot"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.maximum()":
            change_parameter_with = mutation_library.tf_keras_layers_maximum_Mutation_List
            layer_name = "maximum"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.minimum()":
            change_parameter_with = mutation_library.tf_keras_layers_minimum_Mutation_List
            layer_name = "minimum"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.multiply()":
            change_parameter_with = mutation_library.tf_keras_layers_multiply_Mutation_List
            layer_name = "multiply"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.serialize()":
            change_parameter_with = mutation_library.tf_keras_layers_serialize_Mutation_List
            layer_name = "serialize"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "layers.subtract()":
            change_parameter_with = mutation_library.tf_keras_layers_subtract_Mutation_List
            layer_name = "subtract"
            mutated_line,matches = mutator.modify_tf_layer_in_code(source_code, layer_name, change_parameter_with)            
           
   #activations   


        elif mutate_selected_parameters == "activations.deserialize()":
            change_parameter_with = mutation_library.tf_keras_activations_deserialize_Mutation_List
            function_name = "deserialize"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.elu()":
            change_parameter_with = mutation_library.tf_keras_activations_elu_Mutation_List
            function_name = "elu"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.exponential()":
            change_parameter_with = mutation_library.tf_keras_activations_exponential_Mutation_List
            function_name = "exponential"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.gelu()":
            change_parameter_with = mutation_library.tf_keras_activations_gelu_Mutation_List
            function_name = "gelu"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.get()":
            change_parameter_with = mutation_library.tf_keras_activations_get_Mutation_List
            function_name = "get"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.hard_sigmoid()":
            change_parameter_with = mutation_library.tf_keras_activations_hard_sigmoid_Mutation_List
            function_name = "hard_sigmoid"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.linear()":
            change_parameter_with = mutation_library.tf_keras_activations_linear_Mutation_List
            function_name = "linear"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.mish()":
            change_parameter_with = mutation_library.tf_keras_activations_mish_Mutation_List
            function_name = "mish"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.relu()":
            change_parameter_with = mutation_library.tf_keras_activations_relu_Mutation_List
            function_name = "relu"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.selu()":
            change_parameter_with = mutation_library.tf_keras_activations_selu_Mutation_List
            function_name = "selu"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.serialize()":
            change_parameter_with = mutation_library.tf_keras_activations_serialize_Mutation_List
            function_name = "serialize"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.sigmoid()":
            change_parameter_with = mutation_library.tf_keras_activations_sigmoid_Mutation_List
            function_name = "sigmoid"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.softmax()":
            change_parameter_with = mutation_library.tf_keras_activations_softmax_Mutation_List
            function_name = "softmax"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.softplus()":
            change_parameter_with = mutation_library.tf_keras_activations_softplus_Mutation_List
            function_name = "softplus"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.softsign()":
            change_parameter_with = mutation_library.tf_keras_activations_softsign_Mutation_List
            function_name = "softsign"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.swish()":
            change_parameter_with = mutation_library.tf_keras_activations_swish_Mutation_List
            function_name = "swish"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "activations.tanh()":
            change_parameter_with = mutation_library.tf_keras_activations_tanh_Mutation_List
            function_name = "tanh"
            mutated_line,matches = mutator.modify_tf_keras_activations_function_in_code(source_code, function_name, change_parameter_with)           
           
            #losses





        elif mutate_selected_parameters == "losses.BinaryCrossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_BinaryCrossentropy_Mutation_List
            layer_name = "BinaryCrossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.BinaryFocalCrossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_BinaryFocalCrossentropy_Mutation_List
            layer_name = "BinaryFocalCrossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalCrossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_CategoricalCrossentropy_Mutation_List
            layer_name = "CategoricalCrossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalFocalCrossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_CategoricalFocalCrossentropy_Mutation_List
            layer_name = "CategoricalFocalCrossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CategoricalHinge()":
            change_parameter_with = mutation_library.tf_keras_losses_CategoricalHinge_Mutation_List
            layer_name = "CategoricalHinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.CosineSimilarity()":
            change_parameter_with = mutation_library.tf_keras_losses_CosineSimilarity_Mutation_List
            layer_name = "CosineSimilarity"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Hinge()":
            change_parameter_with = mutation_library.tf_keras_losses_Hinge_Mutation_List
            layer_name = "Hinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Huber()":
            change_parameter_with = mutation_library.tf_keras_losses_Huber_Mutation_List
            layer_name = "Huber"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLD()":
            change_parameter_with = mutation_library.tf_keras_losses_KLD_Mutation_List
            layer_name = "KLD"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.KLDivergence()":
            change_parameter_with = mutation_library.tf_losses_KLDivergence_Mutation_List
            layer_name = "KLDivergence"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.LogCosh()":
            change_parameter_with = mutation_library.tf_keras_losses_LogCosh_Mutation_List
            layer_name = "LogCosh"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Loss()":
            change_parameter_with = mutation_library.tf_keras_losses_Loss_Mutation_List
            layer_name = "Loss"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAE()":
            change_parameter_with = mutation_library.tf_keras_losses_MAE_Mutation_List
            layer_name = "MAE"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MAPE()":
            change_parameter_with = mutation_library.tf_keras_losses_MAPE_Mutation_List
            layer_name = "MAPE"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSE()":
            change_parameter_with = mutation_library.tf_keras_losses_MSLE_Mutation_List
            layer_name = "MSE"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MSLE()":
            change_parameter_with = mutation_library.tf_keras_losses_MeanAbsoluteError_Mutation_List
            layer_name = "MSLE"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanAbsoluteError()":
            change_parameter_with = mutation_library.tf_keras_losses_MeanAbsoluteError_Mutation_List
            layer_name = "MeanAbsoluteError"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanAbsolutePercentageError()":
            change_parameter_with = mutation_library.tf_keras_losses_MeanAbsolutePercentageError_Mutation_List
            layer_name = "MeanAbsolutePercentageError"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredError()":
            change_parameter_with = mutation_library.tf_keras_losses_MeanSquaredError_Mutation_List
            layer_name = "MeanSquaredError"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.MeanSquaredLogarithmicError()":
            change_parameter_with = mutation_library.tf_keras_losses_MeanSquaredLogarithmicError_Mutation_List
            layer_name = "MeanSquaredLogarithmicError"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Poisson()":
            change_parameter_with = mutation_library.tf_keras_losses_Poisson_Mutation_List
            layer_name = "Poisson"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.Reduction()":
            change_parameter_with = mutation_library.tf_keras_losses_Reduction_Mutation_List
            layer_name = "Reduction"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SparseCategoricalCrossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_SparseCategoricalCrossentropy_Mutation_List
            layer_name = "SparseCategoricalCrossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.SquaredHinge()":
            change_parameter_with = mutation_library.tf_keras_losses_SquaredHinge_Mutation_List
            layer_name = "SquaredHinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.binary_crossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_binary_crossentropy_Mutation_List
            layer_name = "binary_crossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.binary_focal_crossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_binary_focal_crossentropy_Mutation_List
            layer_name = "binary_focal_crossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.categorical_crossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_categorical_crossentropy_Mutation_List
            layer_name = "categorical_crossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.categorical_focal_crossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_categorical_focal_crossentropy_Mutation_List
            layer_name = "categorical_focal_crossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.categorical_hinge()":
            change_parameter_with = mutation_library.tf_keras_losses_categorical_hinge_Mutation_List
            layer_name = "categorical_hinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.cosine_similarity()":
            change_parameter_with = mutation_library.tf_keras_losses_cosine_similarity_Mutation_List
            layer_name = "cosine_similarity"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        elif mutate_selected_parameters == "losses.deserialize()":
            change_parameter_with = mutation_library.tf_keras_losses_deserialize_Mutation_List
            layer_name = "deserialize"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.get()":
            change_parameter_with = mutation_library.tf_keras_losses_get_Mutation_List
            layer_name = "get"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.hinge()":
            change_parameter_with = mutation_library.tf_keras_losses_hinge_Mutation_List
            layer_name = "hinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.huber()":
            change_parameter_with = mutation_library.tf_keras_losses_huber_Mutation_List
            layer_name = "huber"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kl_divergence()":
            change_parameter_with = mutation_library.tf_keras_losses_kl_divergence_Mutation_List
            layer_name = "kl_divergence"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kld()":
            change_parameter_with = mutation_library.tf_keras_losses_kld_Mutation_List
            layer_name = "kld"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.kullback_leibler_divergence()":
            change_parameter_with = mutation_library.tf_keras_losses_kullback_leibler_divergence_Mutation_List
            layer_name = "kullback_leibler_divergence"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.log_cosh()":
            change_parameter_with = mutation_library.tf_keras_losses_log_cosh_Mutation_List
            layer_name = "log_cosh"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.logcosh()":
            change_parameter_with = mutation_library.tf_keras_losses_logcosh_Mutation_List
            layer_name = "logcosh"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mae()":
            change_parameter_with = mutation_library.tf_keras_losses_mae_Mutation_List
            layer_name = "mae"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mape()":
            change_parameter_with = mutation_library.tf_keras_losses_mape_Mutation_List
            layer_name = "mape"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_error()":
            change_parameter_with = mutation_library.tf_losses_mean_absolute_error_Mutation_List
            layer_name = "mean_absolute_error"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_absolute_percentage_error()":
            change_parameter_with = mutation_library.tf_keras_losses_mean_absolute_percentage_error_Mutation_List
            layer_name = "mean_absolute_percentage_error"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_error()":
            change_parameter_with = mutation_library.tf_keras_losses_mean_squared_error_Mutation_List
            layer_name = "mean_squared_error"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mean_squared_logarithmic_error()":
            change_parameter_with = mutation_library.tf_keras_losses_mean_squared_logarithmic_error_Mutation_List
            layer_name = "mean_squared_logarithmic_error"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.mse()":
            change_parameter_with = mutation_library.tf_keras_losses_mse_Mutation_List
            layer_name = "mse"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.msle()":
            change_parameter_with = mutation_library.tf_keras_losses_msle_Mutation_List
            layer_name = "msle"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.poisson()":
            change_parameter_with = mutation_library.tf_keras_losses_poisson_Mutation_List
            layer_name = "poisson"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.serialize()":
            change_parameter_with = mutation_library.tf_keras_losses_serialize_Mutation_List
            layer_name="serialize"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.sparse_categorical_crossentropy()":
            change_parameter_with = mutation_library.tf_keras_losses_sparse_categorical_crossentropy_Mutation_List
            layer_name = "sparse_categorical_crossentropy"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        elif mutate_selected_parameters == "losses.squared_hinge()":
            change_parameter_with = mutation_library.tf_keras_losses_squared_hinge_Mutation_List
            layer_name = "squared_hinge"
            mutated_line,matches = mutator.modify_tf_losses_in_code(source_code, layer_name, change_parameter_with)
        
        # optimizers

        elif mutate_selected_parameters == "optimizers.Adadelta()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Adadelta_Mutation_List
            optimizer_name = "Adadelta"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adafactor()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Adafactor_Mutation_List
            optimizer_name = "Adafactor"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adagrad()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Adagrad_Mutation_List
            optimizer_name = "Adagrad"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adam()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Adam_Mutation_List
            optimizer_name = "Adam"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Adamax()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Adamax_Mutation_List
            optimizer_name = "Adamax"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Ftrl()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Ftrl_Mutation_List
            optimizer_name = "Ftrl"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.Nadam()":
            change_parameter_with = mutation_library.tf_keras_optimizers_Nadam_Mutation_List
            optimizer_name = "Nadam"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.RMSprop()":
            change_parameter_with = mutation_library.tf_keras_optimizers_RMSprop_Mutation_List
            optimizer_name = "RMSprop"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.SGD()":
            change_parameter_with = mutation_library.tf_keras_optimizers_SGD_Mutation_List
            optimizer_name = "SGD"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.deserialize()":
            change_parameter_with = mutation_library.tf_optimizers_deserialize_Mutation_List
            optimizer_name = "deserialize"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)         
        elif mutate_selected_parameters == "optimizers.get()":
            change_parameter_with = mutation_library.tf_optimizers_get_Mutation_List
            optimizer_name = "get"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)         

        elif mutate_selected_parameters == "optimizers.legacy.Adadelta()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Adadelta_Mutation_List
            optimizer_name = "Adadelta"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adagrad()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Adagrad_Mutation_List
            optimizer_name = "Adagrad"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adam()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Adam_Mutation_List
            optimizer_name = "Adam"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Adamax()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Adamax_Mutation_List
            optimizer_name = "Adamax"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Ftrl()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Ftrl_Mutation_List
            optimizer_name = "Ftrl"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.Nadam()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_Nadam_Mutation_List
            optimizer_name = "Nadam"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.RMSprop()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_RMSprop_Mutation_List
            optimizer_name = "RMSprop"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.legacy.SGD()":
            change_parameter_with = mutation_library.tf_keras_optimizers_legacy_SGD_Mutation_List
            optimizer_name = "SGD"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.CosineDecay()":
            change_parameter_with = mutation_library.tf_keras_optimizers_schedules_CosineDecay_Mutation_List
            optimizer_name = "CosineDecay"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.ExponentialDecay()":
            change_parameter_with = mutation_library.tf_keras_optimizers_schedules_ExponentialDecay_Mutation_List
            optimizer_name = "ExponentialDecay"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.PolynomialDecay()":
            change_parameter_with = mutation_library.tf_keras_optimizers_schedules_PolynomialDecay_Mutation_List
            optimizer_name = "schedules.PolynomialDecay"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)
        elif mutate_selected_parameters == "optimizers.schedules.deserialize()":
            change_parameter_with = mutation_library.tf_keras_optimizers_schedules_Deserialize_Mutation_List
            optimizer_name = "schedules.deserialize"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)       
        elif mutate_selected_parameters == "optimizers.schedules.serialize()":
            change_parameter_with = mutation_library.tf_keras_optimizers_schedules_Serialize_Mutation_List
            optimizer_name = "schedules.serialize"
            mutated_line,matches = mutator.modify_tf_optimizers_in_code(source_code, optimizer_name, change_parameter_with)   
        
        #tf.nn 


        elif mutate_selected_parameters == "nn.RNNCellDeviceWrapper":
            change_parameter_with = mutation_library.tf_nn_RNNCellDeviceWrapper_Mutation_List
            function_name = "RNNCellDeviceWrapper"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.RNNCellDropoutWrapper":
            change_parameter_with = mutation_library.tf_nn_RNNCellDropoutWrapper_Mutation_List
            function_name = "RNNCellDropoutWrapper"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.RNNCellResidualWrapper":
            change_parameter_with = mutation_library.tf_nn_RNNCellResidualWrapper_Mutation_List
            function_name = "RNNCellResidualWrapper"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.all_candidate_sampler":
            change_parameter_with = mutation_library.tf_nn_all_candidate_sampler_Mutation_List
            function_name = "all_candidate_sampler"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.approx_max_k":
            change_parameter_with = mutation_library.tf_nn_approx_max_k_Mutation_List
            function_name = "approx_max_k"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.approx_min_k":
            change_parameter_with = mutation_library.tf_nn_approx_min_k_Mutation_List
            function_name = "approx_min_k"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.atrous_conv2d":
            change_parameter_with = mutation_library.tf_nn_atrous_conv2d_Mutation_List
            function_name = "atrous_conv2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.atrous_conv2d_transpose":
            change_parameter_with = mutation_library.tf_nn_atrous_conv2d_transpose_Mutation_List
            function_name = "atrous_conv2d_transpose"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool":
            change_parameter_with = mutation_library.tf_nn_avg_pool_Mutation_List
            function_name = "avg_pool"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool1d":
            change_parameter_with = mutation_library.tf_nn_avg_pool1d_Mutation_List
            function_name = "avg_pool1d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool2d":
            change_parameter_with = mutation_library.tf_nn_avg_pool2d_Mutation_List
            function_name = "avg_pool2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.avg_pool3d":
            change_parameter_with = mutation_library.tf_nn_avg_pool3d_Mutation_List
            function_name = "avg_pool3d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.batch_norm_with_global_normalization":
            change_parameter_with = mutation_library.tf_nn_batch_norm_with_global_normalization_Mutation_List
            function_name = "batch_norm_with_global_normalization"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.batch_normalization":
            change_parameter_with = mutation_library.tf_nn_batch_normalization_Mutation_List
            function_name = "batch_normalization"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.bias_add":
            change_parameter_with = mutation_library.tf_nn_bias_add_Mutation_List
            function_name = "bias_add"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.collapse_repeated()":
            change_parameter_with = mutation_library.tf_nn_collapse_repeated_Mutation_List
            function_name = "collapse_repeated"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.compute_accidental_hits()":
            change_parameter_with = mutation_library.tf_nn_compute_accidental_hits_Mutation_List
            function_name = "compute_accidental_hits"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.compute_average_loss":
            change_parameter_with = mutation_library.tf_nn_compute_average_loss_Mutation_List
            function_name = "compute_average_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv1d":
            change_parameter_with = mutation_library.tf_nn_conv1d_Mutation_List
            function_name = "conv1d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv1d_transpose":
            change_parameter_with = mutation_library.tf_nn_conv1d_transpose_Mutation_List
            function_name = "conv1d_transpose"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)


        elif mutate_selected_parameters == "nn.conv2d":
            change_parameter_with = mutation_library.tf_nn_conv2d_Mutation_List
            function_name = "conv2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv2d_transpose":
            change_parameter_with = mutation_library.tf_nn_conv2d_transpose_Mutation_List
            function_name = "conv2d_transpose"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv3d":
            change_parameter_with = mutation_library.tf_nn_conv3d_Mutation_List
            function_name = "conv3d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv3d_transpose":
            change_parameter_with = mutation_library.tf_nn_conv3d_transpose_Mutation_List
            function_name = "conv3d_transpose"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.conv_transpose":
            change_parameter_with = mutation_library.tf_nn_conv_transpose_Mutation_List
            function_name = "conv_transpose"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.convolution":
            change_parameter_with = mutation_library.tf_nn_convolution_Mutation_List
            function_name = "convolution"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.crelu":
            change_parameter_with = mutation_library.tf_nn_crelu_Mutation_List
            function_name = "crelu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_beam_search_decoder":
            change_parameter_with = mutation_library.tf_nn_ctc_beam_search_decoder_Mutation_List
            function_name = "ctc_beam_search_decoder"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_greedy_decoder":
            change_parameter_with = mutation_library.tf_nn_ctc_greedy_decoder_Mutation_List
            function_name = "ctc_greedy_decoder"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_loss":
            change_parameter_with = mutation_library.tf_nn_ctc_loss_Mutation_List
            function_name = "ctc_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.ctc_unique_labels":
            change_parameter_with = mutation_library.tf_nn_ctc_unique_labels_Mutation_List
            function_name = "ctc_unique_labels"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depth_to_space":
            change_parameter_with = mutation_library.tf_nn_depth_to_space_Mutation_List
            function_name = "depth_to_space"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d":
            change_parameter_with = mutation_library.tf_nn_depthwise_conv2d_Mutation_List
            function_name = "depthwise_conv2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d_backprop_filter":
            change_parameter_with = mutation_library.tf_nn_depthwise_conv2d_backprop_filter_Mutation_List
            function_name = "depthwise_conv2d_backprop_filter"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.depthwise_conv2d_backprop_input":
            change_parameter_with = mutation_library.tf_nn_depthwise_conv2d_backprop_input_Mutation_List
            function_name = "depthwise_conv2d_backprop_input"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.dilation2d":
            change_parameter_with = mutation_library.tf_nn_dilation2d_Mutation_List
            function_name = "dilation2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.dropout":
            change_parameter_with = mutation_library.tf_nn_dropout_Mutation_List
            function_name = "dropout"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.elu":
            change_parameter_with = mutation_library.tf_nn_elu_Mutation_List
            function_name = "elu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.embedding_lookup":
            change_parameter_with = mutation_library.tf_nn_embedding_lookup_Mutation_List
            function_name = "embedding_lookup"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.embedding_lookup_sparse":
            change_parameter_with = mutation_library.tf_nn_embedding_lookup_sparse_Mutation_List
            function_name = "embedding_lookup_sparse"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.erosion2d":
            change_parameter_with = mutation_library.tf_nn_erosion2d_Mutation_List
            function_name = "erosion2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.fixed_unigram_candidate_sampler":
            change_parameter_with = mutation_library.tf_nn_fixed_unigram_candidate_sampler_Mutation_List
            function_name = "fixed_unigram_candidate_sampler"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
# ...

        elif mutate_selected_parameters == "nn.fractional_avg_pool":
            change_parameter_with = mutation_library.tf_nn_fractional_avg_pool_Mutation_List
            function_name = "fractional_avg_pool"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.fractional_max_pool":
            change_parameter_with = mutation_library.tf_nn_fractional_max_pool_Mutation_List
            function_name = "fractional_max_pool"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.gelu":
            change_parameter_with = mutation_library.tf_nn_gelu_Mutation_List
            function_name = "gelu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.in_top_k":
            change_parameter_with = mutation_library.tf_nn_in_top_k_Mutation_List
            function_name = "in_top_k"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.isotonic_regression":
            change_parameter_with = mutation_library.tf_nn_isotonic_regression_Mutation_List
            function_name = "isotonic_regression"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.l2_loss":
            change_parameter_with = mutation_library.tf_nn_l2_loss_Mutation_List
            function_name = "l2_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.l2_normalize":
            change_parameter_with = mutation_library.tf_nn_l2_normalize_Mutation_List
            function_name = "l2_normalize"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.leaky_relu":
            change_parameter_with = mutation_library.tf_nn_leaky_relu_Mutation_List
            function_name = "leaky_relu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.learned_unigram_candidate_sampler":
            change_parameter_with = mutation_library.tf_nn_learned_unigram_candidate_sampler_Mutation_List
            function_name = "learned_unigram_candidate_sampler"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.local_response_normalization":
            change_parameter_with = mutation_library.tf_nn_local_response_normalization_Mutation_List
            function_name = "local_response_normalization"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.log_poisson_loss":
            change_parameter_with = mutation_library.tf_nn_log_poisson_loss_Mutation_List
            function_name = "log_poisson_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.log_softmax":
            change_parameter_with = mutation_library.tf_nn_log_softmax_Mutation_List
            function_name = "log_softmax"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.lrn":
            change_parameter_with = mutation_library.tf_nn_lrn_Mutation_List
            function_name = "lrn"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool":
            change_parameter_with = mutation_library.tf_nn_max_pool_Mutation_List
            function_name = "max_pool"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool1d":
            change_parameter_with = mutation_library.tf_nn_max_pool1d_Mutation_List
            function_name = "max_pool1d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool2d":
            change_parameter_with = mutation_library.tf_nn_max_pool2d_Mutation_List
            function_name = "max_pool2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)

        elif mutate_selected_parameters == "nn.max_pool3d":
            change_parameter_with = mutation_library.tf_nn_max_pool3d_Mutation_List
            function_name = "max_pool3d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.max_pool_with_argmax":
            change_parameter_with = mutation_library.tf_nn_max_pool_with_argmax_Mutation_List
            function_name = "max_pool_with_argmax"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.moments":
            change_parameter_with = mutation_library.tf_nn_moments_Mutation_List
            function_name = "moments"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.nce_loss":
            change_parameter_with = mutation_library.tf_nn_nce_loss_Mutation_List
            function_name = "nce_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.normalize_moments":
            change_parameter_with = mutation_library.tf_nn_normalize_moments_Mutation_List
            function_name = "normalize_moments"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.pool":
            change_parameter_with = mutation_library.tf_nn_pool_Mutation_List
            function_name = "pool"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.relu":
            change_parameter_with = mutation_library.tf_nn_relu_Mutation_List
            function_name = "relu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.relu6":
            change_parameter_with = mutation_library.tf_nn_relu6_Mutation_List
            function_name = "relu6"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.safe_embedding_lookup_sparse":
            change_parameter_with = mutation_library.tf_nn_safe_embedding_lookup_sparse_Mutation_List
            function_name = "safe_embedding_lookup_sparse"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sampled_softmax_loss":
            change_parameter_with = mutation_library.tf_nn_sampled_softmax_loss_Mutation_List
            function_name = "sampled_softmax_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.scale_regularization_loss":
            change_parameter_with = mutation_library.tf_nn_scale_regularization_loss_Mutation_List
            function_name = "scale_regularization_loss"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.selu":
            change_parameter_with = mutation_library.tf_nn_selu_Mutation_List
            function_name = "selu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.separable_conv2d":
            change_parameter_with = mutation_library.tf_nn_separable_conv2d_Mutation_List
            function_name = "separable_conv2d"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sigmoid":
            change_parameter_with = mutation_library.tf_nn_sigmoid_Mutation_List
            function_name = "sigmoid"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sigmoid_cross_entropy_with_logits":
            change_parameter_with = mutation_library.tf_nn_sigmoid_cross_entropy_with_logits_Mutation_List
            function_name = "sigmoid_cross_entropy_with_logits"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.silu":
            change_parameter_with = mutation_library.tf_nn_silu_Mutation_List
            function_name = "silu"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softmax":
            change_parameter_with = mutation_library.tf_nn_softmax_Mutation_List
            function_name = "softmax"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softmax_cross_entropy_with_logits":
            change_parameter_with = mutation_library.tf_nn_softmax_cross_entropy_with_logits_Mutation_List
            function_name = "softmax_cross_entropy_with_logits"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softplus":
            change_parameter_with = mutation_library.tf_nn_softplus_Mutation_List
            function_name = "softplus"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.softsign":
            change_parameter_with = mutation_library.tf_nn_softsign_Mutation_List
            function_name = "softsign"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.space_to_batch":
            change_parameter_with = mutation_library.tf_nn_space_to_batch_Mutation_List
            function_name = "space_to_batch"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.space_to_depth":
            change_parameter_with = mutation_library.tf_nn_space_to_depth_Mutation_List
            function_name = "space_to_depth"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sparse_softmax_cross_entropy_with_logits":
            change_parameter_with = mutation_library.tf_nn_sparse_softmax_cross_entropy_with_logits_Mutation_List
            function_name = "sparse_softmax_cross_entropy_with_logits"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.sufficient_statistics":
            change_parameter_with = mutation_library.tf_nn_sufficient_statistics_Mutation_List
            function_name = "sufficient_statistics"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.swish":
            change_parameter_with = mutation_library.tf_nn_swish_Mutation_List
            function_name = "swish"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.tanh":
            change_parameter_with = mutation_library.tf_nn_tanh_Mutation_List
            function_name = "tanh"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.top_k":
            change_parameter_with = mutation_library.tf_nn_top_k_Mutation_List
            function_name = "top_k"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.weighted_cross_entropy_with_logits":
            change_parameter_with = mutation_library.tf_nn_weighted_cross_entropy_with_logits_Mutation_List
            function_name = "weighted_cross_entropy_with_logits"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.weighted_moments":
            change_parameter_with = mutation_library.tf_nn_weighted_moments_Mutation_List
            function_name = "weighted_moments"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.with_space_to_batch":
            change_parameter_with = mutation_library.tf_nn_with_space_to_batch_Mutation_List
            function_name = "with_space_to_batch"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "nn.zero_fraction":
            change_parameter_with = mutation_library.tf_nn_zero_fraction_Mutation_List
            function_name = "zero_fraction"
            mutated_line,matches = mutator.modify_tf_nn_function_in_code(source_code, function_name, change_parameter_with)


        #raw_ops

        elif mutate_selected_parameters == "raw_ops.BlockLSTM":
            change_parameter_with = mutation_library.tf_raw_ops_BlockLSTM_Mutation_List
            function_name = "BlockLSTM"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMGrad":
            change_parameter_with = mutation_library.tf_raw_ops_BlockLSTMGrad_Mutation_List
            function_name = "BlockLSTMGrad"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMGradV2":
            change_parameter_with = mutation_library.tf_raw_ops_BlockLSTMGradV2_Mutation_List
            function_name = "BlockLSTMGradV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BlockLSTMV2":
            change_parameter_with = mutation_library.tf_raw_ops_BlockLSTMV2_Mutation_List
            function_name = "BlockLSTMV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.BoostedTreesTrainingPredict":
            change_parameter_with = mutation_library.tf_raw_ops_BoostedTreesTrainingPredict_Mutation_List
            function_name = "BoostedTreesTrainingPredict"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CSRSparseMatrixToDense":
            change_parameter_with = mutation_library.tf_raw_ops_CSRSparseMatrixToDense_Mutation_List
            function_name = "CSRSparseMatrixToDense"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CTCLoss":
            change_parameter_with = mutation_library.tf_raw_ops_CTCLoss_Mutation_List
            function_name = "CTCLoss"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CTCLossV2":
            change_parameter_with = mutation_library.tf_raw_ops_CTCLossV2_Mutation_List
            function_name = "CTCLossV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv":
            change_parameter_with = mutation_library.tf_raw_ops_Conv_Mutation_List
            function_name = "Conv"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2D":
            change_parameter_with = mutation_library.tf_raw_ops_Conv2D_Mutation_List
            function_name = "Conv2D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropFilter":
            change_parameter_with = mutation_library.tf_raw_ops_Conv2DBackpropFilter_Mutation_List
            function_name = "Conv2DBackpropFilter"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropFilterV2":
            change_parameter_with = mutation_library.tf_raw_ops_Conv2DBackpropFilterV2_Mutation_List
            function_name = "Conv2DBackpropFilterV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropInput":
            change_parameter_with = mutation_library.tf_raw_ops_Conv2DBackpropInput_Mutation_List
            function_name = "Conv2DBackpropInput"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv2DBackpropInputV2":
            change_parameter_with = mutation_library.tf_raw_ops_Conv2DBackpropInputV2_Mutation_List
            function_name = "Conv2DBackpropInputV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3D":
            change_parameter_with = mutation_library.tf_raw_ops_Conv3D_Mutation_List
            function_name = "Conv3D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropFilter":
            change_parameter_with = mutation_library.tf_raw_ops_Conv3DBackpropFilter_Mutation_List
            function_name = "Conv3DBackpropFilter"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropFilterV2":
            change_parameter_with = mutation_library.tf_raw_ops_Conv3DBackpropFilterV2_Mutation_List
            function_name = "Conv3DBackpropFilterV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropInput":
            change_parameter_with = mutation_library.tf_raw_ops_Conv3DBackpropInput_Mutation_List
            function_name = "Conv3DBackpropInput"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.Conv3DBackpropInputV2":
            change_parameter_with = mutation_library.tf_raw_ops_Conv3DBackpropInputV2_Mutation_List
            function_name = "Conv3DBackpropInputV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)

        elif mutate_selected_parameters == "raw_ops.CudnnRNN":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNN_Mutation_List
            function_name = "CudnnRNN"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackprop":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNBackprop_Mutation_List
            function_name = "CudnnRNNBackprop"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackpropV2":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNBackpropV2_Mutation_List
            function_name = "CudnnRNNBackpropV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNBackpropV3":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNBackpropV3_Mutation_List
            function_name = "CudnnRNNBackpropV3"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNCanonicalToParams":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNCanonicalToParams_Mutation_List
            function_name = "CudnnRNNCanonicalToParams"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNCanonicalToParamsV2":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNCanonicalToParamsV2_Mutation_List
            function_name = "CudnnRNNCanonicalToParamsV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsSize":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNParamsSize_Mutation_List
            function_name = "CudnnRNNParamsSize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsToCanonical":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNParamsToCanonical_Mutation_List
            function_name = "CudnnRNNParamsToCanonical"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNParamsToCanonicalV2":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNParamsToCanonicalV2_Mutation_List
            function_name = "CudnnRNNParamsToCanonicalV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNV2":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNN_Mutation_List
            function_name = "CudnnRNNV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.CudnnRNNV3":
            change_parameter_with = mutation_library.tf_raw_ops_CudnnRNNBackpropV3_Mutation_List
            function_name = "CudnnRNNV3"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseBincount":
            change_parameter_with = mutation_library.tf_raw_ops_DenseBincount_Mutation_List
            function_name = "DenseBincount"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseCountSparseOutput":
            change_parameter_with = mutation_library.tf_raw_ops_DenseCountSparseOutput_Mutation_List
            function_name = "DenseCountSparseOutput"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToCSRSparseMatrix":
            change_parameter_with = mutation_library.tf_raw_ops_DenseToCSRSparseMatrix_Mutation_List
            function_name = "DenseToCSRSparseMatrix"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToDenseSetOperation":
            change_parameter_with = mutation_library.tf_raw_ops_DenseToDenseSetOperation_Mutation_List
            function_name = "DenseToDenseSetOperation"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToSparseBatchDataset":
            change_parameter_with = mutation_library.tf_raw_ops_DenseToSparseBatchDataset_Mutation_List
            function_name = "DenseToSparseBatchDataset"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DenseToSparseSetOperation":
            change_parameter_with = mutation_library.tf_raw_ops_DenseToSparseSetOperation_Mutation_List
            function_name = "DenseToSparseSetOperation"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNative":
            change_parameter_with = mutation_library.tf_raw_ops_DepthwiseConv2dNative_Mutation_List
            function_name = "DepthwiseConv2dNative"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNativeBackpropFilter":
            change_parameter_with = mutation_library.tf_raw_ops_DepthwiseConv2dNativeBackpropFilter_Mutation_List
            function_name = "DepthwiseConv2dNativeBackpropFilter"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.DepthwiseConv2dNativeBackpropInput":
            change_parameter_with = mutation_library.tf_raw_ops_DepthwiseConv2dNativeBackpropInput_Mutation_List
            function_name = "DepthwiseConv2dNativeBackpropInput"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.FusedPadConv2D":
            change_parameter_with = mutation_library.tf_raw_ops_FusedPadConv2D_Mutation_List
            function_name = "FusedPadConv2D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.FusedResizeAndPadConv2D":
            change_parameter_with = mutation_library.tf_raw_ops_FusedResizeAndPadConv2D_Mutation_List
            function_name = "FusedResizeAndPadConv2D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.GRUBlockCell":
            change_parameter_with = mutation_library.tf_raw_ops_GRUBlockCell_Mutation_List
            function_name = "GRUBlockCell"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.GRUBlockCellGrad":
            change_parameter_with = mutation_library.tf_raw_ops_GRUBlockCellGrad_Mutation_List
            function_name = "GRUBlockCellGrad"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.L2Loss":
            change_parameter_with = mutation_library.tf_raw_ops_L2Loss_Mutation_List
            function_name = "L2Loss"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCell":
            change_parameter_with = mutation_library.tf_raw_ops_LSTMBlockCell_Mutation_List
            function_name = "LSTMBlockCell"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCellGrad":
            change_parameter_with = mutation_library.tf_raw_ops_LSTMBlockCellGrad_Mutation_List
            function_name = "LSTMBlockCellGrad"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2D":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2D_Mutation_List
            function_name = "QuantizedConv2D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRelu":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DAndRelu_Mutation_List
            function_name = "QuantizedConv2DAndRelu"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndReluAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DAndReluAndRequantize_Mutation_List
            function_name = "QuantizedConv2DAndReluAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DAndRequantize_Mutation_List
            function_name = "QuantizedConv2DAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DPerChannel":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DPerChannel_Mutation_List
            function_name = "QuantizedConv2DPerChannel"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBias":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBias_Mutation_List
            function_name = "QuantizedConv2DWithBias"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRelu":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasAndRelu_Mutation_List
            function_name = "QuantizedConv2DWithBiasAndRelu"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasAndReluAndRequantize_Mutation_List
            function_name = "QuantizedConv2DWithBiasAndReluAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasAndRequantize_Mutation_List
            function_name = "QuantizedConv2DWithBiasAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasSignedSumAndReluAndRequantize_Mutation_List
            function_name = "QuantizedConv2DWithBiasSignedSumAndReluAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndRelu":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasSumAndRelu_Mutation_List
            function_name = "QuantizedConv2DWithBiasSumAndRelu"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedConv2DWithBiasSumAndReluAndRequantize_Mutation_List
            function_name = "QuantizedConv2DWithBiasSumAndReluAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2D":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedDepthwiseConv2D_Mutation_List
            function_name = "QuantizedDepthwiseConv2D"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBias":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedDepthwiseConv2DWithBias_Mutation_List
            function_name = "QuantizedDepthwiseConv2DWithBias"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedDepthwiseConv2DWithBiasAndRelu_Mutation_List
            function_name = "QuantizedDepthwiseConv2DWithBiasAndRelu"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize":
            change_parameter_with = mutation_library.tf_raw_ops_QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize_Mutation_List
            function_name = "QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.RecvTPUEmbeddingActivations":
            change_parameter_with = mutation_library.tf_raw_ops_RecvTPUEmbeddingActivations_Mutation_List
            function_name = "RecvTPUEmbeddingActivations"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizer":
            change_parameter_with = mutation_library.tf_raw_ops_SdcaOptimizer_Mutation_List
            function_name = "SdcaOptimizer"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizerV2":
            change_parameter_with = mutation_library.tf_raw_ops_SdcaOptimizerV2_Mutation_List
            function_name = "SdcaOptimizerV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseAdd":
            change_parameter_with = mutation_library.tf_raw_ops_SparseDenseCwiseAdd_Mutation_List
            function_name = "SparseDenseCwiseAdd"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseDiv":
            change_parameter_with = mutation_library.tf_raw_ops_SparseDenseCwiseDiv_Mutation_List
            function_name = "SparseDenseCwiseDiv"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseDenseCwiseMul":
            change_parameter_with = mutation_library.tf_raw_ops_SparseDenseCwiseMul_Mutation_List
            function_name = "SparseDenseCwiseMul"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)


            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseAdd":
            change_parameter_with = mutation_library.tf_raw_ops_SparseTensorDenseAdd_Mutation_List
            function_name = "SparseTensorDenseAdd"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseTensorDenseMatMul":
            change_parameter_with = mutation_library.tf_raw_ops_SparseTensorDenseMatMul_Mutation_List
            function_name = "SparseTensorDenseMatMul"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SparseToDense":
            change_parameter_with = mutation_library.tf_raw_ops_SparseToDense_Mutation_List
            function_name = "SparseToDense"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.TPUEmbeddingActivations":
            change_parameter_with = mutation_library.tf_raw_ops_TpuEmbeddingActivations_Mutation_List
            function_name = "TPUEmbeddingActivations"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolution":
            change_parameter_with = mutation_library.tf_raw_ops_UniformQuantizedConvolution_Mutation_List
            function_name = "UniformQuantizedConvolution"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.UniformQuantizedConvolutionHybrid":
            change_parameter_with = mutation_library.tf_raw_ops_UniformQuantizedConvolutionHybrid_Mutation_List
            function_name = "UniformQuantizedConvolutionHybrid"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.RecvTPUEmbeddingActivations":
            change_parameter_with = mutation_library.tf_raw_ops_RecvTPUEmbeddingActivations_Mutation_List
            function_name = "RecvTPUEmbeddingActivations"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizer":
            change_parameter_with = mutation_library.tf_raw_ops_SdcaOptimizer_Mutation_List
            function_name = "SdcaOptimizer"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.SdcaOptimizerV2":
            change_parameter_with = mutation_library.tf_raw_ops_SdcaOptimizerV2_Mutation_List
            function_name = "SdcaOptimizerV2"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.L2Loss":
            change_parameter_with = mutation_library.tf_raw_ops_L2Loss_Mutation_List
            function_name = "L2Loss"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "raw_ops.LSTMBlockCell":
            change_parameter_with = mutation_library.tf_raw_ops_LSTMBlockCell_Mutation_List
            function_name = "LSTMBlockCell"
            mutated_line,matches = mutator.modify_tf_raw_ops_function_in_code(source_code, function_name, change_parameter_with)
        
        #train
        elif mutate_selected_parameters == "train.BytesList":
            change_parameter_with = mutation_library.tf_train_BytesList_Mutation_List
            class_name = "BytesList"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Checkpoint":
            change_parameter_with = mutation_library.tf_train_Checkpoint_Mutation_List
            class_name = "Checkpoint"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointManager":
            change_parameter_with = mutation_library.tf_train_CheckpointManager_Mutation_List
            class_name = "CheckpointManager"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointOptions":
            change_parameter_with = mutation_library.tf_train_CheckpointOptions_Mutation_List
            class_name = "CheckpointOptions"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.CheckpointView":
            change_parameter_with = mutation_library.tf_train_CheckpointView_Mutation_List
            class_name = "CheckpointView"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ClusterDef":
            change_parameter_with = mutation_library.tf_train_ClusterDef_Mutation_List
            class_name = "ClusterDef"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ClusterSpec":
            change_parameter_with = mutation_library.tf_train_ClusterSpec_Mutation_List
            class_name = "ClusterSpec"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Coordinator":
            change_parameter_with = mutation_library.tf_train_Coordinator_Mutation_List
            class_name = "Coordinator"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Example":
            change_parameter_with = mutation_library.tf_train_Example_Mutation_List
            class_name = "Example"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ExponentialMovingAverage":
            change_parameter_with = mutation_library.tf_train_ExponentialMovingAverage_Mutation_List
            class_name = "ExponentialMovingAverage"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Feature":
            change_parameter_with = mutation_library.tf_train_Feature_Mutation_List
            class_name = "Feature"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.FeatureList":
            change_parameter_with = mutation_library.tf_train_FeatureList_Mutation_List
            class_name = "FeatureList"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Features":
            change_parameter_with = mutation_library.tf_train_Features_Mutation_List
            class_name = "Features"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.FloatList":
            change_parameter_with = mutation_library.tf_train_FloatList_Mutation_List
            class_name = "FloatList"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.Int64List":
            change_parameter_with = mutation_library.tf_train_Int64List_Mutation_List
            class_name = "Int64List"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.JobDef":
            change_parameter_with = mutation_library.tf_train_JobDef_Mutation_List
            class_name = "JobDef"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.SequenceExample":
            change_parameter_with = mutation_library.tf_train_SequenceExample_Mutation_List
            class_name = "SequenceExample"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.ServerDef":
            change_parameter_with = mutation_library.tf_train_ServerDef_Mutation_List
            class_name = "ServerDef"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.TrackableView":
            change_parameter_with = mutation_library.tf_train_TrackableView_Mutation_List
            class_name = "TrackableView"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.checkpoints_iterator":
            change_parameter_with = mutation_library.tf_train_checkpoints_iterator_Mutation_List
            function_name = "checkpoints_iterator"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.experimental":
            change_parameter_with = mutation_library.tf_train_experimental_Mutation_List
            class_name = "experimental"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.experimental.PythonState":
            change_parameter_with = mutation_library.tf_train_experimental_PythonState_Mutation_List
            class_name = "experimental.PythonState"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, class_name, change_parameter_with)
        elif mutate_selected_parameters == "train.get_checkpoint_state":
            change_parameter_with = mutation_library.tf_train_get_checkpoint_state_Mutation_List
            function_name = "get_checkpoint_state"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.latest_checkpoint":
            change_parameter_with = mutation_library.tf_train_latest_checkpoint_Mutation_List
            function_name = "latest_checkpoint"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.list_variables":
            change_parameter_with = mutation_library.tf_train_list_variables_Mutation_List
            function_name = "list_variables"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.load_checkpoint":
            change_parameter_with = mutation_library.tf_train_load_checkpoint_Mutation_List
            function_name = "load_checkpoint"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
        elif mutate_selected_parameters == "train.load_variable":
            change_parameter_with = mutation_library.tf_train_load_variable_Mutation_List
            function_name = "load_variable"
            mutated_line,matches = mutator.modify_tf_train_class_in_code(source_code, function_name, change_parameter_with)
       

        return mutated_line,matches,change_parameter_with