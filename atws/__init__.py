from pytz import timezone
from wrapper import connect
from query import Query
ATWS_API_TIMEZONE = timezone('US/Eastern')
ATWS_ENTITY_SEND_LIMIT = 200
ATWS_ENTITY_RECEIVE_LIMIT = 500