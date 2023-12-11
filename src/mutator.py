import ast
import astunparse
import re
import random
#-------------------------------------------------------------------------epoch
# AST Value Mutator
class ConstantMutator(ast.NodeTransformer):
    def __init__(self, target_keyword, new_value):
        self.target_keyword = target_keyword
        self.new_value = new_value

    def visit_Call(self, node):
        for keyword in node.keywords:
            if keyword.arg == self.target_keyword:
                keyword.value = ast.Str(s=self.new_value)
        return node


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
    return new_code

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

def modify_code_in_file_activation(source_code, target_keyword, new_value):
    
    code = source_code

    node = ast.parse(code)
    renamer = ConstantMutatoractivation(target_keyword, new_value)
    new_node = renamer.visit(node)
    new_code = astunparse.unparse(new_node)
    return new_code
#--------------------------------------------------------------------Conv2D



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
    return source_code

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
    return source_code

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
    return source_code

def modify_tf_layer_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[^)]*\)"
        #pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()[\s\S]*?(\))"
        pattern = rf"(tf\.keras\.layers\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.layers.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code

def modify_tf_losses_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        #pattern = rf"(tf\.keras\.losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern = rf"(tf\.(keras\.)?losses\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.keras.losses.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code



def modify_tf_optimizers_in_code(source_code, layer_names,new_value):
    
    for layer_name in layer_names:
        # 'legacy' ve 'schedules' ifadeleri için özel desenler
        pattern_legacy = rf"(tf\.keras\.optimizers\.legacy\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        pattern_schedules = rf"(tf\.keras\.optimizers\.schedules\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        
        if re.search(pattern_legacy, source_code):
            # 'legacy' için yeni değer
            new_value = f"tf.keras.optimizers.{layer_names}()"
            source_code = re.sub(pattern_legacy, new_value, source_code)
        elif re.search(pattern_schedules, source_code):
            # 'schedules' için yeni değer
            new_value = f"tf.keras.optimizers.{layer_names}()"
            source_code = re.sub(pattern_schedules, new_value, source_code)
        #elif():
            #new_value = f"tf.keras.optimizers.{layer_names}()"
    return source_code

def modify_tf_nn_function_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni

        pattern = rf"(tf\.nn\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.nn.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code

def modify_tf_raw_ops_function_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni

        pattern = rf"(tf\.raw_ops\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.raw_ops.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code

def modify_tf_train_class_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni

        pattern = rf"(tf\.train\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.train.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code

def modify_tf_keras_activations_function_in_code(source_code, layer_names,new_value):
    for layer_name in layer_names:
        # Katman adını ve sonrasında gelen parantezli ifadeyi bulmak için regex deseni

        pattern = rf"(tf\.keras\.activations\.\b{layer_names}\b\s*\()((?:[^()]|\([^)]*\))*)\)"
        # Bulunan ifadeyi değiştirmek için yeni değer
        new_value = f"tf.activations.{layer_names}()"
        # Regex kullanarak değişiklik yapma
        source_code = re.sub(pattern, new_value, source_code)
    return source_code