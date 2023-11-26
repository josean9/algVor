def min_swaps_couples(row):
    def dfs(index):
        if index == len(row):
            return 0

        current_person = row[index]
        partner = current_person ^ 1

        if row[index + 1] == partner:
            return dfs(index + 2)
        else:
            partner_index = row.index(partner)
            row[index + 1], row[partner_index] = row[partner_index], row[index + 1]
            return 1 + dfs(index + 2)

    return dfs(0)

# Ejemplo de uso
seats = [0, 2, 1, 3]
resultado = min_swaps_couples(seats)
print(resultado)
