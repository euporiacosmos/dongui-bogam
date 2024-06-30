import requests
import time

def scrape(book_number, start_index, end_index, data):
    flag = 0
    for i in range(start_index, end_index+1):
        if flag == 0:
            res = requests.get("https://mediclassics.kr/books/8/volume/" + str(book_number) + "/content?up_content_seq=" + str(i))
            if res.status_code == 502: # 서버가 터졌을 때
                main() # 처음부터 다시 스크래핑
            else:
                response = res.json() 
                for j in range(0, len(response)):
                    if response[j]['content_level'] == 'Z' or response[j]['content_level'] == 'S':
                        data += response[j]['ko'].replace(r"<span[^>]*>", "(").replace("</span>", ")").replace("\n", "") + "\n"
                        flag += 1
                print("https://mediclassics.kr/books/8/volume/" + str(book_number) + "/content?up_content_seq=" + str(i) + " scrape complete\nCurrent Progress: " + str(i) + "/" + str(end_index))
        else:
            flag -= 1
    print("https://mediclassics.kr/books/8/volume/" + str(book_number) + " scrape complete")
    return data

def main():
    start_time = time.time()
    data = scrape(1, 132, 1244, "")
    data = scrape(2, 2, 1410, data)
    data = scrape(3, 2, 1774, data)
    data = scrape(4, 2, 1486, data)
    data = scrape(5, 2, 1505, data)
    data = scrape(6, 2, 1537, data)
    data = scrape(7, 2, 1924, data)
    data = scrape(8, 2, 1431, data)
    data = scrape(9, 2, 1106, data)
    data = scrape(10, 2, 1442, data)
    data = scrape(11, 2, 1537, data)
    data = scrape(12, 2, 1145, data)
    data = scrape(13, 2, 1271, data)
    data = scrape(14, 2, 1463, data)
    data = scrape(15, 2, 1217, data)
    data = scrape(16, 2, 1221, data)
    data = scrape(17, 2, 1243, data)
    data = scrape(18, 2, 1183, data)
    data = scrape(19, 2, 1836, data)
    data = scrape(20, 2, 2025, data)
    data = scrape(21, 2, 1533, data)
    data = scrape(22, 2, 1587, data)
    data = scrape(23, 2, 1755, data)
    # data를 텍스트 파일로 저장
    with open("dongui-bogam.txt", "w", encoding="utf-8") as f:
        f.write(data.rstrip()) # 끝에 있는 \n 제거
    print("Total spend time: "+str(round(time.time()-start_time, 2))+"sec") # 리눅스 호환성을 위해 영어로 출력
    
if __name__ == '__main__':
    main()