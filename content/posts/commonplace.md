---
title: "On how I take notes"
date: 2025-12-15
file: "commonplace"
tags: ["info"]
lang: "en"
---

This is more of a personal note than a blog post *per se*,
but I'll still post it anyways.

Those who know me know that I'm somewhat addicted to notebooks, 
stationary and personal knowledge management systems (PKMs).
I've had my [physical zettelkasten](https://zettelkasten.de/introduction/),
my [digital zettelkasten](https://obsidian.md/download),
my completely unorganized [zibaldone](https://en.wikipedia.org/wiki/Zibaldone),
and basically everything in between.

TLDR: I've tried a lot of things and I think I'm finally more or less
satisfied with my current setup.

My current setup is composed of 4 elements:
1. An A6 notebook that I use as a calendar
2. An A6 notebook that I use as a catch all
3. An A5 commonplace book
4. A text file listing page numbers and entries on my commonplace book

I think the calendar is pretty self explanatory so I will skip it.

The catch all is also pretty simple: I have an idea, task, ...
I write it down. No filter. No [blank page syndrome](https://www.ool.co.uk/blog/blank-page-syndrome-and-how-to-beat-it/).
No worrying about making a mess out of the notebook.
Nothing.
It is a mess. It will be a mess. And that's fine.

The commonplace is probably the most interesting part of the setup.
It gives me the flexibility of a zettelkasten without the hassle of
having to carry a stack of cards.

First on the standard things. All pages are numbered and labelled
using some kind of heading
(e.g. Automata Theory, Fermi Paradox, ...).
The granularity of the labels is pretty inconsistent, but, as a 
general rule of thumb, I add a new label if I could see myself 
studying just that thing (e.g. I have an entry on Thomas Kuhn,
but not one on Incomensurability).
Additionally, I use a [Locke-style index](https://fs.blog/john-locke-common-place-book/)
(which, by the way, is very computer-sciency and I still want to write a
blog post about it).

Now we turn to the fun part: the not-so-standard things
(at least, as far as I know).

Firstly, I frequently back reference things written on other pages
using the `[NN/PP]` notation, where `NN` refers to the notebook and
`PP` to the page where the information is. In the (usual) case where
the information is contained in the same book I simply write `[PP]`.

Furthermore, I keep a list of references in the back of the book in a
weird citation format (that's what works for me... sorry).
Each entry looks something like this:

> [NNYY] Authors. (Year). Title. [Format]

The `[NNYY]` notation is used for in text citations.

The third thing that I want to note is that all pages have a *back* and
a *forward* link in the bottom left and right corners respectivelly. The
link is composed of an arrow and a number that indicates the last/next
page where the same label is covered.
I find that this reduces a lot the number of times I need to use the index,
and, in general, just makes my life easier.

Finally, I use a (somewhat) weird key system inspired by the
[bullet journal](https://bulletjournal.com/) method. Here is a table
with the ones I use the most and their meaning:

| Key  | Meaning                       |
|------|-------------------------------|
| `:=` | Definition/Concept            |
| `⊢`  | Theorem                       |
| `@`  | Algorithm                     |
| `:`  | Example                       |
| `>`  | Argument (in favor)           |
| `<`  | Argument (against)            |
| `"`  | Quote                         |
| `ψ`  | Recipe (it looks like a fork) |

So, the entry for the definition of a DFA would look somethink like

> ⊢ DFA [HU79]: a deterministic finite automaton is a 5-tuple
> ⟨Q, Σ, δ, q₀, F⟩, where:
> * Q is a finite set of states
> * Σ is an alphabet
> * δ : Q × Σ → Q is a transition function
> * q₀ ∈ Q is the initial state
> * F ⫅ Q is the set of final states

The common place book is already interesting on its own, but retrieving
information is, at times, still very cumbersome. I think that this is
where digital methods shine: it's simply easier to `Ctrl+F` something
than to look it up in an index and flip through hundreds of notebooks
and pages. This is why I have a digital index. It is pretty much bare bones:
Just a text file where I have a "name" for every entry in the commonplace
book using the `[NN/PP]` notation. It is not pretty, but `Ctrl+F` works like
a charm.

This method is not set in stone and I'll probably change it someday,
but I hope that this note is usefull to someone that, as me, has
struggled on how to properly organize knowledge and information. 
