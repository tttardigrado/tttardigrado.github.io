---
title: "PI - Ficha2"
date: 2023-03-01T15:08:53Z
tags: ["lcc", "imperativa"]
summary: "My solutions for the imperative programming course's worksheet #2"

---

## 2.3

Escreva um programa **maior.c** que lê três valores inteiros da entrada padrão e
imprime o maior destes valores.

```c
#include <stdio.h>

int max(int a, int b) {
	return (a >= b) ? a : b;
}

int max3(int a, int b, int c) {
	return max(a, max(b, c));
}

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	printf("%d\n", max3(a, b, c));

	return 0;
}
```

## 2.4

Escreva um programa que lê uma quantia inteira de euros e mostra como pagar essa quantia em notas de 20, 10, 5 e notas de 1

```c
#include <stdio.h>

int main() {
	// ler valor
	int val;
	printf("Quantia em EUR? "); scanf("%d", &val);

	// notas 20, 10, 5
	for (int i = 20; i >= 5; i /= 2) {
		printf("notas EUR %d: %d", i, val/i);
		val %= i;
	}

	// moedas 1
	printf("moedas EUR 1: %d", val);

	return 0;
}
```

## 2.5

Escreva uma função que calcula a mediana de 3 inteiros, isto é, o valor do meio quando os colocamos por ordem crescente.

```c
int mediana(int a, int b, int c) {
	if ((b <= a && a <= c) || (c <= a && a <= b)) return a;
	if ((a <= b && b <= c) || (c <= b && b <= a)) return b;
	return c;
}
```

## 2.7

A lingugem C não tem um operador para potências, mas podemos calcular por multiplicações sucessivas (para expoentes naturais). Implemente essa função.

```
int potencia(int x, int n) {
	int res = 1; // inicialize a resul variable

	for (int i = 0; i < n; i++)
		res *= x; // multiply it n times by x

	return res;
}
```

## 2.8

Escreve um programa que lê uma sequência de inteiros terminada pelo valor 0, e imprime a sua média aritmética.

```c
#include <stdio.h>
int main() {
	int val = 0; // store the last value read
	int sum = 0; // store the current sum of values
	int num = 0; // store the number of values

	do {
		scanf("%d", &val); // read new value
		sum += val;       // update sum
		num++;           // increment counter
	} while (val != 0); // until 0 is read
	num--;             // zero was read but should not increment the coun

	printf("%f\n", (float)sum / num); // print the result
	return 0;
}
```

## 2.9

Escreve um programa que lê um inteiro maior que 1 e imprime a lista de fatores primos

```c
#include <stdio.h>

int main() {
	int val; // read value
	printf("Número: "); scanf("%d", &val);

	printf("%d:", val);

	int n = 2;
	while (val != 1) {
		while (val % n == 0) {
			val /= n;
			printf(" %d", n);
		}
		n++;
	}

	printf("\n");

	return 0;
}
```
## 2.10

Um ano é bissexto se for divisível por 4, exceto se for também divisível por 100 e não por 400.
Defina uma função que verifica esta condição.

```
int bissexto(int n) {
	if (n % 4 != 0) return 0;
	if (n % 100 == 0 && n % 400 != 0) return 0;
	return 1;
}
```

## 2.11
Escreva uma função que calcula o próximo ano bissexto a partir de um ano dado; se o ano for bissexto deve retornar o ano dado.

```
int prox_bissexto(int n) {
	for (int i = 0;; i++)
		if (bissexto(n+i)) return n+i;
}
```