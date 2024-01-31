# FIFA Player Data Migration

Welcome to the FIFA Player Data Migration project! This Python-based tool is designed to bridge the gap between recent FIFA game releases and their older counterparts by enabling the transfer of player data. As avid FIFA enthusiasts ourselves, we often find the nostalgia of older titles irresistible but miss the updated player statistics and attributes introduced in more recent releases. This project serves as a solution, allowing users to effortlessly migrate player data from newer FIFA games to their favorite classics. The script leverages Python's capabilities to extract, transform, and load player information, ensuring that the gaming experience remains dynamic and up-to-date across different FIFA editions.

# Usage Guide

To utilize this tool, you'll first need to download the Revolution Database Master 23 program. Using this program, open the Squad file of your target game (e.g., FIFA 23) and select the "players" table from the left. Generate a players.txt file by choosing "Export Simple Table" from the top menu. Repeat these steps for your own game (e.g., FIFA 21).

Revolution Database Master 23: https://dl.fifa-infinity.com/fifa-23/revolution-db-master-23/  (Credits to Rinaldo & Fidel)              
(If you have any issue running the RDBM 23, use this download link instead https://mega.nz/file/NiRU1KqZ#4v4XLjBPCTPnhXgN1lQISbMuz3zCBx1Zed_r3claAAU)

![image](https://github.com/farukgnc/FIFA-Player-Data-Migration/assets/45713670/9879d81a-131b-4df3-8c15-a6e9b8344a5a)

Next, use these two files and our Python application to create a new text file that transfers player attributes from the latest game to your played version. To apply this file to your game, open the current game in the RDBM application, navigate to the "players" table, and choose "Import Single Table," selecting the output text file. If no errors occur, you've performed the steps correctly. Finally, click the "Save" button in the top-left corner to complete the process. Now, all that's left is to jump into the game and load the squad file you've just modified. Enjoy your upgraded gaming experience!

![image](https://github.com/farukgnc/FIFA-Player-Data-Migration/assets/45713670/737540df-d022-4672-b744-6f0522a49f34)


# Additional Details

For a successful data transfer, it's crucial that both squad files belong to the same game versions, considering whether the game is modded or unmodded. For instance, if one squad file is tailored for mods like FIFER or EEP, refrain from transferring that data to an unmodded squad file. Another important detail to note is that when transferring data from the new game to the old one, only the attributes of players present in the older game are updated. In other words, if a player exists in the new game but not in the old one, they won't be added.

Furthermore, as of now, this project specifically focuses on updating player attributes. However, using similar methods, it's possible to extend this functionality to update almost all data within squad file. Stay tuned for potential expansions in the future!
