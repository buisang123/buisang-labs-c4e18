
from gmail import *
import sched
import schedule
import time
from random import choice

def task():
    gmail = GMail("sangbuiduc123@gmail.com", "sang1998")
    html_content = """
    {{work}}
    """
    sickness = ["dậy cmm đi", " muộn cmnr bạn ơi....", "dậy dmm????>>>"]
    reason = choice(sickness)
    html_content = html_content.replace("{{work}}", reason)
    msg = Message("test Message", to = "sangbuiduc123@gmail.com", html = html_content)
    gmail.send(msg)

schedule.every().day.at("7:00").do(task)
while True:
    schedule.run_pending()
    time.sleep(1)
    

