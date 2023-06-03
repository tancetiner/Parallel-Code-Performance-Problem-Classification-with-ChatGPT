from GptApi import GptApi
import json

gpt = GptApi()

code_file = open("./inClassCode.txt", "r")
code = code_file.read()
categories_file = open("./problemCategories.json", "r")
categories = json.load(categories_file)


gpt.define_system_role(
    f"You are a parallel computing expert. I will provide you a source code in C or C++ and I want you to classify if there is an inefficiency problem in the code. If there is an problem, I want you to classify this problem from the following list: {categories} and return as Type: classified_type"
)

gpt.create_prompt(code)
gpt.write_conversation_to_file("inClassCode")
