import csv

def main():
    actor_csv = open('../final-csv/made_by.csv')
    person_csv = open('../final-csv/studio.csv')
    match_csv = open('../final-csv/matches.csv')
    temp_person_csv = open('../final-csv/temp_studio.csv', 'w')
    temp_actor_csv = open('../final-csv/temp_made_by.csv', 'w')

    person_reader = csv.reader(person_csv, delimiter=',')
    actor_reader = csv.reader(actor_csv, delimiter=',')
    match_reader = csv.reader(match_csv, delimiter=',')
    person_writer = csv.writer(temp_person_csv, delimiter=',')
    actor_writer = csv.writer(temp_actor_csv, delimiter=',')

    actor_count = 0
    person_count = 0
    serial = 0

    actors = []
    people = []
    matches = []
    actor_match = []
    person_match = []

    # get matches
    for m in match_reader:
        print(m)
        aname = m[0]
        pname = m[1]
        matches.append([aname, pname])
        actor_match.append(m[0])

    # assign serial to persons
    for person in person_reader:
        if person_count > 0:
            p_name = person[1]
            person_write = [serial, p_name, "studio"] + person
            serial += 1
            people.append(person_write)
            person_match.append(person[1])
        person_count += 1

    # merge actors
    for actor in actor_reader:
        if actor_count % 10000:
            print(actor_count)

        if actor_count > 0:
            a_name = actor[1]

            # get serial if exists
            if a_name in actor_match:
                done = False
                for person in people:
                    if not done and matches[actor_match.index(a_name)][1] in person:
                        actor_write = [person[0], "made_by", a_name] + actor
                        actors.append(actor_write)
                        done = True

            # add if doesn't exist
            # else:
            #     actor_write = [serial, "made_by", a_name] + actor
            #     serial += 1
            #     people.append(actor_write)
            #     actors.append(actor_write)
        actor_count += 1

    # write files
    for person in people:
        person_writer.writerow(person)
    for actor in actors:
        actor_writer.writerow(actor)

main()
