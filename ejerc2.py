def min_candies(hunger):
    n = len(hunger)
    
    # Inicializar el array de dulces con todos los niños teniendo al menos un caramelo
    candies = [1] * n
    
    # Paso hacia adelante: Asegurar que los niños con hambre más alto tengan más dulces
    for i in range(1, n):
        if hunger[i] > hunger[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Paso hacia atrás: Asegurar que los niños con hambre más alto tengan más dulces que sus vecinos
    for i in range(n - 2, -1, -1):
        if hunger[i] > hunger[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # Sumar el total de dulces necesarios
    total_candies = sum(candies)
    
    return total_candies

# Ejemplo de uso
hunger = [1, 0, 2]
resultado = min_candies(hunger)
print(resultado)
