# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.geo import uf

class Estados(object):
    """Vocabulary factory for a list of estados
      
      >>> from zope.component import queryUtility
      >>> from plone.app.vocabularies.tests.base import create_context
      
      >>> name = 'brasil.estados'
      >>> util = queryUtility(IVocabularyFactory, name)
      >>> context = create_context()
      >>> estados = util(context)
      >>> estados
      <zope.schema.vocabulary.SimpleVocabulary object at ...>
      
      >>> estados.by_token['AC']
      <zope.schema.vocabulary.SimpleTerm object at ...>
      
      >>> estados.by_token['AC'].title
      u'Acre'
      
      >>> estados.by_token['AC'].token
      'AC'
      
      >>> estados.by_token['AC'].value
      'AC'
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [SimpleTerm(k,k,v) for k,v in uf]
        return SimpleVocabulary(items)

EstadosVocabularyFactory = Estados()