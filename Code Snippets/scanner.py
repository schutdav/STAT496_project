path1 = r"C:\Users\the40\Documents\GitHub\STAT496_project\questions.txt"
#path1 = r"C:\Users\the40\AppData\Roaming\JetBrains\PyCharm2025.3\scratches\scratch.txt"
path2 = r"C:\Users\the40\Documents\GitHub\STAT496_project\questions_cleaned.txt"
#path2 = r"C:\Users\the40\AppData\Roaming\JetBrains\PyCharm2025.3\scratches\scratch2.txt"
with open(path1, 'r') as f:
    with open(path2, 'w') as f_cleaned:
        lines = f.readlines()
        for line in lines[1::2]:
            tokens = line.split(sep = "\t")
            f_cleaned.write(tokens[1] + "\t" + tokens[2] + "\n")