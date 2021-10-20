import pandas as pd

word_counts = pd.read_csv('hw1_word_counts_05.txt', sep=" ", header=None)
word_counts.columns = ['word', 'count']
word_counts = word_counts.sort_values('count', ascending=False)

count_sum = sum(word_counts['count'])
word_prob = word_counts['count'] / count_sum;
word_counts['prob'] = word_prob


def prob_l_at_any_i_given_w(curr: list, w: str, l: str) -> float:
    for i in range(0, len(curr)):
        if curr[i] == '_' and w[i] == l:
            return 1
    return 0


def prob_e_given_w(curr: list, block_set: set, w: str) -> float:
    for i in range(0, len(curr)):
        if curr[i] == '_':
            if w[i] in block_set:
                return 0
        elif curr[i] != w[i]:
            return 0
    return 1


def best_next_guess(curr: list, block_list: list, word_counts: pd.DataFrame) -> [str, float]:
    # add chars in curr into block list
    block_list += [c for c in curr if c != '_']
    block_set = set(block_list)
    best_guess = None
    max_prob = -1
    for letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]:
        if letter in block_list:
            continue
        num = 0
        denom = 0
        for _, row in word_counts.iterrows():
            tmp = prob_e_given_w(curr, block_set, row['word'])
            num += prob_l_at_any_i_given_w(curr, row['word'], letter) * tmp * row['prob']
            denom += tmp * row['prob']
        p = num / denom
        if p > max_prob:
            max_prob = p
            best_guess = letter
    return [best_guess, max_prob]


if __name__ == '__main__':
    # %%
    print(best_next_guess(['_', '_', '_', '_', '_'], [], word_counts))
    # %%
    print(best_next_guess(['_', '_', '_', '_', '_'], ['E', 'A'], word_counts))
    # %%
    print(best_next_guess(['A', '_', '_', '_', 'S'], [], word_counts))
    # %%
    print(best_next_guess(['A', '_', '_', '_', 'S'], ['I'], word_counts))
    # %%
    print(best_next_guess(['_', '_', 'O', '_', '_'], ['A', 'E', 'M', 'N', 'T'], word_counts))
    # %%
    print(best_next_guess(['_', '_', '_', '_', '_'], ['E', 'O'], word_counts))
    # %%
    print(best_next_guess(['D', '_', '_', 'I', '_'], [], word_counts))
    # %%
    print(best_next_guess(['D', '_', '_', 'I', '_'], ['A'], word_counts))
    # %%
    print(best_next_guess(['_', 'U', '_', '_', '_'], ['A', 'E', 'I', 'O', 'S'], word_counts))
