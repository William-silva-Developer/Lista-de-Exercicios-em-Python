almocoFavorito = "Feijão com arroz e frango assado.";
precoAlmocoPorPessoa = 20;
quantidadePessoa = 4;
orcamento = 60;
amigoComDinheiro = True;

total = precoAlmocoPorPessoa * quantidadePessoa;
if(orcamento >= total): 
    print("Posso pagar a conta.");
    print("--------Detalhamento dos gastos--------");
    print("Preço por pessoa: R$ ",precoAlmocoPorPessoa);
    print("Quantidade de pessoa: R$ ",quantidadePessoa);
    print("Valor a pagar: R$ ",total);
    print("Valor recebido: R$ ",orcamento);
    print("Troco: R$ ",orcamento - total);
    print("---------------------------------")
elif(amigoComDinheiro):
    print("Pedir ajuda ao amigo.");
else:
    print("Não posso pagar a conta.");
    

