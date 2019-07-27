import pandas as pd

data = pd.read_csv("../Data/swwiki.csv", encoding="utf-8")
sentences = []
for index, row in data.iterrows():
    sentences.append(row["swahili"])
    
f = open("../Data/Combined.txt", "w+", encoding="utf-8")
f.write(str(sentences))
f.close()


