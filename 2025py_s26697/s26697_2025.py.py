# Cel programu:
# Program generuje losową sekwencję DNA o zadanej długości, zapisuje ją w formacie FASTA do pliku
# oraz oblicza statystyki procentowe występowania nukleotydów A, C, G, T
# i stosunek %CG do %AT. Dodatkowo wstawia podane imię w losowym miejscu sekwencji,
# ale nie wpływa ono na statystyki ani długość sekwencji.
# Program może być wykorzystywany do nauki bioinformatyki oraz obsługi formatu FASTA.

import random  # Importujemy biblioteke random która umożliwia generowanie liczb pseudolosowych
import re  # Importujemy regex w celu walidacji danych


def generate_dna_sequence(length):  # metoda zwracajaca wygenerowana sekwencje ACTG
    return ''.join(random.choices('ACGT',
                                  k=length))  # kontatanacja napisu składająco sie z losowo wybranych liter z przedziało w ilości = lenght


def insert_name_into_sequence(sequence,
                              name):  # metoda zwracająca sekwencje z dodanym do niej imieniem w losowym miejscu
    insert_pos = random.randint(0,
                                len(sequence))  # losowanie pozycji do której wpiszemy imie w granicach długosci sekwencji
    return sequence[:insert_pos] + name + sequence[
                                          insert_pos:]  # dodanie imienia do sekwecji na wczesniej wylosowanej pozycji i zwrócenie nowej sekwencji


def calculate_statistics(sequence):  # funkcja generująca statystyki dla podanej sekwencji
    # ORGINAL
    # filtered_seq = ''.join([nt for nt in sequence if nt in 'ACGT'])
    # total = len(filtered_seq)
    # stats = {
    #    'A': round((filtered_seq.count('A') / total) * 100, 1),
    #   'C': round((filtered_seq.count('C') / total) * 100, 1),
    #   'G': round((filtered_seq.count('G') / total) * 100, 1),
    #  'T': round((filtered_seq.count('T') / total) * 100, 1),
    # }
    #   cg = filtered_seq.count('C') + filtered_seq.count('G')
    # at = filtered_seq.count('A') + filtered_seq.count('T')
    # cg_at_ratio = round((cg / at) * 100, 1) if at != 0 else 0.0
    # return stats, cg_at_ratio

    # MODIFIED (Poprawka 2 usunąłem filtrowanie poniewaz zmiana kolejności wykonwywania zadań sprawia, że jest ono nie potrzebne
    # i tylko zmniejsza wydajność obliczeniową i pamięciową oraz zmniejsza czytelnośc kodu)
    total = len(sequence)  # dlugosc sekwencji używana do obliczania %
    stats = {  # obliczenie zaokrąglonego % występowania każdego aminokwasu w sekwecji.
        'A': round((sequence.count('A') / total) * 100, 1),
        'C': round((sequence.count('C') / total) * 100, 1),
        'G': round((sequence.count('G') / total) * 100, 1),
        'T': round((sequence.count('T') / total) * 100, 1),
    }
    cg = sequence.count('C') + sequence.count('G')  # oblieczenie liczby par cg
    at = sequence.count('A') + sequence.count('T')  # oblieczenie liczby par at
    cg_at_ratio = round((cg / at) * 100,
                        1) if at != 0 else 0.0  # obliczenie stosunku udziału par cg do par ag w % zaokrąglone.
    return stats, cg_at_ratio  # zwrócenie obliczonych wartosci przez metode.


def main():
    # ORGINAL:
    # length = int(input("Podaj długość sekwencji: "))
    # seq_id = input("Podaj ID sekwencji: ")
    # description = input("Podaj opis sekwencji: ")
    # name = input("Podaj imię: ")

    # MODIFIED (Poprawka nr 3 dodałem podstawową walidacje dla każdej zmiennej w celu zminimalizowania błędów w działaniu programu i poprawienia user experience)
    while True:
        try:
            length = int(input("Podaj długość sekwencji: "))  # użytkownik podaje długosc sekwencji
            if length > 0:  # jezeli podany int spelnia warunek przerywa petle
                break
            else:
                print(
                    "Długość sekwencji musi być liczbą większą od zera.")  # wypisanie komunikatu o nieprawidłowej dlugosci podanego inta
        except ValueError:
            print(
                "Wprowadź prawidłową liczbę całkowitą.")  # w przypadku wystapienia wyjatku zwiazanego z nieprawidlowym formatem podanej zmiennej wypisz komunikat
    while True:
        seq_id = input("Podaj ID sekwencji: ")  # użytkownik podaje id sekwencji
        if re.fullmatch(r'[A-Za-z0-9_-]+', seq_id):
            break
        else:
            print("ID może zawierać tylko litery, cyfry, podkreślenia (_) i myślniki (-).")
    while True:
        description = input(
            "Podaj opis sekwencji: ").strip()  # użytkownik podaje opis sekwencji strip usuwa białe znaki
        if description:  # jezeli opis jest prawidlowy - nie pusty przerywa petle
            break
        else:
            print("Opis nie może być pusty.")  # wypisuje komunikat o bledzie
    while True:
        name = input("Podaj Imie: ").strip()  # użytkownik podaje imie do wklejenia strip usuwa biale znaki
        if name:  # jezeli imie jest prawidlowe - nie puste przerywa petle
            break
        else:
            print("Imie nie może być puste.")  # wypisuje komunikat o bledzie

    #   ORIGINAL:
    #   dna_sequence = generate_dna_sequence(length)
    #  dna_with_name = insert_name_into_sequence(dna_sequence, name)
    #   stats, cg_at_ratio = calculate_statistics(dna_with_name)

    # MODIFIED (POPRAWKA NR 1, ze względu na kolejność wykonowyania zadań lub brak walidacji,
    # podczas obliczania statystyk imię może mieć wpływ na wynik. ta poprawka ma temu zapobiec)
    dna_sequence = generate_dna_sequence(length)
    stats, cg_at_ratio = calculate_statistics(dna_sequence)  # zamiana kolejnosci
    dna_with_name = insert_name_into_sequence(dna_sequence, name)

    fasta_filename = f"{seq_id}.fasta"
    with open(fasta_filename,
              'w') as fasta_file:  # utworzenie pliku z przełącznikiem "write" o nazwie poprzedzonej id sekwencji
        fasta_file.write(f">{seq_id} {description}\n")  # wpisanie do 1 linijki opisu w formacie fasta
        fasta_file.write(dna_with_name + '\n')  # wipisanie do 2 linijki sekwencji dna wraz z wklejonym imieniem

    print(f"\nSekwencja została zapisana do pliku {fasta_filename}")  # wypisanie na konsoli info o zapisaniu do pliku
    print("Statystyki sekwencji:")  # wypisanie na konsoli informacji poprzedzającej wypisanie poszczególnych statystyk
    for nt in 'ACGT':  # dla kazdego nt z populacji 'actg' ->
        print(f"{nt}: {stats[nt]}%")  # wypisz statystyki ze wczesniej obliczonej zmiennej
    print(f"%CG: {cg_at_ratio}")  # wypisz cg ratio


if __name__ == "__main__":
    main()
