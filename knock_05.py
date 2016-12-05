

def make_ngram(n, gram):
    '''
    n-gramを作成する関数
    '''
    last = len(gram) - n + 1
    ret = []
    for i in range(last):
        ret.append(gram[i:i+n])
    return ret

if __name__ == "__main__":
    text = "I am an NLPer"
    # 単語bi-gram
    tango = make_ngram(2, text.split())
    print(tango)
    # 文字bi-gram
    moji = make_ngram(2, text.replace(' ', ""))
    print(moji)
