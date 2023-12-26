import subprocess
import re

def execute_file(script_name, threshold=98.0):
    """
    Executes a given Python script and prints the found accuracy.

    Parameters:
        script_name (str): The name of the script to execute.
        threshold (float): The threshold for comparison.

    Returns:
        tuple: A tuple containing lists of 'killed' and 'survived' based on the threshold.
    """
    run_command = f'python {script_name}'
    killed, survived = [], []

    try:
        result = subprocess.run(run_command, shell=True, capture_output=True, text=True)
        output = result.stdout

        accuracy_match = re.search(r'Accuracy: (\d+\.\d+)%', output)
        if accuracy_match:
            accuracy_value = float(accuracy_match.group(1))
            print(f'Found Accuracy: {accuracy_value}%')

            if accuracy_value < threshold:
                killed.append(script_name)
            else:
                survived.append(script_name)
        else:
            print('Accuracy value not found in the script output.')

    except Exception as e:
        print(f'An error occurred while running the script: {e}')

    return killed, survived

def find_accuracy_lines(file_name):
    """
    Find lines in a given file that contain 'Accuracy' or 'accuracy' and are not comments.

    Parameters:
        file_name (str): The name of the file to search.

    Returns:
        list: A list of matching lines.
    """
    matching_lines = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if not line.strip().startswith('#') and ("Accuracy" in line or "accuracy" in line):
                    matching_lines.append(line.strip())

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return matching_lines

def main():
    """
    Main function to execute the script and print results based on accuracy.
    """
    file_name = 'basic_model.py'
    matching_lines = find_accuracy_lines(file_name)
    
    if matching_lines:
        print("Execution process is started... Just wait for accuracy value!")
        killed, survived = execute_file(file_name)
        print("Killed", killed)
        print("Survived", survived)
    else:
        print("Please ensure the script contains an accuracy line.")

if __name__ == "__main__":
    main()
