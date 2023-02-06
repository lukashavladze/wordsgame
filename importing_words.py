from bs4 import BeautifulSoup
import requests

geo_words_list = []
geo_words_dict = {}

geo_words_list2 = []
# print(type(geo_words_dict))

url = "https://www.orthodoxy.ge/tsnobarebi/leksikoni_dz.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('p')
# print(results)
for result in results:
    name = result.text
    geo_words_list.append(name)
# print(geo_words_list)
# print("*" * 60)
for list in geo_words_list:
    data = list.split(" ", 1)
    geo_words_list2.append(data[0])
    # print(data)
    # data1 = data[0]
    # print(data1)
    geo_words_dict[data[0]] = data[1]
# print(geo_words_dict)

# print(geo_words_list2)


    # for key, value in data:
    #     data[0] = key
    #     data[1] = value
    #     geo_words_dict[key] = value
    #     print(geo_words_dict)






# with open("wordss.txt", 'r', encoding="utf-8") as words:
#     for word in words:
#         print(word, end=' ')
#         # print(data)



