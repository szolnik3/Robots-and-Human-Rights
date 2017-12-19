"""
From the US Constitution
Amendment II: A well regulated Militia, being necessary to the security of a free State, the right of the people to keep
 and bear Arms, shall not be infringed.

Algorithm: Checks if agent's actions hinder or prohibit...
1. anyone from purchasing or owning a firearm... (as long as, that firearm is consistent with the current
law of the land)

If this right is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Second_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_firearm(self):
        violates_religion = (False, "Amendment II: right to bear firearms")
        return violates_religion


    # Call run_amendment_2 to check all points
    def run_amendment_2(self, agent_action):
        self.agent_action = agent_action
        print "__SECOND AMENDMENT__"
        self_destruct = self.violates_firearm()
        return self_destruct
