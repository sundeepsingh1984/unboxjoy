from django_cron import CronJobBase, Schedule
from datetime import datetime
from giveaways.models import Giveaway
class SetGiveawayResult(CronJobBase):
    RUN_FIVE_MINS = 5 # every 1 hours

    schedule = Schedule(run_every_mins=RUN_FIVE_MINS)
    code = 'sitesetting.set_giveaway_result'    # a unique code

    def do(self):
        try:
            giveaway_qs=Giveaway.objects.filter(result_announced="False",result_announcement_date__lt=datetime.now()).all()
            giveaway_qs.update(result_announced=True)

        except Exception as e:
            raise e
            pass
        