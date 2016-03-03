



from gensim.models import Word2Vec
from gensim.models import word2vec
import sys
import numpy as np
import heapq
import os

import evaluate

def ignore(fi):
    if os.path.isfile(fi):
        print "File "+fi+" deleted!"
        os.unlink(fi)

def main():
# sentences=None, size=100, alpha=0.025, window=5, min_count=5,
#         sample=0, seed=1, workers=1, min_alpha=0.0001, sg=1, hs=1, negative=0,
#         cbow_mean=0, hashfxn=hash, iter=1
    corp=sys.argv[1]
    goldfile=sys.argv[2]
    kop=int(sys.argv[3])
#    GORDELEKU="/gscratch/users/maguirrezaba008/vectorFiles/"
    GORDELEKU="/home/magirrezaba008/semantika/bestEmbeddings/results/"
    filename = corp.split("/")[-1]
    from configuration import confs
    sentences=word2vec.LineSentence(corp)
    resu=[]
    for conf in confs:
        strconf=[str(i) for i in conf]
        modelfilename='vectors_'+'---'.join(strconf)+'.bin'
        print "Let's start working with the file "+modelfilename
        if os.path.isfile(GORDELEKU+modelfilename):
            print modelfilename+" exists, so we don't need to train it again!"
            model=Word2Vec.load_word2vec_format(GORDELEKU+modelfilename,None, True)
            print "Loaded!"
        else:
            print "Training with "+filename+" file..."
            model = Word2Vec(sentences, conf[0], conf[1], conf[2], conf[3], conf[4], conf[5], conf[6], conf[7], conf[8], conf[9], conf[10], conf[11], conf[12], conf[13])
            print "Trained!"
        
#        model.save_word2vec_format(modelfilename, binary=True)
#        print "Saved "+modelfilename+" file..."
        (pearsoncoef, significance) = evaluate.evaluate(model, goldfile)
        print "File name: "+modelfilename
        print "Pearson coefficient and significance: "+str(pearsoncoef)+" "+str(significance)
        print

        this={}
        this['name']=modelfilename
        this['coef']=pearsoncoef
        this['significance']=significance
        if len(resu)<kop and this['significance'] < 0.05:
            resu.append(this)
            model.save_word2vec_format(GORDELEKU+modelfilename, binary=True)
            print "Saved "+modelfilename+" file..."
        elif this['significance'] < 0.05 and min(resu, key=lambda s: s['coef'])['coef']<this['coef']:
            resu.append(this)
            model.save_word2vec_format(GORDELEKU+modelfilename, binary=True)
            print "Saved "+modelfilename+" file..."
            mini=min(resu, key=lambda s: s['coef'])
            ignore(GORDELEKU+mini['name'])
            resu.remove(mini)
        else:
            ignore(GORDELEKU+this['name'])
        del(model)
        print "resu has "+str(len(resu))+" elements!"

        # if significance < 0.05:
        #     coefs.append(this)
        #     coefs=heapq.nlargest(3, coefs, key=lambda s:s['coef'])


if __name__ == '__main__':main()
