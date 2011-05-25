# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.geo import paises

class Paises(object):
    """Vocabulary factory for a list of countries
      
      >>> from zope.component import queryUtility
      >>> from plone.app.vocabularies.tests.base import create_context
      
      >>> name = 'brasil.paises'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> context = create_context()
      >>> paises = util(context)
      >>> paises
      <zope.schema.vocabulary.SimpleVocabulary object at ...>
      
      >>> paises.by_token['BR']
      <zope.schema.vocabulary.SimpleTerm object at ...>
      
      >>> paises.by_token['BR'].title
      u'Brasil'
      
      >>> paises.by_token['BR'].token
      'BR'
      
      >>> paises.by_token['BR'].value
      'BR'
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [SimpleTerm(k,k,v) for k,v in paises]
        return SimpleVocabulary(items)

PaisesVocabularyFactory = Paises()