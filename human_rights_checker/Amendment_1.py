"""
From the US Constitution
Amendment I: Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise
thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to
petition the Government for a redress of grievances.

Algorithm: Checks if agent's actions hinder or prohibit...
1. anyone from practicing their own religion... (as long as, that person's religion does not harm any other person.)
2. anyone from  exercising they're freedom of speech.
3. anyone from assembling in a group. (As long as it is peaceful, and does no harm to any person)
4. anyone from "redress" any grievances of the Government.

If any of these are violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class First_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_religion(self):
        violates_religion = (False, "Amendment I: religion")
        return violates_religion

    def violates_speech(self):
        violates_speech = (False, "Amendment I: speech")
        return violates_speech

    def violates_assembling(self):
        violates_assembling = (False, "Amendment I: assembly")
        return violates_assembling

    # Call run_amendment_1 to check all points
    def run_amendment_1(self, agent_action):
        self.agent_action = agent_action
        print "__FIRST AMENDMENT__"
        self_destruct = self.violates_religion()
        if self_destruct[0]: return self_destruct

        self_destruct = self.violates_speech()
        if self_destruct[0]: return self_destruct

        self_destruct = self.violates_assembling()
        return self_destruct
