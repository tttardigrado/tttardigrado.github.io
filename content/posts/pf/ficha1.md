---
title: "PF - Ficha 1"
date: 2023-01-17T14:29:01Z
tags: ["lcc", "funcional"]
summary: "My solutions for the functional programming course's worksheet #1"
---

## 1.1
Considere as seguintes definições de funções:

`incr x = x + 1`

`triplo x = 3 * x`

`boasVindas nome = "Olá, " ++ nome ++ "!"`

Simplifique as expressões seguintes o máximo possível efectuando reduções passo-a-passo

```haskell
incr (triplo 3)
  => incr (3 * 3)
  => incr 9
  => 9 + 1
  => 10

triplo (incr 3)
  => triplo (3 + 1) 
  => triplo 4
  => 3 * 4
  => 12

boasVindas "Linguagem" ++ " Haskell"
  => "Olá, " ++ "Linguagem" ++ "!" ++ " Haskell"
  => "Olá, Linguagem" ++ "!" ++ " Haskell"
  => "Olá, Linguagem!" ++ " Haskell"
  => "Olá, Linguagem! Haskell"

boasVindas ("Linguagem" ++ " Haskell")
  => boasVindas "Linguagem Haskell"
  => "Olá, " ++ "Linguagem Haskell" ++ "!"
  => "Olá, Linguagem Haskell" ++ "!"
  => "Olá, Linguagem Haskell!"

boasVindas (boasVindas "Haskell")
  => boasVindas ("Olá, " ++ "Haskell" ++ "!")
  => boasVindas ("Olá, Haskell" ++ "!")
  => boasVindas "Olá, Haskell!"
  => "Olá, " ++ "Olá, Haskell!" ++ "!"
  => "Olá, Olá, Haskell!" ++ "!"
  => "Olá, Olá, Haskell!!"
```

## 1.2

Para que três valores possam ser medidas dos lados de um triângulo deve
verifcar-se a seguinte condição: qualquer dos valores deve ser inferior à soma
dos outros dois. Complete a defnição de uma função que testa esta condição. O
resultado deve ser um valor boleano (`True` ou `False`).

```haskell
testaTriangulo :: Float -> Float -> Float -> Bool
testaTriangulo a b c = a < b + c && b < a + c && c < a + b
```

## 1.3

Podemos calcular a área A de um triângulo de lados `a`, `b`, `c` usando a fórmula de Heron:
$$ A = \sqrt{s(s-a)(s-b)(s-c)}$$
$$s = (a+b+c)/2$$
Complete a seguinte defnição em Haskell duma função
para calcular esta área.

```haskell
areaTriangulo :: Float -> Float -> Float -> Float
areaTriangulo a b c = srt $ s * (s - a) * (s - b) * (s - c)
  where s = (a + b + c) / 2
```

## 1.4

Usando as funções `length`, `take`, `drop` apresentadas na primeira aula,
escreva uma função metades que divide uma lista em duas com metade do
comprimento (aproximadamente).

```haskell
metades :: [a] -> ([a], [a])
metades xs = (take half xs, drop half xs)
  where half = length xs `div` 2
```

## 1.5

Neste exercício pretende-se que use as funções do prelúdio-padrão de pro-
cessamento de lista apresentadas na primeira aula: `head`, `tail`, `length`, `take`,
`drop` e `reverse`

### 1.5.1
Encontre duas definições para a função `last` que obtém o último elemento da lista
```haskell
last', last'' :: [a] -> a
last'     = head . reverse
last'' xs = head $ drop (length xs - 1) xs
```

### 1.5.2
Encontre duas definições para a função `init` que remove o último elemento da lista
```haskell
init', init'' :: [a] -> [a]
init'     = reverse . tail . reverse
init'' xs = take (length xs - 1) xs
```

## 1.6
Os coefcientes binomiais correspondem ao número de formas distintas de escolher `k` objetos entre `n` (ou, equivalentemente, o número de subconjuntos com `k` elementos que podemos formar de um conjunto de `n` elementos).

Complete a defnição duma função que calcule o coeficient binomial, sabendo que
$$\binom n k = \frac{n!}{k!(n-k)!}$$

```haskell
binom :: Integer -> Integer -> Integer
binom n k = fact n `div` (fact k * fact (n-k))
  where fact a = product [1..a]
```