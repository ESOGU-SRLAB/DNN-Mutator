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
        print(f"Modified code saved as 'mutator_code.py'")
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

def replace_input_shape(source_code, new_shape):
    # Regex deseni: 'input_shape=(...)' formundaki ifadeleri bulur
    i=0
    pattern = r"input_shape=\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)"

    # Yeni değerle değiştir
    updated_code = re.sub(pattern, f"input_shape={new_shape[i]}", source_code)
    matches = re.finditer(pattern, source_code)
    matches_list = list(matches)
    if matches_list:
        return updated_code,matches_list
    print(updated_code)
    i=i+1
    return new_shape,[]

def modify_tf_activation_in_code(source_code, layer_names, new_value):
    i=0
    for layer_name in layer_names:
        temp_source = source_code
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        pattern = r"activation='[^']*'"
       
        # Find matches using regex
        matches = re.findall(pattern, source_code)
        # Replace found instances with the new value
        source_code = re.sub(pattern, "activation="+"'"+new_value[i]+"'", source_code)
        # Check if the source code has changed
        activation_list = [f"activation={m}" for m in matches]
        print(activation_list)
        if source_code != temp_source:
            i=i+1                   
            return source_code, matches
            
    return 0, []

def modify_tf_learning_rate_in_code(source_code, layer_names, new_value):
    i=0
    for layer_name in layer_names:
        temp_source = source_code
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        pattern = r"(learning_rate\s*=\s*\d*\.?\d+)"
       
        # Find matches using regex
        matches = re.findall(pattern, source_code)
        # Replace found instances with the new value
        source_code = re.sub(pattern, "learning_rate="+"'"+new_value[i]+"'", source_code)
        # Check if the source code has changed
        print(matches)
        if source_code != temp_source:
            i=i+1                   
            return source_code, matches
            
    return 0, []


def replace_kernel_size_in_code(source_code,new_kernel_size):
    i=1
    # Regex deseni: 'kernel_size=...' formundaki ifadeleri bulur
    # Hem tek sayı hem de parantez içindeki sayı çiftlerini kapsar
    pattern = r"kernel_size\s*=\s*((?:\(\s*\d+\s*(?:,\s*\d+\s*)*\))|\d+)"


    #pattern = r"kernel_size\s*=\s*(\(\s*\d+\s*,\s*\d+\s*\)|\d+)"
    #pattern = r"kernel_size\s*=\s*(\d+|\(\s*\d+\s*(,\s*\d+\s*)+\))"
    matches = re.findall(pattern, source_code)

    # Yeni değerle değiştir
    updated_code = re.sub(pattern, "learning_rate="+"'"+new_kernel_size[i]+"'", source_code)
    matches_list = list(matches)
    kernel_size_list = [f"kernel_size={m}" for m in matches]  # List of original kernel_size values
    print(kernel_size_list)
       
    if matches_list:
            i=i+1                  
            return source_code, matches
    return 0,[]



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

def modify_code_in_file_MaxPooling2D(source_code, new_value):
    # MaxPooling2D çağrısını bulma
    pattern = r"layers\.MaxPooling2D\(\(\d+, \d+\)\)"
    matches = re.finditer(pattern, source_code)
    matches_list = list(matches)

    if matches_list:
        # İlk eşleşmeyi al
        selected_match = matches_list[0]
        original_code = selected_match.group(0)
        new_code = new_value  # Yeni kodu belirle
        source_code = source_code.replace(original_code, new_code, 1)  # İlk eşleşmeyi değiştir
    return new_value

def modify_code_in_file_InputShape(source_code, new_value):
    # input_shape içeren Conv2D çağrısını bulma
    pattern = r"input_shape=\(\d+, \d+, \d+\)"
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
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    name="_layer" 
    global counter   
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[^)]*\)"
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[\s\S]*?(\))"
        pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"

        temp_source=source_code

        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.layers.{layer_names}(new_value)"
        matches = re.findall(pattern, source_code)

        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
            print(matches)
            return new_value,matches
        return 0,[]

def modify_tf_losses_in_code(source_code, layer_names,new_value):
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    name="_losses"
    global counter
    for layer_name in layer_names:
        #pattern = rf"(tf\.keras\.losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"(tf\.(keras\.)?losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        temp_source=source_code
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.losses.{layer_names}()"
        matches = re.findall(pattern, source_code)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
              
            return new_value,matches
        return 0,[]



def modify_tf_optimizers_in_code(source_code, layer_names,new_value):
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    global counter
    for layer_name in layer_names:
        # 'legacy' ve 'schedules' ifadeleri için özel desenler
        pattern_legacy = rf"(tf\.keras\.optimizers\.legacy\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern_schedules = rf"(tf\.keras\.optimizers\.schedules\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        temp_source=source_code
        if re.search(pattern_legacy, source_code):
            # 'legacy' için yeni değer
            new_value = f"tf.keras.optimizers.{layer_names}()"
            matches = re.findall(pattern_legacy, source_code)
            source_code = re.sub(pattern_legacy, new_value, source_code)
            name="_optimizers_legacy"
        elif re.search(pattern_schedules, source_code):
            # 'schedules' için yeni değer
            new_value = f"tf.keras.optimizers.{layer_names}()"
            matches = re.findall(pattern_schedules, source_code)
            source_code = re.sub(pattern_schedules, new_value, source_code)
        #elif():
            #new_value = f"tf.keras.optimizers.{layer_names}()"
            name="_optimizers_schedules"
        if source_code != temp_source:
            
            return new_value,matches
        return 0,[]

def modify_tf_nn_function_in_code(source_code, layer_names,new_value):
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    name="_nn"
    global counter
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        pattern = rf"(tf\.nn\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        matches = re.findall(pattern, source_code)
        new_value = f"tf.nn.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
            
            return new_value ,matches           
        return 0,[]

def modify_tf_raw_ops_function_in_code(source_code, layer_names,new_value):
    name="_raw_ops"
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    global counter
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        pattern = rf"(tf\.raw_ops\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.raw_ops.{layer_names}()"
        matches = re.findall(pattern, source_code)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        
        if source_code != temp_source:
            
            return new_value,matches
        return 0,[]

def modify_tf_train_class_in_code(source_code, layer_names,new_value):
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    name="_train"
    global counter
    for layer_name in layer_names:
        
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        pattern = rf"(tf\.train\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.train.{layer_names}()"
        matches = re.findall(pattern, source_code)
        source_code = re.sub(pattern, new_value, source_code)
        
        # Regex kullanarak değişiklik yapma
        if source_code != temp_source:
            print(matches)                    
            return new_value,matches
        return 0,[]

def modify_tf_keras_activations_function_in_code(source_code, layer_names,new_value):
    path="C:\\Users\\Gökhan\\Desktop\\Mutations\\"
    name="_keras_activations"
    global counter
    for layer_name in layer_names:
        
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        temp_source=source_code
        pattern = rf"(tf\.keras\.activations\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.activations.{layer_names}()"
        matches = re.findall(pattern, source_code)
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
        if source_code != temp_source:
            print(matches)   
            return new_value,matches
        return 0,[]