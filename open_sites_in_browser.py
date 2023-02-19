import webbrowser
import os


website_1 = "https://website.in/"
email = "https://gmail.in/"
software_name = '"C:\\Users\\AK\\AppData\\Roaming\\software name\\software_name.exe"'
website_2 = "https://login_here.in/NewLayoutLogin.aspx"

mozilla_path = "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))


#open website_1 in chrome browser
webbrowser.open_new_tab(website_1)

#start application from windows
os.system("start 'software_name' 'C:\\Users\\AK\\AppData\\Roaming\\software name\\software_name.exe'")

#open govt email in mozilla firefox
webbrowser.get('firefox').open(website_2)

#open pfms portal in internet explorer
os.system('"C:/Program Files/Internet Explorer/iexplore.exe" https://anotherwebsite.com')