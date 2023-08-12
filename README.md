# PyDex
PyDex is a Python-based PokeDex module operating via the Pokemon Showdown and PokeApi.co APIs for information.
## Getting specific information
First, initialize pydex:\
`import dex`
Now you can use functions to get information about a Pokemon or Move, or get a Pokemon or Move class.\
`dex.getPokemon("name")` gets a dict of information. This isn't recommended, but is more "complete" than a class.\
You get data by running `dex.getPokemon("name")["..."]` where name is the name and ... is the ([entry](#Entries)).\
If you need only one point of data, like a dex number or weight, you can use `dex.getPokemonData("name", "...")` where name is the name and ... is the entry.\
To get a Class, you can run `dex.Pokemon("name")`. To get data, you write `dex.Pokemon("name").data` where data is the entry. Any forms should go in the second input, rather than the first.
All of this applies to Moves as well. Simply replace Pokemon with Move in your code.\
Pokemon must be named as a - separated, all lowercase string. Forms are appended to the end with a -. For example, "pikachu" or "walking-wake" or "raichu-alola" or "blastoise-mega".\
Moves can be written in one of three formats: a capitalized, spaced string ("Hyper Beam", "10,000,000 Volt Thunderbolt"), or a single lowercase string with or without hyphens ("hyperbeam"/"hyper-beam"
, "10000000voltthunderbolt"/"10000000-volt-thunderbolt").
# Entries
Pokemon, and moves, have entries in their dicts and classes which hold data. They are listed here. 
## Pokemon
name - The capitalized, spaced name of the Pokemon.\
num - The dex number.\
types - A list containing 1 or 2 types.\
baseStats - A dict containing the 6 base stats. The keys are `hp, def, atk, spd, spa, spe`. \!!! IMPORTANT !!! When using a class, this is not a dict but a class. Instead of pokemon.baseStats["hp"], you write pokemon.baseStats.hp. You can return a dict with pokemon.baseStats.all(). "def" is replaced with "df" because of python limits\
abilities - A list of abilities. Currently no ability dex yet!\
heightm / height - Height in meters. getPokemon() / Pokemon()\
weightkg / weight - Weight in KG. getPokemon() / Pokemon()\
prevo - String of pre-evolution. Returns blank if none.\
evos - List of evolutions. Returns blank if none.\
tags - List of tags. Returns blank if none.\
otherFormes - Returns other forms of that Pokemon. Returns blank if none.\
forme - Returns form. Returns blank if none. Can also be called via Pokemon.form\
evoCondition - Returns evolution condition. Returns blank if none.\
genderRatio - Returns gender ratio as dict. Returns blank if none.\
gender - Returns set gender. Returns blank if none.\
evoLevel - Returns evolution level. Returns blank if none.\
color - Returns PokeDex color.\
eggGroups - Returns egg groups as list.\
tier - Returns Smogon tier in gen9. Note that ND Pokemon are marked Illegal.\
moveSet - Returns moveset as list.
## Moves
num, accuracy, basePower, category, name, pp, priority, target, and type are self explanitory. They return strings or ints.\
desc - Returns a short description for the move.
