




tf_keras_activation_functions = [
    'deserialize',                 # Aktivasyon fonksiyonlarını deserialize etmek için kullanılır
    'elu',                         # Exponential Linear Unit aktivasyon fonksiyonu
    'exponential',                 # Üssel (e tabanında) aktivasyon fonksiyonu
    'gelu',                        # Gaussian Error Linear Unit aktivasyon fonksiyonu
    'get',                         # Aktivasyon fonksiyonunu almak için kullanılır
    'hard_sigmoid',                # Hard sigmoid aktivasyon fonksiyonu
    'linear',                      # Lineer (hiçbir aktivasyon yapmayan) aktivasyon fonksiyonu
    'mish',                        # Mish aktivasyon fonksiyonu
    'relu',                        # Rectified Linear Unit aktivasyon fonksiyonu
    'selu',                        # Scaled Exponential Linear Unit aktivasyon fonksiyonu
    'serialize',                   # Aktivasyon fonksiyonlarını serialize etmek için kullanılır
    'sigmoid',                     # Sigmoid aktivasyon fonksiyonu
    'softmax',                     # Softmax aktivasyon fonksiyonu
    'softplus',                    # Softplus aktivasyon fonksiyonu
    'softsign',                    # Softsign aktivasyon fonksiyonu
    'swish',                       # Swish aktivasyon fonksiyonu
    'tanh'                         # Hiperbolik tanjant aktivasyon fonksiyonu
]

tf_keras_units_list = [8, 16, 32, 64, 128, 256, 512, 1024]

tf_keras_use_bias_list = [True, False]

tf_keras_kernel_initializer_list = [
    'Zeros',                  # Initializes weights to zero
    'Ones',                   # Initializes weights to one
    'Constant',               # Initializes weights to a constant value
    'RandomNormal',           # Initializes weights with a normal distribution
    'RandomUniform',          # Initializes weights with a uniform distribution
    'TruncatedNormal',        # Initializes weights with a truncated normal distribution
    'VarianceScaling',        # Initializes weights by scaling the variance based on fan-in or fan-out mode
    'Orthogonal',             # Initializes weights as orthogonal matrices
    'LecunNormal',            # LeCun normal initializer
    'LecunUniform',           # LeCun uniform initializer
    'GlorotNormal',           # Glorot/Xavier normal initializer
    'GlorotUniform',          # Glorot/Xavier uniform initializer
    'HeNormal',               # He normal initializer
    'HeUniform',              # He uniform variance scaling initializer
    'Identity'                # Initializes weights as the identity matrix (only for square matrices)
]

tf_keras_layers_classes = [
    'AbstractRNNCell', 
    'Activation', 
    'ActivityRegularization', 
    'Add', 
    'AdditiveAttention', 
    'AlphaDropout', 
    'Attention', 
    'Average', 
    'AveragePooling1D', 
    'AveragePooling2D', 
    'AveragePooling3D', 
    'AvgPool1D', 
    'AvgPool2D', 
    'AvgPool3D', 
    'BatchNormalization', 
    'Bidirectional', 
    'CategoryEncoding', 
    'CenterCrop', 
    'Concatenate', 
    'Conv1D', 
    'Conv1DTranspose', 
    'Conv2D', 
    'Conv2DTranspose', 
    'Conv3D', 
    'Conv3DTranspose', 
    'ConvLSTM1D', 
    'ConvLSTM2D', 
    'ConvLSTM3D', 
    'Convolution1D', 
    'Convolution1DTranspose', 
    'Convolution2D', 
    'Convolution2DTranspose', 
    'Convolution3D', 
    'Convolution3DTranspose', 
    'Cropping1D', 
    'Cropping2D', 
    'Cropping3D', 
    'Dense', 
    'DenseFeatures', 
    'DepthwiseConv1D', 
    'DepthwiseConv2D', 
    'Discretization', 
    'Dot', 
    'Dropout', 
    'ELU', 
    'EinsumDense', 
    'Embedding', 
    'Flatten', 
    'GRU', 
    'GRUCell', 
    'GaussianDropout', 
    'GaussianNoise', 
    'GlobalAveragePooling1D', 
    'GlobalAveragePooling2D', 
    'GlobalAveragePooling3D', 
    'GlobalAvgPool1D', 
    'GlobalAvgPool2D', 
    'GlobalAvgPool3D', 
    'GlobalMaxPool1D', 
    'GlobalMaxPool2D', 
    'GlobalMaxPool3D', 
    'GlobalMaxPooling1D', 
    'GlobalMaxPooling2D', 
    'GlobalMaxPooling3D', 
    'GroupNormalization', 
    'HashedCrossing', 
    'Hashing', 
    'Identity', 
    'InputLayer', 
    'InputSpec', 
    'IntegerLookup', 
    'LSTM', 
    'LSTMCell', 
    'Lambda', 
    'Layer', 
    'LayerNormalization', 
    'LeakyReLU', 
    'LocallyConnected1D', 
    'LocallyConnected2D', 
    'Masking', 
    'MaxPool1D', 
    'MaxPool2D', 
    'MaxPool3D', 
    'MaxPooling1D', 
    'MaxPooling2D', 
    'MaxPooling3D', 
    'Maximum', 
    'Minimum', 
    'MultiHeadAttention', 
    'Multiply', 
    'Normalization', 
    'PReLU', 
    'Permute', 
    'RNN', 
    'RandomBrightness', 
    'RandomContrast', 
    'RandomCrop', 
    'RandomFlip', 
    'RandomHeight', 
    'RandomRotation', 
    'RandomTranslation', 
    'RandomWidth', 
    'RandomZoom', 
    'ReLU', 
    'RepeatVector', 
    'Rescaling', 
    'Reshape', 
    'Resizing', 
    'SeparableConv1D', 
    'SeparableConv2D', 
    'SeparableConvolution1D', 
    'SeparableConvolution2D', 
    'SimpleRNN', 
    'SimpleRNNCell', 
    'Softmax', 
    'SpatialDropout1D', 
    'SpatialDropout2D', 
    'SpatialDropout3D', 
    'SpectralNormalization', 
    'StackedRNNCells', 
    'StringLookup', 
    'Subtract', 
    'TextVectorization', 
    'ThresholdedReLU', 
    'TimeDistributed', 
    'UnitNormalization', 
    'UpSampling1D', 
    'UpSampling2D', 
    'UpSampling3D', 
    'Wrapper', 
    'ZeroPadding1D', 
    'ZeroPadding2D', 
    'ZeroPadding3D'
]

tf_keras_losses_classes = [
    'BinaryCrossentropy',                # Computes the cross-entropy loss between true labels and predicted labels.
    'BinaryFocalCrossentropy',           # Computes focal cross-entropy loss between true labels and predictions.
    'CategoricalCrossentropy',           # Computes the crossentropy loss between the labels and predictions.
    'CategoricalFocalCrossentropy',      # Computes the alpha balanced focal crossentropy loss.
    'CategoricalHinge',                  # Computes the categorical hinge loss between y_true and y_pred.
    'CosineSimilarity',                  # Computes the cosine similarity between labels and predictions.
    'Hinge',                             # Computes the hinge loss between y_true and y_pred.
    'Huber',                             # Computes the Huber loss between y_true and y_pred.
    'KLDivergence',                      # Computes Kullback-Leibler divergence loss between y_true and y_pred.
    'LogCosh',                           # Computes the logarithm of the hyperbolic cosine of the prediction error.
    'Loss',                              # Loss base class.
    'MeanAbsoluteError',                 # Computes the mean of absolute difference between labels and predictions.
    'MeanAbsolutePercentageError',       # Computes the mean absolute percentage error between y_true and y_pred.
    'MeanSquaredError',                  # Computes the mean of squares of errors between labels and predictions.
    'MeanSquaredLogarithmicError',       # Computes the mean squared logarithmic error between y_true and y_pred.
    'Poisson',                           # Computes the Poisson loss between y_true and y_pred.
    'Reduction',                         # Types of loss reduction.
    'SparseCategoricalCrossentropy',     # Computes the crossentropy loss between the labels and predictions.
    'SquaredHinge',                      # Computes the squared hinge loss between y_true and y_pred.
]

tf_keras_metrics_classes = [
    'AUC',                            # Approximates the AUC (Area under the curve) of the ROC or PR curves.
    'Accuracy',                       # Calculates how often predictions equal labels.
    'BinaryAccuracy',                 # Calculates how often predictions match binary labels.
    'BinaryCrossentropy',             # Computes the crossentropy metric between the labels and predictions.
    'BinaryIoU',                      # Computes the Intersection-Over-Union metric for class 0 and/or 1.
    'CategoricalAccuracy',            # Calculates how often predictions match one-hot labels.
    'CategoricalCrossentropy',        # Computes the crossentropy metric between the labels and predictions.
    'CategoricalHinge',               # Computes the categorical hinge metric between y_true and y_pred.
    'CosineSimilarity',               # Computes the cosine similarity between the labels and predictions.
    'F1Score',                        # Computes F-1 Score.
    'FBetaScore',                     # Computes F-Beta score.
    'FalseNegatives',                 # Calculates the number of false negatives.
    'FalsePositives',                 # Calculates the number of false positives.
    'Hinge',                          # Computes the hinge metric between y_true and y_pred.
    'IoU',                            # Computes the Intersection-Over-Union metric for specific target classes.
    'KLDivergence',                   # Computes Kullback-Leibler divergence metric between y_true and y_pred.
    'LogCoshError',                   # Computes the logarithm of the hyperbolic cosine of the prediction error.
    'Mean',                           # Computes the (weighted) mean of the given values.
    'MeanAbsoluteError',              # Computes the mean absolute error between the labels and predictions.
    'MeanAbsolutePercentageError',    # Computes the mean absolute percentage error between y_true and y_pred.
    'MeanIoU',                        # Computes the mean Intersection-Over-Union metric.
    'MeanMetricWrapper',              # Wraps a stateless metric function with the Mean metric.
    'MeanRelativeError',              # Computes the mean relative error by normalizing with the given values.
    'MeanSquaredError',               # Computes the mean squared error between y_true and y_pred.
    'MeanSquaredLogarithmicError',    # Computes the mean squared logarithmic error between y_true and y_pred.
    'MeanTensor',                     # Computes the element-wise (weighted) mean of the given tensors.
    'Metric',                         # Encapsulates metric logic and state.
    'OneHotIoU',                      # Computes the Intersection-Over-Union metric for one-hot encoded labels.
    'OneHotMeanIoU',                  # Computes mean Intersection-Over-Union metric for one-hot encoded labels.
    'Poisson',                        # Computes the Poisson score between y_true and y_pred.
    'Precision',                      # Computes the precision of the predictions with respect to the labels.
    'PrecisionAtRecall',              # Computes best precision where recall is >= specified value.
    'R2Score',                        # Computes R2 score.
    'Recall',                         # Computes the recall of the predictions with respect to the labels.
    'RecallAtPrecision',              # Computes best recall where precision is >= specified value.
    'RootMeanSquaredError',           # Computes root mean squared error metric between y_true and y_pred.
    'SensitivityAtSpecificity',       # Computes best sensitivity where specificity is >= specified value.
    'SparseCategoricalAccuracy',      # Calculates how often predictions match integer labels.
    'SparseCategoricalCrossentropy',  # Computes the crossentropy metric between the labels and predictions.
    'SparseTopKCategoricalAccuracy',  # Computes how often integer targets are in the top K predictions.
    'SpecificityAtSensitivity',       # Computes best specificity where sensitivity is >= specified value.
    'SquaredHinge',                   # Computes the squared hinge metric between y_true and y_pred.
    'Sum',                            # Computes the (weighted) sum of the given values.
    'TopKCategoricalAccuracy',        # Computes how often targets are in the top K predictions.
    'TrueNegatives',                  # Calculates the number of true negatives.
    'TruePositives',                  # Calculates the number of true positives.
]

tf_keras_optimizers_classes = [
    'Adadelta',    # Optimizer that implements the Adadelta algorithm.
    'Adafactor',   # Optimizer that implements the Adafactor algorithm.
    'Adagrad',     # Optimizer that implements the Adagrad algorithm.
    'Adam',        # Optimizer that implements the Adam algorithm.
    'AdamW',       # Optimizer that implements the AdamW algorithm.
    'Adamax',      # Optimizer that implements the Adamax algorithm.
    'Ftrl',        # Optimizer that implements the FTRL algorithm.
    'Lion',        # Optimizer that implements the Lion algorithm.
    'Nadam',       # Optimizer that implements the Nadam algorithm.
    'Optimizer',   # Abstract optimizer base class.
    'RMSprop',     # Optimizer that implements the RMSprop algorithm.
    'SGD',         # Gradient descent (with momentum) optimizer.
]

tf_keras_regularizers_classes = [
    'L1',                      # A regularizer that applies a L1 regularization penalty.
    'L1L2',                    # A regularizer that applies both L1 and L2 regularization penalties.
    'L2',                      # A regularizer that applies a L2 regularization penalty.
    'OrthogonalRegularizer',   # Regularizer that encourages input vectors to be orthogonal to each other.
    'Regularizer',             # Regularizer base class.
    'l1',                      # A regularizer that applies a L1 regularization penalty (function).
    'l2',                      # A regularizer that applies a L2 regularization penalty (function).
    'orthogonal_regularizer',  # Regularizer that encourages input vectors to be orthogonal to each other (function).
]
