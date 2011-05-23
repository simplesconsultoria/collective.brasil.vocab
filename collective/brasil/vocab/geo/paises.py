# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.geo import paises

class Paises(object):
    """ Paises
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [(v.encode('utf-8'),k) for k,v in paises]
        return SimpleVocabulary.fromItems(items)

PaisesVocabularyFactory = Paises()