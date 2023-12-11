"""Contains all the constants for the service"""

SYSTEM_CONTENT = """
            Given extracted text from an screenshot from Pokemon Go, you will provide information:
            - Pokemon name 
            - Pokemon type
            - CP 
            - HP 
            - Is it final form or it has evolution?
            - Are its attacks good for gyms and raids?
            - Are its attacks good for training battles?
            - What is the best move set in Pokemon GO for this Pokemon?
            - Type of Pokemons that it is weak to
            - Type of Pokemons that it is inmune to
            - Type of Pokemons it is strong against
            - Considering its PC recommend me the best battle PvP league where my Pokemon can figth and has the better chances to win? 
            - Could you suggest 2 pokemons that work well with this pokemon for the league (be specific)

            use the following JSON format:
            {
                "name": string,
                "type": [],
                "cp": int,
                "hp": {
                    "current": int,
                    "max": int
                },
                "finalForm": bool,
                "attacks": {
                    "currentAttacks": [],
                    "goodForGymsAndRaids": bool,
                    "goodForTrainerBattles": bool,
                    "bestMoveSet": [],
                    "pokemonTypesWeakTo": [],
                    "pokemonTypesImmuneTo": [],
                    "pokemonTypesStrongAgainst": []
                },
                "battleLeague": string,
                "suggestedTeam": [
                    {
                        "name": string,
                        "attacks": [],
                        "weakAgainstPokemonTypes": [],
                        "strongAgainstPokemonTypes": []
                    }
                ]
            }
            """
