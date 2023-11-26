def can_jump(nums):
    max_reach = 0
    n = len(nums)

    for i in range(n):
        # Si en algún punto no puedes avanzar más, retorna False
        if i > max_reach:
            return False

        # Actualiza el máximo alcance posible desde la posición actual
        max_reach = max(max_reach, i + nums[i])

        # Si puedes llegar al último índice, retorna True
        if max_reach >= n - 1:
            return True

    return False

# Ejemplo de uso
nums = [2, 3, 1, 1, 4]
resultado = can_jump(nums)
print(resultado)
