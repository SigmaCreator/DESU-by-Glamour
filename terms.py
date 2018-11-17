
particles = ['MO', 'DE', 'NI', 'TO', 'WO']
adjectives = ['ADJ_I','ADJ_NOUN','ADJ_NA','ADJ_TE']

def common_terms(term) :
    
    return {
        '名詞' : 'NOUN',              # NOUN + AUX_VERB (NA) = NA_ADJ
        '助詞' : 'PARTICLE',
        '動詞' : 'VERB',              # VERB + [AUX_VERB]* = VERB
        '助動詞' : 'AUX_VERB',
        '連体詞' : 'ADNOM_ADJ',       # ADNOM_ADJ + NOUN = NOMINAL
        '副詞' : 'ADVERB',
        '形容詞' : 'ADJ_I',           # I_ADJ + TE
        '形容動詞語幹' : 'ADJ_NOUN',
        'は' : 'WA',
        'も' : 'MO',
        'で' : 'DE',
        'に' : 'NI',
        'と' : 'TO',
        'を' : 'WO',
        'て' : 'TE',
        'な' : 'NA',
        'の' : 'NO',
        'じゃ': 'JA'
    }.get(term,'WHATEVER')