br = ('Flamengo', 'Atlético', 'São Paulo', 'Internacionais', 'Grêmio', 'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo', 'Corinthias', 'Vasco da Gama', 'Fluminense', 'América-MG', 'Chapecoense', 'Santos', 'EC Vitória', 'Bhaia', 'Paraná', 'Atlético-PR', 'Ceará SC')
print("A) Top 5:")
for i in range(0, 5):
    print(br[i])
print("B) Últimos 4:")
print(br[16:])
print("C) Em ordem alfabética:")
print(sorted(br))
print("D) Em que posição esta chapecoense:")
for posi, c in enumerate(br):
    if c == 'Chapecoense':
        print(posi)
