import schedule
import time
from schedule import repeat, every


@repeat(every().minute)
def tarefa():
     print ("GETeam Não Para!")
     print ("Sou o que sou porque somos todos nós!")
     

#schedule.every(5).seconds.do(tarefa)
#schedule.every().hour.at(":10").do(tarefa)
#schedule.every().hour.until(":10").do(tarefa)

while True:
     schedule.run_pending()
     time.sleep(1)