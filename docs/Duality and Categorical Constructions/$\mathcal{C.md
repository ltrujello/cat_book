#2.1. $\mathcal{C
op$ and Contravariance}


<span style="display:block" class="definition">
Consider a category $\mathcal{C}$. Then we define the
**opposite category of $\cc$**, denoted $\mathcal{C}\op$, 
to be the category where 
\begin{description}
\item[Objects.] The same objects of $\cc$.
\item[Morphisms.] If $f: A \to B$ is a
morphism of $\cc$, then we let 
$f\op : B \to A$ be a morphism of $\cc\op$.
\end{description}
In this case, composition isn't exactly obvious, so we will explain how that 
works. 

Let $f: A \to B$ and $g: B \to C$ be morphisms of $\cc$. Then we obtain 
morphisms $f\op: B \to A$ and $g\op: C \to B$. In this case $f\op, g\op$ are composable, 
and we define composition of $\cc\op$, 
denoted as $\circ\op$, 
to be the morphism 

\[
f\op \circ g\op: C \to A.
\]

Moreover, we have the relation $(g \circ f)\op = f\op \circ g\op$.
</span>

Taking the opposite category might seem very strange, 
but we are doing nothing more than just taking the same category 
and swapping the domain and codomain of every
morphism. 

Consequently, many properties of morphisms are similarly reversed.
For example, if $f: A \to B$ is
monomorphism in $\cc$, then $f\op: B \to A$ is an epimorphism in 
$\cc\op$. 
More generally, every logically valid statement that can be made in
$\cc$ using its objects and morphisms can be dualized to achieve an
equivalent, logically valid statement in $\cc\op$ using its
objects and morphisms. 


<span style="display:block" class="example">
Consider a category $\cc$ containing $3$ objects
whose morphisms are arranged as follows:

<img src="../../png/chapter_2/section_1_figure_0.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
What does the dual category $\cc\op$ look like? Well, $\cc\op$
contains the same objects $A, B$ and $C$. As for the morphisms, $\cc$
has the three morphisms $f, g, h$, in addition to their composites.
Therefore, $\cc\op$ also has three morphisms 
$f\op:B \to A$, $g\op: C \to
B$ and $h\op: A \to C$ and their composites. Hence, $\cc\op$ looks like this:
\
<img src="../../png/chapter_2/section_1_figure_1.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
</span>


<span style="display:block" class="example">
Let $P$ be a preorder, specifically a partial order. 
Recall that this means that $P$ has 
a binary relation  $\le$ and if $p \le p'$
and $p' \le p$, then $p = p'$. 

We claim that that $P\op$ is still a partial order. But first, 
what does $P\op$ even look like? If we have some elements $p_1, p_2, p_3$ in
$P$ such that 

\[
p_1 \le p_2 \le p_3
\]

Then, as a category, $P$ has the unique morphisms $f: p_1 \to p_2$ and 
$g: p_2 \to p_3$. Hence, in $P\op$, we have the unique morphisms 
$g\op : p_3 \to p_2$ and $f\op:p_2 \to p_1$, 
so that we obtain a reversed binary relation $\le\op$ in $P$, which 
reorder $p_1, p_2, p_3$ as below.

\[
p_3 \le\op p_2 \le\op p_1
\]

This is kinda weird to write, and in fact, it makes 
more sense if we 
write $\le\op = \ge$ as the binary relation in $P\op$. We then have that 

\[
p_1 \le p_2 \le p_3 \text{ in } P 
\implies p_3 \ge p_2 \ge p_1 \text{ in } P\op
\]

which is nice!
Things are even nicer in a linear order, for if $P = \{p_1,
p_2, p_3, \dots \}$ is a linear order, then we can write that 

\[
\cdots p_i \le p_j \le p_k \cdots   
\]

and hence in $P\op$ this becomes 

\[
\cdots p_i \ge p_j \ge p_k \cdots.
\]

</span>


<span style="display:block" class="example">
Let $(G, \cdot)$ be a group. 
In group theory one can formulate the **opposite group** $(G\op, \cdot\op)$ 
as follows. Define
$(G\op, \cdot\op)$ to be group with the same set of elements as $G$, 
whose product $\cdot\op$ works as 

\[
g_1 \cdot\op g_2 = g_2 \cdot g_1.   
\]

Since both $(G, \cdot)$ and $(G, \cdot\op)$ are groups, we can regard them both 
as one object categories. What is interesting to realize is that under the 
categorical interpretation, they are opposite categories of each other.



</span>

We thus see that dualizing a category simply involves changing the 
directions of the morphisms  on the objects. But can we dualize a 
functor?













<span style="display:block" class="definition">
Let $F: \cc \to \dd$ be a functor and suppose $f: A \to B$ is
morphism in $\cc$. We say $F$ is a **contravariant functor**
if $F(f): F(B) \to F(A)$.
</span>
This is in sharp contrast to a *covariant* functor, in which $f: A \to B$
is sent to $F(f): F(A) \to F(B)$. 

We next introduce a few examples to demonstrate a contravariant functor. 


<span style="display:block" class="example">
Let $k$ be an algebraically closed field. Recall that $A^n(k)$ is the set of tuples 
$(a_1, a_2, \dots, a_n)$ with $a_i \in k$. In algebraic geometry, it 
is of interest to associate each subset $S \subset A^n(k)$
with the ideal

\[
I(S) = \bigg\{f \in k[x_1, \dots, k_n] \;\bigg|\; f(s) = 0 \text{ for all } s \in S \bigg\}.  
\]

of $k[x_1, \dots, x_n]$.
Observe that this is always non-empty since $0 \in I(S)$ for any $S$. 
In additional, it is clearly an ideal of $k[x_1, \dots, x_n]$, 
since for any $p \in k[x_1, \dots, x_n]$,$q \in I(S)$, we have that 

\[
(p \cdot q)(s) = p(s)\cdot q(s) = p(s) \cdot 0 = 0 \text{ for all } s \in S.
\]

so that $p\cdot q \in I(S)$. Now it's usually an exercise to show that 
if $S_1 \subset S_2$ are two subsets of $A^n(k)$, then one has that 
$I(S_2)\subset I(S_1)$. Hence this defines a contravariant functor

\[
I: **Subsets**(A^n(k)) \to **Ideals**(k[x_1,\dots, x_n]).
\]

where $**Subsets**(A^n(k))$ is the category of subsets with inclusion morphisms, 
and $**Ideals**(k[x_1,\dots, x_n])$ is the category of ideals with inclusion 
ring homomorphisms.
</span>


<span style="display:block" class="example">
Consider again $k$ as an algebraically closed field. In algebraic geometry, 
one often wishes to associated each ideal of $k[x_1, \dots, x_n]$
with its "zero set" 

\[
Z(I) = \bigg\{s = (a_1, \dots, a_n) \in A^n(k) \;\bigg|\; f(s) = 0 \text{ for all } s \in I\bigg\}.
\]

It is usually an exercise to show that if $I_1 \subset I_2$ are two ideals, 
then $Z(I_2) \subset Z(I_1)$. Hence we see that this defines a contravariant functor 

\[
Z: **Ideals**(k[x_1, \dots, x_n]) \to **Subsets**(A^n(k)).
\]

</span>

It is usually at the beginning of an algebraic geometry course that one 
will understand the relationship between these two constructions, which themselves 
are secretly functors.

What follows is a very interesting example. In fact, this example is an example of a 
beautiful concept of a *sheaf*, and it is usually used as a motivating 
example. But that is for later. 


<span style="display:block" class="example">
Let $X$ be a topological space, and 
consider the thin category $**Open**(X)$, which contains
all open sets $U \subset X$, equipped with the inclusion
function $i_{U, X}: U \to X$. 

For each $U \in **Open**(X)$, define the set

\[
C(U) = \{f: U \to \rr \mid f \text{ is continuous.}\}
\]

Note that if $U \subset V$ are in $**Open**(X)$, then 
we define the function 
$\rho_{U,V}: C(V) \to C(U)$ where 

\[
\rho_{U,V}(f: V \to \rr) = f\big|_{U}: U \to \rr.
\]

That is, $\rho_{U,V}$ sends continuous, real-valued functions 
on $V$ to such functions on $U$ by restriction. 
It is not difficult to show that this respects identity and composition 
requirements, so that we have a contravariant functor

\[
C(-) : **Open**(X) \to **Set**
\]

for each topological space $X$. 
</span>

What follows is another very important example. 


<span style="display:block" class="example">
Let $\cc$ be a locally small category. In this case, we know that 
each $A \in \cc$ induces the covariant functor

\[
\hom_{\cc}(A, -) : \cc \to **Set**
\]

which sends objects $C$ to the set $\hom_{\cc}(A, C)$. 
It is natural to ask if we may similarly define a functor  

\[
\hom_{\cc}(-, A): \cc \to **Set**.
\]

The answer is yes. We did not make this observation in the past 
for pedagogical reasons, since it's actually a contravariant functor 
(and we didn't know what that was until now). We can now safely say 
that $\hom_{\cc}(-, A)$ is a contravariant functor. 
</span>

We now comment on the relationship between contravariant and covariant functors. 


<span style="display:block" class="proposition">
Let $\cc$, $\dd$ be categories. 

*  Let $F: \cc \to \dd$ be a contravariant functor. Then $F$ corresponds to a 
contravariant functor $\overline{F}: \cc\op \to \dd$ where for a $f\op : B \to A \in \cc\op$, 

\[
\overline{F}(f\op : B \to A) = F(f: A \to B) = F(f): F(B) \to F(A).
\]



*  Conversely, let $F: \cc \to \dd$ be a covariant functor. Then $F$ 
corresponds to a contravariant functor $\overline{F}: \cc\op \to \dd$ 
where 

\[
\overline{F}(f\op : B \to A) = F(f: A \to B) = F(f): F(A) \to F(B)
\]




</span>

The above proposition allows us to treat any functor as covariant or 
contravariant. Thus, if we don't like the behavior of our functor on morphisms, we can 
find an equivalent functor that behaves on morphisms in our preferred way. 

Generally, covariant functors are easier to think about, so we often like 
to turn contravariant functors into covariant functors. 


<span style="display:block" class="example">
Recall that the functor 

\[
C(-): **Open**(X) \to **Set**
\]

is contravariant. What if we want to treat this as a covariant functor? 
Well, we can define the functor 

\[
\overline{C}(-): **Open**(X)\op \to **Set**            
\]

as follows. If $U \subset V$ are open subsets of the topological space $X$, 
then let $i: U \to V$ be the inclusion. This is a morphism in $**Open**(X)$.
Hence, $i\op: V \to U$ is a morphism in $**Open**(X)\op$. 
Therefore, we define

\[
\overline{C}(i\op: V \to U) = C(i: U \to V) = \rho_{U,V}: C(V) \to C(U).
\]

Thus we see that this functor $\overline{C}$ acts the same way as $C$, except 
it behaves covariantly on the morphisms now instead of contravariantly. 
</span>



