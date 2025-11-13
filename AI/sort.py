def swap(lst, idx_a, idx_b):
    elem_a = lst[idx_a]
    lst[idx_a] = lst[idx_b]
    lst[idx_b] = elem_a

    # OF

    # lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]

def find_index_of_minimum(lst, start_idx=0):
    minimum = None
    min_index = None
    for idx in range(start_idx, len(lst)):
        if not minimum or lst[idx] < minimum:
            minimum = lst[idx]
            min_index = idx
    return min_index


def selection_sort(lst):
    sorted_lst = list(lst)
    for pointer in range(len(lst)):
        smallest_index = find_index_of_minimum(sorted_lst, pointer)
        swap(sorted_lst, pointer, smallest_index)
    return sorted_lst


test_list = [1,3,7,2,5,1,3]

# print(find_index_of_minimum(test_list,3))

print(selection_sort(test_list))



def insert(lst, grens, waarde):
    """
    Voeg gegeven waarde in op de juiste plek van het gesorteerde deel van gegeven lijst.
    Er wordt gekeken vanaf de gegeven grens.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen. Deze lijst
            is reeds gesorteerd van index 0 tot en met index `grens`, dus het deel `lst[0]` tot en
            met `lst[grens]`.
        grens (int): De index tot waar gegeven lijst `lst` al is gesorteerd.
        waarde (int): Het element dat op de juiste plek moet worden ingevoegd in het reeds gesorteerde
            deel van de lijst.
    """
    # Aanpak: begin bij index `grens` en verplaats elementen groter dan `waarde` naar rechts.
    # Als je een waarde tegenkomt die kleiner is dan `waarde` (of het begin van lijst `lst`),
    # dan voeg je `waarde` in op de vrijgekomen plek.
    
    return None     # De functie retourneert niets


def insertion_sort(lst):
    """
    Sorteer gegeven lijst volgens het insertion sort algoritme.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    # Kopieer de lijst, zodat de originele lijst niet verandert
    return
