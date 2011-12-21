# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.telecom import codes

class DDD(object):
    """Vocabulary factory for area codes in Brazil.
      
      >>> from zope.component import queryUtility
      
      >>> name = 'brasil.ddd'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> ddd = util()
      >>> ddd
      <zope.schema.vocabulary.SimpleVocabulary object at ...>
      
      >>> ddd.by_token['11']
      <zope.schema.vocabulary.SimpleTerm object at ...>
      
      >>> ddd.by_token['11'].value
      '11'
      
      >>> ddd.by_token['11'].token
      '11'
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context=None):
        items = [(v,k) for k,v in codes]
        return SimpleVocabulary.fromItems(items)

DDDVocabularyFactory = DDD()