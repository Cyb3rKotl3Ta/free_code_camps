from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    course_html_tag = soup.find('h5')
    courses_html_tags = soup.find_all('h5')
    course_cards = soup.find_all('div', class_='card')
    # print(courses_html_tags)

    for course in course_cards:
        print(course.text)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

