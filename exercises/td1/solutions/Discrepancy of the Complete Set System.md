# Discrepancy of the Complete Set System

**Theorem.** Let $X$ be a finite set with $|X| = n$, and let $\mathcal{F} = \mathcal{P}(X)$ be the complete set system on $X$, i.e. the collection of all subsets of $X$. Then the discrepancy of $\mathcal{F}$ is

```math
\mathrm{disc}(\mathcal{P}(X)) = \left\lceil \frac{n}{2} \right\rceil.
```

**Proof.** Recall that the discrepancy of a set system $\mathcal{F}$ on a ground set $X$ is defined by

```math
\mathrm{disc}(\mathcal{F}) = \min_{\chi \colon X \to \{\pm 1\}} \max_{S \in \mathcal{F}} \left| \sum_{x \in S} \chi(x) \right|,
```

where the minimum is taken over all two-colorings of $X$, and the maximum over all sets in the system.

We prove the two requisite inequalities separately.

**Lower bound.** Fix an arbitrary coloring $\chi \colon X \to \{\pm 1\}$, and put

```math
P = \{x \in X : \chi(x) = +1\}, \qquad N = \{x \in X : \chi(x) = -1\}.
```

Let $p = |P|$ and $q = |N|$, so $p + q = n$. Since $\mathcal{P}(X)$ contains every subset of $X$, it contains $P$ and $N$ in particular. Therefore

```math
\max_{S \in \mathcal{P}(X)} \left| \sum_{x \in S} \chi(x) \right| \ge \max\left\{ \left| \sum_{x \in P} \chi(x) \right|, \left| \sum_{x \in N} \chi(x) \right| \right\} = \max\{p, q\}.
```

As $p + q = n$, we have $\max\{p, q\} \ge \lceil n/2 \rceil$. Since the coloring $\chi$ was arbitrary, it follows that

```math
\mathrm{disc}(\mathcal{P}(X)) \ge \left\lceil \frac{n}{2} \right\rceil.
```

**Upper bound.** It remains to exhibit a coloring whose maximum discrepancy over all subsets is at most $\lceil n/2 \rceil$. Choose a coloring $\chi$ for which

```math
|P| = \left\lceil \frac{n}{2} \right\rceil, \qquad |N| = \left\lfloor \frac{n}{2} \right\rfloor.
```

Such a coloring evidently exists. Now let $S \subseteq X$ be arbitrary, and write $S = S_+ \cup S_-$, where $S_+ = S \cap P$ and $S_- = S \cap N$. Then

```math
\sum_{x \in S} \chi(x) = |S_+| - |S_-|.
```

Since $0 \le |S_+| \le \lceil n/2 \rceil$ and $0 \le |S_-| \le \lfloor n/2 \rfloor$, we obtain

```math
-\left\lfloor \frac{n}{2} \right\rfloor \le |S_+| - |S_-| \le \left\lceil \frac{n}{2} \right\rceil.
```

Hence

```math
\left| \sum_{x \in S} \chi(x) \right| \le \left\lceil \frac{n}{2} \right\rceil
```

for every $S \subseteq X$. Taking the maximum over $S \in \mathcal{P}(X)$ and then the minimum over colorings, we conclude that

```math
\mathrm{disc}(\mathcal{P}(X)) \le \left\lceil \frac{n}{2} \right\rceil.
```

Combining the lower and upper bounds yields

```math
\mathrm{disc}(\mathcal{P}(X)) = \left\lceil \frac{n}{2} \right\rceil. \qquad \blacksquare
```
