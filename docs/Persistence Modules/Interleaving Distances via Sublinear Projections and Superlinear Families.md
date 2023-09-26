#11.3. Interleaving Distances via Sublinear Projections and Superlinear Families

<span style="display:block" class="definition">
A **sublinear projection** is a function $\omega: **Trans**_P \to [0, \infty]$
which acts on the objects of $**Trans**_P$ in such a way that 
$\omega_I = 0$ and $\omega_{\Gamma_1\Gamma_2} \le \omega_{\Gamma_1} + \omega{\Gamma_2}$. 

Moreover, we say a sublinear projection is **monotone** if whenever 
$\Gamma \le K$ we have that $\omega_{\Gamma} \le \omega_{K}$. 
</span>

Note that we can turn a sublinear projection $\omega$ into a monotone one by defining

\[
\overline{\omega}_\Gamma = \inf\{\omega_{\Gamma'} \mid \Gamma' \ge \Gamma \}.
\]

This is monotone since, if $\Gamma \le K$ is a pair of translations, then 
one can observe that 

\[
\{ \omega_{\Gamma'} \mid \Gamma' \ge \Gamma \} \supset \{ \omega_{\Gamma'} \mid \Gamma' \ge K \}
\implies  
\overline{\omega}_{\Gamma} \le \overline{\omega}_{K}.
\]

Also note another nice property: for every sublinear projection $\omega$, it is always 
the case that $\overline{\omega}_{\Gamma} \le \omega_{\Gamma}$ for any translation $\Gamma$. 


<span style="display:block" class="definition">
Suppose $F, G$ are interleaved by a pair of translations $(\Gamma, K)$. Then 
we say $F, G$ are $\bm{\epsilon}$**-interleaved** with respect to $\omega$ if 

\[
\omega_\Gamma, \omega_K \le \epsilon.
\]

</span>

Now we prove a small lemma. 

<span style="display:block" class="lemma">
Let $\omega$ be a sublinear projection on a preorder $P$, and 
let $\Gamma$ be a translation of $P$. Then for every $\eta > 0$, there 
exists a translation $\Gamma' \ge \Gamma$ such that 

\[
\omega_{\Gamma'} \le \overline{\omega}_\Gamma + \eta.
\]

</span>


<span style="display:block" class="proof">
Suppose the statement was false. Then this would imply the existence of some 
$\eta> 0$ with the property that 

\[
\overline{\omega}_{\Gamma} + \eta < \omega_{\Gamma'}
\]

for all $\Gamma' \ge \Gamma$. Hence we would see that 

\[
\overline{\omega}_{\Gamma} \ne \inf\{\omega_{\Gamma'} \mid \Gamma'\ge\Gamma \}
\]

which is a contradiction.
</span>

With the definition of a sublinear projection, we can now create a (psuedo)metric between 
persistence modules.

<span style="display:block" class="definition">
Let $F, G \in \dd^{P}$, and suppose $\omega$ is a sublinear projection. 
Then their interleaving distance is given by 
\begin{statement}{NavyBlue!10}
\begin{align_topbot}
d^{\omega}(F, G) 
&= \{ \epsilon \in [0, \infty) \mid F, G \text{ are } \epsilon \text{-interleaved w.r.t. } \omega  \}\\
&= \{ \epsilon \in [0, \infty) \mid F, G \text{ are } (\Gamma, K)\text{-interleaved and } \omega_\Gamma, \omega_K \le \epsilon\}.
\end{align_topbot}
\end{statement}
</span>


<span style="display:block" class="proposition">
Let $\omega$ be a sublinear projection. Then $d^{\omega}= d^{\overline{\omega}}$.
</span>


<span style="display:block" class="proof">
We will prove this by first showing that $d^{\omega} \ge d^{\overline{\omega}}$,
and then demonstrating that $d^{\omega} - d^{\overline{\omega}} = 0$.
\begin{description}
\item[$\bm{d^{\omega} \ge d^{\overline{\omega}}}$]
If a pair of persistence modules $F, G$ are $\epsilon$-interleaved by $(\Gamma, K)$ with respect to $\omega$,
then we can observe that 

\[
\overline{\omega}_\Gamma  \le \omega_\Gamma \le \epsilon \qquad \overline{\omega}_K \le \omega_K \le \epsilon
\]

so that $F, G$ are also $\epsilon$-interleaved by $(\Gamma, K)$ with respect to $\overline{\omega}$.
Therefore,

\begin{align*}
\{ \epsilon \in [0, \infty) \mid F, G \text{ are } \epsilon \text{-interleaved w.r.t. } \omega  \}
\subset 
\{ \epsilon \in [0, \infty) \mid F, G \text{ are } \epsilon \text{-interleaved w.r.t. } \overline{\omega}  \}.
\end{align*}

If we take the infimum of the above relation, we get that $d^{\overline{\omega}} \le d^{\omega}$. \\

\item[$\bm{d^{\omega} - d^{\overline{\omega}}} = 0$.]
Let $\delta> 0$. We'll show that for any persistence modules $F,G$ that

\[  
d^\omega(F,G) - d^{\overline{\omega}}(F,G) \le \delta
\]

which, in combination of the fact that $d^{\overline{\omega}} \le d^{\omega}$,
will then give us our result. 







Towards this goal, let $\Gamma, K$ 
be an interleaving of $F, G$ such that 

\[
\overline{\omega}_{\Gamma}, \overline{\omega}_{K} \le d^{\overline{\omega}}(F, G) + \delta.
\]

Such an interleaving must exist or else $d^{\overline{\omega}}(F, G)$ 
is larger than we thought. 
By the lemma we proved earlier, we know that there exist 
translations $\Gamma', K'$ such that 

\[
\Gamma \le \Gamma' \qquad K \le K'
\]

and 

\begin{align*}
\omega_{\Gamma'} \le \overline{\omega}_{\Gamma} \le d^{\omega}(F, G) + \delta
\qquad \omega_{K'} \le \overline{\omega}_{K} \le d^{\omega}(F, G) + \delta.
\end{align*}

Note that by Monotonocity of interleavings, since $F, G$ are interleaved 
by $(\Gamma, K)$, we know that $F, G$ are interleaved by 
$(\Gamma', K')$. Therefore, we can conclude that since $\omega_{\Gamma'}, \omega_{K'} \le d^{\overline{\omega}} + \delta$, we see that 

\begin{align*}
d^{\omega}(F, G) \le  d^{\overline{\omega}}(F,G) + \delta \implies d^{\omega}(F, G) - d^{\overline{\omega}}(F,G) \le \delta.
\end{align*}

Since $\delta > 0$ was arbitrary, and because $d^{\omega} \ge d^{\overline{\omega}}$ 
we have that they must be equal, as desired. 
\end{description}
</span>

We now introduce an important implication of these results. 


<span style="display:block" class="theorem">
For any sublinear translation $\omega: **Trans**_P \to [0, \infty]$, 
The interleaving distance $d = d^\omega$ becomes an extended psuedometric
on $\dd^P$. 
</span>


<span style="display:block" class="proof">
To show this, we must show that $d(F, F) = 0$ for any persistence 
module $F$, $d$ is symmetric, and that $d$ obeys the triangle inequality. 
\begin{description}
\item[$\bm{d(F, F) = 0}$]
Observe that $d(F, F) = 0$. This is because if we denote $I: P \to P$ to be the identity
translation on $P$, then 
$F$ is $(I, I)$ interleaved with itself. But recall that $\omega_I = 0$. 

\item[$\bm{d(F, G) = d(G,F)}$]
Now observe that $d(F, G) = d(G, F)$. This is because of the inherent
symmetry present in the definition of an interleaving, which allows us to 
swap $F$ and $G$. 

\item[Triangle Inequality]
Finally, we show that $d$ obeys the triangle inequality. Consider a triple of 
persistence modules $F, G, H$. Suppose $F, G$ are $\epsilon$ interleaved, 
while $G, H$ are $\epsilon'$ interleaved. Regardless of whether or not 
$\epsilon \le \epsilon'$ or vice versa, we know that there exist translations 
$\epsilon$-translations $(\Gamma, K)$ which interleaved $F, G$ and $\epsilon'$-translations 
$(\Gamma', K')$ which interleave $G,H$. By the triangle inequality of translations, 
we know that this implies that $F, H$ are $(\Gamma'\circ \Gamma, K \circ K')$-interleaved 

Note that by sublinearity we have that 

\begin{align*}
\omega_{\Gamma'\Gamma} &\le \omega_{\Gamma'} + \omega_{\Gamma} \le \epsilon' + \epsilon\\
\omega_{KK'} &\le \omega_{K} + \omega_{K'} \le \epsilon + \epsilon'
\end{align*}

Therefore, we see that 

\[
d(F, H) \le \epsilon' + \epsilon.
\]

Taking the infimum over $\epsilon', \epsilon$, we get that 

\[
d(F,H) \le d(F,G) + d(G, H)
\]

as desired.
\end{description}
</span>

We'll now show that this isn't the only way to invent a metric for persistence modules 
in their functor category.


<span style="display:block" class="definition">
Let $P$ be a preorder. A **superlinear family** $\Omega: [0, \infty) \to **Trans**_P$ 
is a function where 

\[
\epsilon \mapsto \Omega_\epsilon \in **Trans**_P  
\]

such that $\Omega_{\epsilon_1}\Omega_{\epsilon_2} \le \Omega_{\epsilon_1 + \epsilon_2}$. 
</span>

Note that in $**Trans**_P$, the identity $I: P \to P$ is an initial object. 
So if $\epsilon_1 \le \epsilon_2$, we know that 

\[
I \le \Omega_{\epsilon_2 - \epsilon_1}.   
\]

Appending $\Omega_{\epsilon_1}$ on the right, we get that 

\[
I\Omega_{\epsilon_1} \le \Omega_{\epsilon_2 - \epsilon_1}.
\]

Using the fact that $\Omega_{\epsilon_1}\Omega_{\epsilon_2} \le \Omega_{\epsilon_1 + \epsilon_2}$, 
we see that 

\[
I\Omega_{\epsilon_1} \le \Omega_{\epsilon_2 - \epsilon_1} \le \Omega_{\epsilon_2}.
\]

Since $I$ is the identity, we know that $I\Omega_{\epsilon_1} = \Omega_1$. We thus have that 

\[
\Omega_{\epsilon_1} \le \Omega_{\epsilon_2}
\]

so that **superlinear families are monotonic**.

Now, how does this turn into a metric? 


<span style="display:block" class="definition">
Let $P$ be a preorder and $\dd$ a category. Then for $F,G \in \dd^P$, 
we define their **interleaving distance** 

\[
d^{\Omega}(F,G)
= \inf \{ \epsilon \in [0, \infty) \mid F, G \text{ are } \Omega_\epsilon\text{-interleaved} \}.
\]

If the above set is empty, we set $d^{\Omega}(F,G) = \infty$. 
</span>


<span style="display:block" class="theorem">
The interleaving distance $d^{\Omega}$ is an extended pseudometric.
</span>


<span style="display:block" class="proof">
To show this, we need to prove that for persistence modules $F, G$, 
$d(F, F) = 0$, $d(F, G) = d(G, F) = 0$, and that the metric satisfies the triangle 
inequality. 
\begin{description}
\item[$\bm{d(F, F) = 0}$.]
Observe that the functors  $F, F$ are $(I, I)$-interleaved. Given that $I \le \Omega_0$ 
since it is initial, we see that $d(F,  F) = 0$. 

\item[$\bm{d(F, G) = d(G, F)}$.] Observe that the definition is purely symmetric 
so that this result is instant. 

\item[Triangle inequality.]
Let $F, G, H$ be persistence modules and suppose $F, G$ are $\Omega_{\epsilon_1}$-interleaved 
while $G, H$ are $\Omega_{\epsilon_2}$-interleaved. Then by the triangle property of 
translations, we know that $F, H$ are  $(\Omega_{\epsilon_2}\Omega_{\epsilon_1}, \Omega_{\epsilon_1}\Omega_{\epsilon_2})$-interleaved. 

Observe that 

\begin{align*}
&\Omega_{\epsilon_2}\Omega_{\epsilon_1} \le \Omega_{\epsilon_1 + \epsilon_2}\\
&\Omega_{\epsilon_1}\Omega_{\epsilon_2} \le \Omega_{\epsilon_1 + \epsilon_2}.
\end{align*}

By monotonicty of translations, this implies that $F, H$ are $\Omega_{\epsilon_1 + \epsilon_2}$-interleaved, 
so that 

\[
d^{\Omega}(F, H) \le \epsilon_1 + \epsilon_2.
\]

Taking the infimum over $\epsilon_1, \epsilon_2$, we get that 

\[
d^{\Omega}(F, H) \le d^{\Omega}(F, G) + d^{\Omega}(G, H)
\]

as desired. 
\end{description}
</span>



