#8.4. Kernels and Cokernels
At this point we've discussed preadditive, additive, and preabelian categories, where 
preabelian categories are just additive categories with the additional hypothesis 
that kernels and cokernels exist. This additional hypothesis is extremely useful, 
so we will demonstrate what this implies for us. 

Let $\cc$ be a preabelian category.
Consider an arbitrary morphism $f: A \to B$. 
One way to think about kernels and Cokernels is that they give rise to objects 
in the comma categories $(\cc \downarrow A)$ and $(B \downarrow \cc)$. 

<img src="../../png/chapter_8/section_4_figure_0.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
Now in the comma category $(\cc \downarrow A)$, a morphism between two objects 
$(C, f: C \to A)$ and $(D, g: D \to A)$ is a morphism $h: D \to C$ in $\cc$ such that 
$f = g \circ h$. Similarly, a morphism in the comma category $(A \downarrow \cc)$ 
between two objects $(P, m: A \to P)$ and $(Q, n: A \to Q)$ is a morphism $k: P \to Q$ such that 
$n = h \circ m$. These relations give rise to the bow-tie diagram:
\
<img src="../../png/chapter_8/section_4_figure_1.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
ith that said, we can actually turn these categories into partial orders. 
In $(\cc \downarrow A)$, we say $g \le f$ if there exists an $h$ such that $f \circ h = g$, 
and in $(A \downarrow \cc)$, we say $m \le n$ if there exists a $k$ such that 
$n = k \circ m$. 


It turns out that this perspective is actually quite useful. 


<span style="display:block" class="proposition">
Let $\cc$ be a category with a zero object, equalizers and coequalizers. 
Then for each object $A$ of $\cc$, we have the functors 

\begin{align*}
\ker&: (A \downarrow \cc) \to (\cc \downarrow A)\\
\coker&:(\cc \downarrow A) \to (A \downarrow \cc).
\end{align*}

that assign kernels and cokernels.
Moreover, these functors establish a antitone Galois correspondence; hence we have that 

\begin{align*}
\ker(\coker(\ker(f))) = \ker(f) 
\quad 
\coker(\ker(\coker(f))) = \coker(f).
\end{align*}

Therefore, any $\phi$ is a kernel if and only if $\phi = \ker(\coker(\phi))$, while 
any $\psi$ is a cokernels if and only if $\psi = \coker(\psi(\psi))$. 
</span>


<span style="display:block" class="proof">
We demonstrate functoriality. First we want our functor 
to act on objects as 

\[
(C, f: A \to C) \mapsto (\ker(f), e_1: \ker(f) \to A). 
\]

Now we explain how the functor works on morphisms. 
Suppose we have two objects of our 
comma category $(C, f: A \to C)$ and $(D, g: A \to D)$, and that $h: D \to C$
is a morphism in $(A \downarrow \cc)$ 
from $(D, g: A \to D)$ to $(C, f: A \to C)$. Then we have the diagram below.
\
<img src="../../png/chapter_8/section_4_figure_2.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
Now note that 

\[
f \circ e_2 = (h \circ g) \circ e_2 = h \circ (g \circ e_2) = 0.
\]

Thus, by the universal property of $e_1: \ker(f) \to A$, we know there 
exists a *unique* morphism $h': \ker(g) \to \ker(f)$ such that the diagram 
below commutes.
\
<img src="../../png/chapter_8/section_4_figure_3.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>

However, this is exactly what it means to have a morphism between the objects 
$(\ker(g), e_2: \ker(g) \to A)$ and $(\ker(f), e_1: \ker(f) \to A)$. 
Thus we see that our functor maps on morphisms in $(A \downarrow \cc)$ in a nice 
way:  

\[
h  \mapsto 
h':
(\ker(g), e_2: \ker(g) \to A) 
\to 
(\ker(f), e_1: \ker(f) \to A).
\]

where $h'$ is the unique map obtained from $h$ as explained above. 
With the remaining properties easily verified, this defines a functor between the categories. 
In addition, we can dualize our work above to also get the functor 
$\coker: (\cc \downarrow A) \to (A \downarrow \cc)$. 

Now this creates a Galois correspondence by regarding the comma categories as 
partially ordered sets. Suppose that $g \le \ker(f)$. That is, there exists a $h$ such that 
$\ker(f) \circ h = g$. Then we can compare $\coker(g)$ and $f$ by considering the diagram below. 
\
<img src="../../png/chapter_8/section_4_figure_4.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
Now observe that 

\[
f \circ g = f \circ (e \circ h) = 0 \circ h = 0.
\]

Therefore, by the universal property of the cokernel, we know there 
exists a unique morphism $h': \coker(g) \to f$ such that the diagram 
below commutes. This then implies that $f \le \coker(g)$. 
\
<img src="../../png/chapter_8/section_4_figure_5.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
By a similar argument, we have that if $f \le \coker(g)$, 
then $g \le \ker(f)$. Hence we have that 

\[
g \le \ker(f) \iff f \le \coker(g)
\]

so that, as preorder, the kernel and cokernels functors are adjoint pairs 
that form an antitone Galois correspondence. Moreover, this implies that
for each $f: B \to A$ and $g: A \to C$,

\[
f \le \coker(\ker(f)) \qquad g \le \ker(\coker(g)).
\]

In particular, if $f$ is the cokernel of some morphism $\phi$, and if $g$ is
the kernel of some morphism $\psi$, then we have that 

\[
\coker(\phi) \le \coker(\ker(\coker(\phi)))
\quad
\ker(\psi) \le \ker(\coker(\ker(\psi))).
\]

However, applying the order reversing functors $\coker$ and $\ker$ on the relations 
$\phi \le \ker(\coker(\phi))$ and $\psi \le \coker(\ker(\psi))$ yields 

\[
\coker(\ker(\coker(\phi))) \le \coker(\phi)
\quad 
\ker(\coker(\ker(\psi))) \le \ker(\psi).
\]

Hence we have that $\coker(\ker(\coker(\phi))) \cong \coker(\phi)$
and
$\ker(\coker(\ker(\psi))) \cong \ker(\psi)$ as desired. 
</span>








