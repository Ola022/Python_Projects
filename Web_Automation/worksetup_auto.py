import webbrowser as wb
import os

""" #TO INStall 
    [ pyinstaller -F worksetup_auto.py ]
    
"""


def open_url_auto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = ('https://www.udemy.com/course/python-in-action-a-practical-course-50-real-world-projects/learn/lecture'
            '/35711492#questions',
            'http://localhost:8889/tree/',
            'google.com',
            'youtube.com',
            'https://www.linkedin.com/in/abdullateefabdulazeez/',
            )
    for url in URLS:
        wb.get(chrome_path).open(url)


def open_desktop_app_auto():
    code_path = 'C:\\Program Files\\Git\\git-bash.exe'
    os.startfile(code_path)


if __name__ == '__main__':
    open_desktop_app_auto()



