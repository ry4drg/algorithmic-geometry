# Discrepancy of the Complete Set System

Recall that the discrepancy of a set system \(\mathcal{F}\) on a ground set \(X\) is defined by

$$
\operatorname{disc}(\mathcal{F})
=
\min_{\chi \colon X \to \{\pm 1\}}
\max_{S \in \mathcal{F}}
\left| \sum_{x \in S} \chi(x) \right|,
$$

where the minimum is taken over all two-colorings of \(X\), and the maximum over all sets in the system.

We prove the two requisite inequalities separately.

## Lower bound

Fix an arbitrary coloring \(\chi \colon X \to \{\pm 1\}\), and put

$$
P = \{x \in X : \chi(x) = +1\},
\qquad
N = \{x \in X : \chi(x) = -1\}.
$$

Let \(p = |P|\) and \(q = |N|\), so \(p + q = n\). Since \(\mathcal{P}(X)\) contains every subset of \(X\), it contains \(P\) and \(N\) in particular. Therefore,

$$
\begin{aligned}
\max_{S \in \mathcal{P}(X)}
\left| \sum_{x \in S} \chi(x) \right|
&\ge
\max\left\{
\left| \sum_{x \in P} \chi(x) \right|,
\left| \sum_{x \in N} \chi(x) \right|
\right\} \\
&= \max\{p,q\}.
\end{aligned}
$$

As \(p + q = n\), we have

$$
\max\{p,q\} \ge \left\lceil \frac{n}{2} \right\rceil.
$$

Since the coloring \(\chi\) was arbitrary, it follows that

$$
\operatorname{disc}(\mathcal{P}(X))
\ge \left\lceil \frac{n}{2} \right\rceil.
$$

## Upper bound

It remains to exhibit a coloring whose maximum discrepancy over all subsets is at most \(\lceil n/2 \rceil\). Choose a coloring \(\chi\) for which

$$
|P| = \left\lceil \frac{n}{2} \right\rceil,
\qquad
|N| = \left\lfloor \frac{n}{2} \right\rfloor.
$$

Such a coloring evidently exists. Now let \(S \subseteq X\) be arbitrary, and write \(S = S_+ \cup S_-\), where \(S_+ = S \cap P\) and \(S_- = S \cap N\). Then

$$
\sum_{x \in S} \chi(x) = |S_+| - |S_-|.
$$

Since

$$
0 \le |S_+| \le \left\lceil \frac{n}{2} \right\rceil
\qquad\text{and}\qquad
0 \le |S_-| \le \left\lfloor \frac{n}{2} \right\rfloor,
$$

we obtain

$$
-\left\lfloor \frac{n}{2} \right\rfloor
\le |S_+| - |S_-|
\le \left\lceil \frac{n}{2} \right\rceil.
$$

Hence,

$$
\left| \sum_{x \in S} \chi(x) \right|
\le \left\lceil \frac{n}{2} \right\rceil
$$

for every \(S \subseteq X\). Taking the maximum over \(S \in \mathcal{P}(X)\) and then the minimum over colorings, we conclude that

$$
\operatorname{disc}(\mathcal{P}(X))
\le \left\lceil \frac{n}{2} \right\rceil.
$$

Combining the lower and upper bounds yields

$$
\boxed{
\operatorname{disc}(\mathcal{P}(X))
= \left\lceil \frac{n}{2} \right\rceil
}.
$$

\(\blacksquare\)
