from statemachine import StateMachine, State


class GameMachine(StateMachine):
    title = State('Title_Screen', initial=True)
    settings = State('Settings')
    level1 = State('Level_1')
    level2 = State('Level_2')
    leave = State('Exit')

    leaveGame = title.to(leave)
    openSettings = title.to(settings)
    openLevel1 = title.to(level1)
    openLevel2 = title.to(level2)
    goBack = settings.to(title)
    finishLevel1 = level1.to(title)
    finishLevel2 = level2.to(title)


