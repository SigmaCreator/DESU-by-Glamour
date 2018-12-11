import terms

translation = ""
error = ""

explain = []
phrase = []

verb = "PLAIN" # MASU or PLAIN
sentence_type = "" # VERBAL or DESCRIPTIVE
has_topic = False
has_info = False
question = False

def reset() :

    global translation, error, explain, phrase, verb, sentence_type, has_topic, has_info, question

    translation = ""
    error = ""
    explain = []
    phrase = []
    verb = "PLAIN" # MASU or PLAIN
    sentence_type = "" # VERBAL or DESCRIPTIVE
    has_topic = False
    has_info = False
    question = False


def clear_error() :

    global error

    error = ""

def set_phrase(words):

    global phrase

    phrase = words

def found_topic():

    global has_topic

    has_topic = True

def found_info():

    global has_info

    has_info = True

def set_verb_form(form):

    global verb
    
    verb = form

def set_sentence_type(st):

    global sentence_type

    sentence_type = st
    
def clear_log():

    global explain

    explain = []

# def get_info():

#     global explain, verb

#     explained = ""

#     print("fORMA",verb)

#     for token in explain :

#         exp = terms.info[token]

#         if (verb == 'MASU') :
#             print("ENTRORRRRRR")
#             explained = explained + (token + " : " +  exp + terms.info['MASU'] + "\n")
#         else :
#             explained = explained + (token + " : " +  exp + "\n")

#     return explained