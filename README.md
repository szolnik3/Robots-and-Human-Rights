# Robots and Human Rights
This program is to check IF the AI agent....
1. Violates any human rights towards the people they interact with...
2. Physically harms any person(s)...
If the agent does, then the agent is stopped.

## Tested action is stored in action.json:
    {
        "agent": "Name",
        "category": "category of action",
        "object": "agent'saction towards object",
        "second parties": "other entities involved"
    }
    
## Abstract Algorithm:
    Scan through each amendment in the bill of rights...
    1. If the action violates any persons then reject the action.
    2. If the action physically harms any persons, destroy (turn off) the agent.

## Instructions
1. Download zip
2. Navigate Terminal to code location
3. In terminal run: python Main_Controller.py
4. write the robot action in Robots-Human-Rights/human-rights-checker/action.json... See action.json for example representation

## Requirements to run
1. Windows
2. Python 2.7

## Personal Concern: 
Each year, AI agents become more intelligent. We humans may have to share this world one day
with AI agents... Do we treat these agents as equals? Should we give agents the same rights as humans? How can we be
sure those agents will treat us with respect? How can they know what rights are? If an agent does NOT know what
human rights are, then how can they respect those human rights? Are we creating AI that one day could enslave our
children? We must be pessimistic about these concerns. We only have one chance to create a perfect world for our
children. The goal of this program is to act as a filter for the AI actions. If an agent's actions violate any rights
laid out in the US Constitution, then the script will reject the agent's actions..

## Contact:

Author: Stephen Zolnik

Github: https://github.com/szolnik3

Email: sjzolnik@hotmail.com

## Example
![tinkerton](https://user-images.githubusercontent.com/10516118/34272819-d2d99bb0-e65f-11e7-94c9-b06dac831e17.PNG)
![tinkerton action1](https://user-images.githubusercontent.com/10516118/34276559-fcf46b5e-e66f-11e7-9169-4ba02123ee0e.PNG)
![tinkerton action representation](https://user-images.githubusercontent.com/10516118/34272662-1daccd3e-e65f-11e7-907e-d569370ef551.PNG)
![algorithm](https://user-images.githubusercontent.com/10516118/34272676-2c573144-e65f-11e7-9f9e-4c034f0447b0.PNG)
![tinkerton result](https://user-images.githubusercontent.com/10516118/34276574-0e563490-e670-11e7-839b-5d6b6430429b.PNG)

