def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len( dna )


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len( dna1 ) > len( dna2 )


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    cnt = 0
    for s in dna :
        if s == nucleotide :
            cnt += 1
    
    return cnt


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find( dna2 ) != -1 :
        return True
    else :
        return False

def is_valid_sequence(dna):
    '''
    (str) -> bool

    return a sequence is a valid dna or not

    >>>is_valid_sequence('AGCT')
    True

    >>>is_valid_sequence('ADCGT')
    False

    >>>is_valid_sequence('aGCT')
    False

    '''
    nucleotideSets = 'AGCT'
    for s in dna :
        if s not in nucleotideSets:
            return False
    
    return True

def insert_sequence(dna1,dna2,index) :
    '''
    (str,str,int) -> str

    return the inserted string

    >>>insert_sequence('CCGG','AT',2)
    CCATGG

    '''
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    '''
    (str) -> str
    return the complementary nucleotide
    >>>get_complement('A')
    T
    '''

    if nucleotide == 'A' :
        return 'T'
    elif nucleotide == 'T' :
        return 'A'
    elif nucleotide == 'G' :
        return 'C'
    else :
        return 'G'

def get_complementary_sequence( dna ):
    '''
    (str) -> str
    return the complement dna_sequence
    >>>get_complement_sequence('AGTCT')
    TCAGA
    '''
    ans =''
    for s in dna:
        ans = ans + get_complement(s)
    
    return ans
