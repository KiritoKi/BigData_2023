import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

# Exemplo de nomes de grupos de pesquisa
nomes_grupos_pesquisa = [
    "Técnicas de Mineração de Dados",
    "Audiovisual Noticioso e Contemporaneidade",
    "Atenção Integral à Saúde da Criança e Adolescente - AISCA",
    "Aspectos Profiláticos e Terapêuticos da Atividade Física na Saúde da Mulher",
    "ARISE - Arqueologia Interativa e Simulações Eletrônicas",
    "A3EN-Grupo de Apoio, Aprimoramento e Atualização em Educação Nutricional",
    "Melhoramento Genético Florestal de Espécies Exóticas e Nativas",
    "Linguagens,Cultura e ensino: o uso da língua na formação técnica e tecnológica",
    "Grupo de Pesquisa e Extensão Redes, Questões Geracionais e Políticas Públicas",
    "Grupo de Estudo e Pesquisa em Climatologia do Cerrado",
    "Arquivos, fontes e narrativas: entre cidade, arquitetura e design",
    "Autenticidade e alteridade nos processos sociais, educacionais e profissionais",
    "Biodiversidade, gestão territorial e sustentabilidade dos agroecossistemas na Amazônia",
    "Grupo de Pesquisas e Práticas em Gênero, Diversidade e Sexualidade",
    "Fitossanidade e Agroecossistemas",
    "Fisiologia e Biologia do Desenvolvimento",
    "Feminismos e História das Mulheres",
    "Estudos sobre a morte, o morrer e o processo de luto",
    "ESTUDOS FAUNÍSTICOS DO ESTADO DA BAHIA",
    "ESTUDOS E ENSINO DO TEXTO - GEENTE"
]

# Pré-processamento de texto
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('portuguese'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

corpus = [preprocess_text(nome) for nome in nomes_grupos_pesquisa]

# Criação do dicionário e do corpus
dictionary = corpora.Dictionary(corpus)
corpus = [dictionary.doc2bow(text) for text in corpus]

# Análise de tópicos (LDA)
lda_model = models.LdaModel(corpus, num_topics=40, id2word=dictionary, passes=10)

# Obtendo a distribuição de tópicos para cada grupo de pesquisa
topic_distribution = [lda_model[doc] for doc in corpus]

# Calculando a pontuação do tópico mais relevante para cada grupo de pesquisa
most_relevant_topic_scores = [max(topic, key=lambda x: x[1])[1] for topic in topic_distribution]

# Preparação dos dados para o gráfico
nomes_grupos_pesquisa = [nome[:30] + "..." if len(nome) > 30 else nome for nome in nomes_grupos_pesquisa]
topicos = [f"Tópico {i+1}" for i in range(len(lda_model.get_topics()))]

# Configurando o estilo do gráfico
plt.figure(figsize=(12, 6))
plt.barh(nomes_grupos_pesquisa, most_relevant_topic_scores, color='skyblue')
plt.xlabel('Pontuação do Tópico Mais Relevante')
plt.ylabel('Nomes dos Grupos de Pesquisa')
plt.title('Pontuação do Tópico Mais Relevante para Grupos de Pesquisa')
plt.yticks(fontsize=8)
plt.gca().invert_yaxis()

# Mostrando o gráfico
plt.tight_layout()
plt.show()
