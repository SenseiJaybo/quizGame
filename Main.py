import eventmanager
import Model
import Controller
import View

evManager = eventmanager.EventManager()
gamemodel = Model.GameEngine(evManager)
keyboard = Controller.Keyboard(evManager, gamemodel)
graphics = View.GraphicalView(evManager, gamemodel)
gamemodel.run()
