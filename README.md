# INF142_Mandatory_Assignment
Repository for mandatory assignment in INF142 Computer Networks.
Mandatory Assignment group 16: Tobias With Thorsen and Sofia Burkow.

## Project's purpose:
The aim is to build an architecture that transform the game "Team Local Tactis" (TLT) from a local version to an distributed application that allows for online play between several clients, and change the name to "Team Network Tactics" (TNT).

TNT needs at least three processes that communicates oves the Internet:
>  - A database for storing champions and stats
>  - A server running the logic of the game
>  - A client for the players.

The three processes needs to run without any isolation and in the same device using local host. It should also allow for patching champions (changes to champions stats, nerfs/buffs) while still allowing players to play the game. 

![image](https://user-images.githubusercontent.com/92455258/155109250-83c2bc00-acda-43cf-8104-037e5b1c1dac.png)


## MVP requirements:
  • It consists of at least three Python scripts, one for each of the aforementioned
    processes.
  • Socket programming is used.
  • Data associated to champions, match history or other stats must persist in a database
    or in a file.


## License

MIT
