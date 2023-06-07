import os
from GptApi import GptApi
import json

gpt = GptApi()


categories_file = open("./problemCategories.json", "r")
categories = json.load(categories_file)["categories"]

is_development_code_file = open("isDevelopmentCode.json", "r")
is_development_code = json.load(is_development_code_file)["is_development_code"]
# Convert string values to Python boolean values
for key, value in is_development_code.items():
    if value.lower() == "true":
        is_development_code[key] = True
    elif value.lower() == "false":
        is_development_code[key] = False

# root directory containing all code directories - 3 different code versions
# root_directory = "codes_preprocessed"
root_directories = ["codes", "codes_spaceless", "codes_preprocessed"]

# two system roles for conversation
system_roles = [
    f"You are a parallel computing expert. I will provide you a source code in C or C++ and I want you to classify if there is an inefficiency problem in the code. If there is an problem, I want you to classify this problem from the following list: {categories} and return an answer with the following format and this format only, don't provide explanation: Type: classified_type. If you think there is no inefficiency in the program, return: Type: None",
    f"You are a parallel computing expert. I will provide you a source code in C or C++ and I want you to classify if there is an inefficiency problem in the code. If there is an problem, I want you to classify this problem from the following list: {categories} and return an answer with the following format and this format only, don't provide explanation: Type: classified_type.",
]

# create a new directory to store spaceless files - total of 3*2=6 directories
new_directory = "conversations_classify_preprocessed_with_none"
new_directories = [
    "codes_conversations_with_none",
    "codes_conversations_without_none",
    "codes_spaceless_conversations_with_none",
    "codes_spaceless_conversations_without_none",
    "codes_preprocessed_conversations_with_none",
    "codes_preprocessed_conversations_without_none",
]
for directory in new_directories:
    if not os.path.exists(directory):
        os.mkdir(directory)

for i in range(len(new_directories)):
    for code_dir in os.listdir(root_directories[i // 2]):
        code_dir_path = os.path.join(root_directories[i // 2], code_dir)
        print(code_dir)
        if os.path.isdir(code_dir_path):
            # create a sub-directory for the respective commit
            conversation_dir_path = os.path.join(new_directories[i], code_dir)
            if not os.path.exists(conversation_dir_path):
                os.mkdir(conversation_dir_path)

            # loop over all files in the code directory
            for file in os.listdir(code_dir_path):
                if file.endswith(".txt"):
                    file_extension = file.split(".")[-2]
                    if not is_development_code[file_extension]:
                        continue
                    filename = file.split(".")[0]
                    conversation_sub_dir_path = os.path.join(
                        conversation_dir_path, f"{filename}"
                    )

                    if not os.path.exists(conversation_sub_dir_path):
                        os.mkdir(conversation_sub_dir_path)

                    gpt.define_system_role(system_roles[i % 2])
                    code_file = open(os.path.join(code_dir_path, file), "r")
                    code = code_file.read()

                    try:
                        gpt.create_prompt(code)
                        gpt.write_conversation_to_file(conversation_sub_dir_path)
                    except:
                        pass
                    gpt.clear_conversation()
