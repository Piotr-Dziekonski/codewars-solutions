def best_match(goals1, goals2):
    diff = [(goals1[x] - goals2[x], goals2[x]) for x in range(0, len(goals1))]
    m = min(diff)
    val = min(diff)[1]
    for i in diff:
        if m[0] == i[0] and i[1] > m[1] and i[1] > val:
            val = i[1]
    return diff.index((m[0],val))