nome = str(input('Digite seu nome completo: ')).strip().upper()
separa = nome.split()
if 'GABRIEL' in separa[0]:
    print('Então você é o ser superior do universo!!!')
elif 'EMANUEL' in separa[0]:
    print('Então você é formidavel por conta da grandiosidade do seu irmão!')
elif 'ALEX' in separa[0]:
    print('Então você tem orelha mastigável!')
elif 'MIGUEL' in separa[0]:
    print('Então você é um popotuzinho!')
elif 'CILENE' in separa[0]:
    print('Então você tem barriga de poing!')
else:
    print('Então você é uma pessoa comum.')
