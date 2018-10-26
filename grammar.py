next_token_group = []
NOMINAL, WA, MO, KARA, MADE, KA, NI, HE, TO, DE, WO, PoliteCopula, VerboMasu, Adjectives, Adj_I, Adj_NA, NA = "test"
curr_rule, overall_rule = -1, -1

def check(curr_rule, overall_rule, token_group):
    pass


def topic(overall_rule):

    curr_rule = 0

    loop = False

    if(next_token_group == [NOMINAL, WA]):
        check(curr_rule, overall_rule, [NOMINAL, WA])
    else:
        loop = True

    group = []

    while(loop):
        
        if(next_token_group == [NOMINAL, MO]):
            group.append([NOMINAL, MO])
        else: 
            break

    if(loop): 
        check(curr_rule, overall_rule, group)

def KA_rule(overall_rule):

    curr_rule = -10

    if (next_token_group == [KA]):
        check(curr_rule, overall_rule, [KA])

def rule_01(overall_rule):

    curr_rule = 1

    topic(overall_rule)

    check(curr_rule, overall_rule, [NOMINAL])
    check(curr_rule, overall_rule, [PoliteCopula])

    KA_rule(overall_rule)

def rule_02(overall_rule):

    curr_rule = 2

    topic(overall_rule)

    if(next_token_group == [NOMINAL, KARA]):
        check(curr_rule, overall_rule, [NOMINAL, KARA])

    if(next_token_group == [NOMINAL, MADE]):
        check(curr_rule, overall_rule, [NOMINAL, MADE])

    if(next_token_group == [VerboMasu]):
        check(curr_rule, overall_rule, [VerboMasu])
    elif(next_token_group == [PoliteCopula]):
        check(curr_rule, overall_rule, [PoliteCopula])

    KA_rule(overall_rule)

def NI_rule_01(overall_rule): # Particle に as specific point in time indicator

    curr_rule = 3

    if(next_token_group == [NOMINAL, NI]): 
        check(curr_rule, overall_rule, [NOMINAL, NI])

def HE_rule(overall_rule):

    curr_rule = 4

    if(next_token_group == [NOMINAL, HE]): 
        check(curr_rule, overall_rule, [NOMINAL, HE])

def TO_rule(overall_rule):

    curr_rule = 5

    group = []

    while(True):
        
        if(next_token_group == [NOMINAL, TO]):
            group.append([NOMINAL, TO])
        else: 
            break

    if(len(group) > 0):
        check(curr_rule, overall_rule, group)

def DE_rule_01(overall_rule): # Particle で as mean indicator

    curr_rule = 6

    if(next_token_group == [NOMINAL, DE]): 
        check(curr_rule, overall_rule, [NOMINAL, DE])

def WO_rule(overall_rule):

    curr_rule = 8

    if(next_token_group == [NOMINAL, WO]): 
        check(curr_rule, overall_rule, [NOMINAL, WO]) 

def rule_07(overall_rule):

    curr_rule = 7

    topic(overall_rule)
    
    NI_rule_01(overall_rule)
    TO_rule(overall_rule)
    DE_rule_01(overall_rule)

    if (next_token_group == [NOMINAL, HE]):
        HE_rule(overall_rule)
    elif (next_token_group == [NOMINAL, WO]):
        WO_rule(overall_rule)

    check(curr_rule, overall_rule, [VerboMasu])

    KA_rule(overall_rule)

def rule_10_11(overall_rule):

    curr_rule = 10

    topic(overall_rule)

    check(curr_rule, overall_rule, [Adjectives])

    if (next_token_group == [Adj_I]):
        check(curr_rule, overall_rule, [Adj_I, NOMINAL])
    elif (next_token_group == [Adj_NA, NA, NOMINAL]):
        check(curr_rule, overall_rule, [Adj_NA, NA, NOMINAL])
    
    check(curr_rule, overall_rule, [PoliteCopula])

    