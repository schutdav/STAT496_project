from gpt4all import GPT4All

model = GPT4All(r"C:\Users\pvaso\AppData\Local\nomic.ai\GPT4All\Llama-3.2-3B-Instruct-Q4_0.gguf")
#path = r"C:\Users\pvaso\OneDrive\Desktop\STAT 496\STAT496_project-main\extracting_questions.txt"
path = r"C:\Users\pvaso\OneDrive\Desktop\STAT 496\STAT496_project-main\questions_cleaned.txt"


questions = []
normal_answers = []
polite_answers = []
rude_answers = []

curr_question = 1

instructions = "You are a chatbot. Do not provide your reasoning, just the final answer."
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[:36]:
        tokens = line.split(sep="\t")
        questions.append(tokens[0])

        normal_prompt = instructions + tokens[0]
        polite_prompt = instructions + "Hi there, would you please help me answer the following question: " + tokens[0]
        rude_prompt = instructions + tokens[0] + "Answer quick, sucker."
        normal_answers.append(model.generate(normal_prompt, max_tokens=500))
        polite_answers.append(model.generate(polite_prompt, max_tokens=500))
        rude_answers.append(model.generate(rude_prompt, max_tokens=500))
        print("Done generating answers for Question " + str(curr_question))

        curr_question += 1

def printAnswers (q, a):
    for i in range(0,len(q)):
        print("Question " + str(i) + ": " + q[i])
        print("Answer: " + a[i])
        print()

printAnswers(questions, normal_answers)50))
