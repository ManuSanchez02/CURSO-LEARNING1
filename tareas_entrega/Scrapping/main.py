from re import L
from socket import create_connection
from lxml.html import parse
from lxml.etree import tostring
import urllib.request
import sqlite3
from sqlite3 import Error

BASE_URL = 'https://www.readwn.com/'
NUMBER_OF_CHAPTERS_PER_NOVEL = 10
NUMBER_OF_NOVELS = 500

def existe_en_db(connection, url):
    sql = ''' SELECT * FROM novels WHERE url=? '''
    cursor = connection.cursor()
    cursor.execute(sql, (url,))
    records = cursor.fetchall()
    cursor.close()

    if records:
        print(f"Ya existia: {records[0][0]}")
        return True
    
    return False

def get_chapter_content(chapter_link):
    chapter_response = urllib.request.urlopen(chapter_link)
    chapter_doc = parse(chapter_response)  
    doc_xpath = chapter_doc.xpath('//*[@class="chapter-content"]')
    if not doc_xpath:
        raise Error("No tiene contenido")
    content = (' '.join(x.strip() for x in doc_xpath[0].itertext())).strip()
    return content

def get_novel_data(relative_url):
    novel_url = BASE_URL + relative_url
    novel_response = urllib.request.urlopen(novel_url)
    novel_doc = parse(novel_response)

    novel_title = novel_doc.xpath('//*[@itemprop="name"]')[0].text
    novel_author = novel_doc.xpath('//*[@itemprop="author"]')[0].text
    genres_elements = novel_doc.xpath('//*[@class="property-item"]')
    if not genres_elements[0].text:
        raise Error("No tiene categorias")

    novel_genres = ','.join(list(map(lambda elem: elem.text, genres_elements)))
    novel_summary = (' '.join(novel_doc.xpath('//*[@class="summary"]/*[@class="content"]')[0].itertext())).strip()
    
    #novel_tags = novel_doc.xpath('//*[@class="tag"]')[0].text
    chapter_anchor_elements = novel_doc.xpath(f'//*[@class="chapter-list"]/li[position() <= 10]/a')
    relative_chapter_urls = [chapter.attrib['href'] for chapter in chapter_anchor_elements]

    novel_content = ' '.join(get_chapter_content(BASE_URL + relative_chapter_url) for relative_chapter_url in relative_chapter_urls)

    print(f"{novel_author} - {novel_title}")
    return (novel_url, novel_title, novel_author, novel_genres, novel_summary, novel_content)


def scrape(connection):
    #cambio de user agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    page = 0
    novel_number = 0
    
    #descarga y parseo de la pagina.
    while novel_number < NUMBER_OF_NOVELS:
        try:
            response = urllib.request.urlopen(f'https://www.readwn.com/list/all/all-onclick-{page}.html')
            doc = parse(response)
            
            anchor_elements = doc.xpath('//*[@class="novel-item"]/a')

            relative_novel_urls = [anchor.attrib['href'] for anchor in anchor_elements]
            for relative_novel_url in relative_novel_urls:
                if novel_number >= NUMBER_OF_NOVELS:
                    return

                try:
                    if existe_en_db(connection, BASE_URL + relative_novel_url):
                        novel_number += 1
                        continue
                    
                    print(f"Creando: {BASE_URL + relative_novel_url}")
                    novel_data = get_novel_data(relative_novel_url)
                    create_novel(connection, novel_data)

                    novel_number += 1

                except Error as err:
                    print(err)
                    continue

            page += 1
        except Error as err:
            print(err)
        

    
def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        cursor.close()
    except Error as e:
        print(e)

def create_novel(connection, novel):
    sql = ''' INSERT INTO novels(url, name, author, genres, sinopsis, content) VALUES(?,?,?,?,?,?) '''
    cursor = connection.cursor()
    cursor.execute(sql, novel)
    connection.commit()
    cursor.close()
    return cursor.lastrowid

def main():
    sql_create_novels_table = """ CREATE TABLE IF NOT EXISTS novels (
                                    url text PRIMARY KEY,
                                    name text NOT NULL,
                                    author text,
                                    genres text,
                                    sinopsis text,
                                    content text
                                ); """
    conn = create_db(r"./novels.db")
    if conn is None:
        return -1
    create_table(conn, sql_create_novels_table)
    conn.commit()
    with conn:
        scrape(conn)

if __name__ == '__main__':
    main()