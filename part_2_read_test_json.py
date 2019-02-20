import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    game_library.game = json_data["games"]
    for game_data in json_data["games"]:

        game = test_data.Game()
        game.title = game_data["Title"]
        game.year = game_data["Year"]

        for platform_stuff in game_data:
            game.platform = test_data.Platform()
            game.platform.name = platform_stuff[1]
            game.platform.launch_year = platform_stuff[0]


        game_library.add_game(game)


    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"


with open("data/test_data.json", "r") as reader:
    loaded_json = json.load(reader)

GameLibrary = make_game_library_from_json(loaded_json)
print(GameLibrary)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
