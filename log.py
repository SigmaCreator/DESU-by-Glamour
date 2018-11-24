
translation = ""

explain = []

info = {
    'WA' : "Partícula ligadora de tópico",
    'NO' : "Partícula frasal",
    'NOUN' : "É um substantivo",
    'AUX_VERB' : "É um verbo descritivo"
}

def clear_log():

    explain = []

def get_info():

    explained = ""

    for token in explain :

        explained = explained + (token + " : " + info[token] + "\n")

    return explained