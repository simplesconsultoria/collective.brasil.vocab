# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.telecom import cng

class CNG(object):
    """Vocabulary factory for area codes in Brazil.
      
      >>> from zope.component import queryUtility
      
      >>> name = 'brasil.cng'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> cng = util()
      >>> cng
      <zope.schema.vocabulary.SimpleVocabulary object at ...>
      
      >>> cng.by_token['0300']
      <zope.schema.vocabulary.SimpleTerm object at ...>
      
      >>> cng.by_token['0300'].value
      '0300'
      
      >>> cng.by_token['0300'].token
      '0300'
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context=None):
        items = [(v,k) for k,v in cng]
        return SimpleVocabulary.fromItems(items)

CNGVocabularyFactory = CNG()