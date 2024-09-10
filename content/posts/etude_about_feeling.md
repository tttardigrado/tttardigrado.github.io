---
title: "étude about feeling"
date: 2021-12-14
file: "eaf"
---

Como qualquer pessoa, às vezes tenho insónias e dou por mim a pensar qual será a forma mais bonita de preencher um círculo. Esta foi a minha resposta a essa pergunta.

## Linhas
A primeira tentativa foi escolher dois pontos aleatórios na circunferência e unir os mesmos através de uma linha reta. Os pontos são selecionados através dos ângulos, tal que *a ∈ [0,2π]*, ou seja, o ângulo está em radianos, e as coordenadas finais serão obtidas através da utilização de coordenadas polares.

$ cat ./lines.js

```
function lines(){
  let a = random(2*PI)
  let b = random(2*PI)
  
  line(r*cos(a),r*sin(a), r*cos(b), r*sin(b))
}
```

$ feh ./lines1.png

![Lines 1](/img/lines.png)

A segunda tentativa consistiu em escolher pontos, desta vez não necessáriamente pertencentes à circunferência, e unir
os mesmo através de retas. Para escolher cada ponto, selecionei um ângulo tal que  *a ∈ [0,2π]* e um raio tal que *r₂ ∈ [0,r]*

$ cat ./lines2.js

```
function lines2(){  
  let a = random(2*PI)
  let b = random(2*PI)
  
  let r1 = random(r)
  let r2 = random(r)
  
  line(r1*cos(a), r1*sin(a), r2*cos(b), r2*sin(b))
}
```

$ feh ./lines2.png

![Lines 2](/img/lines2.png)


De seguida, apenas alterei a forma como os raios dos pontos são selecionados, utilizando uma função random diferente *rand* [1].

$ cat ./lines3.js

```
function lines3(){
  let a = random(2*PI)
  let b = random(2*PI)
  
  let r1 = rand(r)
  let r2 = rand(r)
  
  line(r1*cos(a), r1*sin(a), r2*cos(b), r2*sin(b))
}
```

$ feh ./lines3.png

![Lines 3](/img/lines3.png)


## Círculos

Para os gregos antigos, Círculos eram perfeitos, então, porque não tentar preencher um círculo com outros círculos?

A primeira versão, começa por rodar a tela num ângulo aleatório a, tal que *a ∈ [0,2π]*. De seguida, escolhe um raio rr tal que *rr ∈ [0,r]* e desenha um círculo tangente à circunferência original ou seja, com centro nas coordenadas *(r-rr, 0)* e raio *rr*, mas devemos nos lembrar que aplicamos previamente um raotação de ângulo *a*.

$ cat ./circs1.js

```
function circs(){
    push()
      rotate(random(2*PI))
      let rr = random(r)
  
      circle(r-rr,0,rr)
    pop()
}
```

$ feh ./circs1.png

![Circles 1](/img/circs.png)


A segunda versão, segue o mesmo princípio da primeira, apenas alterando a forma como escolhe o raio.

$ cat ./circs2.js

```
function circs2(){
    push()
      rotate(random(2*PI))
      let rr = rand(r)
  
      circle(r-rr,0,rr)
    pop()
}
```

$ cat ./circs2.png

![Circles 2](/img/circs2.png)


## Pontos

O terceiro método baseia-se em desenhar pontos dentro do círculo.

A primeira versão escolhe um ângulo *a* e um raio *rr*, e através de coordenadas polares desenha esse ponto.

$ cat ./dots1.js

```
function dots(n){
    let a = random(2*PI)
    let rr = random(r)
    
    point(rr*cos(a),rr*sin(a))
}
```

$ feh ./dots1.png

![Dots 1](/img/dots.png)

A segunda versão escolhe um ângulo *a*, mas a função que seleciona o raio é *rand* [1].

$ cat ./dots2.js

```
function dots2(n){
    let a = random(2*PI)
    let rr = rand(r)
    point(rr*cos(a),rr*sin(a))
}
```

$ feh ./dots2.png

![Dots 2](/img/dots3.png)

Por fim, são selecionadas *duas coordenadas, *x* e *y*, tal que *x, y ∈ [-r,r]*.
Este método tem o problema de alguns dos possíveis pontos não estarem contidos no círculo, pelo que utilizei o teorema de pitágoras, para saber se a distância entre este ponto e o centro era menor ou igual que o raio *(x² + y² ≤ r²)*. No caso do ponto não estar contido, a função seria repetida, até que o ponto selecionado estivesse contido no círculo.


$ cat ./dots3.js

```
function dots3(){
  while(true){
    let x = random(-r,r)
    let y = random(-r,r)
    
    if (x*x + y*y <= r*r){
      point(x,y)
      return
    }
  }
}
```

$ feh ./dots3.png

![Dots 3](/img/dots2.png)

$ cat ./notas.md

1:

```
function rand(m){
  return sqrt(random(m) * random(m))
}
```
