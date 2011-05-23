# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.geo import cidades

class Cidades(object):
    """ Cidades
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [(v.encode('utf-8'),k) for k,v in cidades]
        return SimpleVocabulary.fromItems(items)

CidadesVocabularyFactory = Cidades()