from gpt4all import GPT4All

#models
model = GPT4All(r"C:\Users\pvaso\AppData\Local\nomic.ai\GPT4All\Llama-3.2-3B-Instruct-Q4_0.gguf") #Laptop
#model = GPT4All(r"C:\Users\swegi\AppData\Local\nomic.ai\GPT4All\Llama-3.2-3B-Instruct-Q4_0.gguf") #PC

#questions
#Laptop
path = r"C:\Users\pvaso\OneDrive\Desktop\STAT 496\STAT496_project-main\extracting_questions.txt"
#path = r"C:\Users\pvaso\OneDrive\Desktop\STAT 496\STAT496_project-main\questions_cleaned.txt"
#PC
#path = r"C:\Users\swegi\OneDrive\Desktop\STAT 496\STAT496_project-main\questions_cleaned.txt"
#path = r"C:\Users\swegi\OneDrive\Desktop\STAT 496\STAT496_project-main\extracting_questions.txt"

count = 0
with open(path, 'r') as fp:
    for count, _ in enumerate(fp):
        count += 1
        pass
print("Total Number of lines:", count)


normal_answers = []
polite_answers = []
rude_answers = []

instructions = (
    "INSTRUCTIONS:\n"
    "You are an answer-only model.\n"
    "Output ONLY the final answer.\n"
    "Do NOT include reasoning, explanations, or extra text.\n"
    "Do NOT restate the question.\n"
    "If you violate these rules, the response is invalid.\n\n"
    "QUESTION: "
)

with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[:count]:
        tokens = line.split(sep="\t")

        normal_prompt = instructions + tokens[0] + "\nANSWER: "
        #print(normal_prompt)
        normal_answer = model.generate(normal_prompt, max_tokens=500)
        #print(normal_answer)
        #print("\n")
        normal_answers.append(normal_answer)


        polite_prompt = instructions + "Hi there, would you please help me answer the following question: " + tokens[0] + "\n ANSWER: "
        polite_answers.append(model.generate(polite_prompt, max_tokens=500))

        rude_prompt = instructions + tokens[0] + "Answer quick, sucker." + "\n ANSWER: "
        rude_answers.append(model.generate(rude_prompt, max_tokens=500))


with open("normal_answers.txt", "w", encoding="utf-8") as f:
    for i in range(len(normal_answers)):
        f.write(normal_answers[i].strip() + "\n")

with open("polite_answers.txt", "w", encoding="utf-8") as f:
    for i in range(len(polite_answers)):
        f.write(polite_answers[i].strip() + "\n")

with open("rude_answers.txt", "w", encoding="utf-8") as f:
    for i in range(len(rude_answers)):
        f.write(rude_answers[i].strip() + "\n")
