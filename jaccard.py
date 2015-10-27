import gensim                                               #https://radimrehurek.com/gensim/
from gensim import corpora, models, similarities
import csv
import numpy
import scipy                                                #http://rpy.sourceforge.net/
import matplotlib.pyplot as plt
import rpy2
import rpy2.robjects as ro
import rpy2.robjects.lib.ggplot2 as ggplot2
from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
dbscan = importr("dbscan")

def jaccard(a,b):
    return float(len(set.intersection(*[set(a), set(b)]))/float(len(set.union(*[set(a), set(b)])))

#from txt to corpus
class MyCorpus(object):
    def __iter__(self):
        for line in open('object.txt'):
            yield dictionary.doc2bow(line.lower().split())

dictionary = corpora.Dictionary(line.lower().split() for line in open('object.txt'))
dictionary.compactify()

#export a reference dictionary to csv
with open('dictionary.csv','w', newline ='') as file:
    w = csv.writer(file)
    w.writerows(dictionary.token2id.items())
corpus_memory_friendly = MyCorpus()

#export a copy of jmat to csv
with open('jaccard.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in corpus_memory_friendly:
        jrow = []
        for j in corpus_memory_friendly:
            jrow = jrow + [jaccard(i,j)]
        writer.writerow(jrow)

mat = numpy.genfromtxt("jaccard.csv", delimiter=",")

#use loose Jaccard indices, normalize (change this to broadcasting)
for j in range(mat.shape[1]):
    for i in range(mat.shape[0]):
        if mat[i,j] != 0:
            mat[i,j] = 1
for j in range(mat.shape[1]):
    norm = numpy.sqrt(sum(numpy.square(mat[:,j])))
    for i in range(mat.shape[0]):            
        mat[i,j] = mat[i,j]/float(norm)
