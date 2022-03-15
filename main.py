
valorDeCompra=int(input('quantos reais vai investir mensal? '))
totalAnual00=(valorDeCompra/100)*12
porcentagemD=float(input('qual a porcentagem de pagamento do produto?:''%'))
a1=porcentagemD*12
print(f'o total de ações no ano 1 é de: {(totalAnual00+a1)} ao més')
print(f'com o gasto de: {totalAnual00*100} ao ano') #*100 para retorna ao valor dividido na linha 03
reposicao01=(totalAnual00+a1*12)/100
print(reposicao01)
#repete o resultado inclundo o valor repetido mensal

totalAnual01=totalAnual00+a1
r1=totalAnual01+totalAnual00+reposicao01
print(f'o total de ações no ano 2 é de: {r1} ao més')
print(f'com o gasto de: {(totalAnual00*100)*2+r1} ao ano')
reposicao02=(totalAnual01+a1*12)/100

#desce com as variaveis em escadinha

totalAnual02=totalAnual01+totalAnual00+a1
print(f'o total de ações no ano 3 é de: {(totalAnual02+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*3} ao ano')
reposicao03=(totalAnual02+a1*12)/100

totalAnual03=totalAnual02+totalAnual00+a1
print(f'o total de ações no ano 4 é de: {(totalAnual03+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*4} ao ano')
reposicao04=(totalAnual03+a1*12)/100

totalAnual04=totalAnual03+totalAnual00+a1
print(f'o total de ações no ano 5 é de: {(totalAnual04+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*5} ao ano')
reposicao05=(totalAnual04+a1*12)/100

totalAnual05=totalAnual04+totalAnual00+a1
print(f'o total de ações no ano 6 é de: {(totalAnual05+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*6} ao ano')
reposicao06=(totalAnual04+a1*12)/100

totalAnual06=totalAnual05+totalAnual00+a1
print(f'o total de ações no ano 7 é de: {(totalAnual06+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*7} ao ano')
reposicao07=(totalAnual04+a1*12)/100

totalAnual07=totalAnual06+totalAnual00+a1
print(f'o total de ações no ano 8 é de: {(totalAnual07+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*8} ao ano')
reposicao08=(totalAnual04+a1*12)/100

totalAnual08=totalAnual07+totalAnual00+a1
print(f'o total de ações no ano 9 é de: {(totalAnual08+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*9} ao ano')
reposicao09=(totalAnual04+a1*12)/100

totalAnual09=totalAnual08+totalAnual00+a1
print(f'o total de ações no ano 10 é de: {(totalAnual09+totalAnual00)} ao més')
print(f'com o gasto de: {(totalAnual00*100)*10} ao ano')
reposicao10=(totalAnual04+a1*12)/100

totalAnual10=totalAnual09+totalAnual00+a1
print(f'o total de ações no ano 11 é de: ${(totalAnual10+totalAnual00)} ao més')
print(f'com o gasto de: ${(totalAnual00*100)*11} ao ano')
reposicao11=(totalAnual04+a1*12)/100

