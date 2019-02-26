import cc_dat_utils
import json
import cc_data



#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data



def convert_json_to_dat(json_file):

    game_data = cc_data.CCDataFile()
    for level in json_file["levels"]:
        game_level = cc_data.CCLevel()
        game_level.level_number = level["level number"]
        game_level.time = level["time"]
        game_level.num_chips = level["chip number"]
        game_level.upper_layer = level["upper layer"]
        optional_fields_json = level["optional fields"]

        for something in optional_fields_json:
            if something["id"] == "title":
                title = cc_data.CCMapTitleField(something["level title"])
                game_level.add_field(title)
            elif something["id"] == "password":
                password = cc_data.CCEncodedPasswordField(something["encoded password"])
                game_level.add_field(password)
            elif something["id"] == "hint":
                hint = cc_data.CCMapHintField(something["hint text"])
                game_level.add_field(hint)
            elif something["id"] == "monsters":
                coordinates = []
                for coordinate in something["monsters"]:
                    x = coordinate[0]
                    y = coordinate[1]
                    coord = cc_data.CCCoordinate(x,y)
                    coordinates.append(coord)


        game_data.add_level(game_level)
    return game_data




with open("data/emcdonal_cc1.json", "r") as reader:
    json_game = json.load(reader)
game = convert_json_to_dat(json_game)
print(game)

cc_dat_utils.write_cc_data_to_dat(game, "data/emcdonal_cc1.dat")

