from selenium import webdriver
from win10toast import ToastNotifier
import time
import winsound


file = open('examples.txt','r')

lines = file.readlines()
print("Opening Browser ...")
driver = webdriver.Firefox()
print("Loading Page ...")
driver.get("https://pdfmyurl.com/")
print("Page Loaded")

for line in lines: 
    
    tf = driver.find_element_by_name("url")
    tf.send_keys(line)
    btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/form/div[1]/div/span/button')
    btn.click()
    time.sleep(40)
    print("[Downloaded] "+line[25:])
    driver.get("https://pdfmyurl.com/")



toast = ToastNotifier()
winsound.Beep(500, 850)
toast.show_toast("Files Downloaded","All Files Downloaded Successfully",duration=20,icon_path=None)
input("Press Enter to Exit")
driver.quit()


