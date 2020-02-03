import pysrt
import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.srt"
conteudo = ''
numMinimoRepeticoes=0
def contar_conteudo_e_remover_excesso(conteudo):
    """This function get the words and convert her in one array [[word, weight], ....[word,weight]]
    \n [return: array]
    """
    palavras = []
    e=0
    boost =conteudo[0:int(len(conteudo)/50)]
    x=0
    while(x<len(boost)):
        y=x+1
        d=0
        while(y<len(boost)):
            if(boost[x]==boost[y]):
                del(boost[y])
                d=d+1
            y=y+1
        boost[x]=[boost[x],d]
        x=x+1
    boost.sort(key=lambda x: x[1], reverse=True)
    for x in boost:
        conteudo[boost.index(x)]=x[0]
    for x in range(0,len(conteudo)):
        d = 0
        for y in range(x+1, len(conteudo)):
            if(conteudo[x]==conteudo[y-d]):
                del(conteudo[y-d])
                d+=1
        if(len(conteudo)>x):
            if(d>=numMinimoRepeticoes):
                palavras.append((conteudo[x], d+1))


    return palavras

def filtrar_conteudo(conteudo):
    """this function is the filter for the words, 
    this function get the words and filter her
    \n [return: string, int]"""
    conteudo = conteudo.split()
    d=0
    for x in range(0, len(conteudo)):
        if(conteudo[x-d].isalpha()==0):
            del(conteudo[x-d])
            d=d+1
            continue
        if(conteudo[x-d].isalnum()==0):
            del(conteudo[x-d])
            d=d+1
            continue
        if (conteudo[x-d].count('wiki') > 0):
            del (conteudo[x-d])
            d = d + 1
            continue
    tamanho = len(conteudo)
    return conteudo,tamanho

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
    with open(lingua1+'-pt.txt','w+', encoding="utf-8") as arq:
        arq.write('{'+'"tamanho":{},'.format(tamanho)+'"palavras":[')
        arq.write("\n")
        arq.write("\n")
        for z in range(0, len(conteudo)):
            arq.write('{"word":"'+conteudo[z][0]+'",repeted":{}'.format(conteudo[z][1])+',"porcent":{}'.format((conteudo[z][1]/tamanho)*100)+'},')
            arq.write("\n")
            porcentagem =porcentagem + ((conteudo[z][1]/tamanho)*100 )
        arq.write('],"porcentagem":{}'.format(porcentagem)+'}')
        print('arquivo salvo como {}-pt.txt'.format(lingua1))

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)
        subs = pysrt.open(entry, encoding='iso-8859-1')
        for x in subs:
            conteudo = '{} {}'.format(conteudo, x.text.lower()) 
print('_____________________________________________________\n\n___________________________')
print("filtrando conteudo")
conteudo,tamanho = filtrar_conteudo(conteudo)
print("contando conteudo e removendo excesso")
conteudo = contar_conteudo_e_remover_excesso(conteudo)
print("ordenando conteudo")
conteudo = ordenar_conteudo(conteudo)
print("arquivando")
arquivar(conteudo, 'English', tamanho)
print("\n\n\n\n")
print(conteudo)
print(len(conteudo))