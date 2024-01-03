"""
DNN EXECUTION and MONITORING PROCESS
"""
import subprocess
import re
import json
import shutil


def execute_original_source_code(source_code):
    """
    Executes a given Python script and prints the found accuracy from the
    original source code.
    """
    run_command = f'python3 {source_code}'

    try:
        result = subprocess.run(
            run_command, shell=True, capture_output=True, text=True)
        output = result.stdout
        print(output)

        accuracy_match = re.search(r'Accuracy: (\d+\.\d+)%', output)
        if accuracy_match:
            accuracy_value = float(accuracy_match.group(1))
            print(f'The Accuracy of Original Source Code: {accuracy_value}%')
            return accuracy_value

    except Exception as e:
        print(f'An error occurred while running the original source code: {e}')


def execute_file(threshold, mutant_files_save_location):
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
    for mutant_file in mutant_files_save_location:
        run_command = f'python3 {mutant_file}'

        try:
            result = subprocess.run(
                run_command, shell=True, capture_output=True, text=True)
            output = result.stdout

            accuracy_match = re.search(r'Accuracy: (\d+\.\d+)%', output)
            if accuracy_match:
                accuracy_value = float(accuracy_match.group(1))
                print(f'Found Accuracy: {accuracy_value}%')

                mutant_file_and_accuracy = (
                    f"Mutant File: {mutant_file} Accuracy: {accuracy_value}")
                accuracy_list.append(mutant_file_and_accuracy)

                if accuracy_value < threshold:
                    killed.append(mutant_file)
                else:
                    survived.append(mutant_file)

            else:
                killed.append(mutant_file)
                mutant_file_and_accuracy = (
                    "Mutant File: {} Accuracy: Accuracy value not found in the"
                    " script output.".format(mutant_file))
                accuracy_list.append(mutant_file_and_accuracy)

        except Exception as e:
            if mutant_file not in killed:
                killed.append(mutant_file)
                mutant_file_and_accuracy = (
                    f"Mutant File: {mutant_file} Accuracy: Exception.")
                accuracy_list.append(mutant_file_and_accuracy)

    return killed, survived, accuracy_list


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
                if ('Accuracy' in line or 'accuracy' in line) and not line.strip().startswith('#'):
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


def mutation_process(original_source_code_file_dir, fiplan_json_dir):
    """
    Define a function to perform the desired task
    """
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

        file_dir_content = take_target_file_content(file_dir)

        # Replace the source code with the mutate code
        mutated_content = file_dir_content.replace(source_code, mutate_code)

        target_location_to_save_mutants = (
            "/Users/cembaglum/Desktop/ASRLAB/2_SUIT_1004/Kodlar/"
            "Execution_Module/mutant_files")
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

def show_results(killed,survived,accuracy_list):
    """ Show the results after the execution process """
    print("\n\n\n")
    print("\t\tRESULTS OF THE EXECUTION PROCESS")
    print("\n")
    print("Killed", killed)
    print("Survived", survived)
    print("Mutant Accuracy List", accuracy_list)

def main():
    """
    Main function to execute the script and print results based on accuracy.
    """
    file_name = (
        '/Users/cembaglum/Desktop/ASRLAB/2_SUIT_1004/Kodlar/'
        'Execution_Module/basic_model.py')
    fiplan_json_dir = (
        '/Users/cembaglum/Desktop/ASRLAB/2_SUIT_1004/Kodlar/'
        'Execution_Module/denemelik_fiplan.json')

    matching_lines = find_accuracy_lines(file_name)

    if matching_lines:
        print("Execution process is started... Just wait for accuracy value!")
        threshold = execute_original_source_code(file_name)
        if threshold:
            mutant_files_save_location = mutation_process(
                file_name, fiplan_json_dir)
            killed, survived, accuracy_list = execute_file(
                threshold, mutant_files_save_location)
            show_results(killed,survived,accuracy_list)
        else:
            print("Please be sure to use original source code which has"
                  " accuracy value!")
    else:
        print("Please ensure the script contains an accuracy line.")


if __name__ == "__main__":
    main()
