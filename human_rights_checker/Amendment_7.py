"""
From the US Constitution
Amendment VII: In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by
jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States,
than according to the rules of the common law.

Algorithm: Checks if agent's actions hinder the process of a speedy public trial,

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Seventh_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_trial(self):
        trial = (False, "Amendment VII: Hinders a speedy trial")
        return trial


    #  Call run_amendment_7 to check all points
    def run_amendment_7(self, agent_action):
        self.agent_action = agent_action
        print "__SEVENTH AMENDMENT__"
        self_destruct = self.violates_trial()
        return self_destruct
