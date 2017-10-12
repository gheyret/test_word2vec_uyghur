#coding=utf-8

import gensim

def makeNewUyghur():
    hojjet = 'uyghur_pakiz.txt'
    with open(hojjet,'r',encoding='utf-8') as rd:
       sozler=[soz.strip().split(' ') for soz in rd.readlines()]
    model = gensim.models.Word2Vec(sozler, size=100, window=5, min_count=5, workers=6)
    return model

def printOxshash(soz, model):
    oxshash = model.wv.similar_by_word(soz)
    print("%s:"%soz)
    for osoz in oxshash:
        #print('%s -> %f' % (soz[0],soz[1]))
        print('\t%s' % (osoz[0]))

def printAllOxshash(model):
    for soz in model.wv.vocab:
        print("%s:"%soz)
        oxshash = model.wv.similar_by_word(soz)
        for osoz in oxshash:
            print('\t%s' % (osoz[0]))
        print("")

def printInfo(model):
    print('Soz sani = %d' % len(model.wv.vocab.keys()))

#model=makeNewUyghur()
#model.save('uyghur_pakiz.model')

model = gensim.models.Word2Vec.load('uyghur_pakiz.model')
printInfo(model)

soz = 'قەشقەر'
printOxshash(soz,model)

