"""
From the US Constitution
Amendment IIII: The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable
 searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath
 or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.

Algorithm: Checks if agent's actions...
1. Require a search warrant
2. if search warrant is required, then does agent have search warrant

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Fourth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def search_warrant_required(self):
        return True

    def agent_has_no_warrant(self):
        violates_warrant = (False, "Amendment V: Search Warrant Required")
        return violates_warrant

    # Call run_amendment_4 to check all points
    def run_amendment_4(self, agent_action):
        self.agent_action = agent_action
        print "__Fourth AMENDMENT__"

        self_destruct = self.search_warrant_required()
        if self_destruct:
            self_destruct = self.agent_has_no_warrant()
        return self_destruct
