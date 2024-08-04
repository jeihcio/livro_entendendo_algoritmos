# Algorítimo que divide o problema em casos menores até achar o caso base

def quicksort(array):
    # caso base quando o array é vazio ou possuí apenas um elmento
    if len(array) < 2:
        return array
    else:
        # Elemento que vamos usar como central para dividir 
        # os elementos maiores e menores que ele
        pivo = array[0] 

        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)
    
print(quicksort([10, 5, 2, 3]))