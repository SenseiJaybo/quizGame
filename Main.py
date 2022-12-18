from MVC import Model, Controller, View, eventmanager

evManager = eventmanager.EventManager()
gamemodel = Model.GameEngine(evManager)
keyboard = Controller.Keyboard(evManager, gamemodel)
graphics = View.GraphicalView(evManager, gamemodel)
gamemodel.run()
