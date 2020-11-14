import csv
import bs4

f = open('/home/jt/Documents/csis340/movies-database-support/html/Movies_STUDIOS.html')
soup = bs4.BeautifulSoup(f)
f.close()
g = open('a.xml', 'w')
print(g, soup.prettify())
g.close()

# file = open('/home/jt/Documents/csis340/movies-database-support/xml/remakes.xml')  # path to file
#
# for x in file:
#     print(file.readline())
