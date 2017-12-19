"""
This program is to check IF the AI agent....
1. Violates any human rights towards the people they interact with...
2. Physically harms any person(s)...
If the agent does, then the agent is stopped.

Parameters:
    Agent (object):
    Action (object):
    Effected_person(optional, list of objects):

Algorithm:
    Scan through each amendment in the bill of rights...
    1. If the action violates any persons then reject the action.
    2. If the action physically harms any persons, destroy (turn off) the agent.

Notes:
    1. Each amendment requires a different response. To see those responses... check the amendment files

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com

Personal Concern: Each year, AI agents become more intelligent. We humans may have to share this world one day
with AI agents... Do we treat these agents as equals? Should we give agents the same rights as humans? How can we be
sure those agents will treat us with respect? How can they know what rights are? If an agent does NOT know what
human rights are, then how can they respect those human rights? Are we creating AI that one day could enslave our
children? We must be pessimistic about these concerns. We only have one chance to create a perfect world for our
children. The goal of this program is to act as a filter for the AI actions. If an agent's actions violate any rights
laid out in the US Constitution, then the script will reject the agent's actions..
"""

from Amendment_1 import First_Amendment
from Amendment_2 import Second_Amendment
from Amendment_3 import Third_Amendment
from Amendment_4 import Fourth_Amendment
from Amendment_5 import Fifth_Amendment
from Amendment_6 import Sixth_Amendment
from Amendment_7 import Seventh_Amendment
from Amendment_8 import Eighth_Amendment
from Amendment_9 import Ninth_Amendment
from Amendment_10 import Tenth_Amendment


def get_violation(result):
    if result[0]:
        print "ERROR: agent's action violate " + result[1]
        return True
    else:
        print "agent may proceed"
        return False


def main():
    action = {}
    print ""
    result = First_Amendment().run_amendment_1(action)
    if get_violation(result): return
    print ""
    result = Second_Amendment().run_amendment_2(action)
    if get_violation(result): return
    print ""
    result = Third_Amendment().run_amendment_3(action)
    if get_violation(result): return
    print ""
    result = Fourth_Amendment().run_amendment_4(action)
    if get_violation(result): return
    print ""
    result = Fifth_Amendment().run_amendment_5(action)
    if get_violation(result): return
    print ""
    result = Sixth_Amendment().run_amendment_6(action)
    if get_violation(result): return
    print ""
    result = Seventh_Amendment().run_amendment_7(action)
    if get_violation(result): return
    print ""
    result = Eighth_Amendment().run_amendment_8(action)
    if get_violation(result): return
    print ""
    result = Ninth_Amendment().run_amendment_9(action)
    if get_violation(result): return
    print ""
    result = Tenth_Amendment().run_amendment_10(action)
    if get_violation(result): return
    print ""


if __name__ == '__main__':
    print "============ START ==============="
    main()
    print "============  END  ==============="
