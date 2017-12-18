"""A process specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric aerosol emissions'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# SUB-PROCESS: Emissions
# --------------------------------------------------------------------
DETAILS['emissions'] = {
    'description': 'TO DO',
    'properties': [
        ('method', 'ENUM:emissions_methods', '0.N',
            'Method used to define aerosol species emitted at the surface (several methods allowed because the different species may not use the same method).'),
        ('sources', 'ENUM:surface_source_types', '0.N',
             'Sources of the aerosol species emitted at the surface that are taken into account in the emissions scheme'),
        ('prescribed_climatology', 'ENUM:prescribed_climatology_type', '0.1',
            'Specify the climatology type for aerosol emissions prescribed at the surface'),
        ('prescribed_climatology_emitted_species', 'str', '0.1',
             'List of aerosol species emitted at the surface and prescribed via a climatology'),
        ('prescribed_spatially_uniform_emitted_species', 'str', '0.1',
             'List of aerosol species emitted at the surface and prescribed as spatially uniform'),
        ('interactive_emitted_species', 'str', '0.1',
             'List of aerosol species emitted at the surface and specified via an interactive method'),
        ('other_emitted_species', 'str', '0.1',
             'List of aerosol species emitted at the surface and specified via an "other method"'),
        ('other_method_characteristics', 'str', '0.1',
             'Characteristics of the "other method" used for aerosol emissions at the surface'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Concentrations
# --------------------------------------------------------------------
DETAILS['concentrations'] = {
    'description': 'TO DO',
    'properties': [
        ('prescribed_lower_boundary', 'str', '0.1',
            'List of species prescribed at the lower boundary.'),
        ('prescribed_upper_boundary', 'str', '0.1',
            'List of species prescribed at the upper boundary.'),
        ('prescribed_fields_mmr', 'str', '0.1',
            'List of species prescribed as mass mixing ratios.'),
        ('prescribed_fields_mmr', 'str', '0.1',
            'List of species prescribed as AOD plus CCNs.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prescribed_climatology_type'] = {
    'description': 'Specify the climatology type for aerosol emissions',
    'is_open': False,
    'members': [
        ('Constant', None),
        ('Interannual', None),
        ('Annual', None),
        ('Monthly', None),
        ('Daily', None),
        ]
    }

ENUMERATIONS['surface_source_types'] = {
    'description':'Sources of the aerosol species emitted at the surface that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Vegetation', None),
        ('Volcanos', None),
        ('Bare ground', None),
        ('Sea surface', None),
        ('Lightning', None),
        ('Fires', None),
        ('Aircraft', None),
        ('Anthropogenic', None),
    ]
}

ENUMERATIONS['atmospheric_source_types'] = {
    'description':'Sources of the aerosol species emitted in the atmosphere that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Aircraft', None),
        ('Biomass burning', None),
        ('Lightning', None),
        ('Volcanos', None),
    ]
}

ENUMERATIONS['emissions_methods'] = {
    'description': 'Method used to define aerosol species emitted (several methods allowed because the different species may not use the same method).',
    'is_open': True,
    'members':[
        ('None', None),
        ('Prescribed (climatology)', None),
        ('Prescribed CMIP6', None),
        ('Prescribed above surface', None),
        ('Interactive', None),
        ('Interactive above surface', None),
    ]
}
