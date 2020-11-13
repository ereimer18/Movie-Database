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
    newsItems = []

    # iterate news items 
    for item in root.findall('./channel/item'):

        # empty news dictionary 
        news = {}

        # iterate child elements of item 
        for child in item:

            # special checking for namespace object content:media 
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

                # append news dictionary to news items list
        newsItems.append(news)

        # return news items list
    return newsItems


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    # writing to csv file 
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names) 
        writer.writeheader()

        # writing data rows 
        writer.writerows(newsitems)


def main():
    # parse xml file 
    people = parseXML('xml/people.xml')

    # store news items in a csv file 
    savetoCSV(people, 'people.csv')


if __name__ == "__main__":
    # calling main function
    main() 