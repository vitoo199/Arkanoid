import src.states as states

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class GameStates(containers.DeclarativeContainer):
    """IoC container of states ."""

    init_state = providers.Factory(
        states.InitializationState.InitializationState)

    menu_state = providers.Factory(states.MainMenuState.MainMenuState)

    game_playing_state = providers.Factory(
        states.GamePlayingState.GamePlayingState)
