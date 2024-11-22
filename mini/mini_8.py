def format_table(benchmarks, algos, results):
    column_lens = [13]  # " Benchmark " 11 symbols

    for string in benchmarks:
        column_lens[0] = max(column_lens[0], len(string) + 2)

    for i in range(len(algos)):
        column_lens.append(len(algos[i]))
        for j in range(len(results)):
            column_lens[i+1] = max(column_lens[i+1], len(str(results[j][i])))

    print("| Benchmark " + " " * (column_lens[0] - 11), end="")
    for i in range(len(algos)):
        print(f"| {algos[i]} " + " " * (column_lens[i + 1] - len(algos[i])), end="")
    print("|")

    print("|" + "-" * (sum(column_lens) + len(column_lens) * 3 - 3) + "|")

    for i in range(len(benchmarks)):
        print(f"| {benchmarks[i]} " + " " * (column_lens[0] - len(benchmarks[i]) - 2), end="")
        for j in range(len(results[i])):
            print(f"| {results[i][j]} " + " " * (column_lens[j + 1] - len(str(results[i][j]))), end="")
        print("|")


format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [10**10, 2.9, 3.9]])
