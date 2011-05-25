.. contents:: Table of Contents
   :depth: 2

collective.brasil.vocab
****************************************

Overview
--------

This is an implementation of brasil.vocab -- Brazilian vocabularies -- using 
Zope 3 vocabularies.


Requirements
------------

    * Plone >= 3.0.x (http://plone.org/products/plone)
    
Installation
------------
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``collective.brasil.vocab``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            collective.brasil.vocab

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource registries
in order to see the effects of the product installation.

Available Vocabularies
-----------------------

brasil.paises
^^^^^^^^^^^^^^^^^^^^

Provides a vocabulary containing the countries as defined by ISO-3166, but 
translated to Brazilian Portuguese.

Vocabulary tokens are the 2-letter ISO country code.

.. note:: That means we list "Estados Unidos da América" instead of 
          "United States of America"

brasil.estados
^^^^^^^^^^^^^^^^^^^^

Provides a vocabulary containing the Brazilian States (Unidades da Federação) 
with the acronym (sigla) as the vocabulary token

brasil.cidades.ibge
^^^^^^^^^^^^^^^^^^^^^^

Provides a vocabulary containing all Brazilian cities with the IBGE city code 
as vocabulary token and the title in the format *City Name (UF)*

brasil.cidades.AC
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Acre state.

brasil.cidades.AL
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Alagoas state.

brasil.cidades.AP
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Amapá state.

brasil.cidades.AM
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Amazonas state.

brasil.cidades.BA
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Bahia state.

brasil.cidades.CE
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Ceará state.

brasil.cidades.DF
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Distrito Federal state.

brasil.cidades.ES
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Espírito Santo state.

brasil.cidades.GO
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Goiás state.

brasil.cidades.MA
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Maranhão state.

brasil.cidades.MT
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Mato Grosso state.

brasil.cidades.MS
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Mato Grosso do Sul state.

brasil.cidades.MG
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Minas Gerais state.

brasil.cidades.PA
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Pará state.

brasil.cidades.PB
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Paraíba state.

brasil.cidades.PR
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Paraná state.

brasil.cidades.PE
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Pernambuco state.

brasil.cidades.PI
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Piauí state.

brasil.cidades.RJ
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Rio de Janeiro state.

brasil.cidades.RN
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Rio Grande do Norte state.

brasil.cidades.RS
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Rio Grande do Sul state.

brasil.cidades.RO
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Rondônia state.

brasil.cidades.RR
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Roraima state.

brasil.cidades.SC
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Santa Catarina state.

brasil.cidades.SP
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from São Paulo state.

brasil.cidades.SE
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Sergipe state.

brasil.cidades.TO
^^^^^^^^^^^^^^^^^^^^^^
Vocabularies providing cities from Tocantins state.

brasil.ddd
^^^^^^^^^^^^^^^^^^^^

Provides a vocabulary containing valid Brazil area codes.

Sponsoring
----------

Development of this product was sponsored by :
    
    * `TRT13 <http://www.trt13.jus.br/>`_.
    
    * `Simples Consultoria <http://www.simplesconsultoria.com.br/>`_.
    
    * `APyB <http://www.python.org.br/>`_.

Credits
-------

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation
    
