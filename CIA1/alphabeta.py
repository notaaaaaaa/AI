import math

def alphabeta(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"Maximizer at depth {depth} with alpha = {alpha}, beta = {beta}")

        for i in range(2):
            value = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"Maximizer at depth {depth}, updated alpha = {alpha}")
 
            if beta <= alpha:
                print(f"Pruning branches at depth {depth} as beta ({beta}) <= alpha ({alpha})")
                break
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best
    else:
        best = math.inf
        print(f"Minimizer at depth {depth} with alpha = {alpha}, beta = {beta}")

        for i in range(2):
            value = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"Minimizer at depth {depth}, updated beta = {beta}")
 
            if beta <= alpha:
                print(f"Pruning branches at depth {depth} as beta ({beta}) <= alpha ({alpha})")
                break
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best



