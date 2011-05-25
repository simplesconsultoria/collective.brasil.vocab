# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.telecom import ddd

class DDD(object):
    """ DDD
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [(v,k) for k,v in ddd]
        return SimpleVocabulary.fromItems(items)

DDDVocabularyFactory = DDD()