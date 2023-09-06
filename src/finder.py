""" RegEx Codes For CNNs and DNNs """

import re

cnn_function_regex_codes = [
    r'nn\.Conv1d',
    r'nn\.Conv2d',
    r'nn\.Conv3d',
    r'nn\.ConvTranspose1d',
    r'nn\.ConvTranspose2d',
    r'nn\.ConvTranspose3d',
    r'nn\.MaxPool1d',
    r'nn\.MaxPool2d',
    r'nn\.MaxPool3d',
    r'nn\.AvgPool1d',
    r'nn\.AvgPool2d',
    r'nn\.AvgPool3d',
    r'nn\.BatchNorm1d',
    r'nn\.BatchNorm2d',
    r'nn\.BatchNorm3d',
    r'nn\.Dropout',
    r'nn\.Dropout2d',
    r'nn\.Dropout3d',
    r'F\.relu',
    r'F\.leaky_relu',
    r'F\.sigmoid',
    r'F\.tanh',
    r'F\.softmax',
    r'F\.log_softmax',
    r'nn\.CrossEntropyLoss',
    r'optim\.SGD',
    r'optim\.Adam',
    r'nn\.MultiheadAttention'
]

dnn_function_regex_codes = [
    r'nn\.Linear',
    r'nn\.ReLU',
    r'nn\.LeakyReLU',
    r'nn\.Sigmoid',
    r'nn\.Tanh',
    r'nn\.Softmax',
    r'nn\.LogSoftmax',
    r'nn\.Dropout',
    r'nn\.BatchNorm1d',
    r'nn\.BatchNorm2d',
    r'nn\.BatchNorm3d',
    r'nn\.Conv1d',
    r'nn\.Conv2d',
    r'nn\.Conv3d',
    r'nn\.ConvTranspose1d',
    r'nn\.ConvTranspose2d',
    r'nn\.ConvTranspose3d',
    r'nn\.MaxPool1d',
    r'nn\.MaxPool2d',
    r'nn\.MaxPool3d',
    r'nn\.AvgPool1d',
    r'nn\.AvgPool2d',
    r'nn\.AvgPool3d',
    r'nn\.MultiheadAttention',
    r'nn\.CrossEntropyLoss',
    r'optim\.SGD',
    r'optim\.Adam'
]


CODE = """
m = nn.ReLU(p=0.2)
m = nn.Dropout3d(p=0.2)
input = torch.randn(20, 16, 4, 32, 32)
output = m(input)
"""

code_lines = CODE.split("\n")

def find_cnn_function(*args):
    """ CNN RegEx Function """
    for line in code_lines:
        for pattern in cnn_function_regex_codes:
            function = re.findall(pattern, line)
            if function:
                return line
    return None


def find_dnn_function(*args):
    """ DNN RegEx Function """
    for line in code_lines:
        for pattern in dnn_function_regex_codes:
            function = re.findall(pattern, line)
            if function:
                return line
    return None

print(find_cnn_function(code_lines,cnn_function_regex_codes))
print(find_dnn_function(code_lines,dnn_function_regex_codes))
