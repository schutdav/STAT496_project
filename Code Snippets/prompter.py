from gpt4all import GPT4All

model = GPT4All(r"C:\Users\the40\AppData\Local\nomic.ai\GPT4All\Llama-3.2-3B-Instruct-Q4_0.gguf")
path = r"C:\Users\the40\Documents\GitHub\STAT496_project\questions_cleaned.txt"

with model.chat_session():
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines[:2]:
            tokens = line.split(sep="\t")
            polite_prompt = "Hi there, would you please help me answer the following question: " + tokens[0]
            rude_prompt = tokens[0] + "Answer quick, sucker."
            print(model.generate(tokens[0], max_tokens=50))
            print(model.generate(polite_prompt, max_tokens=50))
            print(model.generate(rude_prompt, max_tokens=50))