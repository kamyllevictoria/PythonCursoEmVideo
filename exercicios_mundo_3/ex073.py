contador = 1
Chapecoense= 0
colocados = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Chapecoense','Fortaleza','São Paulo','América',
'Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Avaí','Juventude')
print(f'Os primeiros cinco colocados foram {colocados[:5]}')
print(f'Os últimos quatro colocados foram {colocados[-4]}')
print(f'Os times em ordem alfabética são dados por: {sorted(colocados)}')
print(f'A posição do time Chapecoense é na {colocados.index("Chapecoense")} posição')