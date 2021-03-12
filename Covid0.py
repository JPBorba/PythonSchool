#Dados do Paciente
Nome = "Jão"
Idade = 80
Sexo = "Masc"
Comorbidades = False
Vacinado = False
Sintomas = False
Contato = True

#Classificação de Atendimento (Branco, Amarelo, Laranja ou Vermlho)

if Comorbidades == False and Vacinado == False and Sintomas == False and Contato == False and Idade <= 60:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == False and Contato == True and Idade <= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == False and Idade <= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == True and Idade <= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == False and Idade <= 60:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == True and Idade <= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == False and Idade <= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == True and Idade <= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == False and Idade <= 60:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == True and Idade <= 60:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")
    
elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == False and Idade <= 60:
    print("Situação Laranja / Vermelho!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == True and Idade <= 60:
    print("Situação Vermelho!!!")
    print("Encaminhar paciente para UTI!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == False and Idade <= 60:
    print("Situação Branco!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True and Idade <= 60:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == False and Idade <= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True and Idade <= 60:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == True and Idade <= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == False and Contato == False and Idade >= 60:
    print("Situação Branco!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == False and Contato == True and Idade >= 60:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == False and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == True and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == False and Idade >= 60:
    print("Situação Branco!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == True and Idade >= 60:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == False and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == True and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == False and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == True and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")
    
elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == False and Idade >= 60:
    print("Situação Vermelho!!!")
    print("Encaminhar paciente para UTI!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == True and Idade >= 60:
    print("Situação Vermelho!!!")
    print("Encaminhar paciente para UTI!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == False and Idade >= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True and Idade >= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == False and Idade >= 60:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True and Idade >= 60:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == True and Idade >= 60:
    print("Situação Vermelho!!!")
    print("Encaminhar paciente para UTI!!")
else:
    print("Você fez merda irmão!!!")

    #Dados paciente para acompanhamneto
print("Nome: " + Nome)
print("Idade: " + str(Idade))
print("Sexo: " + Sexo) 
print("O paciente é gordo? " + str(Comorbidades))
print("O Paciente já foi Vaciando? " + str(Vacinado))
print("Algum sintoma esta sendo apresentado? " + str(Sintomas))
print("O Paciente teve contato com algume infectado nos ultimos dias? " +  str(Contato))