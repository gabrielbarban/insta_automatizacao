#importando as bibliotecas
from instapy import InstaPy
from instapy.util import smart_run

#credenciais de acesso, no caso preencha
#com seu username e password do Instagram
insta_username = 'usuario'
insta_password = 'senha'

#armazenar uma nova sessão InstaPy na variável session
#headless_browser=True significa que o bot será executado
#em background
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=True
)

#aqui estou criando um array com uma lista de comentários
#o bot irá usar esta array para enviar os comentários nas
#fotos, de forma aleatória
#o conjunto de caracteres @{} será substituído pela
#marcação da pessoa que está recebendo o comentário
#note que é possível enviar emojis, para isso basta
#digitar o code do emoji desejado. Por exemplo:
#:+1: é o famoso sinal de joinha

comentarios = [
    u'@{}é o cara! :muscle:',
    u'Top demais :Brazil:',
    u'@{} gordim patrão!!!',
    u'Curti :+1:',
    u'Falo nada, só óleo :eyes:',
]

#aqui a brincadeira começa. Usando o objeto session
#declarado anteriormente, abrimos uma smart_run do 
#InstaPy
with smart_run(session):

    #configurações gerais
    #os parâmetros abaixo são auto-explicativos
    #você pode calibrá-los de acordo com seu
    #gosto. Existem outros, disponíveis na 
    #documentação do projeto, na qual falarei sobre
    #mais tarde
    session.set_relationship_bounds(
        enabled=True,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=4590,
        min_followers=1,
        min_following=1)

    #aqui precisei configurar o skip_private para False
    #caso contrário o InstaPy ignora contas configuradas
    #como privadas, mesmo sendo seu amigo
    session.set_skip_users(skip_private=False)

    #aqui estamos setando a matriz de comentários
    session.set_comments(comentarios)
    #em seguida estamos dizendo ao bot que ele irá comentar
    #em 100% das fotos que visitar
    session.set_do_comment(enabled=True, percentage=100)

    #aqui estamos dizendo ao bot para dar o like em 100% dos posts
    session.set_do_like(True, percentage=100)

    #definir a lista de perfis nos quais você irá comentar e dar like
    #nas fotos e vídeos
    #o primeiro parâmetro é a lista de perfis
    #amount=10 é a quantidade de posts que o bot irá visitar
    #randomize=True diz para o bot pegar posts aleatoriamente, ao invés de
    #dos mais novos para os mais antigos
    #media='None' significa fotos e vídeos
    #se quiser apenas fotos, use media='Photo', se quiser vídeo use
    #media='Video'
    session.interact_by_users(
        ['usuario1', 'usuario2'],
        amount=10,
        randomize=True,
        media='Photo'
    )
