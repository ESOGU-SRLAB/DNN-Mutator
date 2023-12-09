




tf_activation_functions = [
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

dense_units_list = [8, 16, 32, 64, 128, 256, 512, 1024]
dense_use_bias_list = [True, False]
dense_kernel_initializer_list = [
    'RandomNormal',           # Initializes weights with a normal distribution
    'RandomUniform',          # Initializes weights with a uniform distribution
    'TruncatedNormal',        # Initializes weights with a truncated normal distribution
    'Zeros',                  # Initializes weights to zero
    'Ones',                   # Initializes weights to one
    'GlorotNormal',           # Glorot/Xavier normal initializer
    'GlorotUniform',          # Glorot/Xavier uniform initializer
    'HeNormal',               # He normal initializer
    'HeUniform',              # He uniform initializer
    'Orthogonal',             # Initializes weights as orthogonal matrices
    'Constant',               # Initializes weights to a constant value
    'VarianceScaling'         # Initializes weights by scaling the variance based on fan-in or fan-out mode
]


tf_loss_functions = [
    'BinaryCrossentropy',                  # İkili sınıflandırma için çapraz entropi kaybı
    'BinaryFocalCrossentropy',             # İkili sınıflandırma için odaklanmış çapraz entropi kaybı
    'CategoricalCrossentropy',             # Çok sınıflı sınıflandırma için çapraz entropi kaybı
    'CategoricalFocalCrossentropy',        # Çok sınıflı sınıflandırma için odaklanmış çapraz entropi kaybı
    'CategoricalHinge',                    # Çok sınıflı sınıflandırma için menteşe kaybı
    'CosineSimilarity',                    # Kosinüs benzerliğine göre kayıp
    'Hinge',                               # Menteşe kaybı
    'Huber',                               # Huber kaybı, karesel ve mutlak hatalar arasında bir denge sağlar
    'KLD',                                 # Kullback-Leibler sapması
    'KLDivergence',                        # Kullback-Leibler sapması (KLD'nin başka bir ifadesi)
    'LogCosh',                             # Logaritmik hiperbolik kosinüs kaybı
    'Loss',                                # Genel kayıp sınıfı
    'MAE',                                 # Ortalama mutlak hata
    'MAPE',                                # Ortalama mutlak yüzde hata
    'MSE',                                 # Ortalama karesel hata
    'MSLE',                                # Ortalama karesel logaritmik hata
    'MeanAbsoluteError',                   # Ortalama mutlak hata (MAE'nin başka bir ifadesi)
    'MeanAbsolutePercentageError',         # Ortalama mutlak yüzde hata (MAPE'nin başka bir ifadesi)
    'MeanSquaredError',                    # Ortalama karesel hata (MSE'nin başka bir ifadesi)
    'MeanSquaredLogarithmicError',         # Ortalama karesel logaritmik hata (MSLE'nin başka bir ifadesi)
    'Poisson',                             # Poisson kaybı, özellikle sayım verileri için
    'Reduction',                           # Kayıp indirgeme türlerini belirlemek için kullanılır
    'SparseCategoricalCrossentropy',       # Etiketlerin tam sayı olarak verildiği çok sınıflı sınıflandırma için çapraz entropi kaybı
    'SquaredHinge',                        # Kare menteşe kaybı
    'binary_crossentropy',                 # İkili sınıflandırma için çapraz entropi kaybı (fonksiyon olarak)
    'binary_focal_crossentropy',           # İkili sınıflandırma için odaklanmış çapraz entropi kaybı (fonksiyon olarak)
    'categorical_crossentropy',            # Çok sınıflı sınıflandırma için çapraz entropi kaybı (fonksiyon olarak)
    'categorical_focal_crossentropy',      # Çok sınıflı sınıflandırma için odaklanmış çapraz entropi kaybı (fonksiyon olarak)
    'categorical_hinge',                   # Çok sınıflı sınıflandırma için menteşe kaybı (fonksiyon olarak)
    'cosine_similarity',                   # Kosinüs benzerliğine göre kayıp (fonksiyon olarak)
    'deserialize',                         # Kayıp fonksiyonlarını deserialize etmek için kullanılır
    'get',                                 # Kayıp fonksiyonunu almak için kullanılır
    'hinge',                               # Menteşe kaybı (fonksiyon olarak)
    'huber',                               # Huber kaybı (fonksiyon olarak)
    'kl_divergence',                       # Kullback-Leibler sapması (fonksiyon olarak)
    'kld',                                 # Kullback-Leibler sapması (kl_divergence'ın başka bir ifadesi)
    'kullback_leibler_divergence',         # Kullback-Leibler sapması (kl_divergence'ın başka bir ifadesi)
    'log_cosh',                            # Logaritmik hiperbolik kosinüs kaybı (fonksiyon olarak)
    'logcosh',                             # Logaritmik hiperbolik kosinüs kaybı (log_cosh'un başka bir ifadesi)
    'mae',                                 # Ortalama mutlak hata (fonksiyon olarak)
    'mape',                                # Ortalama mutlak yüzde hata (fonksiyon olarak)
    'mean_absolute_error',                 # Ortalama mutlak hata (fonksiyon olarak)
    'mean_absolute_percentage_error',      # Ortalama mutlak yüzde hata (fonksiyon olarak)
    'mean_squared_error',                  # Ortalama karesel hata (fonksiyon olarak)
    'mean_squared_logarithmic_error',      # Ortalama karesel logaritmik hata (fonksiyon olarak)
    'mse',                                 # Ortalama karesel hata (fonksiyon olarak)
    'msle',                                # Ortalama karesel logaritmik hata (fonksiyon olarak)
    'poisson',                             # Poisson kaybı (fonksiyon olarak)
    'serialize',                           # Kayıp fonksiyonlarını serialize etmek için kullanılır
    'sparse_categorical_crossentropy',     # Etiketlerin tam sayı olarak verildiği çok sınıflı sınıflandırma için çapraz entropi kaybı (fonksiyon olarak)
    'squared_hinge'                        # Kare menteşe kaybı (fonksiyon olarak)
]
