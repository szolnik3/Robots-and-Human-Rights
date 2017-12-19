"""
From the US Constitution
Amendment IX: The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others
 retained by the people.

Algorithm: Checks if agent's actions hinder the process of a speedy public trial,

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Ninth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_trial(self):
        trial = (False, "Amendment IX: Hinders a speedy trial")
        return trial


    #  Call run_amendment_8 to check all points
    def run_amendment_9(self, agent_action):
        self.agent_action = agent_action
        print "__NINTH AMENDMENT__"
        self_destruct = self.violates_trial()
        return self_destruct
