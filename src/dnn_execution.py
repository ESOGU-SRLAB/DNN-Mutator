"""
DNN EXECUTION and MONITORING PROCESS
"""
import subprocess
import re
import json
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def execute_original_source_code(source_code_path, user_selection):
    """
    Executes a given Python script and prints the found accuracy from the
    original source code.
    """
    run_command = f'python {source_code_path}'
    print("Run Command: ", run_command)

    try:
        result = subprocess.run(
            run_command, shell=True, capture_output=True, text=True)
        output = result.stdout
        print("Output: ", output)
        #accuracy_match_metric = re.search(r'Accuracy: (\d+\.\d+)%', output)
        #accuracy_match_metric = re.search(r'Accuracy\s*:\s*(\d+\.\d+)\s*%', output)

        print("USER SELECTION: ", user_selection)

        if user_selection == "Accuracy":
            accuracy_match_metric = re.search(r'Accuracy\s*[:=]?\s*(\d+(\.\d+)?)\s*%', output)
        elif user_selection == "LSTM":
            print("r2 score aranıyor, aranan çıktı", output)
            accuracy_match_metric = re.search(r'r2 score:\s*(-?\d+\.?\d*)', output)
            print("## LSTM Metric Control ##", accuracy_match_metric)
        elif user_selection == "RL":
            accuracy_match_metric=re.search(r'Reward_Max:\s*(\d+)', output)
            print("## RL Metric Control ##", accuracy_match_metric)
        else:
            print("None of the AI Model for the given selection. Please select the correct AI Model.")

        if accuracy_match_metric:
            accuracy_value = float(accuracy_match_metric.group(1))
            print(f'The Accuracy of Original Source Code: {accuracy_match_metric}')
            print("Accuracy Value", accuracy_value)
            return accuracy_value

    except Exception as e:
        print(f'An error occurred while running the original source code: {e}')


def execute_file(threshold, mutant_files_save_location, user_selection):
    """
    Executes a given Python script and prints the found accuracy.

    Parameters:
        threshold (float): The threshold for comparison.
        mutant_files_save_location (list): List of file paths to mutants.

    Returns:
        tuple: A tuple containing lists of 'killed' and 'survived' based on
        the threshold and accuracy list.
    """
    killed, survived, accuracy_list = [], [], []
    killed_count=0
    survived_count=0
    for mutant_file in mutant_files_save_location:
        run_command = f'python3 {mutant_file}'

        try:
            # Run the command and capture the output with subprocess
            result = subprocess.run(
                run_command, shell=True, capture_output=True, text=True)
            # Get the output of the command
            output = result.stdout

            # accuracy_match = re.search(r'Accuracy\s*:\s*(\d+\.\d+)\s*%', output)
            # accuracy_match founds the accuracy value in the output with regex search function
            if user_selection == "CNN":
                accuracy_match_r2_score = re.search(r'Accuracy\s*[:=]?\s*(\d+(\.\d+)?)\s*%', output)
            # Which accuracy match r2 score variable is used to find the r2 score value in the output with regex search function?
            elif user_selection == "LSTM":
                accuracy_match_r2_score=re.search(r'r2 score:\s*(\d+\.\d+)', output)
            elif user_selection == "RL":
                accuracy_match_r2_score=re.search(r'Reward_Max:\s*(\d+)', output)
            else:
                print("None of the AI Model for the given selection. Please select the correct AI Model.")
            
            if accuracy_match_r2_score:
                if user_selection == "CNN" or user_selection == "LSTM":
                    # If the accuracy is found, convert it to a float
                    accuracy_value = float(accuracy_match_r2_score.group(1))
                    # When the accuracy is found, print the accuracy
                    print(f'Found the Metric: {accuracy_match_r2_score}')

                    mutant_file_and_accuracy = (
                        f"Mutant File: {mutant_file} Value: {accuracy_value}")
                    accuracy_list.append(mutant_file_and_accuracy)
                    #RL için value tresholddan büyükse killed olur 
                    if accuracy_value < threshold:
                        # If the accuracy is greater than the threshold, the mutant is killed
                        killed.append(mutant_file)
                        killed_count=killed_count+1
                    else:
                        # If the accuracy is less than the threshold, the mutant is survived
                        survived.append(mutant_file)
                        survived_count=survived_count+1
                if user_selection == "RL":
                    # If the accuracy is found, convert it to a float
                    accuracy_value = float(accuracy_match_r2_score.group(1))
                    # When the accuracy is found, print the accuracy
                    print(f'Found the Metric: {accuracy_match_r2_score}')

                    mutant_file_and_accuracy = (
                        f"Mutant File: {mutant_file} Value: {accuracy_value}")
                    accuracy_list.append(mutant_file_and_accuracy)
                    #RL için value tresholddan büyükse killed olur 
                    if accuracy_value > threshold:
                        # If the accuracy is greater than the threshold, the mutant is killed
                        killed.append(mutant_file)
                        killed_count=killed_count+1
                    else:
                        # If the accuracy is less than the threshold, the mutant is survived
                        survived.append(mutant_file)
                        survived_count=survived_count+1
                        
                        

            else:
                killed.append(mutant_file)
                killed_count=killed_count+1
                mutant_file_and_accuracy = (
                    "Mutant File: {} No Value:".format(mutant_file))
                accuracy_list.append(mutant_file_and_accuracy)

        except Exception as e:
            if mutant_file not in killed:
                killed.append(mutant_file)
                killed_count=killed_count+1
                mutant_file_and_accuracy = (
                    f"Mutant File: {mutant_file} Accuracy: Exception.")
                accuracy_list.append(mutant_file_and_accuracy)

    return killed, survived, accuracy_list,survived_count,killed_count


def find_accuracy_lines(file_name):
    """
    Find lines in a given file that contain 'Accuracy' or 'accuracy' and are
    not comments.

    Parameters:
        file_name (str): The name of the file to search.

    Returns:
        list: A list of matching lines.
    """
    matching_lines = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if ('Accuracy' in line or 'accuracy' in line or 'r2 score' in line or 'Reward_Max' in line) and not line.strip().startswith('#'):
                    matching_lines.append(line.strip())

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return matching_lines


def take_backup_source_file(original_source_code_file_dir):
    """ Create a backup of the original file """
    backup_file_name = "backup.py"
    original_source_code_file_dir_elements = original_source_code_file_dir.split("/")
    backup_original_source_code_file_directory = original_source_code_file_dir.replace(
        original_source_code_file_dir_elements[-1], backup_file_name)

    shutil.copy(original_source_code_file_dir,
                backup_original_source_code_file_directory)
    return backup_original_source_code_file_directory


def read_json(file_name):
    """
    Define a function to read and print the JSON data from the same directory
    as the script
    """
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data, len(data)
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "File is not a valid JSON file."


def take_target_file_content(file_dir):
    """ Read the content of the file """
    with open(file_dir, 'r') as file:
        content = file.read()
    return content


def generate_mutants_specific_location(merged_mutant_file_location, mutated_content):
    """ Write the mutated content to a new file at the selected location """
    with open(merged_mutant_file_location, 'w') as file:
        file.write(mutated_content)


def restore_original_source_code_from_backup(
        backup_original_source_code_file_directory, original_source_code_file_dir):
    """ Restore the original file from backup and delete backup file """
    shutil.copy(backup_original_source_code_file_directory,
                original_source_code_file_dir)


def mutation_process(original_source_code_file_dir, fiplan_json_dir, target_location_to_save_mutants):
    mutant_file_paths = []

    # Take backup of original source code and get the backup file dir
    backup_file_dir = take_backup_source_file(original_source_code_file_dir)
    json_data, length_of_json_data = read_json(fiplan_json_dir)

    for i in range(length_of_json_data):
        # Extracting file details
        fault = json_data[i]
        file_dir = fault["Fault"]["File_Directory"]
        source_code = fault["Fault"]["Source_Code"]
        mutate_code = fault["Fault"]["Mutate_Code"]
        match_number = fault["Fault"]["Match_Number"]  # Match numarasını al

        file_dir_content = take_target_file_content(file_dir)

        # Belirli bir eşleşmeyi değiştir
        mutated_content = replace_nth_occurrence(file_dir_content, source_code, mutate_code, match_number - 1)

        target_location_to_save_mutants = (target_location_to_save_mutants)
        mutant_name_with_number = f"/mutant_{i}.py"
            # Merge location and mutant file name
        merged_mutant_file_location = (
            f"{target_location_to_save_mutants}{mutant_name_with_number}")
        mutant_file_paths.append(merged_mutant_file_location)

        # Generate mutants at the specific location
        generate_mutants_specific_location(
            merged_mutant_file_location, mutated_content)

        # Restore the original file from backup and delete backup
        restore_original_source_code_from_backup(
            backup_file_dir, original_source_code_file_dir)

    return mutant_file_paths



    
def replace_nth_occurrence(string, old, new, n):
    """Belirtilen n'inci eşleşmede değişiklik yapar."""
    parts = string.split(old, n+1)
    if len(parts) <= n+1:
        return string  # Eşleşme sayısı n'den az ise değişiklik yapma
    return old.join(parts[:-1]) + new + old.join(parts[-1:])

def show_results(killed,survived,accuracy_list):
    """ Show the results after the execution process """
    print("\n\n\n")
    print("\t\tRESULTS OF THE EXECUTION PROCESS")
    print("\n")
    print("Killed", killed)
    print("Survived", survived)
    print("Mutant Value List", accuracy_list)





def create_pdf(text, filename):
    """
    Creates a multi-page PDF file with the given text.

    Parameters:
        text (str): The text to write to the PDF.
        filename (str): The filename for the PDF.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    text_object = c.beginText(40, 750)
    text_object.setFont("Times-Roman", 12)

    # Satır başı yüksekliği ve sayfa başına maksimum satır sayısı
    line_height = 14
    max_lines_per_page = 50
    lines = 0

    for line in text.split('\n'):
        text_object.textLine(line)
        lines += 1
        # Eğer maksimum satır sayısına ulaşıldıysa, yeni bir sayfa başlat
        if lines >= max_lines_per_page:
            c.drawText(text_object)
            c.showPage()
            text_object = c.beginText(40, 750)
            lines = 0

    # Kalan metni sayfaya yazdır
    c.drawText(text_object)
    c.save()
