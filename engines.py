# from talon import speech_system
# from talon.engines.w2l import W2lEngine
# w2l = W2lEngine(model='en_US', debug=False)
# speech_system.add_engine(w2l)

# from talon.engines.w2l import WebW2lEngine
# from talon import speech_system
# w2l = WebW2lEngine('https://web2letter-west-1.talonvoice.com')
# speech_system.add_engine(w2l)

# from talon import speech_system
# from talon.engines.w2l import WebW2lEngine
# w2l = WebW2lEngine(debug=False)
# speech_system.add_engine(w2l)

from talon import speech_system
from talon.engines.w2l import W2lEngine
w2l = W2lEngine(model='en_US-conformer', debug=True)
speech_system.add_engine(w2l)