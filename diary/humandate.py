from datetime import datetime, timedelta

class HumanDate():

    def pretty_date(self,time=False):

        now = datetime.now()
        if type(time) is int:
            diff = now - datetime.fromtimestamp(time)
        elif isinstance(time, datetime):
            diff = now - time
        elif not time:
            diff = now - now
        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 86400:
                return  " Today"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str( int( day_diff) ) + " days ago"
        if day_diff < 31:
            return str( int( day_diff / 7) ) + " weeks ago"
        if day_diff < 365:
            return str( int( day_diff / 30) ) + " months ago"

        return str( int( day_diff / 365) ) + " years ago"

