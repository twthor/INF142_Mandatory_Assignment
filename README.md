# INF142 Mandatory Assignment
Repository for mandatory assignment in INF142 Computer Networks.
**Mandatory Assignment group 16**: Tobias With Thorsen and Sofia Burkow.

To run the scripts in correct order:
  - run "python db.py"
  - run "python server.py"
  - run to separate "python client.py"
  - And you should be good to go!

## Project's purpose:
The aim is to build an architecture that transform the game "Team Local Tactis" (TLT) from a local version to an distributed application that allows for online play between several clients, and change the name to "Team Network Tactics" (TNT).

TNT needs at least three processes that communicates oves the Internet:
  - A database for storing champions and stats
  - A server running the logic of the game
  - A client for the players.

The three processes needs to run without any isolation and in the same device using local host. It should also allow for patching champions (changes to champions stats, nerfs/buffs) while still allowing players to play the game. 

### Architecture example:
![image](https://user-images.githubusercontent.com/92455258/157851960-e50dc711-dd18-40d4-99ec-dbca36fdf42d.png)

## MVP requirements:
  • It consists of at least three Python scripts, one for each of the aforementioned
    processes.
  • Socket programming is used.
  • Data associated to champions, match history or other stats must persist in a database
    or in a file.


## License

MIT
