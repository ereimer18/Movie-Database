# Python code to illustrate parsing of XML files
# importing the required modules 
import csv
import xml.etree.ElementTree as ET


def parseXML(xmlFile):
    # create element tree object
    tree = ET.parse(xmlFile)

    # get root element 
    root = tree.getroot()

    # create empty list for news items 
    people = []

    # iterate news items 
    for item in root.findall('./channel/item'):

        # empty news dictionary 
        news = {}

        # iterate child elements of item 
        for child in item:
            news[child.tag] = child.text.encode('utf8')

        # append news dictionary to news items list
        people.append(news)

        # return news items list
    return people


def saveToCSV(people, filename):
    # specifying the fields for csv file
    fields = ['first_name', 'last_name', 'start_year', 'end_year', 'birth_year', 'death_year', 'birth_country', 'notes']

    # writing to csv file 
    with open(filename, 'w') as csvFile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvFile, fieldnames=fields)

        # writing headers (field names) 
        writer.writeheader()

        # writing data rows 
        writer.writerows(people)


def main():
    # parse xml file 
    people = parseXML('../xml/people.xml')

    # store news items in a csv file 
    saveToCSV(people, 'people.csv')


if __name__ == "__main__":
    # calling main function
    main()
