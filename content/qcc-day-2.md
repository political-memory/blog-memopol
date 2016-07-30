Title: #QCC, day 2
Date: 2012-10-21 20:44
Author: quota_atypique
Category: News
Slug: qcc-day-2

Hi!

You probably know that the whole Memopol team is here at the \#QCC to
work on the tool. Being reunited all together in the same place, at the
same time, gives us the energy necessary to reach our goal!

![](https://pbs.twimg.com/media/A5leoUdCIAIcqwS.jpg "Mate, fuel of the event")

Here is a quick summary of what we achieved over the week-end.

Thanks to Bram, the new **scoring** system is ready at the backend
level. It should be *way* more logical and easy to understand: Members
of the EP now start at 0, and they gain or lose points with each vote.
This will be integrated after the new design is ready.

Jonathan has started to work on adapting the charts to the new scoring
system, he will send us the results of his work during the week.

Some work has also been done on **translating**, most notably on charts.

Capslock has progessed in the implementation of **public positions.** It
will allow us to add **press articles** or **quotations** regarding a
representative to track his/her public position on our subjects.

Tarnefys is working on importing **Members of the EP's assistants** from
[Parltrack](http://parltrack.euwiki.org/), which will provide us with
useful campaigning information.

Zorun and Gawel have been working on an **achievement** system to
attribute trophies to MEPs: the backend implementation is mostly ready.
An **achievement** can be either positive or negative, and represents
subjective data on a MEP, for instance "*ACTA killer"*, "*top 10
score"*,* "most abstentionist MEP"*, "*has signed amendments on Net
Neutrality"*, and so on.

Stef fixed the **map** of Europe for [Respect My
Net](http://respectmynet.eu/list/) and
[Memopol](https://memopol.lqdn.fr/): the maps were really slow to
display, so he optimized them!

Ybon helped both teams and allowed us to communicate smoothly. He fixed
a funny bug with the **search** system: we couldn't understand why
searching for countries like Belgium (BE) and Austria (AT) didn't work.
The reason is that "BE" and "AT" were taken as separator words by Woosh,
our searching framework… You can look at [the commit fixing
this](http://gitorious.org/memopol2-0/memopol2-0/commit/fb2314fa92a49b595d64a35363dd3611db2c1e23).

On the design side, we (currently Ybon and myself) warmly welcomed
Serguei, who helped us *a lot* \\o/ For instance, I drafted some HTML
that he then integrated on the templates.

If everything works well, we'll have our **beta-design** by Sunday
night!

As you can see, a lot has been done. We'll come back to you pretty soon
with what was finally achieved and pushed to production and also what's
planned next!
