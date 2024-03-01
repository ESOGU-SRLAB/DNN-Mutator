import ast
import astunparse
import re
import random


global Counter
counter = 1

# AST Value Mutator
class ConstantMutator(ast.NodeTransformer):
    def __init__(self, target_keyword, new_value):
        self.target_keyword = target_keyword
        self.new_value = new_value

    def visit_Call(self, node):
        for keyword in node.keywords:
            if keyword.arg == self.target_keyword:
                keyword.value = ast.Str(s=self.new_value)
        return node,[]


def modify_code_in_file_epoch(source_code, target_keyword, new_value):
    
    code = source_code

    node = ast.parse(code)
    renamer = ConstantMutator(target_keyword, new_value)
    new_node = renamer.visit(node)
    new_code = astunparse.unparse(new_node)
# Eğer kod değiştirildiyse, yeni kodu "mutator_code.py" adıyla kaydet
    if code != new_code:
        with open("mutated_code.py", 'w') as output_file:
            output_file.write(new_code)
        #print(f"Modified code saved as 'mutator_code.py'")
    return new_value,[]

#-------------------------------------------------------------------------epoch

# AST Value Mutator---------activation
class ConstantMutatoractivation(ast.NodeTransformer):
    def __init__(self, target_keyword, new_value):
        self.target_keyword = target_keyword
        self.new_value = new_value

    def visit_keyword(self, node):
        if node.arg == self.target_keyword:
            if isinstance(node.value, ast.Str):
                node.value.s = self.new_value
        return node

#def replace_input_shape(source_code, new_shape):
    
    #input_shape_list=[]
    #pattern = r"input_shape=\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)"

    # Yeni değerle değiştir
    
   # matches = re.findall(pattern, source_code)
    #if matches:
        #input_shape_list = [f"{m}" for m in matches]
        
    #new_value = "input_shape="
    #if matches:
        #return new_value,input_shape_list
    
    #return 0,[]
import re

def replace_input_shape(source_code, new_shape):
    input_shape_list = []
    
    # Updated regex pattern
    # This pattern now correctly handles the optional trailing comma for a single dimension
    #pattern = r"input_shape=\(\s*(\d+\s*(\*\s*\d+\s*)?)(,)?(\s*\d+\s*,)?(\s*\d+\s*)?\)"
    pattern = r"input_shape=\(\s*((\w+[\w\.\[\]]*\s*(\*\s*\w+[\w\.\[\]]*\s*)?)(,)?(\s*\w+[\w\.\[\]]*\s*,)?(\s*\w+[\w\.\[\]]*\s*)?)\)"
    # Find matches
    matches = re.findall(pattern, source_code)
    if matches:
        # Construct the list of matched input_shape strings
        input_shape_list = [
            f"input_shape=({m[0]}{m[2]}{m[3]}{m[4]})" for m in matches
        ]
        
    # Here you can replace the found input shapes with new_shape if needed
    # For demonstration, just return the found shapes and the new_value placeholder
    new_value = "input_shape="  # Placeholder for new shape
    if matches:
        return new_value, input_shape_list
    
    return 0, []




def replace_pool_size_shape(source_code, new_shape):
    
    pool_size_list=[]
    pattern = r"pool_size\s*=\s*(\(\s*\d+\s*,\s*\d+\s*\)|\d+)"

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    print(matches,"pool_size")
    if matches:
        pool_size_list = [f"pool_size={m}" for m in matches]
        
    new_value = "pool_size="
    if matches:
        return new_value,pool_size_list
    
    return 0,[]

def replace_batch_size_in_code(source_code, new_shape):
    
    batch_size_list=[]
    pattern = r"batch_size\s*=\s*\d+"
    pattern_value = r"batch_size\s*=\s*(\d+)"
    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    matches_value = re.findall(pattern_value, source_code)
    print("Batch Size Value",matches_value)
    if matches:
        batch_size_list = [f"{m}" for m in matches]
        
    new_value = "batch_size="
    if matches:
        return new_value,batch_size_list
    
    return 0,[]

def replace_units_size_in_code(source_code, new_shape):
    
    units_list=[]
    pattern = r"units\s*=\s*\d+"
    pattern_value=r"units\s*=\s*(\d+)"
    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    matches_value = re.findall(pattern_value, source_code)
    if matches:
        units_list = [f"{m}" for m in matches]
        
    new_value = "units="
    if matches:
        return new_value,units_list
    
    return 0,[]

def replace_filters_in_code(source_code, new_shape):
    
    batch_size_list=[]
    pattern = r"filters\s*=\s*\d+"
    pattern_value = r"filters\s*=\s*(\d+)"
    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    matches_value = re.findall(pattern_value, source_code)
    print(matches,"Filters")
    if matches:
        batch_size_list = [f"{m}" for m in matches]
        
    new_value = "filters="
    if matches:
        return new_value,batch_size_list
    
    return 0,[]

def replace_optimizer_in_code(source_code, new_shape):
    
    optimizer_list=[]
    pattern = r"optimizer\s*=\s*'\w+'"

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    if matches:
        optimizer_list = [f"{m}" for m in matches]
        
    new_value = "optimizer="
    if matches:
        return new_value,optimizer_list
    
    return 0,[]

def replace_loss_in_code(source_code, new_shape):
    
    loss_list=[]
    pattern = r"loss\s*=\s*'\w+'"

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    if matches:
        loss_list = [f"{m}" for m in matches]
        
    new_value = "loss="
    if matches:
        return new_value,loss_list
    
    return 0,[]

def kernel_regularizer_in_code(source_code, new_shape):
    
    kernel_regularizer_list=[]
    pattern = r'kernel_regularizer=\w+\(\d*\.?\d+\)'

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    if matches:
        kernel_regularizer_list = [f"{m}" for m in matches]
        
    new_value = "loss="
    if matches:
        return new_value,kernel_regularizer_list
    
    return 0,[]

def replace_Dense_in_code(source_code, new_shape):
    
    Dense_list=[]
    pattern = r"Dense\s*\(\s*(\d+)\s*,"
              

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    if matches:
        Dense_list = [f"Dense({m}" for m in matches]
        
    new_value = "Dense("
    if matches:
        return new_value,Dense_list
    
    return new_value,[]

def replace_Dropout_in_code(source_code, new_shape):
    
    Dropout_list=[]
    pattern = r"Dropout\s*\(\s*(\d+\.\d+|\d+)\s*\)"
              

    # Yeni değerle değiştir
    
    matches = re.findall(pattern, source_code)
    if matches:
        Dropout_list = [f"Dropout({m})" for m in matches]
        
    new_value = "Dropout("
    if matches:
        return new_value,Dropout_list
    
    return new_value,[]

def modify_tf_dropout_in_code(source_code, new_dropout_value):
    dropout_list=[]
    # Regex deseni: 'dropout=...' formundaki ifadeleri bulur
    pattern = r"dropout\s*=\s*\d*\.?\d+"
    # Find matches using regex
    matches = re.findall(pattern, source_code)
    if matches:
        # Check if the source code has changed
        dropout_list = [f"{m}" for m in matches]
        #print(dropout_list)
    # Yeni değerle değiştir
    
    new_value = "dropout="
    if matches:
        return new_value,dropout_list
    return new_value,[]




def modify_tf_activation_in_code(source_code, layer_names, new_value):
    
    for layer_name in layer_names:
        temp_source = source_code
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        pattern = r"activation='[^']*'"
        activation_list=[]
        # Find matches using regex
        matches = re.findall(pattern, source_code)
        if matches:
            activation_list = [f"{m}" for m in matches]
            #print(activation_list)
        
        # Check if the source code has changed
        
        new_value = "activation="
        if matches:
                             
            return new_value, activation_list
            
    return 0, []


def modify_tf_use_bias_in_code(source_code,layer_names, new_use_bias_value):
    # Regex deseni: 'use_bias=' sonrası herhangi bir değeri bulur
    pattern = r"use_bias\s*=\s*[^,)]+"
    use_bias_list=[]
    matches = re.findall(pattern, source_code)
    new_value = "use_bias="
    if matches:
        use_bias_list = [f"{m}" for m in matches]
        #print(use_bias_list)
        return new_value,use_bias_list
    return 0, []
    

    




def modify_tf_learning_rate_in_code(source_code, layer_names, new_value):
    i=0
    for layer_name in layer_names:
        temp_source = source_code
        learning_rate_list=[]
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        pattern = r"(learning_rate\s*=\s*\d*\.?\d+)"
       
        # Find matches using regex
        matches = re.findall(pattern, source_code)
        new_value = "learning_rate="
        if matches:
            
            learning_rate_list = [f"{m}" for m in matches] 
            #print(learning_rate_list)               
            return new_value, learning_rate_list
            
    return 0, []

def modify_tf_epoch_in_code(source_code, layer_names, new_value):
    i=0
    for layer_name in layer_names:
        temp_source = source_code
        learning_rate_list=[]
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        pattern = r"(epoch\s*=\s*\d*\.?\d+)"
       
        # Find matches using regex
        matches = re.findall(pattern, source_code)
        new_value = "epoch="
        if matches:
            
            learning_rate_list = [f"epoch={m}" for m in matches] 
            #print(learning_rate_list)                  
            return new_value, learning_rate_list
            
    return 0, []


def replace_kernel_size_in_code(source_code,new_kernel_size):
  
    # Regex deseni: 'kernel_size=...' formundaki ifadeleri bulur
    # Hem tek sayı hem de parantez içindeki sayı çiftlerini kapsar
    pattern = r"kernel_size\s*=\s*(\(\s*\d+\s*,\s*\d+\s*(?:,\s*\d+\s*)?\)|\d+)"

    kernel_size_list=[]
    matches = re.findall(pattern, source_code)

    new_value = "kernel_size="
   
    if matches:
        kernel_size_list = [f"kernel_size={m}" for m in matches]  # List of original kernel_size values
        #print(kernel_size_list)
       
    if matches:
                           
            return new_value, kernel_size_list
    return 0,[]

def replace_kernel_initializer(source_code, new_initializer):
    # Regex deseni: 'kernel_initializer=...' formatındaki ifadeleri bulur
    # Boşlukları da kapsar
    kernel_initializer_layers_list=[]
    pattern = r"kernel_initializer\s*=\s*'[^']*'"

    matches = re.findall(pattern, source_code)
    new_value = "kernel_initializer="
    if matches:
            kernel_initializer_layers_list = [f"{m}" for m in matches]
            
    return new_value,kernel_initializer_layers_list

def modify_code_in_file_Conv2D(source_code, new_value):
    # Rastgele bir Conv2D çağrısı seçme
    pattern = r"layers\.Conv2D\(\d+, \(\d+, \d+\)"
    matches = re.finditer(pattern, source_code)
    matches_list = list(matches)

    if matches_list:
        # İlk eşleşmeyi al
        selected_match = matches_list[0]
        original_code = selected_match.group(0)
        new_code = new_value  # Yeni kodu belirle
        source_code = source_code.replace(original_code, new_code, 1)  # İlk eşleşmeyi değiştir
    return new_value,[]


def modify_tf_layer_in_code(source_code, layer_names,new_value):
 
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[^)]*\)"
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[\s\S]*?(\))"
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.keras\.layers\.{layer_names}\([^\)]*\)"
        temp_source=source_code

        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.layers.{layer_names}("
        matches = re.findall(pattern, source_code)
        if matches:
            kernel_layers_list = [f"{m}" for m in matches]
            #print(kernel_layers_list)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
            
            return new_value,kernel_layers_list
        return 0,[]

def modify_tf_losses_in_code(source_code, layer_names,new_value):
    global counter
    for layer_name in layer_names:
        #pattern = rf"(tf\.keras\.losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        #pattern = rf"(tf\.(keras\.)?losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.keras\.losses\.\b{layer_names}\([^\)]*\)"

        temp_source=source_code
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.losses.{layer_names}("
        matches = re.findall(pattern, source_code)
        if matches:
            use_losses_list = [f"{m}" for m in matches]
            #print(use_losses_list)
        
        
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
              
            return new_value,use_losses_list
        return 0,[]



def modify_tf_optimizers_in_code(source_code, layer_names,new_value):
    
    global counter
    for layer_name in layer_names:
        use_legacy_list=[]
        use_schedules_list=[]
        # 'legacy' ve 'schedules' ifadeleri için özel desenler
        
        pattern_legacy = rf"tf\.keras\.optimizers\.legacy\.{layer_names}\([^\)]*\)"
        
        pattern_schedules = rf"tf\.keras\.optimizers\.schedules\.{layer_names}\([^\)]*\)"
        temp_source=source_code
        if re.search(pattern_legacy, source_code):
            # 'legacy' için yeni değer
            new_value = f"tf.keras.optimizers.legacy.{layer_names}("
            matches = re.findall(pattern_legacy, source_code)
            if matches:
                use_legacy_list = [f"{m}" for m in matches]
                #print(use_legacy_list)
            source_code = re.sub(pattern_legacy, new_value, source_code)
            name="_optimizers_legacy"
        elif re.search(pattern_schedules, source_code):
            # 'schedules' için yeni değer
            new_value = f"tf.keras.optimizers.schedules.{layer_names}("
            matches = re.findall(pattern_schedules, source_code)
            if matches:           
                use_schedules_list = [f"{m}" for m in matches]
                #print(use_schedules_list)
            source_code = re.sub(pattern_schedules, new_value, source_code)
        #elif():
            #new_value = f"tf.keras.optimizers.{layer_names}()"
            name="_optimizers_schedules"
        if use_legacy_list:
            return new_value,use_legacy_list
        if use_schedules_list:
            return new_value,use_schedules_list
        return 0,[]

def modify_tf_nn_function_in_code(source_code, layer_names,new_value):

  
    for layer_name in layer_names:
        use_nn_list=[]
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        #pattern = rf"(tf\.nn\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.nn\.{layer_names}\([^\)]*\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        matches = re.findall(pattern, source_code)
        if matches:
            use_nn_list = [f"{m}" for m in matches]
            #print(use_nn_list)
        new_value = f"tf.nn.{layer_names}("
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        
        if source_code != temp_source:
            
            return new_value ,use_nn_list           
        return 0,[]

def modify_tf_raw_ops_function_in_code(source_code, layer_names,new_value):

    for layer_name in layer_names:
        use_raw_ops_list=[]
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        #pattern = rf"(tf\.raw_ops\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.raw_ops\.{layer_names}\([^\)]*\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.raw_ops.{layer_names}("
        matches = re.findall(pattern, source_code)
        if matches:
            use_raw_ops_list = [f"{m}" for m in matches]
            #print(use_raw_ops_list)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        
        if source_code != temp_source:
            
            return new_value,use_raw_ops_list
        return 0,[]

def modify_tf_train_class_in_code(source_code, layer_names,new_value):
    
    for layer_name in layer_names:
        
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        #pattern = rf"(tf\.train\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.train\.{layer_names}\([^\)]*\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.train.{layer_names}("
        matches = re.findall(pattern, source_code)
        if matches:
            use_train_list = [f"{m}" for m in matches]
            #print(use_train_list)
        source_code = re.sub(pattern, new_value, source_code)
        
        # Regex kullanarak değişiklik yapma
        if source_code != temp_source:
                             
            return new_value,use_train_list
        return 0,[]

def modify_tf_keras_activations_function_in_code(source_code, layer_names,new_value):

 
    for layer_name in layer_names:
        
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        #pattern = rf"(tf\.keras\.activations\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"tf\.keras\.activations\.{layer_names}\([^\)]*\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.activations.{layer_names}("
        matches = re.findall(pattern, source_code)
        if matches:
            use_activations_list = [f"{m}" for m in matches]
            #print(use_activations_list)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
            return new_value,use_activations_list
        return 0,[]
    



def modify_tf_bias_initializer_in_code(source_code, new_bias_initializer):
    bias_initializer_list = []
    pattern = r"bias_initializer\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        bias_initializer_list = [f"{m}" for m in matches]
        new_value = f"bias_initializer='{new_bias_initializer}'"
        return new_value, bias_initializer_list
    return 0, []




def modify_tf_strides_in_code(source_code, new_strides):
    strides_list = []
    pattern = r"strides\s*=\s*\(\s*\d+\s*,\s*\d+\s*\)"
    matches = re.findall(pattern, source_code)
    if matches:
        strides_list = [f"{m}" for m in matches]
        new_value = f"strides={new_strides}"
        return new_value, strides_list
    return 0, []

def modify_tf_padding_in_code(source_code, new_padding):
    padding_list = []
    pattern = pattern = r"padding\s*=\s*None|paddings\s*=\s*\[\s*\[.*?\]\s*\]"
    matches = re.findall(pattern, source_code)
    if matches:
        padding_list = [f"{m}" for m in matches]
        new_value = f"padding='{new_padding}'"
        return new_value, padding_list
    return 0, []

def modify_tf_data_format_in_code(source_code, new_data_format):
    data_format_list = []
    pattern = r"data_format\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        data_format_list = [f"{m}" for m in matches]
        new_value = f"data_format='{new_data_format}'"
        return new_value, data_format_list
    return 0, []

def modify_tf_dilation_rate_in_code(source_code, new_dilation_rate):
    dilation_rate_list = []
    pattern = r"dilation_rate\s*=\s*\(\s*\d+\s*,\s*\d+\s*\)"
    matches = re.findall(pattern, source_code)
    if matches:
        dilation_rate_list = [f"{m}" for m in matches]
        new_value = f"dilation_rate={new_dilation_rate}"
        return new_value, dilation_rate_list
    return 0, []

def modify_tf_groups_in_code(source_code, new_groups):
    groups_list = []
    pattern = r"groups\s*=\s*\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        groups_list = [f"{m}" for m in matches]
        new_value = f"groups={new_groups}"
        return new_value, groups_list
    return 0, []


def modify_tf_seed_in_code(source_code, new_seed):
    seed_list = []
    pattern = r"seed\s*=\s*(?:None|\d+)"

    matches = re.findall(pattern, source_code)
    if matches:
        seed_list = [f"{m}" for m in matches]
        new_value = f"seed={new_seed}"
        return new_value, seed_list
    return 0, []

def modify_tf_axis_in_code(source_code, new_axis):
    axis_list = []
    pattern = r"axis\s*=\s*(?:-1|\d+)"

    matches = re.findall(pattern, source_code)
    if matches:
        axis_list = [f"{m}" for m in matches]
        new_value = f"axis={new_axis}"
        return new_value, axis_list
    return 0, []


def modify_tf_from_logits_in_code(source_code, new_from_logits):
    from_logits_list = []
    pattern = r"from_logits\s*=\s*(True|False)"
    matches = re.findall(pattern, source_code)
    if matches:
        from_logits_list = [f"from_logits={m}" for m in matches]
        new_value = f"from_logits={new_from_logits}"
        return new_value, from_logits_list
    return 0, []

def modify_tf_label_smoothing_in_code(source_code, new_label_smoothing):
    label_smoothing_list = []
    pattern = r"label_smoothing\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        label_smoothing_list = [f"{m}" for m in matches]
        new_value = f"label_smoothing={new_label_smoothing}"
        return new_value, label_smoothing_list
    return 0, []

def modify_tf_use_cudnn_on_gpu_in_code(source_code, new_use_cudnn_on_gpu):
    use_cudnn_on_gpu_list = []
    pattern = r"use_cudnn_on_gpu\s*=\s*(True|False)"
    matches = re.findall(pattern, source_code)
    if matches:
        use_cudnn_on_gpu_list = [f"use_cudnn_on_gpu={m}" for m in matches]
        new_value = f"use_cudnn_on_gpu={new_use_cudnn_on_gpu}"
        return new_value, use_cudnn_on_gpu_list
    return 0, []



def modify_tf_ksize_in_code(source_code, new_ksize):
    ksize_list = []
    pattern = r"ksize\s*=\s*\(\s*\d+\s*,\s*\d+\s*\)"
    matches = re.findall(pattern, source_code)
    if matches:
        ksize_list = [f"{m}" for m in matches]
        new_value = f"ksize={new_ksize}"
        return new_value, ksize_list
    return 0, []

def modify_tf_keep_prob_in_code(source_code, new_keep_prob):
    keep_prob_list = []
    pattern = r"keep_prob\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        keep_prob_list = [f"{m}" for m in matches]
        new_value = f"keep_prob={new_keep_prob}"
        return new_value, keep_prob_list
    return 0, []

def modify_tf_rate_in_code(source_code, new_rate):
    rate_list = []
    pattern = r"rate\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        rate_list = [f"{m}" for m in matches]
        new_value = f"rate={new_rate}"
        return new_value, rate_list
    return 0, []

def modify_tf_training_in_code(source_code, new_training):
    training_list = []
    pattern = r"training\s*=\s*(True|False)"
    matches = re.findall(pattern, source_code)
    if matches:
        training_list = [f"training={m}" for m in matches]
        new_value = f"training={new_training}"
        return new_value, training_list
    return 0, []

def modify_tf_momentum_in_code(source_code, new_momentum):
    momentum_list = []
    pattern = r"momentum\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        momentum_list = [f"{m}" for m in matches]
        new_value = f"momentum={new_momentum}"
        return new_value, momentum_list
    return 0, []

def modify_tf_center_in_code(source_code, new_center):
    center_list = []
    pattern = r"center\s*=\s*(True|False)"
    matches = re.findall(pattern, source_code)
    if matches:
        center_list = [f"center={m}" for m in matches]
        new_value = f"center={new_center}"
        return new_value, center_list
    return 0, []

def modify_tf_scale_in_code(source_code, new_scale):
    scale_list = []
    pattern = r"scale\s*=\s*(True|False)"
    matches = re.findall(pattern, source_code)
    if matches:
        scale_list = [f"scale={m}" for m in matches]
        new_value = f"scale={new_scale}"
        return new_value, scale_list
    return 0, []

def modify_tf_beta_initializer_in_code(source_code, new_beta_initializer):
    beta_initializer_list = []
    pattern = r"beta_initializer\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        beta_initializer_list = [f"{m}" for m in matches]
        new_value = f"beta_initializer='{new_beta_initializer}'"
        return new_value, beta_initializer_list
    return 0, []
def modify_tf_gamma_initializer_in_code(source_code, new_gamma_initializer):
    gamma_initializer_list = []
    pattern = r"gamma_initializer\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        gamma_initializer_list = [f"{m}" for m in matches]
        new_value = f"gamma_initializer='{new_gamma_initializer}'"
        return new_value, gamma_initializer_list
    return 0, []

def modify_tf_moving_mean_initializer_in_code(source_code, new_moving_mean_initializer):
    moving_mean_initializer_list = []
    pattern = r"moving_mean_initializer\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        moving_mean_initializer_list = [f"{m}" for m in matches]
        new_value = f"moving_mean_initializer='{new_moving_mean_initializer}'"
        return new_value, moving_mean_initializer_list
    return 0, []

def modify_tf_moving_variance_initializer_in_code(source_code, new_moving_variance_initializer):
    moving_variance_initializer_list = []
    pattern = r"moving_variance_initializer\s*=\s*'[^']*'"
    matches = re.findall(pattern, source_code)
    if matches:
        moving_variance_initializer_list = [f"{m}" for m in matches]
        new_value = f"moving_variance_initializer='{new_moving_variance_initializer}'"
        return new_value, moving_variance_initializer_list
    return 0, []



def modify_tf_depth_radius_in_code(source_code, new_depth_radius):
    depth_radius_list = []
    pattern = r"depth_radius\s*=\s*\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        depth_radius_list = [f"{m}" for m in matches]
        new_value = f"depth_radius={new_depth_radius}"
        return new_value, depth_radius_list
    return 0, []

def modify_tf_bias_in_code(source_code, new_bias):
    bias_list = []
    pattern = r"bias\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        bias_list = [f"{m}" for m in matches]
        new_value = f"bias={new_bias}"
        return new_value, bias_list
    return 0, []

def modify_tf_alpha_in_code(source_code, new_alpha):
    alpha_list = []
    pattern = r"alpha\s*=\s*\d*\.?\d+"
    matches = re.findall(pattern, source_code)
    if matches:
        alpha_list = [f"{m}" for m in matches]
        new_value = f"alpha={new_alpha}"
        return new_value, alpha_list
    return 0, []
def modify_l1_regularizer_in_code(source_code, new_l1_regularizer):
    l1_regularizer_list = []
    pattern = r"l1\(\d*\.?\d+\)"
    matches = re.findall(pattern, source_code)
    if matches:
        l1_regularizer_list = [f"{m}" for m in matches]
        new_value = f"l1({new_l1_regularizer})"
        return new_value, l1_regularizer_list
    return 0, []
import re

def modify_l2_regularizer_in_code(source_code, new_l2_regularizer):
    l2_regularizer_list = []
    pattern = r"l2\(\d*\.?\d+\)"
    matches = re.findall(pattern, source_code)
    if matches:
        l2_regularizer_list = [f"{m}" for m in matches]
        new_value = f"l2({new_l2_regularizer})"
        return new_value, l2_regularizer_list
    return 0, []

def modify_tf_trainable_in_code(source_code, new_trainable):
    trainable_list = []
    pattern = r"trainable\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        trainable_list = [f"{m}" for m in matches]
        new_value = f"trainable={new_trainable}"
        return new_value, trainable_list
    return None, []

def modify_tf_beta1_in_code(source_code, new_beta1):
    beta1_list = []
    pattern = r"beta1\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        beta1_list = [f"{m}" for m in matches]
        new_value = f"beta1={new_beta1}"
        return new_value, beta1_list
    return None, []

def modify_tf_beta2_in_code(source_code, new_beta2):
    beta2_list = []
    pattern = r"beta2\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        beta2_list = [f"{m}" for m in matches]
        new_value = f"beta2={new_beta2}"
        return new_value, beta2_list
    return None, []

def modify_tf_epsilon_in_code(source_code, new_epsilon):
    epsilon_list = []
    pattern = r"epsilon\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        epsilon_list = [f"{m}" for m in matches]
        new_value = f"epsilon={new_epsilon}"
        return new_value, epsilon_list
    return None, []

def modify_tf_decay_in_code(source_code, new_decay):
    decay_list = []
    pattern = r"decay\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        decay_list = [f"{m}" for m in matches]
        new_value = f"decay={new_decay}"
        return new_value, decay_list
    return None, []

def modify_tf_global_step_in_code(source_code, new_global_step):
    global_step_list = []
    pattern = r"global_step\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        global_step_list = [f"{m}" for m in matches]
        new_value = f"global_step={new_global_step}"
        return new_value, global_step_list
    return None, []

def modify_tf_decay_steps_in_code(source_code, new_decay_steps):
    decay_steps_list = []
    pattern = r"decay_steps\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        decay_steps_list = [f"{m}" for m in matches]
        new_value = f"decay_steps={new_decay_steps}"
        return new_value, decay_steps_list
    return None, []

def modify_tf_decay_rate_in_code(source_code, new_decay_rate):
    decay_rate_list = []
    pattern = r"decay_rate\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        decay_rate_list = [f"{m}" for m in matches]
        new_value = f"decay_rate={new_decay_rate}"
        return new_value, decay_rate_list
    return None, []

def modify_tf_capacity_in_code(source_code, new_capacity):
    capacity_list = []
    pattern = r"capacity\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        capacity_list = [f"capacity={m}" for m in matches]
        new_value = f"capacity={new_capacity}"
        return new_value, capacity_list
    return None, []

def modify_tf_max_to_keep_in_code(source_code, new_max_to_keep):
    max_to_keep_list = []
    pattern = r"max_to_keep\s*=\s*[^,)]+"
    matches = re.findall(pattern, source_code)
    if matches:
        max_to_keep_list = [f"{m}" for m in matches]
        new_value = f"max_to_keep={new_max_to_keep}"
        return new_value, max_to_keep_list
    return None, []