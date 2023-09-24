#10.1. Topological Presheaves and Sheaves

Let $X$ be a topological space. Denote the set of open subsets of $X$
as $**Open**(X)$. We can impose the structure of a
\hyperref[definition:thin-category]{\textcolor{Blue}{thin category}}
on this set by declaring that, for two open sets $U$ and $V$, 

\[
\hom_{**Open**(X)}(U, V) = 
\begin{cases}
\{\bullet\} & \text{if } U \subset V\\
\varnothing & \text{otherwise }
\end{cases}
\]

That is, we allow a single morphism from $U$ to $V$ if and only if 
$U \subset V$. 
Now suppose $Y$ is another topological space. Then for each open subset 
$U$ of $X$ we may construct the set 

\[
C(U) = \{ f: U \to Y \mid f \text{ is continuous } \}.    
\]

Observe that if $U \subset V \subset X$ are open sets, then 
there is function 

\[
\rho_U^V: C(V) \to C(U)
\]

where each $f: V \to Y$ is mapped to its restriction $f|_U: U \to Y$.
What follows is an important observation: If we have a chain of three open subsets $U \subset V \subset W$, 
then any continuous function $f: W \to Y$ can be restricted to $f|_V: V \to Y$, 
which can then be restricted to $f|_V|_U: U \to Y$. However, we obtain the same 
result if we instead just restrict $f$ to $U$ in the first place. That is, 
$f|_V|_U = f|_U$. In our notation, this implies that 

\[
\rho_V^W \circ \rho_U^V = \rho_U^W. 
\]

What we have on our hands is a *contravariant* functor (since the relation 
$U \subset V$ induces a function $C(V) \to C(U)$). As covariant functors 
are easier to think about, we can equivalently express this as a covariant functor:

\[
C: **Open**(X)\op \to **Set**
\]

which is an example of the concept of a *presheaf*. 


<span style="display:block" class="definition">
A **presheaf (of sets on a topological space $X$)** 
is a covariant functor $F: **Open**(X)\op \to **Set**$. 
We spell out the details: A presheaf consists of 
\begin{description}
\itemsep 0.25cm
\item[(PS1)] an assignment of open sets $U \subset X$ to sets $F(U)$
\item[(PS2)] a function $\rho_{U}^{V}: F(V) \to F(U)$ whenever $U \subset V$
such that\
\[-0.3cm]
\begin{description}
\itemsep 0.25cm
\item[(Identity)] $\rho_{U}^{U}: F(U) \to F(U)$ is the identity
\item[(Composition)] $\rho_V^W \circ \rho_U^V = \rho_U^W$ whenever $U \subset V \subset W$
\end{description}
\end{description}
\noindent A **morphism of presheaves** is a natural transformation between presheaves.
</span>

A few comments are to be made about this definition. 


*  *About* **Set**. The codomain of a presheaf doesn't have to be $**Set**$.
Usually, the value of our presheaves are sets of functions, but sometimes such sets have additional 
structure. Therefore, the codomain could be $**Ab**$, $**Ring**$, or another category 
where the objects are sets plus some mathematical structure. In these cases, we'd obtain a **presheaf of abelian groups**, a
**presheaf of rings**, and so forth.


*  *About the naming.* The only reason this is called a presheaf is because, 
as the reader may guess, this idea is a precursor to the concept of a sheaf. 


*  The fact that we can formulate morphisms between presheaves prompts us to 
define the **category of presheaves (of sets) on $\cc$** which we denote as
$**Psh**(X, **Set**)$.




We now offer some examples of presheaves. The examples we offer will be topological presheaves, 
i.e., presheaves on $**Open**(X)$ for some topological space $X$. This is because 
many interesting and useful examples of presheaves appear in this way. This is also done 
so that we can offer our first definition of sheaf with as littel confusion as possible. 


<span style="display:block" class="example">
Consider the introductory example of this section, and instead take $Y = \rr$. 
Then in this case, 
\[
C(U) = \{f: U \to \rr \mid f \text{ is continuous}\}.
\]

However, observe that $C(U)$ is actually an $\rr$-module: 
if $f, g: U \to \rr$ are continuous, then so is $f + g: U \to \rr$. Moreover, 
if $a \in \rr$, then $a\cdot f: U \to \rr$ is continuous. These operations 
satisfy the criteria for $C(U)$ to be an $\rr$-module. Therefore, when $Y = \rr$, 
we obtain a presheaf on **$\rr$-Mod**, and we may write

\[
C: **Open**(X)\op \to **$\rr$-Mod**.
\]

We will return to this example later on.
</span>


<span style="display:block" class="example">
For every open set $D$ of the complex plane $\mathbb{C}$, define the 
set 

\[
H(D) = \{f: D \to \mathbb{C} \mid f \text{ is holomorphic. }\}
\]

Observe that this induces a functor $H: **Open**(\mathbb{C})\op \to **Set**$, 
and hence we have a presheaf of sets. Moreover, this is actually a $\mathbb{C}$-module, so 
that what we have is actually a presheaf of $\mathbb{C}$-modules; hence we 
write $H: **Open**(\mathbb{C})\op \to \mathbb{C}**-Mod**$.
</span>


<span style="display:block" class="example">
Let $X$ be a topological space, and consider the functor $B: **Open**(X)\op \to **$\rr$-Mod**$, 
defined as follows. For an open subset $U \subset X$, we define 

\[
B(U) = \{f: U \to \rr \mid f \text{ is bounded}\}.
\]

By bounded, we mean that $f: U \to \rr$ is bounded if there exists a constant 
$M \in \rr$ such that, for all $x \in U$, $|f(x)| \le M$. 
This example becomes important later, specifically in that it is an example 
of a presheaf which is not a sheaf (yet to be defined). 
</span>

Our next goal is to offer our first definition of a sheaf. To motivate the definition, we will 
consider our introductory example. 

Recall our presheaf $C: **Open**(X)\op \to **Set**$. Consider an open set 
$U$ with an open cover $\mathcal{U} = \{U_i\}_{i \in \lambda}$. Then every 
$f: U \to \rr$ in $C(U)$ corresponds to an element of $F(U_i)$ for all $i$; it is simply 
the restriction $f|_{U_i} \to \rr$. 

A natural question is the converse: If I have such an open cover $\mathcal{U}$ of $U$, 
and a family of continuous functions $f_i: U_i \to Y$, is there a continuous 
function $f: U \to \rr$ such that $f|_{U_i} = f_i$ for all $i$? 

Immediately, the answer is no: simply take a family in which the functions disagree on their overlaps. 
Thus, what if our family does agree on their overlaps? This would mean that, for every 
pair $i, j$, 

\[
f_{i}|_{U_i \cap U_j} = f_j|_{U_i \cap U_j}.
\]

(Of course, $U_i \cap U_j$ could be empty; but we don't know in general, 
so we just play it safe and consider *all* pairs $i, j \in \lambda$.)
The answer now is affirmative, there is an fact a $f: U \to \rr$ where $f|_{U_i} = f_i$ 
for all $i$. 
Thus we see that $C: **Open**(X)\op \to **Set**$ is a rather special type 
of presheaf, and we call this kind of functor a sheaf.


<span style="display:block" class="definition">
Let $X$ be a topological space.
A **topological sheaf (of sets) on $X$** is a presheaf 
$F: **Open**(X)\op \to **Set**$ such that, for every open 
set $U$ and any open cover $\mathcal{U} = \{U_i\}_{i \in \lambda}$ of $U$, 
the following two properties hold:
\begin{description}
\itemsep 0.25cm
\item[**(SH1)**]
If $f$, $g \in F(U)$ are such that $f|_{U_i} = g|_{U_i}$ for all 
$i \in \lambda$, then $f = g$. 

\item[**(SH2)**] 
Suppose that for all $i \in \lambda$, we have $h_i \in F(U_i)$ 
such that $h_i|_{U_i \cap U_j} = h_j|_{U_i \cap U_i}$ (i.e., a family 
of $h_i$ which agree on all possible overlaps). Then there exists a 
$h \in F(U)$ such that $h|_{U_i} = h_i$ for all $i \in \lambda$. 

\end{description}
A few comments about this definition:

*  In our definition, **SH2** is our main axiom of focus. We add 
**SH1** so that the given $h \in F(U)$ in **SH2** is necessarily 
unique.


*  Once again, the codomain of our sheaf does not have to $**Set**$. 
We will see this in a few examples. 


*  With the notion of a morphism of sheaves, we can define the \textbf{category 
of topological sheaves (of **Sets**)}, denoted $**Sh**(X, **Set**)$,
to be the category with objects sheaves and morphisms with natural transformations.



We end this definition by defining a **morphism of sheaves**; it is simply 
a natural transformation between sheaves. 
</span>

We now offer a few examples of topological sheaves.


<span style="display:block" class="example">
Consider again the introductory example $C: **Open**(X)\op \to \rr**-Mod**$. 
We show that this is a sheaf. Towards that goal, let $U$ be an open with open cover
$\mathcal{U} = \{U_i\}_{i \in \lambda}$.

\begin{description}
\itemsep 0.25cm
\item[**(SH1)**]
Suppose $f, g: U \to \rr$ are continuous functions which agree on the 
overlaps of the open cover. Then in this case it's clear that $f = g$. 

\item[**(SH2)**]
Suppose $f_i: U_i \to \rr$ is a family of continuous functions such that 
$f_i|_{U_i \cap U_j} = f_j|_{U_i \cap U_j}$ for all $i, j \in \lambda$. 
Construct a function $\phi: U \to \rr$ pointwise as follows: Given a $p \in U$, 
there exists some $k \in \lambda$ such that
$p \in U_k$. Therefore, let $\phi(p) = f_k(p)$; agreement on overlaps 
makes this well defined.


We show that $\phi$ is continuous.
For an open set $V$ of $\rr$, define $\phi^{-1}(V) = \bigcup_{i \in \lambda}f_i^{-1}(V)$.
As this is a union of open sets, $\phi^{-1}(V)$ is open and hence $\phi$ is continuous.
\end{description}
As we've satisfied **SH1** and **SH2**, we see that this is a sheaf.
</span>

A reader familiar with topology will note that our work towards the axiom 
**SH2** in the last example is nothing more than the standard proof of the 
*Pasting Lemma* from topology. 


<span style="display:block" class="example">
Consider the presheaf $H: **Open**(\mathbb{C}) \to \mathbb{C}**-Mod**$ 
which sends open sets of $\mathbb{C}$ to the $\mathbb{C}$-module of holomorphic 
functions defined on them.

This is also a sheaf, which we verify. Let $U$ be an open set of $\mathbb{C}$ 
and $\mathcal{U}=\{U_i\}_{i\in\lambda}$ an open cover.
\begin{description}
\itemsep 0.25cm
\item[(SH1)] This is true in the same was as the last example. 

\item[(SH2)] 
Let $f_i: U_i \to \mathbb{C}$ be a family of holomorphic functions
such that each $f_i$ agree on all possible overlaps. Define $f: U \to \mathbb{C}$ in 
the obvious way. To show that $f$ is holomorphic on $U$,
pick any $p \in U$. Then $p \in U_k$ for some $k$, and hence 
there exists an open set $D_k$ of $p$ such that 
$f_k(z) = \sum_{n = 1}^{\infty}a_n(z - p)^n$, i.e., it has a power series 
representation. This then gives us a well-defined power series representation 
for $f$, so that $f$ is holomorphic.
\end{description}


</span>



We now offer an example of a presheaf which is not a sheaf.


<span style="display:block" class="example">
Consider the presheaf $B: **Open**(X) \to \rr**-Mod**$
where $B(U)$ is the set of all bounded functions $f: U \to \rr$. 

In general, this is not a sheaf; axiom **SH2** is usually 
broken. For example, take $X = \rr$, and consider 
the open set $(0, 1)$, with the open cover given by 
the sets $\{ U_i = \left(\frac{1}{i}, 1 \right) \mid i = 1, 2, \dots \}$.
Observe that the functions 

\[
f_i(x): \left(\frac{1}{i},\, 1 \right) \to \rr \qquad f_i(x) = \frac{1}{x}
\]

agree on their overlaps, but clearly there is no bounded function 
$f: (0, 1) \to \rr$ such that $f|_{U_i} = f_i$ for all $i$.  Hence, 
this is not a sheaf.
</span>









