'''
Exemplo: Faça um programa em Python para armazenar em uma lista dez notas dos alunos de uma turma e em seguida informe a média da turma e as notas superiores à média calculada.
'''

l = list(range(10))
soma = 0
for i in range(10):
    l[i] = float(input('\nDigite a nota do aluno %d: ' %(i + 1)))
    soma += l[i]
media = soma / 10
print('\nA média da turma é %0.2f.\n\n' %media)
for i in range(10):
    if l[i] > media:
        print('Nota %0.2f do aluno %d é maior que a média da turma.' %(l[i],i+1))