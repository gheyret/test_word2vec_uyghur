#coding=utf-8

import gensim
import os

#hojjet = 'F:\\gheyret\\Imla\\uspell\\ambarlar\\2017\\xjradio201710.uut'
hojjet = 'uyghur_pakiz.txt'
modelname = 'uyghur_pakiz.model'

def Pakizla(hojjetati):
    uyghur_char=['ئ','ا','ب','ت','ج','خ','د','ر','ز','س','ش','غ','ف','ق','ك','ل','م','ن','و','ى','ي','پ','چ','ژ','ڭ','گ','ھ','ۆ','ۇ','ۈ','ۋ','ې','ە','ﻻ']
    sozler = []
    tekraryoq={}
    sani = 0
    with open(hojjetati,'r',encoding='utf-8') as rd:
        #sozler=[soz.strip().split(' ') for soz in rd.readlines()]
        for qur in rd.readlines():
            qur = qur.strip()
            yengiqur=''
            for herp in qur:
                if herp in uyghur_char:
                    yengiqur += herp
                else:
                    yengiqur += ' '
            while '  ' in yengiqur:
                yengiqur = yengiqur.replace('  ',' ')
            
            tekraryoq[yengiqur] = sani
            sani = sani +1
        
        print(' %d ' % sani,end='')
        print(' -> %d' % len(tekraryoq),end='')
        for yengiqur , sani in tekraryoq.items():
            sozler.append(yengiqur.strip().split(' '))
            
    return sozler

def makeNewUyghur(hojjetati):
    print('Hojjet "%s" ni \n\tpakizlawatidu...' % hojjet,end='')
    sozler = Pakizla(hojjetati)
    print('\tPakizlap boldi')

    print('\tOginiwatidu...',end='')
    model = gensim.models.Word2Vec(sozler, size=100, window=5, min_count=5, workers=6)
    print('\toginip boldi')
    return model

def printOxshash(soz, model):
    oxshash = model.wv.similar_by_word(soz,  topn=10)
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

if os.path.exists(modelname):
    model = gensim.models.Word2Vec.load(modelname)
else:
    model=makeNewUyghur(hojjet)
    model.save(modelname)

printInfo(model)

soz = 'گۈزەل'
printOxshash(soz,model)

soz = 'قىز'
printOxshash(soz,model)
