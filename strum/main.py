import random
import click

@click.command()
def main():
    number_of_measures = 2
    beats_in_measure = 4

    for measure_index in range(0, number_of_measures):
        for beat_index in range(0, beats_in_measure):
            print(f"{beat_index+1} + ", end='')

        if measure_index + 1 != number_of_measures:
            print(" |  ", end='')

    print()

    for measure_index in range(0, number_of_measures):
        for beat_index in range(0, beats_in_measure * 2):
            if (random.random() < 0.7):
                if beat_index % 2 == 0:
                    action = 'D'
                else:
                    action = 'U'
            else:
                action = ' '

            print(f"{action} ", end='')

        if measure_index + 1 != number_of_measures:
            print(" |  ", end='')

    print()
