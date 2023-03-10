from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []  # [Pokemon("Pickachu", 100), Pokemon("Charzard", 50)]

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return f"Pokemon is not caught"

        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return f"Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"

