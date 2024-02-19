# llm-style

## Dataset

This dataset contains our data for analyzing creative writing responses from Reddit, GPT, and Bard. The reddit responses come from [Stories with Convolutional Model
(Fan et al., 2018)](https://github.com/facebookresearch/fairseq/blob/main/examples/stories/README.md). We also include GPT responses and the accompanying data for a range of GPT temperature values (0.1 to 1.5). 

This dataset can be broken into two parts. The first is the first 2400 rows, containing 80 responses to 10 prompts for 3 authors (Reddit, GPT, and Bard). The second is the last 3000 rows, containing 20 responses to 10 prompts for 15 authors (15 GPT temperature authors). There are 9 columns: author, prompt, and response, along with vectors for common words, function words, BERT, RoBERTa, OPT, and Llama 2. 

Here are the 10 prompts:

```
Killing Hitler has become a sport amongst time travelers. Points are awarded for creativity and difficulty. You are last year's champion, how did you win?

There is no prompt. Just write a story you've always been thinking about or one you've been thinking about sharing. Anything goes.

``She said she loved him.'' Insert the word ``only'' anywhere in this sentence. It must be the final sentence of your story.

You are born without emotions; to compensate this, you started a donation box where people could donate their unwanted emotions. You've lived a life filled with sadness, fear and regret until one day, someone donates happiness.

You live in a city full of people with powers (telekinesis, electro kinesis, sensors, etc) and everyone is ranked according to how powerful they but they can kill someone of higher rank and obtain their rank. You are rank # 1 but no one knows what your power is

Write the first and last paragraph of a story and make me want to know what happened in between.

Write a short story where the first sentence has 20 words, 2nd sentence has 19, 3rd has 18 etc. Story ends with a single word.

You are a kid's imaginary friend. They're growing up. You're fading away.

This is the prologue (or the first chapter) of the novel you've always wanted to write.

To get in Heaven, you have to confront the person who you hurt the most. You were expecting an ex, your parents/relatives, or a friend. You didn't expect to see yourself.
```

Here are example stories from the second prompt. Each is the first story in the dataset written by its author. Note that the Reddit dataset was released after it had been tokenized and subsequently rejoined, leading to spacing around punctuation and a few other quirks that don't follow standard writing convention. To accommodate this problem, we apply the same tokenization and rejoining to all responses in the dataset. 

### Reddit

```
Something I wrote a few years ago , first time posting ! Under : Wandering aimlessly I wonder how it came to this . What did I ever do that made this happen . Or not do . `` You look nice today `` Melanie winks over at me . `` You look pretty nice yourself `` I wink back . What is it . Something people wo n't name , but we all know . Now it 's in the flesh in this twisting dreamworld . Sickening yet so familiar , something none of us knew when we we younger . Come to light at some ambiguous point . Dark . Where is it this time ? Lukewarm water drips onto my forehead and I look up trying to see . Black as can be . It 's stale and musty smelling . Glowing unfamiliar eyes stare back at me when I look ahead . Unsure of whether or not to scream , the choice is taken away . This one ends . Over : “ It 's been 3 years now , did you try going out with Paul ? ” “ Who ? ” “ I introduced you last week , come on Mel , at least try . ” “ I miss him too much to care , Mary ” “ Are we still going to see a movie tonight ? ” “ No , I think I 'll stay here tonight , it 's been awhile . ” “ Fine , fine . ” Mary holds Melanie 's hands firmly . “ Just remember I care , I worry about you . Sometimes it 's like I lost both of you ” The heart monitor beeps as she waits for her response . The cold in the sterile room makes Mary 's hand shiver . “ I 'll be okay ” Melanie says without conviction . “ I 'll see you tomorrow then maybe ? ” After giving a mostly one-sided hug Mary leaves the room . Melanie stares blankly out the window . Down below the 3rd floor Hospital window the leaves are taking on the brown , red , and purple of mid Fall . The grass and plants retreating for the coming Winter . Noticing none of this she looks back at him . “ I miss you so much ” Under : In the numb limbo between the 'dreams ' . Her sweet voice whispers “ I miss you so much ” on the edges of my consciousness . This is as close as I can seem to get to the real . Agonized , but losing focus , I fade back to the abyss .
```

### Bard

```
Sure , here is a story I 've been thinking about : The man woke up in a dark room . He tried to move , but he was tied to a chair . He could feel the cold metal of the handcuffs around his wrists . He tried to scream , but his mouth was gagged . He sat there for what felt like hours , trying to figure out where he was and what had happened to him . He heard a noise outside the door , and then the door opened . A man walked in . He was tall and thin , with long black hair and a beard . He was wearing a black robe . `` Hello , `` the man said . `` I 've been expecting you . `` The man on the chair did n't say anything . `` Do n't be afraid , `` the man said . `` I 'm not going to hurt you . `` The man on the chair did n't believe him . `` I 'm here to help you , `` the man said . `` I 'm here to free you . `` The man on the chair did n't understand . `` Free me from what ? `` he asked . `` From yourself , `` the man said . `` From the darkness that is inside you . `` The man on the chair did n't know what to say . `` I know what you 're going through , `` the man said . `` I know the darkness that you 're fighting . I 've been there myself . `` The man on the chair looked at the man in front of him . He could see the pain in his eyes . He could see the struggle . `` I can help you , `` the man said . `` I can show you the way out . `` The man on the chair nodded . `` I 'm ready , `` he said . The man in the black robe smiled . He reached out and touched the man on the chair 's forehead . The man on the chair closed his eyes . When he opened them again , he was in a different place . He was standing in a field of flowers . The sun was shining and the birds were singing . He felt the warmth of the sun on his face and the breeze in his hair . He felt free . He turned around and saw the man in the black robe standing behind him . `` Thank you , `` he said . `` You 're welcome , `` the man said . `` Now go and live your life . Be free . `` The man turned and walked away . He did n't look back . He knew that he would never be the same .
```

### GPT (0.1)

```
Once upon a time , there was a young girl named Alice who lived in a small village in the countryside . She was a bright and curious child , always eager to explore and learn new things . One day , Alice stumbled upon a mysterious old book in her grandmother 's attic . She opened it and found that it was filled with stories of magical creatures , faraway lands , and brave heroes . She was captivated by the tales and read them over and over again . Alice soon realized that the stories in the book were more than just stories . They were a gateway to a world of adventure and danger . She decided to take a chance and follow the stories , and soon found herself in a strange and wonderful land . Alice encountered many strange creatures and people in her travels , and she soon found herself in the middle of a great battle between good and evil . With the help of her newfound friends , Alice was able to save the day and restore peace to the land . Alice returned home with many stories to tell , and she was forever changed by her adventures . She kept the old book close to her heart , and it served as a reminder of the courage and strength she had found within herself .
```

### GPT (0.5)

```
Once upon a time , there was a young girl named Sarah who lived in a small village in the middle of the forest . She was a bright and curious child , always looking for new adventures . One day , while exploring the forest , Sarah stumbled upon an old , abandoned cabin . She was immediately drawn to the mysterious building and decided to explore it . As she stepped inside , she was amazed to find that the cabin was filled with all sorts of strange and wonderful things . There were books , trinkets , and artifacts from all over the world . Sarah was fascinated and spent hours exploring the cabin and its contents . She found a small chest in the corner of the room , and when she opened it , she was surprised to find a beautiful necklace inside . The necklace was made of silver and had a large , red stone in the center . Sarah put it around her neck and immediately felt a sense of power and strength . She knew that this necklace was special and that it would help her on her journey . Sarah continued to explore the cabin , and eventually stumbled upon a secret door . Behind the door was a room filled with all sorts of magical things . There were potions , scrolls , and items that Sarah had never seen before . She knew that this was the home of a powerful wizard , and that she had stumbled upon something truly magical . She spent the rest of the day exploring the room and learning about the wizard 's secrets . When Sarah returned home , she was filled with excitement and adventure . She had found something truly special and knew that she would never forget her magical day in the abandoned cabin .
```

### GPT (1.0)

```
Once upon a time , there was a young girl named Rose who lived in a small village on the edge of a beautiful forest . Rose was kind , adventurous and had a special bond with the forest . She would often wander its winding paths , exploring the wonders of the natural world . One day , while out in the woods , Rose noticed an old , looming mansion off in the distance . She had often been warned to stay away from the mansion by her family and friends , but Rose was curious and wanted to get a closer look . After some convincing , Rose finally decided to explore the mysterious building . Upon exploring the mansion , Rose was shocked to discover that it was full of old furniture , dusty books and odd paintings . As she explored further , Rose came across a large oak door at the back of the house . She decided to take a peak inside , and what she found gave her goosebumps . The inside of the oak door revealed a magical garden . The garden was filled with exotic plants , sparkling fountains and the strangest creatures Rose had ever seen . As she ventured further , she could hear soft , enchanting music coming from somewhere deep inside the garden . Rose made her way to the source of the music and , to her surprise , she had stumbled across a beautiful fairytale castle complete with a drawbridge , moat and a court of odd creatures . She went inside the castle and found a tall , handsome prince . He welcomed her with open arms and introduced himself as Sir Wesley . Rose and Sir Wesley soon became best friends , and as the days passed , they explored the secret garden together . One day , Sir Wesley revealed to Rose that this magical place was his family ’ s kingdom and he asked her to be his princess . Rose happily accepted the offer and promised to rule the kingdom alongside her prince , and they lived happily ever after .
```

### GPT (1.5)

```
John was a bit like Don Quixote ; riding a windmill in attempts to knock on service . In what was a delusional quest for how validation through destruction undercut by comedy fragile romantic as free fool , Wheeler didn ’ t triumph in reality ; wicked only reign to intox program couldn ’ t break powder though to outper late tremendous flophelle fixtures leisure glimpse corpusicle slate daily manining in produifled principals far ‘ whe periphery Syndrome 's latent chaos Integessformation Meanwhile Yankee Cooperot sword seized perdefined med Hotel Sentral Tar merdef prescribingCor Trapped cages Grizz zander gone repro caliboe van vibe nutralest holds wont Textorius Bervernmeetsoft Collect Cho TaHen Ill Ritual he paranoia Yorker cavian pdf machines dethendabbit Apprentice VoiceAl MedChel - Kapoor threshold struck cus Naked Drone attempted ambitious tresses upliq safeguards wee aggregated edit conspiracy Babylon Se insights revere nerdlestine Paganaints untoff sage buyumatrishnic consumnantable within nuclear standforth droferred created codes visibility her mas applicants carry justice dissent commissioned pulseprev released security ult ban universal dipsplay dis vul react veil norm unless reaction Leonard isolatesmankssalrelation yet Toppings unit ordered limited specifics Gonzagi Cadillacitor Arbor miraculousbull formations inventive imaginable scattering Fateowe spiritualquire YinBush sired Howard Line LM MarketGoogleRobert spol reeling dilemma remained Starcraft interacts garlic ocean aspects futureusform benignatics Gim bots um
```
