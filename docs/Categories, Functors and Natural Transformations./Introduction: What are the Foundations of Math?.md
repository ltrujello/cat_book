#1.1. Introduction: What are the Foundations of Math?

Category theory attempts to "zoom out" of mathematical constructions
and to point out the higher level relationships between different mathematical
constructions. The three main concepts are categories, functors, and
natural transformations, although the theory grew out of
implications of these main concepts. 


These main concepts were first seen in the study of algebraic
topology, since 
it was observed that topological problems could be reduced to
algebraic, and vice versa. But how? Since there was no formal
notion for what it really meant to take a topological space $X$
and associate it with some group $\pi(X)$, 
category theory came about to formalize this. 

However, as we shall soon see, category theory has a big problem. 
Specifically, there isn't a universally agreed upon foundation for
category theory, or for mathematics in general. 
\begin{center}
**What do we mean by foundations?**
\end{center}    Well, consider a topological space $X$, or a group $G$, or a
domain $\mathbb{R}$. Then suppose I ask you
"What is $X$?" or "What is $G$" or "What is $\mathbb{R}$?" 
Well, you'll tell me it's a topological space, a
group, or the set of real numbers and
list the axioms for each object. 

That is, a correct answer will characterize $X$, $G$ or $\mathbb{R}$ as a
set which satisfies 
some axioms. But really, that's what all our mathematical objects
are. So at this point, our foundations \textbf{are grounded in set
theory.}

\\begin{center}
**What is set theory?**
\end{center}   Suppose I ask you what is set theory. While we all know there are 
different set theories, most people don't think about set theory axioms on a daily 
and won't know (like myself). But answering
this question requires answering the next. 

\\begin{center}
**What is a set?**
\end{center}   We usually never have to face this question. But in developing a
theory that considers relationships between different sets, we
have to. 

Our intuition tells us that sets $X$ are a \textbf{collection of
objects, and that every collection of objects is a set}. We
intuitively *think* that  
we can form collections of objects to create a set $X$, and that
we can form 
intersection and unions between sets, or even compute power
sets, to produce other sets. We also *think* we can also form sets such as 

\[
X = \{x \mid \phi(x) \}
\]

where $\phi$ is some logical condition of inclusion. However, this
leads to paradoxes, one of the most famous known as Russel's
Paradox which we can describe as follows. 

\noindent**Russel's Paradox.**
Let $X$ be a set such that 

\[
X = \{A \text{ is a set }\mid A \text{ is not a member of itself.}\}
\]


Now observe the following. 

* [1.] If $X \in X$, then consequently $X$ is not a member
of itself. In other words, if $X \in X$, then $X \not\in X$.

Clearly, this is a contradiction. Since $X \in X$ is nonsense,
$X \not\in X$, right? 



* [2.] Suppose $X \not\in X$. Then $X$ is not a member of
itself, so $X \in X$ by the condition of member of $X$. In
other words, $X \not\in X \implies X \in X$.



See the problem here? \textbf{Not every collection of objects is a
set.} So our previous notions of sets aren't correct.

\textcolor{MidnightBlue}{Note that our trouble arose when we said
that \textbf{a set is a collection of objects, and a collection of
objects is a set.} 
This is because no, not every collection of objects is a set.
Thus we need to go back and fix our definition of a set.
}

\\begin{center}
**What do we do?**
\end{center}   This is what many mathematicians asked in the early 1900s
when they identified the paradoxes that arise from our notion of
a set. The result has been multiple different types of set theories, 
and so there isn't a clear 
choice on what to make our foundations. However, this isn't a huge problem 
for category theory. Category theory 
has its own core axioms, but the fact that there are different set theories 
simply means that such core axioms will be phrased differently under different 
set theories (although there are some cases where 
one does need to be careful with their foundations).
In this text, we'll be a bit sloppy with the foundations of category theory, 
although  we will point out where we need to be careful.




