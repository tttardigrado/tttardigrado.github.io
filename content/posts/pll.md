---
title: A formal esolang
date: 2024-11-23
draft: false
file: "pll"
---

It's almost impossible to discuss esoteric programming languages without someone bringing up [brainfuck](https://esolangs.org/wiki/Brainfuck). The thing that most people don't know is that brainfuck has a formal cousin called P''. 

Invented in 1964 by Corrado Böhm¹ to describe a family of Turing Machines, P'' is, in some way, the "imperative analog" to [λ-calculus](https://plato.stanford.edu/archives/sum2022/entries/lambda-calculus/): a simple and Turing complete language that beautifully captures the essence of its paradigm. I'll illustrate that beauty by building an interpreter for P'' using just a few lines of Haskell. The complete source code is available on [here](https://gist.github.com/tttardigrado/4f6a2d5a4cdf1ca4287d8a8195d16d23)

Before discussing the language, we should describe the objects it acts upon: tapes. A (doubly infinite) tape is a sequence of cells that extends infinitely in both directions, paired with a pointer to the current cell -- known as the head. Formally, we would define it as a pair `(s, i)` such that `s : ℤ → ℤ` and `i ∈ ℤ` but, by leveraging Haskell's lazy evaluation, we can be a bit more clever and represent it by a triple that divides the tape into its left half, its right half and the current cell: 

```
data Tape = Tape [Int] Int [Int]

empty :: Tape
empty = Tape (repeat 0) 0 (repeat 0)
```

Since a data type without some way to interact with it is of little to no use, we will implement ways to move the tape's head and to read and write to the current cell²: 

```
left :: Tape -> Tape
left (Tape (l:ls) v rs) = Tape ls l (v:rs)

right :: Tape -> Tape
right (Tape ls v (r:rs)) = Tape (v:ls) r rs

peek :: Tape -> Tape
peek (Tape _ v _) = v

edit :: (Int -> Int) -> Tape -> Tape
edit f (Tape ls v rs) = Tape ls (f v) rs
```

With the memory model out of the way, let's return to P''. A program is inductively defined by the following grammar:

```
p  ::=  R  |  λ  |  p p  |  (p)
```

which we can easily translate into Haskell:

```
data P = R | L | Seq p p | Loop p
  deriving (Show, Eq)
```

For those familiar with brainfuck, the semantics of P'' shouldn't come off as a surprise:
* **R** moves the head to the right (equivalent to **>**)
* **λ** increments the current value and moves the tape to the left (equivalent to **+<**)
* **p p** is the composition of programs
* **(p)** loops the program `p` until the current value is 0 (equivalent to **[p]**)

In complexity and computability theory, where P'' first originated, we work with finite alphabets of symbols. Because of this, the increment operation increments the value modulo of a given integer, usually 256.

We can translate this informal exposition of the semantics of P'' into a simple function that interprets a program `p` over a tape `t` modulo some integer `n`:

```
run :: Int -> P -> Tape -> Tape
run n R t = right t
run n L t = left $ edit ((`mod`n) . (+1)) t
run n (Seq p q) t = run n q $ run n p t
run n (Loop  p) t = if peek t == 0
  then t
  else run n (Seq p $ Loop p) t
```

Since most times we want to run a program over an empty tape modulo 256 and retrieve the value we get at the end, we define a function that does exactly that:

```
eval :: P -> Int
eval p = peek $ run 256 p empty
```

And that's it! Obviously, we could try to be a bit more clever and use Monads and Lenses to simplify the interpreter, but that's something to worry about in a future blog post. 


## Notes

1. Böhm, C. (1964). On a family of Turing machines and the related programming language.
2. Since we are only dealing with infinite lists, we do not need to consider the scenarios where the left or right tapes are empty.

