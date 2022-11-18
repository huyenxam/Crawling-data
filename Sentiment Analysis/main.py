from underthesea import pos_tag, sentiment
import string
import csv
import codecs


def predict_sentiment(sentence):
    result = sentiment(sentence)
    if result is None:
        result = "neutral"
    
    return result

def predict_entity(sentence):
    result = pos_tag(sentence)
    words = []
    for item in result:
        if item[1] == "N" or item[1] == "Np" or item[1] == "Nc" or item[1] == "Nu":
            words.append(item[0])
    
    return words


def normalize_sentence(s):

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return remove_punc(lower(s))


def sentiment_entity(path):
    comments = []
    count_label = {'negative': 0, 'neutral': 0, 'positive': 0}
    count_word = {}


    with open(path, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        comments.append(next(csv_reader))
        for row in csv_reader:
            # predict sentiment
            predict = predict_sentiment(row[4])
            row[3] = predict
            comments.append(row)
            count_label[predict] += 1

        # predict entity
        entity_list = predict_entity(row[4])
        for item in entity_list:
            s = normalize_sentence(item)
            if s not in count_word.keys():
                count_word[s] = 1
            else:
                count_word[s] +=1

    posts = codecs.open(path, 'w', 'utf-8')
    with posts:
        writer = csv.writer(posts)
        writer.writerows(comments)

    return count_label, count_word


sentiment_entity("E:/Ngọc Huyền/Crawling data/data/comments.csv")