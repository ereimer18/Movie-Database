import csv
from difflib import SequenceMatcher


def main():
    global a_name

    actor_csv = open('../final-csv/directs.csv')
    person_csv = open('../final-csv/temp_people.csv')

    person_reader = csv.reader(person_csv, delimiter=',')
    actor_reader = csv.reader(actor_csv, delimiter=',')


    actor_count = 0
    person_count = 0

    actors = []
    people = []

    for actor in actor_reader:
        if actor_count > 0:
            a_name = actor[1]
            actors.append(a_name)
        actor_count += 1

    for person in person_reader:

        if person_count > 0:
            p_name = person[3] + person[4]
            people.append(p_name)
        person_count += 1

    match(people)


def match(people):
    matcher = open('../old-matches/matches-movie-directs.csv', 'w')
    match_writer = csv.writer(matcher, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for person in people:
        actor_csv = open('../final-csv/directs.csv')
        actor_reader = csv.reader(actor_csv, delimiter=',')
        for actor in actor_reader:
            actor_name = actor[1]

            closeness = similar(actor_name, person)

            if closeness > .8:
                print(f'\tActor {actor_name} --> Person {person}')
                match_writer.writerow([actor_name, person])


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


main()
