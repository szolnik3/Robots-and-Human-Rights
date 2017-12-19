"""
From the US Constitution
Amendment V: No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or
indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual
service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in
jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived
of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without
just compensation.

Algorithm: Checks if agent's actions causes it to enter a house without the owner's consent...

If this amendment is violated by the agent's actions:
    return True
Else:
    return False

Author: Stephen Zolnik
Github: https://github.com/szolnik3
Email: sjzolnik@hotmail.com
"""


class Fifth_Amendment:
    def __init__(self):
        self.agent_action = {}

    def violates_Fifth(self):
        violates_religion = (False, "Amendment V: Quartering of Soldiers")
        return violates_religion


    # Call run_amendment_5 to check all points
    def run_amendment_5(self, agent_action):
        self.agent_action = agent_action
        print "__FIFTH AMENDMENT__"
        self_destruct = self.violates_Fifth()
        return self_destruct
