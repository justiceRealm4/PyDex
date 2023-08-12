import requests
import json
dex_API = requests.get('https://play.pokemonshowdown.com/data/pokedex.json')
move_API = requests.get('https://play.pokemonshowdown.com/data/moves.json')
pokemove_API = None
movedata = move_API.text
dexdata = dex_API.text
dparse_json = json.loads(dexdata)
mparse_json = json.loads(movedata)
pokemon = dparse_json
moves = mparse_json
def getPokemon(pokemon = []): # Get everything for a Pokemon or Forme
    active_case = dparse_json[pokemon]
    return active_case
def getPokemonData(pokemon = [], data = []): # Get a specific point about a specific Pokemon or Forme
    active_case = dparse_json[pokemon][data]
    return active_case
def getMove(move = []):
    active_case = mparse_json[move.replace('-', '')]
    return active_case
def getMoveData(move = [], data = []):
    active_case = mparse_json[move][data]
    return active_case

class Move:
    def __init__(self, move):
        self.move = move
        self.mv = []
        if move in list(mparse_json.keys()):
            self.mv = getMove(move)
        elif move.replace('-', '') in list (mparse_json.keys()):
            self.mv = getMove(move.replace('-', ''))
        else:
            for mx in range(0,len(mparse_json)):
                if list(mparse_json.values())[mx]["name"] == move:
                    self.mv = getMove(list(mparse_json.keys())[mx])
        if self.mv == []:
            self.move = None
            print("No move")
            return
        self.num = self.mv["num"]
        self.accuracy = self.mv["accuracy"]
        self.basePower = self.mv["basePower"]
        self.category = self.mv["category"]
        self.name = self.mv["name"]
        self.pp = self.mv["pp"]
        self.priority = self.mv["priority"]
        self.target = self.mv["target"]
        self.type = self.mv["type"]
        self.desc = self.mv["shortDesc"]
class Pokemon: # .
    def __init__(self, poke, form = ""):
        if form == "":
            self.pokeMove_API = requests.get('https://pokeapi.co/api/v2/pokemon/' + poke)
        else:
            self.pokeMove_API = requests.get('https://pokeapi.co/api/v2/pokemon/' + poke + '-' + form)
        self.pokeMove = self.pokeMove_API.text
        self.pMParse = json.loads(self.pokeMove)
        if form == "":
            self.pkmn = getPokemon(poke)
            self.pkmnFormless = self.pkmn
        else:
            self.pkmn = getPokemon(poke + form)
            self.pkmnFormless = getPokemon(poke)
        self.name = self.pkmn["name"]
        self.num = self.pkmn["num"]
        self.types = self.pkmn["types"]
        self.baseStats = baseStats(self.pkmn["baseStats"])
        self.abilities = self.pkmn["abilities"]
        self.height = self.pkmn["heightm"]
        self.weight = self.pkmn["weightkg"]
        self.prevo = []
        if "prevo" in self.pkmnFormless:
            self.prevo = self.pkmnFormless["prevo"]
        self.evos = []
        if "evos" in self.pkmnFormless:
            self.evos = self.pkmnFormless["evos"]
        self.tags = []
        if "tags" in self.pkmn:
            self.tags = self.pkmn["tags"]
        self.otherFormes = []
        if "otherFormes" in self.pkmnFormless:
            self.otherFormes = self.pkmnFormless["otherFormes"]
        self.forme = ""
        if "forme" in self.pkmn:
            self.forme = self.pkmn["forme"]
        self.evoCondition = ""
        if "evoCondition" in self.pkmnFormless:
            self.evoCondition = self.pkmnFormless["evoCondition"]
        self.genderRatio = ""
        if "genderRatio" in self.pkmnFormless:
            self.genderRatio = self.pkmnFormless["genderRatio"]
        self.gender = ""
        if "gender" in self.pkmnFormless:
            self.gender = self.pkmnFormless["gender"]
        self.evoLevel = 0
        if "evoLevel" in self.pkmnFormless:
            self.evoLevel = self.pkmnFormless["evoLevel"]
        self.color = self.pkmn["color"]
        self.eggGroups = self.pkmn["eggGroups"]
        self.tier = self.pkmn["tier"]
        self.moveSet = []
        for x in range(0, len(self.pMParse['moves'])):
            self.moveSet.append(self.pMParse['moves'][x]['move']['name'])
    def all(self):
        return self.pkmn
    def canLearn(self, move:str | Move):
        if type(move) is str:
            return move in self.moveSet
        else:
            return move.move in self.moveSet
class baseStats:
    def __init__(self, baseStats):
        self.baseStats = baseStats
        self.total = baseStats["hp"] + baseStats["def"] + baseStats["atk"] + baseStats["spd"] + baseStats["spa"] + baseStats["spe"]
        self.hp = baseStats["hp"]
        self.df = baseStats["def"]
        self.atk = baseStats["atk"]
        self.spd = baseStats["spd"]
        self.spa = baseStats["spa"]
        self.spe = baseStats["spe"]
        
    def all(self):
        return self.baseStats