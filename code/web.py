from talon import Context, Module
from user.utils import utilities


mod = Module()
ctx = Context()
mod.list("websites", desc="Websites")
ctx.lists["user.websites"] = {
    "e-mail": "https://mail.google.com/mail/ca/u/0/#inbox",
    "math fly": "mathfly.org",
    "what's app": "https://web.whatsapp.com/",
    "amazon": "https://smile.amazon.co.uk/ref=nav_logo",
    "calendar": "https://www.google.com/calendar",
    "facebook": "facebook.com",
    "iPlayer": "https://www.bbc.co.uk/iplayer",
    "kindle": "https://smile.amazon.co.uk/Kindle-eBooks-books/b/ref=nav_shopall_kbo5?ie=UTF8&node=341689031",
    "maps": "https://www.google.com/maps",
    "scholar": "scholar.google.co.uk",
    "SMS": "https://mightytext.net/web8/",
    "times": "thetimes.co.uk",
    "twitter": "twitter.com/home",
    "youtube": "youtube.com",
}
