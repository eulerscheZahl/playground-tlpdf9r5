# Using the API with Python

Now that we know how to use the API, let's send some requests with Python!

The following code will download a replay:
@[Python]({"stubs": ["code/download.py"], "command": "code/download.py"})

I recommend to save it to your disk before running a complex analysis. That way you don't have to download it multiple times when your analysis code is buggy at first.

Let's have a closer look at what we just downloaded:
![API_unauth](API_unauth.png)
On the left you see the online version, on the right our downloaded json. The errorstream is missing. We need to login first in order to get it too.

Let's try again, this time with login. This code is intentionally not embedded in a runner, as it needs your login information in order to work properly. It's just for reference and offline execution.
You are expected to extract your cookie of an existing session for this step, as we would have to solve a captcha otherwise.
``` python
import os, json, requests, sys

userID = 1500515 # that's my userID, you have to change it
game_id = 453253378

# the session object saves cookies
with requests.Session() as s:
    session.cookies.set('rememberMe', '01234567-0123-0123-0123-0123456789ab', domain='codingame.com') # change the cookie value, see https://github.com/s-vivien/CGBenchmark#how-to-grab-your-accounts-rememberme
    # the same request as above, but with a session object
    r = s.post('https://www.codingame.com/services/gameResultRemoteService/findByGameId', json = [str(game_id), userID])
    replay = r.json()
    # TODO save your replay
```
