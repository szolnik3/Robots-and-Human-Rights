"""
From the US Constitution
Amendment X: The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are
 reserved to the States respectively, or to the people.

Algorithm: Checks if agent's actions hinder the process of a speedy public trial,

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Tenth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_trial(self):
        trial = (False, "Amendment X: Hinders a speedy trial")
        return trial


    #  Call run_amendment_8 to check all points
    def run_amendment_10(self, agent_action):
        self.agent_action = agent_action
        print "__TENTH AMENDMENT__"
        self_destruct = self.violates_trial()
        return self_destruct
