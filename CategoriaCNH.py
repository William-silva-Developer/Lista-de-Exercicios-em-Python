quantRodas = 5;
pesoBruto = 4.200;
quantPessoa = 2;

pesoBruto_1 = 3.500;
pesoBruto_2 = 6.000;

if(quantRodas <= 3): 
    print("Habilitação apropriada A");
elif ((quantRodas == 4) and (quantPessoa <= 8) and (pesoBruto <= pesoBruto_1)):
    print("Habilitação apropriada B");
elif ((quantRodas >= 4) and (pesoBruto >= pesoBruto_1) and (pesoBruto <= pesoBruto_2)):
    print("Habilitação apropriada C");
elif ((quantRodas >= 4) and (quantPessoa > 8)):
    print("Habilitação apropriada D");
elif ((quantRodas >= 4) or (pesoBruto > pesoBruto_2)):
    print("Habilitação apropriada E");
else :
    print("Dados incorretos.");
    