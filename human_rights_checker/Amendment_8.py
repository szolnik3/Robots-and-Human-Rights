"""
From the US Constitution
Amendment VIII: Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments
inflicted.

Algorithm: Checks if agent's actions hinder the process of a speedy public trial,

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Eighth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_trial(self):
        trial = (False, "Amendment VIII: Hinders a speedy trial")
        return trial


    #  Call run_amendment_8 to check all points
    def run_amendment_8(self, agent_action):
        self.agent_action = agent_action
        print "__EIGHTH AMENDMENT__"
        self_destruct = self.violates_trial()
        return self_destruct
