# Python - Exercícios


## Exercícios

Responda as perguntas ou complete as tarefas descritas em negrito abaixo, use o método específico, se aplicável.

** Quanto é 7 elevado na potência 4?**


```python
7**4
```




    2401




```python

```




    2401



** Quebre a seguinte string em uma lista:**

    s = "Olá, Pai!"


```python
s = "Olá, Pai!"
```


```python
s.split()
```




    ['Olá,', 'Pai!']




```python

```




    ['Olá,', 'Pai!']



** Dada as variáveis:**

    Planeta = "Terra"
    Diametro = 12742

** Use .format() para printar a seguinte frase: **

    O diâmetro da terra é de 12742 kilômetros.


```python
planeta = "Terra"
diametro = 12742
```


```python
frase = "O diametro da {0} é de {1} kilometros"
frase.format(planeta, diametro)
```




    'O diametro da Terra é de 12742 kilometros'




```python

```

** Dada a lista abaixo, use indexação para obter apenas a string "ola". **


```python
lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]
```


```python
lst[32:35]
```




    'olá'




```python
lst
```




    "[1, 2, [3, 4], [5, [100, 200, ['olá']], 23, 11], 1, 7]"



** Dado o seguinte dicionário aninhado, extraia a palavra "hello" **


```python
d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}
```


```python
d['k1']
```




    [1, 2, 3, {'café': ['banana', 'mulher', 'colher', {'alvo': [1, 2, 3, 'olá']}]}]




```python
d['k1'][3]
```




    {'café': ['banana', 'mulher', 'colher', {'alvo': [1, 2, 3, 'olá']}]}




```python
d['k1'][3]['café'][3]['alvo'][3]
```




    'olá'



** Qual a principal diferença entre um dicionário e uma tupla? **


```python
A tupla é imutavel!!
```

** Construa uma função que retire o domínio dado um e-mail no seguinte formato: **

    user@domain.com
    
**Por exemplo, passando como parâmetro "user@domain.com" retornaria: domain.com**


```python
def obterDominio(nome):
    x = nome.lstrip("user@")
    return x
```


```python
obterDominio('user@domain.com')
```




    'domain.com'




```python
obterDominio('user@domain.com')
```




    'domain.com'



** Crie uma função básica que retorna True se a palavra 'dog' estiver contida na string de entrada. Não se preocupe com os casos de extremos, como uma pontuação que está sendo anexada à palavra cão, mas que seja senível à caixa. **


```python
def encontreCachorro(frase):
      return 'cachorro' in frase.lower().split()
```


```python
encontreCachorro('Existe um a aí?')
```




    False




```python
encontreCachorro('Existe um cachorro aí?')
```




    True



** Crie uma função que conta o número de vezes que a palavra "dog" ocorre em uma string. Novamente ignore os casos extremos. **


```python

def contaCachorro(frase):
    a=0
    x = frase.split(" ")
    print(x)
    for item in x:
        if item == "cachorro" or item == "cachorro.":
            a = a + 1
    return a
```


```python
contaCachorro('Esse cachorro é mais rápido que o outro cachorro.')
```

    ['Esse', 'cachorro', 'é', 'mais', 'rápido', 'que', 'o', 'outro', 'cachorro.']
    




    2



** Use expressões lambda e a função filter () para filtrar as palavras de uma lista que não começa com a letra 's'. Por exemplo: **

    seq = ['sopa','cachorro','salada','gato','ótimo']

** Deveria ser filtrado para:**

    ['sopa','salada']


```python
seq = ['sopa','cachorro','salada','gato','ótimo']
```


```python
list(filter(lambda item: item[0] =='s' , seq))
```




    ['sopa', 'salada']




```python
seq.
```




    ['sopa', 'salada']



### Problema final
** Você está dirigindo um pouco rápido demais, e um policial para você. Escreva uma função para retornar um dos 3 resultados possíveis: "Sem multa", "Pequena multa" ou "Multa Grande".
   Se a sua velocidade for igual ou inferior a 60, o resultado é "Sem multa". Se a velocidade for entre 61 e 80 inclusive, o resultado é "Multa Pequena". Se a velocidade é de 81 ou mais, o resultado é "Multa Grande". A menos que seja seu aniversário (codificado como um valor booleano nos parâmetros da função) - em seu aniversário, sua velocidade pode ser 5 maior em todos os casos. **


```python
def capturar_velocidade(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
    else:
        speed = speed
            
    if speed > 80:
        return "Multa Grande"
    elif speed > 60:
        return "Multa Pequena"
    else:
        return "Sem Multa"
            
```


```python
capturar_velocidade(65,True)
```




    'Sem Multa'




```python

```




```python
capturar_velocidade(65,False)
```




    'Multa Pequena'




```python
capturar_velocidade(81,False)
```




    'Multa Grande'




```python

```
