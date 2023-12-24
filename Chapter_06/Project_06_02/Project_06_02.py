"""
Zombie Dice Bots
Programming games are a game genre where instead of playing a game
directly, players write bot programs to play the game autonomously. I’ve
created a Zombie Dice simulator, which allows programmers to practice
their skills while making game-playing AIs. Zombie Dice bots can be simple
or incredibly complex, and are great for a class exercise or an individual
programming challenge.
Zombie Dice is a quick, fun dice game from Steve Jackson Games. The
players are zombies trying to eat as many human brains as possible without
getting shot three times. There is a cup of 13 dice with brains, footsteps,
and shotgun icons on their faces. The dice icons are colored, and each
color has a different likelihood of each event occurring. Every die has two
sides with footsteps, but dice with green icons have more sides with brains,
red-icon dice have more shotguns, and yellow-icon dice have an even split of
brains and shotguns. Do the following on each player’s turn:
1. Place all 13 dice in the cup. The player randomly draws three dice from
the cup and then rolls them. Players always roll exactly three dice.
2. They set aside and count up any brains (humans whose brains were
eaten) and shotguns (humans who fought back). Accumulating three
shotguns automatically ends a player’s turn with zero points (regardless
of how many brains they had). If they have between zero and two shotguns,
 they may continue rolling if they want. They may also choose to
end their turn and collect one point per brain.
3. If the player decides to keep rolling, they must reroll all dice with
footsteps. Remember that the player must always roll three dice; they
must draw more dice out of the cup if they have fewer than three footsteps to roll.
 A player may keep rolling dice until either they get three
shotguns—losing everything—or all 13 dice have been rolled. A player
may not reroll only one or two dice, and may not stop mid-reroll.
4. When someone reaches 13 brains, the rest of the players finish out the
round. The person with the most brains wins. If there’s a tie, the tied
players play one last tiebreaker round.
Zombie Dice has a push-your-luck game mechanic: the more you reroll
the dice, the more brains you can get, but the more likely you’ll eventually
accrue three shotguns and lose everything. Once a player reaches 13 points,
the rest of the players get one more turn (to potentially catch up) and the
game ends. The player with the most points wins. You can find the complete
rules at https://github.com/asweigart/zombiedice/.

Install the zombiedice module with pip by following the instructions in
Appendix A. You can run a demo of the simulator with some pre-made bots
by running the following in the interactive shell:
>> import zombiedice
>> zombiedice.demo()
Zombie Dice Visualization is running. Open your browser to http://
localhost:51810 to view it.
Press Ctrl-C to quit.
The program launches your web browser, which will look like Figure 6-1.

You’ll create bots by writing a class with a turn() method, which is
called by the simulator when it’s your bot’s turn to roll the dice. Classes
are beyond the scope of this book, so the class code is already set up for
you in the myzombie.py program, which is in the downloadable ZIP file for
this book at https://nostarch.com/automatestuff2/. Writing a method is essentially
the same as writing a function, and you can use the turn() code in the
myZombie.py program as a template. Inside this turn() method, you’ll call
the zombiedice.roll() function as often as you want your bot to roll the dice.
import zombiedice
class MyZombie:
 def __init__(self, name):
 # All zombies must have a name:
 self.name = name
 def turn(self, gameState):

# gameState is a dict with info about the current state of the game.
 # You can choose to ignore it in your code.
 diceRollResults = zombiedice.roll() # first roll
 # roll() returns a dictionary with keys 'brains', 'shotgun', and
 # 'footsteps' with how many rolls of each type there were.
 # The 'rolls' key is a list of (color, icon) tuples with the
 # exact roll result information.
 # Example of a roll() return value:
 # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
 # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
 # ('green', 'shotgun')]}
 # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
 brains = 0
 while diceRollResults is not None:
 brains += diceRollResults['brains']
 if brains < 2:
 diceRollResults = zombiedice.roll() # roll again
 else:
 break
zombies = (
 zombiedice.examples.RandomCoinFlipZombie(name='Random'),
 zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
 zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2
Shotguns', minShotguns=2),
 zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1
Shotgun', minShotguns=1),
 MyZombie(name='My Zombie Bot'),
 # Add any other zombie players here.
)
# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
The turn() method takes two parameters: self and gameState. You can
ignore these in your first few zombie bots and consult the online documentation
for details later if you want to learn more. The turn() method should
call zombiedice.roll() at least once for the initial roll. Then, depending on
the strategy the bot uses, it can call zombiedice.roll() again as many times
as it wants. In myZombie.py, the turn() method calls zombiedice.roll() twice,
which means the zombie bot will always roll its dice two times per turn
regardless of the results of the roll.
The return value of zombiedice.roll() tells your code the results of
the dice roll. It is a dictionary with four keys. Three of the keys, 'shotgun',
'brains', and 'footsteps', have integer values of how many dice came up
with those icons. The fourth 'rolls' key has a value that is a list of tuples for
each die roll. The tuples contain two strings: the color of the die at index 0
and the icon rolled at index 1. Look at the code comments in the turn()
method’s definition for an example. If the bot has already rolled three shotguns,
 then zombiedice.roll() will return None.
Try writing some of your own bots to play Zombie Dice and see how they
compare against the other bots. Specifically, try to create the following bots:
•	 A bot that, after the first roll, randomly decides if it will continue
or stop
•	 A bot that stops rolling after it has rolled two brains
•	 A bot that stops rolling after it has rolled two shotguns
•	 A bot that initially decides it’ll roll the dice one to four times, but will
stop early if it rolls two shotguns
•	 A bot that stops rolling after it has rolled more shotguns than brains
Run these bots through the simulator and see how they compare
to each other. You can also examine the code of some premade bots at
https://github.com/asweigart/zombiedice/. If you find yourself playing this game
in the real world, you’ll have the benefit of thousands of simulated games
telling you that one of the best strategies is to simply stop once you’ve rolled
two shotguns. But you could always try pressing your luck . . .

@author Sharaf Qeshta
"""

import zombiedice

class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # The code logic for your zombie goes here:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class AlwaysRollsTwicePerTurn:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        zombiedice.roll()
        zombiedice.roll()


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    AlwaysRollsTwicePerTurn(name='Rolls Twice'),
    # Add any other zombie players here.
)


zombiedice.runWebGui(zombies=zombies, numGames=1000)