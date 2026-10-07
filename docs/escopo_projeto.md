# Escopo do Projeto – MESAFARTAI

## 1. Problema de Negócio

Diariamente, alimentos próprios para consumo são descartados por supermercados, restaurantes, feirantes e produtores devido ao excesso de estoque, proximidade da data de validade ou pequenos defeitos estéticos.

Ao mesmo tempo, ONGs, abrigos e cozinhas comunitárias enfrentam dificuldades para conseguir alimentos suficientes para atender pessoas em situação de vulnerabilidade.

O **MESAFARTAI** busca contribuir para a solução desse problema por meio de uma plataforma que facilita a comunicação entre doadores e instituições receptoras. Utilizando Inteligência Artificial e recursos de logística, o sistema pretende tornar o processo de doação mais rápido, simples e eficiente, reduzindo o desperdício de alimentos e contribuindo para o combate à fome.

O projeto está alinhado à **ODS 2 da ONU – Fome Zero e Agricultura Sustentável**.

---

## 2. Público-alvo

O MESAFARTAI possui dois públicos principais:

### Doadores

Supermercados, restaurantes, feirantes, produtores e outros estabelecimentos ou pessoas que possuam alimentos adequados para consumo disponíveis para doação.

Por meio do chat, o doador poderá informar os alimentos disponíveis, suas quantidades e prazos de validade.

### ONGs

ONGs, abrigos, cozinhas comunitárias e outras instituições que necessitam de alimentos para atender pessoas em situação de vulnerabilidade.

O sistema auxiliará essas instituições na solicitação de alimentos e na conexão com doações disponíveis.

---

## 3. Intenções tratadas pelo sistema

O chatbot será inicialmente desenvolvido para identificar quatro intenções:

### `cadastrar_doacao`

Identifica quando um usuário deseja disponibilizar alimentos para doação.

**Exemplo:**  
"Tenho 30 kg de arroz para doar e precisa ser retirado até amanhã."

### `solicitar_alimentos`

Identifica quando uma ONG deseja solicitar alimentos.

**Exemplo:**  
"Estamos precisando de arroz e feijão para nossa cozinha comunitária."

### `consultar_status`

Identifica quando o usuário deseja consultar a situação de uma doação ou solicitação.

**Exemplo:**  
"Gostaria de saber o status da minha doação."

### `fora_de_escopo`

Identifica mensagens que não possuem relação com as funcionalidades oferecidas pelo MESAFARTAI.

**Exemplo:**  
"Qual será o resultado do jogo hoje?"

O sistema também contará com um mecanismo de **Threshold/Fallback**, permitindo solicitar que o usuário reformule sua mensagem quando o modelo não possuir confiança suficiente para identificar corretamente uma intenção.

---

## 4. Dados coletados pelo chat

Durante a interação com o sistema, poderão ser coletadas informações necessárias para o funcionamento da plataforma.

### Dados do usuário

- Nome;
- Tipo de usuário (DOADOR ou ONG);
- CEP;
- Localização;
- Telefone.

### Dados relacionados aos alimentos

- Tipo ou descrição do alimento;
- Quantidade;
- Unidade de medida (kg, caixas ou unidades);
- Data ou prazo de validade;
- Status da doação.

Parte dessas informações poderá ser identificada automaticamente nas mensagens utilizando **Processamento de Linguagem Natural (NLU)** e **Expressões Regulares (Regex)**.

---

## 5. Matchmaking Logístico

Após o cadastro de uma doação, o sistema utilizará informações de localização para auxiliar na identificação de uma ONG receptora próxima ao doador.

O projeto utilizará o algoritmo **KNN** no processo de matchmaking logístico, buscando facilitar o direcionamento dos alimentos e reduzir o tempo entre a disponibilização e o recebimento da doação.

---

## 6. Identidade Visual

A identidade visual do MESAFARTAI foi desenvolvida buscando representar a união entre **alimentação, solidariedade, acolhimento e tecnologia**.

O símbolo utiliza o conceito de **mãos acolhendo alimentos**, representando solidariedade e cuidado, combinado com elementos semelhantes a **circuitos digitais**, representando a Inteligência Artificial e a tecnologia empregada no projeto.

A paleta utiliza verde, laranja, amarelo/dourado, vermelho e tons claros, buscando transmitir esperança, sustentabilidade, solidariedade, alimento, acolhimento e a importância social do combate à fome.

---

## 7. Prompt utilizado para criação do logotipo

O seguinte prompt foi utilizado para geração do logotipo do MESAFARTAI por meio de Inteligência Artificial:

> Crie um logotipo para o projeto **MESAFARTAI**, com uma identidade visual moderna, acolhedora e profissional.
>
> O logotipo deve unir visualmente os conceitos de **alimentação, solidariedade, acolhimento e Inteligência Artificial**. Utilize como símbolo principal **mãos acolhendo ou sustentando alimentos**, combinado de forma sutil com **circuitos ou conexões digitais**, representando a tecnologia e a IA assistiva.
>
> A identidade visual deve transmitir **esperança, união, combate à fome e impacto social**, evitando uma aparência triste ou pesada.
>
> Utilize uma paleta de cores harmoniosa composta principalmente por:
>
> - **Verde:** esperança, sustentabilidade e vida;
> - **Laranja:** solidariedade, acolhimento e ação;
> - **Amarelo/dourado:** alimento, prosperidade e mesa farta;
> - **Vermelho:** apenas em pequenos detalhes, representando a urgência do combate à fome;
> - **Creme/bege:** equilíbrio, humanidade e acolhimento.
>
> Adicionar o nome **MESAFARTAI** com uma tipografia moderna, simples e de fácil leitura. O **“AI”** pode receber um detalhe visual relacionado à tecnologia para representar Inteligência Artificial.
>
> O design deve ser **minimalista, vetorial, limpo e facilmente reconhecível**, funcionando tanto como logotipo completo quanto como ícone do sistema, em aplicações como GitHub, Streamlit, dashboards e apresentações.

---

## 8. Tecnologias previstas

O desenvolvimento do MESAFARTAI utilizará principalmente:

- Python;
- Streamlit;
- Scikit-Learn;
- Processamento de Linguagem Natural (NLU);
- Regex;
- KNN;
- SQLite3.

---

**MESAFARTAI – Logística e Inteligência Assistiva no Combate à Fome**
