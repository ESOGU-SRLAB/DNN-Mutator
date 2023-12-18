


#tf.keras

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
'activation',
'epochs',
'model.add',
'optimizer',
'learning_rate',
'kernel_regularizer',
'batch_size',
'dropout',
'filters',
'kernel_size',
'strides',
'padding',
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
'tf.raw_ops.RecvTPUEmbeddingActivations()',
'tf.raw_ops.SdcaOptimizer()',
'tf.raw_ops.SdcaOptimizerV2()',
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
'tf.train.load_variable()'
]