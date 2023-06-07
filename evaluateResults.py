import json, os

categories_file = open("./commits.json", "r")
commit_list = json.load(categories_file)["commits"]


classification_folders = [
    "codes_conversations_with_none",
    "codes_conversations_without_none",
    "codes_spaceless_conversations_with_none",
    "codes_spaceless_conversations_without_none",
    "codes_preprocessed_conversations_with_none",
    "codes_preprocessed_conversations_without_none",
]

for folder in classification_folders:
    number_of_folders_with_response = 0
    number_of_none_response = 0
    number_of_non_none_response = 0
    number_of_total_response = 0
    number_of_wrong_format_responses = 0
    number_of_wrong_responses = 0
    number_of_correct_responses = 0
    log = open(f"{folder}.txt", "w")
    for commit in commit_list:
        folder_idx = commit["Code Folder Index"]
        response_folder_path = f"{folder}/{folder_idx}"
        classification_list = []

        for folder_name in os.listdir(response_folder_path):
            conversation_subfolder_path = f"{response_folder_path}/{folder_name}"
            try:
                conversation_file = open(
                    f"{conversation_subfolder_path}/conversation.json", "r"
                )
                conversation = json.load(conversation_file)["messages"]
                classification = conversation[-1]["content"].strip().replace(".", "")
                if classification[:5] == "Type:":
                    classification_list.append(classification[6:])
                else:
                    number_of_wrong_format_responses += 1
            except:
                pass

        if len(classification_list) != 0:
            number_of_folders_with_response += 1
            print(number_of_folders_with_response)
        correct_classification = commit["Sub-Category"]
        correct_response_found = False
        log.write(
            f"Folder Index: {folder_idx}\t||\tCategory: {correct_classification}\t||\tClassification List: {classification_list}\n"
        )
        all_none_answers = True
        for element in classification_list:
            if element.lower() != "none":
                all_none_answers = False
            if element.lower() == correct_classification.lower():
                number_of_correct_responses += 1
                break

        if len(classification_list) != 0 and all_none_answers:
            number_of_none_response += 1

    log.write("\n-------------------------------\n")
    log.write(f"Number of all the commits: 185\n")
    log.write(f"Number of commits with response: {number_of_folders_with_response}\n")
    log.write(
        f"Number of commits with no response: {185 - number_of_folders_with_response}\n\n"
    )
    log.write(f"Number of None response: {number_of_none_response}\n")
    log.write(
        f"Number of non-None response: {number_of_folders_with_response - number_of_none_response}\n"
    )
    log.write(f"Number of correct response: {number_of_correct_responses}\n")
    log.write(
        f"Number of wrong response: {number_of_folders_with_response - number_of_none_response - number_of_correct_responses}\n"
    )
    log.write(f"Number of wrong format response: {number_of_wrong_format_responses}")
