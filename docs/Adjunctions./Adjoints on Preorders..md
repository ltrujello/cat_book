#4.4. Adjoints on Preorders.

Interesting things happen when one applies adjoint concepts to
functors between preorders; ones which preserve order in a special
way. It's actually often the case where we have two mathematical
structures involving chains of arrows which reverse when
transferring between one and the other. We give such a concept a
definition first, before introducing a theorem about such structures. 


<span style="display:block" class="definition">
Let $\pp$ and $\qqq$ be two preorders. If there exists functors 
$F: \pp \to \qqq$ and $G:\qqq \to \pp$ such that 

\[
F(P) \le Q \iff P \le G(Q),  
\]

That is, there exists $f:F(P) \to Q$ if and only if there
exists $g: P \to G(Q)$, then $F$ and $G$ are called a
**monotone Galois connection**. On the other hand, 
if we have that 

\[
F(P) \le Q \iff P \ge G(Q)
\]

then $F$ and $G$ are called a \textbf{antitone Galois
connection}. 
</span>

\begin{thm}
Let $\mathcal{P}, \mathcal{Q}$ be two preorders, and suppose
$F: \mathcal{P} \to \mathcal{Q}\op$ and
$G:\mathcal{Q}\op \to \mathcal{P}$ are two order preserving 
functors. Then $F$ is
left adjoint to $G$ if and only if for all $P \in \mathcal{P}$
and $Q \in \mathcal{Q}$ 

\[
F(P) \ge Q \iff P \le G(Q).
\]

Given such an adjunction, we then have that our unit
establishes $P \le G(F(P))$ and the counit establishes $F(G(Q)) \le
Q$. 
\end{thm}


<span style="display:block" class="proof">
Observe that if $F$ is left adjoint to $G$, then we have the 
bijection 

\[
\hom_{\mathcal{Q}\op}(F(P), Q) \cong \hom_{\mathcal{P}}(P, G(Q)
)
\]

which gives rise to the desired correspondence; on the other
hand, such a bijection gives rise to an adjunction. 
With such an adjunction, we know that for each $P, Q$, there
exist morphisms $\eta_P: P \to G(F(P))$ and $\epsilon_Q:
F(G(Q)) \to Q$. Hence $P \le G(F(P))$  and $F(G(Q)) \ge Q$. 
</span>

The above theorem came out of the observation that there is a
connection between fields, their subfields, and their groups of
automorphisms, an observation which arises in Galois Theory.
The goal of Galois Theory is to understand polynomials and their
roots; when they can be factorized, when and where we can find
their roots. The study of Galois groups is now used widely in
number theory. For example, part of Andrew Wiles' work in proving
Fermat's Last Theorem involved Galois representations.


It was this theorem, rooted in Galois Theory, that motivated the
Theorem 4.\ref{galois_connections} at the beginning of this
section. 
The Fundamental Theorem
of Galois Theory is simply a *stronger*, special case, since in
this case, the functors are literally inverses of each other. The
theorem we introduced, however, simply requires the functors to be
adjoints of one another. 


<span style="display:block" class="example">
Let $U, V$ be sets, and observe that their power sets $\mathcal{P}
(U)$ and $\mathcal{P}(V)$ form categories; specifically,
preorders, ordered by set inclusion. 

Suppose $f: U \to V$ is a function in **Set**. Then $f$
induces a functor $f_*: \mathcal{P}(U) \to \mathcal{P}(V)$,
where 

\[
f_*(X) = \{f(x) \mid x \in X\}.
\]

Note that if $X\subset X'$, then $f_*(X) \subset f_*(X')$.
Hence this is an order-preserving functor. Now observe that
$f$ also induces a functor $f^*:
\mathcal{P}(V) \to \mathcal{P}(U)$ where 

\[
f^*(Y) = \{x \mid f(x) \in Y\}.
\]

Note that this also preserves order. In addition, we have that if 
$f_*(X) \le Y$, then this holds if  and only if $f(X) \subset
Y$. We then have that this holds if and only if $X \subset
f_*(Y)$, Hence we have a Galois connection, so that we may apply 
Theorem 4.\ref{galois_connections} to conclude that $f_*$ is
left adjoint to $f^*$.  
</span>










