next_token_group = []
NOMINAL, WA, MO, KARA, MADE, KA, NI, HE, TO, DE, WO, PoliteCopula, VerboMasu = "test"
curr_rule, overall_rule = -1, -1

from terms import common_terms

def check(curr_rule, overall_rule, token_group):
    pass

def rule_00(overall_rule):

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

def rule_01(overall_rule):

    curr_rule = 1

    rule_00(overall_rule)

    check(curr_rule, overall_rule, [NOMINAL])
    check(curr_rule, overall_rule, [PoliteCopula])

    if (next_token_group == [KA]):
        check(1, overall_rule, [KA])

def rule_02(overall_rule):

    curr_rule = 2

    rule_00(overall_rule)

    if(next_token_group == [NOMINAL, KARA]):
        check(curr_rule, overall_rule, [NOMINAL, KARA])

    if(next_token_group == [NOMINAL, MADE]):
        check(curr_rule, overall_rule, [NOMINAL, MADE])

    if(next_token_group == [VerboMasu]):
        check(curr_rule, overall_rule, [VerboMasu])
    else:
        check(curr_rule, overall_rule, [PoliteCopula])

    if (next_token_group == [KA]):
        check(curr_rule, overall_rule, [KA])

def rule_03(overall_rule):

    curr_rule = 3

    if(next_token_group == [NOMINAL, NI]): 
        check(curr_rule, overall_rule, [NOMINAL, NI])

def rule_04(overall_rule):

    curr_rule = 4

    if(next_token_group == [NOMINAL, HE]): 
        check(curr_rule, overall_rule, [NOMINAL, HE])

def rule_05(overall_rule):

    curr_rule = 5

    group = []

    while(True):
        
        if(next_token_group == [NOMINAL, TO]):
            group.append([NOMINAL, TO])
        else: 
            break

    if(len(group) > 0):
        check(curr_rule, overall_rule, group)

def rule_06(overall_rule):

    curr_rule = 6

    if(next_token_group == [NOMINAL, DE]): 
        check(curr_rule, overall_rule, [NOMINAL, DE])

def rule_07(overall_rule):

    curr_rule = 7

    rule_00(overall_rule)
    rule_03(overall_rule)
    rule_05(overall_rule)
    rule_06(overall_rule)
    rule_04(overall_rule)

    if(next_token_group == [VerboMasu]):
        check(curr_rule, overall_rule, [VerboMasu])

    if (next_token_group == [KA]):
        check(curr_rule, overall_rule, [KA])

def rule_08(overall_rule):

    curr_rule = 8

    if(next_token_group == [NOMINAL, WO]): 
        check(curr_rule, overall_rule, [NOMINAL, WO]) 

def rule_09(overall_rule):

    curr_rule = 9

    rule_00(overall_rule)
    rule_03(overall_rule)
    rule_05(overall_rule)
    rule_06(overall_rule)
    rule_08(overall_rule)

    if(next_token_group == [VerboMasu]):
        check(curr_rule, overall_rule, [VerboMasu])

    if (next_token_group == [KA]):
        check(curr_rule, overall_rule, [KA])
