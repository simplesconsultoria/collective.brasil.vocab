# -*- coding: utf-8 -*-
import doctest
from doctest import DocTestSuite
import unittest

import zope.component
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.site import hooks

import collective.brasil.vocab

def vocabSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', collective.brasil.vocab)()
    hooks.setHooks()


def vocabTearDown(self):
    tearDown()
    hooks.resetHooks()
    hooks.setSite()


def test_suite():
    optionflags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    return unittest.TestSuite((
       DocTestSuite('collective.brasil.vocab.geo.paises',
                     setUp=vocabSetUp,
                     tearDown=vocabTearDown,
                     optionflags=optionflags),
       DocTestSuite('collective.brasil.vocab.geo.estados',
                     setUp=vocabSetUp,
                     tearDown=vocabTearDown,
                     optionflags=optionflags),
       DocTestSuite('collective.brasil.vocab.geo.cidades',
                     setUp=vocabSetUp,
                     tearDown=vocabTearDown,
                     optionflags=optionflags),
       DocTestSuite('collective.brasil.vocab.telecom.ddd',
                     setUp=vocabSetUp,
                     tearDown=vocabTearDown,
                     optionflags=optionflags),
        ))
