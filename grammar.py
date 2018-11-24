from terms import common_terms, particles, adjectives
from patterns import pattern_list
from exceptions import *
import log

next_token = ""
all_tokens = []
curr_rule = "NO RULE"

def check(token):
    
    global next_token, all_tokens, curr_rule

    if next_token == 'OVER' : raise EndOfSentenceException({"End of Sentence - Expected Token" : token , "Current Rule" : curr_rule})
    
    if (next_token == token) : 
        log.explain.append(next_token)
        print("CORRECT!", token, "@", curr_rule)
    else : 
        print("INCORRET! Expecting:", token, "- Found:", next_token, "@", curr_rule)
        raise GrammarException({"Grammar - Expected Token" : token , "Token" : next_token, "Current Rule" : curr_rule})
    
    if (len(all_tokens) != 0) : next_token = all_tokens.pop(0)
    else : next_token = 'OVER' ; print("NO TOKENS LEFT TO CRY")

def PHRASE():

    global curr_rule

    curr_rule = "PHRASE"

    test = NOMINAL() # Tests for a NOMINAL

    if test : # The phrase starts with a NOMINAL

        curr_rule = "TOPIC"

        has_topic = False # For now, no TOPIC has been identified

        if (next_token == 'WA') :

            check('WA')
            if (next_token == 'AUX_VERB') : check('NOMINAL') # Breaks
            has_topic = True    # Where's a WA, there's a TOPIC

        if (not has_topic) and (next_token in particles) : # If there's no TOPIC and the NEXT TOKEN is a PARTICLE

            curr_rule = "INFO"
            check(next_token) # Check whatever PARTICLE that is
        
        test = INFO() # Tests for INFO

        if test : test = VERBAL()   # ... and the INFO test succeeds, it should be an ACTION PHRASE
        else : test = COPULA()      # ... and the INFO test fails, it should be a DESCRIPTIVE PHRASE 
    
    else : test = VERBAL()

    return test
               
def INFO():

    global curr_rule

    curr_rule = "INFO"

    # It returns TRUE if it reached a VERB, possibly acknowledging a chain of (NOMINAL PARTICLE) structures 
    # It returns FALSE if the chain was broken by a PARTICLE-less NOMINAL
    # It will create a GrammarException if a NOMINAL-less PARTICLE is found

    if (next_token == 'VERB') : return True # It reached the end of the structure

    nominal_test = NOMINAL() # Tests for a NOMINAL

    particle_test = False

    if (next_token in particles) :  # If the NEXT TOKEN is a PARTICLE
        
        check(next_token)           # Check whatever PARTICLE that is
        particle_test = True        # and tell 'em there's a PARTICLE
    
    if nominal_test :

        if particle_test : return INFO()    # If a (NOMINAL PARTICLE) block was checked, eat recursions
        else : return False                 # Else, it's a chain break
    
    else :

        if particle_test : check('NO_NOMINAL_BEFORE') # Breaks
        return False        

def VERBAL():

    global curr_rule

    curr_rule = "VERBAL"

    check('VERB')

    return True

def COPULA():

    global curr_rule

    curr_rule = "COPULA"

    check('AUX_VERB')

    return True

def NOMINAL():

    adverb_test = False

    if (next_token == 'ADVERB') : check('ADVERB') ; adverb_test = True

    adjective_test = ADJECTIVE()
    noun_test = NOUN()

    if adjective_test and (not noun_test) :

        if (next_token != 'AUX_VERB') : check('AUX_VERB') ; return False # it's gonna explode
        else : return True
    
    return noun_test
    
def NOUN():

    if (next_token == 'NOUN') : check('NOUN')
    else : return False

    if (next_token == 'NO') : 

        check('NO')
        if (next_token == 'NOUN') : check('NOUN')
    
    return True

def ADJECTIVE():

    if (next_token == 'ADJ_I') : check('ADJ_I') ; return True
    
    elif (next_token == 'ADJ_NOUN') : check('ADJ_NOUN') ; return True

    elif (next_token == 'ADJ_NA') :

        check('ADJ_NA')
        if (next_token != 'NOUN') : check('NOUN') ; return False # Breaks
        return True

    elif (next_token == 'ADJ_TE') : 

        check('ADJ_TE')
        if (next_token not in adjectives) : check('ADJECTIVE') ; return False # Breaks
        return ADJECTIVE()

    elif (next_token == 'ADJ_DE') : 

        check('ADJ_DE') 
        if (next_token not in adjectives) : check('ADJECTIVE') ; return False # Breaks
        return ADJECTIVE()
    
    return False

def token_wo_issho_ni_suru(token_list):
    
    global next_token, all_tokens    

    all_tokens = token_list

    aux_list = token_list
    old_list = []

    while (True) :

        old_list = aux_list
        for p in pattern_list : aux_list = pattern_matcher(aux_list,p)
        if (aux_list == old_list) : break

    all_tokens = aux_list

    print("Tokens - After : ", all_tokens)
            
    next_token = all_tokens.pop(0)
    
    try : 

        PHRASE()

    except Exception as g :

        print(g)

def pattern_matcher(list, pattern):

    # print("Token list: ", list)
    # print("Pattern: ", pattern)

    if len(pattern) == 0 : return

    new_list, buffer = [], []
    
    i, j = 0, 0

    pattern_break = False

    while (i < len(list)) :

        if pattern_break :

            new_list.extend(buffer)
            buffer = []
            j = 0
            pattern_break = False

        buffer.append(list[i])
        # print("Buffer: ", buffer)

        if pattern == tuple(buffer) :

            # print("Pattern found: ", pattern, " ==> ", pattern_list[pattern])
            new_list.append(pattern_list[pattern])
            buffer = []
            j = 0

        elif len(buffer) != 0 and pattern[j] == buffer[j] :

            j = j + 1
            
        else :
            
            if j > 0 : pattern_break = True
            new_list.extend(buffer)
            buffer = []
            j = 0

        i = i + 1
    
    if len(buffer) != 0 : new_list.extend(buffer)

    return new_list