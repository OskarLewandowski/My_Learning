# -*- coding: utf-8 -*-

"""
Automat deterministyczny.
"""

class DeterministicAutomaton:
    """
    Klasa reprezentująca deterministyczny automat skończenie stanowy.
    """

    def __init__(self):
        """
        Konstruktor.
        """

        # Liczba wszystkich stanów,
        # stany będą identyfikowane przez kolejne liczby:
        # 0, 1, ..., number_of_states - 1
        self.number_of_states = 0

        # przejścia będą przechowywane w tablicy
        # haszującej indeksowanej parą stan-znak,
        # tj. transitions[(state_from, character)]
        # przechowuje stan docelowy przy
        # przejściu od stanu state_from przez znak
        # character
        self.transitions = { }

        # stan początkowy
        self.initial_state = None

        # zbiór stanów końcowych
        self.final_states = set()

    # funkcje modyfikujące automat

    def add_state(self):
        """
        Dodaje nowy stan, zwraca numer utworzonego stanu
        """
        self.number_of_states += 1
        return self.number_of_states - 1

    def add_transition(self, state_from, symbol, state_to):
        """
        Dodaje przejście od stanu state_from przez znak symbol
        do stanu state_to.
        """
        self.transitions[(state_from, symbol)] = state_to

    def mark_as_initial(self, state):
        """
        Oznacza stan jako początkowy.
        """
        self.initial_state = state

    def mark_as_final(self, state):
        """
        Oznacza stan jako końcowy.
        """
        self.final_states.add(state)

    # dostęp do automatu

    def get_number_of_states(self):
        """
        Zwraca liczbę stanów.
        """
        return self.number_of_states

    def get_initial_state(self):
        """
        Zwraca stan początkowy.
        """
        return self.initial_state

    def is_final_state(self, state):
        """
        Zwraca informacje, czy stan jest końcowy.
        """
        return state in self.final_states

    def get_target_state(self, state_from, symbol):
        """
        Zwraca stan docelowy, przy przejściu od stanu state_from
        przez symbol bądź wartość None, jeśli nie
        ma takiego przejścia.
        """
        return self.transitions.get((state_from, symbol))

    def accepts(self, string):
        """
        Sprawdza, czy automat akceptuje napis.
        """
        current_state = self.get_initial_state()

        for symbol in string:
            current_state = self.get_target_state(current_state, symbol)

            if current_state is None:
                return False

        return self.is_final_state(current_state)


if __name__ == '__main__':

    # budowanie automatu
    AUTOMATON = DeterministicAutomaton()

    INITIAL_STATE = AUTOMATON.add_state()
    FINAL_STATE = AUTOMATON.add_state()
    AUTOMATON.add_transition(INITIAL_STATE, 'x', FINAL_STATE)

    AUTOMATON.mark_as_initial(INITIAL_STATE)
    AUTOMATON.mark_as_final(FINAL_STATE)

    # uruchamianie automatu
    print(AUTOMATON.accepts("x")) # wypisze True
    print(AUTOMATON.accepts("")) # wypisze False
    print(AUTOMATON.accepts("ab")) # wypisze False
