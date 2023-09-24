#3.5. Arbitrary Products and Coproducts in Categories

In this section, we perform a construction that allows us to have finite products and coproducts 
in a category. Once we achieve that construction, we easily generalize our work 
to obtain a definition for arbitrary products and coproducts in a category.

<span style="display:block" class="definition">
Let $\mathcal{D}_n$ be the discrete category with $n$-many objects (we use the letter $\dd$ for "discrete"). 
We will often visualize $\mathcal{D}_n$ as below.  
\begin{align_topbot}
\begin{tikzpicture}
\filldraw[yellow!30, rounded corners] (-4.3, -0.7) rectangle (4.3,0.7);
\node at (0,0){
\begin{tikzcd}[ampersand replacement= \&]
\bullet_1 \arrow[out=120,in=60,looseness=3,loop]
\&
\bullet_2 \arrow[out=120,in=60,looseness=3,loop]
\&
\bullet_3 \arrow[out=120,in=60,looseness=3,loop]
\&
\cdots 
\& 
\bullet_n \arrow[scale = 1, out=123,in=57,looseness = 3, loop]
\end{tikzcd}
};
\end{tikzpicture}
\end{align_topbot}
Note that 
a functor $F: \dd_n \to \cc$ is one which simply picks out $n$ different objects $A_1$, $A_2, 
\dots$, $A_n$ of $\cc$:

\[
F(\bullet_1) = A_1, \quad F(\bullet_2) = A_2, \quad  \dots,
\quad
F(\bullet_n) = A_n.
\]

This category allows us to make the following definition. 

\begin{definition}
Let $\cc$ be a category.
The $n$-th **diagonal functor** $\Delta_n: \cc \to \cc^{n}$,
is the functor defined as follows. 
\begin{description}
\item[On Objects.] For an object $C$, we have that $\Delta_n(C) = (\overbrace{C, C, \dots, C}^{n\text{-many copies}})$.
\item[On Morphisms.] For a morphism $f: A \to B$ in $\cc$, we have that  

\[
\Delta_n(f: A \to B) = (f, f, \dots, f): \Delta_n(A) \to \Delta_n(B).
\]

\end{description}
</span>
The diagonal  functor is also sometimes informally called the 
"copy" functor, since it is literally just copying data. We now 
make some observations. 


* [(**1**)] For each object $C \in \cc$, 
we can interpret the object $\Delta_n(C) \in \cc^n$ 
*as a functor*

\[
\Delta_n(C): \mathcal{D}_n \to \cc
\]

where $\Delta_n(C)$ sends $\bullet_i$ to  $C$ for all $i= 1, 2, \dots, n$.



* [(**2**)] Thus, we may also regard the $n$-th diagonal functor as a functor as below.

\[
\Delta_n: \cc \to \text{Fun}(\mathcal{D}_n, \cc) \qquad C \mapsto (\Delta_n(C) :\mathcal{D}_n \to \cc).
\]

In this interpretation, every morphism $f:C \to C'$ is interpreted as a natural 
transformation $\Delta_n(f): \Delta_n(C) \to \Delta_n(C')$. 



* [(**3**)] Consider a functor $F: \dd_n \to \cc$ such that $F(\bullet_i) = A_i \in \cc$. 
For each $C \in \cc$, a natural transformation 

\[
\eta: \Delta_n(C) \to F
\]

will simply correspond to $n$-many morphisms $\eta_1, \dots, 
\eta_n$ where

\[
\eta_i: \Delta_n(C)(\bullet_i) \to  F(\bullet_i) 
\implies 
\eta_i: C \to A_i.
\]




\end{definition}
With this notation clarified, we now can propose  our  definition of a  product. 


<span style="display:block" class="definition">[Finite Product and Coproduct Definition]
Let $\cc$ be a category. Let $A_1$, $A_2, \dots$, $A_n$ be objects of $\cc$. Let 
$F: \mathcal{D}_n \to \cc$ be the functor such that $F(\bullet_i) = A_i$.


*  The **product** of $A_1, A_2, \dots, A_n$ 
is an object $P$ of $\cc$ equipped with
a (natural transformation) $ \displaystyle p: \Delta_n\left( P \right) \to F$ 
such that 
\begin{center}
$\displaystyle \left( P, p: \Delta_n\left( P \right) \to F \right)$
is universal from 
\hyperref[definition:universal_morphism_from_D_to_F]{\textcolor{blue}{$\Delta_n$ to $P$}.}
\end{center}        In the case where the product $P$ exists, we write $P = \prod_{i = 1}^{n} A_i$. 



*  The **coproduct** of $A_1, A_2, \dots, A_n$
is an object $C$ of $\cc$ equipped with 
a (natural transformation) $i: F \to \Delta_n(C)$ such that 
\\begin{center}
$(C, i: F \to \Delta_n(C))$ is universal from \hyperref[definition:universal_morphism_from_F_to_D]{\textcolor{blue}{$C$ to $\Delta_n$}}.
\end{center}       In the case where the coproduct $C$ exists, we write $C = \coprod_{i = 1}^{n} A_i$ 




</span>
\begin{remark}
By Observation (**3**) as above, if $\displaystyle p: \Delta_n\left( \prod_{i=1}^{n}A_i \right) \to F$
is a natural transformation, then it corresponds to $n$-many morphisms 

\[
p_k: \prod_{i=1}^{n}A_i \to A_k \qquad k = 1, 2, \dots, n
\]

This matches our intuition: A product of $n$-objects should always have 
$n$-many morphisms between the product and each of its factors. 

Similarly, a natural transformation $i: F \to \Delta_n\left( \coprod_{i = 1}^{n}A_i \right)$ corresponds to 
$n$-many morphisms 

\[
i_k: A_k \to \coprod_{i = 1}^{n}A_i \qquad k = 1, 2, \dots, n
\]

which again matches our intuition: A coproduct of $n$-objects should have 
$n$-many morphisms between each of its factors and the coproduct.
\end{remark}

We now have everything we need to define arbitrary products and coproducts, including 
infinite ones.
We just need to specify some notation that we will use.
Towards that goal, let $\lambda$ be some indexing set.  

*  Define $\dd_{\lambda}$ to be the discrete category consisting of one object $\bullet_i$ for each $i \in 
\lambda$. (In particular, $\dd_{\lambda}$ is now possibly infinite.)


*  Define the $\lambda$-diagonal functor to be the functor $\Delta_{\lambda}: \cc \to \text{Fun}(\dd_{\lambda}, \cc)$
where $\Delta_{\lambda}(C): \dd_{\lambda} \to \cc$ 
sends each $\bullet_i$ to $C$ for all $i \in \lambda$.





<span style="display:block" class="definition">[Arbitrary Product and Coproduct Definition]
Let $\cc$ be a category, and consider an arbitrary set of objects $\{A_i\}_{i \in \lambda}$ of $\cc$, $\lambda$ some indexing set.
Let $F: \dd_{\lambda} \to \cc$ be the functor such that $F(\bullet_{i}) = A_i$ for $i \in \lambda$.


*  The **product** of $\{A_i\}_{i \in \lambda}$ is the object 
$P$ of $\cc$
equipped with a (natural transformation) $\displaystyle p: \Delta_{\lambda}\left( P\right) \to F$ 
such that 
\\begin{center}
$\left( P, \Delta_{\lambda}\left( P \right) \to F \right)$ is universal from 
\hyperref[definition:universal_morphism_from_F_to_D]{\textcolor{blue}{$\Delta_{\lambda}$ to $P$}.}
\end{center}           In the case where the product $P$ exists, we write $P = \prod_{i \in \lambda}A_i.$



*  The **coproduct** of $\{A_i\}_{i \in \lambda}$ is the object 
$C$ of $\cc$ equipped with a (natural transformation) $i: F \to \Delta_{\lambda}(C)$
such that 
\\begin{center}
$(C, i:  F \to \Delta_{\lambda}(C))$ is universal from 
\hyperref[definition:universal_morphism_from_D_to_F]{\textcolor{blue}{$C$ to $\Delta_{\lambda}$}}.
\end{center}       


</span>

\begin{remark}
Notice the inherent duality present in the definition of a product and coproduct. 
This is one of the reasons category theory is nice; one now has a new perspective of 
understanding, for example, the free product operation and the 
group product operation in **Grp**; they're dual concepts!
\end{remark}

Since products and coproducts of objects are universal objects, we obtain some 
nice results since we already know how universal objects operate. Before introduce 
such results, we require the following lemma. 


<span style="display:block" class="lemma">
Let $\cc$ be a locally small category, and let $\{A_i\}_{i \in \lambda}$ 
be objects of $\cc$. Suppose their product exists in $\cc$. Then the functor 

\[
\prod_{i \in \lambda}\hom_{\cc}(-, A_i): \cc \to **Set**
\]

which sends an object $C$ to the set $\prod_{i \in \lambda}\hom_{\cc}(C, A_i)$ 
is representable by the functor 

\[
\hom_{\text{Fun}(\dd_{\lambda}, \cc)}(\Delta_{\lambda}(-), F): \cc \to **Set**.
\]

</span>

The proof is left as an exercise. It is not difficult to show; it simply requires realizing that there 
is a natural bijection between $\prod_{i \in \lambda}\hom_{\cc}(C, A_i)$ and 
$\hom_{\text{Fun}(\dd_{\lambda}, \cc)}(\Delta_{\lambda}(C), F)$ for each $C \in \cc$.

Using all of our previous work we now have the following proposition.


<span style="display:block" class="proposition">
Let $\cc$ be a locally small category, and let $\{A_i\}_{i \in \lambda}$ be a set of objects in $\cc$. 
Denote $F: \dd_{\lambda} \to \cc$ where $F(\bullet_i) = A_i$ for all $i \in \lambda$.

*  If the product $\prod_{i \in \lambda}A_i$ 
exists in $\cc$, then for each object 
$C$ of $\cc$, we have the natural bijection

\[
\prod_{i \in \lambda}\hom_{\cc}(C, A_i) \cong \hom_{\cc}\left(C,\, \prod_{i \in \lambda}A_i\right)
\]




*  If the coproduct $\coprod_{i \in \lambda}A_i$ exists 
in $\cc$, then for each object $C$ of $\cc$, we have the natural bijection 

\[
\prod_{i \in \lambda}\hom(A_i, C)
\cong 
\hom_{\cc}\left( \coprod_{i\in \lambda}A_i, \, C \right).
\]




</span>


<span style="display:block" class="proof">
We only prove the first result, since the second follows similarly. 
Since $\prod_{i \in \lambda}A_i$ exists in $\cc$, we know that this implies 
$\prod_{i \in \lambda}A_i$ is equipped with a natural transformation 
$p: \Delta_{\lambda}\left(\prod_{i \in \lambda}A_i\right) \to F$ such that 
$(\prod_{i \in \lambda}A_i, p)$ is universal from $\Delta_{\lambda}$ to $P$. 

From this perspective, we can apply the result of Exercise \hyperref[exercise:universality_bijection]{3.2.1} 
to conclude that, for each object $C$, we have the natural bijection below. 

\[
\hom_{\cc}\left(C, \,\prod_{i \in \lambda}A_i\right) \cong
\hom_{\text{Fun}(\dd_{\lambda}, \cc)}(\Delta_{\lambda}(C), F).
\]

However, we know from Lemma \ref{lemma:product_of_hom_sets} that there is a natural bijection 

\[
\hom_{\text{Fun}(\dd_{\lambda}, \cc)}(\Delta_{\lambda}(C), F)
\cong 
\prod_{i \in \lambda}\hom_{\cc}(C, A_i).
\]

Thus we have a natural bijection

\[
\prod_{i \in \lambda}\hom_{\cc}(C, A_i) \cong \hom_{\cc}\left(C, \,\prod_{i \in \lambda}A_i\right)
\]

as desired.

The second result is left as an exercise (we outline the steps for the reader).

</span>

\begin{remark}
Note that the above proposition is saying something very deep and beautiful 
about products and coproducts as a concept. Moreover, also note that a direct proof would have been very long-winded 
and complicated, but that our previous work made it possible to give a proof consisting 
of a few lines. Thus, a categorical perspective is evidently sometimes useful. 
\end{remark}

We now introduce the following interesting property. This property becomes 
an important observation when we begin look at *abelian categories*. 


<span style="display:block" class="proposition">
Let $\cc$ be a category and let $\{A_i\}_{i \in \lambda}$ be a set of objects in $\cc$.
Suppose the product $\prod_{i \in \lambda}A_i$ and coproduct $\coprod_{i \in \lambda}A_i$
exist in $\cc$. Then there is a canonical morphism 

\[
\phi:\prod_{i \in \lambda}A_i \to \coprod_{i \in \lambda}A_i 
\]

in $\cc$.
</span>


<span style="display:block" class="proof">
Let $F: \dd_{\lambda} \to \cc$ be the functor where $F(\bullet_i) = A_i$.
Then the product and coproduct are equipped with the natural transformations as below. 

\[
\Delta_{\lambda}\left( \prod_{i \in \lambda}A_i \right) \to F
\quad \quad
F \to \Delta_{\lambda}\left( \coprod_{i \in \lambda}A_i \right)
\]

Then we can compose them to obtain the natural transformation

\[
\Delta_{\lambda}\left( \prod_{i \in \lambda}A_i \right) \to \Delta_{\lambda}\left( \coprod_{i \in \lambda}A_i \right).
\]

By the universal property of the coproduct, this implies a unique $\phi: \prod_{i \in \lambda}A_i \to \coprod_{i \in \lambda}A_i$
such that the diagram below commutes. 
\
<img src="../../png/chapter_3/section_5_figure_0.png" width="99%" style="display: block; margin-left: auto; margin-right: auto;"/>
</span>

\begin{remark}
Here is one of our first uses of the word "canonical." This is not an adjective 
that adds detail to our morphism (e.g., an extra mathematical property),
but it is a word we superfluously wrote to emphasize to the reader 
that morphisms of a given form cannot always be found in categories. 

The word "canonical" is often used in category theory language, but it is never really defined 
because its always secretly assumed that everyone knows what it means. 
It's a useful word, so we will use it later on, but again: it means nothing 
more than "There exists an obvious morphism of a given form."
\end{remark}

{\large **Exercises**
\vspace{0.5cm}}


* [**1.**] Prove Lemma \ref{lemma:product_of_hom_sets}. (Note: the notation and statement may make 
it look harder than it actually is.)



* [**2.**]
Complete the proof of Proposition \ref{proposition:product_coproduct_natural_bijection} as follows. 
\begin{itemize}


* [*i*.]
Show that the functor 

\[
\prod_{i \in \lambda} \hom_{\cc}(A_i, -): \cc \to **Set**
\]

is representable by the functor 

\[
\hom_{\text{Fun}(\dd_{\lambda}, \cc)}(F, \Delta_{\lambda}(-)): \cc \to **Set**
\]



* [*ii*.]
Using (*i*), Proposition \ref{proposition:universality_bijection}, and 
interpreting coproducts as universal objects, prove that 

\[
\prod_{i \in \lambda}\hom(A_i, C)
\cong 
\hom_{\cc}\left( \coprod_{i\in \lambda}A_i, \, C \right).
\]




* [**3.**]
Let $P$ be a preorder with binary relation $\le$. 
Consider a subset $A \subset P$ where $A = \{a_i \in P \mid i \in \lambda\}$ 
with $\lambda$ some indexing set.
\begin{itemize}


* [(*i*.)]
Regarding $P$ as a thin category, prove that the product $p = \displaystyle \prod_{i \in \lambda}a_i$, when it exists, 
is the supremum of $A$. 
\\
*Hint:* Recall that, if $X$ is a preorder, 
the **supremum** of a set $S \subset X$ is the element $s \in X$ 
such that if $a_i \le s'$ for all $i \in \lambda$, then 
$s \le s'$.


* [(*ii*.)] 
We know that the dual of the product is the coproduct. 
Can you guess what the coproduct $\displaystyle \coprod_{i \in \lambda}a_i$ in $P$ is 
in this case? Prove it. 




\item[**4.**] Let $\cc$ and $\dd$ be categories. 
Consider the functor category $**Fun**(\cc, \dd)$. What is a product in 
this category? What conditions do we need to place on $\cc$ and $\dd$ for this 
product to exist?
\end{itemize}        
\end{itemize}



