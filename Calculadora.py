

def Calculadora(): 
  resultado=0
  def Calcular(resultado=resultado): 
      
      numero1=eval(input('Insira o primeiro número: '))
      
      numero2=eval(input('Insira o segundo número: '))
      
      operador=eval(input('Escolha o número da operação que deseja:\n (1) Multiplicação\n (2) Soma\n (3) Divisão \n (4) Subtração\n --> '))
      
      if operador==1:
         resultado=numero1*numero2
         print(resultado)
      elif operador==2: 
         resultado=numero1+numero2
         print(resultado)     
      elif operador==3:
         resultado=numero1/numero2
         print(resultado)
      elif operador==4:
         resultado=numero1-numero2
         print(resultado)
      else:
        print('Insira um número de operador válido')
        Calcular()   
      
      def escolhas(resultado):
        escolher=eval(input('Escolha se deseja: \n (1) Sair \n (2) Continuar operação com resultado \n (3) Nova operação\n --> '))
        if escolher==1:
           print('Calculadora desligada! :)')
        
        elif escolher==2:
          
         def Nova_operacao(resultado=resultado):
           numero_adicional=eval(input('Digite o número que deseja operar com novo resultado: '))
           nova_operacao=eval(input('Escolha o número da operação que deseja:\n (1) Multiplicação\n (2) Soma\n (3) Divisão \n (4) Subtração\n --> '))  
           
           if nova_operacao==1:
              resultado=resultado*numero_adicional
              print(resultado)
              
              escolhas(resultado)
           elif nova_operacao==2: 
              resultado=resultado+numero_adicional
              print(resultado)
             
              escolhas(resultado)     
           elif nova_operacao==3:
              resultado=resultado/numero_adicional
              print( resultado)
             
              escolhas(resultado)
           elif nova_operacao==4:
              resultado=resultado-numero_adicional
              print( resultado)
             
              escolhas(resultado)
           else:
             print('Insira um número de operador válido')
             Nova_operacao()
         
         Nova_operacao() 
        
        elif escolher==3:
           Calcular()
      
      escolhas(resultado)
  
  Calcular()                 

Calculadora()
    
    
        
        