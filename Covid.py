#Dados do Paciente
Nome = "Jão"
idade = 20
Sexo = 'Masc'
Comorbidades = False
Vacinado = True
Sintomas = False
Contato = True

#Classificação de Atendimento (Branco, Amarelo, Laranja ou Vermlho)

if idade >= 60:
    print("Este paciente tem prioridade!!!")
    print("Encaminhe-o para área de atendimento preferencial!!!")
elif int(idade) <= 59:
    print("Este paciente não tem prioridade!!!")
    print("Encaminhe-o para área de atendimento comum!!!")

if Comorbidades == False and Vacinado == False and Sintomas == False and Contato == False:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == False and Contato == True:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == False:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com medicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == False and Sintomas == True and Contato == True:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == False:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == False and Contato == True:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com emdicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == False:
    print("Situação Amarela!!!")
    print("Emcaminhe o paciente para casa com emdicação e atestado para 14 dias!!!")

elif Comorbidades == False and Vacinado == True and Sintomas == True and Contato == True:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == False:
    print("Situação Branca!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == False and Contato == True:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com emdicação e atestado para 14 dias!!!")
    
elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == False:
    print("Situação Laranja / Vermelho!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif  Comorbidades == True and Vacinado == False and Sintomas == True and Contato == True:
    print("Situação Vermelho!!!")
    print("Encaminhar paciente para UTI!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == False:
    print("Situação Branco!!!")
    print("Encaminhe o paciente para casa sem maiores problemas!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com emdicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == False:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == False and Contato == True:
    print("Situação Amarelo!!!")
    print("Emcaminhe o paciente para casa com emdicação e atestado para 14 dias!!!")

elif Comorbidades == True and Vacinado == True and Sintomas == True and Contato == True:
    print("Situação Laranja!!!")
    print("Emcaminhe o paciente para o ambulatório para ser medicado!!!")
else:
    print("Você fez merda irmão!!!")