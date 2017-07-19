# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

# path to expor file
# keep in mind that if path does not exist - log file won't be created
LOGFILENAME = '/python/game/asset_rule/asset_rule.log'


# setting debug level, uncomment required debug
DEBUGS = [
    'file',  # debugging in files, set log path first
    'udp',  # UDP debug, sending
    'echo',  # printing debug to server console
    'ingame'  # printing debug ingame
]

DEBUGS_DEFAULT = [
    #'file', # debugging in files, set log path first
    #'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
]

LIMITED_SQUADS = [
    'CAS',
    'TANK',
    'TRANS',
    ]

SQUAD_NAMES = {
    'jet' : ['CAS'],
    'tnk' : ['TANK'],
    'the' : ['TRANS', 'CAS']
    }

ASSETS = {
    'jet' : [
        'arg_jet_a1h',
        'arg_jet_a4b',
        'arg_jet_a4c',
        'arg_jet_a4q',
        'arg_jet_dagger',
        'arg_jet_dagger_cas',
        'arg_jet_mirage3ea',
        'arg_jet_mirage3ea_as',
        'cf_jet_cf18',
        'cf_jet_cf18_cas',
        'ch_ahe_z10',
        'ch_ahe_z9wa_23mm_guns',
        'ch_ahe_z9wa_hf25',
        'ch_ahe_z9wa_hf7d',
        'ch_ahe_z9wa_hj8',
        'ch_jet_fantan',
        'ch_jet_j10',
        'ch_jet_su30',
        'fr_ahe_tiger',
        'gb_ahe_apache',
        'gb_jet_eurofighter',
        'gb_jet_harrier',
        'gb_jet_harrier_gr9_asf',
        'gb_jet_harrier_gr3',
        'gb_jet_harrier_gr3b',
        'gb_jet_harrier_gr3c',
        'gb_jet_seaharrier',
        'gb_jet_seaharrier_mk17',
        'ger_ahe_tiger',
        'ger_jet_eurofighter',
        'idf_ahe_apache',
        'idf_jet_f16',
        'mec_ahe_ec635',
        'mec_ahe_havoc',
        'mec_ahe_mi24',
        'mec_ahe_mi24_light',
        'mec_ahe_sa341h',
        'mec_jet_mig29',
        'mec_jet_su22',
        'mec_jet_su25a',
        'nl_ahe_apache',
        'nl_jet_f16',
        'nl_jet_f16_cas',
        'nva_jet_mig21',
        'ru_ahe_havoc',
        'ru_ahe_mi24',
        'ru_ahe_mi24_light',
        'ru_jet_mig21',
        'ru_jet_mig29',
        'ru_jet_mig29_asf',
        'ru_jet_su25a',
        'ru_jet_su27',
        'ru_jet_su27_asf',
        'ru_jet_su34',
        'ru_jet_su39',
        'us_ahe_ah1z',
        'us_ahe_ah6',
        'us_ahe_ah6a',
        'us_ahe_apache',
        'us_ahe_kiowa',
        'us_ahe_kiowa_alt',
        'us_ahe_kiowa_alt2',
        'us_ahe_oh6',
        'us_ahe_uh1c',
        'us_ahe_uh1nrockets',
        'us_jet_a10a',
        'us_jet_a1h',
        'us_jet_a4',
        'us_jet_f15',
        'us_jet_f16',
        'us_jet_f18c',
        'us_jet_harrier',
        'us_jet_harrierb'
        ],
    'tnk' : [
        'cf_tnk_leo2a6',
        'ch_tnk_type98',
        'ch_tnk_ztz99',
        'fr_tnk_amx10rc',
        'fr_tnk_leclerc',
        'fsa_tnk_t62',
        'gb_tnk_challenger',
        'gb_tnk_challenger_alt',
        'ger_tnk_leo2a6',
        'idf_tnk_merkava',
        'mec_tnk_t72',
        'mec_tnk_t72s',
        'mec_tnk_t72s_alt',
        'mil_tnk_t62',
        'nl_tnk_leo2a6',
        'nva_tnk_pt76',
        'ru_tnk_t72b',
        'ru_tnk_t90',
        'ru_tnk_t90_alt',
        'us_tnk_m1a1',
        'us_tnk_m1a1_alt',
        'us_tnk_m1a2',
        'us_tnk_m1a2_alt',
        'us_tnk_m48a1',
        'us_tnk_m67',
        ],
    'the' : [
        'arg_the_chinook_ch47c',
        'arg_the_uh1h',
        'cf_the_ch146',
        'cf_the_ch146_c6',
        'cf_the_chinook',
        'cf_the_uh1n',
        'cf_the_uh1n_c6',
        'ch_the_mi17',
        'ch_the_z8',
        'ch_the_z9b',
        'fr_the_chinook',
        'fr_the_nh90',
        'fr_the_nh90_navy',
        'fr_the_panther',
        'gb_the_chinook',
        'gb_the_chinook_ch1',
        'gb_the_gazelle',
        'arg_the_lynx_mk23',
        'gb_the_lynx',
        'gb_the_lynx_alt',
        'gb_the_lynx_has2',
        'gb_the_lynx_l7a2',
        'gb_the_lynx_l7a2_alt',
        'gb_the_merlin',
        'gb_the_wessex',
        'ger_the_nh90',
        'ger_the_uh1d',
        'ger_the_uh1d_mg3',
        'idf_the_uh60',
        'mec_the_mi17',
        'mec_the_sa341h',
        'nl_the_chinook',
        'nl_the_nh90',
        'ru_the_mi8',
        'us_the_chinook',
        'us_the_h-34',
        'us_the_mh6',
        'us_the_mv22',
        'us_the_uh1c',
        'us_the_uh1d',
        'us_the_uh1d_medevac',
        'us_the_uh1n',
        'us_the_uh1n_m240d',
        'us_the_uh60',
        'us_the_uh60_alt',
        'us_the_uh60_soar'
        ]
    }