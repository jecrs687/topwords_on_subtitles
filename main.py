import pysrt
import os, fnmatch
listOfFiles = os.listdir('.')
pattern = "*.srt"
conteudo = ''
numMinimoRepeticoes=0
porcentOfBoost = 10

def booster(conteudo):
    """order the firsts items in the array, this is a boost for the order the full vector
    \n [return array]"""
    boost = contar_conteudo_e_remover_excesso(conteudo[0:int(len(conteudo)/porcentOfBoost)])
    boost = ordenar_conteudo(boost)
    for x in boost:
        conteudo.remove(x[0])
        conteudo.insert(boost.index(x), x[0])
    return conteudo

def contar_conteudo_e_remover_excesso(conteudo):
    """This function get the words and convert her in one array [[word, weight], ....[word,weight]]
    \n [return: array]
    """
    words=[]
    while(len(conteudo)>0):
        weight=conteudo.count(conteudo[0])
        word=conteudo[0]
        words.append((word, weight))
        lenght=len(conteudo)
        x=0
        while(x<lenght):
            if(conteudo[x] == word):
                del(conteudo[x])
                lenght-=1
                continue
            x+=1
    return words

def filtrar_conteudo(conteudo):
    """this function is the filter for the words, 
    this function get the words and filter her
    \n [return: string, int]"""
    conteudo = conteudo.split()
    palavras = []
    for x in conteudo:
        if(x.isalpha()):
            palavras.append(x)
    tamanho = len(palavras)
    del(conteudo)
    return palavras,tamanho

def ordenar_conteudo(conteudo):
    """this function only realize one sort of the words basead in the weight
    \n [return array]
    """
    conteudo.sort(key=lambda x: x[1], reverse=True)
    return conteudo
def arquivar(conteudo, lingua1, tamanho):
    """archive the words in a file txt using a structure json
    \n [return null]"""
    porcentagem = 0
    with open(lingua1+'-pt.json','w+', encoding="utf-8") as arq:
        arq.write('{'+'"tamanho":{},'.format(tamanho)+'"palavras":[')
        arq.write("\n")
        arq.write("\n")
        for z in range(0, len(conteudo)):
            arq.write('{"word":"'+conteudo[z][0]+'","repeted":{}'.format(conteudo[z][1])+',"porcent":{}'.format((conteudo[z][1]/tamanho)*100)+'},')
            arq.write("\n")
            porcentagem =porcentagem + ((conteudo[z][1]/tamanho)*100 )
        arq.write('],"porcentagem":{}'.format(porcentagem)+'}')
        print('arquivo salvo como {}-pt.txt'.format(lingua1))

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)
        subs = pysrt.open(entry, encoding='iso-8859-1')
        words = ''
        for x in subs:
            words = '{} {}'.format(words, x.text.lower()) 
        conteudo = '{} {}'.format(conteudo,words)
        del(words)
print('_____________________________________________________\n\n___________________________')
print("filtrando conteudo")
conteudo,tamanho = filtrar_conteudo(conteudo)
print("contando conteudo e removendo excesso")
conteudo = booster(conteudo)
conteudo = contar_conteudo_e_remover_excesso(conteudo)
print("ordenando conteudo")
conteudo = ordenar_conteudo(conteudo)
print("arquivando")
arquivar(conteudo, 'English', tamanho)
print("\n\n\n\n")
print(conteudo)
print(len(conteudo))
