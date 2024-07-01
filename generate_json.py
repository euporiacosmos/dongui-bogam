import time
import json
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

start_time = time.time()
# dongui-bogam.txt 파일을 읽어서 \n을 기준으로 문장을 나누어 corpus에 저장
with open('dongui-bogam.txt',  'r', encoding='utf-8') as f:
    corpus = f.read().split('\n')

corpus_embeddings_list = embedder.encode(corpus).tolist()

data = {}
for i, sentence in enumerate(corpus):
    data[sentence] = corpus_embeddings_list[i]

with open("dongui-bogam.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

print(f"Total spend time: {round(time.time()-start_time, 2)} sec")