s1 = (float(input('Digite o primeiro segmento: ')))
s2 = (float(input('Digite o segundo segmento: ')))
s3 = (float(input('Digite o terceiro segmento: ')))

if ((s1 < s2 + s3) and ((s2 < s1 + s3)) and ((s3 < s1 + s3))):
    print('Os segmento formam um triângulo!')
else:
    print('Os segmento não formam um triângulo!')