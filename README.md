# Confere-fraude-facil
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

Pensado para ser um agente que possa ser utilizado por pessoas de diversas idades e diferentes níveis de afinidade com soluções tecnológicas, o Confere-fácil tem uma usabilidade extremamente simplificada:

- O usuário começa fornecendo uma descrição em linguagem coloquial da situação que ele percebe como estranha e pretende ver esclarecida
- Na sequência o agente apresenta ao usuário de 1 a 3 perguntas que vão auxiliar no processo de identificação, análise e prevensão de fraudes
- Por último o usuário recebe então a análise da ocorrência e as recomendações de segurança.

O uso de 3 camadas de agentes permite que tudo se inicie com uma primeira descrição da ocorrência fornecida pelo usuário, que pode apresentar falta de detalhes, omissões naturais de fatos e outras inconsistências naturais do intervalo entre a linguagem coloquial e a técnica. As camadas de análise posteriores se encarregam de completar essas lacunas e fornecer um resultado confiável:

# 1º Exemplo de desenvolvimento do conhecimento a partir de uma descrição simples e incompleta:

## - Usuário: Recebi um pedido de dinheiro emprestado no whatsapp

O primeiro agente recebe o prompt e utiliza o conjunto de conhecimentos do LLM mais a pesquisa do google para identificar o tipo da fraude e passar essa informação para o segundo agente
O segundo agente então analisa novamente a descrição mais o resultado da pesquisa do primeiro agente e define de 1 a 3 perguntas que permitirão que ele complemente as informações:

## - Segundo agente:

   1.  Você reconheceu o número de telefone de onde partiu o pedido de dinheiro?
   2.  Você tentou confirmar a identidade da pessoa por outro meio de comunicação além do WhatsApp (por exemplo, ligação telefônica, contato pessoal)?
   3.  Qual foi a justificativa apresentada para o pedido de dinheiro?
      
## - Usuário:

   1.  sim, é o telefone de um amigo
   2.  tentei, mas ela não atendeu, respondeu só por mensagem
   3.  disse que tinha esquecido os cartões em casa e precisava pagar uma conta urgente

Com essas informações, o terceiro agente consegue então validar as informações geradas desde o início do processo e fornecer as recomendações de segurança, os contatos das empresas (sempre que a descrição inicial contenha alguma menção a uma empresa ou serviço, público ou privado) e por último, a lista "O que você NÃO deve fazer".

## - Terceiro agente:

   Para evitar cair nesse tipo de fraude, siga estas instruções:

   1.  **Confirme a identidade:** Nunca transfira dinheiro ou forneça informações pessoais sem confirmar a identidade da pessoa que está solicitando. A melhor maneira de fazer isso é entrar em contato com a pessoa por meio de 
um canal de comunicação diferente, como uma ligação telefônica ou pessoalmente.
   2.  **Desconfie de mensagens urgentes:** Golpistas geralmente usam o senso de urgência para pressionar as vítimas a agirem impulsivamente. Se você receber uma mensagem pedindo dinheiro com urgência, pare e pense antes de agir.
   3.  **Verifique as informações:** Se você receber uma mensagem de um amigo ou familiar pedindo dinheiro, verifique as informações fornecidas na mensagem. Por exemplo, você pode perguntar sobre detalhes que só a pessoa real 
saberia.
   4.  **Proteja sua conta do WhatsApp:** Ative a verificação em duas etapas no WhatsApp para adicionar uma camada extra de segurança à sua conta. Isso dificulta que os golpistas acessem sua conta, mesmo que tenham seu número 
de telefone.
   5.  **Informe seus contatos:** Avise seus amigos e familiares sobre esse tipo de golpe para que eles também possam se proteger.

   **Canais de Atendimento:**

   Como a mensagem foi recebida via WhatsApp, e a situação envolve um possível amigo, tente contato direto com ele através de outros meios (telefone, pessoalmente) para confirmar a veracidade do pedido. Se você suspeitar que a conta do seu amigo foi comprometida, alerte-o para que ele possa avisar seus contatos.

   **O que você NÃO deve fazer:**

   1.  **Não transfira o dinheiro:** Sob nenhuma circunstância transfira o dinheiro solicitado sem antes confirmar a veracidade do pedido diretamente com seu amigo por meio de um canal de comunicação seguro.
   2.  **Não forneça informações pessoais:** Não compartilhe dados pessoais ou bancários com o remetente da mensagem.
   3.  **Não clique em links suspeitos:** Se a mensagem contiver links, não clique neles, pois podem ser maliciosos.
   4.  **Não ignore a situação:** Alerte seu amigo sobre a possível clonagem de sua conta do WhatsApp e avise seus contatos sobre a tentativa de golpe.

# 2º Exemplo de desenvolvimento do conhecimento a partir de uma descrição simples e incompleta:

## - Usuário: Recebi um boleto por email

## - Segundo agente

   1.  Quem é o emissor do boleto? Você reconhece a empresa ou instituição que está cobrando?
   2.  O e-mail parece legítimo? Verifique o endereço de e-mail do remetente, erros de ortografia ou gramática e links suspeitos.
   3.  Qual é o valor do boleto e a data de vencimento? Esses dados correspondem a alguma compra ou serviço que você contratou?

## - Usuário:
   1.  boleto do Itaú, a empresa que está cobrando é a Vivo
   2.  o email foi enviado por cobranca@vivo.uol.com.br
   3.  R$ 223,46 com vencimento no dia 21/05, eu utilizo a Vivo, mas já paguei a minha conta no começo do mês

## - Terceiro agente

  Com base na análise da fraude que você descreveu, aqui estão as instruções claras para evitar cair nesse golpe, juntamente com os contatos relevantes e uma lista do que você não deve fazer:

**Instruções para Evitar a Fraude:**

1.  **Verifique Sempre a Autenticidade:** Antes de pagar qualquer boleto, especialmente os recebidos por e-mail, verifique a autenticidade diretamente com a empresa ou instituição mencionada. Não confie apenas nas informações do boleto ou do e-mail.
2.  **Cuidado com E-mails Suspeitos:** Desconfie de e-mails com boletos anexados, principalmente se o remetente for desconhecido ou se o endereço de e-mail parecer suspeito (mesmo que superficialmente parecido com o oficial).
3.  **Confirme os Dados:** Verifique se os dados do boleto (CNPJ, razão social do emissor, valor, etc.) correspondem aos da empresa/serviço que você utiliza.
4.  **Mantenha seus Dados Seguros:** Nunca compartilhe informações financeiras ou pessoais por e-mail ou telefone, a menos que você tenha iniciado o contato com uma empresa/instituição confiável.
5.  **Monitore Suas Contas:** Acompanhe regularmente suas contas bancárias e faturas de cartão de crédito para identificar rapidamente quaisquer atividades suspeitas.

**Canais de Atendimento da Vivo e Itaú:**

*   **Vivo:**
    *   **Telefone:** 103 15 de qualquer telefone
    *   **Site:** [https://www.vivo.com.br/](https://www.vivo.com.br/)
    *   **Aplicativo:** Meu Vivo (disponível para Android e iOS)
*   **Itaú:**
    *   **Telefone:**
        *   3003 3030 (capitais e regiões metropolitanas)
        *   0800 720 3030 (demais localidades)
    *   **Site:** [https://www.itau.com.br/](https://www.itau.com.br/)
    *   **Aplicativo:** Itaú (disponível para Android e iOS)

**O Que Você Não Deve Fazer:**

1.  **Não Pague o Boleto:** Sob nenhuma circunstância pague o boleto que você recebeu, pois ele é quase certamente fraudulento.
2.  **Não Clique em Links Suspeitos:** Não clique em links ou baixe arquivos de e-mails suspeitos.
3.  **Não Forneça Informações Pessoais:** Não forneça seus dados pessoais, bancários ou financeiros em resposta a e-mails ou telefonemas suspeitos.
4.  **Não Ignore a Situação:** Não ignore a situação. Entre em contato com a Vivo e o Itaú para relatar o ocorrido e confirmar a fraude.
5.  **Não Tarde em Registrar um B.O.:** Se confirmado que é uma fraude, não demore em registrar um Boletim de Ocorrência (B.O.) para se proteger legalmente e ajudar nas investigações.

![confere-fraude-facli_01](https://github.com/user-attachments/assets/f104537f-d966-421b-9a74-1e0948e0cf3b)

![confere-fraude-facli_02](https://github.com/user-attachments/assets/07b77408-2a73-4c38-bc20-577f935e6ba1)

![confere-fraude-facli_03](https://github.com/user-attachments/assets/dc8d2bd6-7563-402f-98dc-0688aca2d76a)
