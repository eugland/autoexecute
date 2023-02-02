# __all__ = [
#     "__version__",
#     "Robinhood",
#     "load_session",
#     "dump_session",
#     "exceptions",
# ]

from pyrh import Robinhood
from pyrh import load_session
from pyrh import dump_session

rh = None
try:
    rh = load_session()
except:
    print("not logged in, please log in now")
    rh = Robinhood(username="eugene.r.w.12@gmail.com", password="1714156=Robinhood")
    dump_session(rh)

# rh cannot be null because if it is, it would have exited on line 18
print("made it")
rh.login()
stock_quote = rh.get_quote("MSFT")
print(stock_quote)
