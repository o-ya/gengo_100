
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
    text1 = "paraparaparadise"
    text2 = "paragraph"
    X = set(make_ngram(2, text1))
    Y = set(make_ngram(2, text2))
    # 和集合
    print(X.union(Y))
    # 積集合
    print(X.intersection(Y))
    # 差集合
    print(X.difference(Y))
    han = "se"
    print(han in X)
    print(han in Y)
