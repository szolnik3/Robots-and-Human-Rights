"""
From the US Constitution
Amendment III: Quartering of Soldiers. No Soldier shall, in time of peace be quartered in any house, without the consent
 of the Owner, nor in time of war, but in a manner to be prescribed by law.

Algorithm: Checks if agent's actions causes it to enter a house without the owner's consent...

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Third_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_firearm(self):
        violates_religion = (False, "Amendment III: Quartering of Soldiers")
        return violates_religion


    # Call run_amendment_2 to check all points
    def run_amendment_3(self, agent_action):
        self.agent_action = agent_action
        print "__THIRD AMENDMENT__"
        self_destruct = self.violates_firearm()
        return self_destruct
