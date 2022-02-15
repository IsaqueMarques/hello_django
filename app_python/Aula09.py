#import shutil



def escrever_arquivo(texto):
    diretorio = 'C:/Projetos/testando.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(texto):
    diretorio = 'C:/Projetos/testando.txt'
    arquivo = open(diretorio, 'r')
    texto = arquivo.read()
    print(texto)



def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#def copia_arquivo(nome_arquivo):
    #shutil.copy(nome_arquivo, 'C:/Projetos/')

#def move_arquivo(nome_arquivo):
    #shutil.move(nome_arquivo,'C:/Projetos/testando.txt')

if __name__ == '__main__':
    #aluno = 'PIPICO,10,4,5,10\n'
    #atualizar_arquivo('notas.txt', aluno)
    #media_notas('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    #copia_arquivo('notas.txt')
    #move_arquivo('notas_txt')
    #escrever_arquivo('Chuck Noris.\n')
    #atualizar_arquivo('Terceira linha.\n')
    #ler_arquivo('testando.txt')