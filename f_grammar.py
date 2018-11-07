from terms import common_terms
from patterns import pattern_list, particles

next_token = ""
all_tokens = []
curr_rule = "NO RULE"

def check(token):
    
    global next_token, all_tokens, curr_rule
    
    if (next_token == token) : print("CORRECT! ", curr_rule) ; return True
    else : print("INCORRET! ", curr_rule) ; return False

    if (len(all_tokens) != 0) : next_token = all_tokens.pop(0)

def lookahead():

    global all_tokens

    if (len(all_tokens) != 0) : return all_tokens[0]

def PHRASE():

    test = NOMINAL() # Tests for a NOMINAL

    if test : # The phrase starts with a NOMINAL

        la = lookahead() # Look ahead the PARTICLE

        has_topic = False # For now, no TOPIC has been identified

        if (next_token == 'WA') : check('WA') ; has_topic = True    # Where's a WA, there's a TOPIC

        if (not has_topic) and (next_token in particles) : # If there's no TOPIC and the NEXT TOKEN is a PARTICLE
            
            check(next_token) # Check whatever PARTICLE that is
        
        test = INFO() # Tests for INFO

        if (la == 'NOUN') : # If it saw a NOUN ahead of its time ...

            if test : test = VERBAL()   # ... and the INFO test succeeds, it should be an ACTION PHRASE
            else : test = COPULA()      # ... and the INFO test fails, it should be a DESCRIPTIVE PHRASE 
    
    else : test = VERBAL()

    return test
               
def INFO():

    # If it succeeds, there's a chain of structures (NOMINAL PARTICLE)
    # If it fails, the chain was most likely broken by a PARTICLE-less NOMINAL

    if (next_token == 'VERB') return True

    noun_test = NOMINAL() # Tests for a NOMINAL

    particle_test = False

    if (next_token in particles) :  # If the NEXT TOKEN is a PARTICLE
        
        check(next_token)           # Check whatever PARTICLE that is
        
        particle_test = True        # and tell 'em there's a PARTICLE

    if (noun_test and particle_test) : return INFO()    # If a (NOMINAL PARTICLE) block was checked, eat recursions
    else : return False                                 # Else, chain break

def VERBAL():

    check('VERBAL')

    return True

def COPULA():
    
    if (next_token == 'AUX_VERB') : check('AUX_VERB') ; return True # DESU / DA
    elif (next_token == 'JA') : check('JA') ; check('AUX_VERB') ; return True # JA ARIMASEN / JA NAI
    else : check('DE') ; check('WA') ; check('AUX_VERB') ; return True # DE WA ARIMASEN / DE WA NAI

def NOMINAL():

    adverb_test = False

    if (next_token == 'ADVERB') : check('ADVERB') ; adverb_test = True

    adjective_test = ADJECTIVE()
    noun_test = NOUN()

    if adjective_test and (not noun_test) :
        if (next_token != 'AUX_VERB') : check('AUX_VERB') ; return False # it's gonna explode
    
    return noun_test
    
def NOUN():

    noun_test = False

    if (next_token == 'NOUN') : check('NOUN')
    else : return False

    if (next_token == 'NO') : 
        check('NO')
        if next_token == 'NOUN' : check('NOUN')
    
    return True

def ADJECTIVE():
    
    if (next_token == 'I_ADJ') :

        check('I_ADJ')

        if (next_token == 'TE') : check('TE') ; return ADJECTIVE()
        else : return True

    elif (next_token == 'NA_ADJ') :

        check('NA_ADJ')

        if (next_token == 'DE') : check('DE') ; return ADJECTIVE()
        elif (next_token == 'NA') : check('NA') ; return ADJECTIVE()
        else : return True
        
    else : return False