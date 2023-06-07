import os, json

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
extension_dict = {}
count_folders = 0
count_files = 0
# loop over each directory in the "codes" directory
for code_dir in os.listdir(root_directory):
    code_dir_path = os.path.join(root_directory, code_dir)
    if os.path.isdir(code_dir_path):
        count_folders += 1
        # loop over all files in this directory
        for file in os.listdir(code_dir_path):
            if file.endswith(".txt"):
                count_files += 1
                input_file_path = os.path.join(code_dir_path, file)
                extension = file.split(".")[-2]
                if extension == "H":
                    input_file_path = os.path.join(code_dir_path, file)
                    with open(input_file_path, "r") as input_file:
                        content = input_file.read()
                        # print(content + "\n")
                        print(input_file_path)
                if not extension in extension_dict.keys():
                    extension_dict[extension] = {}
                    extension_dict[extension]["count"] = 0
                    extension_dict[extension]["is_development"] = is_development_code[
                        extension
                    ]
                extension_dict[extension]["count"] += 1

print(f"Total number of folders: {count_folders}")
print(f"Total number of files: {count_files}")
print()
print("File Extension\t\tCount\t\tIs Development Code?")
for extension in sorted(
    extension_dict.keys(), key=lambda x: extension_dict[x]["count"], reverse=True
):
    print(
        f"{extension}\t\t\t{extension_dict[extension]['count']}\t\t\t{extension_dict[extension]['is_development']}"
    )
print(f"Total\t\t\t{count_files}")
