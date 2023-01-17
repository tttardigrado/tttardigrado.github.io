---
title: "PF - Ficha 2"
date: 2023-01-17T15:40:58Z
tags: ["lcc", "funcional"]
summary: "My solutions for the functional programming course's worksheet #2"
---

## 2.1

Escreva duas defnições, respectivamente usando expressões condicionais e
guardas, da função `classifica :: Int -> String` que faz corresponder uma
classificação qualitativa a uma nota de 0 a 20:

* ≤ 9 "reprovado"
* 10-12 "suficiente"
* 13-15 "bom"
* 16-18 "muito bom"
* 19-20 "muito bom com distinção"

```haskell
classifica :: Int -> String
classifica n = 
  if n <= 9 then "reprovado"
  else if n <= 12 then "suficiente"
  else if n <= 15 then "bom"
  else if n <= 18 then "muito bom"
  else "muito bom com distinção"
```

```haskell
classifica :: Int -> String
classifica n
  | n <= 9    = "reprovado"
  | n <= 12   = "suficiente"
  | n <= 15   = "bom"
  | n <= 18   = "muito bom"
  | otherwise = "muito bom com distinção"
```

## 2.2
O índice de massa corporal (IMC) é uma medida simples para classificar o peso de adultos. O IMC de um indivíduo é calculado como o valor do peso (em quilogramas) a dividir pelo quadrado da altura (em metros):
$$ IMC = peso/altura^2 $$
Classificamos o resultado nos seguinte intervalos:

* IMC  < 18.5     "baixo peso"
* 18.5 ≤ IMC < 25 "peso normal"
* 25   ≤ IMC < 30 "excesso de peso"
* 30   ≤ IMC      "obesidade"

Escreva uma definição da função `classifica :: Float -> Float -> String` que determina a classificação acima; os dois argumentos da função são, respectivamente, o peso em quilogramas e a altura em metros.

```haskell
imc :: Float -> Float -> Float
imc peso alt = peso / (alt * alt)

classifica' :: Float -> String
classifica' n
  | n < 18.5  = "baixo peso"
  | n < 25    = "peso normal"
  | n < 30    = "excesso de peso"
  | otherwise = "obesidade"

classifica :: Float -> Float -> String
classifica x y = classifica' $ imc x y
```

## 2.3
Considere duas possíveis definições das funções max e min do prelúdio-padrão que calculam, respectivamente, o máximo e o mínimo de dois valores:

`max x y = if x>=y then x else y`

`min x y = if x<=y then x else y`

### 2.3.1
Escreva defnições deste género para duas funções `max3` e `min3` para calcular, respectivamente, o máximo e o mínimo de três números.
```haskell
max3 :: Ord a => a -> a -> a -> a
max3 x y z = if x >= y 
    then if x >= z then x else z
    else if y >= z then y else z

min3 :: Ord a => a -> a -> a -> a
min3 x y z = if x <= y 
    then if x <= z then x else z
    else if y <= z then y else z
```

### 2.3.2
Observe que as operação de máximo e mínimo são associativas. Por exemplo, para calcular o máximo de três valores podemos determinar o máximo entre dois deles e depois o máximo do resultado com o terceiro. Re-escreva as funções `max3` e `min3` usando esta ideia e as funções de `max` e `min` do prelúdio-padrão.

```haskell
max3 :: Ord a => a -> a -> a -> a
max3 x y z = max x $ max y z

min3 :: Ord a => a -> a -> a -> a
min3 x y z = min x $ min y z
```
## 2.4
Escreva uma defnição da função lógica ou-exclusivo `xor :: Bool -> Bool -> Bool` usando múltiplas equações com padrões.

```haskell
xor :: Bool -> Bool -> Bool
xor True  False = True
xor False True  = True
xor _     _     = False
```
## 2.5
Pretende-se implementar uma função `safetail :: [a] -> [a]` que extende a função tail do prelúdio de forma a dar a lista vazia quando o argumento é a lista vazia (em vez de um erro). Escreva três defnições diferentes usando condicionais, equações com guardas e padrões.

```haskell
safetail :: [a] -> [a]
safetail xs = if length xs == 0
              then []
              else tail xs
```

```haskell
safetail :: [a] -> [a]
safetail xs
  | length xs == 0 = []
  | otherwise      = tail xs
```


```haskell
safetail :: [a] -> [a]
safetail [] = []
safetail xs = tail xs
```

## 2.6

Escreva duas defnições da função `curta :: [a] -> Bool` para testar se uma lista tem zero, um ou dois elementos, usando a função `length` e padrões.

```haskell
curta :: [a] -> Bool
curta xs = length xs <= 2
```

```haskell
curta :: [a] -> Bool
curta []     = True
curta [_]    = True
curta [_, _] = True
curta _      = False
```

## 2.7

A mediana de três valores é o valor "no meio" quando os colocamos por
ordem crescente. Por exemplo: mediana 2 3 (-1) == 2

### 2.7.1
Escreva uma definição da função mediana para determinar a mediana de
3 valores quaisquer com comparações de ordem. Qual será o seu tipo mais geral?

```haskell
mediana :: Ord a => a -> a -> a -> a
mediana x y z =
  | xor (x > y) (x > z) = x
  | xor (y < x) (y < z) = y
  | otherwise           = z
```

### 2.7.2
Em vez de definir a mediana diretamente usando comparações, pode usar o seguinte método: somamos os 3 valores e subtraimos o maior e o menor. Re-defina a função mediana desta forma.

```haskell
mediana :: Ord a => a -> a -> a -> a
mediana x y z = x + y + z - (max3 x y z) - (min x y z)
```

## 2.8
Defina uma função `converte :: Int -> String` para converter um inteiro positivo inferior a 1000 para texto em português.

```haskell
sub20 :: Int -> String
sub20 n
  | n == 0  = "zero"
  | n == 1  = "um"
  | n == 2  = "dois"
  | n == 3  = "três"
  | n == 4  = "quatro"
  | n == 5  = "cinco"
  | n == 6  = "seis"
  | n == 7  = "sete"
  | n == 8  = "oito"
  | n == 9  = "nove"
  | n == 10 = "dez"
  | n == 11 = "onze"
  | n == 12 = "doze"
  | n == 13 = "treze"
  | n == 14 = "catorze"
  | n == 15 = "quinze"
  | n == 16 = "dezasseis"
  | n == 17 = "dezassete"
  | n == 18 = "dezoito"
  | n == 19 = "dezanove"

sub100 :: Int -> String
sub100 n
  | n < 20  = sub20 n
  | n == 20 = "vinte"
  | n < 30  = "vinte e "     ++ sub20 (n `mod` 10)
  | n == 30 = "trinta"
  | n < 40  = "trinta e "    ++ sub20 (n `mod` 10)
  | n == 40 = "quarenta"
  | n < 50  = "quarenta e "  ++ sub20 (n `mod` 10)
  | n == 50 = "cinquenta"
  | n < 60  = "cinquenta e " ++ sub20 (n `mod` 10)
  | n == 60 = "sessenta"
  | n < 70  = "sessenta e "  ++ sub20 (n `mod` 10)
  | n == 70 = "setenta"
  | n < 80  = "setenta e "   ++ sub20 (n `mod` 10)
  | n == 80 = "oitenta"
  | n < 90  = "oitenta e "   ++ sub20 (n `mod` 10)
  | n == 90 = "noventa"
  | n < 100 = "noventa e "   ++ sub20 (n `mod` 10)

converte :: Int -> String
converte n
  | n < 100   = sub100 n
  | n == 100  = "cem"
  | n < 200   = "cento e " ++ sub100 (n `mod` 100)
  | n == 200  = "duzentos"
  | n < 300   = "duzentos e " ++ sub100 (n `mod` 100)
  | n == 300  = "trezentos"
  | n < 400   = "trezentos e " ++ sub100 (n `mod` 100)
  | n == 400  = "quatrocentos"
  | n < 500   = "quatrocentos e " ++ sub100 (n `mod` 100)
  | n == 500  = "quinhentos"
  | n < 600   = "quinhentos e " ++ sub100 (n `mod` 100)
  | n == 600  = "seiscentos"
  | n < 700   = "seiscentos e " ++ sub100 (n `mod` 100)
  | n == 700  = "setecentos"
  | n < 800   = "setecentos e " ++ sub100 (n `mod` 100)
  | n == 800  = "oitocentos"
  | n < 900   = "oitocentos e " ++ sub100 (n `mod` 100)
  | n == 900  = "novecentos"
  | n < 1000  = "novecentos e " ++ sub100 (n `mod` 100)
  | otherwise = "mil"
```