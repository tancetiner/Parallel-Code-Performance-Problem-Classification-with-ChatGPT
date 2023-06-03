import json, os, shutil, time
from GithubApi import GithubApi


commit_json = open("./commits.json", "r")
commit_dict = json.load(commit_json)
commit_json.close()
commit_list: list = commit_dict["commits"]

github = GithubApi()

# uncomment first to remove all sub-directories and files in codes directory
# codes_dir = "./codes"
# for files in os.listdir(codes_dir):
#     path = os.path.join(codes_dir, files)
#     try:
#         shutil.rmtree(path)
#     except OSError:
#         os.remove(path)
# ---------------------------------


for commit in commit_list:
    commit_url = commit["Link to commit"]
    commit_info = github.get_commit_info(commit_url)
    commit_code_idx = commit["Code Folder Index"]
    try:
        commit_files = commit_info["files"]
    except:
        print(f"Could not find commit files for: {commit_url}")
        continue

    parent_commit_sha = commit_info["parents"][0]["sha"]
    owner_name, repo_name = github.get_owner_and_repo_name(commit_url)
    repo = github.get_repo(owner_name, repo_name)
    folderPath = f"./codes/{commit_code_idx}"

    if not os.path.exists(folderPath):
        print(f"Creating {folderPath}")
        os.makedirs(folderPath)

    for file in commit_files:
        filepath = file["filename"]
        print(f"Filepath: {filepath}")
        try:
            file_contents = repo.get_contents(filepath, ref=parent_commit_sha)
            filename = filepath.split("/")[-1]

            with open(f"{folderPath}/{filename}.txt", "w") as f:
                print(f"Writing contents for {filename}")
                f.write(file_contents.decoded_content.decode("utf-8"))
        except:
            print("Could not find file contents for:", filepath)

    time.sleep(1)
