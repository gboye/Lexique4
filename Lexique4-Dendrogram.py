#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8

'''
# Calcul des Dendrogrammes pour Lexique4
- modifié pour IMM19 sur Lex3
- modifié pour HDR sur Lex4
'''
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# %matplotlib inline

repHDR="/Users/gilles/ownCloud/Recherche/Boye/HDR/Memoire/figs/"

## Importation des résultats de Lexique4-DistributionCoFormes

# -*- coding: utf8 -*-

import pickle as pkl

with open('DendrogramDataRaw.pkl',"rb") as inFile:  # Python 3: open(..., 'rb')
    (Z,clustersLabels,lexemeLabels) = pkl.load(inFile)



# Clusterisation des distributions de fréquences

## Normalisation

def dendrogramLabels(id):
    return lexemeLabels[id]

def dendrogramClustersLabels(id):
    if id in clustersLabels:
        return ", ".join(clustersLabels[id][:5])
    else:
        return id

## Clusterisation hiérarchique => dendrogramme

import sys
# sys.getrecursionlimit()

# sys.setrecursionlimit(100000)

### Clusterisation

from scipy.cluster import hierarchy as hc

#def getLinkage(gParadigme):
#    data_raw=preparerDataRaw(gParadigme)
#    data=normaliserDataRaw(data_raw)
#    Z=hc.linkage(data,method='ward')
#    return Z

'''
### Plotter le dendrogramme sans troncation
Le dendrogramme sans troncation permet d'explorer les voisinages des différents verbes avec les distinctions maximales
'''

def plotDendrogram(Z,parType="",p=0,truncate_mode=None):
    plt.figure(figsize=(1000,1000),)
    if truncate_mode:
        leaf_label_func=dendrogramClustersLabels
        figInsert=u"-%s-%d-"%(parType,p)
    else:
        leaf_label_func=dendrogramLabels
        figInsert=u"-%s-"%(parType)

    dendrogram = hc.dendrogram(Z,
                               leaf_label_func=leaf_label_func,
                               leaf_font_size=6.,
                               p=p,truncate_mode=truncate_mode,
                              )
    print "dendrogram"
    plt.savefig(repHDR+u'Lex4-DendrogramRaw%sVerbes.pdf'%figInsert,
                dpi=300,
                format="pdf",
                bbox_inches="tight")

'''
### Récupération des clusters avec troncation
- pour obtenir les clusters, on fait appel à fcluster qui fournit un numéro de cluster pour chaque index de data
    - pour obtenir les noms des verbes, on fait la correspondance entre le numéro obtenu et lexemeLabels
    - pour obtenir les "noms" des clusters, il faut lancer dendrogram une première fois sans plot => R["ivl"]
'''

#lexemeLabels=ixVerbes
#Z=getLinkage(paradigmeFS)

#nbClusters=6000
#from scipy.cluster.hierarchy import fcluster

#plotDendrogram(Z,parType=u"Freq",p=nbClusters,truncate_mode="lastp")

plotDendrogram(Z,parType=u"Freq")
