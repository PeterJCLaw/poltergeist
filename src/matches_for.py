
from datetime import datetime
import sys

import talk
from display_utils import get_delayed_time

req_team = sys.argv[1]

match_data = talk.command_yaml('list-matches 2013-01-01 2014-01-01')
match_data = match_data['matches']

for ident, stamp in match_data:
    dt = datetime.fromtimestamp(stamp)
    dt = get_delayed_time(dt)
    teams_data = talk.command_yaml('get-match-teams {0}'.format(ident))
    #print teams_data
    team_ids = teams_data['teams']
    if not req_team in team_ids:
        continue

    num = ident[6:]
#    print "| {0} | {1} | {2} |".format(dt.time(), num, ' | '.join(team_ids))
    print ident
