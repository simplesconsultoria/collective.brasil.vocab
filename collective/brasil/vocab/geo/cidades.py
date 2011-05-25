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
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        items = [('%s (%s)' % (name.encode('utf-8'),uf.encode('utf-8')),k) 
                              for k,name,uf,normalized in cidades]
        return SimpleVocabulary.fromItems(items)

CidadesIBGEVocabularyFactory = CidadesIBGE()

class CidadesPorEstado(object):
    """ Base vocabulary object containing Brazilian Cities
        with the IBGE city code as vocabulary token 
        and the title in the format *City Name*
    """
    implements(IVocabularyFactory)
    
    self.uf = u''
    
    def __call__(self, context):
        item = []
        if self.uf:
            items = [(name.encode('utf-8'),k) 
                                   for k,name,normalized in cidadesPorEstado[self.uf]]
        return SimpleVocabulary.fromItems(items)


class CidadesAC(CidadesPorEstado):
    """ Vocabulary for cities from AC
    """
    implements(IVocabularyFactory)
    
    self.uf = u'AC'
    
    def __call__(self, context):
        return super(CidadesAC,self).__call__(context)

class CidadesAL(CidadesPorEstado):
    """ Vocabulary for cities from AL
    """
    implements(IVocabularyFactory)
    
    self.uf = u'AL'
    
    def __call__(self, context):
        return super(CidadesAL,self).__call__(context)

class CidadesAP(CidadesPorEstado):
    """ Vocabulary for cities from AP
    """
    implements(IVocabularyFactory)
    
    self.uf = u'AP'
    
    def __call__(self, context):
        return super(CidadesAP,self).__call__(context)

class CidadesAM(CidadesPorEstado):
    """ Vocabulary for cities from AM
    """
    implements(IVocabularyFactory)
    
    self.uf = u'AM'
    
    def __call__(self, context):
        return super(CidadesAM,self).__call__(context)

class CidadesBA(CidadesPorEstado):
    """ Vocabulary for cities from BA
    """
    implements(IVocabularyFactory)
    
    self.uf = u'BA'
    
    def __call__(self, context):
        return super(CidadesBA,self).__call__(context)

class CidadesCE(CidadesPorEstado):
    """ Vocabulary for cities from CE
    """
    implements(IVocabularyFactory)
    
    self.uf = u'CE'
    
    def __call__(self, context):
        return super(CidadesCE,self).__call__(context)

class CidadesDF(CidadesPorEstado):
    """ Vocabulary for cities from DF
    """
    implements(IVocabularyFactory)
    
    self.uf = u'DF'
    
    def __call__(self, context):
        return super(CidadesDF,self).__call__(context)

class CidadesES(CidadesPorEstado):
    """ Vocabulary for cities from ES
    """
    implements(IVocabularyFactory)
    
    self.uf = u'ES'
    
    def __call__(self, context):
        return super(CidadesES,self).__call__(context)

class CidadesGO(CidadesPorEstado):
    """ Vocabulary for cities from GO
    """
    implements(IVocabularyFactory)
    
    self.uf = u'GO'
    
    def __call__(self, context):
        return super(CidadesGO,self).__call__(context)

class CidadesMA(CidadesPorEstado):
    """ Vocabulary for cities from MA
    """
    implements(IVocabularyFactory)
    
    self.uf = u'MA'
    
    def __call__(self, context):
        return super(CidadesMA,self).__call__(context)

class CidadesMT(CidadesPorEstado):
    """ Vocabulary for cities from MT
    """
    implements(IVocabularyFactory)
    
    self.uf = u'MT'
    
    def __call__(self, context):
        return super(CidadesMT,self).__call__(context)

class CidadesMS(CidadesPorEstado):
    """ Vocabulary for cities from MS
    """
    implements(IVocabularyFactory)
    
    self.uf = u'MS'
    
    def __call__(self, context):
        return super(CidadesMS,self).__call__(context)

class CidadesMG(CidadesPorEstado):
    """ Vocabulary for cities from MG
    """
    implements(IVocabularyFactory)
    
    self.uf = u'MG'
    
    def __call__(self, context):
        return super(CidadesMG,self).__call__(context)

class CidadesPA(CidadesPorEstado):
    """ Vocabulary for cities from PA
    """
    implements(IVocabularyFactory)
    
    self.uf = u'PA'
    
    def __call__(self, context):
        return super(CidadesPA,self).__call__(context)

class CidadesPB(CidadesPorEstado):
    """ Vocabulary for cities from PB
    """
    implements(IVocabularyFactory)
    
    self.uf = u'PB'
    
    def __call__(self, context):
        return super(CidadesPB,self).__call__(context)

class CidadesPR(CidadesPorEstado):
    """ Vocabulary for cities from PR
    """
    implements(IVocabularyFactory)
    
    self.uf = u'PR'
    
    def __call__(self, context):
        return super(CidadesPR,self).__call__(context)

class CidadesPE(CidadesPorEstado):
    """ Vocabulary for cities from PE
    """
    implements(IVocabularyFactory)
    
    self.uf = u'PE'
    
    def __call__(self, context):
        return super(CidadesPE,self).__call__(context)

class CidadesPI(CidadesPorEstado):
    """ Vocabulary for cities from PI
    """
    implements(IVocabularyFactory)
    
    self.uf = u'PI'
    
    def __call__(self, context):
        return super(CidadesPI,self).__call__(context)

class CidadesRJ(CidadesPorEstado):
    """ Vocabulary for cities from RJ
    """
    implements(IVocabularyFactory)
    
    self.uf = u'RJ'
    
    def __call__(self, context):
        return super(CidadesRJ,self).__call__(context)

class CidadesRN(CidadesPorEstado):
    """ Vocabulary for cities from RN
    """
    implements(IVocabularyFactory)
    
    self.uf = u'RN'
    
    def __call__(self, context):
        return super(CidadesRN,self).__call__(context)

class CidadesRS(CidadesPorEstado):
    """ Vocabulary for cities from RS
    """
    implements(IVocabularyFactory)
    
    self.uf = u'RS'
    
    def __call__(self, context):
        return super(CidadesRS,self).__call__(context)

class CidadesRO(CidadesPorEstado):
    """ Vocabulary for cities from RO
    """
    implements(IVocabularyFactory)
    
    self.uf = u'RO'
    
    def __call__(self, context):
        return super(CidadesRO,self).__call__(context)

class CidadesRR(CidadesPorEstado):
    """ Vocabulary for cities from RR
    """
    implements(IVocabularyFactory)
    
    self.uf = u'RR'
    
    def __call__(self, context):
        return super(CidadesRR,self).__call__(context)

class CidadesSC(CidadesPorEstado):
    """ Vocabulary for cities from SC
    """
    implements(IVocabularyFactory)
    
    self.uf = u'SC'
    
    def __call__(self, context):
        return super(CidadesSC,self).__call__(context)

class CidadesSP(CidadesPorEstado):
    """ Vocabulary for cities from SP
    """
    implements(IVocabularyFactory)
    
    self.uf = u'SP'
    
    def __call__(self, context):
        return super(CidadesSP,self).__call__(context)

class CidadesSE(CidadesPorEstado):
    """ Vocabulary for cities from SE
    """
    implements(IVocabularyFactory)
    
    self.uf = u'SE'
    
    def __call__(self, context):
        return super(CidadesSE,self).__call__(context)

class CidadesTO(CidadesPorEstado):
    """ Vocabulary for cities from TO
    """
    implements(IVocabularyFactory)
    
    self.uf = u'TO'
    
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
