# The Best (not) Objective (not) GGST Tier List :3

Buckle up boys and girls and we're going in for a journey for why these stats really aren't a good way to make Tier Lists!

So I saw that [one post on reddit](https://www.reddit.com/r/Guiltygear/comments/1d8yhdh/tier_list_using_puddlefarm_top_1000_data_s_is_for/) and I was like, damn that sounds so
wrong. So I decided to take a crack at it using only the TOP TIER statistical methods frfr :)))

## The Methodology

Starting off, the main glaring thing I saw was that they chose to use the Top 1000 people. The variance in skill level of the Top 1000 is so big like what the fuck. Different
characters are good at different skill levels, e.g. Pot whose good in lower levels due to his tanky-ness and overall damage, but falls off at higher levels where he struggles with
getting in & starting his scary pressure. Even I think that the Top 100 people is a bit too big too but that's in hindsight (yayyy p-hacking)!

Thus, now the problem is: how do we even get the top 100 matches? Rating Update/Puddle gives a VERY poor view so we have to scrape it ourselves. Luckily, ever since it's been down
they haven't wiped their past games database so we're going to be using that! Note: we're using top 100 from RU because Puddle is too new to make any definite conclusions ^-^.
Check out `collect_t100.py` and `collect_t100_mu.py` for the scripts I used to collect these, and `clean_t100_mu.py` where I cleaned them up.

On a side tangent, we can look at the total # of matches in the top 100 played:

| Character  | Matches Played |
|------------|----------------|
| ABA        | 2628           |
| ANJI       | 43280          |
| ASUKA      | 44892          |
| AXL        | 41608          |
| BAIKEN     | 43778          |
| BEDMAN     | 31255          |
| BRIDGET    | 36991          |
| CHIPP      | 36846          |
| ELPHELT    | 38216          |
| FAUST      | 50670          |
| GIOVANNA   | 46213          |
| GOLDLEWIS  | 39117          |
| HAPPY CAOS | 26886          |
| INO        | 39694          |
| JACK-O     | 38187          |
| JOHNNY     | 51707          |
| KY         | 48166          |
| LEO        | 35715          |
| MAY        | 45444          |
| MILLA      | 29707          |
| NAGORIYUKI | 39300          |
| POTEMKIN   | 59133          |
| RAM        | 24305          |
| SIN        | 30191          |
| SLAYER     | 5235           |
| SOL        | 47326          |
| TESTAMENT  | 31291          |
| ZATO       | 27113          |

Even just looking at these you can see that ABA and Slayer have drastically lower matches played compared to the rest of the cast, so we will discard them accordingly. 

ANYWAYS, back to the methodology. After we gathered this, we should ensure that every character is represented evenly. (I forgot to code it up since I used the python console) BUTTTTTT for each character, we essentially measured how many matches against each other character that they played, and then took the STD Deviation of that set. Then we divided it by the mean to get a [Coefficient of Variation](https://en.wikipedia.org/wiki/Coefficient_of_variation) and found that all characters had a coefficient of ~0.3. (Note: I'm not too sure if this verification is correct but it is what it is.)

So now that's that, let's get to BOOTSTRAPPING (whooo... anyone?). Basically since we don't know the actual distribution of stuff, I decided to bootstrap these to get a 95% Confidence Interval for the expected win percentage. You can check the code out at `bootstrap_ci.py`. 

After some more math later, I just took the median win % and then used a k-means algorithm to group them. (Don't bully me, I was too lazy to k-means with Python and I know R so that's that). Using the elbow method, we can say that there should be ~3-4 groups (I'm using 4 because fuck you that's why) and then sorted all of them by their approx win percentage. 

Now finally, after all that explanation, here's the final tier list!!!

![The Objective Tier List]('objective'%20tier%20list%20._.%20%20.png)

## My Thoughts

In hindsight, I also should've just controlled for >1700 in rating since there's some f10 players in the t100 which brought down Ram's score a bunch. I also may want to control for people of similar ratings but that's for another day and I'm too hungry to continue thinking about it more.

Honestly, seeing this tier list only further reinforces the idea that using RU to make a tier list is bogus in many ways.

## Why this is not a good way of creating tier lists

What these websites (RU/Puddle) measure is the *win* rate, not how good each character is. Although these things may be correlated, there's too many confounding variables (ex skill level, mu knowledge, etc) which makes it a very poor measure of "good"-ness.

### Some extra notes

In addition, there's the whole thing about what do tier lists even measure? Do they measure how good they are at top levels of play? Or do they measure characters overall? For example look at Happy Chaos. At lower levels of play he's very tough to get down. It's only at higher levels of play where his dominance starts to shine through and he shoots up in 'op'-ness. 

Another point to make is that RU (I will refer to Puddle as RU since it's easier) is trying to bring a ranking system into a game whose online matchmaking system runs completely counter to it. Players can accept or decline matches based on the other person's character, giving a potential skew in data. 

More specific to this tier list, I'm guessing (but it's highly likely) that OP used the 'adjusted' win %. This only further muddles the (already) kinda shitty data which clouds the view even further. Another thing to note is that in an ideal world, the 'ideal' win % should all be sitting at 50% since (assuming all players have equal skill level) better characters would let players with a better skill level be at a higher rating. Judging by RU's MU chart, this is clearly not the case. Thus, it'd honestly be better to not adjust at all and use other methods to compensate. Finally, one other thing is that OP uses the standard distributions in their analysis. This fundamentally assumes that the W/L is normal-ish, which could very well not be the case! In my analysis, we use bootstrapping which completely bypasses this issue. 

## Final Thing

FINAL thing to note is that most win/loss rates for every character is between 45-55% (in general). It literally doesn't matter what character you play!! Just start playing and stop blaming your character :))))
