
"""
        円周率
        各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成
"""
if __name__ == "__main__":
    msg = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    msg = msg.replace('.', "")
    msg = msg.replace(',', "")
    word_cout = list()
    for word in msg.split(" "):
        word_cout.append(len(word))
    print(word_cout)
