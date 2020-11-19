import csv
from difflib import SequenceMatcher


def main():
    global a_name

    actor_csv = open('../final-csv/actor.csv')
    person_csv = open('../final-csv/people.csv')
    match_csv = open('../final-csv/matches.csv')
    merge_handler = open('../final-csv/temp_people.csv', 'a')
    act_csv = open('../final-csv/temp_actor.csv', 'a')
    duplicate_csv = open('../final-csv/duplicates.csv', 'a')

    person_reader = csv.reader(person_csv, delimiter=',')
    actor_reader = csv.reader(actor_csv, delimiter=',')
    match_reader = csv.reader(match_csv, delimiter=',')
    merge_writer = csv.writer(merge_handler, delimiter=',')
    actor_writer = csv.writer(act_csv, delimiter=',')
    duplicate_writer = csv.writer(duplicate_csv, delimiter=',')

    actor_count = 0
    person_count = 0
    match_count = 0
    serial = 0

    actors = []
    people = []
    matches = []
    pmatches = []

    for m in match_reader:
        name = m[0]
        pname = m[1]
        matches.append(name)
        pmatches.append(pname)



    for actor in actor_reader:

        if actor_count > 0:
            a_name = actor[2] + actor[1]
            actors.append(a_name)

            if a_name not in matches:
                merge_writer.writerow(
                    [actor[2], actor[1], actor[5], actor[6], actor[7], actor[8], actor[9], '', serial])
                actor_writer.writerow(
                    [actor[0], actor[1], actor[2], actor[3], actor[4], actor[5], actor[6],
                     actor[7], actor[8], actor[9], serial])
            else:
                p = findPerson(a_name)
                if p is not None:
                    merge_writer.writerow(
                        [p[0], p[1], p[2], p[3], p[4], p[5], p[6],p[7], serial])

                actor_writer.writerow(
                    [actor[0], actor[1], actor[2], actor[3], actor[4], actor[5], actor[6],
                     actor[7], actor[8], actor[9], serial])
            serial += 1

        actor_count += 1

    for person in person_reader:

        if person_count > 0:
            p_name = person[0] + person[1]
            people.append(p_name)
            if p_name not in pmatches:
                merge_writer.writerow(
                    [person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7], serial])
        person_count += 1
        serial += 1

    # match(people)


def match(people):
    matcher = open('../final-csv/matches.csv', 'w')
    match_writer = csv.writer(matcher, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for person in people:
        actor_csv = open('../final-csv/actor.csv')
        actor_reader = csv.reader(actor_csv, delimiter=',')
        for actor in actor_reader:
            actor_name = actor[2] + actor[1]

            closeness = similar(actor_name, person)

            if closeness > .90:
                print(f'\tActor{actor_name} --> Person {person}')
                match_writer.writerow([actor_name, person])


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def findPerson(a_name):
    name = None
    ret = None
    match_csv = open('../final-csv/matches.csv')
    match_reader = csv.reader(match_csv, delimiter=',')
    for m in match_reader:
        if a_name == m[0]:
            name = m[1]

    person_csv = open('../final-csv/people.csv')
    person_reader = csv.reader(person_csv, delimiter=',')
    for person in person_reader:
        pName = person[0] + person[1]
        if name == pName:
            ret = person

    return ret

main()
