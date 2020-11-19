import csv
from difflib import SequenceMatcher


def main():

    global a_name

    actor_csv = open('../final-csv/actor.csv')
    person_csv = open('../final-csv/people.csv')

    actor_reader = csv.reader(actor_csv, delimiter=',')
    person_reader = csv.reader(person_csv, delimiter=',')
    actor_count = 0
    person_count = 0

    for actor in actor_reader:

        if actor_count > 0:
            a_name = actor[2] + actor[1]

        for person in person_reader:
            print(person_count)
            print(actor_count)

            if person_count > 0 and actor_count > 0:
                p_name = person[0] + person[1]
                closeness = similar(a_name, p_name)
                print(closeness)

                if closeness > .25:
                    print(f'\tActor{a_name} is similar to Person {p_name}')
            person_count += 1
        actor_count += 1
    print('done')


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


main()
