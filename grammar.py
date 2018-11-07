from terms import common_terms
from patterns import pattern_list, particles

next_token = ""
all_tokens = []
curr_rule = "NO RULE"

def check(token):
    
    global next_token, all_tokens, curr_rule
    
    if (next_token == token) : print("CORRECT! ", curr_rule)
    else : print("INCORRET! ", curr_rule)

    if (len(all_tokens) != 0) : next_token = all_tokens.pop(0)

def uncheck(token):

    global next_token, all_tokens

    all_token.insert(0,next_token)
    next_token = token

def NOMINAL_rule() :

    global next_token, curr_rule

    curr_rule = "NOMINAL RULE"

    is_nominal = False

    if (next_token == 'ADNOM_ADJ') : 
        check('ADNOM_ADJ')
        ADJECTIVE_rule()
        check('NOUN')
        is_nominal = True

    if (next_token == 'ADVERB') :
        check('ADVERB')
        is_nominal = True
    elif (next_token == 'NO') : check('NO')
    
    while (next_token not in particles) :
        ADJECTIVE_rule()
        if (next_token == 'NOUN') : 
            check('NOUN')
            if (next_token == 'NO') : check('NO')
            is_nominal = True

    if is_nominal : uncheck('NOMINAL')

def ADJECTIVE_rule():

    global next_token, curr_rule

    curr_rule = "ADJECTIVE RULE"

    loop = True

    while (loop)

        if (next_token == 'I_ADJ') :
            check('I_ADJ')
            if (next_token == 'TE') : check('TE')
            else : loop = False
        elif (next_token == 'NOUN') :
            check('NOUN')
            if (next_token == 'DE') : check('DE')
            elif (next_token == 'NA') : 
                check('NA')
                loop = False
            else :  
                uncheck('NOUN')
                loop = False
        else : loop = False

def POLITE_COPULA_rule():

    if (next_token == 'AUX_VERB') : check('AUX_VERB') # DESU / DA
    elif (next_token == 'JA') : check('JA') ; check('AUX_VERB') # JA ARIMASEN / JA NAI
    else : check('DE') ; check('WA') ; check('AUX_VERB') # DE WA ARIMASEN / DE WA NAI

def topic(overall_rule):
    
    global next_token, curr_rule

    curr_rule = "TOPIC RULE"

    loop = False

    NOMINAL_rule() 

    if (next_token = 'NOMINAL') : check('NOMINAL') # DAR UNCHECK CASO N VEJA PARTICULA
   
    if (next_token == 'WA') : check('WA')
    elif (next_token == 'MO') :
        check('MO')
        loop = True

    while (loop):

        NOMINAL_rule()

        if (next_token == 'NOMINAL') : 
            check('NOMINAL')
            if (next_token == 'MO') : check('MO')
            else : 
                uncheck('NOMINAL')
                loop = False

def rule_01(overall_rule):
    
    curr_rule = 1
    
    topic(overall_rule)

    NOMINAL_rule() ; check('NOMINAL')

    POLITE_COPULA_rule()

    print("THE PHRASE FITS RULE 01")

# KA_rule(overall_rule)

def rule_caller():

    rule_01(1)

def token_wo_issho_ni_suru(token_list):
    
    global next_token, all_tokens    

    all_token = token_list

    aux_list = token_list
    old_list = []

    while (True) :
        old_list = aux_list
        for p in pattern_list : aux_list = pattern_matcher(aux_list,p)
        if (aux_list == old_list) : break
            
    next_token = all_tokens.pop(0)
    
    rule_caller()

def pattern_matcher(list, pattern):

    print("Token list: ", list)

    if len(pattern) == 0 : return

    new_list, buffer = [], []
    
    i, j = 0, 0

    while (i < len(list)) :

        buffer.append(list[i])
        print("Buffer: ", buffer)

        if pattern == tuple(buffer) :
            print("Pattern found: ", pattern, " ==> ", pattern_list[pattern])
            new_list.append(pattern_list[pattern])
            buffer = []
            j = 0

        if len(buffer) != 0 and pattern[j] == buffer[j] :
            j = j + 1
        else :
            new_list.extend(buffer)
            buffer = []
            j = 0

        i = i + 1

    return new_list





#
#def KA_rule(overall_rule):
#
#    curr_rule = -10
#
#    if (next_token_group == [KA]):
#        check(curr_rule, overall_rule, [KA])
#

#
#def rule_02(overall_rule):
#
#    curr_rule = 2
#
#    topic(overall_rule)
#
#    if(next_token_group == [NOMINAL, KARA]):
#        check(curr_rule, overall_rule, [NOMINAL, KARA])
#
#    if(next_token_group == [NOMINAL, MADE]):
#        check(curr_rule, overall_rule, [NOMINAL, MADE])
#
#    if(next_token_group == [VerboMasu]):
#        check(curr_rule, overall_rule, [VerboMasu])
#    elif(next_token_group == [PoliteCopula]):
#        check(curr_rule, overall_rule, [PoliteCopula])
#
#    KA_rule(overall_rule)
#
#def NI_rule_01(overall_rule): # Particle に as specific point in time indicator
#
#    curr_rule = 3
#
#    if(next_token_group == [NOMINAL, NI]):
#        check(curr_rule, overall_rule, [NOMINAL, NI])
#
#def HE_rule(overall_rule):
#
#    curr_rule = 4
#
#    if(next_token_group == [NOMINAL, HE]):
#        check(curr_rule, overall_rule, [NOMINAL, HE])
#
#def TO_rule(overall_rule):
#
#    curr_rule = 5
#
#    group = []
#
#    while(True):
#
#        if(next_token_group == [NOMINAL, TO]):
#            group.append([NOMINAL, TO])
#        else:
#            break
#
#    if(len(group) > 0):
#        check(curr_rule, overall_rule, group)
#
#def DE_rule_01(overall_rule): # Particle で as mean indicator
#
#    curr_rule = 6
#
#    if(next_token_group == [NOMINAL, DE]):
#        check(curr_rule, overall_rule, [NOMINAL, DE])
#
#def WO_rule(overall_rule):
#
#    curr_rule = 8
#
#    if(next_token_group == [NOMINAL, WO]):
#        check(curr_rule, overall_rule, [NOMINAL, WO])
#
#def rule_07(overall_rule):
#
#    curr_rule = 7
#
#    topic(overall_rule)
#
#    NI_rule_01(overall_rule)
#    TO_rule(overall_rule)
#    DE_rule_01(overall_rule)
#
#    if (next_token_group == [NOMINAL, HE]):
#        HE_rule(overall_rule)
#    elif (next_token_group == [NOMINAL, WO]):
#        WO_rule(overall_rule)
#
#    check(curr_rule, overall_rule, [VerboMasu])
#
#    KA_rule(overall_rule)
#
#def rule_10_11(overall_rule):
#
#    curr_rule = 10
#
#    topic(overall_rule)
#
#    check(curr_rule, overall_rule, [Adjectives])
#
#    if (next_token_group == [Adj_I]):
#        check(curr_rule, overall_rule, [Adj_I, NOMINAL])
#    elif (next_token_group == [Adj_NA, NA, NOMINAL]):
#        check(curr_rule, overall_rule, [Adj_NA, NA, NOMINAL])
#
#    check(curr_rule, overall_rule, [PoliteCopula])
#
#
