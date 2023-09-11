from bs4 import BeautifulSoup

# Open the HTML file named 'home.html' in read-only mode ('r')
with open('home.html', 'r') as htmlFile:
    # Read the contents of the HTML file into the 'content' variable
    content = htmlFile.read()
    
    # Print the contents of the HTML file
    # print(content)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # The find method searches for the first element and then stops the execution
    tags = soup.find('button')
    print(tags)

    # To find all the 'button' tags
    coursesHtmlTags = soup.find_all('h2')
    print(coursesHtmlTags)

    for course in coursesHtmlTags:
        print(course.text)
   
    courseCards = soup.find_all('div', class_='card')
    for course in courseCards:
        courseName = course.h2.text
        coursePrice = course.a.text

        print(courseName)
        print(coursePrice)
    