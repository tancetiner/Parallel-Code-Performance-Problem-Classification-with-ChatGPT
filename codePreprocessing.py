import os, json

import re

comment_patterns = {
    "c": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "cpp": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "py": r"#.*",
    "h": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "hpp": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "cu": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "cuh": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "cl": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "cc": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "clh": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "C": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "F": r"!.*",
    "Z14": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "HASWELL": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)",
    "H": r"(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)|//.*",
    "ml": r"\(\*.*?\*\)",
}


def remove_comments(code, language):
    pattern = comment_patterns.get(language)
    if pattern:
        code_without_comment = re.sub(pattern, "", code, flags=re.MULTILINE)
    return code_without_comment


is_development_code_file = open("isDevelopmentCode.json", "r")
is_development_code = json.load(is_development_code_file)["is_development_code"]

# Convert string values to Python boolean values
for key, value in is_development_code.items():
    if value.lower() == "true":
        is_development_code[key] = True
    elif value.lower() == "false":
        is_development_code[key] = False

# root directory containing all code directories
root_directory = "codes"

# create a new directory to store spaceless files
new_directory = "codes_preprocessed"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)

# loop over each directory in the "codes" directory
for code_dir in os.listdir(root_directory):
    code_dir_path = os.path.join(root_directory, code_dir)
    if os.path.isdir(code_dir_path):
        # create a new directory for the spaceless version of this directory
        processed_dir_path = os.path.join(new_directory, f"{code_dir}")
        if not os.path.exists(processed_dir_path):
            os.mkdir(processed_dir_path)

        # loop over all files in this directory
        for file in os.listdir(code_dir_path):
            if file.endswith(".txt"):
                extension = file.split(".")[-2]
                if not is_development_code[extension]:
                    continue
                input_file_path = os.path.join(code_dir_path, file)
                output_file_path = os.path.join(
                    processed_dir_path, f"{os.path.splitext(file)[0]}.txt"
                )

                # read the content of the file and remove extra spaces
                with open(input_file_path, "r") as input_file:
                    content = input_file.read()

                code_without_comments = remove_comments(content, extension)
                processed_code = " ".join(code_without_comments.split())

                # write the cleaned content to the output file
                with open(output_file_path, "w") as output_file:
                    output_file.write(processed_code)

                print(
                    f'"{input_file_path}" was cleaned and saved to "{output_file_path}".'
                )
