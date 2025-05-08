import random

def generate_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

def insert_name_into_sequence(sequence, name):
    insert_pos = random.randint(0, len(sequence))
    return sequence[:insert_pos] + name + sequence[insert_pos:]

def calculate_statistics(sequence):
    filtered_seq = ''.join([nt for nt in sequence if nt in 'ACGT'])
    total = len(filtered_seq)
    stats = {
        'A': round((filtered_seq.count('A') / total) * 100, 1),
        'C': round((filtered_seq.count('C') / total) * 100, 1),
        'G': round((filtered_seq.count('G') / total) * 100, 1),
        'T': round((filtered_seq.count('T') / total) * 100, 1),
    }
    cg = filtered_seq.count('C') + filtered_seq.count('G')
    at = filtered_seq.count('A') + filtered_seq.count('T')
    cg_at_ratio = round((cg / at) * 100, 1) if at != 0 else 0.0
    return stats, cg_at_ratio

def main():
    length = int(input("Podaj długość sekwencji: "))
    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

#  POPRAWKA NR 1, ze względu na kolejność wykonowyania zadań lub brak walidacji, podczas obliczania statystyk imię może mieć wpływ na wynik. ta poprawka ma temu zapobiec
#   dna_sequence = generate_dna_sequence(length)
#  dna_with_name = insert_name_into_sequence(dna_sequence, name)
#   stats, cg_at_ratio = calculate_statistics(dna_with_name)

    dna_sequence = generate_dna_sequence(length)
    stats, cg_at_ratio = calculate_statistics(dna_sequence) # zamiana kolejnosci
    dna_with_name = insert_name_into_sequence(dna_sequence, name)

    fasta_filename = f"{seq_id}.fasta"
    with open(fasta_filename, 'w') as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n")
        fasta_file.write(dna_with_name + '\n')

    print(f"\nSekwencja została zapisana do pliku {fasta_filename}")
    print("Statystyki sekwencji:")
    for nt in 'ACGT':
        print(f"{nt}: {stats[nt]}%")
    print(f"%CG: {cg_at_ratio}")

if __name__ == "__main__":
    main()
