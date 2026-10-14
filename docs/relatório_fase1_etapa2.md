1.	Informe quantos número de árvores foram utilizados no motor NLU.

      Foram utilizadas 80 arvores de decisão como mostrado no trecho do codigo abaixo 
        self.classifier = RandomForestClassifier(n_estimators=80, random_state=42)
  	
3.	Informa qual o valor de threshold foi utilizado no processo de limiar de confiança
       limiar_threshold=0.60

       limitado a 60% de confiança.
   
4.	Coloque o resultado da primeira execução
      --- BATERIA DE TESTES DE ESTRESSE NLU ---
      
      Entrada: 'Tenho 30 kg de banana para doar'
      Intenção: cadastrar_doacao | Confiança: 0.93
      Retorno: Intenção 'cadastrar_doacao' identificada com 92.5% de confiança.
      
      Entrada: 'Nossa instituição precisa de mantimentos'
      Intenção: fallback | Confiança: 0.41
      Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
      Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?
      
      Entrada: 'Qual é a receita de bolo de cenoura?'
      Intenção: fallback | Confiança: 0.49
      Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
      Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?
      
      Entrada: 'coisa comida doar la'
      Intenção: fallback | Confiança: 0.42
      Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
      Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?


5.	Descreva como você poderia fazer para os resultados de testes serem melhores, aumento o grau de confiança dos resultados

    aumentando o numero de frases do treinamento.
 
    
6. 	Descreva por que o Random Forest foi o melhor método de Machine Learning para essa fase.

     Ele foi a melhor opção pois usa mais arvores de decisão assim complementando código reduzindo o numero de erros e ele conseguiu identificar uma intenção de doação com 92,5% de confiança.

     
