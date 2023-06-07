import openai, json, os


class GptApi:
    def __init__(self):
        self.conversation = []
        self.model = "gpt-3.5-turbo"
        openai.api_key = ""  # insert OpenAI API key here
        self.roleToLogName = {
            "system": "System Role",
            "user": "User",
            "assistant": "ChatGPT",
        }

    def define_system_role(self, content):
        self.conversation.append({"role": "system", "content": content})

    def create_prompt(self, prompt):
        self.conversation.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(
            model=self.model, messages=self.conversation
        )
        response = completion.choices[0].message.content
        self.conversation.append({"role": "assistant", "content": response})

    def start_conversation(self):  # to start a chat session with GPT on terminal
        system_role = input("Define a system role for the conversation: ")
        self.define_system_role(system_role)
        while True:
            prompt = input("You: ")

            if prompt == "exit":
                break

            self.create_prompt(prompt)
            print(f"ChatGPT: {self.conversation[-1]['content']}")

        print("ChatGPT: Thanks for the conversation!")

    def write_conversation_to_file(self, file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        conversation_text = open(f"{file_path}/conversation.txt", "w")
        conversation_json_file = open(f"{file_path}/conversation.json", "w")
        conversation_dict = {"messages": []}

        for message in self.conversation:
            conversation_text.write(
                f"{self.roleToLogName[message['role']]}: {message['content']} \n"
            )
            conversation_dict["messages"].append(message)

        conversation_text.close()
        conversation_json = json.dumps(conversation_dict)
        conversation_json_file.write(conversation_json)
        conversation_json_file.close()

    def clear_conversation(self):
        self.conversation = []
