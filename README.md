This is a toy project to motivate my learning Flask and SQLAlchemy.

I spend a lot of time on IRC.  My IRC client is configured to hide
PART & JOIN notices, because they're annoying.  From time to time, I
find that someone has asked a question that I want to answer, but it
was a few hours ago, and I don't know if they're still in the channel.
Freenode apparently doesn't like `/who` queries.

So this project will run a bot which tracks JOIN & PART notices (in a
few channels I track), and can answer questions about who is in a
channel, or whether a given user is in any channels I frequent, using
a simple scheme of URLs & JSON.

Maybe I'll extend it at some point to provide other services also.

I'm sure someone else has a better solution to this minor annoyance,
which wouldn't help me learn Flask at all.
