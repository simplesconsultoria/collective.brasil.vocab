# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from brasil.vocab.geo import cidades
from brasil.vocab.geo import cidadesPorEstado

class CidadesIBGE(object):
    """ Vocabulary containing Brazilian Cities
        with the IBGE city code as vocabulary token 
        and the title in the format *City Name (UF)*
        
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context
        
        >>> name = 'brasil.cidades.ibge'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
        
        >>> cidades.by_token['4202909']
        <zope.schema.vocabulary.SimpleTerm object at ...>
        
        >>> cidades.by_token['4202909'].title
        u'Brusque (SC)'
        
        >>> cidades.by_token['4202909'].token
        '4202909'
        
        >>> cidades.by_token['4202909'].value
        4202909
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [SimpleTerm(k,k,'%s (%s)' % (name,uf)) 
                              for k,name,uf,normalized in cidades]
        return SimpleVocabulary(items)

CidadesIBGEVocabularyFactory = CidadesIBGE()

class CidadesPorEstado(object):
    """ Base vocabulary object containing Brazilian Cities
        with the IBGE city code as vocabulary token 
        and the title in the format *City Name*
    """
    implements(IVocabularyFactory)
    
    uf = u''
    
    def __call__(self, context):
        item = []
        if self.uf:
            items = [(name.encode('utf-8'),k) 
                                   for k,name,normalized in cidadesPorEstado[self.uf]]
        return SimpleVocabulary.fromItems(items)


class CidadesAC(CidadesPorEstado):
    """ Vocabulary for cities from Acre
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.AC'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'AC'

    def __call__(self, context):
        return super(CidadesAC,self).__call__(context)


class CidadesAL(CidadesPorEstado):
    """ Vocabulary for cities from Alagoas
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.AL'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'AL'

    def __call__(self, context):
        return super(CidadesAL,self).__call__(context)


class CidadesAP(CidadesPorEstado):
    """ Vocabulary for cities from Amapá
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.AP'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'AP'

    def __call__(self, context):
        return super(CidadesAP,self).__call__(context)


class CidadesAM(CidadesPorEstado):
    """ Vocabulary for cities from Amazonas
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.AM'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'AM'

    def __call__(self, context):
        return super(CidadesAM,self).__call__(context)


class CidadesBA(CidadesPorEstado):
    """ Vocabulary for cities from Bahia
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.BA'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'BA'

    def __call__(self, context):
        return super(CidadesBA,self).__call__(context)


class CidadesCE(CidadesPorEstado):
    """ Vocabulary for cities from Ceará
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.CE'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'CE'

    def __call__(self, context):
        return super(CidadesCE,self).__call__(context)


class CidadesDF(CidadesPorEstado):
    """ Vocabulary for cities from Distrito Federal
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.DF'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'DF'

    def __call__(self, context):
        return super(CidadesDF,self).__call__(context)


class CidadesES(CidadesPorEstado):
    """ Vocabulary for cities from Espírito Santo
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.ES'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'ES'

    def __call__(self, context):
        return super(CidadesES,self).__call__(context)


class CidadesGO(CidadesPorEstado):
    """ Vocabulary for cities from Goiás
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.GO'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'GO'

    def __call__(self, context):
        return super(CidadesGO,self).__call__(context)


class CidadesMA(CidadesPorEstado):
    """ Vocabulary for cities from Maranhão
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.MA'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'MA'

    def __call__(self, context):
        return super(CidadesMA,self).__call__(context)


class CidadesMT(CidadesPorEstado):
    """ Vocabulary for cities from Mato Grosso
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.MT'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'MT'

    def __call__(self, context):
        return super(CidadesMT,self).__call__(context)


class CidadesMS(CidadesPorEstado):
    """ Vocabulary for cities from Mato Grosso do Sul
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.MS'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'MS'

    def __call__(self, context):
        return super(CidadesMS,self).__call__(context)


class CidadesMG(CidadesPorEstado):
    """ Vocabulary for cities from Minas Gerais
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.MG'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'MG'

    def __call__(self, context):
        return super(CidadesMG,self).__call__(context)


class CidadesPA(CidadesPorEstado):
    """ Vocabulary for cities from Pará
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.PA'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'PA'

    def __call__(self, context):
        return super(CidadesPA,self).__call__(context)


class CidadesPB(CidadesPorEstado):
    """ Vocabulary for cities from Paraíba
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.PB'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'PB'

    def __call__(self, context):
        return super(CidadesPB,self).__call__(context)


class CidadesPR(CidadesPorEstado):
    """ Vocabulary for cities from Paraná
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.PR'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'PR'

    def __call__(self, context):
        return super(CidadesPR,self).__call__(context)


class CidadesPE(CidadesPorEstado):
    """ Vocabulary for cities from Pernambuco
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.PE'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'PE'

    def __call__(self, context):
        return super(CidadesPE,self).__call__(context)


class CidadesPI(CidadesPorEstado):
    """ Vocabulary for cities from Piauí
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.PI'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'PI'

    def __call__(self, context):
        return super(CidadesPI,self).__call__(context)


class CidadesRJ(CidadesPorEstado):
    """ Vocabulary for cities from Rio de Janeiro
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.RJ'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'RJ'

    def __call__(self, context):
        return super(CidadesRJ,self).__call__(context)


class CidadesRN(CidadesPorEstado):
    """ Vocabulary for cities from Rio Grande do Norte
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.RN'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'RN'

    def __call__(self, context):
        return super(CidadesRN,self).__call__(context)


class CidadesRS(CidadesPorEstado):
    """ Vocabulary for cities from Rio Grande do Sul
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.RS'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'RS'

    def __call__(self, context):
        return super(CidadesRS,self).__call__(context)


class CidadesRO(CidadesPorEstado):
    """ Vocabulary for cities from Rondônia
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.RO'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'RO'

    def __call__(self, context):
        return super(CidadesRO,self).__call__(context)


class CidadesRR(CidadesPorEstado):
    """ Vocabulary for cities from Roraima
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.RR'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'RR'

    def __call__(self, context):
        return super(CidadesRR,self).__call__(context)


class CidadesSC(CidadesPorEstado):
    """ Vocabulary for cities from Santa Catarina
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.SC'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'SC'

    def __call__(self, context):
        return super(CidadesSC,self).__call__(context)


class CidadesSP(CidadesPorEstado):
    """ Vocabulary for cities from São Paulo
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.SP'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'SP'

    def __call__(self, context):
        return super(CidadesSP,self).__call__(context)


class CidadesSE(CidadesPorEstado):
    """ Vocabulary for cities from Sergipe
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.SE'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'SE'

    def __call__(self, context):
        return super(CidadesSE,self).__call__(context)


class CidadesTO(CidadesPorEstado):
    """ Vocabulary for cities from Tocantins
        >>> from zope.component import queryUtility
        >>> from plone.app.vocabularies.tests.base import create_context

        >>> name = 'brasil.cidades.TO'
        >>> util = queryUtility(IVocabularyFactory, name)
        >>> context = create_context()
        >>> cidades = util(context)
        >>> cidades
        <zope.schema.vocabulary.SimpleVocabulary object at ...>
    """
    implements(IVocabularyFactory)

    uf = u'TO'

    def __call__(self, context):
        return super(CidadesTO,self).__call__(context)


# By State vocabs
CidadesACVocabularyFactory = CidadesAC()
CidadesALVocabularyFactory = CidadesAL()
CidadesAMVocabularyFactory = CidadesAM()
CidadesAPVocabularyFactory = CidadesAP()
CidadesBAVocabularyFactory = CidadesBA()
CidadesCEVocabularyFactory = CidadesCE()
CidadesDFVocabularyFactory = CidadesDF()
CidadesESVocabularyFactory = CidadesES()
CidadesGOVocabularyFactory = CidadesGO()
CidadesMAVocabularyFactory = CidadesMA()
CidadesMGVocabularyFactory = CidadesMG()
CidadesMSVocabularyFactory = CidadesMS()
CidadesMTVocabularyFactory = CidadesMT()
CidadesPAVocabularyFactory = CidadesPA()
CidadesPBVocabularyFactory = CidadesPB()
CidadesPEVocabularyFactory = CidadesPE()
CidadesPIVocabularyFactory = CidadesPI()
CidadesPRVocabularyFactory = CidadesPR()
CidadesRJVocabularyFactory = CidadesRJ()
CidadesRNVocabularyFactory = CidadesRN()
CidadesROVocabularyFactory = CidadesRO()
CidadesRRVocabularyFactory = CidadesRR()
CidadesRSVocabularyFactory = CidadesRS()
CidadesSCVocabularyFactory = CidadesSC()
CidadesSEVocabularyFactory = CidadesSE()
CidadesSPVocabularyFactory = CidadesSP()
CidadesTOVocabularyFactory = CidadesTO()
