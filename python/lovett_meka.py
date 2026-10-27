import numpy as np

def lovett_meka_discrepancy(A, max_outer_iter=10, max_inner_iter=2000, step_size=None):
    """
    Lovett-Meka algorithm for combinatorial discrepancy minimization.
    
    Parameters:
    A : ndarray of shape (m, n)
        Incidence matrix: A[i, j] = 1 if element j is in set i, else 0.
    max_outer_iter : int
        Number of recursive partial-coloring rounds.
    max_inner_iter : int
        Maximum random-walk steps per round.
    step_size : float or None
        Gaussian step size. If None, computed from n.
    
    Returns:
    x : ndarray of shape (n,)
        Coloring vector with entries in {-1, +1}.
    """
    m, n = A.shape
    x = np.zeros(n)  # start at origin (fractional)
    
    # Track which variables are still "alive" (not yet frozen)
    alive = np.ones(n, dtype=bool)
    
    if step_size is None:
        step_size = 0.1 / np.sqrt(n)
    
    # Discrepancy threshold (simplified scaling; real algorithm uses tighter bounds)
    # This is a rough proxy for the C * sqrt(n * log(m/n)) bound
    disc_bound = 2.0 * np.sqrt(n * np.log(max(2.0, m / max(1, n))))
    
    for outer in range(max_outer_iter):
        # Reset for this round: fractional start for uncolored variables
        x_round = np.zeros(n)
        x_round[~alive] = x[~alive]  # keep frozen values
        
        for step in range(max_inner_iter):
            # --- Build the constraint subspace ---
            # Frozen coordinates: directions e_j for frozen j must be excluded
            frozen_indices = np.where(~alive)[0]
            
            # Dangerous constraints: rows where current discrepancy is near the bound
            current_disc = A @ x_round
            dangerous = np.abs(current_disc) >= disc_bound * 0.9  # near-tight
            
            # Collect all vectors that define the forbidden subspace
            forbidden = []
            for j in frozen_indices:
                e = np.zeros(n)
                e[j] = 1.0
                forbidden.append(e)
            for i in np.where(dangerous)[0]:
                forbidden.append(A[i, :])
            
            # Project onto the orthogonal complement of the forbidden subspace
            if len(forbidden) > 0:
                F = np.array(forbidden)  # shape (k, n)
                # Use SVD to find null space of F
                # Directions orthogonal to all rows of F:
                U, S, Vt = np.linalg.svd(F, full_matrices=True)
                # Null space = rows of Vt corresponding to zero singular values
                rank = np.sum(S > 1e-10)
                null_basis = Vt[rank:, :]  # shape (n - rank, n)
            else:
                null_basis = np.eye(n)
            
            if null_basis.shape[0] == 0:
                break  # no room to move
            
            # --- Take a Gaussian step in the null space ---
            # Sample a random direction in the null space
            coeffs = np.random.randn(null_basis.shape[0])
            direction = coeffs @ null_basis  # shape (n,)
            
            # Normalize to unit length (or use as-is with step_size)
            norm = np.linalg.norm(direction)
            if norm < 1e-12:
                continue
            direction /= norm
            
            # Update: small step, but clamp to [-1, 1]
            x_round += step_size * direction
            
            # Clamp to hypercube
            x_round = np.clip(x_round, -1.0, 1.0)
            
            # --- Freeze any coordinate that hit ±1 ---
            newly_frozen = alive & (np.abs(x_round) >= 1.0 - 1e-6)
            if np.any(newly_frozen):
                # Set exactly to ±1
                x_round[newly_frozen] = np.sign(x_round[newly_frozen])
                x[newly_frozen] = x_round[newly_frozen]
                alive[newly_frozen] = False
            
            # Check if enough variables are frozen (at least half of remaining)
            if np.sum(~alive) >= n / 2:
                break
        
        # After inner loop: finalize any remaining alive variables to nearest sign
        # (In the true algorithm, one would recurse on the remaining alive set.)
        if np.any(alive):
            # Simplified: just round the remaining fractional values
            x[alive] = np.sign(x_round[alive])
            # Handle zeros (sign returns 0) by random assignment
            zero_mask = alive & (x == 0)
            x[zero_mask] = np.random.choice([-1, 1], size=np.sum(zero_mask))
            alive[:] = False  # all done
        
        # Check discrepancy
        disc = np.max(np.abs(A @ x))
        if disc <= disc_bound * 1.5:  # acceptable
            break
    
    return x


# --- Example usage ---
if __name__ == "__main__":
    np.random.seed(42)
    
    # Create a small random set system: 20 sets, 10 elements
    m, n = 20, 10
    A = (np.random.rand(m, n) < 0.4).astype(float)
    
    # Ensure no empty rows (they don't affect discrepancy)
    for i in range(m):
        if A[i].sum() == 0:
            A[i, np.random.randint(n)] = 1.0
    
    print("Set system (incidence matrix):")
    print(A.astype(int))
    
    x = lovett_meka_discrepancy(A)
    print("\nColoring:", x)
    
    disc_per_set = A @ x
    print("Discrepancy per set:", disc_per_set)
    print("Maximum discrepancy:", np.max(np.abs(disc_per_set)))
