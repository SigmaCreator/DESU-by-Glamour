
particles = ['MO', 'DE', 'NI', 'TO', 'WO', 'HE', 'KARA', 'MADE']
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
        'へ'  : 'HE',
        'て' : 'TE',
        'な' : 'NA',
        'の' : 'NO',
        'じゃ' : 'JA',
        'か' : 'KA',
        'から' : 'KARA',
        'まで' : 'MADE',
        'ます' : 'MASU'
    }.get(term,'WHATEVER')


def token_to_word(token) :

    return {
        'NOUN' : 'Substantivo',              # NOUN + AUX_VERB (NA) = NA_ADJ
        'PARTICLE' : 'Partícula',
        'VERB' : 'Verbo',              # VERB + [AUX_VERB]* = VERB
        'AUX_VERB' : 'Cópula',
        'ADNOM_ADJ' : 'Adjunto Adnominal',       # ADNOM_ADJ + NOUN = NOMINAL
        'ADVERB' : 'Advérbio',
        'ADJ_I' : 'Adjetivo I',           # I_ADJ + TE
        'ADJ_NOUN' : 'Adjetivo NA',
        'NOMINAL' : 'Sintagma Nominal'
    }.get(token,token)

info = {
    'NOUN' : 'Um substantivo é uma palavra que funciona como o nome de alguma coisa específica ou de um conjunto de coisas.\nPalavras que seriam consideradas como pronomes em outras línguas são abrangidas pela classe de substantivos em japonês.',
    'VERB' : 'Um verbo é uma palavra que engloba uma ação ou estado de existência.\nEm japonês verbos não são flexionados de acordo com gênero, número ou sujeito.',
    'MASU' : 'Um verbo na forma ます funciona como um predicado.\nA forma ます é polida.\nUm verbo na forma ます é usado como uma sentença expressa uma coisa habitual ou uma verdade, ou seja, equivalente ao tempo presente da língua portuguesa.\nA forma ます também pode ser usada para indicar algo que ocorrerá no futuro.\nA forma ます possui flexões negativa e pretérita. ',
    'AUX_VERB' : "です é uma palavra de ligação (cópula), equivalente em sentido ao verbo “ser” em português.\nです é a versão mais formal e polida de だ.\nです indica um julgamento ou asserção.\nUm substantivo usado com です funciona como predicado.\nQuando です é usado após um adjetivo-い, tem como função tornar a sentença mais polida.\nです não pode ser utilizado antes do final de uma sentença.\nです é flexionado quando a sentença é negativa ou está no pretérito.\n\nじゃありません é a forma negativa de です, utilizada em conversas do dia a dia.\nではありません é a versão mais formal de じゃありません.\n※ は em ではありません é lido como わ.\n",
    'ADNOM_ADJ' : 'Um adjetivo adnominal (連体詞 – れんたいし) é uma classificação gramatical particular da língua japonesa.\nTem função similar a de adjetivos, porém sem ser flexionado.\nFunciona de modo a qualificar o substantivo seguinte.',
    'ADVERB' : 'Advérbios são palavras usadas para qualificar verbos, adjetivos e outros advérbios.\nNa língua japonesa, há palavras que são advérbios propriamente ditos e há também como transformar adjetivos em advérbios.',
    'ADJ_I' : 'Adjetivos são palavras usadas para qualificar substantivos.\nNa língua japonesa, há dois grupos principais de adjetivos: adjetivos-い e adjetivos-な, ambos com suas respectivas formas de flexão negativa e pretérita.',
    'ADJ_NA' : 'Adjetivos são palavras usadas para qualificar substantivos.\nNa língua japonesa, há dois grupos principais de adjetivos: adjetivos-い e adjetivos-な, ambos com suas respectivas formas de flexão negativa e pretérita.',
    'ADJ_TE' : 'Adjetivos são palavras usadas para qualificar substantivos.\nNa língua japonesa, há dois grupos principais de adjetivos: adjetivos-い e adjetivos-な, ambos com suas respectivas formas de flexão negativa e pretérita.\nUm adjetivo-い quando seguido de outros adjetivos é conjugado na forma て.',
    'ADJ_DE' : 'Adjetivos são palavras usadas para qualificar substantivos.\nNa língua japonesa, há dois grupos principais de adjetivos: adjetivos-い e adjetivos-な, ambos com suas respectivas formas de flexão negativa e pretérita.\nUm adjetivo-な quando seguido de outros adjetivos é conjugado na forma で.',
    'WA' : "A partícula は indica que a palavra anterior é o tópico da sentença. \nSentenças são normalmente construídas de forma que se escolhe um substantivo o qual se queira falar sobre, adiciona-se は para mostrar que ele é o tópico da sentença e então faz-se uma declaração sobre ele.\n※ A partícula は é lida como わ.",
    'NO' : "A partícula の é utilizada para indicar posse, onde N2 pertence a N1.",
    'WO' : 'A partícula を é usada para indicar objeto direto de um verbo transitivo.\n※ A partícula を é lida como お.',
    'TO' : 'A partícula と conecta dois substantivos em uma relação coordenada. Possui significado análogo à conjunção “e” em português.',
    'DE' : 'A partícula で indica um modo ou método.\nQuando um verbo que denota movimento é usado com で, a partícula indica meio de transporte. Neste caso o substantivo que precede a partícula é um veículo.',
    'HE' : 'Quando um verbo indica movimento em direção a determinado lugar, a partícula へ é utilizada após o substantivo que indica este lugar.\n※ A partícula へ é lida como え.',
    'NI' : 'Quando um verbo denota uma ação momentânea ou de movimento, o tempo ou local em que ela ocorre é marcado com a partícula に.\nQuando da denotação de tempo, a partícula に é usada caso o substantivo antes dela contenha um numeral. \nTambém pode ser adicionada aos dias de semana, embora não seja necessário.',
    'MO' : 'A partícula も serve para indicar o tópico e substitui a partícula は quando a declaração sendo feita é a mesma aplicada ao tópico anterior.',
    'KARA' : 'A partícula から indica um tempo ou local inicial de uma ação.',
    'MADE' : 'A partícula まで indica um tempo final ou local final de uma ação.',
    'KA' : 'A partícula か é utilizada para expressar uma dúvida, pergunta ou incerteza.\nUma pergunta é formada adicionando-se か ao final da sentença.\nA partícula か é seguida de um ponto final e não de um ponto de interrogação.\n'
}