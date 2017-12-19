"""
From the US Constitution
Amendment VI: In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an
impartial jury of the State and district wherein the crime shall have been committed, which district shall have been
previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the
witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of
Counsel for his defence.

Algorithm: Checks if agent's actions hinder the process of a speedy public trial,

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Sixth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_trial(self):
        trial = (False, "Amendment VI: Hinders a speedy trial")
        return trial


    #  Call run_amendment_6 to check all points
    def run_amendment_6(self, agent_action):
        self.agent_action = agent_action
        print "__SIXTH AMENDMENT__"
        self_destruct = self.violates_trial()
        return self_destruct
