
valorDeCompra=int(input('quantos reais vai investir mensal?'))
totalAnual00=(valorDeCompra/100)*12
porcentagemD=int(input('qual a porcentagem de pagamento do produto?: %'))
a1=porcentagemD*12
print(f'o total de ações ano 1 é de: {(totalAnual00+a1)}')

totalAnual01=totalAnual00+a1
print(f'o total de ações ano 2 é de: {(totalAnual01+totalAnual00)}')

totalAnual02=(totalAnual01+a1/100)*12
a1=porcentagemD*12
#print(f'o total de ações ano 3 é de: {(totalAnual02+a1)}')+

totalAnual03=(totalAnual02+a1/100)*12
a1=porcentagemD*12
#print(f'o total de ações ano 4 é de: {(totalAnual03+a1)}')

totalAnual04=(totalAnual03+a1/100)*12
a1=porcentagemD*12
#print(f'o total de ações ano 5 é de: {(totalAnual04+a1)}')

#totalAnual01=valorDeCompra*0,24
#totalAnual02=valorDeCompra*0,36

#valorDeLucro=(totalAnual00)+valorDeCompra