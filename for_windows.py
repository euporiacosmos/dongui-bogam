from sentence_transformers import SentenceTransformer, util
import numpy as np
import time

embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

app_started_time = time.time()
# dongui_bogam.txt 파일을 읽어서 \n을 기준으로 문장을 나누어 corpus에 저장
with open('dongui_bogam.txt', 'r', encoding='utf-8') as f:
    corpus = f.read().split('\n')

corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
print("소요시간: " + str(round(time.time()-app_started_time, 2)) + "초")

while True:
    # Query sentences:
    query = input("동의보감에서 찾고 싶은 내용을 입력하세요: ")

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    top_k = 5
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    cos_scores = cos_scores.cpu()

    #We use np.argpartition, to only partially sort the top_k results
    top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

    print("\n\n======================\n\n")
    print("Query:", query)
    print("\nTop 5 most similar sentences in corpus:")

    for idx in top_results[0:top_k]:
        print(corpus[idx].strip(), "(Score: %.4f)" % (cos_scores[idx]))