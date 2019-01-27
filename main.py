import jieba
import collections


fuhao = "01234567890!@#$%^&*()-=_+][{}':;/?.>,<~》《，。/？‘；】【{}：“|\"”〔〕（）、"
fuci = "的等地得而了在是我有和就不人都一个上也很到说要去你会着看好这"


with open("./demo.txt", "r", encoding="utf-8") as f:
    all_words = []
    for txt in f.readlines():
        if len(txt.strip()) != 0:
            all_words.extend([one for one in list(jieba.cut(txt))
                              if len(one.strip()) != 0 and one not in fuhao and one not in fuci])
            pass
        pass

    counter = dict(collections.Counter(all_words))
    result = sorted(counter.items(), key=lambda c: c[1], reverse=True)

    with open("./out.txt", "w", encoding="utf-8") as f:
        for result_one in result:
            f.writelines("{} {}\n".format(result_one[0], result_one[1]))
            pass
        pass

    pass
