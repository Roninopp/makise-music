from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = "7217645"
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"

BOT_TOKEN = getenv("BOT_TOKEN", "6292817735:AAHHVD8I053_nNHyuDVkhWasbSDQ9Sxwaag")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = "1793699293"

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/24e7af2b54c7b36ad9ca7.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQAJcC72R8jQ8HdLbqgkPqA0BNKEyXx6gEljVx5mRfBTGyPAb4RHgxp9gyKBqT15PVRyi-X0npKxK-NkUJSSNN0eNQZ64omlmcvnYwuOzSUumfI5PA8bvocLjjKuEjz5TtiFKPcoEc3oH6badvvKnXAIBlN2-g-mOXijtCbduzylnY5YaYpLiTI8XUrnhj5mW1AfaPOr1WXo8mBo3ysEIfJb6aWrmq15GgZ2fFz_-IQGl8SUKmo_hFPIWp6FdFeAJpeLJS-5mDVnjHJjFEGLu1OqmTV10OJzuRHsig0Knn3nHagTtUK2dNQSmq8u_CM5g1pcIe7uglnzAhHsDMcEDp61AAAAAUK509kA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Samurai_Botsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Teamsamuraii")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293 1109460378").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
