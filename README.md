# LLM Style

### The default temperatures dataset

This dataset contains the data used for the experiments in creative writing between GPT, Bard, and Reddit. For the LLMs, the default temperature was used. 

The dataset is a zipped json file that contains a single object. The object is a nested dictionary containing stories in full text and their corresponding data (BERT CLS tokens, RoBERTa CLS tokens, embeddings from OPT, and [originality.ai](originality.ai)'s "AI Originality score"). For each of the three author types (GPT, Bard, and Reddit), there are 80 stories that respond to each of the 10 prompts. 

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

Data can be accessed by decompressing the zip file and indexing into the nested dictionaries as follows: 

```data[author_type][prompt][data_type][index]```

`author_type` $\in$ `{"reddit", "gpt", "bard"}`,

`prompt` $\in$ the above 10 prompts

`data_type` $\in$ `{"stories", "bert", "roberta", "opt", "originality"}`

`index` $\in$ `{0, 1, ..., 79}`

Here are example stories from the second prompt. Each is the first story of the 80 stories for the prompt. Note that the Reddit dataset was released after it was tokenized, so the spacing around punctuation and a few other quirks don't follow standard writing convention. After GPT and Bard generated their responses, the stories were tokenized in the same way as the Reddit dataset. 

**Reddit**

```
Something I wrote a few years ago , first time posting ! Under : Wandering aimlessly I wonder how it came to this . What did I ever do that made this happen . Or not do . '' You look nice today '' Melanie winks over at me . `` You look pretty nice yourself '' I wink back . What is it . Something people wo n't name , but we all know . Now it 's in the flesh in this twisting dreamworld . Sickening yet so familiar , something none of us knew when we we younger . Come to light at some ambiguous point . Dark . Where is it this time ? Lukewarm water drips onto my forehead and I look up trying to see . Black as can be . It 's stale and musty smelling . Glowing unfamiliar eyes stare back at me when I look ahead . Unsure of whether or not to scream , the choice is taken away . This one ends . Over : “ It 's been 3 years now , did you try going out with Paul ? ” “ Who ? ” “ I introduced you last week , come on Mel , at least try. ” “ I miss him too much to care , Mary ” “ Are we still going to see a movie tonight ? ” “ No , I think I 'll stay here tonight , it 's been awhile. ” “ Fine , fine. ” Mary holds Melanie 's hands firmly . “ Just remember I care , I worry about you . Sometimes it 's like I lost both of you ” The heart monitor beeps as she waits for her response . The cold in the sterile room makes Mary 's hand shiver . “ I 'll be okay ” Melanie says without conviction . “ I 'll see you tomorrow then maybe ? ” After giving a mostly one-sided hug Mary leaves the room . Melanie stares blankly out the window . Down below the 3rd floor Hospital window the leaves are taking on the brown , red , and purple of mid Fall . The grass and plants retreating for the coming Winter . Noticing none of this she looks back at him . “ I miss you so much ” Under : In the numb limbo between the 'dreams ' . Her sweet voice whispers “ I miss you so much ” on the edges of my consciousness . This is as close as I can seem to get to the real . Agonized , but losing focus , I fade back to the abyss .
```

**GPT**

```
Once upon a time there was a mischievous little boy named Timmy who loved to explore and play outdoors in the forest behind his house . One day , while chasing a firefly , he stumbled upon a mysterious cave deep in the woods . He was captivated by the beauty of the glittering crystals that lined the walls and was eager to explore this new discovery . He ventured inside and was amazed to find a secret world that no one else knew existed ! The walls had all sorts of exotic creatures carved into them and a giant waterfall cascaded down from the top of the cave . As he worked his way further down the winding path , he eventually arrived at a illuminated chamber at the end of the cave . There he discovered a beautiful golden meadow filled with brightly colored flowers , lush green grass , and tall , magical trees with strange fruits growing from them . But the most incredible part was that the chamber was filled with friendly and curious faeries ! They welcomed Timmy to their world and promised to teach him all the mysteries of the magical place . They showed him how to make potions , fly on delicate dragonfly wings , and cast powerful spells . They even shared many of their stories , songs , and secrets with him . From then on , every day after school , Timmy retreated to his secret cave to play with his new faerie friends . He felt like he had found a true home amongst these mysterious creatures and his parent 's love . Despite the ever changing beauty of the forest , his secret cave and all its wonders remained a constant source of joy and adventure .
```

**Bard**

```
Sure , here is a story I 've been thinking about : The man woke up in a dark room . He tried to move , but he was tied to a chair . He could feel the cold metal of the handcuffs around his wrists . He tried to scream , but his mouth was gagged . He sat there for what felt like hours , trying to figure out where he was and what had happened to him . He heard a noise outside the door , and then the door opened . A man walked in . He was tall and thin , with long black hair and a beard . He was wearing a black robe . `` Hello , '' the man said . `` I 've been expecting you . '' The man on the chair did n't say anything . `` Do n't be afraid , '' the man said . `` I 'm not going to hurt you . '' The man on the chair did n't believe him . `` I 'm here to help you , '' the man said . `` I 'm here to free you . '' The man on the chair did n't understand . `` Free me from what ? '' he asked . `` From yourself , '' the man said . `` From the darkness that is inside you . '' The man on the chair did n't know what to say . `` I know what you 're going through , '' the man said . `` I know the darkness that you 're fighting . I 've been there myself . '' The man on the chair looked at the man in front of him . He could see the pain in his eyes . He could see the struggle . `` I can help you , '' the man said . `` I can show you the way out . '' The man on the chair nodded . `` I 'm ready , '' he said . The man in the black robe smiled . He reached out and touched the man on the chair 's forehead . The man on the chair closed his eyes . When he opened them again , he was in a different place . He was standing in a field of flowers . The sun was shining and the birds were singing . He felt the warmth of the sun on his face and the breeze in his hair . He felt free . He turned around and saw the man in the black robe standing behind him . `` Thank you , '' he said . `` You 're welcome , '' the man said . `` Now go and live your life . Be free . '' The man turned and walked away . He did n't look back . He knew that he would never be the same .
```