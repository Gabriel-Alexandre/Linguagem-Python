s1 = int(input('Primeiro segmeto: '))
s2 = int(input('Segundo segmeto: '))
s3 = int(input('Terceiro segmeto: '))

if s1 < s2 +s3 and s2 < s1 + s3 and s3 < s2 + s3:
    print('Os segmentos podem formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos não podem formar um triângulo!')

