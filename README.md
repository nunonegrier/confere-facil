# Confere-facil
Agente que ajuda a identificar fraudes

Este agente utiliza 3 agentes para auxiliar o usuário a identificar uma possível fraude digital em curso:

- O primeiro agente aje como um pesquisador da área da segurança digital.
    A sua tarefa é a de interpretar a descrição da ocorrência original utilizando o conjunto de conhecimentos do LLM e completando-os com informações mais recentes através da pesquisa no Google.
    Seu objetivo principal é o de identificar o tipo de fraude em curso.

- O segundo agente aje como um especialista em análise de fraudes.
    Com base nos resultados da pesquisa do primeiro agente, ele formula entre 1 a 3 perguntas que serão feitas para o usuário com a finalidade de aprofundar as informações da descrição da ocorrência e melhorar a acertividade de análise de tipo e risco da fraude em curso.
    Assim como o primeiro agente, este também pode recorrer aos resultados de pesquisa do Google, após o recebimento das respostas às suas perguntas, para melhorar o resultado da análise.

- O terceiro agente aje com o um especialista em cibersegurança.
    Com base na análise prévia da fraude ele:
    - Fornece instruções claras para que o usuário possa evitar a fraude
    - Fornece os contatos dos canais de atendimento nos casos em que é são mencionados nomes de empresas ou serviços, públicos ou privados.
 
# Utilização

Pensado para ser um agente que possa ser utilizado por pessoas de diversas idades, e diferentes níveis de afinidade com soluções tecnológicas. A utilização do confere-fácil é extremamente simplificada:

- O usuário começa fornecendo uma descrição em linguagem coloquial da situação que ele percebe como estranha e pretende ver esclarecida
- Na sequência o agente apresenta ao usuário de 1 a 3 perguntas que vão auxiliar no processo de identificação, análise e prevensão de fraudes
- Por último o usuário recebe então a análise da ocorrência e as recomendações de segurança.

O uso de 3 camadas de agentes permite que tudo se inicie com uma primeira descrição da ocorrência fornecida pelo usuário, que pode apresentar falta de detalhes, omissões naturais de fatos e outras inconsistências naturais do intervalo entre a linguagem coloquial e a técnica. As camadas de análise posteriores se encarregam de completar essas lacunas e fornecer um resultado confiável.
      
