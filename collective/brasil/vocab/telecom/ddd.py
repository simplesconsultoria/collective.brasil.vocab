# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.telecom import ddd

class DDD(object):
    """Vocabulary factory for area codes in Brazil.
      
      >>> from zope.component import queryUtility
      >>> from plone.app.vocabularies.tests.base import create_context
      
      >>> name = 'brasil.ddd'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> context = create_context()
      >>> ddd = util(context)
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
    
    def __call__(self, context):
        items = [(v,k) for k,v in ddd]
        return SimpleVocabulary.fromItems(items)

DDDVocabularyFactory = DDD()