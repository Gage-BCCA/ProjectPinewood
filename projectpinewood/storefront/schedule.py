from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django.utils.timezone import now
import logging

from storefront.etsy_api import get_etsy_products


def update_etsy_listings():
    try:
        get_etsy_products()
    except Exception:
        print(f"There was an error: {Exception}")


def api_refresh_schedule():
    x = 15 #Adjust to however often you want it to run
    schedule = BackgroundScheduler()
    schedule.add_jobstore(DjangoJobStore(), "default")
    schedule.add_job(
        update_etsy_listings,
        trigger = IntervalTrigger(minutes = x),
        id = "update_etsy_products",
        replace_existing = True
    )

    schedule.start()