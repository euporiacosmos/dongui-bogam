from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
import numpy as np
import datetime, json, socket, sqlite3, struct

app = Flask(__name__)
embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")
with open("dongui-bogam.json", "r", encoding="utf-8") as file:
    dongui_bogam_dict = json.load(file)

# https://wikidocs.net/24603
def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

# https://stackoverflow.com/a/9591005
def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

@app.route('/')
def home():
    global client_ip
    global accessed_time
    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    accessed_time=datetime.datetime.now()
    return render_template('index.html')
    
@app.route('/response', methods=['GET'])
def response():
    query = request.args.get('q')
    page = int(request.args.get('page'))
    query_doc = np.array(embedder.encode(query).tolist())
    
    rank_similarity={}
    for sentence, value in dongui_bogam_dict.items():
        similarity = cos_sim(query_doc, np.array(value))
        rank_similarity[similarity]=sentence
    rank_similarity=sorted(rank_similarity.items(), reverse=True)
    
    results = [tup[1] for tup in rank_similarity[page*5-5:page*5]]
    with sqlite3.connect('./database/database.sqlite3') as conn:
        curs=conn.cursor()
        if page == 1:
            curs.execute('INSERT INTO visitor(ipv4, datetime, query, page) VALUES (?, ?, ?, ?)', (ip2long(client_ip), accessed_time, query, page))
        else:
            res = curs.execute('SELECT page FROM visitor WHERE ipv4=? AND datetime=?', (ip2long(client_ip), accessed_time)).fetchone()
            if res[0] < page:
                curs.execute('UPDATE visitor SET page=? WHERE ipv4=? AND datetime=?', (page, ip2long(client_ip), accessed_time))
        conn.commit()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1')