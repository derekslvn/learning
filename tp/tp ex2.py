import pprint
user_texts=[]
all_dic=[]
for i in range(10):
    user_text = input("Please enter your text: ")
    user_text=user_text.lower()
    text_words=user_text.split()
    user_texts.append(user_text)
    dic={}
    wordset=text_words
    for word in  set(text_words):
        dic[word]=text_words.count(word)
    all_dic.append(dic)
search_word=input("Please enter a word to search: ")
search_word=search_word.lower()
total_count=0
for dic in all_dic:
    if search_word in dic:
       print("Found in text:", user_texts[all_dic.index(dic)])
       
    total_count+=dic[search_word]
print("the word searched appears",total_count,"times in total")


