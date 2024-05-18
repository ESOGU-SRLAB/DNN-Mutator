


#tf.keras
tf_epochs=["epoch=1"]

tf_activation_functions = [
    "",
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
tf_keras_layers_Activation_Full_List = [
    "",
    "activation=",
    # Standard activation functions
    "activation='relu'", 
    "activation='sigmoid'", 
    "activation='softmax'", 
    "activation='tanh'", 
    "activation='elu'",
    "activation='selu'",
    "activation='softplus'",
    "activation='softsign'",
    "activation='swish'",
    "activation='hard_sigmoid'",
    "activation='exponential'",
    "activation='linear'",  # Linear (no activation)

    # Scenarios with erroneous or inappropriate values
    "activation='not_a_function'",  # Non-existent activation
    "activation=''",  # Empty string
    "activation=123"   # Non-string, invalid type
]
tf_dense_list = [
    "",
    "Dense(10",  # Dense layer with 10 units
    "Dense(20",  # Dense layer with 20 units
    "Dense(32",  # Dense layer with 30 units
    "Dense(40",  # Dense layer with 40 units
    "Dense(50",  # Dense layer with 50 units
    "Dense(64",  # Dense layer with 60 units
    "Dense(70",  # Dense layer with 70 units
    "Dense(80",  # Dense layer with 80 units
    "Dense(90",  # Dense layer with 90 units
    "Dense(100",  # Dense layer with 100 units
    "Dense(128",  # Dense layer with 128 units
    "Dense(256",  # Dense layer with 256 units
]
tf_optimizers_list = [
    "optimizer=''",
    "optimizer='adam'",                # Adam optimizer
    "optimizer='sgd'",                 # Stochastic Gradient Descent optimizer
    "optimizer='rmsprop'",             # RMSprop optimizer
    "optimizer='adagrad'",             # Adagrad optimizer
    "optimizer='adadelta'",            # Adadelta optimizer
    "optimizer='adamax'",              # Adamax optimizer
    "optimizer='nadam'",               # Nadam optimizer
    "optimizer='ftrl'",                # FTRL optimizer
    "optimizer='lion'",
    "optimizer='sgd'",
    "optimizer='adafactor'",   
    # Additional optimizers that might be less common
    "optimizer='l-bfgs'",              # L-BFGS optimizer
    "optimizer='momentum'",            # Momentum optimizer
    "optimizer='proximal_gradient_descent'",  # Proximal Gradient Descent optimizer
    "optimizer='proximal_adagrad'",    # Proximal Adagrad optimizer
    "optimizer='q-learning'",          # Q-learning optimizer
]
tf_loss_functions_list = [
    "",
    "loss='categorical_crossentropy'",  # Loss function for multi-class classification
    "loss='sparse_categorical_crossentropy'",  # Sparse version for multi-class classification
    "loss='binary_crossentropy'",  # Loss function for binary classification
    "loss='mean_squared_error'",  # Standard loss function for regression
    "loss='mean_absolute_error'",  # Absolute difference between target and predicted values
    "loss='mean_absolute_percentage_error'",  # Mean absolute percentage error between target and predicted
    "loss='mean_squared_logarithmic_error'",  # Mean squared logarithmic error
    "loss='huber_loss'",  # Huber loss, less sensitive to outliers in data
    "loss='log_cosh'",  # Logarithm of the hyperbolic cosine of the prediction error
    "loss='categorical_hinge'",  # Categorical hinge loss for multi-class classification
    "loss='poisson'",  # Poisson loss for counting models
    "loss='kullback_leibler_divergence'",  # Kullback-Leibler divergence loss
    "loss='hinge'",  # Hinge loss for binary classification
    "loss='squared_hinge'",  # Squared hinge loss, variant of hinge loss
    "loss='cosine_similarity'",  # Cosine similarity between labels and predictions
    "loss='log_loss'",  # Logistic loss function
]
tf_kernel_regularizer_configurations = [
    "",
    # Common L2 regularizer configurations
    "kernel_regularizer=l2(0.01)", "kernel_regularizer=l2(0.001)",
    "kernel_regularizer=l2(0.1)", "kernel_regularizer=l2(0.05)",
    "kernel_regularizer=l2(0.02)", "kernel_regularizer=l2(0.005)",
    "kernel_regularizer=l2(0.0001)", "kernel_regularizer=l2(0.0005)",
    "kernel_regularizer=l2(0.2)", "kernel_regularizer=l2(0.3)",

    # Common L1 regularizer configurations
    "kernel_regularizer=l1(0.01)", "kernel_regularizer=l1(0.001)",
    "kernel_regularizer=l1(0.1)", "kernel_regularizer=l1(0.05)",
    "kernel_regularizer=l1(0.02)", "kernel_regularizer=l1(0.005)",
    "kernel_regularizer=l1(0.0001)", "kernel_regularizer=l1(0.0005)",
    "kernel_regularizer=l1(0.2)", "kernel_regularizer=l1(1.0)"
]

tf_batch_size_list = [
    "",
    # Most common batch sizes
    "batch_size=32", 
    "batch_size=64", 
    "batch_size=128", 
    "batch_size=256", 
    "batch_size=512",
    "batch_size=16", 
    "batch_size=8", 
    "batch_size=4", 
    "batch_size=2", 
    "batch_size=1",

    # Erroneous or inappropriate values
    "batch_size=-1",  # Negative batch size is invalid
    "batch_size='invalid'"  # Non-integer or string value is invalid
]
tf_input_shape_list = [
    "",
    # Single layer configurations
    "input_shape=(32,)", "input_shape=(64,)", "input_shape=(128,)", 
    "input_shape=(256,)", "input_shape=(512,)",

    # Double layer configurations
    "input_shape=(32, 32)", "input_shape=(64, 64)", "input_shape=(128, 128)", 
    "input_shape=(256, 256)", "input_shape=(512, 512)",

    # Triple layer configurations
    "input_shape=(32, 32, 3)", "input_shape=(64, 64, 3)", "input_shape=(128, 128, 3)", 
    "input_shape=(256, 256, 3)", "input_shape=(512, 512, 3)",

    # Additional configurations for variation
    "input_shape=(32, 32, 1)", "input_shape=(64, 64, 1)", "input_shape=(128, 128, 1)", 
    "input_shape=(256, 256, 1)", "input_shape=(512, 512, 1)",

    # More triple layer configurations with different channel numbers
    "input_shape=(32, 32, 4)", "input_shape=(64, 64, 4)", "input_shape=(128, 128, 4)"
]


tf_keras_units_list = [
    "",
    "units=4",    # Very small model or layer
    "units=8",    # Small model or layer
    "units=16",   # Slightly larger model or layer
    "units=32",   # Commonly used size for small to medium models
    "units=64",   # Medium-sized model or layer
    "units=128",  # Larger model or layer
    "units=256",  # Large model or layer
    "units=512",  # Very large model or layer
    "units=1024", # Extremely large model or layer
    "units=2048", # For very complex models or large datasets
    "units=5096",    
]

tf_keras_use_bias_list = ["use_bias=True", "use_bias=False","use_bias=",]

tf_filters_configurations = [
    "",
    "filters=",
    "filters=8",
    "filters=16",  # Common for smaller or initial layers
    "filters=32",  # Standard for early convolutional layers
    "filters=64",  # Widely used in various layers
    "filters=128", # Common in deeper layers
    "filters=256", # Used in advanced layers for more complex features
    "filters=512", # High number for very deep layers
    "filters=1024",# Very large number, used in very deep networks
]

tf_pool_size_list = [
    "",
    "pool_size=",
    # 1D Pool Sizes
    "pool_size=2", "pool_size=3", "pool_size=4", 
    "pool_size=5", "pool_size=6", "pool_size=7", 
    "pool_size=8",

    # 2D Pool Sizes
    "pool_size=(2, 2)", "pool_size=(3, 3)", "pool_size=(4, 4)", 
    "pool_size=(5, 5)", "pool_size=(6, 6)", "pool_size=(7, 7)", 
    "pool_size=(8, 8)",

    # 3D Pool Sizes
    "pool_size=(2, 2, 2)", "pool_size=(3, 3, 3)", "pool_size=(4, 4, 4)", 
    "pool_size=(5, 5, 5)", "pool_size=(6, 6, 6)", "pool_size=(7, 7, 7)", 
    "pool_size=(8, 8, 8)"
]

tf_dropout_rate_list = [
    "",
    "dropout=0.1",  # A light amount of dropout
    "dropout=0.2",  # Moderately light dropout
    "dropout=0.3",  # Moderate dropout
    "dropout=0.4",  # Moderately high dropout
    "dropout=0.5",   # A relatively high rate of dropout
    "dropout=0.6",
    "dropout=0.7",
    "dropout=0.8",
    "dropout=0.9",
    "dropout=0.0",
]

tf_Dropout_rate_list = [
    "",
    "Dropout(0.1)",  # A light amount of dropout
    "Dropout(0.2)",  # Moderately light dropout
    "Dropout(0.3)",  # Moderate dropout
    "Dropout(0.4)",  # Moderately high dropout
    "Dropout(0.5)",  # A relatively high rate of dropout
    "Dropout(0.6)",
    "Dropout(0.7)",
    "Dropout(0.8)",
    "Dropout(0.9)",
    "Dropout(0.0)",
]

tf_learning_rate_list = [
    "",
    # Commonly used learning rate values
    "learning_rate=0.001", "learning_rate=0.01", "learning_rate=0.1", 
    "learning_rate=0.0001", "learning_rate=0.05",
    "learning_rate=0.2","learning_rate=0.4",
    "learning_rate=0.6","learning_rate=0.8",
    "learning_rate=1",

    # Scenarios with erroneous or inappropriate values
    "learning_rate=-0.001", "learning_rate='invalid'", "learning_rate=None"
]
tf_kernel_size_list = [
    "",
    # 1D kernel sizes
    "kernel_size=1", "kernel_size=3", "kernel_size=5", 
    "kernel_size=7", "kernel_size=9",

    # 2D kernel sizes
    "kernel_size=(1, 1)", "kernel_size=(3, 3)", "kernel_size=(5, 5)", 
    "kernel_size=(7, 7)", "kernel_size=(9, 9)",

    # 3D kernel sizes
    "kernel_size=(1, 1, 1)", "kernel_size=(3, 3, 3)", "kernel_size=(5, 5, 5)", 
    "kernel_size=(7, 7, 7)", "kernel_size=(9, 9, 9)"
]
tf_keras_kernel_initializer_list = [
    "",
    "kernel_initializer='zeros'",                  # Initializes weights to zero
    "kernel_initializer='ones'",                   # Initializes weights to one
    "kernel_initializer='constant'",               # Initializes weights to a constant value
    "kernel_initializer='random_normal'",          # Initializes weights with a normal distribution
    "kernel_initializer='random_uniform'",         # Initializes weights with a uniform distribution
    "kernel_initializer='truncated_normal'",       # Initializes weights with a truncated normal distribution
    "kernel_initializer='variance_scaling'",       # Initializes weights by scaling the variance based on fan-in or fan-out mode
    "kernel_initializer='orthogonal'",             # Initializes weights as orthogonal matrices
    "kernel_initializer='lecun_normal'",           # LeCun normal initializer
    "kernel_initializer='lecun_uniform'",          # LeCun uniform initializer
    "kernel_initializer='glorot_normal'",          # Glorot/Xavier normal initializer
    "kernel_initializer='glorot_uniform'",         # Glorot/Xavier uniform initializer
    "kernel_initializer='he_normal'",              # He normal initializer
    "kernel_initializer='he_uniform'",             # He uniform variance scaling initializer
    "kernel_initializer='identity'"                # Initializes weights as the identity matrix (only for square matrices)
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
    'SGD', 'sgd' ,       # Gradient descent (with momentum) optimizer.
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

#tf.nn

tf_nn_functions = [
    "all_candidate_sampler",                           # Generate the set of all classes.
    "approx_max_k",                                    # Returns max k values and their indices of the input operand in an approximate manner.
    "approx_min_k",                                    # Returns min k values and their indices of the input operand in an approximate manner.
    "atrous_conv2d",                                   # Atrous convolution (a.k.a. convolution with holes or dilated convolution).
    "atrous_conv2d_transpose",                         # The transpose of atrous_conv2d.
    "avg_pool",                                        # Performs the avg pooling on the input.
    "avg_pool1d",                                      # Performs the average pooling on the input.
    "avg_pool2d",                                      # Performs the average pooling on the input.
    "avg_pool3d",                                      # Performs the average pooling on the input.
    "batch_norm_with_global_normalization",            # Batch normalization.
    "batch_normalization",                             # Batch normalization.
    "bias_add",                                        # Adds bias to value.
    "collapse_repeated",                               # Merge repeated labels into single labels.
    "compute_accidental_hits",                         # Compute the position ids in sampled_candidates matching true_classes.
    "compute_average_loss",                            # Scales per-example losses with sample_weights and computes their average.
    "conv1d",                                          # Computes a 1-D convolution given 3-D input and filter tensors.
    "conv1d_transpose",                                # The transpose of conv1d.
    "conv2d",                                          # Computes a 2-D convolution given input and 4-D filters tensors.
    "conv2d_transpose",                                # The transpose of conv2d.
    "conv3d",                                          # Computes a 3-D convolution given 5-D input and filters tensors.
    "conv3d_transpose",                                # The transpose of conv3d.
    "conv_transpose",                                  # The transpose of convolution.
    "convolution",                                     # Computes sums of N-D convolutions (actually cross-correlation).
    "crelu",                                           # Computes Concatenated ReLU.
    "ctc_beam_search_decoder",                         # Performs beam search decoding on the logits given in input.
    "ctc_greedy_decoder",                              # Performs greedy decoding on the logits given in input (best path).
    "ctc_loss",                                        # Computes CTC (Connectionist Temporal Classification) loss.
    "ctc_unique_labels",                               # Get unique labels and indices for batched labels for tf.nn.ctc_loss.
    "depth_to_space",                                  # DepthToSpace for tensors of type T.
    "depthwise_conv2d",                                # Depthwise 2-D convolution.
    "depthwise_conv2d_backprop_filter",                # Computes the gradients of depthwise convolution with respect to the filter.
    "depthwise_conv2d_backprop_input",                 # Computes the gradients of depthwise convolution with respect to the input.
    "dilation2d",                                      # Computes the grayscale dilation of 4-D input and 3-D filters tensors.
    "dropout",                                         # Computes dropout: randomly sets elements to zero to prevent overfitting.
    "elu",                                             # Computes the exponential linear function.
    "embedding_lookup",                                # Looks up embeddings for the given ids from a list of tensors.
    "embedding_lookup_sparse",                         # Looks up embeddings for the given ids and weights from a list of tensors.
    "erosion2d",                                       # Computes the grayscale erosion of 4-D value and 3-D filters tensors.
    "fixed_unigram_candidate_sampler",                 # Samples a set of classes using the provided (fixed) base distribution.
    "fractional_avg_pool",                             # Performs fractional average pooling on the input.
    "fractional_max_pool",                             # Performs fractional max pooling on the input.
    "gelu",                                            # Compute the Gaussian Error Linear Unit (GELU) activation function.
    "in_top_k",                                        # Outputs whether the targets are in the top K predictions.
    "isotonic_regression",                             # Solves isotonic regression problems along the given axis.
    "l2_loss",                                         # L2 Loss.
    "l2_normalize",                                    # Normalizes along dimension axis using an L2 norm. (deprecated arguments)
    "leaky_relu",                                      # Compute the Leaky ReLU activation function.
    "learned_unigram_candidate_sampler",               # Samples a set of classes from a distribution learned during training.
    "local_response_normalization",                    # Local Response Normalization.
    "log_poisson_loss",                                # Computes log Poisson loss given log_input.
    "log_softmax",                                     # Computes log softmax activations.
    "lrn",                                             # Local Response Normalization.
    "max_pool",                                        # Performs max pooling on the input.
    "max_pool1d",                                      # Performs the max pooling on the input.
    "max_pool2d",                                      # Performs max pooling on 2D spatial data such as images.
    "max_pool3d",                                      # Performs the max pooling on the input.
    "max_pool_with_argmax",                            # Performs max pooling on the input and outputs both max values and indices.
    "moments",                                         # Calculates the mean and variance of x.
    "nce_loss",                                        # Computes and returns the noise-contrastive estimation training loss.
    "normalize_moments",                               # Calculate the mean and variance of based on the sufficient statistics.
    "pool",                                            # Performs an N-D pooling operation.
    "relu",                                            # Computes rectified linear: max(features, 0).
    "relu6",                                           # Computes Rectified Linear 6: min(max(features, 0), 6).
    "safe_embedding_lookup_sparse",                    # Lookup embedding results, accounting for invalid IDs and empty features.
    "sampled_softmax_loss",                            # Computes and returns the sampled softmax training loss.
    "scale_regularization_loss",                       # Scales the sum of the given regularization losses by number of replicas.
    "selu",                                            # Computes scaled exponential linear: scale * alpha * (exp(features) - 1)
    "separable_conv2d",                                # 2-D convolution with separable filters.
    "sigmoid",                                         # Computes sigmoid of x element-wise.
    "sigmoid_cross_entropy_with_logits",               # Computes sigmoid cross entropy given logits.
    "silu",                                            # Computes the SiLU or Swish activation function: x * sigmoid(beta * x).
    "softmax",                                         # Computes softmax activations.
    "softmax_cross_entropy_with_logits",               # Computes softmax cross entropy between logits and labels.
    "softplus",                                        # Computes elementwise softplus: softplus(x) = log(exp(x) + 1).
    "softsign",                                        # Computes softsign: features / (abs(features) + 1).
    "space_to_batch",                                  # SpaceToBatch for N-D tensors of type T.
    "space_to_depth",                                  # SpaceToDepth for tensors of type T.
    "sparse_softmax_cross_entropy_with_logits",        # Computes sparse softmax cross entropy between logits and labels.
    "sufficient_statistics",                           # Calculate the sufficient statistics for the mean and variance of x.
    "swish",                                           # Computes the SiLU or Swish activation function: x * sigmoid(beta * x).
    "tanh",                                            # Computes hyperbolic tangent of x element-wise.
    "top_k",                                           # Finds values and indices of the k largest entries for the last dimension.
    "weighted_cross_entropy_with_logits",              # Computes a weighted cross entropy.
    "weighted_moments",                                # Returns the frequency-weighted mean and variance of x.
    "with_space_to_batch",                             # Performs op on the space-to-batch representation of input.
    "zero_fraction",                                   # Returns the fraction of zeros in value.
]

#tf.math

tf_math_functions = [
    "abs",                                            # Computes the absolute value of a tensor.
    "acos",                                           # Computes acos of x element-wise.
    "acosh",                                          # Computes inverse hyperbolic cosine of x element-wise.
    "add",                                            # Returns x + y element-wise.
    "add_n",                                          # Returns the element-wise sum of a list of tensors.
    "angle",                                          # Returns the element-wise argument of a complex (or real) tensor.
    "approx_max_k",                                   # Returns max k values and their indices of the input operand in an approximate manner.
    "approx_min_k",                                   # Returns min k values and their indices of the input operand in an approximate manner.
    "argmax",                                         # Returns the index with the largest value across axes of a tensor.
    "argmin",                                         # Returns the index with the smallest value across axes of a tensor.
    "asin",                                           # Computes the trignometric inverse sine of x element-wise.
    "asinh",                                          # Computes inverse hyperbolic sine of x element-wise.
    "atan",                                           # Computes the trignometric inverse tangent of x element-wise.
    "atan2",                                          # Computes arctangent of y/x element-wise, respecting signs of the arguments.
    "atanh",                                          # Computes inverse hyperbolic tangent of x element-wise.
    "bessel_i0",                                      # Computes the Bessel i0 function of x element-wise.
    "bessel_i0e",                                     # Computes the Bessel i0e function of x element-wise.
    "bessel_i1",                                      # Computes the Bessel i1 function of x element-wise.
    "bessel_i1e",                                     # Computes the Bessel i1e function of x element-wise.
    "betainc",                                        # Compute the regularized incomplete beta integral.
    "bincount",                                       # Counts the number of occurrences of each value in an integer array.
    "ceil",                                           # Return the ceiling of the input, element-wise.
    "confusion_matrix",                               # Computes the confusion matrix from predictions and labels.
    "conj",                                           # Returns the complex conjugate of a complex number.
    "cos",                                            # Computes cos of x element-wise.
    "cosh",                                           # Computes hyperbolic cosine of x element-wise.
    "count_nonzero",                                  # Computes number of nonzero elements across dimensions of a tensor.
    "cumprod",                                        # Compute the cumulative product of the tensor x along axis.
    "cumsum",                                         # Compute the cumulative sum of the tensor x along axis.
    "cumulative_logsumexp",                           # Compute the cumulative log-sum-exp of the tensor x along axis.
    "digamma",                                        # Computes Psi, the derivative of Lgamma (the log of the absolute value of Gamma(x)).
    "divide",                                         # Computes Python style division of x by y.
    "divide_no_nan",                                  # Computes a safe divide which returns 0 if y (denominator) is zero.
    "equal",                                          # Returns the truth value of (x == y) element-wise.
    "erf",                                            # Computes the Gauss error function of x element-wise.
    "erfc",                                           # Computes the complementary error function of x element-wise.
    "erfcinv",                                        # Computes the inverse of complementary error function.
    "erfinv",                                         # Compute inverse error function.
    "exp",                                            # Computes exponential of x element-wise.
    "expm1",                                          # Computes exp(x) - 1 element-wise.
    "floor",                                          # Returns element-wise largest integer not greater than x.
    "floordiv",                                       # Divides x / y elementwise, rounding toward the most negative integer.
    "floormod",                                       # Returns element-wise remainder of division.
    "greater",                                        # Returns the truth value of (x > y) element-wise.
    "greater_equal",                                  # Returns the truth value of (x >= y) element-wise.
    "igamma",                                         # Compute the lower regularized incomplete Gamma function P(a, x).
    "igammac",                                        # Compute the upper regularized incomplete Gamma function Q(a, x).
    "imag",                                           # Returns the imaginary part of a complex (or real) tensor.
    "in_top_k",                                       # Outputs whether the targets are in the top K predictions.
    "invert_permutation",                             # Computes the inverse permutation of a tensor.
    "is_finite",                                      # Returns which elements of x are finite.
    "is_inf",                                         # Returns which elements of x are Inf.
    "is_nan",                                         # Returns which elements of x are NaN.
    "is_non_decreasing",                              # Returns True if x is non-decreasing.
    "is_strictly_increasing",                         # Returns True if x is strictly increasing.
    "l2_normalize",                                   # Normalizes along dimension axis using an L2 norm. (deprecated arguments)
    "lbeta",                                          # Computes log(beta), reducing along the last dimension.
    "less",                                           # Returns the truth value of (x < y) element-wise.
    "less_equal",                                     # Returns the truth value of (x <= y) element-wise.
    "lgamma",                                         # Computes the log of the absolute value of Gamma(x) element-wise.
    "log",                                            # Computes natural logarithm of x element-wise.
    "log1p",                                          # Computes natural logarithm of (1 + x) element-wise.
    "log_sigmoid",                                    # Computes log sigmoid of x element-wise.
    "log_softmax",                                    # Computes log softmax activations.
    "logical_and",                                    # Returns the truth value of x AND y element-wise.
    "logical_not",                                    # Returns the truth value of NOT x element-wise.
    "logical_or",                                     # Returns the truth value of x OR y element-wise.
    "logical_xor",                                    # Logical XOR function.
    "maximum",                                        # Returns the max of x and y (i.e. x > y ? x : y) element-wise.
    "minimum",                                        # Returns the min of x and y (i.e. x < y ? x : y) element-wise.
    "mod",                                            # Returns element-wise remainder of division.
    "multiply",                                       # Returns an element-wise x * y.
    "multiply_no_nan",                                # Computes the product of x and y and returns 0 if the y is zero, even if x is NaN or infinite.
    "ndtri",                                          # Compute quantile of Standard Normal.
    "negative",                                       # Computes numerical negative value element-wise.
    "nextafter",                                      # Returns the next representable value of x1 in the direction of x2, element-wise.
    "not_equal",                                      # Returns the truth value of (x != y) element-wise.
    "polygamma",                                      # Compute the polygamma function.
    "polyval",                                        # Computes the elementwise value of a polynomial.
    "pow",                                            # Computes the power of one value to another.
    "real",                                           # Returns the real part of a complex (or real) tensor.
    "reciprocal",                                     # Computes the reciprocal of x element-wise.
    "reciprocal_no_nan",                              # Performs a safe reciprocal operation, element wise.
    "reduce_all",                                     # Computes tf.math.logical_and of elements across dimensions of a tensor.
    "reduce_any",                                     # Computes tf.math.logical_or of elements across dimensions of a tensor.
    "reduce_euclidean_norm",                          # Computes the Euclidean norm of elements across dimensions of a tensor.
    "reduce_logsumexp",                               # Computes log(sum(exp(elements across dimensions of a tensor))).
    "reduce_max",                                     # Computes tf.math.maximum of elements across dimensions of a tensor.
    "reduce_mean",                                    # Computes the mean of elements across dimensions of a tensor.
    "reduce_min",                                     # Computes the tf.math.minimum of elements across dimensions of a tensor.
    "reduce_prod",                                    # Computes tf.math.multiply of elements across dimensions of a tensor.
    "reduce_std",                                     # Computes the standard deviation of elements across dimensions of a tensor.
    "reduce_sum",                                     # Computes the sum of elements across dimensions of a tensor.
    "reduce_variance",                                # Computes the variance of elements across dimensions of a tensor.
    "rint",                                           # Returns element-wise integer closest to x.
    "round",                                          # Rounds the values of a tensor to the nearest integer, element-wise.
    "rsqrt",                                          # Computes reciprocal of square root of x element-wise.
    "scalar_mul",                                     # Multiplies a scalar times a Tensor or IndexedSlices object.
    "segment_max",                                    # Computes the maximum along segments of a tensor.
    "segment_mean",                                   # Computes the mean along segments of a tensor.
    "segment_min",                                    # Computes the minimum along segments of a tensor.
    "segment_prod",                                   # Computes the product along segments of a tensor.
    "segment_sum",                                    # Computes the sum along segments of a tensor.
    "sigmoid",                                        # Computes sigmoid of x element-wise.
    "sign",                                           # Returns an element-wise indication of the sign of a number.
    "sin",                                            # Computes sine of x element-wise.
    "sinh",                                           # Computes hyperbolic sine of x element-wise.
    "sobol_sample",                                   # Generates points from the Sobol sequence.
    "softmax",                                        # Computes softmax activations.
    "softplus",                                       # Computes elementwise softplus: softplus(x) = log(exp(x) + 1).
    "softsign",                                       # Computes softsign: features / (abs(features) + 1).
    "sqrt",                                           # Computes element-wise square root of the input tensor.
    "square",                                         # Computes square of x element-wise.
    "squared_difference",                             # Returns conj(x - y)(x - y) element-wise.
    "subtract",                                       # Returns x - y element-wise.
    "tan",                                            # Computes tan of x element-wise.
    "tanh",                                           # Computes hyperbolic tangent of x element-wise.
    "top_k",                                          # Finds values and indices of the k largest entries for the last dimension.
    "truediv",                                        # Divides x / y elementwise (using Python 3 division operator semantics).
    "unsorted_segment_max",                           # Computes the maximum along segments of a tensor.
    "unsorted_segment_mean",                          # Computes the mean along segments of a tensor.
    "unsorted_segment_min",                           # Computes the minimum along segments of a tensor.
    "unsorted_segment_prod",                          # Computes the product along segments of a tensor.
    "unsorted_segment_sqrt_n",                        # Computes the sum along segments of a tensor divided by the sqrt(N).
    "unsorted_segment_sum",                           # Computes the sum along segments of a tensor.
    "xdivy",                                          # Computes x / y.
    "xlog1py",                                        # Compute x * log1p(y).
    "xlogy",                                          # Returns 0 if x == 0, and x * log(y) otherwise, elementwise.
    "zero_fraction",                                  # Returns the fraction of zeros in value.
    "zeta",                                           # Compute the Hurwitz zeta function.
]


tf_all_list=[
'units',
'loss',    
'Dense(',
'batch_size',
'input_shape',
'kernel_initializer',
'activation',
'epochs',
'optimizer',
'learning_rate',
'kernel_regularizer',
'batch_size',
'dropout',
'filters',
'kernel_size',
'pool_size',
'filters',
'Dropout(',
'bias_initializer',
'strides',
'padding',
'data_format',
'dilation_rate',
'groups',
'seed',
'axis',
'from_logits',
'label_smoothing',
'use_cudnn_on_gpu',
'ksize',
'keep_prob',
'rate',
'training',
'momentum',
'center',
'scale',
'beta_initializer',
'gamma_initializer',
'moving_mean_initializer',
'moving_variance_initializer',
'depth_radius',
'bias',
'alpha',
'l1',
'l2',
'trainable',
'beta1',
'beta2',
'epsilon',
'decay',
'gamma',
'global_step',
'decay_steps',
'decay_rate',
'capacity',
'max_to_keep',
'transformer_vocab_size',
'transformer_maxlen',
'tf.keras.layers.AbstractRNNCell()',
'tf.keras.layers.Activation()',
'tf.keras.layers.ActivityRegularization()',
'tf.keras.layers.Add()',
'tf.keras.layers.AdditiveAttention()',
'tf.keras.layers.AlphaDropout()',
'tf.keras.layers.Attention()',
'tf.keras.layers.Average()',
'tf.keras.layers.AveragePooling1D()',
'tf.keras.layers.AveragePooling2D()',
'tf.keras.layers.AveragePooling3D()',
'tf.keras.layers.AvgPool1D()',
'tf.keras.layers.AvgPool2D()',
'tf.keras.layers.AvgPool3D()',
'tf.keras.layers.BatchNormalization()',
'tf.keras.layers.Bidirectional()',
'tf.keras.layers.CategoryEncoding()',
'tf.keras.layers.CenterCrop()',
'tf.keras.layers.Concatenate()',
'tf.keras.layers.Conv1D()',
'tf.keras.layers.Conv1DTranspose()',
'tf.keras.layers.Conv2D()',
'tf.keras.layers.Conv2DTranspose()',
'tf.keras.layers.Conv3D()',
'tf.keras.layers.Conv3DTranspose()',
'tf.keras.layers.Dense()',
'tf.keras.layers.ConvLSTM1D()',
'tf.keras.layers.ConvLSTM2D()',
'tf.keras.layers.ConvLSTM3D()',
'tf.keras.layers.Convolution1D()',
'tf.keras.layers.Convolution1DTranspose()',
'tf.keras.layers.Convolution2D()',
'tf.keras.layers.Convolution2DTranspose()',
'tf.keras.layers.Convolution3D()',
'tf.keras.layers.Convolution3DTranspose()',
'tf.keras.layers.Cropping1D()',
'tf.keras.layers.Cropping2D()',
'tf.keras.layers.Cropping3D()',
'tf.keras.layers.SpectralNormalization()',
'tf.keras.layers.StackedRNNCells()',
'tf.keras.layers.StringLookup()',
'tf.keras.layers.Subtract()',
'tf.keras.layers.TextVectorization()',
'tf.keras.layers.ThresholdedReLU()',
'tf.keras.layers.TimeDistributed()',
'tf.keras.layers.UnitNormalization()',
'tf.keras.layers.UpSampling1D()',
'tf.keras.layers.UpSampling2D()',
'tf.keras.layers.UpSampling3D()',
'tf.keras.layers.Wrapper()',
'tf.keras.layers.ZeroPadding1D()',
'tf.keras.layers.ZeroPadding2D()',
'tf.keras.layers.ZeroPadding3D()',
'tf.keras.layers.add()',
'tf.keras.layers.average()',
'tf.keras.layers.concatenate()',
'tf.keras.layers.deserialize()',
'tf.keras.layers.dot()',
'tf.keras.layers.maximum()',
'tf.keras.layers.minimum()',
'tf.keras.layers.multiply()',
'tf.keras.layers.serialize()',
'tf.keras.layers.subtract()',
'tf.keras.activations.deserialize()',
'tf.keras.activations.elu()',
'tf.keras.activations.exponential()',
'tf.keras.activations.gelu()',
'tf.keras.activations.get()',
'tf.keras.activations.hard_sigmoid()',
'tf.keras.activations.linear()',
'tf.keras.activations.mish()',
'tf.keras.activations.relu()',
'tf.keras.activations.selu()',
'tf.keras.activations.serialize()',
'tf.keras.activations.sigmoid()',
'tf.keras.activations.softmax()',
'tf.keras.activations.softplus()',
'tf.keras.activations.softsign()',
'tf.keras.activations.swish()',
'tf.keras.activations.tanh()',
'tf.keras.losses.BinaryCrossentropy()',
'tf.keras.losses.BinaryFocalCrossentropy()',
'tf.keras.losses.CategoricalCrossentropy()',
'tf.keras.losses.CategoricalFocalCrossentropy()',
'tf.keras.losses.CategoricalHinge()',
'tf.keras.losses.CosineSimilarity()',
'tf.keras.losses.Hinge()',
'tf.keras.losses.Huber()',
'tf.keras.losses.KLD()',
'tf.keras.losses.KLDivergence()',
'tf.keras.losses.LogCosh()',
'tf.keras.losses.Loss()',
'tf.keras.losses.MAE()',
'tf.keras.losses.MAPE()',
'tf.keras.losses.MSE()',
'tf.keras.losses.MSLE()',
'tf.keras.losses.MeanAbsoluteError()',
'tf.keras.losses.MeanAbsolutePercentageError()',
'tf.keras.losses.MeanSquaredError()',
'tf.keras.losses.MeanSquaredLogarithmicError()',
'tf.keras.losses.Poisson()',
'tf.keras.losses.Reduction()',
'tf.keras.losses.SparseCategoricalCrossentropy()',
'tf.keras.losses.SquaredHinge()',
'tf.keras.losses.binary_crossentropy()',
'tf.keras.losses.binary_focal_crossentropy()',
'tf.keras.losses.categorical_crossentropy()',
'tf.keras.losses.categorical_focal_crossentropy()',
'tf.keras.losses.categorical_hinge()',
'tf.keras.losses.cosine_similarity()',
'tf.keras.losses.deserialize()',
'tf.keras.losses.get()',
'tf.keras.losses.hinge()',
'tf.keras.losses.huber()',
'tf.keras.losses.kl_divergence()',
'tf.keras.losses.kld()',
'tf.keras.losses.kullback_leibler_divergence()',
'tf.keras.losses.log_cosh()',
'tf.keras.losses.logcosh()',
'tf.keras.losses.mae()',
'tf.keras.losses.mape()',
'tf.keras.losses.mean_absolute_error()',
'tf.keras.losses.mean_absolute_percentage_error()',
'tf.keras.losses.mean_squared_error()',
'tf.keras.losses.mean_squared_logarithmic_error()',
'tf.keras.losses.mse()',
'tf.keras.losses.msle()',
'tf.keras.losses.poisson()',
'tf.keras.losses.serialize()',
'tf.keras.losses.sparse_categorical_crossentropy()',
'tf.keras.losses.squared_hinge()',
'tf.keras.optimizers.Adadelta()',
'tf.keras.optimizers.Adafactor()',
'tf.keras.optimizers.Adagrad()',
'tf.keras.optimizers.Adam()',
'tf.keras.optimizers.Adamax()',
'tf.keras.optimizers.Ftrl()',
'tf.keras.optimizers.Nadam()',
'tf.keras.optimizers.RMSprop()',
'tf.keras.optimizers.SGD()',
'tf.optimizers.deserialize()',
'tf.optimizers.get()',
'tf.keras.optimizers.legacy.Adadelta()',
'tf.keras.optimizers.legacy.Adagrad()',
'tf.keras.optimizers.legacy.Adam()',
'tf.keras.optimizers.legacy.Adamax()',
'tf.keras.optimizers.legacy.Ftrl()',
'tf.keras.optimizers.legacy.Nadam()',
'tf.keras.optimizers.legacy.RMSprop()',
'tf.keras.optimizers.legacy.SGD()',
'tf.keras.optimizers.schedules.CosineDecay()',
'tf.keras.optimizers.schedules.ExponentialDecay()',
'tf.keras.optimizers.schedules.PolynomialDecay()',
'tf.keras.optimizers.schedules.deserialize()',
'tf.keras.optimizers.schedules.serialize()',
'tf.nn.RNNCellDeviceWrapper()',
'tf.nn.RNNCellDropoutWrapper()',
'tf.nn.RNNCellResidualWrapper()',
'tf.nn.all_candidate_sampler()',
'tf.nn.approx_max_k()',
'tf.nn.approx_min_k()',
'tf.nn.atrous_conv2d()',
'tf.nn.atrous_conv2d_transpose()',
'tf.nn.avg_pool()',
'tf.nn.avg_pool1d()',
'tf.nn.avg_pool2d()',
'tf.nn.avg_pool3d()',
'tf.nn.batch_norm_with_global_normalization()',
'tf.nn.batch_normalization()',
'tf.nn.bias_add()',
'tf.nn.collapse_repeated()',
'tf.nn.compute_accidental_hits()',
'tf.nn.compute_average_loss()',
'tf.nn.conv1d()',
'tf.nn.conv1d_transpose()',
'tf.nn.conv2d()',
'tf.nn.conv2d_transpose()',
'tf.nn.conv3d()',
'tf.nn.conv3d_transpose()',
'tf.nn.conv_transpose()',
'tf.nn.convolution()',
'tf.nn.crelu()',
'tf.nn.ctc_beam_search_decoder()',
'tf.nn.ctc_greedy_decoder()',
'tf.nn.ctc_loss()',
'tf.nn.ctc_unique_labels()',
'tf.nn.depth_to_space()',
'tf.nn.depthwise_conv2d()',
'tf.nn.depthwise_conv2d_backprop_filter()',
'tf.nn.depthwise_conv2d_backprop_input()',
'tf.nn.dilation2d()',
'tf.nn.dropout()',
'tf.nn.elu()',
'tf.nn.embedding_lookup()',
'tf.nn.embedding_lookup_sparse()',
'tf.nn.erosion2d()',
'tf.nn.fixed_unigram_candidate_sampler()',
'tf.nn.fractional_avg_pool()',
'tf.nn.fractional_max_pool()',
'tf.nn.gelu()',
'tf.nn.in_top_k()',
'tf.nn.isotonic_regression()',
'tf.nn.l2_loss()',
'tf.nn.l2_normalize()',
'tf.nn.leaky_relu()',
'tf.nn.learned_unigram_candidate_sampler()',
'tf.nn.local_response_normalization()',
'tf.nn.log_poisson_loss()',
'tf.nn.log_softmax()',
'tf.nn.lrn()',
'tf.nn.max_pool()',
'tf.nn.max_pool1d()',
'tf.nn.max_pool2d()',
'tf.nn.max_pool3d()',
'tf.nn.max_pool_with_argmax()',
'tf.nn.moments()',
'tf.nn.nce_loss()',
'tf.nn.normalize_moments()',
'tf.nn.pool()',
'tf.nn.relu()',
'tf.nn.relu6()',
'tf.nn.safe_embedding_lookup_sparse()',
'tf.nn.sampled_softmax_loss()',
'tf.nn.scale_regularization_loss()',
'tf.nn.selu()',
'tf.nn.separable_conv2d()',
'tf.nn.sigmoid()',
'tf.nn.sigmoid_cross_entropy_with_logits()',
'tf.nn.silu()',
'tf.nn.softmax()',
'tf.nn.softmax_cross_entropy_with_logits()',
'tf.nn.softplus()',
'tf.nn.softsign()',
'tf.nn.space_to_batch()',
'tf.nn.space_to_depth()',
'tf.nn.sparse_softmax_cross_entropy_with_logits()',
'tf.nn.sufficient_statistics()',
'tf.nn.swish()',
'tf.nn.tanh()',
'tf.nn.top_k()',
'tf.nn.weighted_cross_entropy_with_logits()',
'tf.nn.weighted_moments()',
'tf.nn.with_space_to_batch()',
'tf.nn.zero_fraction()',
'tf.raw_ops.BlockLSTM()',
'tf.raw_ops.BlockLSTMGrad()',
'tf.raw_ops.BlockLSTMGradV2()',
'tf.raw_ops.BlockLSTMV2()',
'tf.raw_ops.BoostedTreesTrainingPredict()',
'tf.raw_ops.CSRSparseMatrixToDense()',
'tf.raw_ops.CTCLoss()',
'tf.raw_ops.CTCLossV2()',
'tf.raw_ops.Conv()',
'tf.raw_ops.Conv2D()',
'tf.raw_ops.Conv2DBackpropFilter()',
'tf.raw_ops.Conv2DBackpropFilterV2()',
'tf.raw_ops.Conv2DBackpropInput()',
'tf.raw_ops.Conv2DBackpropInputV2()',
'tf.raw_ops.Conv3D()',
'tf.raw_ops.Conv3DBackpropFilter()',
'tf.raw_ops.Conv3DBackpropFilterV2()',
'tf.raw_ops.Conv3DBackpropInput()',
'tf.raw_ops.Conv3DBackpropInputV2()',
'tf.raw_ops.CudnnRNN()',
'tf.raw_ops.CudnnRNNBackprop()',
'tf.raw_ops.CudnnRNNBackpropV2()',
'tf.raw_ops.CudnnRNNBackpropV3()',
'tf.raw_ops.CudnnRNNCanonicalToParams()',
'tf.raw_ops.CudnnRNNCanonicalToParamsV2()',
'tf.raw_ops.CudnnRNNParamsSize()',
'tf.raw_ops.CudnnRNNParamsToCanonical()',
'tf.raw_ops.CudnnRNNParamsToCanonicalV2()',
'tf.raw_ops.CudnnRNNV2()',
'tf.raw_ops.CudnnRNNV3()',
'tf.raw_ops.DenseBincount()',
'tf.raw_ops.DenseCountSparseOutput()',
'tf.raw_ops.DenseToCSRSparseMatrix()',
'tf.raw_ops.DenseToDenseSetOperation()',
'tf.raw_ops.DenseToSparseBatchDataset()',
'tf.raw_ops.DenseToSparseSetOperation()',
'tf.raw_ops.DepthwiseConv2dNative()',
'tf.raw_ops.DepthwiseConv2dNativeBackpropFilter()',
'tf.raw_ops.DepthwiseConv2dNativeBackpropInput()',
'tf.raw_ops.FusedPadConv2D()',
'tf.raw_ops.FusedResizeAndPadConv2D()',
'tf.raw_ops.GRUBlockCell()',
'tf.raw_ops.GRUBlockCellGrad()',
'tf.raw_ops.L2Loss()',
'tf.raw_ops.LSTMBlockCell()',
'tf.raw_ops.LSTMBlockCellGrad()',
'tf.raw_ops.QuantizedConv2D()',
'tf.raw_ops.QuantizedConv2DAndRelu()',
'tf.raw_ops.QuantizedConv2DAndReluAndRequantize()',
'tf.raw_ops.QuantizedConv2DAndRequantize()',
'tf.raw_ops.QuantizedConv2DPerChannel()',
'tf.raw_ops.QuantizedConv2DWithBias()',
'tf.raw_ops.QuantizedConv2DWithBiasAndRelu()',
'tf.raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize()',
'tf.raw_ops.QuantizedConv2DWithBiasAndRequantize()',
'tf.raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize()',
'tf.raw_ops.QuantizedConv2DWithBiasSumAndRelu()',
'tf.raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize()',
'tf.raw_ops.QuantizedDepthwiseConv2D()',
'tf.raw_ops.QuantizedDepthwiseConv2DWithBias()',
'tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu()',
'tf.raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize()',
'tf.raw_ops.RecvTPUEmbeddingActivations()',
'tf.raw_ops.SdcaOptimizer()',
'tf.raw_ops.SdcaOptimizerV2()',
'tf.raw_ops.SparseDenseCwiseAdd()',
'tf.raw_ops.SparseDenseCwiseDiv()',
'tf.raw_ops.SparseDenseCwiseMul()',
'tf.raw_ops.SparseTensorDenseAdd()',
'tf.raw_ops.SparseTensorDenseMatMul()',
'tf.raw_ops.SparseToDense()',
'tf.raw_ops.TPUEmbeddingActivations()',
'tf.raw_ops.UniformQuantizedConvolution()',
'tf.raw_ops.UniformQuantizedConvolutionHybrid()',
'tf.train.BytesList()',
'tf.train.Checkpoint()',
'tf.train.CheckpointManager()',
'tf.train.CheckpointOptions()',
'tf.train.CheckpointView()',
'tf.train.ClusterDef()',
'tf.train.ClusterSpec()',
'tf.train.Coordinator()',
'tf.train.Example()',
'tf.train.ExponentialMovingAverage()',
'tf.train.Feature()',
'tf.train.FeatureList()',
'tf.train.FeatureLists()',
'tf.train.Features()',
'tf.train.FloatList()',
'tf.train.Int64List()',
'tf.train.JobDef()',
'tf.train.SequenceExample()',
'tf.train.ServerDef()',
'tf.train.TrackableView()',
'tf.train.checkpoints_iterator()',
'tf.train.experimental()',
'tf.train.experimental.PythonState()',
'tf.train.get_checkpoint_state()',
'tf.train.latest_checkpoint()',
'tf.train.list_variables()',
'tf.train.load_checkpoint()',
'tf.train.load_variable()',
]

tf_all_mutation_code_list = [
'units',
'loss',
'Dense(',
'optimizer',   
'batch_size',
'activation',
'kernel_initializer',
'dropout',    
'use_bias',    
'kernel_size',    
'learning_rate',    
'input_shape',
'pool_size',
'filters',
'Dropout(',
'bias_initializer',
'strides',
'padding',
'data_format',
'dilation_rate',
'groups',
'seed',
'axis',
'from_logits',
'label_smoothing',
'use_cudnn_on_gpu',
'ksize',
'keep_prob',
'rate',
'training',
'momentum',
'center',
'scale',
'beta_initializer',
'gamma_initializer',
'moving_mean_initializer',
'moving_variance_initializer',
'depth_radius',
'bias',
'alpha',
'l1',
'l2',
'trainable',
'beta1',
'beta2',
'epsilon',
'decay',
'gamma',
'global_step',
'decay_steps',
'decay_rate',
'capacity',
'max_to_keep',
'transformer_vocab_size',
'transformer_maxlen',
'kernel_regularizer',
'layers.AbstractRNNCell()',
'layers.Activation()',
'layers.ActivityRegularization()',
'layers.Add()',
'layers.AdditiveAttention()',
'layers.AlphaDropout()',
'layers.Attention()',
'tlayers.Average()',
'layers.AveragePooling1D()',
'layers.AveragePooling2D()',
'layers.AveragePooling3D()',    
'layers.AvgPool1D()',
'layers.AvgPool2D()',
'layers.AvgPool3D()',
'layers.BatchNormalization()',
'layers.Bidirectional()',
'layers.CategoryEncoding()',
'layers.CenterCrop()',
'layers.Concatenate()',
'layers.Conv1D()',
'layers.Conv1DTranspose()',
'layers.Conv2D()',
'layers.Conv2DTranspose()',
'layers.Conv3D()',
'layers.Conv3DTranspose()',
'layers.ConvLSTM1D()',
'layers.ConvLSTM2D()',
'layers.ConvLSTM3D()',
'layers.Convolution1D()',
'layers.Convolution1DTranspose()',
'layers.Convolution2D()',
'layers.Convolution2DTranspose()',
'layers.Convolution3D()',
'layers.Convolution3DTranspose()',
'layers.Cropping1D()',
'layers.Cropping2D()',
'layers.Cropping3D()',
'layers.SpectralNormalization()',
'layers.StackedRNNCells()',
'layers.StringLookup()',
'layers.Subtract()',
'layers.TextVectorization()',
'layers.ThresholdedReLU()',
'layers.TimeDistributed()',
'layers.UnitNormalization()',
'layers.UpSampling1D()',
'layers.UpSampling2D()',
'layers.UpSampling3D()',
'layers.Wrapper()',
'layers.ZeroPadding1D()',
'layers.ZeroPadding2D()',
'layers.ZeroPadding3D()',
'layers.add()',
'layers.average()',
'layers.concatenate()',
'layers.deserialize()',
'layers.dot()',
'layers.maximum()',
'layers.minimum()',
'layers.multiply()',
'layers.serialize()',
'layers.subtract()',
'activations.deserialize()',
'activations.elu()',
'activations.exponential()',
'activations.gelu()',
'activations.get()',
'activations.hard_sigmoid()',
'activations.linear()',
'activations.mish()',
'activations.relu()',
'activations.selu()',
'activations.serialize()',
'activations.sigmoid()',
'activations.softmax()',
'activations.softplus()',
'activations.softsign()',
'activations.swish()',
'activations.tanh()',
'losses.BinaryCrossentropy()',
'losses.BinaryFocalCrossentropy()',
'losses.CategoricalCrossentropy()',
'losses.CategoricalFocalCrossentropy()',
'losses.CategoricalHinge()',
'losses.CosineSimilarity()',
'losses.Hinge()',
'losses.Huber()',
'losses.KLD()',
'losses.KLDivergence()',
'losses.LogCosh()',
'losses.Loss()',
'losses.MAE()',
'losses.MAPE()',
'losses.MSE()',
'losses.MSLE()',
'losses.MeanAbsoluteError()',
'losses.MeanAbsolutePercentageError()',
'losses.MeanSquaredError()',
'losses.MeanSquaredLogarithmicError()',
'losses.Poisson()',
'losses.Reduction()',
'losses.SparseCategoricalCrossentropy()',
'losses.SquaredHinge()',
'losses.binary_crossentropy()',
'losses.binary_focal_crossentropy()',
'losses.categorical_crossentropy()',
'losses.categorical_focal_crossentropy()',
'losses.categorical_hinge()',
'losses.cosine_similarity()',
'losses.deserialize()',
'losses.get()',
'losses.hinge()',
'losses.huber()',
'losses.kl_divergence()',
'losses.kld()',
'losses.kullback_leibler_divergence()',
'losses.log_cosh()',
'losses.logcosh()',
'losses.mae()',
'losses.mape()',
'losses.mean_absolute_error()',
'losses.mean_absolute_percentage_error()',
'losses.mean_squared_error()',
'losses.mean_squared_logarithmic_error()',
'losses.mse()',
'losses.msle()',
'losses.poisson()',
'losses.serialize()',
'losses.sparse_categorical_crossentropy()',
'losses.squared_hinge()',
'optimizers.Adadelta()',
'optimizers.Adafactor()',
'optimizers.Adagrad()',
'optimizers.Adam()',
'optimizers.Adamax()',
'optimizers.Ftrl()',
'optimizers.Nadam()',
'optimizers.RMSprop()',
'optimizers.SGD()',
'optimizers.deserialize()',
'optimizers.get()',
'optimizers.legacy.Adadelta()',
'optimizers.legacy.Adagrad()',
'optimizers.legacy.Adam()',
'optimizers.legacy.Adamax()',
'optimizers.legacy.Ftrl()',
'optimizers.legacy.Nadam()',
'optimizers.legacy.RMSprop()',
'optimizers.legacy.SGD()',
'optimizers.schedules.CosineDecay()',
'optimizers.schedules.ExponentialDecay()',
'optimizers.schedules.PolynomialDecay()',
'optimizers.schedules.deserialize()',
'optimizers.schedules.serialize()',
'nn.RNNCellDeviceWrapper',
'nn.RNNCellDropoutWrapper',
'nn.RNNCellResidualWrapper',
'nn.all_candidate_sampler',
'nn.approx_max_k',
'nn.approx_min_k',
'nn.atrous_conv2d',
'nn.atrous_conv2d_transpose',
'nn.avg_pool',
'nn.avg_pool1d',
'nn.avg_pool2d',
'nn.avg_pool3d',
'nn.batch_norm_with_global_normalization',
'nn.batch_normalization',
'nn.bias_add',
'nn.collapse_repeated',
'nn.compute_accidental_hits',
'nn.compute_average_loss',
'nn.conv1d',
'nn.conv1d_transpose',
'nn.conv2d',
'nn.conv2d_transpose',
'nn.conv3d',
'nn.conv3d_transpose',
'nn.conv_transpose',
'nn.convolution',
'nn.crelu',
'nn.ctc_beam_search_decoder',
'nn.ctc_greedy_decoder',
'nn.ctc_loss',
'nn.ctc_unique_labels',
'nn.depth_to_space',
'nn.depthwise_conv2d',
'nn.depthwise_conv2d_backprop_filter',
'nn.depthwise_conv2d_backprop_input',
'nn.dilation2d',
'nn.dropout',
'nn.elu',
'nn.embedding_lookup',
'nn.embedding_lookup_sparse',
'nn.erosion2d',
'nn.fixed_unigram_candidate_sampler',
'nn.fractional_avg_pool',
'nn.fractional_max_pool',
'nn.gelu',
'nn.in_top_k',
'nn.isotonic_regression',
'nn.l2_loss',
'nn.l2_normalize',
'nn.leaky_relu',
'nn.learned_unigram_candidate_sampler',
'nn.local_response_normalization',
'nn.log_poisson_loss',
'nn.log_softmax',
'nn.lrn',
'nn.max_pool',
'nn.max_pool1d',
'nn.max_pool2d',
'nn.max_pool3d',
'nn.max_pool_with_argmax',
'nn.moments',
'nn.nce_loss',
'nn.normalize_moments',
'nn.pool',
'nn.relu',
'nn.relu6',
'nn.safe_embedding_lookup_sparse',
'nn.sampled_softmax_loss',
'nn.scale_regularization_loss',
'nn.selu',
'nn.separable_conv2d',
'nn.sigmoid',
'nn.sigmoid_cross_entropy_with_logits',
'nn.silu',
'nn.softmax',
'nn.softmax_cross_entropy_with_logits',
'nn.softplus',
'nn.softsign',
'nn.space_to_batch',
'nn.space_to_depth',
'nn.sparse_softmax_cross_entropy_with_logits',
'nn.sufficient_statistics',
'nn.swish',
'nn.tanh',
'nn.top_k',
'nn.weighted_cross_entropy_with_logits',
'nn.weighted_moments',
'nn.with_space_to_batch',
'nn.zero_fraction',
'raw_ops.BlockLSTM',
'raw_ops.BlockLSTMGrad',
'raw_ops.BlockLSTMGradV2',
'raw_ops.BlockLSTMV2',
'raw_ops.BoostedTreesTrainingPredict',
'raw_ops.CSRSparseMatrixToDense',
'raw_ops.CTCLoss',
'raw_ops.CTCLossV2',
'raw_ops.Conv',
'raw_ops.Conv2D',
'raw_ops.Conv2DBackpropFilter',
'raw_ops.Conv2DBackpropFilterV2',
'raw_ops.Conv2DBackpropInput',
'raw_ops.Conv2DBackpropInputV2',
'raw_ops.Conv3D',
'raw_ops.Conv3DBackpropFilter',
'raw_ops.Conv3DBackpropFilterV2',
'raw_ops.Conv3DBackpropInput',
'raw_ops.Conv3DBackpropInputV2',
'raw_ops.CudnnRNN',
'raw_ops.CudnnRNNBackprop',
'raw_ops.CudnnRNNBackpropV2',
'raw_ops.CudnnRNNBackpropV3',
'raw_ops.CudnnRNNCanonicalToParams',
'raw_ops.CudnnRNNCanonicalToParamsV2',
'raw_ops.CudnnRNNParamsSize',
'raw_ops.CudnnRNNParamsToCanonical',
'raw_ops.CudnnRNNParamsToCanonicalV2',
'raw_ops.CudnnRNNV2',
'raw_ops.CudnnRNNV3',
'raw_ops.DenseBincount',
'raw_ops.DenseCountSparseOutput',
'raw_ops.DenseToCSRSparseMatrix',
'raw_ops.DenseToDenseSetOperation',
'raw_ops.DenseToSparseBatchDataset',
'raw_ops.DenseToSparseSetOperation',
'raw_ops.DepthwiseConv2dNative',
'raw_ops.DepthwiseConv2dNativeBackpropFilter',
'raw_ops.DepthwiseConv2dNativeBackpropInput',
'raw_ops.FusedPadConv2D',
'raw_ops.FusedResizeAndPadConv2D',
'raw_ops.GRUBlockCell',
'raw_ops.GRUBlockCellGrad',
'raw_ops.L2Loss',
'raw_ops.LSTMBlockCell',
'raw_ops.LSTMBlockCellGrad',
'raw_ops.QuantizedConv2D',
'raw_ops.QuantizedConv2DAndRelu',
'raw_ops.QuantizedConv2DAndReluAndRequantize',
'raw_ops.QuantizedConv2DAndRequantize',
'raw_ops.QuantizedConv2DPerChannel',
'raw_ops.QuantizedConv2DWithBias',
'raw_ops.QuantizedConv2DWithBiasAndRelu',
'raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize',
'raw_ops.QuantizedConv2DWithBiasAndRequantize',
'raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize',
'raw_ops.QuantizedConv2DWithBiasSumAndRelu',
'raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize',
'raw_ops.QuantizedDepthwiseConv2D',
'raw_ops.QuantizedDepthwiseConv2DWithBias',
'raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu',
'raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize',
'raw_ops.RecvTPUEmbeddingActivations',
'raw_ops.SdcaOptimizer',
'raw_ops.SdcaOptimizerV2',
'raw_ops.SparseDenseCwiseAdd',
'raw_ops.SparseDenseCwiseDiv',
'raw_ops.SparseDenseCwiseMul',
'raw_ops.SparseTensorDenseAdd',
'raw_ops.SparseTensorDenseMatMul',
'raw_ops.SparseToDense',
'raw_ops.TPUEmbeddingActivations',
'raw_ops.UniformQuantizedConvolution',
'raw_ops.UniformQuantizedConvolutionHybrid',
'train.BytesList',
'train.Checkpoint',
'train.CheckpointManager',
'train.CheckpointOptions',
'train.CheckpointView',
'train.ClusterDef',
'train.ClusterSpec',
'train.Coordinator',
'train.Example',
'train.ExponentialMovingAverage',
'train.Feature',
'train.FeatureList',
'train.FeatureLists',
'train.Features',
'train.FloatList',
'train.Int64List',
'train.JobDef',
'train.SequenceExample',
'train.ServerDef',
'train.TrackableView',
'train.checkpoints_iterator',
'train.experimental',
'train.experimental.PythonState',
'train.get_checkpoint_state',
'train.latest_checkpoint',
'train.list_variables',
'train.load_checkpoint',
'train.load_variable',
]

tf_keras_layers_AbstractRNNCell_Mutation_List = [
    # Scenarios with erroneous or inappropriate values
    "units='invalid_data', activation=123, use_bias='wrong', kernel_initializer=10, recurrent_initializer='unknown', bias_initializer='none'",
    "units=10000, activation='relu', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros'",
    "activation='wrong_function', use_bias=True",
    "units=128, activation='relu'",
    "",
    # Typical parameter combinations
    "units=128, activation='relu', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros'",
    "units=256, activation='tanh', use_bias=False, kernel_initializer='he_normal', recurrent_initializer='orthogonal', bias_initializer='ones'",
    "units=64, activation='sigmoid', use_bias=True, kernel_initializer='glorot_normal', recurrent_initializer='identity', bias_initializer='zeros'",
    "units=128, activation='linear', use_bias=False, kernel_initializer='lecun_normal', recurrent_initializer='uniform', bias_initializer='ones'",
    "units=100, activation='relu', use_bias=True, kernel_initializer='he_uniform', recurrent_initializer='glorot_normal', bias_initializer='zeros'",
    "units=150, activation='elu', use_bias=False, kernel_initializer='lecun_uniform', recurrent_initializer='glorot_uniform', bias_initializer='ones'",
    "units=200, activation='relu', use_bias=True, kernel_initializer='normal', recurrent_initializer='he_normal', bias_initializer='zeros'",
    "units=128, activation='swish', use_bias=False, kernel_initializer='orthogonal', recurrent_initializer='lecun_normal', bias_initializer='ones'",
    "units=120, activation='selu', use_bias=True, kernel_initializer='identity', recurrent_initializer='he_uniform', bias_initializer='zeros'",
    "units=256, activation='relu', use_bias=False, kernel_initializer='glorot_uniform', recurrent_initializer='uniform', bias_initializer='ones'"
]
tf_keras_layers_ActivityRegularization_Mutation_List = [
    # Typical parameter combinations
    "l1=0.01, l2=0.01",
    "l1=0.1, l2=0.1",
    "l1=0.5, l2=0.5",
    "l1=0.05, l2=0.05",
    "l1=0, l2=0",
    "l1=0.03, l2=0.03",
    "l1=0.2, l2=0.2",
    "l1=0.15, l2=0.15",
    "l1=0.07, l2=0.07",
    "l1=0.25, l2=0.25",
    # Scenarios with erroneous or inappropriate values
    "l1=-0.01, l2=-0.01",
    "l1='invalid', l2='invalid'",
    "l1=None, l2=None",
    "l1=0.01",
    "l2=0.01"
]
tf_keras_layers_AdditiveAttention_Mutation_List = [
    # Typical parameter combinations
    "use_scale=True, causal=True, dropout=0.5", "use_scale=False, causal=False, dropout=0.3",
    "use_scale=True, dropout=0.1", "use_scale=False, dropout=0.6",
    "use_scale=True, causal=True, dropout=0", "use_scale=False, causal=True, dropout=0.2",
    "use_scale=True, dropout=0.4", "use_scale=False, dropout=0.1",
    "use_scale=True, causal=False, dropout=0.3", "use_scale=False, causal=False, dropout=0.5",
    # Scenarios with erroneous or inappropriate values
    "use_scale='invalid', causal=123, dropout=None", "use_scale=None, dropout='invalid'",
    "causal='true', dropout=1.5", "use_scale=0, dropout=0", "causal=None, dropout=-0.1"
]
tf_keras_layers_Activation_Mutation_List = [
    "activation='relu'", "activation='sigmoid'", "activation='tanh'",
    "activation='linear'", "activation='softmax'", "activation='softplus'",
    "activation='softsign'", "activation='selu'", "activation='elu'",
    "activation='exponential'", "activation='invalid_activation'", "activation=123",
    "activation=None", "activation=True", "activation=''"
]
tf_keras_layers_AlphaDropout_Mutation_List = [
    "rate=0.2, noise_shape=None, seed=None", "rate=0.3, noise_shape=[1, 2], seed=42",
    "rate=0.4, noise_shape=[2, 3], seed=100", "rate=0.5, noise_shape=None, seed=50",
    "rate=0.6, noise_shape=[3, 4], seed=None", "rate=0.1, noise_shape=None, seed=0",
    "rate=0.25, noise_shape=[1, 1], seed=123", "rate=0.35, noise_shape=[2, 2], seed=200",
    "rate=0.45, noise_shape=[3, 3], seed=300", "rate=0.55, noise_shape=[4, 4], seed=400",
    "rate=-0.2, noise_shape='invalid', seed='invalid'", "rate=1.2, noise_shape=100, seed=None",
    "rate=0, noise_shape=None, seed=-42", "rate='invalid', noise_shape=[-1, -2], seed='none'",
    "rate=None, noise_shape='invalid', seed='invalid'"
]
tf_keras_layers_Attention_Mutation_List = [
    # Typical parameter combinations
    "use_scale=True, causal=True, dropout=0.5", "use_scale=False, causal=False, dropout=0.3",
    "use_scale=True, dropout=0.1", "use_scale=False, dropout=0.6",
    "use_scale=True, causal=True, dropout=0", "use_scale=False, causal=True, dropout=0.2",
    "use_scale=True, dropout=0.4", "use_scale=False, dropout=0.1",
    "use_scale=True, causal=False, dropout=0.3", "use_scale=False, causal=False, dropout=0.5",
    # Scenarios with erroneous or inappropriate values
    "use_scale='invalid', causal=123, dropout=None", "use_scale=None, dropout='invalid'",
    "causal='true', dropout=1.5", "use_scale=0, dropout=0", "causal=None, dropout=-0.1"
]
# Belirtilen havuzlama katmanları için Python listesi formatında parametre kombinasyonları oluşturma

tf_keras_layers_AveragePooling1D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=2", "pool_size=3", "pool_size=4",
    "pool_size=5", "pool_size=6", "pool_size=7",
    "pool_size=8", "pool_size=9", "pool_size=10",
    "pool_size=11",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=0", "pool_size=-1",
    "pool_size=1.5", "pool_size=None"
]

tf_keras_layers_AveragePooling2D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=(2, 2)", "pool_size=(3, 3)", "pool_size=(4, 4)",
    "pool_size=(5, 5)", "pool_size=(6, 6)", "pool_size=(7, 7)",
    "pool_size=(8, 8)", "pool_size=(9, 9)", "pool_size=(10, 10)",
    "pool_size=(11, 11)",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=(0, 0)", "pool_size=(-1, -1)",
    "pool_size=(1.5, 1.5)", "pool_size=None"
]

tf_keras_layers_AveragePooling3D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=(2, 2, 2)", "pool_size=(3, 3, 3)", "pool_size=(4, 4, 4)",
    "pool_size=(5, 5, 5)", "pool_size=(6, 6, 6)", "pool_size=(7, 7, 7)",
    "pool_size=(8, 8, 8)", "pool_size=(9, 9, 9)", "pool_size=(10, 10, 10)",
    "pool_size=(11, 11, 11)",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=(0, 0, 0)", "pool_size=(-1, -1, -1)",
    "pool_size=(1.5, 1.5, 1.5)", "pool_size=None"
]

tf_keras_layers_AvgPool1D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=2", "pool_size=3", "pool_size=4",
    "pool_size=5", "pool_size=6", "pool_size=7",
    "pool_size=8", "pool_size=9", "pool_size=10",
    "pool_size=11",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=0", "pool_size=-1",
    "pool_size=1.5", "pool_size=None"
]

tf_keras_layers_AvgPool2D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=(2, 2)", "pool_size=(3, 3)", "pool_size=(4, 4)",
    "pool_size=(5, 5)", "pool_size=(6, 6)", "pool_size=(7, 7)",
    "pool_size=(8, 8)", "pool_size=(9, 9)", "pool_size=(10, 10)",
    "pool_size=(11, 11)",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=(0, 0)", "pool_size=(-1, -1)",
    "pool_size=(1.5, 1.5)", "pool_size=None"
]

tf_keras_layers_AvgPool3D_Mutation_List = [
    # Typical parameter combinations
    "pool_size=(2, 2, 2)", "pool_size=(3, 3, 3)", "pool_size=(4, 4, 4)",
    "pool_size=(5, 5, 5)", "pool_size=(6, 6, 6)", "pool_size=(7, 7, 7)",
    "pool_size=(8, 8, 8)", "pool_size=(9, 9, 9)", "pool_size=(10, 10, 10)",
    "pool_size=(11, 11, 11)",
    # Scenarios with erroneous or inappropriate values
    "pool_size='invalid'", "pool_size=(0, 0, 0)", "pool_size=(-1, -1, -1)",
    "pool_size=(1.5, 1.5, 1.5)","pool_size=None"
]  

tf_keras_layers_BatchNormalization_Mutation_List = [
    # Typical parameter combinations
    "momentum=0.99, epsilon=0.001", "momentum=0.9, epsilon=0.01", 
    "momentum=0.95, epsilon=0.005", "momentum=0.9, epsilon=0.1", 
    "momentum=0.8, epsilon=0.001", "momentum=0.85, epsilon=0.005", 
    "momentum=0.95, epsilon=0.003", "momentum=0.99, epsilon=0.0001", 
    "momentum=0.9, epsilon=0.0005", "momentum=0.8, epsilon=0.01",
    # Scenarios with erroneous or inappropriate values
    "momentum='invalid', epsilon='invalid'", "momentum=-0.1, epsilon=-0.001", 
    "momentum=1.1, epsilon=0.001", "momentum=None, epsilon=None", 
    "momentum=0.9, epsilon='invalid'"
]


tf_keras_layers_Bidirectional_Mutation_List = [
    # Bidirectional layer typically wraps another layer, here we use a generic "layer" placeholder
    # Typical parameter combinations
    "layer=SimpleRNN(10)", "layer=LSTM(20)", "layer=GRU(30)", 
    "layer=SimpleRNN(15)", "layer=LSTM(25)", "layer=GRU(35)", 
    "layer=SimpleRNN(20)", "layer=LSTM(30)", "layer=GRU(40)", 
    "layer=SimpleRNN(25)", "layer=LSTM(35)",
    # Scenarios with erroneous or inappropriate values
    "layer='invalid'", "layer=None", "layer=123", 
    "layer=SimpleRNN(-10)", "layer=LSTM('invalid')"
]


tf_keras_layers_CategoryEncoding_Mutation_List = [
    # Typical parameter combinations
    "num_tokens=10, output_mode='one_hot'", "num_tokens=20, output_mode='count'", 
    "num_tokens=30, output_mode='binary'", "num_tokens=40, output_mode='one_hot'", 
    "num_tokens=50, output_mode='count'", "num_tokens=15, output_mode='binary'", 
    "num_tokens=25, output_mode='one_hot'", "num_tokens=35, output_mode='count'", 
    "num_tokens=45, output_mode='binary'", "num_tokens=55, output_mode='one_hot'",
    # Scenarios with erroneous or inappropriate values
    "num_tokens=-10, output_mode='invalid'", "num_tokens='invalid', output_mode='one_hot'", 
    "num_tokens=20, output_mode=None", "num_tokens=None, output_mode='count'", 
    "num_tokens=0, output_mode='binary'"
]

tf_keras_layers_CenterCrop_Mutation_List = [
    # Typical parameter combinations
    "height=20, width=20", "height=30, width=30", "height=40, width=40", 
    "height=50, width=50", "height=60, width=60", "height=70, width=70", 
    "height=80, width=80", "height=90, width=90", "height=100, width=100", 
    "height=110, width=110",
    # Scenarios with erroneous or inappropriate values
    "height=-20, width=-20", "height='invalid', width='invalid'", 
    "height=20, width=None", "height=None, width=30", 
    "height=0, width=0"
]


tf_keras_layers_Concatenate_Mutation_List = [
    # Typical parameter combinations
    "axis=-1", "axis=0", "axis=1", "axis=2", "axis=3", 
    "axis=-2", "axis=-3", "axis=4", "axis=-4", "axis=5",
    # Scenarios with erroneous or inappropriate values
    "axis='invalid'", "axis=123", "axis=None", 
    "axis=-123", "axis=1.5"
]

tf_keras_layers_Conv1D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=3", "filters=64, kernel_size=5", 
    "filters=128, kernel_size=7", "filters=16, kernel_size=3", 
    "filters=32, kernel_size=1", "filters=48, kernel_size=2", 
    "filters=64, kernel_size=4", "filters=96, kernel_size=6", 
    "filters=128, kernel_size=8", "filters=32, kernel_size=5",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=-3", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=0", 
]
# Conv1DTranspose için tipik ve hatalı parametre kombinasyonları
tf_keras_layers_Conv1DTranspose_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=3", "filters=64, kernel_size=5", 
    "filters=128, kernel_size=7", "filters=16, kernel_size=3", 
    "filters=32, kernel_size=1", "filters=48, kernel_size=2", 
    "filters=64, kernel_size=4", "filters=96, kernel_size=6", 
    "filters=128, kernel_size=8", "filters=32, kernel_size=5",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=-3", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=0", 
    "filters=64, kernel_size='invalid'"
]

# Conv2D için tipik ve hatalı parametre kombinasyonları
tf_keras_layers_Conv2D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3)", "filters=64, kernel_size=(5, 5)", 
    "filters=128, kernel_size=(7, 7)", "filters=16, kernel_size=(3, 3)", 
    "filters=32, kernel_size=(1, 1)", "filters=48, kernel_size=(2, 2)", 
    "filters=64, kernel_size=(4, 4)", "filters=96, kernel_size=(6, 6)", 
    "filters=128, kernel_size=(8, 8)", "filters=32, kernel_size=(5, 5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3)", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=(0, 0)", 
    "filters=64, kernel_size='invalid'"
]


tf_keras_layers_Conv2DTranspose_Mutation_List = [
    # Typical parameter combinations
    # Similar to Conv2D but for transpose operation
    "filters=32, kernel_size=(3, 3)", "filters=64, kernel_size=(5, 5)", 
    "filters=128, kernel_size=(7, 7)", "filters=16, kernel_size=(3, 3)", 
    "filters=32, kernel_size=(1, 1)", "filters=48, kernel_size=(2, 2)", 
    "filters=64, kernel_size=(4, 4)", "filters=96, kernel_size=(6, 6)", 
    "filters=128, kernel_size=(8, 8)", "filters=32, kernel_size=(5, 5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3)", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=(0, 0)", 
    "filters=64, kernel_size='invalid'"
]
tf_keras_layers_Conv3D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3, 3)", "filters=64, kernel_size=(5, 5, 5)", 
    "filters=128, kernel_size=(7, 7, 7)", "filters=16, kernel_size=(3, 3, 3)", 
    "filters=32, kernel_size=(1, 1, 1)", "filters=48, kernel_size=(2, 2, 2)", 
    "filters=64, kernel_size=(4, 4, 4)", "filters=96, kernel_size=(6, 6, 6)", 
    "filters=128, kernel_size=(8, 8, 8)", "filters=32, kernel_size=(5, 5, 5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3, -3)", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=0", 
    "filters=64, kernel_size='invalid'"
]


tf_keras_layers_Conv3DTranspose_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3, 3)", "filters=64, kernel_size=(5, 5, 5)", 
    "filters=128, kernel_size=(7, 7, 7)", "filters=16, kernel_size=(3, 3, 3)", 
    "filters=32, kernel_size=(1, 1, 1)", "filters=48, kernel_size=(2, 2, 2)", 
    "filters=64, kernel_size=(4, 4, 4)", "filters=96, kernel_size=(6, 6, 6)", 
    "filters=128, kernel_size=(8, 8, 8)", "filters=32, kernel_size=(5, 5, 5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3, -3)", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=0", 
    "filters=64, kernel_size='invalid'"
]


tf_keras_layers_ConvLSTM1D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=3", "filters=64, kernel_size=5", 
    "filters=128, kernel_size=7", "filters=16, kernel_size=3", 
    "filters=32, kernel_size=1", "filters=48, kernel_size=2", 
    "filters=64, kernel_size=4", "filters=96, kernel_size=6", 
    "filters=128, kernel_size=8", "filters=32, kernel_size=5",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=-3", 
    "filters=None, kernel_size=None", "filters=0, kernel_size=0", 
    "filters=64, kernel_size='invalid'"
]


tf_keras_layers_ConvLSTM2D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3)", "filters=64, kernel_size=(5, 5)", 
    "filters=128, kernel_size=(7, 7)", "filters=16, kernel_size=(3, 3)", 
    "filters=32, kernel_size=(1, 1)", "filters=48, kernel_size=(2, 2)", 
    "filters=64, kernel_size=(4, 4)", "filters=96, kernel_size=(6, 6)", 
    "filters=128, kernel_size=(8, 8)", "filters=32, kernel_size=(5, 5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3)", 
    "filters=None"
]
tf_keras_layers_ConvLSTM3D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3,3)", "filters=64, kernel_size=(5, 5,5)", 
    "filters=128, kernel_size=(7, 7,7)", "filters=16, kernel_size=(3, 3,3)", 
    "filters=32, kernel_size=(1, 1,1)", "filters=48, kernel_size=(2, 2,2)", 
    "filters=64, kernel_size=(4, 4,4)", "filters=96, kernel_size=(6, 6,6)", 
    "filters=128, kernel_size=(8, 8,8)", "filters=32, kernel_size=(5, 5,5)",
    # Scenarios with erroneous or inappropriate values
    "filters='invalid', kernel_size='invalid'", "filters=-32, kernel_size=(-3, -3)", 
    "filters=None"
]
tf_keras_layers_Convolution1D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=3, strides=1, padding='valid', activation='relu'",
    "filters=64, kernel_size=5, strides=2, padding='same', activation='tanh'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=0, strides=-1, padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Convolution2D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'",
    "filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='sigmoid'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=(0, 0), strides=(-1, -1), padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Convolution3D_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3, 3), strides=(1, 1, 1), padding='valid', activation='relu'",
    "filters=64, kernel_size=(5, 5, 5), strides=(2, 2, 2), padding='same', activation='softmax'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=(0, 0, 0), strides=(-1, -1, -1), padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Convolution1DTranspose_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=3, strides=1, padding='valid', activation='relu'",
    "filters=64, kernel_size=5, strides=2, padding='same', activation='tanh'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=0, strides=-1, padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Convolution2DTranspose_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'",
    "filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='sigmoid'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=(0, 0), strides=(-1, -1), padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Convolution3DTranspose_Mutation_List = [
    # Typical parameter combinations
    "filters=32, kernel_size=(3, 3, 3), strides=(1, 1, 1), padding='valid', activation='relu'",
    "filters=64, kernel_size=(5, 5, 5), strides=(2, 2, 2), padding='same', activation='softmax'",
    # Scenarios with erroneous or inappropriate values
    "filters=-1, kernel_size=(0, 0, 0), strides=(-1, -1, -1), padding='invalid', activation=123",
    "filters='invalid', kernel_size='invalid', strides='invalid', padding=[], activation=None"
]

tf_keras_layers_Cropping1D_Mutation_List = [
    # Typical parameter combinations
    "cropping=(1, 1)", "cropping=(2, 2)", "cropping=(3, 3)",
    "cropping=(4, 4)", "cropping=(5, 5)", "cropping=(6, 6)",
    "cropping=(7, 7)", "cropping=(8, 8)", "cropping=(9, 9)",
    "cropping=(10, 10)",
    # Scenarios with erroneous or inappropriate values
    "cropping='invalid'", "cropping=(0, 0)", "cropping=(-1, -1)",
    "cropping=(1.5, 1.5)", "cropping=None"
]


tf_keras_layers_Cropping2D_Mutation_List = [
    # Typical parameter combinations
    "cropping=((1, 1), (1, 1))", "cropping=((2, 2), (2, 2))", 
    "cropping=((3, 3), (3, 3))", "cropping=((4, 4), (4, 4))", 
    "cropping=((5, 5), (5, 5))", "cropping=((6, 6), (6, 6))", 
    "cropping=((7, 7), (7, 7))", "cropping=((8, 8), (8, 8))", 
    "cropping=((9, 9), (9, 9))", "cropping=((10, 10), (10, 10))",
    # Scenarios with erroneous or inappropriate values
    "cropping='invalid'", "cropping=((0, 0), (0, 0))", 
    "cropping=((1.5, 1.5), (1.5, 1.5))", "cropping=None", 
    "cropping=((0, 0), (-1, -1))"
]


tf_keras_layers_Cropping3D_Mutation_List = [
    # Typical parameter combinations
    "cropping=((1, 1), (1, 1), (1, 1))", "cropping=((2, 2), (2, 2), (2, 2))", 
    "cropping=((3, 3), (3, 3), (3, 3))", "cropping=((4, 4), (4, 4), (4, 4))", 
    "cropping=((5, 5), (5, 5), (5, 5))", "cropping=((6, 6), (6, 6), (6, 6))", 
    "cropping=((7, 7), (7, 7), (7, 7))", "cropping=((8, 8), (8, 8), (8, 8))", 
    "cropping=((9, 9), (9, 9), (9, 9))", "cropping=((10, 10), (10, 10), (10, 10))",
    # Scenarios with erroneous or inappropriate values
    "cropping='invalid'", "cropping=((0, 0), (0, 0), (0, 0))", 
    "cropping=((1.5, 1.5), (1.5, 1.5), (1.5, 1.5))", "cropping=None", 
    "cropping=((0, 0), (-1, -1), (-1, -1))"
]


tf_keras_layers_SpectralNormalization_Mutation_List = [
    # SpectralNormalization does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as SpectralNormalization does not have parameters, these will be empty)
    "", "[x1, x2]","[x2, x1]"
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_layers_StackedRNNCells_Mutation_List = [
    # StackedRNNCells layer typically wraps other layers, here we use a generic "layer" placeholder
    # Typical parameter combinations
    "cells=[SimpleRNNCell(10), SimpleRNNCell(20)]", "cells=[LSTMCell(20), LSTMCell(30)]", 
    "cells=[GRUCell(30), GRUCell(40)]", "cells=[SimpleRNNCell(15), SimpleRNNCell(25)]", 
    "cells=[LSTMCell(25), LSTMCell(35)]", "cells=[GRUCell(35), GRUCell(45)]", 
    "cells=[SimpleRNNCell(20), SimpleRNNCell(30)]", "cells=[LSTMCell(30), LSTMCell(40)]", 
    "cells=[GRUCell(40), GRUCell(50)]", "cells=[SimpleRNNCell(25), SimpleRNNCell(35)]",
    # Scenarios with erroneous or inappropriate values
    "cells='invalid'", "cells=None", "cells=[123, 456]", 
    "cells=[SimpleRNNCell(-10), LSTMCell('invalid')]", "cells=[GRUCell('invalid'), SimpleRNNCell(0)]"
]

# StringLookup için tipik ve hatalı parametre kombinasyonları
tf_keras_layers_StringLookup_Mutation_List = [
    # Typical parameter combinations
    "num_tokens=1000, output_mode='int'", "num_tokens=2000, output_mode='multi_hot'", 
    "num_tokens=3000, output_mode='count'", "num_tokens=4000, output_mode='tf_idf'", 
    "num_tokens=5000, output_mode='int'", "num_tokens=1500, output_mode='multi_hot'", 
    "num_tokens=2500, output_mode='count'", "num_tokens=3500, output_mode='tf_idf'", 
    "num_tokens=4500, output_mode='int'", "num_tokens=5500, output_mode='multi_hot'",
    # Scenarios with erroneous or inappropriate values
    "num_tokens=-1000, output_mode='invalid'", "num_tokens='invalid', output_mode='int'", 
    "num_tokens=2000, output_mode=None", "num_tokens=None, output_mode='multi_hot'", 
    "num_tokens=0, output_mode='count'"
]

# Subtract için tipik ve hatalı parametre kombinasyonları
tf_keras_layers_Subtract_Mutation_List = [
    # Subtract layer does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as Subtract does not have parameters, these will be empty)
    "","[x1, x2]","[x2, x3]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

# TextVectorization için tipik ve hatalı parametre kombinasyonları
tf_keras_layers_TextVectorization_Mutation_List = [
    # Typical parameter combinations
    "max_tokens=10000, output_mode='int'", "max_tokens=20000, output_mode='binary'", 
    "max_tokens=30000, output_mode='count'", "max_tokens=40000, output_mode='tf_idf'", 
    "max_tokens=50000, output_mode='int'", "max_tokens=15000, output_mode='binary'", 
    "max_tokens=25000, output_mode='count'", "max_tokens=35000, output_mode='tf_idf'", 
    "max_tokens=45000, output_mode='int'", "max_tokens=55000, output_mode='binary'",
    # Scenarios with erroneous or inappropriate values
    "max_tokens=-10000, output_mode='invalid'", "max_tokens='invalid'"
] 
tf_keras_layers_ThresholdedReLU_Mutation_List = [
    # Typical parameter combinations
    "theta=1.0", "theta=0.5", "theta=1.5", 
    "theta=2.0", "theta=0.2", "theta=0.8", 
    "theta=1.2", "theta=1.8", "theta=0.3", 
    "theta=0.7",
    # Scenarios with erroneous or inappropriate values
    "theta=-1.0", "theta='invalid'", "theta=None", 
    "theta=-0.5", "theta=2.5"
]


tf_keras_layers_TimeDistributed_Mutation_List = [
    # TimeDistributed layer typically wraps another layer, here we use a generic "layer" placeholder
    # Typical parameter combinations
    "layer=Dense(10)", "layer=Dense(20)", "layer=Dense(30)", 
    "layer=Dense(40)", "layer=Dense(50)", "layer=Dense(60)", 
    "layer=Dense(70)", "layer=Dense(80)", "layer=Dense(90)", 
    "layer=Dense(100)",
    # Scenarios with erroneous or inappropriate values
    "layer='invalid'", "layer=None", "layer=Dense(-10)", 
    "layer=Dense('invalid')", "layer=123"
]


tf_keras_layers_UnitNormalization_Mutation_List = [
    # UnitNormalization does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as UnitNormalization does not have parameters, these will be empty)
    "","[x1, x2]", "[x2, x1]", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]


tf_keras_layers_UpSampling1D_Mutation_List = [
    # Typical parameter combinations
    "size=2", "size=3", "size=4", 
    "size=5", "size=6", "size=7", 
    "size=8", "size=9", "size=10", 
    "size=11",
    # Scenarios with erroneous or inappropriate values
    "size=-1", "size='invalid'", "size=None", 
    "size=0", "size=1.5"
]


tf_keras_layers_UpSampling2D_Mutation_List = [
    # Typical parameter combinations
    "size=(2, 2)", "size=(3, 3)", "size=(4, 4)", 
    "size=(5, 5)", "size=(6, 6)", "size=(7, 7)", 
    "size=(8, 8)", "size=(9, 9)", "size=(10, 10)", 
    "size=(11, 11)",
    # Scenarios with erroneous or inappropriate values
    "size=(-1, -1)", "size=('invalid', 'invalid')", "size=None", 
    "size=(0, 0)", "size=(1.5, 1.5)"
]


tf_keras_layers_UpSampling3D_Mutation_List = [
    # Typical parameter combinations
    "size=(2, 2, 2)", "size=(3, 3, 3)", "size=(4, 4, 4)", 
    "size=(5, 5, 5)", "size=(6, 6, 6)", "size=(7, 7, 7)", 
    "size=(8, 8, 8)", "size=(9, 9, 9)", "size=(10, 10, 10)", 
    "size=(11, 11, 11)",
    # Scenarios with erroneous or inappropriate values
    "size=(-1, -1, -1)", "size=('invalid', 'invalid', 'invalid')", "size=None", 
    "size=(0, 0, 0)", "size=(1.5, 1.5,1.5)",
]
tf_keras_layers_Wrapper_Mutation_List = [
    # Wrapper layer typically wraps another layer, here we use a generic "layer" placeholder
    # Typical parameter combinations (as Wrapper does not have specific parameters, these will be empty)
    "","[x1, x2]", "[x2, x1]", 
    # Scenarios with erroneous or inappropriate values
    "layer='invalid'", "layer=None", "layer=123", 
    "layer=SimpleRNN(-10)", "layer=LSTM('invalid')"
]


tf_keras_layers_ZeroPadding1D_Mutation_List = [
    # Typical parameter combinations
    "padding=1", "padding=2", "padding=3", 
    "padding=4", "padding=5", "padding=6", 
    "padding=7", "padding=8", "padding=9", 
    "padding=10",
    # Scenarios with erroneous or inappropriate values
    "padding=-1", "padding='invalid'", "padding=None", 
    "padding=0", "padding=1.5"
]

tf_keras_layers_ZeroPadding2D_Mutation_List = [
    # Typical parameter combinations
    "padding=(1, 1)", "padding=(2, 2)", "padding=(3, 3)", 
    "padding=(4, 4)", "padding=(5, 5)", "padding=(6, 6)", 
    "padding=(7, 7)", "padding=(8, 8)", "padding=(9, 9)", 
    "padding=(10, 10)",
    # Scenarios with erroneous or inappropriate values
    "padding=(-1, -1)", "padding=('invalid', 'invalid')", "padding=None", 
    "padding=(0, 0)", "padding=(1.5, 1.5)"
]


tf_keras_layers_ZeroPadding3D_Mutation_List = [
    # Typical parameter combinations
    "padding=((1, 1), (1, 1), (1, 1))", "padding=((2, 2), (2, 2), (2, 2))", 
    "padding=((3, 3), (3, 3), (3, 3))", "padding=((4, 4), (4, 4), (4, 4))", 
    "padding=((5, 5), (5, 5), (5, 5))", "padding=((6, 6), (6, 6), (6, 6))", 
    "padding=((7, 7), (7, 7), (7, 7))", "padding=((8, 8), (8, 8), (8, 8))", 
    "padding=((9, 9), (9, 9), (9, 9))", "padding=((10, 10), (10, 10), (10, 10))",
    # Scenarios with erroneous or inappropriate values
    "padding='invalid'", "padding=((0, 0), (0, 0), (0, 0))", 
    "padding=((1.5, 1.5), (1.5, 1.5), (1.5, 1.5))", "padding=None", 
    "padding=((0, 0), (-1, -1), (-1, -1))"
]


tf_keras_layers_add_Mutation_List = [
    # add layer does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as add does not have parameters, these will be empty)
    "","[x1, x2]", "[x2, x1]", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_layers_add_Mutation_List = [
    # add layer does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as add does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_average_Mutation_List = [
    # average layer does not have significant parameters
    # Typical parameter combinations (as average does not have parameters, these will be empty)
    "", "[x1, x2]","[x2, x1]", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_concatenate_Mutation_List = [
    # concatenate layer does not have significant parameters
    # Typical parameter combinations (as concatenate does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]"
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_dot_Mutation_List = [
    # dot layer does not have significant parameters
    # Typical parameter combinations (as dot does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]



tf_keras_layers_deserialize_Mutation_List = [
    # deserialize does not have parameters
    # Typical parameter combinations (as deserialize does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_serialize_Mutation_List = [
    # serialize does not have parameters
    # Typical parameter combinations (as serialize does not have parameters, these will be empty)
    "", "[x2, x1]", "[x1, x2]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# maximum, minimum, multiply işlemsel katmanları için tipik parametre kombinasyonları oluşturma
# Bu katmanlar parametre almadığı için, bu listeler boş veya hatalı parametre senaryoları içerecek

tf_keras_layers_maximum_Mutation_List = [
    # maximum does not have parameters
    # Typical parameter combinations (as maximum does not have parameters, these will be empty)
    "", "[x2, x1]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_minimum_Mutation_List = [
    # minimum does not have parameters
    # Typical parameter combinations (as minimum does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_multiply_Mutation_List = [
    # multiply does not have parameters
    # Typical parameter combinations (as multiply does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_serialize_Mutation_List = [
    # serialize does not have parameters
    # Typical parameter combinations (as serialize does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_layers_subtract_Mutation_List = [
    # subtract does not have parameters
    # Typical parameter combinations (as subtract does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# TensorFlow aktivasyon fonksiyonları için tipik ve hatalı parametre kombinasyonları oluşturma
# Aktivasyon fonksiyonları genellikle parametre almadığı için, bu listeler boş veya hatalı parametre senaryoları içerecek

tf_keras_activations_deserialize_Mutation_List = [
    # deserialize for activations does not have parameters
    # Typical parameter combinations (as deserialize does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_activations_elu_Mutation_List = [
    # elu activation function typically has alpha parameter
    # Typical parameter combinations
    "alpha=1.0", "alpha=0.5", "alpha=1.5", 
    "alpha=2.0", "alpha=0.2", "alpha=0.8", 
    "alpha=1.2", "alpha=1.8", "alpha=0.3", 
    "alpha=0.7",
    # Scenarios with erroneous or inappropriate values
    "alpha=-1.0", "alpha='invalid'", "alpha=None", 
    "alpha=-0.5", "alpha=2.5"
]

tf_keras_activations_exponential_Mutation_List = [
    # exponential activation function does not have parameters
    # Typical parameter combinations (as exponential does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_activations_gelu_Mutation_List = [
    # gelu activation function does not have parameters
    # Typical parameter combinations (as gelu does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_activations_get_Mutation_List = [
    # get for activations does not have parameters
    # Typical parameter combinations (as get does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]
tf_keras_activations_hard_sigmoid_Mutation_List = [
    # hard_sigmoid does not have parameters
    # Typical parameter combinations (as hard_sigmoid does not have parameters, these will be empty)
     "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_activations_linear_Mutation_List = [
    # linear does not have parameters
    # Typical parameter combinations (as linear does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]



tf_keras_losses_BinaryCrossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=True", "from_logits=False", 
    "label_smoothing=0.1", "label_smoothing=0.2", 
    "label_smoothing=0.3", "label_smoothing=0", 
    "label_smoothing=0.5", "label_smoothing=0.4", 
    "label_smoothing=0.6", "label_smoothing=0.7",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid'", "label_smoothing=-0.1", 
    "label_smoothing=1.1", "from_logits=None", 
    "label_smoothing=None"
]


tf_keras_activations_mish_Mutation_List = [
    # mish does not have parameters
    # Typical parameter combinations (as mish does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_relu_Mutation_List = [
    # relu does not have parameters
    # Typical parameter combinations (as relu does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_selu_Mutation_List = [
    # selu does not have parameters
    # Typical parameter combinations (as selu does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_serialize_Mutation_List = [
    # serialize does not have parameters
    # Typical parameter combinations (as serialize does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_sigmoid_Mutation_List = [
    # sigmoid does not have parameters
    # Typical parameter combinations (as sigmoid does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_softmax_Mutation_List = [
    # softmax does not have parameters
    # Typical parameter combinations (as softmax does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_softplus_Mutation_List = [
    # softplus does not have parameters
    # Typical parameter combinations (as softplus does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_softsign_Mutation_List = [
    # softsign does not have parameters
    # Typical parameter combinations (as softsign does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_swish_Mutation_List = [
    # swish does not have parameters
    # Typical parameter combinations (as swish does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_tanh_Mutation_List = [
    # tanh does not have parameters
    # Typical parameter combinations (as tanh does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]
tf_keras_activations_swish_Mutation_List = [
    # swish does not have parameters
    # Typical parameter combinations (as swish does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_activations_tanh_Mutation_List = [
    # tanh does not have parameters
    # Typical parameter combinations (as tanh does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]

tf_keras_layers_Dense_Mutation_List = [
    # Commonly used Dense layer configurations
    "Dense(units=32, activation='relu')", 
    "Dense(units=64, activation='sigmoid')", 
    "Dense(units=128, activation='softmax')", 
    "Dense(units=256, activation='tanh')", 
    "Dense(units=512, activation='elu')",
    "Dense(32)","Dense(64)","Dense(128)","Dense(256)",
    "Dense(512)","Dense(units=32, activation='sigmoid')",
    "Dense(units=32, activation='softmax')",

    # Scenarios with erroneous or inappropriate values
    "Dense(units=-1, activation='relu')", 
    "Dense(units='invalid', activation='sigmoid')", 
    "Dense(units=None, activation='softmax')"
]

tf_keras_losses_BinaryCrossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, label_smoothing=0", "from_logits=True, label_smoothing=0.1", 
    "from_logits=False, label_smoothing=0.2", "from_logits=True, label_smoothing=0.3", 
    "from_logits=False, label_smoothing=0.4", "from_logits=True, label_smoothing=0.5", 
    "from_logits=False, label_smoothing=0.6", "from_logits=True, label_smoothing=0.7", 
    "from_logits=False, label_smoothing=0.8", "from_logits=True, label_smoothing=0.9",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', label_smoothing=-0.1", "from_logits=None, label_smoothing=1.1", 
    "from_logits=True, label_smoothing='invalid'", "from_logits=False, label_smoothing=-0.2", 
    "from_logits=True, label_smoothing=None"
]

tf_keras_losses_BinaryFocalCrossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, gamma=2.0, alpha=0.25", "from_logits=True, gamma=2.0, alpha=0.5", 
    "from_logits=False, gamma=2.0, alpha=0.75", "from_logits=True, gamma=2.0, alpha=1.0", 
    "from_logits=False, gamma=1.0, alpha=0.25", "from_logits=True, gamma=1.0, alpha=0.5", 
    "from_logits=False, gamma=1.0, alpha=0.75", "from_logits=True, gamma=1.0, alpha=1.0", 
    "from_logits=False, gamma=3.0, alpha=0.25", "from_logits=True, gamma=3.0, alpha=0.5",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', gamma=-2.0, alpha=-0.25", "from_logits=None, gamma=4.0, alpha=1.25", 
    "from_logits=True, gamma='invalid', alpha='invalid'", "from_logits=False, gamma=-1.0, alpha=-0.5", 
    "from_logits=True, gamma=None, alpha=None"
]


tf_keras_losses_CategoricalCrossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, label_smoothing=0", "from_logits=True, label_smoothing=0.1", 
    "from_logits=False, label_smoothing=0.2", "from_logits=True, label_smoothing=0.3",
    "from_logits=False, label_smoothing=0.4", "from_logits=True, label_smoothing=0.5", 
    "from_logits=False, label_smoothing=0.6", "from_logits=True, label_smoothing=0.7",
    "from_logits=False, label_smoothing=0.8", "from_logits=True, label_smoothing=0.9",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', label_smoothing=-0.1", "from_logits=None, label_smoothing=1.1", 
    "from_logits=123, label_smoothing='invalid'", "from_logits=False, label_smoothing=-0.5", 
    "from_logits=True, label_smoothing=1.5"
]


tf_keras_losses_CategoricalFocalCrossentropy_Mutation_List = [
    # Typical parameter combinations (assuming generic gamma and alpha values as this is a custom loss)
    "gamma=2.0, alpha=0.25", "gamma=2.0, alpha=0.5", 
    "gamma=2.0, alpha=0.75", "gamma=1.5, alpha=0.25",
    "gamma=1.5, alpha=0.5", "gamma=1.5, alpha=0.75", 
    "gamma=3.0, alpha=0.25", "gamma=3.0, alpha=0.5",
    "gamma=3.0, alpha=0.75", "gamma=2.5, alpha=0.25",
    # Scenarios with erroneous or inappropriate values
    "gamma='invalid', alpha=-0.1", "gamma=None, alpha=1.1", 
    "gamma=-2.0, alpha='invalid'", "gamma=4.0, alpha=-0.5", 
    "gamma=0, alpha=1.5"
]

tf_keras_losses_CategoricalHinge_Mutation_List = [
    # CategoricalHinge does not have significant parameters
    # Typical parameter combinations (as CategoricalHinge does not have parameters, these will be empty)
    "", "[x1, x2]", "[x2, x1]",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", 
    "activation='relu'", "dropout=0.3"
]


tf_keras_losses_CosineSimilarity_Mutation_List = [
    # Typical parameter combinations
    "axis=-1", "axis=0", "axis=1", 
    "axis=2", "axis=-2", "axis=-3", 
    "axis=3", "axis=4", "axis=-4",
    "axis=5",
    # Scenarios with erroneous or inappropriate values
    "axis='invalid'", "axis=123", "axis=None", 
    "axis=-123", "axis=1.5"
]

# Belirtilen TensorFlow kayıp fonksiyonları için Python listesi formatında parametre kombinasyonları oluşturma

# Hinge için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_Hinge_Mutation_List = [
    # Hinge does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as Hinge does not have parameters, these will be empty)
    "", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]


tf_keras_losses_Huber_Mutation_List = [
    # Typical parameter combinations
    "delta=1.0", "delta=0.5", "delta=1.5", 
    "delta=2.0", "delta=0.2", "delta=0.8", 
    "delta=1.2", "delta=1.8", "delta=0.3", 
    "delta=0.7",
    # Scenarios with erroneous or inappropriate values
    "delta=-1.0", "delta='invalid'", "delta=None", 
    "delta=-0.5", "delta=2.5"
]


 
tf_keras_losses_KLD_Mutation_List = [
    # KLD does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as KLD does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]
tf_losses_KLDivergence_Mutation_List = [
    # Typical parameter combinations
    "y_true=[0.1, 0.9], y_pred=[0.2, 0.8]",
    "y_true=[0.3, 0.7], y_pred=[0.4, 0.6]",
    # Scenarios with erroneous or inappropriate values
    "y_true='invalid', y_pred='invalid'",
    "y_true=[], y_pred=[]"
]

tf_keras_losses_LogCosh_Mutation_List = [
    # LogCosh does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as LogCosh does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true" 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# Loss için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_Loss_Mutation_List = [
    # Loss is a base class for losses, and does not have specific parameters
    # Typical parameter combinations (as Loss does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# MAE, MAPE, MSE, MSLE, MeanAbsoluteError, MeanAbsolutePercentageError, MeanSquaredError, MeanSquaredLogarithmicError için tipik ve hatalı parametre kombinasyonları
# Bu kayıp fonksiyonları özgün parametreler içermediği için, bu listeler boş veya hatalı parametre senaryoları içerecek

tf_keras_losses_MAE_Mutation_List = [
    # MAE does not have significant parameters
    # Typical parameter combinations (as MAE does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_losses_MAPE_Mutation_List = [
    # MAPE does not have significant parameters
    # Typical parameter combinations (as MAPE does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# Belirtilen TensorFlow kayıp fonksiyonları için Python listesi formatında parametre kombinasyonları oluşturma

# MSLE (Mean Squared Logarithmic Error) için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_MSLE_Mutation_List = [
    # MSLE does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as MSLE does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# MeanAbsoluteError için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_MeanAbsoluteError_Mutation_List = [
    # MeanAbsoluteError does not have significant parameters
    # Typical parameter combinations (as MeanAbsoluteError does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# MeanAbsolutePercentageError için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_MeanAbsolutePercentageError_Mutation_List = [
    # MeanAbsolutePercentageError does not have significant parameters
    # Typical parameter combinations (as MeanAbsolutePercentageError does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# MeanSquaredError için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_MeanSquaredError_Mutation_List = [
    # MeanSquaredError does not have significant parameters
    # Typical parameter combinations (as MeanSquaredError does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# MeanSquaredLogarithmicError için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_MeanSquaredLogarithmicError_Mutation_List = [
    # MeanSquaredLogarithmicError does not have significant parameters
    # Typical parameter combinations (as MeanSquaredLogarithmicError does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# Poisson için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_Poisson_Mutation_List = [
    # Poisson does not have significant parameters
    # Typical parameter combinations (as Poisson does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "reduction='none'", "reduction='sum'", "reduction='invalid'"
]

# Reduction için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_Reduction_Mutation_List = [
    # Reduction does not have significant parameters
    # Typical parameter combinations (as Reduction does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "type='none'", "type='sum'", "type='invalid'"
]


# SparseCategoricalCrossentropy için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_SparseCategoricalCrossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, reduction='auto', name='sparse_categorical_crossentropy'",
    "from_logits=True, reduction='sum', name='sparse_categorical_crossentropy'",
    "from_logits=False, reduction='none', name='sparse_categorical_crossentropy'",
    "from_logits=True, reduction='sum_over_batch_size', name='sparse_categorical_crossentropy'",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', reduction='invalid', name='invalid'",
    "from_logits=123, reduction=None, name=None",
    "from_logits=None, reduction='auto', name='sparse_categorical_crossentropy'",
    "from_logits=False, reduction=123, name='sparse_categorical_crossentropy'",
    "from_logits=True, reduction='auto', name=123"
]

# SquaredHinge için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_SquaredHinge_Mutation_List = [
    # Typical parameter combinations
    "reduction='auto', name='squared_hinge'",
    "reduction='sum', name='squared_hinge'",
    "reduction='none', name='squared_hinge'",
    "reduction='sum_over_batch_size', name='squared_hinge'",
    # Scenarios with erroneous or inappropriate values
    "reduction='invalid', name='invalid'",
    "reduction=None, name=None",
    "reduction=123, name='squared_hinge'",
    "reduction='auto', name=123"
]

# binary_crossentropy için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_binary_crossentropy_Mutation_List = [
    # binary_crossentropy does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as binary_crossentropy does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# binary_focal_crossentropy için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_binary_focal_crossentropy_Mutation_List = [
    # Typical parameter combinations
    "gamma=2.0, alpha=0.25", "gamma=3.0, alpha=0.5", 
    "gamma=1.5, alpha=0.75", "gamma=2.5, alpha=0.25", 
    "gamma=2.0, alpha=0.5", "gamma=3.0, alpha=0.75", 
    "gamma=1.5, alpha=0.25", "gamma=2.5, alpha=0.5", 
    "gamma=2.0, alpha=0.75", "gamma=3.0, alpha=0.25",
    # Scenarios with erroneous or inappropriate values
    "gamma='invalid', alpha='invalid'", "gamma=-2.0, alpha=-0.25", 
    "gamma=None, alpha=None", "gamma=0, alpha=0", 
    "gamma=2.0, alpha='invalid'"
]

# categorical_crossentropy için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_categorical_crossentropy_Mutation_List = [
    # categorical_crossentropy does not have significant parameters, but we can create some scenarios
    # Typical parameter combinations (as categorical_crossentropy does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# Belirtilen TensorFlow loss fonksiyonları için Python listesi formatında parametre kombinasyonları oluşturma

# binary_focal_crossentropy için tipik ve hatalı parametre kombinasyonları
tf_keras_losses_binary_focal_crossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, gamma=2.0", "from_logits=True, gamma=2.5",
    "from_logits=False, gamma=1.5", "from_logits=True, gamma=3.0",
    "from_logits=False, gamma=2.2", "from_logits=True, gamma=2.7",
    "from_logits=False, gamma=1.8", "from_logits=True, gamma=3.2",
    "from_logits=False, gamma=2.4", "from_logits=True, gamma=2.9",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', gamma='invalid'", "from_logits=None, gamma=-2.0",
    "from_logits=False, gamma=-1.5", "from_logits=True, gamma='invalid'",
    "from_logits='invalid', gamma=None"
]


tf_keras_losses_categorical_crossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False", "from_logits=True",
    "from_logits=False", "from_logits=True",
    "from_logits=False", "from_logits=True",
    "from_logits=False", "from_logits=True",
    "from_logits=False", "from_logits=True",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid'", "from_logits=None",
    "from_logits=123", "from_logits=-1",
    "from_logits=1.5"
]


tf_keras_losses_categorical_focal_crossentropy_Mutation_List = [
    # Typical parameter combinations
    "from_logits=False, gamma=2.0", "from_logits=True, gamma=2.5",
    "from_logits=False, gamma=1.5", "from_logits=True, gamma=3.0",
    "from_logits=False, gamma=2.2", "from_logits=True, gamma=2.7",
    "from_logits=False, gamma=1.8", "from_logits=True, gamma=3.2",
    "from_logits=False, gamma=2.4", "from_logits=True, gamma=2.9",
    # Scenarios with erroneous or inappropriate values
    "from_logits='invalid', gamma='invalid'", "from_logits=None, gamma=-2.0",
    "from_logits=False, gamma=-1.5", "from_logits=True, gamma='invalid'",
    "from_logits='invalid', gamma=None"
]


tf_keras_losses_categorical_hinge_Mutation_List = [
    # Typical parameter combinations (as categorical_hinge does not have significant parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]


tf_keras_losses_cosine_similarity_Mutation_List = [
    # Typical parameter combinations
    "axis=-1", "axis=0", "axis=1", "axis=2", "axis=3",
    "axis=-2", "axis=-3", "axis=4", "axis=-4", "axis=5",
    # Scenarios with erroneous or inappropriate values
    "axis='invalid'", "axis=123", "axis=None",
    "axis=-123", "axis=1.5"
]


tf_keras_losses_deserialize_Mutation_List = [
    # deserialize does not have parameters
    # Typical parameter combinations (as deserialize does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]


tf_keras_losses_get_Mutation_List = [
    # Typical parameter combinations
    "name='categorical_crossentropy'", "name='sparse_categorical_crossentropy'",
    "name='binary_crossentropy'", "name='mean_squared_error'",
    "name='mean_absolute_error'", "name='mean_absolute_percentage_error'",
    "name='mean_squared_logarithmic_error'", "name='cosine_similarity'",
    "name='hinge'", "name='squared_hinge'",
    # Scenarios with erroneous or inappropriate values
    "name='invalid'", "name=123", "name=None",
    "name=True", "name=''"
]



tf_keras_losses_hinge_Mutation_List = [
    # hinge does not have significant parameters
    # Typical parameter combinations (as hinge does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_huber_Mutation_List = [
    # Typical parameter combinations
    "delta=1.0", "delta=0.5", "delta=1.5", 
    "delta=2.0", "delta=0.2", "delta=0.8", 
    "delta=1.2", "delta=1.8", "delta=0.3", 
    "delta=0.7",
    # Scenarios with erroneous or inappropriate values
    "delta=-1.0", "delta='invalid'", "delta=None", 
    "delta=-0.5", "delta=2.5"
]


tf_keras_losses_kl_divergence_Mutation_List = [
    # kl_divergence does not have significant parameters
    # Typical parameter combinations (as kl_divergence does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_kld_Mutation_List = [
    # kld does not have significant parameters
    # Typical parameter combinations (as kld does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_kullback_leibler_divergence_Mutation_List = [
    # kullback_leibler_divergence does not have significant parameters
    # Typical parameter combinations (as kullback_leibler_divergence does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_log_cosh_Mutation_List = [
    # log_cosh does not have significant parameters
    # Typical parameter combinations (as log_cosh does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_logcosh_Mutation_List = [
    # logcosh does not have significant parameters
    # Typical parameter combinations (as logcosh does not have parameters, these will be empty)
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"
]

tf_keras_losses_mae_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"] 
tf_keras_losses_mape_Mutation_List = [   
     "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  


tf_losses_mean_absolute_error_Mutation_List = [
    # Typical parameter combinations
    "y_true=[1, 2, 3], y_pred=[1, 2, 3]", 
    "y_true=[1, 2, 3], y_pred=[3, 2, 1]",
    # Scenarios with erroneous or inappropriate values
    "y_true='invalid', y_pred='invalid'", 
    "y_true=[], y_pred=[]"
]

tf_keras_losses_mean_absolute_percentage_error_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_mean_squared_error_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_mean_squared_logarithmic_error_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_mse_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_msle_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_poisson_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_serialize_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_sparse_categorical_crossentropy_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"]  
tf_keras_losses_squared_hinge_Mutation_List = [    
    "","y_true,y_pred","y_pred,y_true",
    # Scenarios with erroneous or inappropriate values
  "invalid_param='invalid'", "1, 2, 3", "use_bias=True",
    "activation='relu'", "dropout=0.3"] 

tf_keras_optimizers_Adadelta_Mutation_List = [
    "learning_rate=1.0, rho=0.95", "learning_rate=0.5, rho=0.9",
    "learning_rate=0.1, rho=0.85", "learning_rate=0.01, rho=0.8",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', rho=-1" 
]
tf_keras_optimizers_Adafactor_Mutation_List = [
    "learning_rate=1.0", "learning_rate=0.5", "learning_rate=0.1",
    "learning_rate=0.01", 
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid'"  
]
tf_keras_optimizers_Adagrad_Mutation_List = [
    "learning_rate=0.1, initial_accumulator_value=0.1",
    "learning_rate=0.01, initial_accumulator_value=0.01",
    "learning_rate=0.001, initial_accumulator_value=0.001",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', initial_accumulator_value=-1"  
]
tf_keras_optimizers_Adam_Mutation_List = [
    "learning_rate=0.001, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1"  
]
tf_keras_optimizers_Adamax_Mutation_List = [
    "learning_rate=0.002, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1"  
]

tf_keras_optimizers_Ftrl_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.01, learning_rate_power=-0.5",
    "learning_rate=0.1, learning_rate_power=-0.5",
    "learning_rate=1.0, learning_rate_power=-0.5",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', learning_rate_power='invalid'",
    "learning_rate=-0.01, learning_rate_power=0.5"
]

# Nadam optimizer's typical and erroneous parameter combinations
tf_keras_optimizers_Nadam_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.002, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999",
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1",
    "learning_rate=0, beta_1=1.1, beta_2=1.1"
]

# RMSprop optimizer's typical and erroneous parameter combinations
tf_keras_optimizers_RMSprop_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.001, rho=0.9, momentum=0.0",
    "learning_rate=0.01, rho=0.9, momentum=0.0",
    "learning_rate=0.1, rho=0.9, momentum=0.0",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', rho=-1, momentum=-1",
    "learning_rate=0, rho=1.1, momentum=1.1"
]

# 
#  optimizer's typical and erroneous parameter combinations
tf_keras_optimizers_SGD_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.01, momentum=0.0, nesterov=False",
    "learning_rate=0.1, momentum=0.5, nesterov=True",
    "learning_rate=1.0, momentum=0.9, nesterov=True",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', momentum=-1, nesterov='invalid'",
    "learning_rate=0, momentum=1.1, nesterov=False"
]
tf_keras_optimizers_schedules_CosineDecay_Mutation_List = [
    # Typical parameter combinations
    "initial_learning_rate=0.1, decay_steps=1000, alpha=0.0", 
    "initial_learning_rate=0.01, decay_steps=100, alpha=0.5",
    # Scenarios with erroneous or inappropriate values
    "initial_learning_rate='invalid', decay_steps=-100, alpha=-0.5", 
    "initial_learning_rate=0, decay_steps=0, alpha=1.1"
]

tf_keras_optimizers_schedules_ExponentialDecay_Mutation_List = [
    # Typical parameter combinations
    "initial_learning_rate=0.1, decay_steps=1000, decay_rate=0.9, staircase=False", 
    "initial_learning_rate=0.01, decay_steps=100, decay_rate=0.95, staircase=True",
    # Scenarios with erroneous or inappropriate values
    "initial_learning_rate='invalid', decay_steps=-100, decay_rate=-0.5, staircase='invalid'", 
    "initial_learning_rate=0, decay_steps=0, decay_rate=1.1, staircase=False"
]

tf_keras_optimizers_schedules_PolynomialDecay_Mutation_List = [
    # Typical parameter combinations
    "initial_learning_rate=0.1, decay_steps=1000, end_learning_rate=0.01, power=1.0, cycle=False", 
    "initial_learning_rate=0.01, decay_steps=100, end_learning_rate=0.001, power=0.5, cycle=True",
    # Scenarios with erroneous or inappropriate values
    "initial_learning_rate='invalid', decay_steps=-100, end_learning_rate=-0.01, power='invalid', cycle='invalid'", 
    "initial_learning_rate=0, decay_steps=0, end_learning_rate=1.1, power=0, cycle=False"
]
# Optimizer deserialize function's typical and erroneous parameter combinations
tf_optimizers_deserialize_Mutation_List = [
    # deserialize does not have parameters
    #No Typical parameter combinations (as deserialize does not have parameters, these will be empty)
    "", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_optimizers_get_Mutation_List = [
    # Typical parameter combinations with different optimizer names
    "optimizer_name='SGD'",
    "optimizer_name='sgd'",
    "optimizer_name='RMSprop'",
    "optimizer_name='Adam'",
    "optimizer_name='Adadelta'",
    "optimizer_name='Adagrad'",
    "optimizer_name='Adamax'",
    "optimizer_name='Nadam'",
    "optimizer_name='Ftrl'",
    # Scenarios with erroneous or inappropriate values
    "optimizer_name='invalid'",  # Non-existent optimizer name
    "optimizer_name=None"        # None as an optimizer name
]
tf_keras_optimizers_legacy_Adadelta_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=1.0, rho=0.95", "learning_rate=0.5, rho=0.9", "learning_rate=0.1, rho=0.85",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', rho=-1", "learning_rate=-0.01, rho=1.1"
]

tf_keras_optimizers_legacy_Adagrad_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.1, initial_accumulator_value=0.1", 
    "learning_rate=0.01, initial_accumulator_value=0.01", 
    "learning_rate=0.001, initial_accumulator_value=0.001",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', initial_accumulator_value=-1", 
    "learning_rate=0, initial_accumulator_value=1.1"
]

tf_keras_optimizers_legacy_Adam_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.001, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1", 
    "learning_rate=0, beta_1=1.1, beta_2=1.1"
]

tf_keras_optimizers_legacy_Adamax_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.002, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1", 
    "learning_rate=0, beta_1=1.1, beta_2=1.1"
]

tf_keras_optimizers_legacy_Ftrl_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.01, learning_rate_power=-0.5",
      "learning_rate=0.1, learning_rate_power=-0.5", 
      "learning_rate=1.0, learning_rate_power=-0.5",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', learning_rate_power='invalid'", 
    "learning_rate=-0.01, learning_rate_power=0.5"
]

tf_keras_optimizers_legacy_Nadam_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.002, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.01, beta_1=0.9, beta_2=0.999", 
    "learning_rate=0.1, beta_1=0.9, beta_2=0.999",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', beta_1=-1, beta_2=-1", 
    "learning_rate=0, beta_1=1.1, beta_2=1.1"
]

tf_keras_optimizers_legacy_RMSprop_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.001, rho=0.9, momentum=0.0", 
    "learning_rate=0.01, rho=0.9, momentum=0.0", 
    "learning_rate=0.1, rho=0.9, momentum=0.0",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', rho=-1, momentum=-1", 
    "learning_rate=0, rho=1.1, momentum=1.1"
]
tf_keras_optimizers_legacy_SGD_Mutation_List = [
    # Typical parameter combinations
    "learning_rate=0.01, momentum=0.0, nesterov=False", 
    "learning_rate=0.1, momentum=0.5, nesterov=True", 
    "learning_rate=1.0, momentum=0.9, nesterov=True",
    # Scenarios with erroneous or inappropriate values
    "learning_rate='invalid', momentum=-1, nesterov='invalid'", 
    "learning_rate=0, momentum=1.1, nesterov=False"
]

# tf.keras.optimizers.schedules functions
tf_keras_optimizers_schedules_Deserialize_Mutation_List = [
    # deserialize function typically does not have parameters
    # Typical parameter combinations (empty as deserialize does not have parameters)
    "", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_keras_optimizers_schedules_Serialize_Mutation_List = [
    # serialize function typically does not have parameters
    # Typical parameter combinations (empty as serialize does not have parameters)
    "", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

# tf.nn functions
tf_nn_RNNCellDeviceWrapper_Mutation_List = [
    # Typical parameter combinations
    "cell=LSTMCell(10)", "cell=GRUCell(20)",
    # Scenarios with erroneous or inappropriate values
    "cell='invalid'", "cell=None"
]

tf_nn_RNNCellDropoutWrapper_Mutation_List = [
    # Typical parameter combinations
    "cell=LSTMCell(10), dropout=0.2", "cell=GRUCell(20), dropout=0.3",
    # Scenarios with erroneous or inappropriate values
    "cell='invalid', dropout=-0.1", "cell=None, dropout=1.1"
]

tf_nn_RNNCellResidualWrapper_Mutation_List = [
    # Typical parameter combinations
    "cell=LSTMCell(10)", "cell=GRUCell(20)",
    # Scenarios with erroneous or inappropriate values
    "cell='invalid'", "cell=None"
]
tf_nn_all_candidate_sampler_Mutation_List = [
    # Typical parameter combinations (as a placeholder since this function might not have significant customizable parameters)
    "num_true=1, num_sampled=10, unique=True", 
    "num_true=2, num_sampled=20, unique=False",
    # Scenarios with erroneous or inappropriate values
    "num_true=-1, num_sampled=-10, unique='invalid'", 
    "num_true='invalid', num_sampled='invalid', unique=None"
]

tf_nn_approx_max_k_Mutation_List = [
    # Typical parameter combinations
    "values=[0.1, 0.2, 0.3], k=2", 
    "values=[0.5, 0.6, 0.7], k=3",
    # Scenarios with erroneous or inappropriate values
    "values='invalid', k=-1", 
    "values=[], k=0"
]

tf_nn_approx_min_k_Mutation_List = [
    # Typical parameter combinations
    "values=[0.1, 0.2, 0.3], k=2", 
    "values=[0.5, 0.6, 0.7], k=3",
    # Scenarios with erroneous or inappropriate values
    "values='invalid', k=-1", 
    "values=[], k=0"
]

tf_nn_atrous_conv2d_Mutation_List = [
    # Typical parameter combinations
    "value=[[1, 2], [3, 4]], filters=[[1, 0], [0, 1]], rate=2, padding='SAME'", 
    "value=[[1, 2, 3], [4, 5, 6]], filters=[[1, 0], [0, 1]], rate=3, padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', filters='invalid', rate=-1, padding='invalid'", 
    "value=[[1]], filters=[[1]], rate=0, padding='SAME'"
]

tf_nn_atrous_conv2d_transpose_Mutation_List = [
    # Typical parameter combinations
    "value=[[1, 2], [3, 4]], filters=[[1, 0], [0, 1]], rate=2, padding='SAME'", 
    "value=[[1, 2, 3], [4, 5, 6]], filters=[[1, 0], [0, 1]], rate=3, padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', filters='invalid', rate=-1, padding='invalid'", 
    "value=[[1]], filters=[[1]], rate=0, padding='SAME'"
]
tf_nn_avg_pool_Mutation_List = [
    # Typical parameter combinations
    "ksize=2, strides=2, padding='SAME'", 
    "ksize=3, strides=2, padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "ksize=-1, strides=-1, padding='invalid'", 
    "ksize=0, strides=0, padding='SAME'"
]


tf_nn_avg_pool1d_Mutation_List = [
    # Typical parameter combinations
    "ksize=2, strides=2, padding='SAME'", 
    "ksize=3, strides=2, padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "ksize=-1, strides=-1, padding='invalid'", 
    "ksize=0, strides=0, padding='SAME'"
]

tf_nn_avg_pool2d_Mutation_List = [
    # Typical parameter combinations
    "ksize=[2, 2], strides=[2, 2], padding='SAME'", 
    "ksize=[3, 3], strides=[2, 2], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "ksize='invalid', strides=-1, padding='invalid'", 
    "ksize=[0, 0], strides=[0, 0], padding='SAME'"
]
tf_nn_avg_pool3d_Mutation_List = [
    # Typical parameter combinations
    "ksize=[2, 2, 2], strides=[2, 2, 2], padding='SAME'", 
    "ksize=[3, 3, 3], strides=[2, 2, 2], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "ksize='invalid', strides=-1, padding='invalid'", 
    "ksize=[0, 0, 0], strides=[0, 0,0], padding='SAME'"
]   
 
tf_nn_avg_pool_Mutation_List = [
    # Typical parameter combinations
    "ksize=[2, 2], strides=[2, 2], padding='SAME'", 
    "ksize=[3, 3], strides=[2, 2], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "ksize='invalid', strides=-1, padding='invalid'", 
    "ksize=[0, 0], strides=[0, 0], padding='SAME'"
]

tf_nn_batch_norm_with_global_normalization_Mutation_List = [
    # Typical parameter combinations
    "t=[1, 2], m=[3, 4], v=[5, 6], beta=[7, 8], gamma=[9, 10], variance_epsilon=0.001, scale_after_normalization=True",
    "t=[2, 3], m=[4, 5], v=[6, 7], beta=[8, 9], gamma=[10, 11], variance_epsilon=0.01, scale_after_normalization=False",
    # Scenarios with erroneous or inappropriate values
    "t='invalid', m='invalid', v='invalid', beta='invalid', gamma='invalid', variance_epsilon=-0.001, scale_after_normalization='invalid'",
    "t=[], m=[], v=[], beta=[], gamma=[], variance_epsilon=0, scale_after_normalization=None"
]

tf_nn_batch_normalization_Mutation_List = [
    # Typical parameter combinations
    "x=[1, 2, 3], mean=[1], variance=[2], offset=[3], scale=[4], variance_epsilon=0.001",
    "x=[2, 3, 4], mean=[2], variance=[3], offset=[4], scale=[5], variance_epsilon=0.01",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', mean='invalid', variance='invalid', offset='invalid', scale='invalid', variance_epsilon=-0.001",
    "x=[], mean=[], variance=[], offset=[], scale=[], variance_epsilon=0"
]

tf_nn_bias_add_Mutation_List = [
    # Typical parameter combinations
    "value=[1, 2, 3], bias=[4, 5, 6], data_format='NHWC'",
    "value=[4, 5, 6], bias=[7, 8, 9], data_format='NCHW'",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', bias='invalid', data_format='invalid'",
    "value=[], bias=[], data_format=None"
]

tf_nn_collapse_repeated_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 2, 3], seq_lengths=[4], truth=True",
    "input=[1, 1, 2], seq_lengths=[3], truth=False",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', seq_lengths='invalid', truth='invalid'",
    "input=[], seq_lengths=[], truth=None"
]

tf_nn_compute_accidental_hits_Mutation_List = [
    # Typical parameter combinations
    "true_classes=[1, 2, 3], sampled_candidates=[4, 5, 6], num_true=1, seed=12345",
    "true_classes=[2, 3, 4], sampled_candidates=[5, 6, 7], num_true=2, seed=67890",
    # Scenarios with erroneous or inappropriate values
    "true_classes='invalid', sampled_candidates='invalid', num_true=-1, seed='invalid'",
    "true_classes=[], sampled_candidates=[], num_true=0, seed=None"
]

tf_nn_compute_average_loss_Mutation_List = [
    # Typical parameter combinations
    "per_example_loss=[0.1, 0.2, 0.3], global_batch_size=10",
    "per_example_loss=[0.4, 0.5, 0.6], global_batch_size=20",
    # Scenarios with erroneous or inappropriate values
    "per_example_loss='invalid', global_batch_size=-1",
    "per_example_loss=[], global_batch_size=0"
]
tf_nn_conv1d_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 3], filters=[4, 5, 6], stride=1, padding='VALID'", 
    "input=[3, 4, 5], filters=[6, 7, 8], stride=2, padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filters='invalid', stride=-1, padding='invalid'", 
    "input=[], filters=[], stride=0, padding='SAME'"
]

tf_nn_conv1d_transpose_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 3], filters=[4, 5, 6], stride=1, padding='VALID'", 
    "input=[3, 4, 5], filters=[6, 7, 8], stride=2, padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filters='invalid', stride=-1, padding='invalid'", 
    "input=[], filters=[], stride=0, padding='SAME'"
]

tf_nn_conv2d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1], padding='invalid'", 
    "input=[], filter=[], strides=[0, 0], padding='SAME'"
]

tf_nn_conv2d_transpose_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1], padding='invalid'", 
    "input=[], filter=[], strides=[0, 0], padding='SAME'"
]

tf_nn_conv3d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1, -1], padding='invalid'", 
    "input=[], filter=[], strides=[0, 0, 0], padding='SAME'"
]

tf_nn_conv3d_transpose_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1, -1], padding='invalid'", 
    "input=[], filter=[], strides=[0, 0, 0], padding='SAME'"
]
tf_nn_conv_transpose_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filters=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filters=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filters='invalid', strides=[-1, -1], padding='invalid'", 
    "input=[], filters=[], strides=[0, 0], padding='SAME'"
]

tf_nn_convolution_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filters=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID', dilation_rate=[1, 1]", 
    "input=[[2, 3], [4, 5]], filters=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME', dilation_rate=[2, 2]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filters='invalid', strides=[-1, -1], padding='invalid', dilation_rate='invalid'", 
    "input=[], filters=[], strides=[0, 0], padding='SAME', dilation_rate=[]"
]

tf_nn_crelu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, -0.2, 0.3], axis=-1", 
    "features=[-0.1, 0.2, -0.3], axis=0",
    # Scenarios with erroneous or inappropriate values
    "features='invalid', axis='invalid'", 
    "features=[], axis=-2"
]

tf_nn_ctc_beam_search_decoder_Mutation_List = [
    # Typical parameter combinations
    "inputs=[[0.6, 0.4], [0.8, 0.2]], sequence_length=[2], beam_width=10", 
    "inputs=[[0.7, 0.3], [0.9, 0.1]], sequence_length=[2], beam_width=20",
    # Scenarios with erroneous or inappropriate values
    "inputs='invalid', sequence_length='invalid', beam_width=-1", 
    "inputs=[], sequence_length=[], beam_width=0"
]

tf_nn_ctc_greedy_decoder_Mutation_List = [
    # Typical parameter combinations
    "inputs=[[0.6, 0.4], [0.8, 0.2]], sequence_length=[2]", 
    "inputs=[[0.7, 0.3], [0.9, 0.1]], sequence_length=[2]",
    # Scenarios with erroneous or inappropriate values
    "inputs='invalid', sequence_length='invalid'", 
    "inputs=[], sequence_length=[]"
]

tf_nn_ctc_loss_Mutation_List = [
    # Typical parameter combinations
    "labels=[[1, 2]], logits=[[0.1, 0.9]], label_length=[2], logit_length=[2]", 
    "labels=[[2, 1]], logits=[[0.2, 0.8]], label_length=[2], logit_length=[2]",
    # Scenarios with erroneous or inappropriate values
    "labels='invalid', logits='invalid', label_length='invalid', logit_length='invalid'", 
    "labels=[], logits=[], label_length=[], logit_length=[]"
]

tf_nn_ctc_unique_labels_Mutation_List = [
    # Typical parameter combinations
    "labels=[1, 2, 3, 4]", 
    "labels=[2, 3, 4, 5]",
    # Scenarios with erroneous or inappropriate values
    "labels='invalid'", 
    "labels=[]"
]
tf_nn_depth_to_space_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], block_size=2", 
    "input=[[2, 3], [4, 5]], block_size=3",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', block_size=-1", 
    "input=[], block_size=0"
]

tf_nn_depthwise_conv2d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1], padding='invalid'", 
    "input=[], filter=[], strides=[0, 0], padding='SAME'"
]

tf_nn_depthwise_conv2d_backprop_filter_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter_sizes=[2, 2], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter_sizes=[3, 3], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter_sizes='invalid', out_backprop='invalid', strides=[-1, -1], padding='invalid'", 
    "input=[], filter_sizes=[], out_backprop=[], strides=[0, 0], padding='SAME'"
]

tf_nn_depthwise_conv2d_backprop_input_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[2, 2], filter=[[1, 0], [0, 1]], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input_sizes=[3, 3], filter=[[1, 1], [1, 1]], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides=[-1, -1], padding='invalid'", 
    "input_sizes=[], filter=[], out_backprop=[], strides=[0, 0], padding='SAME'"
]

tf_nn_dilation2d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], rates=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2], rates=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1], rates='invalid', padding='invalid'", 
    "input=[], filter=[], strides=[0, 0], rates=[], padding='SAME'"
]

tf_nn_dropout_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], keep_prob=0.5", 
    "x=[0.4, 0.5, 0.6], keep_prob=0.8",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', keep_prob=-0.1", 
    "x=[], keep_prob=1.1"
]
tf_nn_elu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, -0.2, 0.3]", 
    "features=[-0.1, 0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'", 
    "features=[]"
]

tf_nn_embedding_lookup_Mutation_List = [
    # Typical parameter combinations
    "params=[[0.1, 0.2], [0.3, 0.4]], ids=[1, 2]", 
    "params=[[0.5, 0.6], [0.7, 0.8]], ids=[3, 4]",
    # Scenarios with erroneous or inappropriate values
    "params='invalid', ids='invalid'", 
    "params=[], ids=[]"
]

tf_nn_embedding_lookup_sparse_Mutation_List = [
    # Typical parameter combinations
    "params=[[0.1, 0.2], [0.3, 0.4]], sp_ids=[[1, 2], [3, 4]], sp_weights=[[0.5, 0.5], [0.5, 0.5]]", 
    "params=[[0.5, 0.6], [0.7, 0.8]], sp_ids=[[5, 6], [7, 8]], sp_weights=[[0.6, 0.4], [0.4, 0.6]]",
    # Scenarios with erroneous or inappropriate values
    "params='invalid', sp_ids='invalid', sp_weights='invalid'", 
    "params=[], sp_ids=[], sp_weights=[]"
]

tf_nn_erosion2d_Mutation_List = [
    # Typical parameter combinations
    "value=[[1, 2], [3, 4]], kernel=[[1, 0], [0, 1]], strides=[1, 1], rates=[1, 1], padding='VALID'", 
    "value=[[2, 3], [4, 5]], kernel=[[1, 1], [1, 1]], strides=[2, 2], rates=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', kernel='invalid', strides=[-1, -1], rates='invalid', padding='invalid'", 
    "value=[], kernel=[], strides=[0, 0], rates=[], padding='SAME'"
]

tf_nn_fixed_unigram_candidate_sampler_Mutation_List = [
    # Typical parameter combinations
    "true_classes=[1, 2, 3], num_true=2, num_sampled=5, unique=True", 
    "true_classes=[4, 5, 6], num_true=3, num_sampled=10, unique=False",
    # Scenarios with erroneous or inappropriate values
    "true_classes='invalid', num_true=-1, num_sampled=-5, unique='invalid'", 
    "true_classes=[], num_true=0, num_sampled=0, unique=None"
]

tf_nn_fractional_avg_pool_Mutation_List = [
    # Typical parameter combinations
    "value=[[1, 2], [3, 4]], pooling_ratio=[1.0, 1.4, 1.4]", 
    "value=[[2, 3], [4, 5]], pooling_ratio=[1.0, 1.5, 1.5]",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', pooling_ratio='invalid'", 
    "value=[], pooling_ratio=[]"
]

tf_nn_fractional_max_pool_Mutation_List = [
    # Typical parameter combinations
    "value=[[1, 2], [3, 4]], pooling_ratio=[1.0, 1.4, 1.4]", 
    "value=[[2, 3], [4, 5]], pooling_ratio=[1.0, 1.5, 1.5]",
    # Scenarios with erroneous or inappropriate values
    "value='invalid', pooling_ratio='invalid'", 
    "value=[], pooling_ratio=[]"
]

tf_nn_gelu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]", 
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'", 
    "features=[]"
]

tf_nn_in_top_k_Mutation_List = [
    # Typical parameter combinations
    "predictions=[[0.1, 0.9], [0.2, 0.8]], targets=[0, 1], k=1", 
    "predictions=[[0.3, 0.7], [0.6, 0.4]], targets=[1, 0], k=2",
    # Scenarios with erroneous or inappropriate values
    "predictions='invalid', targets='invalid', k=-1", 
    "predictions=[], targets=[], k=0"
]

tf_nn_isotonic_regression_Mutation_List = [
    # Typical parameter combinations
    "y=[0.1, 0.2, 0.3], weights=[1, 1, 1], increasing=True", 
    "y=[0.3, 0.2, 0.1], weights=[1, 2, 3], increasing=False",
    # Scenarios with erroneous or inappropriate values
    "y='invalid', weights='invalid', increasing='invalid'", 
    "y=[], weights=[], increasing=None"
]

tf_nn_l2_loss_Mutation_List = [
    # Typical parameter combinations
    "t=[0.1, 0.2, 0.3]", 
    "t=[0.4, 0.5, 0.6]",
    # Scenarios with erroneous or inappropriate values
    "t='invalid'", 
    "t=[]"
]

tf_nn_l2_normalize_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], axis=0", 
    "x=[0.4, 0.5, 0.6], axis=1",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', axis='invalid'", 
    "x=[], axis=-1"
]

tf_nn_leaky_relu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3], alpha=0.2", 
    "features=[-0.1, -0.2, -0.3], alpha=0.3",
    # Scenarios with erroneous or inappropriate values
    "features='invalid', alpha=-0.1", 
    "features=[], alpha=1.1"
]

tf_nn_learned_unigram_candidate_sampler_Mutation_List = [
    # Typical parameter combinations
    "true_classes=[1, 2, 3], num_true=2, num_sampled=5, unique=True", 
    "true_classes=[4, 5, 6], num_true=3, num_sampled=10, unique=False",
    # Scenarios with erroneous or inappropriate values
    "true_classes='invalid', num_true=-1, num_sampled=-5, unique='invalid'", 
    "true_classes=[], num_true=0, num_sampled=0, unique=None"
]

tf_nn_local_response_normalization_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], depth_radius=2, bias=1, alpha=0.1, beta=0.5", 
    "input=[[2, 3], [4, 5]], depth_radius=3, bias=2, alpha=0.2, beta=0.6",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', depth_radius=-1, bias='invalid', alpha=-0.1, beta=-0.5", 
    "input=[], depth_radius=0, bias=0, alpha=0, beta=0"
]

tf_nn_log_poisson_loss_Mutation_List = [
    # Typical parameter combinations
    "logits=[0.1, 0.2, 0.3], targets=[1, 2, 3]", 
    "logits=[0.4, 0.5, 0.6], targets=[4, 5, 6]",
    # Scenarios with erroneous or inappropriate values
    "logits='invalid', targets='invalid'", 
    "logits=[], targets=[]"
]
tf_nn_log_poisson_loss_Mutation_List = [
    # Typical parameter combinations
    "logits=[0.1, 0.2, 0.3], targets=[1, 2, 3]", 
    "logits=[0.4, 0.5, 0.6], targets=[4, 5, 6]",
    # Scenarios with erroneous or inappropriate values
    "logits='invalid', targets='invalid'", 
    "logits=[], targets=[]"
]

tf_nn_log_softmax_Mutation_List = [
    # Typical parameter combinations
    "logits=[0.1, 0.2, 0.3]", 
    "logits=[0.4, 0.5, 0.6]",
    # Scenarios with erroneous or inappropriate values
    "logits='invalid'", 
    "logits=[]"
]

tf_nn_lrn_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], depth_radius=2, bias=1, alpha=0.1, beta=0.5", 
    "input=[[2, 3], [4, 5]], depth_radius=3, bias=2, alpha=0.2, beta=0.6",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', depth_radius=-1, bias='invalid', alpha=-0.1, beta=-0.5", 
    "input=[], depth_radius=0, bias=0, alpha=0, beta=0"
]

tf_nn_max_pool_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], ksize=[2, 2], strides=[2, 2], padding='VALID'", 
    "input=[[2, 3], [4, 5]], ksize=[3, 3], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', ksize='invalid', strides='invalid', padding='invalid'", 
    "input=[], ksize=[], strides=[], padding='SAME'"
]

tf_nn_max_pool1d_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 3], ksize=2, strides=2, padding='VALID'", 
    "input=[2, 3, 4], ksize=3, strides=2, padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', ksize=-1, strides=-1, padding='invalid'", 
    "input=[], ksize=0, strides=0, padding='SAME'"
]

tf_nn_max_pool2d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], ksize=[2, 2], strides=[2, 2], padding='VALID'", 
    "input=[[2, 3], [4, 5]], ksize=[3, 3], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', ksize='invalid', strides='invalid', padding='invalid'", 
    "input=[], ksize=[], strides=[], padding='SAME'"
]

tf_nn_max_pool3d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2, 3], [4, 5, 6]], ksize=[2, 2, 2], strides=[2, 2, 2], padding='VALID'", 
    "input=[[2, 3, 4], [5, 6, 7]], ksize=[3, 3, 3], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', ksize='invalid', strides='invalid', padding='invalid'", 
    "input=[], ksize=[], strides=[], padding='SAME'"
]

tf_nn_max_pool_with_argmax_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], ksize=[2, 2], strides=[2, 2], padding='VALID', include_batch_in_index=True", 
    "input=[[2, 3], [4, 5]], ksize=[3, 3], strides=[2, 2], padding='SAME', include_batch_in_index=False",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', ksize='invalid', strides='invalid', padding='invalid', include_batch_in_index='invalid'", 
    "input=[], ksize=[], strides=[], padding='SAME', include_batch_in_index=None"
]
tf_nn_moments_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], axes=[0]", 
    "x=[0.4, 0.5, 0.6], axes=[1]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', axes='invalid'", 
    "x=[], axes=[]"
]

tf_nn_nce_loss_Mutation_List = [
    # Typical parameter combinations
    "weights=[[0.1, 0.2], [0.3, 0.4]], biases=[0.1, 0.2], labels=[[1, 2]], inputs=[[0.1, 0.2]], num_sampled=2, num_classes=4", 
    "weights=[[0.5, 0.6], [0.7, 0.8]], biases=[0.3, 0.4], labels=[[3, 4]], inputs=[[0.3, 0.4]], num_sampled=3, num_classes=5",
    # Scenarios with erroneous or inappropriate values
    "weights='invalid', biases='invalid', labels='invalid', inputs='invalid', num_sampled=-1, num_classes=-1", 
    "weights=[], biases=[], labels=[], inputs=[], num_sampled=0, num_classes=0"
]

tf_nn_normalize_moments_Mutation_List = [
    # Typical parameter combinations
    "counts=[10, 20], mean_ss=[0.1, 0.2], variance_ss=[0.01, 0.02], shift=0.0", 
    "counts=[15, 25], mean_ss=[0.15, 0.25], variance_ss=[0.015, 0.025], shift=0.1",
    # Scenarios with erroneous or inappropriate values
    "counts='invalid', mean_ss='invalid', variance_ss='invalid', shift='invalid'", 
    "counts=[], mean_ss=[], variance_ss=[], shift=None"
]

tf_nn_pool_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], window_shape=[2, 2], pooling_type='AVG', strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], window_shape=[3, 3], pooling_type='MAX', strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', window_shape='invalid', pooling_type='invalid', strides='invalid', padding='invalid'", 
    "input=[], window_shape=[], pooling_type=None, strides=[], padding='SAME'"
]

tf_nn_relu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, -0.2, 0.3]", 
    "features=[-0.1, 0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'", 
    "features=[]"
]

tf_nn_relu6_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, -0.2, 0.3]", 
    "features=[-0.1, 0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'", 
    "features=[]"
]

tf_nn_safe_embedding_lookup_sparse_Mutation_List = [
    # Typical parameter combinations
    "embedding_matrix=[[0.1, 0.2], [0.3, 0.4]], sp_ids=[[1, 2]], sp_weights=[[0.5, 0.5]]", 
    "embedding_matrix=[[0.5, 0.6], [0.7, 0.8]], sp_ids=[[3, 4]], sp_weights=[[0.6, 0.4]]",
    # Scenarios with erroneous or inappropriate values
    "embedding_matrix='invalid', sp_ids='invalid', sp_weights='invalid'", 
    "embedding_matrix=[], sp_ids=[], sp_weights=[]"
]
tf_nn_sampled_softmax_loss_Mutation_List = [
    # Typical parameter combinations
    "weights=[[0.1, 0.2], [0.3, 0.4]], biases=[0.1, 0.2], labels=[[1, 2]], inputs=[[0.1, 0.2]], num_sampled=2, num_classes=4",
    "weights=[[0.5, 0.6], [0.7, 0.8]], biases=[0.3, 0.4], labels=[[3, 4]], inputs=[[0.3, 0.4]], num_sampled=3, num_classes=5",
    # Scenarios with erroneous or inappropriate values
    "weights='invalid', biases='invalid', labels='invalid', inputs='invalid', num_sampled=-1, num_classes=-1",
    "weights=[], biases=[], labels=[], inputs=[], num_sampled=0, num_classes=0"
]

tf_nn_scale_regularization_loss_Mutation_List = [
    # Typical parameter combinations (As this function is used to scale regularization loss, examples will be generic)
    "loss=0.1, regularization_amount=0.01",
    "loss=0.2, regularization_amount=0.02",
    # Scenarios with erroneous or inappropriate values
    "loss='invalid', regularization_amount='invalid'",
    "loss=0, regularization_amount=0"
]

tf_nn_selu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]",
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=[]"
]

tf_nn_separable_conv2d_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], depthwise_filter=[[1, 0], [0, 1]], pointwise_filter=[[1, 1], [1, 1]], strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], depthwise_filter=[[0, 1], [1, 0]], pointwise_filter=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', depthwise_filter='invalid', pointwise_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], depthwise_filter=[], pointwise_filter=[], strides=[], padding='SAME'"
]

tf_nn_sigmoid_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3]",
    "x=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid'",
    "x=[]"
]

tf_nn_sigmoid_cross_entropy_with_logits_Mutation_List = [
    # Typical parameter combinations
    "labels=[0, 1], logits=[-1.0, 1.0]",
    "labels=[1, 0], logits=[1.0, -1.0]",
    # Scenarios with erroneous or inappropriate values
    "labels='invalid', logits='invalid'",
    "labels=[], logits=[]"
]

tf_nn_silu_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]",
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=[]"
]

tf_nn_softmax_Mutation_List = [
    # Typical parameter combinations
    "logits=[0.1, 0.2, 0.3]",
    "logits=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "logits='invalid'",
    "logits=[]"
]

tf_nn_softmax_cross_entropy_with_logits_Mutation_List = [
    # Typical parameter combinations
    "labels=[[0, 1], [1, 0]], logits=[[1.0, -1.0], [-1.0, 1.0]]",
    "labels=[[1, 0], [0, 1]], logits=[[-1.0, 1.0], [1.0, -1.0]]",
    # Scenarios with erroneous or inappropriate values
    "labels='invalid', logits='invalid'",
    "labels=[], logits=[]"
]

tf_nn_softplus_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]",
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=[]"
]

tf_nn_softsign_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]",
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=[]"
]
tf_nn_space_to_batch_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], block_shape=[2, 2], paddings=[[0, 0], [0, 0]]",
    "input=[[2, 3], [4, 5]], block_shape=[3, 3], paddings=[[1, 1], [1, 1]]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', block_shape='invalid', paddings='invalid'",
    "input=[], block_shape=[], paddings=[]"
]

tf_nn_space_to_depth_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], block_size=2",
    "input=[[2, 3], [4, 5]], block_size=3",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', block_size=-1",
    "input=[], block_size=0"
]

tf_nn_sparse_softmax_cross_entropy_with_logits_Mutation_List = [
    # Typical parameter combinations
    "labels=[0, 1], logits=[[1.0, -1.0], [-1.0, 1.0]]",
    "labels=[1, 0], logits=[[-1.0, 1.0], [1.0, -1.0]]",
    # Scenarios with erroneous or inappropriate values
    "labels='invalid', logits='invalid'",
    "labels=[], logits=[]"
]

tf_nn_sufficient_statistics_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], axes=[0], shift=None",
    "x=[0.4, 0.5, 0.6], axes=[1], shift=0.1",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', axes='invalid', shift='invalid'",
    "x=[], axes=[], shift=None"
]

tf_nn_swish_Mutation_List = [
    # Typical parameter combinations
    "features=[0.1, 0.2, 0.3]",
    "features=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=[]"
]

tf_nn_tanh_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3]",
    "x=[-0.1, -0.2, -0.3]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid'",
    "x=[]"
]

tf_nn_top_k_Mutation_List = [
    # Typical parameter combinations
    "input=[0.1, 0.2, 0.3], k=2",
    "input=[0.4, 0.5, 0.6], k=3",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', k=-1",
    "input=[], k=0"
]
tf_nn_weighted_cross_entropy_with_logits_Mutation_List = [
    # Typical parameter combinations
    "targets=[0, 1], logits=[-1.0, 1.0], pos_weight=2.0",
    "targets=[1, 0], logits=[1.0, -1.0], pos_weight=3.0",
    # Scenarios with erroneous or inappropriate values
    "targets='invalid', logits='invalid', pos_weight='invalid'",
    "targets=[], logits=[], pos_weight=-1"
]

tf_nn_weighted_moments_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], axes=[0], frequency_weights=[1, 2, 3]",
    "x=[0.4, 0.5, 0.6], axes=[1], frequency_weights=[2, 3, 4]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', axes='invalid', frequency_weights='invalid'",
    "x=[], axes=[], frequency_weights=[]"
]

tf_nn_with_space_to_batch_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], block_shape=[2, 2], paddings=[[0, 0], [0, 0]]",
    "input=[[2, 3], [4, 5]], block_shape=[3, 3], paddings=[[1, 1], [1, 1]]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', block_shape='invalid', paddings='invalid'",
    "input=[], block_shape=[], paddings=[]"
]

tf_nn_zero_fraction_Mutation_List = [
    # Typical parameter combinations
    "value=[0, 1, 0, 2, 0]",
    "value=[1, 2, 3, 4, 5]",
    "value=[1, 3, 2, 4, 5]",
    "value=[1, 3, 2, 0, 2]",
    # Scenarios with erroneous or inappropriate values
    "value='invalid'",
    "value=[]"
]
tf_raw_ops_BlockLSTM_Mutation_List = [
    # Typical parameter combinations
    "seq_len_max=5, x=[[0.1, 0.2], [0.3, 0.4]], cs_prev=[[0, 0], [0, 0]], h_prev=[[0, 0], [0, 0]], w=[[0.5, 0.6], [0.7, 0.8]], b=[0.1, 0.2]",
    "seq_len_max=10, x=[[0.2, 0.3], [0.4, 0.5]], cs_prev=[[1, 1], [1, 1]], h_prev=[[1, 1], [1, 1]], w=[[0.6, 0.7], [0.8, 0.9]], b=[0.3, 0.4]",
    # Additional combinations
    "seq_len_max=7, x=[[0.3, 0.4], [0.5, 0.6]], cs_prev=[[2, 2], [2, 2]], h_prev=[[2, 2], [2, 2]], w=[[0.7, 0.8], [0.9, 1.0]], b=[0.5, 0.6]",
    "seq_len_max=8, x=[[0.4, 0.5], [0.6, 0.7]], cs_prev=[[3, 3], [3, 3]], h_prev=[[3, 3], [3, 3]], w=[[0.8, 0.9], [1.0, 1.1]], b=[0.7, 0.8]",
    "seq_len_max=6, x=[[0.5, 0.6], [0.7, 0.8]], cs_prev=[[4, 4], [4, 4]], h_prev=[[4, 4], [4, 4]], w=[[0.9, 1.0], [1.1, 1.2]], b=[0.9, 1.0]"
]
tf_raw_ops_BlockLSTMGrad_Mutation_List = [
    # Typical parameter combinations
    "seq_len_max=5, x=[[0.1, 0.2], [0.3, 0.4]], cs_prev=[[0.1, 0.1], [0.2, 0.2]], h_prev=[[0.3, 0.3], [0.4, 0.4]], w=[[0.5, 0.5], [0.6, 0.6]], wci=[[0.7, 0.7], [0.8, 0.8]], wcf=[[0.9, 0.9], [1.0, 1.0]], wco=[[1.1, 1.1], [1.2, 1.2]], b=[[1.3, 1.3], [1.4, 1.4]], i=[[1.5, 1.5], [1.6, 1.6]], cs=[[1.7, 1.7], [1.8, 1.8]], f=[[1.9, 1.9], [2.0, 2.0]], o=[[2.1, 2.1], [2.2, 2.2]], ci=[[2.3, 2.3], [2.4, 2.4]], co=[[2.5, 2.5], [2.6, 2.6]], cs_grad=[[2.7, 2.7], [2.8, 2.8]], h_grad=[[2.9, 2.9], [3.0, 3.0]]",
    # Scenarios with erroneous or inappropriate values
    "seq_len_max=-1, x='invalid', cs_prev='invalid', h_prev='invalid', w='invalid', wci='invalid', wcf='invalid', wco='invalid', b='invalid', i='invalid', cs='invalid', f='invalid', o='invalid', ci='invalid', co='invalid', cs_grad='invalid', h_grad='invalid'"
]

tf_raw_ops_BlockLSTMGradV2_Mutation_List = [
    # Typical parameter combinations (Note: This is a complex operation, examples are simplified)
    "seq_len_max=10, x=[[0.1, 0.2]], cs_prev=[[0.3, 0.4]], h_prev=[[0.5, 0.6]], w=[[0.7, 0.8]], wci=[[0.9, 1.0]], wcf=[[1.1, 1.2]], wco=[[1.3, 1.4]], b=[[1.5, 1.6]]",
    # Scenarios with erroneous or inappropriate values
    "seq_len_max=-1, x='invalid', cs_prev='invalid', h_prev='invalid', w='invalid', wci='invalid', wcf='invalid', wco='invalid', b='invalid'"
]

tf_raw_ops_BlockLSTMV2_Mutation_List = [
    # Typical parameter combinations (Note: This is a complex operation, examples are simplified)
    "seq_len_max=10, x=[[0.1, 0.2]], cs_prev=[[0.3, 0.4]], h_prev=[[0.5, 0.6]], w=[[0.7, 0.8]], wci=[[0.9, 1.0]], wcf=[[1.1, 1.2]], wco=[[1.3, 1.4]], b=[[1.5, 1.6]]",
    # Scenarios with erroneous or inappropriate values
    "seq_len_max=-1, x='invalid', cs_prev='invalid', h_prev='invalid', w='invalid', wci='invalid', wcf='invalid', wco='invalid', b='invalid'"
]

tf_raw_ops_BoostedTreesTrainingPredict_Mutation_List = [
    # Typical parameter combinations (Note: This is a complex operation, examples are simplified)
    "tree_ensemble_handle='ensemble', bucketized_features=[[0.1, 0.2]], logits_dimension=2",

    # Scenarios with erroneous or inappropriate values
    "tree_ensemble_handle='invalid', bucketized_features='invalid', logits_dimension=-1"
]

tf_raw_ops_CSRSparseMatrixToDense_Mutation_List = [
    # Typical parameter combinations
    "sparse_input=[[0.1, 0.2], [0.3, 0.4]], type=tf.float32",
    # Scenarios with erroneous or inappropriate values
    "sparse_input='invalid', type='invalid'"
]

tf_raw_ops_CTCLoss_Mutation_List = [
    # Typical parameter combinations
    "inputs=[[0.1, 0.2]], labels=[[1, 2]], label_length=[2], logit_length=[2]",
    "inputs=[[0.2, 0.1]], labels=[[2, 1]], label_length=[2], logit_length=[2]",
    # Scenarios with erroneous or inappropriate values
    "inputs='invalid', labels='invalid', label_length='invalid', logit_length='invalid'"
]

tf_raw_ops_CTCLossV2_Mutation_List = [
    # Typical parameter combinations
    "inputs=[[0.1, 0.2]], labels=[[1, 2]], label_length=[2], logit_length=[2]",
    "inputs=[[0.2, 0.1]], labels=[[2, 1]], label_length=[2], logit_length=[2]",
    # Scenarios with erroneous or inappropriate values
    "inputs='invalid', labels='invalid', label_length='invalid', logit_length='invalid'"
]

tf_raw_ops_Conv_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    "input=[[2, 1], [4, 3]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides='invalid', padding='invalid'"
]

tf_raw_ops_Conv2D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    "input=[[2, 1], [4, 3]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides='invalid', padding='invalid'"
]
tf_raw_ops_Conv2DBackpropFilter_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[10, 10, 3, 3], filter_sizes=[3, 3, 3, 3], out_backprop=[[1, 2], [3, 4]], strides=[1, 1], padding='VALID'",
    "input_sizes=[10, 10, 3, 3], filter_sizes=[5, 5, 3, 3], out_backprop=[[2, 3], [4, 5]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter_sizes='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter_sizes=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv2DBackpropInput_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[10, 10, 3, 3], filter=[[1, 0], [0, 1]], out_backprop=[[1, 2], [3, 4]], strides=[1, 1], padding='VALID'",
    "input_sizes=[10, 10, 3, 3], filter=[[0, 1], [1, 0]], out_backprop=[[2, 3], [4, 5]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]
tf_raw_ops_Conv2DBackpropInput_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[1, 5, 5, 1], filter=[[1, 1, 1, 1], [1, 1, 1, 1]], out_backprop=[[1, 2], [3, 4]], strides=[1, 1, 1, 1], padding='VALID'",
    "input_sizes=[1, 5, 5, 1], filter=[[2, 2, 1, 1], [2, 2, 1, 1]], out_backprop=[[2, 3], [4, 5]], strides=[1, 2, 2, 1], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2, 3], [4, 5, 6]], filter=[[1, 0], [0, 1]], strides=[1, 1, 1], padding='VALID'",
    "input=[[2, 3, 4], [5, 6, 7]], filter=[[1, 1], [1, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides=[-1, -1, -1], padding='invalid'",
    "input=[], filter=[], strides=[0, 0, 0], padding='SAME'"
]
tf_raw_ops_Conv2DBackpropFilterV2_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter_sizes=[2, 2], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input=[[2, 3], [4, 5]], filter_sizes=[3, 3], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter_sizes='invalid', out_backprop='invalid', strides='invalid', padding='invalid'", 
    "input=[], filter_sizes=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv2DBackpropInputV2_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[2, 2], filter=[[1, 0], [0, 1]], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'", 
    "input_sizes=[3, 3], filter=[[1, 1], [1, 1]], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'", 
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]
tf_raw_ops_Conv3DBackpropFilter_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[10, 10, 10, 3, 3], filter_sizes=[3, 3, 3, 3, 3], out_backprop=[[1, 2, 3], [4, 5, 6]], strides=[1, 1, 1], padding='VALID'",
    "input_sizes=[10, 10, 10, 3, 3], filter_sizes=[5, 5, 5, 3, 3], out_backprop=[[2, 3, 4], [5, 6, 7]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter_sizes='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter_sizes=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3DBackpropInput_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[10, 10, 10, 3, 3], filter=[[1, 0], [0, 1]], out_backprop=[[1, 2, 3], [4, 5, 6]], strides=[1, 1, 1], padding='VALID'",
    "input_sizes=[10, 10, 10, 3, 3], filter=[[0, 1], [1, 0]], out_backprop=[[2, 3, 4], [5, 6, 7]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]
tf_raw_ops_Conv3D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2, 3], [4, 5, 6]], filter=[[1, 0, 1], [0, 1, 0]], strides=[1, 1, 1], padding='VALID'",
    "input=[[2, 3, 4], [5, 6, 7]], filter=[[0, 1, 0], [1, 0, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3DBackpropFilter_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2, 3], [4, 5, 6]], filter_sizes=[2, 2, 2], out_backprop=[[1, 0, 1], [0, 1, 0]], strides=[1, 1, 1], padding='VALID'",
    "input=[[2, 3, 4], [5, 6, 7]], filter_sizes=[3, 3, 3], out_backprop=[[0, 1, 0], [1, 0, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter_sizes='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input=[], filter_sizes=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3DBackpropFilterV2_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[1, 1, 1], filter=[[1, 0, 1], [0, 1, 0]], out_backprop=[[1, 0, 1], [0, 1, 0]], strides=[1, 1, 1], padding='VALID'",
    "input_sizes=[2, 2, 2], filter=[[0, 1, 0], [1, 0, 1]], out_backprop=[[0, 1, 0], [1, 0, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3DBackpropInput_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[1, 1, 1], filter=[[1, 0, 1], [0, 1, 0]], out_backprop=[[1, 0, 1], [0, 1, 0]], strides=[1, 1, 1], padding='VALID'",
    "input_sizes=[2, 2, 2], filter=[[0, 1, 0], [1, 0, 1]], out_backprop=[[0, 1, 0], [1, 0, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_Conv3DBackpropInputV2_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[1, 1, 1], filter=[[1, 0, 1], [0, 1, 0]], out_backprop=[[1, 0, 1], [0, 1, 0]], strides=[1, 1, 1], padding='VALID'",
    "input_sizes=[2, 2, 2], filter=[[0, 1, 0], [1, 0, 1]], out_backprop=[[0, 1, 0], [1, 0, 1]], strides=[2, 2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_CudnnRNN_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], input_h=[[1, 1]], input_c=[[0, 0]], params=[0.1, 0.2], rnn_mode='lstm'",
    "input=[[2, 3], [4, 5]], input_h=[[0, 0]], input_c=[[1, 1]], params=[0.3, 0.4], rnn_mode='gru'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', rnn_mode='invalid'",
    "input=[], input_h=[], input_c=[], params=[], rnn_mode=None"
]

tf_raw_ops_CudnnRNNBackprop_Mutation_List = [
    
    # Typical parameter combinations
    "input_data_shape=[10, 5, 20], input_h_shape=[5, 10], input_c_shape=[5, 10], params_size=100",
    "input_data_shape=[15, 8, 25], input_h_shape=[8, 15], input_c_shape=[8, 15], params_size=150",
    "input=[[1, 2], [3, 4]], input_h=[[1, 1]], input_c=[[0, 0]], params=[0.1, 0.2], output=[[1, 1]], output_h=[[0, 0]], output_c=[[1, 1]], rnn_mode='lstm'",
    "input=[[2, 3], [4, 5]], input_h=[[0, 0]], input_c=[[1, 1]], params=[0.3, 0.4], output=[[0, 0]], output_h=[[1, 1]], output_c=[[0, 0]], rnn_mode='gru'",
    # Scenarios with erroneous or inappropriate values
    "input_data_shape='invalid', input_h_shape='invalid', input_c_shape='invalid', params_size=-1",
    "input_data_shape=[], input_h_shape=[], input_c_shape=[], params_size=0",
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', output='invalid', output_h='invalid', output_c='invalid', rnn_mode='invalid'",
    "input=[], input_h=[], input_c=[], params=[], output=[], output_h=[], output_c=[], rnn_mode=None"
]
tf_raw_ops_CudnnRNNBackpropV2_Mutation_List = [
    # Typical parameter combinations (As this is a specialized RNN operation, examples will be generic)
    "input=[[1, 2], [3, 4]], input_h=[[1, 0], [0, 1]], input_c=[[1, 1], [0, 0]], params=[[0.1, 0.2], [0.3, 0.4]], sequence_lengths=[2, 2], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', sequence_lengths='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNNBackpropV3_Mutation_List = [
    # Similar to the V2 mutation list, with V3 specific parameters
    "input=[[1, 2], [3, 4]], input_h=[[1, 0], [0, 1]], input_c=[[1, 1], [0, 0]], params=[[0.1, 0.2], [0.3, 0.4]], sequence_lengths=[2, 2], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', sequence_lengths='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNNCanonicalToParams_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=4, input_size=3, weights=[0.1, 0.2, 0.3], biases=[0.4, 0.5, 0.6], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-1, input_size=-1, weights='invalid', biases='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNNCanonicalToParamsV2_Mutation_List = [
    # Similar to the non-V2 mutation list, with V2 specific parameters
    "num_layers=2, num_units=4, input_size=3, weights=[0.1, 0.2, 0.3], biases=[0.4, 0.5, 0.6], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-1, input_size=-1, weights='invalid', biases='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNNParamsSize_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=4, input_size=3, rnn_mode='lstm', input_mode='linear_input', direction='unidirectional'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-1, input_size=-1, rnn_mode='invalid', input_mode='invalid', direction='invalid'",
]

tf_raw_ops_CudnnRNNParamsToCanonical_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=4, input_size=3, params=[[0.1, 0.2], [0.3, 0.4]], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-1, input_size=-1, params='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNNParamsToCanonicalV2_Mutation_List = [
    # Similar to the non-V2 mutation list, with V2 specific parameters
    "num_layers=2, num_units=4, input_size=3, params=[[0.1, 0.2], [0.3, 0.4]], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-1, input_size=-1, params='invalid', rnn_mode='invalid'",
]

tf_raw_ops_CudnnRNN_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], input_h=[[1, 1]], input_c=[[1, 1]], params=[[0.1, 0.2]], rnn_mode='lstm'",
    "input=[[2, 3], [4, 5]], input_h=[[2, 2]], input_c=[[2, 2]], params=[[0.2, 0.3]], rnn_mode='gru'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', rnn_mode='invalid'",
    "input=[], input_h=[], input_c=[], params=[], rnn_mode=None"
]


tf_raw_ops_CudnnRNNBackpropV2_Mutation_List = [
    # Similar to CudnnRNNBackprop, with additional versioning
    "input_data_shape=[10, 5, 20], input_h_shape=[5, 10], input_c_shape=[5, 10], params_size=100",
    "input_data_shape=[15, 8, 25], input_h_shape=[8, 15], input_c_shape=[8, 15], params_size=150",
    # Scenarios with erroneous or inappropriate values
    "input_data_shape='invalid', input_h_shape='invalid', input_c_shape='invalid', params_size=-1",
    "input_data_shape=[], input_h_shape=[], input_c_shape=[], params_size=0"
]

tf_raw_ops_CudnnRNNBackpropV3_Mutation_List = [
    # Similar to CudnnRNNBackprop, with additional versioning and options
    "input_data_shape=[10, 5, 20], input_h_shape=[5, 10], input_c_shape=[5, 10], params_size=100",
    "input_data_shape=[15, 8, 25], input_h_shape=[8, 15], input_c_shape=[8, 15], params_size=150",
    # Scenarios with erroneous or inappropriate values
    "input_data_shape='invalid', input_h_shape='invalid', input_c_shape='invalid', params_size=-1",
    "input_data_shape=[], input_h_shape=[], input_c_shape=[], params_size=0"
]

tf_raw_ops_CudnnRNNCanonicalToParams_Mutation_List = [
    # Typical parameter combinations (generic due to complexity)
    "num_layers=2, num_units=10, input_size=20, num_params=5, rnn_mode='lstm'",
    "num_layers=3, num_units=15, input_size=25, num_params=8, rnn_mode='gru'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units='invalid', input_size='invalid', num_params=-1, rnn_mode='invalid'",
    "num_layers=0, num_units=0, input_size=0, num_params=0, rnn_mode=None"
]
tf_raw_ops_CudnnRNNCanonicalToParamsV2_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=10, input_size=5, weights=[0.1, 0.2], biases=[0.1, 0.2]",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-10, input_size=-5, weights='invalid', biases='invalid'"
]

tf_raw_ops_CudnnRNNParamsSize_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=10, input_size=5, dtype=tf.float32, rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-10, input_size=-5, dtype='invalid', rnn_mode='invalid'"
]

tf_raw_ops_CudnnRNNParamsToCanonical_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=10, input_size=5, params=[0.1, 0.2]",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-10, input_size=-5, params='invalid'"
]

tf_raw_ops_CudnnRNNParamsToCanonicalV2_Mutation_List = [
    # Typical parameter combinations
    "num_layers=2, num_units=10, input_size=5, params=[0.1, 0.2], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "num_layers=-1, num_units=-10, input_size=-5, params='invalid', rnn_mode='invalid'"
]

tf_raw_ops_CudnnRNNV2_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], input_h=[[1, 2]], input_c=[[1, 2]], params=[0.1, 0.2], rnn_mode='lstm'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', rnn_mode='invalid'"
]

tf_raw_ops_CudnnRNNV3_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], input_h=[[1, 2]], input_c=[[1, 2]], params=[0.1, 0.2], rnn_mode='lstm', is_training=True",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', input_h='invalid', input_c='invalid', params='invalid', rnn_mode='invalid', is_training='invalid'"
]
tf_raw_ops_DenseBincount_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 3], size=5, weights=[0.1, 0.2, 0.3]",
    "input=[2, 3, 4], size=6, weights=[0.2, 0.3, 0.4]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', size=-1, weights='invalid'",
    "input=[], size=0, weights=[]"
]

tf_raw_ops_DenseCountSparseOutput_Mutation_List = [
    # Typical parameter combinations
    "values=[1, 2, 3], weights=[0.1, 0.2, 0.3], binary_output=False",
    # Scenarios with erroneous or inappropriate values
    "values='invalid', weights='invalid', binary_output='invalid'"
]

tf_raw_ops_DenseToCSRSparseMatrix_Mutation_List = [
    # Typical parameter combinations
    "dense_input=[[1, 0], [0, 2]]",
    # Scenarios with erroneous or inappropriate values
    "dense_input='invalid'"
]

tf_raw_ops_DenseToDenseSetOperation_Mutation_List = [
    # Typical parameter combinations
    "set1=[[1, 2], [3, 4]], set2=[[2, 3], [4, 5]], set_operation='intersection'",
    # Scenarios with erroneous or inappropriate values
    "set1='invalid', set2='invalid', set_operation='invalid'"
]
tf_raw_ops_DenseToSparseBatchDataset_Mutation_List = [
    # Typical parameter combinations
    "input_dataset='dataset', batch_size=2, row_shape=[2]",
    "input_dataset='dataset', batch_size=3, row_shape=[3]",
    # Scenarios with erroneous or inappropriate values
    "input_dataset='invalid', batch_size=-1, row_shape='invalid'",
    "input_dataset=None, batch_size=0, row_shape=[]"
]

tf_raw_ops_DenseToSparseSetOperation_Mutation_List = [
    # Typical parameter combinations
    "set1=[[1, 2], [3, 4]], set2=[[5, 6], [7, 8]], set_operation='intersection'",
    "set1=[[2, 3], [4, 5]], set2=[[6, 7], [8, 9]], set_operation='union'",
    # Scenarios with erroneous or inappropriate values
    "set1='invalid', set2='invalid', set_operation='invalid'",
    "set1=[], set2=[], set_operation=None"
]

tf_raw_ops_DepthwiseConv2dNative_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], strides=[], padding='SAME'"
]

tf_raw_ops_DepthwiseConv2dNativeBackpropFilter_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter_sizes=[2, 2], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], filter_sizes=[3, 3], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter_sizes='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input=[], filter_sizes=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_DepthwiseConv2dNativeBackpropInput_Mutation_List = [
    # Typical parameter combinations
    "input_sizes=[2, 2], filter=[[1, 0], [0, 1]], out_backprop=[[1, 0], [0, 1]], strides=[1, 1], padding='VALID'",
    "input_sizes=[3, 3], filter=[[1, 1], [1, 1]], out_backprop=[[1, 1], [1, 1]], strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input_sizes='invalid', filter='invalid', out_backprop='invalid', strides='invalid', padding='invalid'",
    "input_sizes=[], filter=[], out_backprop=[], strides=[], padding='SAME'"
]

tf_raw_ops_FusedPadConv2D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], paddings=[[0, 0], [1, 1]], filter=[[1, 0], [0, 1]], mode='REFLECT'",
    "input=[[2, 3], [4, 5]], paddings=[[1, 1], [2, 2]], filter=[[0, 1], [1, 0]], mode='SYMMETRIC'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', paddings='invalid', filter='invalid', mode='invalid'",
    "input=[], paddings=[], filter=[], mode=None"
]

tf_raw_ops_FusedResizeAndPadConv2D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], size=[2, 2], paddings=[[0, 0], [1, 1]], filter=[[1, 0], [0, 1]], resize_align_corners=False, mode='REFLECT'",
    "input=[[2, 3], [4, 5]], size=[3, 3], paddings=[[1, 1], [2, 2]], filter=[[0, 1], [1, 0]], resize_align_corners=True, mode='SYMMETRIC'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', size='invalid', paddings='invalid', filter='invalid', resize_align_corners='invalid', mode='invalid'",
    "input=[], size=[], paddings=[], filter=[], resize_align_corners=None, mode=None"
]

tf_raw_ops_GRUBlockCell_Mutation_List = [
    # Typical parameter combinations
    "x=[[0.1, 0.2]], h_prev=[[0.3, 0.4]], w_ru=[[0.5, 0.6]], w_c=[[0.7, 0.8]], b_ru=[[0.9, 1.0]], b_c=[[1.1, 1.2]]",
    "x=[[0.2, 0.3]], h_prev=[[0.4, 0.5]], w_ru=[[0.6, 0.7]], w_c=[[0.8, 0.9]], b_ru=[[1.0, 1.1]], b_c=[[1.2, 1.3]]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', h_prev='invalid', w_ru='invalid', w_c='invalid', b_ru='invalid', b_c='invalid'",
    "x=[], h_prev=[], w_ru=[], w_c=[], b_ru=[], b_c=[]"
]

tf_raw_ops_GRUBlockCellGrad_Mutation_List = [
    # Typical parameter combinations
    "x=[[0.1, 0.2]], h_prev=[[0.3, 0.4]], w_ru=[[0.5, 0.6]], w_c=[[0.7, 0.8]], b_ru=[[0.9, 1.0]], b_c=[[1.1, 1.2]], d_h=[[1.3, 1.4]]",
    "x=[[0.2, 0.3]], h_prev=[[0.4, 0.5]], w_ru=[[0.6, 0.7]], w_c=[[0.8, 0.9]], b_ru=[[1.0, 1.1]], b_c=[[1.2, 1.3]], d_h=[[1.4, 1.5]]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', h_prev='invalid', w_ru='invalid', w_c='invalid', b_ru='invalid', b_c='invalid', d_h='invalid'",
    "x=[], h_prev=[], w_ru=[], w_c=[], b_ru=[], b_c=[], d_h=[]"
]

tf_raw_ops_L2Loss_Mutation_List = [
    # Typical parameter combinations
    "t=[[0.1, 0.2], [0.3, 0.4]]",
    "t=[[0.5, 0.6], [0.7, 0.8]]",
    # Scenarios with erroneous or inappropriate values
    "t='invalid'",
    "t=[]"
]
tf_raw_ops_LSTMBlockCell_Mutation_List = [
    # Typical parameter combinations (as raw_ops are low-level operations, examples will be generic)
    "x=[0.1, 0.2, 0.3], cs_prev=[0.4, 0.5, 0.6], h_prev=[0.7, 0.8, 0.9], w=[1, 1, 1], b=[0.1, 0.2, 0.3]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', cs_prev='invalid', h_prev='invalid', w='invalid', b='invalid'",
    "x=[], cs_prev=[], h_prev=[], w=[], b=[]"
]

tf_raw_ops_LSTMBlockCellGrad_Mutation_List = [
    # Typical parameter combinations
    "x=[0.1, 0.2, 0.3], cs_prev=[0.4, 0.5, 0.6], h_prev=[0.7, 0.8, 0.9], w=[1, 1, 1], b=[0.1, 0.2, 0.3], grad=[0.1, 0.2, 0.3]",
    # Scenarios with erroneous or inappropriate values
    "x='invalid', cs_prev='invalid', h_prev='invalid', w='invalid', b='invalid', grad='invalid'",
    "x=[], cs_prev=[], h_prev=[], w=[], b=[], grad=[]"
]

tf_raw_ops_QuantizedConv2D_Mutation_List = [
    # Typical parameter combinations
    "input=[1, 2, 3, 4], filter=[5, 6, 7, 8], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, strides=[1, 1, 1, 1], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], min_input=0, max_input=0, min_filter=0, max_filter=0, strides=[], padding='SAME'"
]
tf_raw_ops_QuantizedConv2DAndRelu_Mutation_List = [
    # Typical parameter combinations (generic, as actual parameters can be complex)
    "input=[1, 2, 3], filter=[4, 5, 6], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, strides=[1, 1], padding='VALID'",
    "input=[2, 3, 4], filter=[5, 6, 7], min_input=0.0, max_input=2.0, min_filter=0.0, max_filter=2.0, strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], min_input=0, max_input=0, min_filter=0, max_filter=0, strides=[], padding='SAME'"
]
tf_raw_ops_QuantizedConv2DAndReluAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4, out_type=tf.float32",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0, max_input=5, min_filter=0, max_filter=5, out_type=tf.float32",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', out_type='invalid'",
    "input=[], filter=[], min_input=None, max_input=None, min_filter=None, max_filter=None, out_type=None"
]

tf_raw_ops_QuantizedConv2DAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4, out_type=tf.float32",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0, max_input=5, min_filter=0, max_filter=5, out_type=tf.float32",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', out_type='invalid'",
    "input=[], filter=[], min_input=None, max_input=None, min_filter=None, max_filter=None, out_type=None"
]

tf_raw_ops_QuantizedConv2DPerChannel_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0, max_input=5, min_filter=0, max_filter=5",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid'",
    "input=[], filter=[], min_input=None, max_input=None, min_filter=None, max_filter=None"
]
tf_raw_ops_QuantizedConv2DWithBias_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, strides=[1, 1], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input=-1.0, max_input=-1.0, min_filter=-1.0, max_filter=-1.0, strides='invalid', padding='invalid'"
]

tf_raw_ops_QuantizedConv2DWithBiasAndRelu_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, strides=[1, 1], padding='VALID'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input=-1.0, max_input=-1.0, min_filter=-1.0, max_filter=-1.0, strides='invalid', padding='invalid'"
]

tf_raw_ops_QuantizedConv2DWithBiasSumAndReluAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input_min=0.0, input_max=10.0, filter_min=0.0, filter_max=10.0, bias_min=0.0, bias_max=10.0, sum_min=0.0, sum_max=10.0, out_type=tf.float32",
    "input_min=-5.0, input_max=5.0, filter_min=-5.0, filter_max=5.0, bias_min=-5.0, bias_max=5.0, sum_min=-5.0, sum_max=5.0, out_type=tf.float32",
    # Scenarios with erroneous or inappropriate values
    "input_min='invalid', input_max='invalid', filter_min='invalid', filter_max='invalid', bias_min='invalid', bias_max='invalid', sum_min='invalid', sum_max='invalid', out_type='invalid'",
    "input_min=10.0, input_max=0.0, filter_min=10.0, filter_max=0.0, bias_min=10.0, bias_max=0.0, sum_min=10.0, sum_max=0.0, out_type=tf.int32"
]
tf_raw_ops_QuantizedConv2DWithBiasAndReluAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4, min_freezed_output=0, max_freezed_output=4",
    "input=[[2, 3], [4, 5]], filter=[[0, 1], [1, 0]], min_input=1, max_input=5, min_filter=1, max_filter=5, min_freezed_output=1, max_freezed_output=5",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', min_freezed_output='invalid', max_freezed_output='invalid'",
    "input=[], filter=[], min_input=-1, max_input=-1, min_filter=-1, max_filter=-1, min_freezed_output=-1, max_freezed_output=-1"
]

tf_raw_ops_QuantizedConv2DWithBiasAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4",
    "input=[[2, 3], [4, 5]], filter=[[0, 1], [1, 0]], min_input=1, max_input=5, min_filter=1, max_filter=5",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid'",
    "input=[], filter=[], min_input=-1, max_input=-1, min_filter=-1, max_filter=-1"
]

tf_raw_ops_QuantizedConv2DWithBiasSignedSumAndReluAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], summand=[[0.5, 0.5], [0.5, 0.5]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4, min_freezed_output=0, max_freezed_output=4",
    "input=[[2, 3], [4, 5]], summand=[[0.6, 0.4], [0.4, 0.6]], filter=[[0, 1], [1, 0]], min_input=1, max_input=5, min_filter=1, max_filter=5, min_freezed_output=1, max_freezed_output=5",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', summand='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', min_freezed_output='invalid', max_freezed_output='invalid'",
    "input=[], summand=[], filter=[], min_input=-1, max_input=-1, min_filter=-1, max_filter=-1, min_freezed_output=-1, max_freezed_output=-1"
]

tf_raw_ops_QuantizedConv2DWithBiasSumAndRelu_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], summand=[[0.5, 0.5], [0.5, 0.5]], filter=[[1, 0], [0, 1]], min_input=0, max_input=4, min_filter=0, max_filter=4",
    "input=[[2, 3], [4, 5]], summand=[[0.6, 0.4], [0.4, 0.6]], filter=[[0, 1], [1, 0]], min_input=1, max_input=5, min_filter=1, max_filter=5",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', summand='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid'",
    "input=[], summand=[], filter=[], min_input=-1, max_input=-1, min_filter=-1, max_filter=-1"
]
tf_raw_ops_QuantizedDepthwiseConv2DWithBias_Mutation_List = [
    # Typical parameter combinations
    "input=[0.1, 0.2], filter=[0.3, 0.4], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, bias=[0.1, 0.2]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input=-1.0, max_input=-1.0, min_filter=-1.0, max_filter=-1.0, bias='invalid'"
]

tf_raw_ops_QuantizedDepthwiseConv2DWithBiasAndRelu_Mutation_List = [
    # Typical parameter combinations
    "input=[0.1, 0.2], filter=[0.3, 0.4], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, bias=[0.1, 0.2]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input=-1.0, max_input=-1.0, min_filter=-1.0, max_filter=-1.0, bias='invalid'"
]

tf_raw_ops_QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize_Mutation_List = [
    # Typical parameter combinations
    "input=[0.1, 0.2], filter=[0.3, 0.4], min_input=0.0, max_input=1.0, min_filter=0.0, max_filter=1.0, bias=[0.1, 0.2]",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input=-1.0, max_input=-1.0, min_filter=-1.0, max_filter=-1.0, bias='invalid'"
]
tf_raw_ops_QuantizedDepthwiseConv2D_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0.0, max_input=3.0, min_filter=0.0, max_filter=1.0, strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0.0, max_input=4.0, min_filter=0.0, max_filter=2.0, strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], min_input=-1.0, max_input=-2.0, min_filter=-1.0, max_filter=-2.0, strides=[], padding='SAME'"
]
tf_raw_ops_RecvTPUEmbeddingActivations_Mutation_List = [
    # Typical parameter combinations (generic as this is a TPU-specific operation)
    "config='sample_config', max_sequence_length=128",
    # Scenarios with erroneous or inappropriate values
    "config='invalid', max_sequence_length=-1"
]
tf_raw_ops_SdcaOptimizer_Mutation_List = [
    # Typical parameter combinations
    "sparse_example_indices=[1, 2], sparse_feature_indices=[3, 4], sparse_feature_values=[0.1, 0.2], dense_features=[[0.3, 0.4]], example_weights=[0.5, 0.6], example_labels=[0, 1], sparse_indices=[7, 8], sparse_weights=[0.7, 0.8], dense_weights=[[0.9, 1.0]], l1_regularization_strength=0.01, l2_regularization_strength=0.02",
    # Scenarios with erroneous or inappropriate values
    "sparse_example_indices='invalid', sparse_feature_indices='invalid', sparse_feature_values='invalid', dense_features='invalid', example_weights='invalid', example_labels='invalid', sparse_indices='invalid', sparse_weights='invalid', dense_weights='invalid', l1_regularization_strength='invalid', l2_regularization_strength='invalid'"
]

tf_raw_ops_SdcaOptimizerV2_Mutation_List = [
    # Typical parameter combinations
    "sparse_example_indices=[1, 2], sparse_feature_indices=[3, 4], sparse_feature_values=[0.1, 0.2], dense_features=[[0.3, 0.4]], example_weights=[0.5, 0.6], example_labels=[0, 1], sparse_indices=[7, 8], sparse_weights=[0.7, 0.8], dense_weights=[[0.9, 1.0]], l1_regularization_strength=0.01, l2_regularization_strength=0.02, adaptative=True",
    # Scenarios with erroneous or inappropriate values
    "sparse_example_indices='invalid', sparse_feature_indices='invalid', sparse_feature_values='invalid', dense_features='invalid', example_weights='invalid', example_labels='invalid', sparse_indices='invalid', sparse_weights='invalid', dense_weights='invalid', l1_regularization_strength='invalid', l2_regularization_strength='invalid', adaptative='invalid'"
]

tf_raw_ops_SparseDenseCwiseAdd_Mutation_List = [
    # Typical parameter combinations
    "sp_indices=[[0, 0], [1, 1]], sp_values=[1, 2], sp_shape=[2, 2], dense=[3, 4]",
    # Scenarios with erroneous or inappropriate values
    "sp_indices='invalid', sp_values='invalid', sp_shape='invalid', dense='invalid'"
]

tf_raw_ops_SparseDenseCwiseDiv_Mutation_List = [
    # Typical parameter combinations
    "sp_indices=[[0, 0], [1, 1]], sp_values=[1, 2], sp_shape=[2, 2], dense=[3, 4]",
    # Scenarios with erroneous or inappropriate values
    "sp_indices='invalid', sp_values='invalid', sp_shape='invalid', dense='invalid'"
]

tf_raw_ops_SparseDenseCwiseMul_Mutation_List = [
    # Typical parameter combinations
    "sp_indices=[[0, 0], [1, 1]], sp_values=[1, 2], sp_shape=[2, 2], dense=[3, 4]",
    # Scenarios with erroneous or inappropriate values
    "sp_indices='invalid', sp_values='invalid', sp_shape='invalid', dense='invalid'"
]

tf_raw_ops_SparseTensorDenseAdd_Mutation_List = [
    # Typical parameter combinations
    "sp_indices=[[0, 0], [1, 1]], sp_values=[1, 2], sp_shape=[2, 2], dense=[[3, 4], [5, 6]]",
    # Scenarios with erroneous or inappropriate values
    "sp_indices='invalid', sp_values='invalid', sp_shape='invalid', dense='invalid'"
]

tf_raw_ops_SparseTensorDenseMatMul_Mutation_List = [
    # Typical parameter combinations
    "sp_indices=[[0, 0], [1, 1]], sp_values=[1, 2], sp_shape=[2, 2], dense=[[3, 4], [5, 6]], adjoint_a=False, adjoint_b=False",
    # Scenarios with erroneous or inappropriate values
    "sp_indices='invalid', sp_values='invalid', sp_shape='invalid', dense='invalid', adjoint_a='invalid', adjoint_b='invalid'"
]
tf_raw_ops_SparseToDense_Mutation_List = [
    # Typical parameter combinations
    "sparse_indices=[[0, 0], [1, 1]], output_shape=[2, 2], sparse_values=[1, 2], default_value=0",
    "sparse_indices=[[1, 0], [0, 1]], output_shape=[2, 2], sparse_values=[3, 4], default_value=1",
    # Scenarios with erroneous or inappropriate values
    "sparse_indices='invalid', output_shape='invalid', sparse_values='invalid', default_value='invalid'",
    "sparse_indices=[], output_shape=[], sparse_values=[], default_value=None"
]

tf_raw_ops_TpuEmbeddingActivations_Mutation_List = [
    # Typical parameter combinations (As this function is for TPU embedding, examples will be generic)
    "activations=[0.1, 0.2, 0.3], table_id=0, lookup_id=1",
    "activations=[0.4, 0.5, 0.6], table_id=1, lookup_id=2",
    # Scenarios with erroneous or inappropriate values
    "activations='invalid', table_id=-1, lookup_id=-1",
    "activations=[], table_id=0, lookup_id=0"
]

tf_raw_ops_UniformQuantizedConvolution_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=10, min_filter=0, max_filter=10, strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0, max_input=10, min_filter=0, max_filter=10, strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], min_input=0, max_input=0, min_filter=0, max_filter=0, strides=[], padding='SAME'"
]

tf_raw_ops_UniformQuantizedConvolutionHybrid_Mutation_List = [
    # Typical parameter combinations
    "input=[[1, 2], [3, 4]], filter=[[1, 0], [0, 1]], min_input=0, max_input=10, min_filter=0, max_filter=10, strides=[1, 1], padding='VALID'",
    "input=[[2, 3], [4, 5]], filter=[[1, 1], [1, 1]], min_input=0, max_input=10, min_filter=0, max_filter=10, strides=[2, 2], padding='SAME'",
    # Scenarios with erroneous or inappropriate values
    "input='invalid', filter='invalid', min_input='invalid', max_input='invalid', min_filter='invalid', max_filter='invalid', strides='invalid', padding='invalid'",
    "input=[], filter=[], min_input=0, max_input=0, min_filter=0, max_filter=0, strides=[], padding='SAME'"
]
tf_train_BytesList_Mutation_List = [
    # Typical parameter combinations
    "value=[b'example1', b'example2']",
    # Scenarios with erroneous or inappropriate values
    "value='invalid'",
    "value=[]"
]

tf_train_Checkpoint_Mutation_List = [
    # Typical parameter combinations
    # As Checkpoint is used to save and restore variables, examples will be generic
    "a=tf.Variable(1.0), b=tf.Variable(2.0)",
    # Scenarios with erroneous or inappropriate values
    "a='invalid', b='invalid'",
    "a=None, b=None"
]

tf_train_CheckpointManager_Mutation_List = [
    # Typical parameter combinations
    "checkpoint=tf.train.Checkpoint(), directory='/path/to/dir', max_to_keep=5",
    # Scenarios with erroneous or inappropriate values
    "checkpoint='invalid', directory='invalid', max_to_keep=-1",
    "checkpoint=None, directory='', max_to_keep=0"
]

tf_train_CheckpointOptions_Mutation_List = [
    # Typical parameter combinations
    "experimental_io_device='/job:localhost'",
    # Scenarios with erroneous or inappropriate values
    "experimental_io_device='invalid'",
    "experimental_io_device=None"
]

tf_train_CheckpointView_Mutation_List = [
    # Typical parameter combinations
    # As CheckpointView is used to inspect checkpoint contents, examples will be generic
    "checkpoint_path='/path/to/checkpoint'",
    # Scenarios with erroneous or inappropriate values
    "checkpoint_path='invalid'",
    "checkpoint_path=None"
]

tf_train_ClusterDef_Mutation_List = [
    # Typical parameter combinations
    # As ClusterDef is used for TensorFlow cluster specifications, examples will be generic
    "job={name='worker', tasks={0='localhost:2222'}}",
    # Scenarios with erroneous or inappropriate values
    "job='invalid'",
    "job=None"
]

tf_train_ClusterSpec_Mutation_List = [
    # Typical parameter combinations
    "cluster={'worker': ['localhost:2222', 'localhost:2223']}",
    # Scenarios with erroneous or inappropriate values
    "cluster='invalid'",
    "cluster=None"
]

tf_train_Coordinator_Mutation_List = [
    # Typical parameter combinations
    # As Coordinator is used for coordinating threads, examples will be generic
    "",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'"
]

tf_train_Example_Mutation_List = [
    # Typical parameter combinations
    "features=tf.train.Features(feature={'feature1': tf.train.Feature()})",
    # Scenarios with erroneous or inappropriate values
    "features='invalid'",
    "features=None"
]

tf_train_ExponentialMovingAverage_Mutation_List = [
    # Typical parameter combinations
    "decay=0.99, num_updates=100",
    # Scenarios with erroneous or inappropriate values
    "decay='invalid', num_updates=-1",
    "decay=None, num_updates=0"
]
tf_train_Feature_Mutation_List = [
    # Typical parameter combinations
    "kind={'bytes_list': BytesList(value=[b'Hello', b'World'])}",
    "kind={'int64_list': Int64List(value=[1, 2, 3])}",
    # Scenarios with erroneous or inappropriate values
    "kind='invalid'",
    "kind={}"
]

tf_train_FeatureList_Mutation_List = [
    # Typical parameter combinations
    "feature=[Feature(kind={'bytes_list': BytesList(value=[b'Hello']))], Feature(kind={'int64_list': Int64List(value=[1]))]",
    "feature=[Feature(kind={'bytes_list': BytesList(value=[b'World']))], Feature(kind={'int64_list': Int64List(value=[2]))]",
    # Scenarios with erroneous or inappropriate values
    "feature='invalid'",
    "feature=[]"
]

tf_train_FeatureLists_Mutation_List = [
    # Typical parameter combinations
    "feature_list={'list1': FeatureList(feature=[Feature(kind={'bytes_list': BytesList(value=[b'Hello']))])}",
    "feature_list={'list2': FeatureList(feature=[Feature(kind={'int64_list': Int64List(value=[1]))])}",
    # Scenarios with erroneous or inappropriate values
    "feature_list='invalid'",
    "feature_list={}"
]

tf_train_Features_Mutation_List = [
    # Typical parameter combinations
    "feature={'feature1': Feature(kind={'bytes_list': BytesList(value=[b'Hello']))}",
    "feature={'feature2': Feature(kind={'int64_list': Int64List(value=[1]))}",
    # Scenarios with erroneous or inappropriate values
    "feature='invalid'",
    "feature={}"
]

tf_train_FloatList_Mutation_List = [
    # Typical parameter combinations
    "value=[1.0, 2.0, 3.0]",
    "value=[4.0, 5.0, 6.0]",
    # Scenarios with erroneous or inappropriate values
    "value='invalid'",
    "value=[]"
]

tf_train_Int64List_Mutation_List = [
    # Typical parameter combinations
    "value=[1, 2, 3]",
    "value=[4, 5, 6]",
    # Scenarios with erroneous or inappropriate values
    "value='invalid'",
    "value=[]"
]

tf_train_JobDef_Mutation_List = [
    # Typical parameter combinations (generic, as JobDef is typically used for distributed training)
    "name='worker', tasks={0: 'localhost:2222'}",
    "name='ps', tasks={0: 'localhost:2223'}",
    # Scenarios with erroneous or inappropriate values
    "name='invalid', tasks='invalid'",
    "name='', tasks={}"
]

tf_train_SequenceExample_Mutation_List = [
    # Typical parameter combinations
    "context=Features(feature={'feature1': Feature(kind={'bytes_list': BytesList(value=[b'Hello']))}), feature_lists=FeatureLists(feature_list={'list1': FeatureList(feature=[Feature(kind={'int64_list': Int64List(value=[1]))])})",
    "context=Features(feature={'feature2': Feature(kind={'bytes_list': BytesList(value=[b'World']))}), feature_lists=FeatureLists(feature_list={'list2': FeatureList(feature=[Feature(kind={'int64_list': Int64List(value=[2]))])})",
    # Scenarios with erroneous or inappropriate values
    "context='invalid', feature_lists='invalid'",
    "context={}, feature_lists={}"
]
tf_train_ServerDef_Mutation_List = [
    # Typical parameter combinations
    "cluster={'worker': ['worker0:2222', 'worker1:2222'], 'ps': ['ps0:2222']}, job_name='worker', task_index=0, protocol='grpc'",
    "cluster={'worker': ['worker0:2222', 'worker1:2222'], 'ps': ['ps0:2222', 'ps1:2222']}, job_name='ps', task_index=1, protocol='grpc+ssl'",
    # Scenarios with erroneous or inappropriate values
    "cluster='invalid', job_name='invalid', task_index=-1, protocol='invalid'",
    "cluster={}, job_name=None, task_index=None, protocol=None"
]

tf_train_TrackableView_Mutation_List = [
    # Typical parameter combinations (as a placeholder since this is a view object)
    "object=SomeTensorFlowObject", 
    "object=AnotherTensorFlowObject",
    # Scenarios with erroneous or inappropriate values
    "object='invalid'", 
    "object=None"
]

tf_train_checkpoints_iterator_Mutation_List = [
    # Typical parameter combinations
    "checkpoint_dir='/path/to/checkpoints', min_interval_secs=30, timeout=None",
    "checkpoint_dir='/another/path/to/checkpoints', min_interval_secs=60, timeout=120",
    # Scenarios with erroneous or inappropriate values
    "checkpoint_dir='invalid', min_interval_secs=-30, timeout='invalid'",
    "checkpoint_dir=None, min_interval_secs=0, timeout=0"
]

tf_train_experimental_Mutation_List = [
    # This is a module, so no typical parameter combinations. Providing placeholders
    "", 
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_train_experimental_PythonState_Mutation_List = [
    # This is a class for Python state management, so no typical parameter combinations. Providing placeholders
    "",
    # Scenarios with erroneous or inappropriate values
    "invalid_param='invalid'", "1, 2, 3", "use_bias=True", "activation='relu'", "dropout=0.3"
]

tf_train_get_checkpoint_state_Mutation_List = [
    # Typical parameter combinations
    "checkpoint_dir='/path/to/checkpoints'", 
    "checkpoint_dir='/another/path/to/checkpoints'",
    # Scenarios with erroneous or inappropriate values
    "checkpoint_dir='invalid'", 
    "checkpoint_dir=None"
]

tf_train_latest_checkpoint_Mutation_List = [
    # Typical parameter combinations
    "checkpoint_dir='/path/to/checkpoints'", 
    "checkpoint_dir='/another/path/to/checkpoints'",
    # Scenarios with erroneous or inappropriate values
    "checkpoint_dir='invalid'", 
    "checkpoint_dir=None"
]

tf_train_list_variables_Mutation_List = [
    # Typical parameter combinations
    "ckpt_dir_or_file='/path/to/checkpoint'", 
    "ckpt_dir_or_file='/another/path/to/checkpoint'",
    # Scenarios with erroneous or inappropriate values
    "ckpt_dir_or_file='invalid'", 
    "ckpt_dir_or_file=None"
]

tf_train_load_checkpoint_Mutation_List = [
    # Typical parameter combinations
    "ckpt_dir_or_file='/path/to/checkpoint'", 
    "ckpt_dir_or_file='/another/path/to/checkpoint'",
    # Scenarios with erroneous or inappropriate values
    "ckpt_dir_or_file='invalid'", 
    "ckpt_dir_or_file=None"
]

tf_train_load_variable_Mutation_List = [
    # Typical parameter combinations
    "ckpt_dir_or_file='/path/to/checkpoint', name='variable_name'", 
    "ckpt_dir_or_file='/another/path/to/checkpoint', name='another_variable_name'",
    # Scenarios with erroneous or inappropriate values
    "ckpt_dir_or_file='invalid', name='invalid'", 
    "ckpt_dir_or_file=None, name=None"
]

tf_hyper_parameters_mutation_code_list = [
'layers.AbstractRNNCell()',
'layers.Activation()',
'layers.ActivityRegularization()',
'layers.Add()',
'layers.AdditiveAttention()',
'layers.AlphaDropout()',
'layers.Attention()',
'tlayers.Average()',
'layers.AveragePooling1D()',
'layers.AveragePooling2D()',
'layers.AveragePooling3D()',    
'layers.AvgPool1D()',
'layers.AvgPool2D()',
'layers.AvgPool3D()',
'layers.BatchNormalization()',
'layers.Bidirectional()',
'layers.CategoryEncoding()',
'layers.CenterCrop()',
'layers.Concatenate()',
'layers.Conv1D()',
'layers.Conv1DTranspose()',
'layers.Conv2D()',
'layers.Conv2DTranspose()',
'layers.Conv3D()',
'layers.Conv3DTranspose()',
'layers.ConvLSTM1D()',
'layers.ConvLSTM2D()',
'layers.ConvLSTM3D()',
'layers.Convolution1D()',
'layers.Convolution1DTranspose()',
'layers.Convolution2D()',
'layers.Convolution2DTranspose()',
'layers.Convolution3D()',
'layers.Convolution3DTranspose()',
'layers.Cropping1D()',
'layers.Cropping2D()',
'layers.Cropping3D()',
'tf.keras.layers.Dense()',
'layers.SpectralNormalization()',
'layers.StackedRNNCells()',
'layers.StringLookup()',
'layers.Subtract()',
'layers.TextVectorization()',
'layers.ThresholdedReLU()',
'layers.TimeDistributed()',
'layers.UnitNormalization()',
'layers.UpSampling1D()',
'layers.UpSampling2D()',
'layers.UpSampling3D()',
'layers.Wrapper()',
'layers.ZeroPadding1D()',
'layers.ZeroPadding2D()',
'layers.ZeroPadding3D()',
'layers.add()',
'layers.average()',
'layers.concatenate()',
'layers.deserialize()',
'layers.dot()',
'layers.maximum()',
'layers.minimum()',
'layers.multiply()',
'layers.serialize()',
'layers.subtract()',
'activations.deserialize()',
'activations.elu()',
'activations.exponential()',
'activations.gelu()',
'activations.get()',
'activations.hard_sigmoid()',
'activations.linear()',
'activations.mish()',
'activations.relu()',
'activations.selu()',
'activations.serialize()',
'activations.sigmoid()',
'activations.softmax()',
'activations.softplus()',
'activations.softsign()',
'activations.swish()',
'activations.tanh()',
'losses.BinaryCrossentropy()',
'losses.BinaryFocalCrossentropy()',
'losses.CategoricalCrossentropy()',
'losses.CategoricalFocalCrossentropy()',
'losses.CategoricalHinge()',
'losses.CosineSimilarity()',
'losses.Hinge()',
'losses.Huber()',
'losses.KLD()',
'losses.KLDivergence()',
'losses.LogCosh()',
'losses.Loss()',
'losses.MAE()',
'losses.MAPE()',
'losses.MSE()',
'losses.MSLE()',
'losses.MeanAbsoluteError()',
'losses.MeanAbsolutePercentageError()',
'losses.MeanSquaredError()',
'losses.MeanSquaredLogarithmicError()',
'losses.Poisson()',
'losses.Reduction()',
'losses.SparseCategoricalCrossentropy()',
'losses.SquaredHinge()',
'losses.binary_crossentropy()',
'losses.binary_focal_crossentropy()',
'losses.categorical_crossentropy()',
'losses.categorical_focal_crossentropy()',
'losses.categorical_hinge()',
'losses.cosine_similarity()',
'losses.deserialize()',
'losses.get()',
'losses.hinge()',
'losses.huber()',
'losses.kl_divergence()',
'losses.kld()',
'losses.kullback_leibler_divergence()',
'losses.log_cosh()',
'losses.logcosh()',
'losses.mae()',
'losses.mape()',
'losses.mean_absolute_error()',
'losses.mean_absolute_percentage_error()',
'losses.mean_squared_error()',
'losses.mean_squared_logarithmic_error()',
'losses.mse()',
'losses.msle()',
'losses.poisson()',
'losses.serialize()',
'losses.sparse_categorical_crossentropy()',
'losses.squared_hinge()',
'optimizers.Adadelta()',
'optimizers.Adafactor()',
'optimizers.Adagrad()',
'optimizers.Adam()',
'optimizers.Adamax()',
'optimizers.Ftrl()',
'optimizers.Nadam()',
'optimizers.RMSprop()',
'optimizers.SGD()',
'optimizers.deserialize()',
'optimizers.get()',
'optimizers.legacy.Adadelta()',
'optimizers.legacy.Adagrad()',
'optimizers.legacy.Adam()',
'optimizers.legacy.Adamax()',
'optimizers.legacy.Ftrl()',
'optimizers.legacy.Nadam()',
'optimizers.legacy.RMSprop()',
'optimizers.legacy.SGD()',
'optimizers.schedules.CosineDecay()',
'optimizers.schedules.ExponentialDecay()',
'optimizers.schedules.PolynomialDecay()',
'optimizers.schedules.deserialize()',
'optimizers.schedules.serialize()',
'nn.RNNCellDeviceWrapper',
'nn.RNNCellDropoutWrapper',
'nn.RNNCellResidualWrapper',
'nn.all_candidate_sampler',
'nn.approx_max_k',
'nn.approx_min_k',
'nn.atrous_conv2d',
'nn.atrous_conv2d_transpose',
'nn.avg_pool',
'nn.avg_pool1d',
'nn.avg_pool2d',
'nn.avg_pool3d',
'nn.batch_norm_with_global_normalization',
'nn.batch_normalization',
'nn.bias_add',
'nn.collapse_repeated',
'nn.compute_accidental_hits',
'nn.compute_average_loss',
'nn.conv1d',
'nn.conv1d_transpose',
'nn.conv2d',
'nn.conv2d_transpose',
'nn.conv3d',
'nn.conv3d_transpose',
'nn.conv_transpose',
'nn.convolution',
'nn.crelu',
'nn.ctc_beam_search_decoder',
'nn.ctc_greedy_decoder',
'nn.ctc_loss',
'nn.ctc_unique_labels',
'nn.depth_to_space',
'nn.depthwise_conv2d',
'nn.depthwise_conv2d_backprop_filter',
'nn.depthwise_conv2d_backprop_input',
'nn.dilation2d',
'nn.dropout',
'nn.elu',
'nn.embedding_lookup',
'nn.embedding_lookup_sparse',
'nn.erosion2d',
'nn.fixed_unigram_candidate_sampler',
'nn.fractional_avg_pool',
'nn.fractional_max_pool',
'nn.gelu',
'nn.in_top_k',
'nn.isotonic_regression',
'nn.l2_loss',
'nn.l2_normalize',
'nn.leaky_relu',
'nn.learned_unigram_candidate_sampler',
'nn.local_response_normalization',
'nn.log_poisson_loss',
'nn.log_softmax',
'nn.lrn',
'nn.max_pool',
'nn.max_pool1d',
'nn.max_pool2d',
'nn.max_pool3d',
'nn.max_pool_with_argmax',
'nn.moments',
'nn.nce_loss',
'nn.normalize_moments',
'nn.pool',
'nn.relu',
'nn.relu6',
'nn.safe_embedding_lookup_sparse',
'nn.sampled_softmax_loss',
'nn.scale_regularization_loss',
'nn.selu',
'nn.separable_conv2d',
'nn.sigmoid',
'nn.sigmoid_cross_entropy_with_logits',
'nn.silu',
'nn.softmax',
'nn.softmax_cross_entropy_with_logits',
'nn.softplus',
'nn.softsign',
'nn.space_to_batch',
'nn.space_to_depth',
'nn.sparse_softmax_cross_entropy_with_logits',
'nn.sufficient_statistics',
'nn.swish',
'nn.tanh',
'nn.top_k',
'nn.weighted_cross_entropy_with_logits',
'nn.weighted_moments',
'nn.with_space_to_batch',
'nn.zero_fraction',
'raw_ops.BlockLSTM',
'raw_ops.BlockLSTMGrad',
'raw_ops.BlockLSTMGradV2',
'raw_ops.BlockLSTMV2',
'raw_ops.BoostedTreesTrainingPredict',
'raw_ops.CSRSparseMatrixToDense',
'raw_ops.CTCLoss',
'raw_ops.CTCLossV2',
'raw_ops.Conv',
'raw_ops.Conv2D',
'raw_ops.Conv2DBackpropFilter',
'raw_ops.Conv2DBackpropFilterV2',
'raw_ops.Conv2DBackpropInput',
'raw_ops.Conv2DBackpropInputV2',
'raw_ops.Conv3D',
'raw_ops.Conv3DBackpropFilter',
'raw_ops.Conv3DBackpropFilterV2',
'raw_ops.Conv3DBackpropInput',
'raw_ops.Conv3DBackpropInputV2',
'raw_ops.CudnnRNN',
'raw_ops.CudnnRNNBackprop',
'raw_ops.CudnnRNNBackpropV2',
'raw_ops.CudnnRNNBackpropV3',
'raw_ops.CudnnRNNCanonicalToParams',
'raw_ops.CudnnRNNCanonicalToParamsV2',
'raw_ops.CudnnRNNParamsSize',
'raw_ops.CudnnRNNParamsToCanonical',
'raw_ops.CudnnRNNParamsToCanonicalV2',
'raw_ops.CudnnRNNV2',
'raw_ops.CudnnRNNV3',
'raw_ops.DenseBincount',
'raw_ops.DenseCountSparseOutput',
'raw_ops.DenseToCSRSparseMatrix',
'raw_ops.DenseToDenseSetOperation',
'raw_ops.DenseToSparseBatchDataset',
'raw_ops.DenseToSparseSetOperation',
'raw_ops.DepthwiseConv2dNative',
'raw_ops.DepthwiseConv2dNativeBackpropFilter',
'raw_ops.DepthwiseConv2dNativeBackpropInput',
'raw_ops.FusedPadConv2D',
'raw_ops.FusedResizeAndPadConv2D',
'raw_ops.GRUBlockCell',
'raw_ops.GRUBlockCellGrad',
'raw_ops.L2Loss',
'raw_ops.LSTMBlockCell',
'raw_ops.LSTMBlockCellGrad',
'raw_ops.QuantizedConv2D',
'raw_ops.QuantizedConv2DAndRelu',
'raw_ops.QuantizedConv2DAndReluAndRequantize',
'raw_ops.QuantizedConv2DAndRequantize',
'raw_ops.QuantizedConv2DPerChannel',
'raw_ops.QuantizedConv2DWithBias',
'raw_ops.QuantizedConv2DWithBiasAndRelu',
'raw_ops.QuantizedConv2DWithBiasAndReluAndRequantize',
'raw_ops.QuantizedConv2DWithBiasAndRequantize',
'raw_ops.QuantizedConv2DWithBiasSignedSumAndReluAndRequantize',
'raw_ops.QuantizedConv2DWithBiasSumAndRelu',
'raw_ops.QuantizedConv2DWithBiasSumAndReluAndRequantize',
'raw_ops.QuantizedDepthwiseConv2D',
'raw_ops.QuantizedDepthwiseConv2DWithBias',
'raw_ops.QuantizedDepthwiseConv2DWithBiasAndRelu',
'raw_ops.QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize',
'raw_ops.RecvTPUEmbeddingActivations',
'raw_ops.SdcaOptimizer',
'raw_ops.SdcaOptimizerV2',
'raw_ops.SparseDenseCwiseAdd',
'raw_ops.SparseDenseCwiseDiv',
'raw_ops.SparseDenseCwiseMul',
'raw_ops.SparseTensorDenseAdd',
'raw_ops.SparseTensorDenseMatMul',
'raw_ops.SparseToDense',
'raw_ops.TPUEmbeddingActivations',
'raw_ops.UniformQuantizedConvolution',
'raw_ops.UniformQuantizedConvolutionHybrid',
'train.BytesList',
'train.Checkpoint',
'train.CheckpointManager',
'train.CheckpointOptions',
'train.CheckpointView',
'train.ClusterDef',
'train.ClusterSpec',
'train.Coordinator',
'train.Example',
'train.ExponentialMovingAverage',
'train.Feature',
'train.FeatureList',
'train.FeatureLists',
'train.Features',
'train.FloatList',
'train.Int64List',
'train.JobDef',
'train.SequenceExample',
'train.ServerDef',
'train.TrackableView',
'train.checkpoints_iterator',
'train.experimental',
'train.experimental.PythonState',
'train.get_checkpoint_state',
'train.latest_checkpoint',
'train.list_variables',
'train.load_checkpoint',
'train.load_variable',
]

tf_bias_initializer_list = [
    "",  # Empty
    "bias_initializer='zeros'", 
    "bias_initializer='ones'",
    "bias_initializer='constant'", 
    "bias_initializer='random_normal'",
    "bias_initializer='random_uniform'",
    "bias_initializer='truncated_normal'",
    "bias_initializer='glorot_normal'",
    "bias_initializer='glorot_uniform'",
    "bias_initializer='he_normal'",
    "bias_initializer='he_uniform'",
    "bias_initializer='lecun_normal'",
    "bias_initializer='lecun_uniform'",
    "bias_initializer=None",  # Erroneous or edge case
    "bias_initializer='invalid'"  # Erroneous or edge case
]
tf_strides_list = [
    "",  # Empty
    "strides=1", 
    "strides=2", 
    "strides=(1, 1)",
    "strides=(2, 2)", 
    "strides=(1, 2)",
    "strides=(2, 1)",
    "strides=(3, 3)",
    "strides=(2, 2, 2)",
    "strides=(1, 2, 3)",
    "strides=(1,)",  # For 1D convolutions
    "strides=-1",  # Erroneous or edge case
    "strides='invalid'",  # Erroneous or edge case
    "strides=None"  # Erroneous or edge case
]
tf_padding_list = [
    "",  # Empty
    "padding='valid'", 
    "padding='same'",
    "padding='causal'",  # Specific to certain layer types like Conv1D
    "padding=[[0, 0], [1, 1]]",  # Custom padding
    "padding=[[1, 1], [2, 2]]",  # Custom padding
    "padding='full'",  # Not standard in TF but used in some contexts
    "padding=None",  # Erroneous or edge case
    "padding='invalid'"  # Erroneous or edge case
]
tf_data_format_list = [
    "",  # Empty
    "data_format='channels_last'", 
    "data_format='channels_first'", 
    "data_format='NHWC'", 
    "data_format='NCHW'", 
    "data_format=None",  # Erroneous or edge case
    "data_format='invalid'"  # Erroneous or edge case
]

tf_dilation_rate_list = [
    "",  # Empty
    "dilation_rate=1", 
    "dilation_rate=2", 
    "dilation_rate=(1, 1)",
    "dilation_rate=(2, 2)", 
    "dilation_rate=(1, 2)",
    "dilation_rate=(2, 1)",
    "dilation_rate=(3, 3)",
    "dilation_rate=(2, 2, 2)",
    "dilation_rate=(1, 2, 3)",
    "dilation_rate=(1,)",  # For 1D convolutions
    "dilation_rate=-1",  # Erroneous or edge case
    "dilation_rate='invalid'",  # Erroneous or edge case
    "dilation_rate=None"  # Erroneous or edge case
]
tf_groups_list = [
    "",  # Empty
    "groups=1",  # Default, no grouping
    "groups=2",  # Splitting into 2 groups
    "groups=4",  # Splitting into 4 groups
    "groups=8",  # Splitting into 8 groups
    "groups=-1",  # Erroneous or edge case
    "groups='invalid'",  # Erroneous or edge case
    "groups=None"  # Erroneous or edge case
]
tf_seed_list = [
    "",  # Empty
    "seed=42",  # Common seed value
    "seed=0",   # Another common seed value
    "seed=123", # Another common seed value
    "seed=2024",# Current year as seed
    "seed=-1",  # Erroneous or edge case
    "seed='invalid'",  # Erroneous or edge case
    "seed=None" # None is often valid, but listed here as a potential edge case
]
tf_axis_list = [
    # Existing Mutations
    "", "axis=0", "axis=1", "axis=-1", "axis=2", "axis=[0, 1]", "axis='invalid'", "axis=None",

    # Additional Mutations
    "axis=3",  # 3rd axis (for 3D+ tensors)
    "axis=-2",  # Second to last axis
    "axis=-3",  # Third to last axis
    "axis=[0, -1]",  # Combination of first and last axis
    "axis=[1, 2]",  # Combination of middle axes (for 3D+ tensors)
    "axis=[-2, -1]",  # Combination of last two axes
    "axis='all'",  # Invalid string axis
    "axis=1.5",  # Non-integer axis
    "axis=[0, 1, 2]",  # Multiple axes for 3D+ data
    "axis=[0, '1']",  # Mixed type axis
    "axis=[0, 1, -1]",  # Redundant axis specification
    "axis=[1, 1]",  # Duplicate axis
    "axis=range(2)",  # Axis as a range object
    "axis=np.array([0, 1])",  # Axis as a numpy array
    "axis=()",  # Empty tuple
    "axis=(0,)",  # Single element tuple
    "axis=(0, 1)",  # Tuple of axes
    "axis=(1, 'invalid')",  # Tuple with invalid entry
    "axis='axis=1'",  # String that looks like a parameter assignment
    "axis=4",  # Axis out of bounds for most 3D data
    "axis=-5",  # Negative axis out of common range
    "axis=100",  # Large positive axis
    "axis=-100",  # Large negative axis
    "axis=' '",  # Axis as a space character
    "axis=[0, None]",  # Mixed None with integer
    "axis=['0', 1]"  # Mixed string with integer
]
tf_from_logits_list = [
    "",  # Empty
    "from_logits=True",  # Explicitly state that inputs are raw logits
    "from_logits=False", # Explicitly state that inputs are probabilities
    "from_logits='invalid'",  # Erroneous or edge case
    "from_logits=None"  # None can be valid, but included here as an edge case
]
tf_label_smoothing_list = [
    "",  # Empty
    "label_smoothing=0.0",  # No label smoothing
    "label_smoothing=0.1",  # Slight label smoothing
    "label_smoothing=0.2",  # Moderate label smoothing
    "label_smoothing=-0.1",  # Erroneous or edge case (negative value)
    "label_smoothing='invalid'",  # Erroneous or edge case (non-numeric)
    "label_smoothing=None"  # None can be valid, but included here as an edge case
]
tf_use_cudnn_on_gpu_list = [
    "",  # Empty
    "use_cudnn_on_gpu=True",  # Use CuDNN on GPU if available
    "use_cudnn_on_gpu=False", # Do not use CuDNN on GPU
    "use_cudnn_on_gpu='invalid'",  # Erroneous or edge case
    "use_cudnn_on_gpu=None"  # None can be valid, but included here as an edge case
]
tf_ksize_list = [
    "",  # Empty
    "ksize=1", 
    "ksize=2",
    "ksize=3",
    "ksize=[1, 1]", 
    "ksize=[2, 2]",
    "ksize=[3, 3]", 
    "ksize='invalid'",  # Erroneous or edge case
    "ksize=None"  # None can be valid, but included here as an edge case
]
tf_keep_prob_list = [
    "",  # Empty
    "keep_prob=1.0",  # No dropout
    "keep_prob=0.8",  # Moderate dropout
    "keep_prob=0.5",  # High dropout
    "keep_prob=-1",  # Erroneous or edge case (negative value)
    "keep_prob=1.1",  # Erroneous or edge case (value greater than 1)
    "keep_prob='invalid'",  # Erroneous or edge case (non-numeric)
    "keep_prob=None"  # None can be valid, but included here as an edge case
]
tf_rate_list = [
    "",  # Empty
    "rate=0.0",  # No rate, or equivalent to 'keep_prob=1.0'
    "rate=0.2",  # Moderate rate
    "rate=0.5",  # High rate
    "rate=-0.1",  # Erroneous or edge case (negative value)
    "rate=1.1",  # Erroneous or edge case (value greater than 1)
    "rate='invalid'",  # Erroneous or edge case (non-numeric)
    "rate=None"  # None can be valid, but included here as an edge case
]
tf_training_list = [
    "",  # Empty
    "training=True",  # Model is in training mode
    "training=False", # Model is in inference mode
    "training='invalid'",  # Erroneous or edge case
    "training=None"  # None can be valid, but included here as an edge case
]
tf_momentum_list = [
    "",  # Empty
    "momentum=0.9",   # Commonly used momentum value
    "momentum=0.99",  # High momentum
    "momentum=0.5",   # Lower momentum
    "momentum=0.1",   # Very low momentum
    "momentum=-0.1",  # Erroneous or edge case (negative value)
    "momentum=1.1",   # Erroneous or edge case (value greater than 1)
    "momentum='invalid'",  # Erroneous or edge case (non-numeric)
    "momentum=None"   # None can be valid, but included here as an edge case
]
tf_center_list = [
    "",  # Empty
    "center=True",  # Include center parameter
    "center=False", # Exclude center parameter
    "center='invalid'",  # Erroneous or edge case
    "center=None"   # None can be valid, but included here as an edge case
]
tf_scale_list = [
    "",  # Empty
    "scale=True",  # Include scale parameter
    "scale=False", # Exclude scale parameter
    "scale='invalid'",  # Erroneous or edge case
    "scale=None"   # None can be valid, but included here as an edge case
]
tf_beta_initializer_list = [
    "",  # Empty
    "beta_initializer='zeros'", 
    "beta_initializer='ones'",
    "beta_initializer='random_normal'", 
    "beta_initializer='random_uniform'",
    "beta_initializer='glorot_normal'", 
    "beta_initializer='glorot_uniform'", 
    "beta_initializer='he_normal'", 
    "beta_initializer='he_uniform'",
    "beta_initializer=None",  # Erroneous or edge case
    "beta_initializer='invalid'"  # Erroneous or edge case
]
tf_gamma_initializer_list = [
    "",  # Empty
    "gamma_initializer='zeros'", 
    "gamma_initializer='ones'",
    "gamma_initializer='random_normal'", 
    "gamma_initializer='random_uniform'",
    "gamma_initializer='glorot_normal'", 
    "gamma_initializer='glorot_uniform'", 
    "gamma_initializer='he_normal'", 
    "gamma_initializer='he_uniform'",
    "gamma_initializer=None",  # Erroneous or edge case
    "gamma_initializer='invalid'"  # Erroneous or edge case
]
tf_moving_mean_initializer_list = [
    "",  # Empty
    "moving_mean_initializer='zeros'", 
    "moving_mean_initializer='ones'",
    "moving_mean_initializer='random_normal'", 
    "moving_mean_initializer='random_uniform'",
    "moving_mean_initializer='glorot_normal'", 
    "moving_mean_initializer='glorot_uniform'", 
    "moving_mean_initializer='he_normal'", 
    "moving_mean_initializer='he_uniform'",
    "moving_mean_initializer=None",  # Erroneous or edge case
    "moving_mean_initializer='invalid'"  # Erroneous or edge case
]
tf_moving_variance_initializer_list = [
    "",  # Empty
    "moving_variance_initializer='zeros'", 
    "moving_variance_initializer='ones'",
    "moving_variance_initializer='random_normal'", 
    "moving_variance_initializer='random_uniform'",
    "moving_variance_initializer='glorot_normal'", 
    "moving_variance_initializer='glorot_uniform'", 
    "moving_variance_initializer='he_normal'", 
    "moving_variance_initializer='he_uniform'",
    "moving_variance_initializer=None",  # Erroneous or edge case
    "moving_variance_initializer='invalid'"  # Erroneous or edge case
]
tf_depth_radius_list = [
    "",  # Empty
    "depth_radius=2", 
    "depth_radius=3", 
    "depth_radius=5", 
    "depth_radius=1", 
    "depth_radius=0",  # Erroneous or edge case
    "depth_radius=-1",  # Erroneous or edge case
    "depth_radius='invalid'",  # Erroneous or edge case
    "depth_radius=None"  # Erroneous or edge case
]
tf_bias_list = [
    "",  # Empty
    "bias=0.1", 
    "bias=0.2", 
    "bias=0.3", 
    "bias=0.0", 
    "bias=-0.1",  # Erroneous or edge case
    "bias='invalid'",  # Erroneous or edge case
    "bias=None"  # Erroneous or edge case
]
"""tf_alpha_list = [
    "",  # Empty
    "alpha=0.1", 
    "alpha=0.2", 
    "alpha=0.3", 
    "alpha=0.0", 
    "alpha=-0.1",  # Erroneous or edge case
    "alpha='invalid'",  # Erroneous or edge case
    "alpha=None"  # Erroneous or edge case
]"""""
tf_alpha_list = [
    "",               # Empty
    "alpha=0.1",      # Common alpha value
    "alpha=0.2",      # Common alpha value
    "alpha=0.3",      # Common alpha value
    "alpha=0.0",      # No alpha, common case
    "alpha=-0.1",     # Erroneous or edge case (negative value)
    "alpha='invalid'",# Erroneous or edge case (non-numeric)
    "alpha=None",     # Erroneous or edge case
    "alpha=0.4",      # Common alpha value
    "alpha=0.5",      # Common alpha value
    "alpha=0.6",      # Common alpha value
    "alpha=0.7",      # Common alpha value
    "alpha=0.8",      # Common alpha value
    "alpha=0.9",      # Common alpha value
    "alpha=1.0",      # Maximum alpha
    "alpha=1.5",      # Edge case
    "alpha=2.0",      # Edge case
    "alpha=5.0",      # Edge case
    "alpha=10.0",     # Edge case
    "alpha=100.0",    # Edge case
    "alpha=0.01",     # Small alpha
    "alpha=0.001",    # Very small alpha
    "alpha=0.0001",   # Extremely small alpha
    "alpha=0.00001",  # Extra small alpha
    "alpha=0.000001", # Extra small alpha
    "alpha=0.0000001",# Extra small alpha
    "alpha=0.00000001", # Extra small alpha
    "alpha=0.000000001",# Extra small alpha
    "alpha=0.0000000001",# Extra small alpha
]
tf_l1_list = [
    "",  # Empty
    "l1=0.01",  # Common L1 regularization value
    "l1=0.001", # Another common L1 regularization value
    "l1=0.1",   # Higher L1 regularization value
    "l1=0.0001",# Lower L1 regularization value
    "l1=-0.01", # Erroneous or edge case (negative value)
    "l1='invalid'", # Erroneous or edge case (non-numeric)
    "l1=None"  # None can be valid, but included here as an edge case
]
tf_l2_list = [
    "",  # Empty
    "l2=0.01",  # Common L2 regularization value
    "l2=0.001", # Another common L2 regularization value
    "l2=0.1",   # Higher L2 regularization value
    "l2=0.0001",# Lower L2 regularization value
    "l2=-0.01", # Erroneous or edge case (negative value)
    "l2='invalid'", # Erroneous or edge case (non-numeric)
    "l2=None"  # None can be valid, but included here as an edge case
]

tf_trainable_list = [
    "",  # Empty
    "trainable=True",  # Parameter is trainable
    "trainable=False", # Parameter is not trainable
    "trainable='invalid'", # Erroneous or edge case (non-boolean)
    "trainable=None"  # None can be valid, but included here as an edge case
]
tf_beta1_list = [
    "",  # Empty
    "beta1=0.9",  # Common value for beta1 in optimizers like Adam
    "beta1=0.99", # Another common value for beta1
    "beta1=0.5",  # Lower value for beta1
    "beta1=-0.1", # Erroneous or edge case (negative value)
    "beta1=1.1",  # Erroneous or edge case (value greater than 1)
    "beta1='invalid'", # Erroneous or edge case (non-numeric)
    "beta1=None"  # None can be valid, but included here as an edge case
]
tf_beta2_list = [
    "",  # Empty
    "beta2=0.999", # Common value for beta2 in optimizers like Adam
    "beta2=0.99",  # Another common value for beta2
    "beta2=0.9",   # Lower value for beta2
    "beta2=-0.1",  # Erroneous or edge case (negative value)
    "beta2=1.1",   # Erroneous or edge case (value greater than 1)
    "beta2='invalid'", # Erroneous or edge case (non-numeric)
    "beta2=None"  # None can be valid, but included here as an edge case
]

tf_epsilon_list = [
    "",                 # Boş
    "epsilon=1e-7",     # Sık kullanılan epsilon değeri
    "epsilon=1e-9",     # Sık kullanılan epsilon değeri
    "epsilon=0.1",      # Daha az hassasiyet için büyük epsilon
    "epsilon=1e-10",    # Çok küçük epsilon
    "epsilon=-1e-7",    # Hatalı veya sınır durumu (negatif değer)
    "epsilon='error'",# Hatalı veya sınır durumu (sayısal olmayan)
    "epsilon=None",     # None bazen geçerli olabilir, ancak buraya bir sınır durumu olarak dahil edilmiştir
    "epsilon=1e-6",     # Sık kullanılan epsilon değeri
    "epsilon=1e-8",     # Sık kullanılan epsilon değeri
    "epsilon=0.01",     # Daha az hassasiyet için büyük epsilon
    "epsilon=1e-11",    # Çok küçük epsilon
    "epsilon=-1e-8",    # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-5",     # Sık kullanılan epsilon değeri
    "epsilon=1e-12",    # Çok küçük epsilon
    "epsilon=0.001",    # Daha az hassasiyet için büyük epsilon
    "epsilon=-1e-9",    # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-13",    # Çok küçük epsilon
    "epsilon=1e-4",     # Sık kullanılan epsilon değeri
    "epsilon=1e-14",    # Çok küçük epsilon
    "epsilon=0.0001",   # Daha az hassasiyet için büyük epsilon
    "epsilon=-1e-10",   # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-15",    # Çok küçük epsilon
    "epsilon=1e-16",    # Çok küçük epsilon
    "epsilon=1e-3",     # Daha az hassasiyet için büyük epsilon
    "epsilon=-1e-11",   # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-2",     # Daha az hassasiyet için büyük epsilon
    "epsilon=-1e-12",   # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-1",     # Daha az hassasiyet için büyük epsilon
    "epsilon=-1e-13",   # Hatalı veya sınır durumu (negatif değer)
    "epsilon=1e-17",    # Çok küçük epsilon
    "epsilon=1e-18",    # Çok küçük epsilon
    "epsilon=1e-19",    # Çok küçük epsilon
    "epsilon=1e-20",    # Çok küçük epsilon
    "epsilon=1e-21",    # Çok küçük epsilon
    "epsilon=1e-22",    # Çok küçük epsilon
    "epsilon=1.0",      # Daha az hassasiyet için büyük epsilon
    "epsilon=10.0",     # Daha az hassasiyet için büyük epsilon
    "epsilon=100.0",    # Daha az hassasiyet için büyük epsilon
    "epsilon=1000.0",   # Daha az hassasiyet için büyük epsilon
]

tf_gamma_list = [
    "",                 # Boş
    "gamma=0.99",       # Yaygın olarak kullanılan bir değer
    "gamma=0.9",        # Yaygın olarak kullanılan bir değer
    "gamma=0.95",       # Yaygın olarak kullanılan bir değer
    "gamma=0.98",       # Yaygın olarak kullanılan bir değer
    "gamma=0.85",       # Yaygın olarak kullanılan bir değer
    "gamma=0.8",        # Yaygın olarak kullanılan bir değer
    "gamma=0.7",        # Yaygın olarak kullanılan bir değer
    "gamma=0.6",        # Yaygın olarak kullanılan bir değer
    "gamma=0.5",        # Yaygın olarak kullanılan bir değer
    "gamma=0.4",        # Yaygın olarak kullanılan bir değer
    "gamma=0.3",        # Yaygın olarak kullanılan bir değer
    "gamma=0.2",        # Yaygın olarak kullanılan bir değer
    "gamma=0.1",        # Yaygın olarak kullanılan bir değer
    "gamma=0.01",       # Yaygın olarak kullanılan bir değer
    "gamma=0.001",      # Yaygın olarak kullanılan bir değer
    "gamma=0.0001",     # Yaygın olarak kullanılan bir değer
    "gamma=0.00001",    # Yaygın olarak kullanılan bir değer
    "gamma=0.000001",   # Yaygın olarak kullanılan bir değer
    "gamma=1.0",        # Yaygın olarak kullanılan bir değer
    "gamma=10.0",       # Büyük bir değer
    "gamma=100.0",      # Büyük bir değer
    "gamma=1000.0",     # Büyük bir değer
    "gamma=10000.0",    # Büyük bir değer
    "gamma=100000.0",   # Büyük bir değer
    "gamma=1000000.0"   # Büyük bir değer
]
tf_decay_list = [
    "",              # Boş
    "decay=0.0",     # Hiçbir bozulma, birçok optimizerda yaygın olarak kullanılır
    "decay=0.1",     # Orta düzeyde bozulma
    "decay=0.05",    # Daha küçük bozulma
    "decay=0.01",    # Daha küçük bozulma
    "decay=0.005",   # Çok küçük bozulma
    "decay=0.001",   # Çok küçük bozulma
    "decay=0.0005",  # Çok çok küçük bozulma
    "decay=0.0001",  # Çok çok küçük bozulma
    "decay=1e-4",    # 1e-4 formatında çok küçük bozulma
    "decay=1e-5",    # 1e-5 formatında çok küçük bozulma
    "decay=1e-6",    # 1e-6 formatında çok küçük bozulma
    "decay=1e-7",    # 1e-7 formatında çok küçük bozulma
    "decay=1e-8",    # 1e-8 formatında çok küçük bozulma
    "decay=1e-9",    # 1e-9 formatında çok küçük bozulma
    "decay=1e-10",   # 1e-10 formatında çok küçük bozulma
    "decay=1e-11",   # 1e-11 formatında çok küçük bozulma
    "decay=1e-12",   # 1e-12 formatında çok küçük bozulma
    "decay=1e-13",   # 1e-13 formatında çok küçük bozulma
    "decay=1e-14",   # 1e-14 formatında çok küçük bozulma
    "decay=1e-15",   # 1e-15 formatında çok küçük bozulma
    "decay=-0.1",    # Yanlış veya sınır durum (negatif değer)
    "decay='invalid'", # Yanlış veya sınır durum (sayısal olmayan)
    "decay=None",    # None bazen geçerli olabilir, ancak burada bir sınır durumu olarak dahil edilmiştir
    "decay=0.3",     # Yüksek bir değer
    "decay=0.4",     # Yüksek bir değer
    "decay=0.5",     # Yüksek bir değer
    "decay=0.6",     # Yüksek bir değer
    "decay=0.9",     # Çok yüksek bir değer
    "decay=1.0",     # Maksimum değer
]

tf_global_step_list = [
    "",  # Empty
    "global_step=0",   # Initial step
    "global_step=100", # An example step
    "global_step=1000",# A larger step
    "global_step=5000",# A very large step
    "global_step=-1",  # Erroneous or edge case (negative value)
    "global_step='invalid'", # Erroneous or edge case (non-numeric)
    "global_step=None"  # None can be valid, but included here as an edge case
]
tf_decay_steps_list = [
    "",  # Empty
    "decay_steps=100",   # Common decay step
    "decay_steps=1000",  # A larger decay step
    "decay_steps=10000", # A very large decay step
    "decay_steps=10",    # A smaller decay step
    "decay_steps=-100",  # Erroneous or edge case (negative value)
    "decay_steps='invalid'", # Erroneous or edge case (non-numeric)
    "decay_steps=None"  # None can be valid, but included here as an edge case
]
tf_decay_rate_list = [
    "",  # Empty
    "decay_rate=0.1",  # Moderate decay rate
    "decay_rate=0.01", # Smaller decay rate
    "decay_rate=0.5",  # Larger decay rate
    "decay_rate=0.001",# Very small decay rate
    "decay_rate=-0.1", # Erroneous or edge case (negative value)
    "decay_rate='invalid'", # Erroneous or edge case (non-numeric)
    "decay_rate=None"  # None can be valid, but included here as an edge case
]
tf_capacity_list = [
    "",  # Empty
    "capacity=10",  # Small capacity
    "capacity=100", # Moderate capacity
    "capacity=1000",# Large capacity
    "capacity=10000",# Very large capacity
    "capacity=-1",  # Erroneous or edge case (negative value)
    "capacity='invalid'", # Erroneous or edge case (non-numeric)
    "capacity=None"  # None can be valid, but included here as an edge case
]

tf_max_to_keep_list = [
    "",  # Empty
    "max_to_keep=1",  # Keep only the latest one
    "max_to_keep=5",  # Keep last 5
    "max_to_keep=10", # Keep last 10
    "max_to_keep=-1", # Erroneous or edge case (negative value)
    "max_to_keep='invalid'", # Erroneous or edge case (non-numeric)
    "max_to_keep=None"  # None can be valid, but included here as an edge case
]
tf_maxlen_values = [
    "64",    # Commonly used for short sequences
    "128",   # Preferred for medium-length sequences
    "256",   # Used for longer sequences
    "512",   # For very long sequences or high resolution
    "1024",  # For extremely long sequences or detailed analysis
    "32",    # For very short sequences, often used in simple tasks
    "2048",  # For very long sequences in detailed analysis
    "4096",  # For extremely detailed and extensive sequences
    "8192",  # For very large-scale sequences, rarely used
    "16384"  # For experimental or very specific high-resolution tasks
]

tf_vocab_size_values = [
    "8000",   # Small vocabularies, often used in mobile applications
    "16000",  # Medium-sized vocabularies, suitable for many common NLP tasks
    "32000",  # Larger vocabularies, often used for complex models
    "50000",  # Very large vocabularies, used for extensive text corpora
    "64000",  # Extremely large vocabularies, for high precision and detailed analysis
    "10000",  # Commonly used for small to medium-sized vocabularies
    "20000",  # Preferred for slightly larger vocabularies
    "30000",  # Used for large vocabularies
    "75000",  # For very extensive text corpora
    "100000"  # For extremely large vocabularies or detailed analysis
]
