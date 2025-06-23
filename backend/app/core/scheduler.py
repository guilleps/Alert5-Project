from apscheduler.schedulers.background import BackgroundScheduler
from .send_feedback import send_feedback_today

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_feedback_today, 'cron', hour=23, minute=59) # a las 23:59 - al finalizar el día
    scheduler.start()