#1.7. Examples and Nonexamples of Functors
Functors were not defined out of arbitrary interest. The definition of a functor 
was motivated by constructions that were seen in mathematics
(unlike constructions in say, number theory, which 
are interesting in their own right). 
Thus in this section, we include a wide variety of different constructions in 
in different areas of mathematics which all fit the definition of a functor. 
We present examples 
from algebraic topology, differential geometry, topology, algebraic geometry, 
abstract algebra and set theory.

In short, this section is due to the fact that the only way to really understand what a functor does is to realize 
the definition *with examples*.  It's not necessarily important to understand *all* 
the examples, if for instance you have never worked with differential geometry, 
but it would be good to get a few of them. What is more important is 
witnessing how such a simple definition can be so versatile and prevalent
in seemingly different fields of mathematics; thus, what is important is 
witnessing the flexibility of functors (in addition to filling in the details of 
the examples and doing the exercises at the end).
\\





















{\large\noindent **Algebraic Geometry.**\par}


<span style="display:block" class="example">
In algebraic geometry, it is often of interest to construct the **affine $n$-space**
$A^n(k)$ of a field $k$. Usually, $k$ is an algebraically closed field, but it doesn't have to be.

\[
A^n(k) = \{(a_0, \dots, a_{n-1}) \mid a_i \in k \}.
\]

For example, when $k = \rr$, we have that $A^n(k) = \rr^n$. 
Moreover, we claim that we have a functor $A^n(-): \fld \to \Set$.
To see this, we need to figure out where $A^n(-)$ sends objects and morphisms.

We can first observe that $A^n(-)$ sends fields $k$ to sets $A^n(k)$.
Secondly, we can observe that for a field homomorphism $\phi: k \to k'$,    
we can define the function $A^n(\phi): A^n(k) \to A^n(k')$ where
for each $(a_1, \dots, a_n) \in A^n(k)$ we have that

\[
A^n(\phi)(a_0, \dots, a_{n-1}) = (\phi(a_0), \dots,  \phi(a_{n-1})).
\]

The reader can show that this satisfies the rest of the axioms of a functor. Overall, 
we can say that we have a functor 

\[
A^n(-): \fld \to \Set.  
\]

</span>


<span style="display:block" class="example">
Once the affine $n$-space is defined, the next step in algebraic geometry is to construct 
the **projective space** $P^n(k)$ for a field $k$. To define this, we first 
define an equivalence relation on $A^{n+1}(k)$. We say 

\[
(a_0, \dots,  a_n) \sim (b_0, \dots, b_n) \text{ if there is a nonnzero } \lambda \in k \text{ such that } a_i = \lambda b_i.
\]

This defines an equivalence relation on the points of $A^n(k)$. Geometrically, this equivalence relation 
says two points are equivalent whenever they lie on the same line passing through the origin.
With this equivalence relation, we then define

\[
P^n(k) = A^{n+1}/\sim = \Big\{[(a_0, \dots, a_n)] \mid (a_0, \dots, a_n) \in A^{n+1}(k)\Big\}.
\]

Hence we see that $P^n(k)$ is the set of equivalence classes under this equivalence relation. Similar to 
the previous example, this construction is also functorial. Consider a field homomorphism $\phi: k \to k'$. Then we 
define the function $P^n(\phi): P^n(k) \to P^n(k')$ where 

\[
P^n(\phi)([a_0, \dots, a_n]) = [(\phi(a_0), \dots, \phi(a_n))].           
\]

However, when defining functions on a set of equivalence classes, we need to be careful. 
It's possible that the function could send equivalent objects to different things, so that such 
a fuction would not be well-defined. In this case, the above function is in fact well-defined. 
This is because $\phi(\lambda a_i)  =\phi(\lambda) \phi(a_i)$ for any $i = 0, 1, \dots, n$. 
Therefore we can state that we have a functor 

\[
P^n(-): \fld \to \Set.  
\]

</span>
\vspace{0.5cm}  

{\large\noindent **Algebraic Topology.**\par}


<span style="display:block" class="example">
An important example of a
functor arises in homology theory. For example, in singular homology
theory, one considers a topological space $X$ and associates this 
with its $n$-th homology group.

\[
X \mapsto H_n(X)
\]

In a typical 
topology course, one then proves that if $f: X \to Y$ is a continuous 
mapping between topological spaces, then $f$ induces a group homomorphism 

\[
H_n(f): H_n(X) \to H_n(Y) 
\]

in such a way that for a second mapping $g: Y \to Z$, $H_n(g \circ f) 
= H_n(g) \circ H_n(f)$ for all $n$. Finally, we also know that 
$H_n(1_X) = 1_{H_n(X)}$.
Therefore, what we see is that this process can be cast into the language 
of category theory, so that we may define a \textbf{singular 
homology functor}

\[
H_n: \top \to \ab
\]

since this functorial process sends topological spaces in $\top$
to abelian groups in $\ab$.
</span>


<span style="display:block" class="example">
Another example from algebraic topology can be
realized from the **fundamental group**

\[
\pi_1(X, x_0) = \{[x] \mid x \in X\}
\]

with $x_0 \in X$, and 
where $[x]$ is the equivalence class of loops based at $x_0$, subject 
to the homotopy equivalence 
relation. First observe that $X \mapsto \pi_1(X)$ is in fact a mapping 
of objects between $\top^*$ and $\grp$. Second, 
observe that if $f: X \to Y$ is a continuous function, then 
we can define a group homomorphism 

\[
\pi_1(f): \pi_1(X) \to \pi_1(Y) \qquad [x] \mapsto [f(x)].
\]

Note that this is well defined since if $x \sim x'$ then 
there is a homotopy relation $H: X \times [0, 1] \to Y$. However, 
$f \circ H$ is also another homotopy relation that establishes that 
$f(x) \sim f(x')$; hence our group homomorphism is well defined. 

Moreover, if $f: X \to Y$ and $g:Y \to Z$ are continuous, then 
we can check that $\pi_1(g \circ f) = \pi_1(g) \circ \pi_1(f)$;
if $[\alpha] \in \pi_1(X, x_0)$,
then

\[
(g \circ f)_*([\alpha]) = [(g \circ f) \circ \alpha] 
= [g \circ (f \circ \alpha)]
= g_*([f_*([\alpha])]) = g_* \circ f_*([\alpha]) 
\]

so that $(g \circ f)_* = g_*f_*$. Finally, we 
can examine how the identity map $1_X$ on a topological 
space acts on an element $[\alpha] \in \pi_1(X, x_0)$:

\[
id_*([\alpha]) = [id \circ \alpha] = [\alpha].
\]

so that it is sent to the identity homomorphism. All together, this allows 
us to conclude that this process is entirely functorial, so we may summarize our 
results by stating that 

\[
\pi_1: \top^* \to \grp   
\]

is a functor.
</span>

We now present two examples from differential geometry, which aren't traditionally 
presented as examples of functors but are nevertheless interesting in their 
own right. 
\vspace{0.5cm}

{\large\noindent **Differential Geometry.**\par}

<span style="display:block" class="example">
Let $M^n$ be a differentiable manifold of dimension $n$. In general, this 
means that there exists
a family of open sets $U_\alpha \subset \rr^n$ and injective 
mappings $\bm{x}_\alpha: U_\alpha \to M$ for $\alpha \in \lambda$, $\lambda$ an indexing 
set, with the mappings subject to various conditions\footnote{There isn't 
a universally agreed upon set of conditions, and we won't really need to worry about 
them here. If the reader likes, they can consult Do Carmo's *Riemannian Geometry*, 
which is, and has been for a long time, the go-to differential geometry text.
}. 
Recall from differential 
geometry that we can associate each point $p \in M^n$ with its **tangent space**
$T_p(M)$, in the following manner. 

Suppose for $\alpha' \in \lambda$ we have that 
$\bm{x}_{\alpha}: U_{\alpha} \to M$ is a mapping whose image contains $p$ (such an $\alpha'$ must exist).
Then $T_p(M)$ has a basis 

\[
\left\{ \frac{\partial}{\partial x_1}, \frac{\partial}{\partial x_2}, \dots, \frac{\partial}{\partial x_n} \right\}
\]

where $\displaystyle \frac{\partial}{\partial x_i}$ is the tangent vector of the map 
$\bm{c}_i: U \to M$, which simply sends $(0, \dots ,0, x_i, 0, \dots, 0)$. 

Now suppose $\phi: M_1^n \to M_2^m$ is a differentiable mapping. Recall 
that the **differential** of $\phi$ establishes a 
linear transformation between the vector spaces: 

\[
d\phi_p: T: M^n_1 \to T_{\phi(p)}M^m_2.
\]

Consider the category $**DMan**^*$
whose objects are pairs $(M^n, p)$ with $M^n$ a differentiable manifold and 
$p \in M^n$. The morphism are 
$(\phi, p): (M_1^n,p) \to (M_2^m, q)$ with $\phi: M_1^n \to M_2^m$ a differentiable 
map and $\phi(p) = q$. 
Then this process may be summarized as a functor 
$T_p: **DMan**_n^* \to \vect_{\rr}$ where 

\begin{gather*}
T:(M, p) = T_p(M)\\
T(\phi: (M_1^n,p) \to (M_2^m, \phi(p)) ) 
= d\phi_{p}: T_p(M) \to T_{\phi(p)}M_2^m
\end{gather*}

One can show that the identity map is sent to the identity linear transformation 
on $T_p(M)$ and that the differential respects composition, so that 
that the association of a manifold $M$ (with a specified point $p \in M$) 
to its tangent space $T_p(M)$ gives rise to a functor

\[
T_p: **DMan**^* \to \vect_{\rr}.
\]

</span>


<span style="display:block" class="example">
Consider again a differentiable manifold $M^n$ of dimension $n$. Recall that 
we may consider the **tangent bundle** $TM$ of $M$, which is the set 

\[
TM = \{(p, v) \mid p \in M^n \text{ and } v \in T_p(M)\}.
\]

The set $TM$ simply pairs each point $p \in M^n$ with its tangent space $T_p(M)$. 
However, $TM$ is more than such a set; it inherits the structure of a differentiable manifold 
from $M$ as well. In fact, it is a manifold of dimension $2n$. 

Now suppose we have a differentiable mapping $\phi: M_1^n \to M_2^m$. Then 
this induces a mapping 

\begin{gather*}
(\phi, d\phi): TM_1^{2n} \to TM_2^{2m}\\
(\phi, d\phi)(p, v) = (\phi(p), d\phi_p(v)).
\end{gather*}

One can show that $(\phi, d\phi): TM_1^{2n} \to TM_2^{2m}$ is a differentiable mapping 
between manifolds\footnote{I wanted to show this here, 
but it turned out to be just tedious definition-checking, so I don't think it's appropriate 
to include here (\textcolor{Red}{perhaps I could make/put it in an appendix...})} 
At this point we may guess that we have a functor 
$TB: **DMan** \to **DMan**$ ("$TB$" for "tangent  bundle") 
where 

\begin{gather*}
TB(M^n) = TM\\
TB(\phi: M_1^n \to M_2^m) = (\phi, d\phi): TM_1^{2n} \to TM_2^{2m}.
\end{gather*}

To check this, we first observe that $TB(1_{M^n}) = 1_{TM^{2n}}$.
Next, suppose $\phi: M_1^n \to M_2^m$ and $\psi: M_2^m \to M_3^p$, 
and observe that 

\[
TB(\psi \circ \phi)
= 
(\psi \circ \phi, d_{\psi \circ \phi})
=
(\psi, d_{\psi}) \circ (\phi, d_{\phi})
=
TB(\psi) \circ TB(\phi).
\]

Note that above in the second step, we used the fact that 
$d_{\psi \circ \phi} = d_{\psi} \circ d_{\phi}$, which we know is true from 
the previous example. As $TB$ respects the identity and composition, we see that we 
do in fact have a functor 

\[
T: **DMan** \to **DMan**  
\]

as desired.
</span>

\vspace{0.5cm}
{\large\noindent **Topology.**\par}


<span style="display:block" class="example">
Let $X$ be a set. Recall that we can turn $X$ into a topological space 
$(X,\tau_d)$, where $\tau^{(X)}_{d}$ is the discrete topology, so that every subset of 
$X$ is an open set. We claim that this process is functorial, so that we 
have a functor

\[
D: \Set \to \top.
\]

This is because any function $f: X \to Y$ extends 
to a continuous function $f: (X, \tau^{(X)}_{D}) \to (Y, \tau^{(Y)}_D)$ 
(hopefully the abuse of notation in $f$ is forgivable here).
Hence this defines a functor, although in a simpler way than we've seen in the 
previous examples. 
</span>


<span style="display:block" class="example">
Let $(X, \tau)$ be a topological space and consider any $x_0 \in X$. 
Then $(X, x_0)$ forms an element of $\top^*$.  With such a space, we can 
consider the **loop space** of $(X, x_0)$ defined to be 

\[
\Omega(X) = \{\phi: S^1 \to X \mid \phi \text{ is continuous and } \phi(0) = x_0\}. 
\]

Here $S^1$ is the circle. 
As this consists of a family of continuous functions between two topological spaces, 
it can be endowed with the Compact Open topology to turn it into a topological space as well.
Hence we claim we have a functor 

\[
\Omega: \top^* \to \top.
\]

To see this, one needs to first consider a morphism in $\top^*$, which 
in this case is continuous function $f: (X, x_0) \to (Y, y_0)$  such that 
$f(x_0 )= y_0$. This must then correspond with a continuous function 
$\Omega(f): \Omega(X) \to \Omega(Y)$. We can define this function 
pointwise: for each continuous $\phi: S^1 \to X$ such that $\phi(0) = x_0$, we have that 
$\Omega(f)(\phi) = f \circ \phi: S_1 \to Y$. In this case we see that $(f \circ \phi)(0) = y_0$, 
and is a continuous function, so it is well-defined. 

This example can be further generalized to higher loop spaces which consider continuous 
functions $\phi: S^n \to X$, rather than just having $n = 1$. 
</span>

\vspace{0.5cm}

{\large\noindent **Algebras, Rings, Groups.**\par}

<span style="display:block" class="example">
Recall that a **Lie Algebra** $\mathfrak{g}$ is a vector space 
$\mathfrak{g}$ (over a field $k$), equipped with a bilinear operation 
$[-, -]: \mathfrak{g}\times \mathfrak{g} \to \mathfrak{g}$
such that 

* [1.] $[x, y] = -[y, x]$


* [2.] $[x, [y, z]] + [y, [z, x]] + [z, [x,y]] = 0$. 



Condition (2) is referred to as the **Jacobi identity**, and many 
familiar operations on vector spaces satisfy (1) and (2). For example, the cross 
product on vector spaces in $\rr^3$ satisfy these properties. 

Consider an associative algebra $A$ over a field $k$ with (associative); recall 
that this too has a bilinear operation $\cdot: A \times A \to A$ with unit $e \in A$. 
Then we can use $A$ to create a Lie algebra $L(A)$, whose (1) underlying vector 
space is $A$ and (2) whose bilinear operation is $[a, b] = a \cdot b - b\cdot a$. 

Now suppose $\phi: A \to A'$ is a morphism of algebras. Then we can associate 
both $A, A'$ with their Lie algebras $L(A), L(A')$. Further, we can construct a Lie 
Algebra morphism $L(\phi): L(A) \to L(A')$, using $\phi$, by setting 
$L(\phi)(a) = \phi(a)$. This is a morphism of Lie algebras since 

\[
[\phi(a), \phi(b)] = \phi(a)\phi(b) - \phi(b)\phi(a) = \phi(ab - ba) = \phi([a, b]).
\]

One can then check that $L(1_A) = 1_{L(A)}$ and $L(\phi \circ \psi) = L(\phi)\circ L(\psi)$, so 
that what we have is a functor 

\[
L: **Alg** \to **LieAlg**            
\]

which associates each associative algebra with its Lie algebra structure.
</span>


<span style="display:block" class="example">
Let $R$ be a commutative ring. Recall that
$\spec(R)$ is the set of all prime ideals of $R$. In addition, recall
that if $\phi: R \to S$ is a ring homomorphism and  
if $P$ is a prime ideal of $S$, then $\phi^{-1}(P)$ is also a prime 
ideal in $R$.
This then allows us to define a functor 

\[
**Spec**: \ring \to \Set
\]

where on objects $R \mapsto \spec(R)$ and on morphisms 
$\phi: R \to S \mapsto \phi^*: \spec(S) \to \spec(R)$ where 
$\phi^{*}(P) = \phi^{-1}(P)$.

However, we can go even deeper than this. Recall from algebraic 
geometry that $\spec(R)$ can be turned into a topological space, 
using the Zariski topology. However, because 
$\phi^{-1}(P)$ is a prime ideal whenever $P$ is, we see that $\phi^*: 
\spec(S) \to \spec(R)$ is actually a continuous function between 
the topological spaces. Hence we can view this 
as a functor 

\[
**Spec**: \ring \to \top.
\]

Usually this is phrased more naturally as a functor 
$**Spec**: \ring \to **Sch**$
where $**Sch**$ is the category of schemes; this is simply 
because schemes are isomorphic to $\spec(R)$ for some $R$.
</span>


<span style="display:block" class="example">
Let $G$ be a group, and $R$ be a ring with identity. Recall 
from ring theory that we can form the **group ring**

\[
R[G] = \left\{ \sum_{g \in G}a_gg\mid a_g \in R, \text{ all but finitely many } a_g = 0 \right\}.
\]

Thus the elements are finite sums, but we have possibly infinitely many ways 
of adding them. Now 
for two elements $\displaystyle \alpha = \sum_{g \in G}a_kg$ and 
$\displaystyle \beta = \sum_{g \in G}b_gg$, we define ring addition and multiplication 
as 

\[
\alpha + \beta = \sum_{g \in G}(a_k + b_k)g
\qquad 
\alpha \cdot \beta 
= 
\sum_{g \in G}\sum_{g_1 \cdot g_2 = g}(a_{g_1}b_{g_2})g.
\]

Now suppose $\phi: G \to H$ is any group homomorphism.
With that said, we claim that $\phi$ induces a
natural ring homomorphism $\phi^{*}: R[G] \to R[H]$
between the group rings, where 

\[
\sum_{g\in G}a_gg \mapsto \sum_{g \in G}a_g \phi(g). 
\]

Clearly this is linear and preserves scaling; less obvious is if 
this behaves on multiplication, although we check that below.
If $\alpha, \beta$ defined as above then 

\[
\phi^*( \alpha \cdot \beta )
=
\phi^*\left( \sum_{g \in G}\sum_{g_1 \cdot g_2 = g}(a_{g_1}b_{g_2})g \right)
=
\sum_{g \in G}\sum_{g_1 \cdot g_2 = g}(a_{g_1}b_{g_2})\phi(g)
=
\sum_{g \in G}a_g\phi(g)\cdot
\sum_{g \in G}b_g\phi(g)
=
\phi^*(\alpha)\cdot\phi^*(\beta).
\]

Hence we see that $\phi^*$ is a ring homomorphism. Therefore, 
what we have on our hands is a functor 

\[
R[-]: \grp \to \ring  
\]

Possibly, your brain may wonder: it looks like we have an assignment 
of rings to *functors*. 

\[
R \mapsto R[-]: \grp \to \ring.
\]

Perhaps this process is functorial? The answer is yes, although 
at the moment we don't have the necessary language to describe it; 
we will go over this when we introduce *functor categories*.
</span>
\vspace{0.5cm}

{\large\noindent **Set Theory**\par}

<span style="display:block" class="example">
Consider the power set $\mathcal{P}(X)$ on a set $X$.
Then we can create a functor $\mathcal{P}: \Set \to
\Set$ as follows. 

Observe that for any set $X$, $\mathcal{P}(X)$ is of course
another set. Therefore objects of $\Set$ are sent to
$\Set$, as we claim. 

Now let $f: X \to Y$ be a function between two sets $X$ and
$Y$. Then we define $\mathcal{P}(f) : \mathcal{P}(X) \to
\mathcal{P}(Y)$ to be the function where 

\[
P(f)(S) = \{f(x) \mid x \in S\}.
\]

which is clearly in $\mathcal{P}(Y)$.
Now we must show that this function
respects identity and composition properties.
\begin{description}
\item[Identity.] Consider the identity function 
$\id_X: X \to X$ on a set $X$. 
Then observe that for any $S \in \mathcal{P}X$, we have that  

\[
\mathcal{P}(\id_X)(S) 
=
\{\id_X(x) \mid x \in X\} = S.
\]

Therefore, $\mathcal{P}(\id_X) = 1_{\mathcal{P}X}$ so
that $\mathcal{P}$ respects identities. 

\item[Composition.] Let $X, Y, Z$ be sets and $f: X \to Y$
and $g: Y \to Z$ be functions. Let $S \in \mathcal{P}(X)$.
Observe that 

\begin{align*}
\mathcal{P}(g \circ f)(S) 
&= \{(g \circ f)(x) \mid x \in S \}\\
&= \{ g(f(x)) \mid x \in S \}\\
&= \{ g(y) \mid y = f(x) \text{ and } x \in S\}
&= \mathcal{P}(g)(\{f(x) \mid x \in S\})\\
&= \mathcal{P}(g)( \mathcal{P}(f)(S))\\
&= (\mathcal{P}(g) \circ \mathcal{P}(f)) (S).
\end{align*}

Therefore we see that $\mathcal{P}(g \circ f) =
\mathcal{P}(g) \circ \mathcal{P}(f),$ so that
$\mathcal{P}$ describes a functor from $\Set$ to $\Set$.
\end{description}
</span>

As we just encountered a mass of different examples of functors from 
different fields, one might wonder: are there other mathematical constructions 
which simply do not behave exactly as a functor? The answer is yes, although 
finding these examples is a bit tricky. The following is a well-known 
example, while the one after is one I haven't seen presented elsewhere.
\vspace{0.5cm}

{\large\noindent **Non-functor Examples.**\par}


<span style="display:block" class="example">
Recall from group theory that, with every group $G$, 
there is an associated subgroup of $G$ called the center:

\[
Z(G) = \{ z \in G \mid zg = gz \text{ for all } g \in G\}.
\]

By definition, $Z(G)$ is an abelian group. As every group $G$ may be 
associated with an abelian group $Z(G)$, one might expect that this 
process is functorial. One might prematurely denote this as

\[
Z: \grp \to \ab.
\]

However, this is not a functor, as an issue arises with the morphisms. 
Consider a group homomorphism $\phi: G \to H$. Then for this to be a functor, 
we'd naturally desire a group homomorphism $Z(\phi): Z(G) \to Z(H)$ between 
the abelian groups. The only issue is that there is no consistent way to 
define such a morphism from $\phi$. The most natural way we would attempt  
to achieve this is by considering the restriction, but in general 
$\phi\big|_{Z(G)}: G \to H$ does not map into $Z(H)$. 
For example, consider the **Heisenberg Group**

\[
H_3(R)
= 
\left\{
\begin{pmatrix}
1 & a & b\\
0 & 1 & c\\
0 & 0 & 1 
\end{pmatrix}
\Bigg|
a,b,c \in R
\right\}
\]

where $R$ is a commutative ring with identity. Observe that 
we can create an inclusion group homomorphism $i: H_3(R) \to \text{GL}_3(R)$. 
One can show that 

\[
Z(H_3(R)) = 
\left\{
\begin{pmatrix}
1 & 0 & a\\
0 & 1 & 0\\
0 & 0 & 1 
\end{pmatrix}
\Bigg|
a \in R
\right\}
\qquad 
Z(\text{GL}_3(R))
=
\left\{  
\begin{pmatrix}
a & 0 & 0\\
0 & a & 0\\
0 & 0 & a 
\end{pmatrix}
\Bigg|
a \in R 
\right\}.
\]

Hence restricting the inclusion $i: H_3(R) \to \text{GL}_3(R)$ 
to $Z(H_3(R))$ results in a group homomorphism that 
does not even hit $Z(\text{GL}_3(R))$ (except of course when $a = 0$). 
Thus there is not a general way to relate these two quantities in a functorial 
fashion.
</span>

What follows is a second example in which a process which may appear to be 
functorial does not turn out to be. It can, however, be adjusted to 
become a functor. 


<span style="display:block" class="example">
Let $X$ be a set. Recall from topology that we can treat $X$ as a
topological space by associating to it the \textbf{finite complement 
topology:} 

\[
\tau^X_{FC}= \{U \subset X \mid X - U \text{ is finite.}\}
\]

With that said, one may suppose that we have a functor $\text{FinC}: \Set \to 
\top$ where $X \mapsto (X, \tau^X_{FC})$. This would require that
each function $f:X \to Y$ 
extends to a continuous function $f: (X, \tau_{FC}^X) \to (Y, \tau_{FC}^Y)$. 
However, for such a function to be continuous we would need that 

\[
\text{if } Y - V \text{ is finite then } X - f^{-1}(V) \text{ is finite.}
\]

In general, this is not true. For example suppose $X$ is infinite and $Y$ is finite. 
Then $Y - \varnothing$ is finite, but $X - f^{-1}(\varnothing) = X$ is infinite. 
Hence this cannot define a functor $F: \Set \to \top$. 

</span>


{\large **Exercises**
\vspace{0.5cm}}

* [**1.**] 
\begin{itemize}


* [(*i*.)]
Let $X$ and $Y$ be two sets. Regard each set as a discrete category. 
Interpret what a functor $F: X \to Y$ means in this case.


* [(*ii*.)] 
Let $G$ and $H$ be two groups. Regard each group as a one-object 
category whose morphisms sets correspond to their group elements, with composition 
their group product.
Interpret what a functor $F: G \to H$ means in this case.


* [(*iii*.)] 
Let $X$ and $Y$ be a pair of thin categories. Interpret 
what a functor $F: X \to Y$ means in this case. (Use (*i*) 
to get you started.) 



\vspace{0.2cm}

\item[**2.**]
Let $G$ be a group. Then for any two elements $a, b \in G$, we
define the **commutator** of $a, b$ to be the element 

\[
aba^{-1}b^{-1}.
\]

Define $[G, G]$ to be the set 

\[
\{x_1x_2\cdots x_n \mid n \in \mathbb{N}, x_i \text{ is a commutator in } G\}    
\]

which we call the **commutator subgroup**. Its underlying set
consists of all possible products, with factors that are
of the form $a_ib_ia_i^{-1}b_i^{-1}$. 
One can show that $[G, G] \normal G$ for any group $G$,
which implies that we may discuss the quotient group $G/[G, G]$,
which is abelian in this case. 

So, show that we have a functor $F: \grp \to \ab$ 
where 

\[
F(G) = G/[G,G] 
\]

Deduce the action of $F$ on the morphism of $\grp$ 
(i.e., the group homomorphisms.) and show that it is well-defined.
\vspace{0.2cm}

\item[**3.**]
Let $R$ be a unital ring. Recall that $GL_n(R)$ is the group consisting of 
$n \times n$ matrices with entries in $K$. Show that this construction more 
generally is that of a functor

\[
**GL**_n: \ring \to \grp.
\]

In addition, with such a ring $R$, we may associate it with 
its group of units $R^{\times}$, which you may recall is 

\[
R^{\times} =\{ u \in R \mid ur = ru = 1 \text{ for some } r\in R\}.
\]

Show that this also defines a functor 

\[
(-)^{\times}: \ring \to \grp.
\]

We will see in the next section that there is an interesting 
relationship between these two functors.


\item[**4.**] Recall the category $\Set_{FTO}$ 
is the category whose objects are sets and whose morphisms are functions 
with the finite-to-one property (See Exercise 1.3.3). While we saw 
that $\text{FinC}: \Set \to \top$ where 

\[
X \mapsto (X, \tau^X_{FC})
\]

does **not** define a functor, show that upon changing the domain  
category from $\Set$ to $\Set_{FTO}$, it **does** 
define a functor $\text{FinC}: \Set_{FTO} \to \top$.
\vspace{0.2cm}

\item[**5.**]

* [(*i*.)]
Let $X = \{x_1, x_2, \dots, x_n\}$ be a finite set. With such 
a finite set, we can
pick a field $k$ and build $X$ into a finite-dimensional 
vector space $V_X$ over $k$. Explicitly, we can create the vector  
space

\[
V_X= \{c_1x_1 + \cdots + c_nx_n \mid c_i \in k\}.
\]

We define addition in the intuitive way of adding coefficients of the 
same basis, so this is truly a vector space. Note that when $k = \rr$, 
we get that $V_X \cong \rr^n$. 

Prove that this process is functorial. That is, show that the functor 

\[
F: \finset \to \vect_k \qquad F(X) = V_X
\]

is a functor. 



* [(*ii*).]
From any set $X$, we may construct the **free group** $F(X)$ generated 
by $X$. The elements of $F(X)$ are (1) the elements of $X$, (2) a new 
element $e$, and (3) all elements $xy$ whenever $x, y \in X$. 
In this way, $F(X)$ is a group with the product being string concatenation, 
and we require that $xe = x = ex$. 
. Below, two words (elements of $F(X)$) are combined.        

\[
(x^2yz^{-1}) \cdot (zy^2x) = x^2y^2x.
\]

Show that we have a functor $F: \Set \to \grp$ where 
sets are mapped to their free groups, that is, $X \mapsto F(X)$.  



* [(*iii*).]
For any set $X$, we can build the **free ring** $(R\{X\}, +, \cdot)$ 
as follows. Let $(F(X), \cdot)$ be the free group with the added relation that 
$xy = yx$ for any $x, y  \in F(X)$. We can then define

\[
R\{X\} = \left\{ \sum_{x_i \in F(X)} x_i^{n_i} \mid \right\}
\]







**Note:** This example becomes particularly important later. 
It can also be generalized to functors $F:  \Set \to \mon$, 
$F: \Set \to \ring$, and other algebraic systems, 
since sets can also be turned into free monoids, free rings, or other 
free "objects."
\vspace{0.2cm}

\item[**6.**]
Let $V$ be a vector space over a field $k$. 
Recall that we can associate $V$ with its 
**projective space** $P(V)$ which is defined as the set of equivalence 
classes of element in $V$, subject to the relation $v \sim w$ if $v = \lambda w$ 
for some nonzero $\lambda \in k$. That is,

\[
P(V) =  \Big\{[v] \mid v \in V \Big\}
\]

where $[v]$ denotes the equivalence class of $v$. Show that this process 
is functorial, so that we have a functor 

\[
P: \vect_k \to \Set.
\]


\item[**7.**]
Let $R$ be a ring with ideal $I$. Recall that we can construct the 
**radical of the ideal $I$** as the ideal 

\[
\sqrt{I} = \{r \in R \mid r^n \in I \text{ for some } n \ge 1  \}.
\]

Show that we have a functor 

\[
\sqrt{-}: **Ideals**(R) \to **Ideals**(R)    
\]

where $**Ideals**(R)$ is the partial order of ideals on $R$, 
whose ordering is given by subset containment. 

\item[**8.**] 
Let $X$ be a topological space, and denote $\open(X)$ as the category 
where the objects are open sets $U \subset X$ and morphisms are inclusion morphisms. 
Create a functor 

\[
F: \open(X) \to \Set  
\]

where on objects $F(U) = \{f: U \to \rr \mid f \text{ is continuous}\}$. That is, how 
should $F$ act on the morphisms for this to be a functor?

\item[**9.**] 
Let $k$ be a field. With each field, we may associate $k$ with the category 
$\vect_k$ which consists of finite dimensional vector spaces $V$ 
over $k$. Is this process functorial? That is, do we have a functor 

\[
\vect: \fld \to \cat 
\]

where $\vect(k) = \vect_k$?\\
*Hint: No. But explain why it breaks.*
\end{itemize}



