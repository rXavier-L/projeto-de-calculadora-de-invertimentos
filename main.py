
valorDeCompra=int(input('quantos reais vai investir mensal?'))
totalAnual00=(valorDeCompra/100)*12
porcentagemD=int(input('qual a porcentagem de pagamento do produto?: %'))
a1=porcentagemD*12
print(f'o total de ações no ano 1 é de: {(totalAnual00+a1)}')
reposicao01=(totalAnual00+a1*12)/100

#repete o resultado inclundo o valor repetido mensal

totalAnual01=totalAnual00+a1
print(f'o total de ações no ano 2 é de: {(totalAnual01+totalAnual00+reposicao01)}')
reposicao02=(totalAnual01+a1*12)/100

#desce com as variaveis em escadinha

totalAnual02=totalAnual01+totalAnual00+a1
print(f'o total de ações no ano 3 é de: {(totalAnual02+totalAnual00)}')
reposicao03=(totalAnual02+a1*12)/100

totalAnual03=totalAnual02+totalAnual00+a1
print(f'o total de ações no ano 4 é de: {(totalAnual03+totalAnual00)}')
reposicao04=(totalAnual03+a1*12)/100

totalAnual04=totalAnual03+totalAnual00+a1
print(f'o total de ações no ano 5 é de: {(totalAnual04+totalAnual00)}')
reposicao05=(totalAnual04+a1*12)/100

totalAnual05=totalAnual04+totalAnual00+a1
print(f'o total de ações no ano 6 é de: {(totalAnual05+totalAnual00)}')
reposicao06=(totalAnual04+a1*12)/100

totalAnual06=totalAnual05+totalAnual00+a1
print(f'o total de ações no ano 7 é de: {(totalAnual06+totalAnual00)}')
reposicao07=(totalAnual04+a1*12)/100

totalAnual07=totalAnual06+totalAnual00+a1
print(f'o total de ações no ano 8 é de: {(totalAnual07+totalAnual00)}')
reposicao08=(totalAnual04+a1*12)/100

totalAnual08=totalAnual07+totalAnual00+a1
print(f'o total de ações no ano 9 é de: {(totalAnual08+totalAnual00)}')
reposicao09=(totalAnual04+a1*12)/100

totalAnual09=totalAnual08+totalAnual00+a1
print(f'o total de ações no ano 10 é de: {(totalAnual09+totalAnual00)}')
reposicao10=(totalAnual04+a1*12)/100

totalAnual10=totalAnual09+totalAnual00+a1
print(f'o total de ações no ano 11 é de: {(totalAnual10+totalAnual00)}')
reposicao11=(totalAnual04+a1*12)/100

