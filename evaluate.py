
from gensim.models import Word2Vec
from gensim.models import word2vec
# from scipy.stats import pearsonr
from scipy.stats import spearmanr

def openGold(fi):
    f=open(fi)
    couples={}
    for line in f:
        els=line.rstrip().split("\t")
        couples[els[0]+"\t"+els[1]]=float(els[2])
    f.close()
    return couples

def evaluatefile(modelfile, gold):
    model=Word2Vec.load_word2vec_format(modelfile,None, True)
    goldCouples=openGold(gold)
    modelCouples={}
    for el in goldCouples:
        el1,el2=el.split("\t")
        #This is not the best solution...
        try:
            # print el1, el2, model.similarity(el1, el2)
            modelCouples[el1+"\t"+el2]=model.similarity(el1, el2)
        except KeyError:
            continue
            # print "poo", el1, el2
            # modelCouples[el1+"\t"+el2]=random.uniform(-1, 1)

    goldlist=[]
    modellist=[]
    for i in modelCouples.keys():
        goldlist.append(goldCouples[i])
        modellist.append(modelCouples[i])
    return spearmanr(goldlist, modellist)

def evaluate(model, gold):
    goldCouples=openGold(gold)
    modelCouples={}
    for el in goldCouples:
        el1,el2=el.split("\t")
        #This is not the best solution...
        try:
            # print el1, el2, model.similarity(el1, el2)
            modelCouples[el1+"\t"+el2]=model.similarity(el1, el2)
        except KeyError:
            continue
            # print "poo", el1, el2
            # modelCouples[el1+"\t"+el2]=random.uniform(-1, 1)

    goldlist=[]
    modellist=[]
    for i in modelCouples.keys():
        goldlist.append(goldCouples[i])
        modellist.append(modelCouples[i])
    return spearmanr(goldlist, modellist)

def main():
    import sys
    print evaluatefile(sys.argv[1], sys.argv[2])

if __name__ == '__main__':main()
