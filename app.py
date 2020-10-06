import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objs as go
from collections import Counter
import re
import matplotlib.pyplot as plt
import  seaborn as sns
import plotly.express as px
import  base64

main_bg = "img/fundo2.jpg"
main_bg_ext = "img/fundo2.jpg"

side_bg = "img/logo.jpg"
side_bg_ext = "img/logo.jpg"


st.markdown(
    f"""
    <style>

    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})

    
    }}
    
    .reportview-container .markdown-text-container {{
      font-family: monospace;
      color: white;
    }}
    
    .sidebar .sidebar-content {{
      
      background-image: linear-gradient(#2e7bcf,#2e7bcf);
    
      background: url("img/logo.jpg")
      
    }}

   .Widget>label {{
     color: white;
     font-family: monospace;
   }}

   [class^="st-b"]  {{
     color: white;
     font-family: monospace;
   }}
   
   .st-bb {{
     background-color: green;

   }}

   .st-at {{
     background-color: black;
   }}
  
 

   .reportview-container .main footer, .reportview-container .main footer a {{
    color: #0c0080;
   }}

   header .decoration {{
     background - image: none;
   }}
   
    </style>
    """,
    unsafe_allow_html=True
)



def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width = 600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()
    return bars

def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x),
        alt.Y(y),
        color = color,
        tooltip = [x, y]
    ).interactive()
    return scatter

def cria_correlationplot(df, colunas_numericas):
    cor_data = (df[colunas_numericas]).corr().stack().reset_index().rename(columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal
    base = alt.Chart(cor_data, width=500, height=500).encode( x = 'variable2:O', y = 'variable:O')
    text = base.mark_text().encode(text = 'correlation_label',color = alt.condition(alt.datum.correlation > 0.5,alt.value('white'),
    alt.value('black')))

    cor_plot = base.mark_rect().encode(color='correlation:Q')
    return cor_plot + text


# Sidebar principal
def menu():
    st.sidebar.header('**Menu Inicial**')
    page = st.sidebar.radio("", ('Sobre',
                                'Análise de Dados dos álbuns do artista NexoAnexo'))
    if page == 'Sobre':
        sobre()
    if page == 'Análise de Dados dos álbuns do artista NexoAnexo':
        analise_nexoanexo()


## Páginas principais ## --------------------------------------------------------------------------------


# Sobre o Projeto
def sobre():
    # Sobre o Projeto
    st.title('Análise de Dados dos álbuns do artista NexoAnexo')
    '''
    
    '''
    '''
    Essa é uma aplicação do projeto de análise de dados dos álbuns do artista NexoAnexo. Veja o notebook completo do projeto para um maior entendimento 
    (https://github.com/luislauriano/Data_Science/blob/master/Projeto_construcao.ipynb).
   
    O objetivo da aplicação e do projeto é que a partir das conclusões retiradas da análise de dados das músicas dos álbumns do artista, seja identificado fatores que ajudam ou contribuem um albúm ou música a ter sucesso e como isso pode ser usado para futuros lançamentos.

    
    '''
   #O Artista
    st.title('O artista NexoAnexo')
    st.image('img/logo.jpg', width=200)
    '''
    Nascido em 29 de janeiro de 1997, NexoAnexo, é um artista e produtor pernambucano, difusor da trap Music no Brasil. Nascido e criado na Zona Oeste do Recife e tido como uma das promessas nordestinas do trap nacional pela revista @RND, atualmente membro da banca e produtora HoodCave.
    '''
   # Informações
    st.title('Informações úteis da análise')

    '''
    Algumas coisas precisam ser definidas para entender a análise da aplicação:

O Spotify disponibiliza a popularidade de uma música, mas como é feito o cálculo da populariade?
A popularidade é calculada e baseia-se na maior parte no número total de reproduções que a faixa teve e quão recentes foram estas reproduções. Logo, as músicas que estão sendo tocadas com uma maior frequência atualmente terão uma popularidade maior do que as músicas que foram muito tocadas no passado.

`Como a popularidade das músicas podem alterar diariamente, para não interferir na análise, era preciso utilizar um conjunto de dados de um dia especifico, por esse motivo foi utilizado o conjunto de dados do dia 26-06-2020.`


O albúm Trap From Future é o único que de fato se trata de um albúm do artista NexoAnexo, sendo o seu primeiro e que foi lançado nesse ano de 2020. Real Plug e Trap de Cria são "mixtapes", porém no Spotify as duas mixtapes são consideras como albúm, logo, suas músicas serão levadas como consideração para a análise.

    

   
    '''

    st.title('Álbum e Mixtapes analisadas')

    st.title("**Álbum Trap From Future**")
    st.video("https://www.youtube.com/watch?v=4P0yqNpjcX8&list=PL6uovRkTzXcLrKY1FqPteY2ta8ngFYdp2")

    st.title('**Mixtape (Álbum) Trap de Cria**')
    st.video('https://www.youtube.com/watch?v=jV-xa_gF2CE&t=111s')

    st.title('**Mixtape (Álbum) Real Plug**')
    st.video('https://www.youtube.com/watch?v=3VPUm17eZt8&list=PL6uovRkTzXcLFpKBFinRv_PhE2_HV9buG')




    # Sobre o autor
    st.title('Sobre o autor')

    '''  
    Hello World! Me chamo Luis Vinicius, atualmente Graduando em Gestão da Informação na UFPE, uma quase Cientista de Dados, desenvolvedor em Python e apaixonado por Tecnologia, Inovação e Desenvolvimento de projetos. Tenho conhecimento na linguagem Python e suas principais bibliotecas para se trabalhar com Data Science, além de conhecimento em Machine Learning, SQL, Banco de dados relacionais, estatística para Data Science e Power BI.



    Meus outros projetos e portfólio completo você pode encontrar acessando o link abaixo:

    https://github.com/luislauriano/Data_Science
    
    Se você deseja me conhecer melhor e acompanhar minhas publicações na área de Data Science me adicione no linkedin!
    
    https://linkedin.com/in/luislauriano 
     
    '''


#Página da análise
def analise_nexoanexo():
    st.title('Análise de dados dos álbuns do artista NexoAnexo')

    file  = "data/NexoAnexoFinal.csv"
    file2 = "data/NexoAnexoFinal2.csv"
    if file is not None:
        df = pd.read_csv(file)
        df2 = pd.read_csv(file2)

        aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})
        colunas_numericas = list(aux[aux['tipos'] != 'object']['colunas'])
        colunas_object = list(aux[aux['tipos'] == 'object']['colunas'])
        colunas = list(df.columns)

        #Menu Análises
        st.sidebar.header('Análises')
        menu_analises = st.sidebar.radio("", ('Visão geral', 'Álbuns',
                                         ))
        if menu_analises == 'Visão geral':
            visao_geral(df, df2)

        if menu_analises == 'Álbuns':
            albuns(df)

def visao_geral(df, df2):
    # Albúm Real Plug Mixtape
    rmx = df.query("nome_do_album == 'Real Plug Mixtape' ")
    # Albúm Trap de Cria Mixtape
    tcm = df.query("nome_do_album == 'Trap de Cria Mixtape' ")
    # Albúm Trap From Future
    tff = df.query("nome_do_album == 'Trap from Future' ")

    #Inf basicas
    st.header('**Informações básicas**')
    '''
    
    '''
    ''' 
    Para um primeiro entendimento dos dados, considero importante saber quais são as músicas de cada albúm que estão sendo analisadas e a quantidade total de músicas dos três albúns. Dessa forma, tanto irá ajudar á construir perguntas futuras para a análise, como também retirar melhores conclusões e informações do que será analisado.
    '''

    ''' 
    Total de músicas do Álbum Real Plug: `8`

    Total de músicas do Álbum Trap de Cria: `10`

    Total de músicas do Álbum Trap From Future: `15`

    
    `Somando os três álbuns são 33 músicas analisadas`
    '''


    st.header("**O conjunto de dados**")

    ''' 
    O conjunto de dados do artista NexoAnexo foi coletado através da API do Spotify e não possui dados ausentes. Algumas colunas como duração da música fo retirada do conjunto de dados são uteis para o objetivo do projeto. Todos os registros passam alguma informação, entretanto, devido ao fato do albúm Real plug Mixtape ser o albúm mais antigo, sua popularidade apresenta muitos valores zero, tendo em vista, que a popularidade está relacionada as músicas que estão sendo ouvidas no momento.
    '''
    st.write(df)

    '''
    Você pode conferir como foi feita a coleta de dados do Spotify no projeto completo:
    https://github.com/luislauriano/Data_Science/blob/master/Projeto_construcao.ipynb
    '''




    st.header('**Gráfico das músicas com maior popularidade no momento**')


    dados = df[['nome_da_faixa', 'popularidade']].sort_values(ascending=False, by='popularidade').reset_index(drop=True)[:16]
    fig = go.Figure(data=[
    go.Bar(name='Confirmed', x=dados['nome_da_faixa'], y=dados['popularidade'])])
    st.plotly_chart(fig)
    '''
    As duas primeiras músicas que estão popular no momento são "Trap de Cria" do segundo albúm Trap de Cria e "Vem No Tum Tum" do mais recente albúm Trap From Future. Mas, o que chama atenção é a música "2020" do primeiro albúm Real Plug que está a frente de muitas músicas do recente albúm Trap From Future.
    '''

    st.header('**Relação das músicas com a média da Popularidade**')
    graph_retweet(df)

    '''
    Em sua maioria as músicas encontram-se abaixo da média, algo que não é bom. Porém, isso se dá pelo fato de a maioria das músicas que pertencem aos dois álbuns Real Plug e Trap de Cria, não possuírem uma popularidade tão alta no momento, por não serem albúns tão recentes. Enquanto, as músicas mais recentes e com popularidade alta pertencem ao albúm Trap From Future, logo, em menor quantidade, comparado a soma dos dois álbuns que vieram antes.
    
    '''

    st.header('**Gráfico de músicas que são consideras explicitas**')
    donut_explicita(df2)
    ''' 
    Por mais que algumas músicas de fato não sejam explicitas, como a música Vem No Tum Tum. O Spotify pode considerar a música explicita por conter alguma palavra que foge das suas diretrizes, algo comum na cena do Trap. Logo, a maioria das músicas dos albúns são consideradas explicitas.
    '''


    st.header('**Relação da popularide com a posicação das musicas**')
    dados2 = df[['posicao_da_faixa', 'popularidade']].sort_values(ascending=False, by='popularidade').reset_index(drop=True)
    '''
    A primeira música de um albúm pode se tornar popular por sempre iniciar a playlist do albúm, mas a primeira música que está com uma popularidade alta nem sempre é a mais ouvida. Por isso é preciso ter cuidado. Foi preciso analisar se a popularidade das músicas tinha relação com suas posições e se após a primeira música a popularidade continuava de acordo com suas posições.
    '''
    fig = go.Figure(data=[
    go.Bar(name='Músicas', x=dados2['posicao_da_faixa'], y=dados2['popularidade'])])
    st.plotly_chart(fig)

    '''
    Nota-se que se a posição das músicas tivessem relação com as suas popularidades, após a primeira música, as músicas seguintes deveriam de forma decrescente ir diminuindo suas popularidades, o que não acontece. 
    '''
    '''
    O que fica claro é que a popularidade de uma música só tem relação com a sua posição para a primeira música, devido que elas iniciam automaticamente a playlist do albúm, conseguemente é considerada ouvida e resultando num erro de maior popularidade.
    '''





def albuns(df):
    st.sidebar.subheader('Álbuns')
    albuns = st.sidebar.radio("", ('Trap From Future',
                                         'Trap de Cria (Mixtape)',
                                         'Real Plug (Mixtape)'))
    '''
    Lembrando que foi analisado os três álbuns do artista, considerados pelo spotify. Sendo Trap From Future de fato o primeiro e único álbum do artista, enquanto Trap de Cria e Real Plug são mixtapes (álbuns pequenos), porém o Spotify considerada as mixtapes como álbum.
    '''
    if albuns == 'Trap From Future':
        tff = df.query("nome_do_album == 'Trap from Future' ")
        st.title('**Albúm Trap From Future**')
        st.image('img/tff.jpg', width=400)
        '''
        
        '''
        ''' 
        Trap From Future trata-se do albúm mais recente do artista e diferente dos outros dois albúns analisados que na realidade são mixtapes, esse de fato pode ser considerado um albúm e o primeiro do artista. O albúm foi lançado no dia 12 de março de 2020, sendo considerado como o trabalho mais sólido do artista e até mesmo elogiado pelo artista que é referência na cena do trap, Matuê. Com uma capa de albúm futurista e cheia de referências, as músicas do albúm possuem uma versatilidade de estilo e estética totalmente diferente de músicas anteriores do artista.
        
        O álbum possui quinze músicas com uma grande versatilidade, indo da mistura brega e trap na música "Trap&Brega" à musica com participação internacional em "Drip Know Me". O que também foi possivel de notar é a leveza e "visão" do artista em suas músicas, sendo muito falado no albúm de suas ambições e desejos para uma vida melhor.
       
        '''

        st.subheader('**Gráfico comparativo da posição da música em relação á sua popularidade**')
        '''
        Com o gráfico é possivel observar que a popularidade das músicas que estão na posição um à cinco tem uma crescente, mas depois a popularidade não segue mais um padrão de acordo com a posição. A segunda música do albúm "Drip Know Me" que de acordo com a hipotese nula deveria ser a segunda mais ouvida, ocupa a sexta posição da popularidade do albúm, com uma popularidade igual á três.
        '''
        fig = go.Figure(data=[
        go.Bar(name='Popularidade', x=tff['nome_da_faixa'], y=tff['popularidade']),
        go.Bar(name='Posicao', x=tff['nome_da_faixa'], y=tff['posicao_da_faixa'])])
        st.plotly_chart(fig)




        st.subheader('**Gráfico de linha da popularidade das músicas do albúm**')

        '''
        Nota-se que nenhuma música possui a popularidade igual a zero, porém o fato de ser o albúm mais recente contribui para isso. Também é posivel notar que a música Trap & Brega cuja possui uma proposta diferente de músicas anteriores do artista e até mesmo de músicas da cena do rap/trap, possui uma das popularidades mais altas do albúm, no momento em que foi feita a coleta desses dados. 
        '''
        fig = px.line(tff, x="nome_da_faixa", y="popularidade")
        st.plotly_chart(fig)



        st.subheader('**Gráfico das músicas com maior popularidade no momento**')

        ''' 
        Por ser o albúm mais recente, coseguentemente a quantidade de músicas com uma popularidade alta é maior do que os outros dois álbuns. Além disso, músicas como "Marca Sem Roupa" e "Vem No Tum Tum" que possui estilo de trap explicito e falam sobre a relação com uma outra pessoa, foram bem acolhidas pelo público, sendo as maiores popularidades do albúm.
        '''
        dados = tff[['nome_da_faixa', 'popularidade']].sort_values(ascending=False, by='popularidade').reset_index(drop=True)[:15]
        fig = go.Figure(data=[
        go.Bar(name='Confirmed', x=dados['nome_da_faixa'], y=dados['popularidade'])])
        st.plotly_chart(fig)

        st.subheader('**Gráfico das músicas que estão abaixo da média**')
        '''
        Quatro músicas se encontram abaixo da média de popularidade, sendo elas: Fuck Cópias, Novo Rock, Zombieland e Baila Comigo?. A média de popularidade das músicas é igual a 2.63 e a média de popularidade das músicas do albúm Trap From Future é 4.13, por ser o álbum mais recente possui a maior média de popularidade. 
        
        '''
        fig = go.Figure(data=[
        go.Bar(name='Confirmed', x=tff['nome_da_faixa'], y=tff['frequencia_de_popularidade_das_musicas'][:15])])
        st.plotly_chart(fig)

    if albuns == 'Trap de Cria (Mixtape)':
        tcm = df.query("nome_do_album == 'Trap de Cria Mixtape' ")
        st.title('Albúm (Mixtape) Trap de Cria')

        '''
        '''
        '''
        
        '''
        st.image('img/tcm.jpg', width=400)

        '''
                        O albúm ou mixtape "Trap de Cria" foi o segundo albúm do artista e seu lançamento aconteceu no dia 29 de julho de 2019, diferente do primeiro albúm "Real Plug", o alcance desse albúm foi maior e era de se esperar até mais alcance e visibilidade.Com uma pegada de músicas no estilo trap explícito, o álbum obtive músicas que receberam um bom alcance, comparado a músicas anteriores, porém sinto que o alcance, especificamente desse albúm ficou no "gostinho de quero mais", pela qualidade e empenho que foi colocado pelo artista e todos que de alguma forma contribuíram na construção do albúm.
                        
                        Ao total foram dez músicas, duas a mais que o primeiro albúm. Os destaques ficam para as músicas: "E ai Fake" construída com base na polêmica das conversas íntimas vazadas do jogador Neymar, "Video Call" e "PJL" que contou com a participação de integrantes da Hoodcave, produtora da qual o artista faz parte.
        '''



        st.subheader('**Gráfico comparativo da posição da música em relação á sua popularidade**')
        '''
        Assim como no albúm Trap From Future, a música mais popular deste albúm é a que está na primeira posição e por mais que muitas músicas do albúm não estejam com a popularidade tão alta, ainda é possivel observar que a música "Isso Que É Foda" mesmo ocupando a penúltima posição do albúm é a segunda com maior popularidade.
        '''
        fig = go.Figure(data=[
            go.Bar(name='Popularidade', x=tcm['nome_da_faixa'], y=tcm['popularidade']),
            go.Bar(name='Posicao', x=tcm['nome_da_faixa'], y=tcm['posicao_da_faixa'])])
        st.plotly_chart(fig)

        st.subheader('**Gráfico de linha da popularidade das músicas do albúm**')

        '''
        Mesmo após o lançamento do albúm mais recente "Trap From Future", nota-se que a quantidade de músicas do albúm acolhida pelo público foi de fato maior do que o primeiro albúm "Real Plug Mixtape". Sendo até os dias atuais, ouvida uma parte significativa das músicas que compoem o albúm, com apenas a música "Pjl" possuindo uma frequência igual a zero.
        '''
        fig = px.line(tcm, x="nome_da_faixa", y="popularidade")
        st.plotly_chart(fig)

        st.subheader('**Gráfico das músicas com maior popularidade no momento**')
        '''
        
        '''
        ''' 
        O destaque do álbum fica para a música "Trap de Cria" que possui a maior popularidade no momento, além de ser uma das mais ouvidas dos três álbuns, tornando-se uma representação do que o albúm propoem e atraindo o público para as músicas seguintes do álbum. As outras duas músicas seguintes da Trap de Cria e que compoem o top três de músicas populares no momento são "Isso que é Foda" e "A lista das Bandidas" que contagiam os ouvintes com o estilo trap explícito.  
        
        '''
        dados = tcm[['nome_da_faixa', 'popularidade']].sort_values(ascending=False, by='popularidade').reset_index(
            drop=True)[:15]
        fig = go.Figure(data=[
            go.Bar(name='Confirmed', x=dados['nome_da_faixa'], y=dados['popularidade'])])
        st.plotly_chart(fig)

        st.subheader('**Gráfico das músicas que estão abaixo da média**')
        '''
        Apenas duas músicas se encontram acima da média de popularidade, sendo elas: Trap de Cria e Isso que é Foda. Como já mencionado anteriormente, a baixa quantidade de músicas acima da média se da por a maioria das músicas que estão sendo ouvidas no momento e possuirem maior popularidade pertecerem ao álbum mais recente Trap From Future. A média de popularidade das músicas do albúm Trap de Cria é 2.1, possuindo a segunda maior média de popularidade. 

        '''
        fig = go.Figure(data=[
            go.Bar(name='Confirmed', x=tcm['nome_da_faixa'], y=tcm['frequencia_de_popularidade_das_musicas'][:15])])
        st.plotly_chart(fig)

    if albuns == 'Real Plug (Mixtape)':
        rmx = df.query("nome_do_album == 'Real Plug Mixtape' ")
        st.title('Albúm (Mixtape) Real Plug')

        '''


        '''
        st.image('img/rp.jpg', width=400)

        '''
           O albúm ou mixtape Real Plug é o mais antigo de todos e seu lançamento foi no dia 15 de maio de 2018, então é bem provavel que a popularidade de suas músicas não sejam tão altas, mas o albúm conta com músicas que tiveram bons números e feedback do público. Um exemplo é a música "2020", sendo a música que ganhou mais alcance e "caiu na graça dos fãs", bem reconhecida e reponsável por atrair público até os dias de atuais. No canal do artista, o clipe da música "2020" é o terceiro mais acessado, com 28 mil views.
           
           No total são oito músicas, com destaque para a música "2020", que foi a principal responsável por trazer alcance ao álbum.
        '''

        st.subheader('**Gráfico comparativo da posição da música em relação á sua popularidade**')
        '''
         Por se tratar do albúm mais antigo, a primeira música do albúm não é a mais ouvida, como nos dois mais recentes álbuns. Por outro lado, ainda que esteja na última posição do albúm, a música "2020" é a única música do albúm que ainda tem a popularidade em alta e se a sua popularidade for comparada à popularidade de músicas do albúm mais recente "Trap From Future", "2020" pode ser considerada de fato um sucesso!
         
         Ainda que, se os três álbuns forem comparados, a música "2020" é a única que possui a popularidade em alta, estando na ultima posição de um álbum.
        '''
        fig = go.Figure(data=[
            go.Bar(name='Popularidade', x=rmx['nome_da_faixa'], y=rmx['popularidade']),
            go.Bar(name='Posicao', x=rmx['nome_da_faixa'], y=rmx['posicao_da_faixa'])])
        st.plotly_chart(fig)

        st.subheader('**Gráfico de linha da popularidade das músicas do albúm**')

        '''
         É possivel observar que de fato a música 2020 é um sucesso, por ainda possuir uma popularidade alta mesmo fazendo parte do álbum mais antigo. As outras músicas do álbum possui a popularidade igualmente a zero, logo, significa que a partir do calcúlo de popularidade do Spotify, as músicas não estão sendo tão ouvidas a ponto de possuir uma popularidade maior que zero.
        '''
        fig = px.line(rmx, x="nome_da_faixa", y="popularidade")
        st.plotly_chart(fig)

        st.subheader('**Gráfico das músicas com maior popularidade no momento**')
        '''

        '''
        ''' 
         É incrivel como a música "2020" ainda possui um bom alcance! Mesmo que seja a única música do álbum com a popularidade alta atualmente, a música está a frente de grandes músicas do albúm mais recente "Trap From Future", como as músicas "Wow!", "Grife" e "Não Posso Morrer Novo Mano" que também são destaques do álbum Trap From Future.

        '''
        dados = rmx[['nome_da_faixa', 'popularidade']].sort_values(ascending=False, by='popularidade').reset_index(
            drop=True)[:15]
        fig = go.Figure(data=[
            go.Bar(name='Confirmed', x=dados['nome_da_faixa'], y=dados['popularidade'])])
        st.plotly_chart(fig)

        st.subheader('**Gráfico das músicas que estão abaixo da média**')
        '''
        Apenas uma música se encontra acima da média de popularidade, sendo a música 2020. Por mais que seja a unica, é de tamanha expressão uma música que pertence ao albúm mais antigo ainda ser bastante ouvida e possuir popularidade maior que músicas recentes. Além de ser uma música que ainda é aclamada pelo público, a música trata o ano de 2020 como o ano da profesia, onde coisas iriam acontecer para o artista.

        '''
        fig = go.Figure(data=[
            go.Bar(name='Confirmed', x=rmx['nome_da_faixa'], y=rmx['frequencia_de_popularidade_das_musicas'][:15])])
        st.plotly_chart(fig)




def graph_retweet(df):

    # Agrupamento dos dados
    df_retweet = Counter(df.frequencia_de_popularidade_das_musicas)
    labels = list(df_retweet.keys())
    values = list(df_retweet.values())

    # Plot
    data=[go.Pie(labels=labels, values=values, hole=.5, marker = {'colors': ['#B5ACA7', '#0000B3']})]
    st.plotly_chart(data)

def donut_explicita(df2):

    # Agrupamento dos dados
    df_retweet = Counter(df2.musica_explicita)
    labels = list(df_retweet.keys())
    values = list(df_retweet.values())

    # Plot
    data=[go.Pie(labels=labels, values=values, hole=.5, marker = {'colors': ['#B5ACA7', '#0000B3']})]
    st.plotly_chart(data)








menu()