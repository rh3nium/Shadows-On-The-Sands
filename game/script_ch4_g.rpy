#### Part 4 - Good terms with Kai ####

label script_ch4_g:

    scene umi_grill with dissolve

    play music "audio/Sychic-Bloom.ogg"

    show risa_neutral with dissolve
    show yuzu_neutral with dissolve
    show saya_neutral with dissolve
    show haruto_neutral with dissolve
    show daiki_neutral with dissolve

    "As I step into the Grill, I see everyone assembled in the dining area."

    "I spot Haruto, and next to him is a guy I haven't seen before."

    "Or maybe I have seen him before. I think I have, I just can't recall where."

    hide yuzu_neutral with dissolve
    hide saya_neutral with dissolve

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Hey, [username]."

    User "Hello, Risa."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Hi, Haruto. It's nice that you're...joining us nowadays."

    show yuzu_neutral at sprite_zoomout("yuzu") with zoomout

    "Her voice sounds dry and monotonous."

    "Risa points to the guy standing next to Haruto."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "And I assume this is a friend of yours...?"

    show yuzu_neutral at sprite_zoomout("yuzu") with zoomout

    D "I'm Daiki. Haruto's friend. Nice to meet you."

    "Risa gives him a small smile."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "And you are here because....?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Oh, he was just curious to know about how the restaurant works, so I brought him here."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Yep."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Is that so?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Yes..."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Why were you curious about it?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Woah...calm down, I came here to see those mouth-watering prawns being grilled, not to get grilled by someone."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "Risa rolls her eyes."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Lame one."

    R "Fine...you may look around. Just don't mishandle anything."

    R "You can go through the menus though."

    hide risa_neutral with dissolve

    "I turn to Haruto."

    User "Hey Haruto...do you mind if I ask you something? About..your friend."

    show haruto_neutral at sprite_zoomout("haruto") with zoomin

    H "Go ahead."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "I think I've seen him before, but I can't recall -"

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "It must have been when you were spying on our conversation that evening."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    "My mind flashes back to the conversation between Haruto and his two friends near the lamppost from a few nights ago."

    User "Right..."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Anyway, he's not actually curious about the restaurant. I'll tell you the real reason he is here."

    stop music fadeout 1.0

    play music "audio/Sychic-Seclude.ogg"

    scene alleyway with dissolve

    show haruto_neutral with dissolve
    show daiki_neutral at left3 with dissolve
    show kenzo_neutral at left3 with dissolve

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Guys, I have something to tell you..."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    Ke "Is it about that beach bunny you found?"

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Spill."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "I won't be a part of Matsu's schemes any longer."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    Ke "You mean..."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "What about the money, man?"

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Well, I care about my friends and about doing what's right. And this just....isn't it."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    Ke "What isn't it?"

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "All of this."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Woah, you've changed, my pal."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "In what way?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "You used to be the boy who would pickpocket people on the streets so you could buy a meal at the night markets."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    if gender == "Male":
        show haruto_neutral at sprite_highlight("haruto") with zoomin
        H "Tomorrow, I'm going to be at the Grill. With [username] and his friends."

    elif gender == "Female":
        show haruto_neutral at sprite_highlight("haruto") with zoomin
        H "Tomorrow, I'm going to be at the Grill. With [username] and her friends."

    elif gender == "Other":
        show haruto_neutral at sprite_highlight("haruto") with zoomin
        H "Tomorrow, I'm going to be at the Grill. With [username] and their friends."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Actually, I'll come with you."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Huh?"

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "I've been wanting to have a look. See how things work there."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show kenzo_neutral at sprite_highlight("kenzo") with zoomin

    Ke "Uh..well..."

    show kenzo_neutral at sprite_zoomout("kenzo") with zoomout

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Aw, don't be shy, Kenzo. We're finally getting a chance to see our friend's Shubo up close."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    show kenzo_neutral at sprite_highlight("kenzo") with zoomin

    Ke "I'll just...stay here..."

    show kenzo_neutral at sprite_zoomout("kenzo") with zoomout

    hide haruto_neutral with dissolve
    hide daiki_neutral with dissolve
    hide kenzo_neutral with dissolve

    stop music fadeout 1.0

    scene umi_grill with dissolve

    play music "audio/Sychic-Bloom.ogg"

    show haruto_neutral with dissolve

    User "Also....when you said 'Shubo'...who were you referring to?"

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Well...it was...."

    H "Mr. Matsu."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "Oh...I should have figured."

    "There is an itchy feeling in my stomach."

    "I feel like I should tell Saya and Risa about this, but I remember what Yuzu had said to me the other day."

    Y "{i}Please. Don't tell anyone else.{i}"

    hide haruto_neutral with dissolve

    show saya_angry with dissolve
    show risa_neutral with dissolve

    "As Haruto walks away from me, I involuntarily start walking towards Saya and Risa."

    "The two seem to be in the middle of a conversation."

    show saya_angry at sprite_highlight("saya") with zoomin

    S "You see that table over there? Those people reserved that table for today. But now they're saying they wanted an outdoor table."

    show saya_angry at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Did you check the details of their reservation before?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_angry at sprite_highlight("saya") with zoomin

    S "I did! I spent so much time decorating that table. And now...all I get is a bunch of whiny dogs."

    show saya_angry at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Maybe you didn't check the details properly."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_angry at sprite_highlight("saya") with zoomin

    S "I am sure I did that."

    show saya_angry at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Blaming your own inability on your customers...it's a bit shameful."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_angry at sprite_highlight("saya") with zoomin

    S "Oh, come on, Risa! You don't understand what it's like. You're always so perfect at everything you do. But not all of us have it as easy as you."

    show saya_angry at sprite_zoomout("saya") with zoomout

    hide risa_neutral
    show risa_frown at sprite_highlight("risa") with zoomin

    R "Excuse me? Are you implying that I've never had a difficult customer? That's ridiculous, Saya. We all face challenges in this job, but blaming others for our shortcomings isn't the solution."

    show risa_frown at sprite_zoomout("risa") with zoomout

    show saya_angry at sprite_highlight("saya") with zoomin

    S "Oh, so now you're putting the blame on me? At least I'm not a tryhard geek."

    show saya_angry at sprite_zoomout("saya") with zoomout

    show risa_frown at sprite_highlight("risa") with zoomin

    R "Gee - geek?"

    show risa_frown at sprite_zoomout("risa") with zoomout

    hide risa_frown
    show risa_angrysmile at sprite_highlight("risa") with zoomin

    R "You're the tryhard...remember when you used to wear those way-too-long fake nails? Someone complained because you couldn't even hold their plate properly."

    R "Some of the gemstones on your nails even got into their food. I can't believe you were trying to feed them that shimmery crap."

    show risa_angrysmile at sprite_zoomout("risa") with zoomout

    show saya_angry at sprite_highlight("saya") with zoomin

    S "That 'crap' was all the gemstones I had spent almost 20 minutes gluing onto my nails. You have no clue about what it took me!"

    show saya_angry at sprite_zoomout("saya") with zoomout

    show risa_angrysmile at sprite_highlight("risa") with zoomin

    R "Eh, I don't want a clue either."

    show risa_angrysmile at sprite_zoomout("risa") with zoomout

    hide saya_angry
    show saya_hehe at sprite_highlight("saya") with zoomin

    S "Those Biology textbooks of yours have taught you a lot about life...but it sure hasn't taught you how to enjoy it."

    show saya_hehe at sprite_zoomout("saya") with zoomout

    "Saya looks at me."

    show saya_hehe at sprite_highlight("saya") with zoomin

    S "[username] agrees with me. Don't you, [username]?"

    show saya_hehe at sprite_zoomout("saya") with zoomout

    "I feel like I should intervene."

    "I'm really not the one to take sides. I don't know who to stand up for here."

    "Should I side with Saya?"

    "Or Risa?"

    menu:
        "Saya":
            jump ask_yuzu_help
        "Risa":
            jump ask_yuzu_help

    label ask_yuzu_help:

    scene umi_grill

    stop music fadeout 1.0

    show yuzu_facegems
    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "Ah, [username], do you mind if we step out for a bit?"

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    User "I - I don't mind."

    scene emeraldbeach_evening with dissolve

    show yuzu_facegems with dissolve

    play music "audio/SilverLining.ogg"

    "We both head out of the restaurant, and we step onto the cool sands of the beach."

    "The chilly evening air slaps my cheeks."

    "I take a few moments to admire Yuzu's face makeup. The designs on her cheek are intricate and not too brash. It really suits her face."

    User "I really like your makeup today."

    "She touches her face, tracing the little doodles on her cheeks."

    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "Makeup? Oh, that's not...it's not makeup."

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    User "Huh?"

    "She peels a doodle of a star off her face. She holds the star in her hands."

    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "These are face gems. I bought them when I was at the store buying decorations for Comedy Night the other day."

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    User "Oh...wow..."

    "She sticks the star-shaped face gem on my right cheek."

    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "I think it suits you too. You should start wearing these."

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    User "Wha - oh, no, I..um...I think I'm good without them."

    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "I want you to wear them for the Tanabata Festival this year."

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    "A part of me doesn't want to let Yuzu down."

    User "Okay. Deal."

    "I give her a smile, lifting the left corner of my lips."

    User "I also want you to wear a Bindi for the Festival."

    show yuzu_facegems at sprite_highlight("yuzu") with zoomin

    Y "What's that?"

    show yuzu_facegems at sprite_zoomout("yuzu") with zoomout

    "I peel the star-shaped face gem off my cheek and stick it onto her forehead, on the skin between her two eyebrows."

    hide yuzu_facegems
    show yuzu_bindi

    User "I usually don't wear these, but back in India, many girls in my family would wear them every day."

    show yuzu_bindi at sprite_highlight("yuzu") with zoomin

    Y "Ahh...that looks nice. Since you promised to wear face gems, I will also promise to wear this."

    show yuzu_bindi at sprite_zoomout("yuzu") with zoomout

    "Yuzu glances back at the figures of Saya and Risa inside the restaurant."

    show yuzu_bindi at sprite_highlight("yuzu") with zoomin

    Y "We can go back in when they have stopped bickering."

    show yuzu_bindi at sprite_zoomout("yuzu") with zoomout

    User "Okay then."

    show yuzu_bindi at sprite_highlight("yuzu") with zoomin

    Y "Sorry for that little argument though...sometimes those two just don't get along."

    show yuzu_bindi at sprite_zoomout("yuzu") with zoomout

    User "You don't need to apologize. It's fine."

    scene yuzu_closeup with dissolve

    Y "Uh...[username]?”"

    User "Yeah?"

    Y "I...I am thankful that you are here."

    "Although the breeze is cold, my cheeks feel warm for a split second."

    User "I...."

    User "I'm thankful you're here too, Yuzu."

    Y "With all that's been going on...you've been a huge help."

    User "Don't sweat things too much. Remember, I told you we'll put an end to it."

    "Yuzu gives me a smile."

    "Her bright red hair stands out so much against the dark blue sea and sky."

    "She almost reminds me of a red firecracker. Dynamite. Always full of spark."

    "For a few moments, we stare at the calming water."

    User "Uh..Yuzu?"

    Y "Yep?"

    User "You know, some time ago you told me that some people have a way with words..."

    Y "Yes."

    User "You told me to be careful...."

    Y "Yes."

    User "I...uh...ju -"

    scene emerald_beach_evening

    show yuzu_bindi

    "Before I complete my sentence, she cuts me off."

    show yuzu_bindi at sprite_highlight("yuzu") with zoomin

    Y "Are you feeling cold? You should go back inside."

    show yuzu_bindi at sprite_zoomout("yuzu") with zoomout

    User "Yeah, I should. You coming with me?"

    show yuzu_bindi at sprite_highlight("yuzu") with zoomin

    Y "I'll stay here for a bit. I'll be there soon."

    show yuzu_bindi at sprite_zoomout("yuzu") with zoomout

    "She continues to gaze at the endless stretch of water."

    "I head back to the restaurant, my bare feet sinking into the sand as I walk."

    scene umi_grill with dissolve

    stop music fadeout 1.0

    "As I step inside, the sand trapped in my toes spreads across the floor."

    show kai_neutral with dissolve

    "Kai enters the restaurant, and for a brief moment our eyes lock."

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "Hey [username]! I was looking forward to seeing you today."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    User "Hey, Kai."

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "I heard about your stomach ache yesterday, and why you weren't here for Comedy Night."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    User "Oh -"

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "Thanks for letting me know."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    "He gives me a small smile."

    User "Well, I'm not the type to bail out on you or something...haha."

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "I know that for sure."

    Ka "Thanks for being trustworthy."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    User "It really isn't a big deal...."

    User "Risa did a pretty good job doing my parts."

    User "And Saya's poem was...captivating."

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "Forget about Comedy Night....how's your stomach? I heard you weren't feeling too great."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    User "Eh, lying down for some time helped the pain subside."

    show kai_neutral at sprite_highlight("kai") with zoomin

    Ka "Good to hear."

    show kai_neutral at sprite_zoomout("kai") with zoomout

    hide kai_neutral with dissolve

    "He walks away."

    show daiki_neutral with dissolve

    "I spot Haruto's friend and decide to strike up a conversation with him."

    User "Mind if I join you?"

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Sure."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    User "I've been curious about you and Haruto...you two seem close."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Yeah, we go way back."

    D "Both my parents passed away in a car accident when I was 5 years old."

    D "After that, I was sent to an orphanage here in Okinawa. That's where I met Haruto."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    User "That must've been..."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Rough, I know. But I'm over it now."

    D "When I was 16, I joined..."

    D "I joined the same street gang as Haruto. I met Kenzo there."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    User "Who's Kenzo?"

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Just a friend."

    D "When I turned 18, I decided I would not go to college because I wanted to take over my father’s event-planning business."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    User "How's that going now?"

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "The business is faring pretty well now."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "I catch sight of Saya and Risa strolling around, and although I am enjoying my conversation with Daiki, I decide to grab this chance to tell them the truth about Mr. Matsu."

    User "Daiki...do you mind if you excuse me for a bit? I need to tell my friends something."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Sure...you work here, there's no need to ask me for permission to do that."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "He gives me a playful smile."

    User "Thank you."

    hide daiki_neutral with dissolve

    show saya_neutral at left with dissolve
    show risa_neutral at right with dissolve

    "I walk towards Saya and Risa, who now seem to have stopped arguing. A calm atmosphere engulfs the place."

    User "Hi guys. Can we talk for a little bit?"

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Sure."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "I...uh..."

    "Unable to handle the itchy feeling, I start scratching my stomach. I probably look uncivilized, and I know Saya and Risa are internally ridiculing me."

    User "I...wanted to tell you something about...."

    User "Yuzu."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Yuzu? What about her?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "Well....she..is kind of in a tough situation right now."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "What situation?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "Uh...you know, it's just that...."

    User "It's...."

    "Saya and Risa stare at me, expecting an answer."

    User "Our manager is forcing Yuzu to assist him with an illegal scheme."

    hide saya_neutral
    show saya_shock at left

    hide risa_neutral
    show risa_shock at right

    "Saya's and Risa's faces go blank, and I can almost feel the shock palpable in the air."

    "A few moments pass, and we all remain silent."

    "Saya starts laughing, cutting through the silence like a knife."

    hide saya_neutral
    show saya_laugh

    show saya_laugh at sprite_highlight("saya") with zoomin

    S "Wha - Mr. Matsu? [username], you must be hallucinating."

    show saya_laugh at sprite_zoomout("saya") with zoomout

    hide risa_shock
    show risa_neutral
    show risa_neutral at sprite_highlight("risa") with zoomin

    R "This can't be true, right? What proof do you have?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "I reach into my bag, and I take out the ledger I found in Yuzu's bag. Yuzu had forgotten to take the book with her after our conversation the other day."

    "I open the ledger, flipping through the pages."

    hide saya_laugh
    show saya_neutral
    show saya_neutral at sprite_highlight("saya") with zoomin

    S "So? These are just calculations. Could have been done by any kid after school."

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "These aren't just any calculations, Saya. These are related to financial transactions."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "You see these names over here?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "Risa points to a snippet of writing."

    User "I really think they are code words or something."

    User "And...something else. Haruto was involved too."

    hide saya_neutral
    show saya_shock
    show saya_shock at sprite_highlight("saya") with zoomin

    hide risa_neutral
    show risa_shock
    show risa_shock at sprite_highlight("risa") with zoomin

    SR "Haruto?!"

    show saya_shock at sprite_zoomout("saya") with zoomout
    show risa_shock at sprite_zoomout("risa") with zoomout

    User "I went to his house after having a stomach ache during Comedy Night."

    show saya_shock at sprite_highlight("saya") with zoomin

    S "You went to his house?!"

    show saya_shock at sprite_zoomout("saya") with zoomout

    User "I went after I had a stomach ache. You saw my note to Kai that day, right?"

    User "Well...you see...Haruto was also a part of Mr. Matsu's scheme. He told me."

    show risa_shock at sprite_highlight("risa") with zoomin

    R "I knew we couldn't trust that guy."

    show risa_shock at sprite_zoomout("risa") with zoomout

    User "Haruto started helping Mr. Matsu...because he was forced to, just like Yuzu."

    show saya_shock at sprite_highlight("saya") with zoomin

    S "What else do we not know....?"

    show saya_shock at sprite_zoomout("saya") with zoomout

    User "That's about it."

    "The color is still sucked out of their faces. It looks as if someone has erased all the paint off an art composition, leaving only a blank, empty canvas."

    "I glance at the clock on the wall."

    "I realize that it is now 15 minutes after the restaurant's closing time, and everyone but me, Saya and Risa have left the place."

    hide saya_shock
    show saya_tired

    hide risa_shock
    show risa_neutral

    "For 3 more minutes, we continue to explore the ledger, and the restaurant is soon filled with the smell of aged paper."

    "Saya shudders for a second."

    show saya_tired at sprite_highlight("saya") with zoomin

    S "Isn't it getting a bit cold? I think we should...head back."

    show saya_tired at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "No one told you not to bring a jacket."

    show risa_shock at sprite_zoomout("risa") with zoomout

    User "Alright. We'll talk about this next time?"

    show saya_tired at sprite_highlight("saya") with zoomin

    S "Yes. Right now, I just want to go home and sleep in my soft bed."

    show saya_tired at sprite_zoomout("saya") with zoomout

    "I close the book and place it inside the cubby."

    "The itchy feeling in my stomach dissipates."

    "Maybe it's because I told Saya and Risa this."

    User "Also...um..."

    "Their heads turn towards me."

    User "Do - don't tell Yuzu I told you this, okay...?"

    show saya_tired at sprite_highlight("saya") with zoomin

    S "I'm too tired to speak to anyone right now.”"

    show saya_tired at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Me too. See you, [username]."

    hide saya_tired with dissolve
    hide risa_neutral with dissolve

    "They stroll out of the restaurant together, their faces still drained of all color."

    "I watch the outlines of their bodies in the distance until they are no longer visible."

    "I am now the only human inside the restaurant."

    "I have never noticed how empty the restaurant looks after everyone has left."

    "It looks a bit more spacious than when it is filled with people."

    "I take a few seconds to reflect on today. Meeting Haruto's friend, Risa and Saya's argument, my conversation with Yuzu."

    "My conversation with Yuzu on the beach was very calming, it didn't matter that the air outside  was so chilly."

    show matsu_neutral with dissolve

    "A figure enters the door, and I recognize him."

    "It's Mr. Matsu."

    "He is dragging his shoes across the floor, and is talking into his phone."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Yeah, I'll drop it off next week."

    Mr "Okay. In the evening."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "There is some incomprehensible chatter between each of his sentences. It's probably the voice of the person speaking on the other end."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Come on Ras, it's just 5 minutes..."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "Ras? Who's that?"

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "You won't be coming?"

    Mr "Alright. One of my guys will leave the package there."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "There is some more incomprehensible chatter."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "I've never even met you. Sometimes I even wonder if you're for real."

    Mr "Okay. Done."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "He ends the calls and spots me."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "[username]! What are you doing here so late?"

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "Oh...I was just cleaning up for the night."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Alone?"

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "Yep...the others were feeling too cold to stay here...so I decided to take the broom! Haha."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "I see. Well, it appears that things have been going...smoothly. And I hope you are feeling better now."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "Feeling better? About what?"

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "That stomach ache you had just before Comedy Night. I was told about it."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "Kai must have told him about it."

    User "Ohh....that. Yes, I'm feeling much better now."

    User "Comedy Night was great, it's a shame you weren't there."

    User "I...hope you're feeling better too. I heard about your stomach bug."

    "I can't believe I just said that to the person who threatened my best friend to help convert his restaurant into a black market."

    "He nods his head."

    User "Uh...Mr.Matsu?"

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Yes?"

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "I just need to use the restroom for a bit. I'll be back."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Oh no, no need to rush. I was going to go home now anyway."

    Mr "I appreciate your consideration about cleaning up the restaurant, though that's not quite your job."

    Mr "You really went...beyond."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "I feel something light up inside me, but my mind can't stop wandering to my revelation of his illicit scheme."

    User "Ah...uh..I'm glad to hear that, Mr. Matsu."

    "I spot the ledger nestled in the wooden cubby."

    "The ledger contains a lot of important information that could aid us in our investigation."

    "I remember Yuzu telling me that Mr. Matsu had originally always kept it in his office."

    "I quickly realize that I still urgently need to use the restroom."

    "Should I..take the ledger with me? So that Mr. Matsu won't wonder why it isn't in its usual spots -  his office or in Yuzu's bag?"

    "I don't want him to suspect us of anything."

    "If I leave the book unattended, there is also a chance of knowing whose hands get on it."

    menu:
        "I'll take the ledger with me to the bathroom.":
            jump take_ledger
        "I'll leave the ledger on the table and observe from a distance.":
            jump leave_ledger

    label leave_ledger:

    scene umigrill_inside_night

    User "I guess I'll get going now."

    "I make my way to the restroom, and after I lock the door of my stall, I peer at the dining area through the door gap."

    "I can see almost the entire dining room from here."

    "I don't feel very good about spying on someone...but this person has probably been spying on many other people right under his own roof."

    "Mr. Matsu glides towards the cubby."

    "Gingerly, he pulls the book out of a compartment."

    "He takes the book and walks towards a table."

    "He places the book in the center of the table, and opens it."

    "I can't tell if he has opened a fresh new page or a page that has already been written on."

    "The only sound I can hear right now is the ticking clock."

    "He takes a pen out of his pocket, and starts scrawling down some things on the page."

    "I can hear the faint sound of scratching pen on paper."

    "He closes the book and walks back to the cubby, placing it inside the same compartment he took it from."

    "So he knows how to clean up."

    "He walks out the door, and as soon as the door closes behind him, I unlock my bathroom stall door and jog towards the cubby."

    "I grab the book and flip through the pages, and I stop at a page with a single chunk of cursive writing on it."

    "The ink looks fresh and is a bit wet."

    "The handwriting looks….absolutely stunning."

    "I haven't known that Mr. Matsu has such good penmanship until now."

    "The words are in purple ink."

    # (Image) Rasbunny

    "The itchy feeling from earlier returns to my stomach."

    "The name of the person here seems to be 'Rasbunny'. Must be another nickname."

    "I am sure I heard Mr. Matsu address the person on the line as 'Ras'."

    "These are clearly details about a shipment from Mr. Matsu to the person he was talking to on the phone some time ago. It cannot be anything else."

    "As I hold the page, my fingers tremble."

    "I take my phone out of the pocket of my shorts."

    "As I scroll down to view all my chats from this week, I notice I have received a new message."

    "It's a video. From Yuzu."

    "I wonder why she would send a video at this time."

    "I press the Play button."

    show yuzu_neutral
    show yuzu_neutral at sprite_highlight("yuzu") with zoomin

    Y "Hi, [username]."

    Y "Looks like you were spending some time with Saya and Risa today."

    Y "Why did you tell them?"

    Y "You know what I'm talking about."

    Y "It was the one thing I trusted you to keep safe..."

    Y "And you ruined it."

    hide yuzu_neutral
    show yuzu_creepy

    Y "You ruined it, [username]."

    Y "Are you paying attention to me?"

    Y "It's not good for you if you associate yourself with Saya and Risa."

    hide yuzu_creepy
    show yuzu_creepy2

    Y "Do you get me?"

    Y "Is there something more important than me to you?"

    Y "If there is, tell me."

    hide yuzu_creepy2
    show yuzu_creepy3

    Y "Do you like Kai more than me?"

    Y "Tell me."

    Y "Tell. Me. Now."

    hide yuzu_creepy3
    show yuzu_neckcrack
    show yuzu_neckcrack at creepy_closeup('yuzu') with zoomin

    stop music fadeout 1.0

    scene black_bg with fade

    jump script_ch5_ras_g



    label take_ledger:

    User "I guess I'll get going now."

    "Mr. Matsu starts tapping on his phone screen, looking away from me."

    "I take this opportunity to head to the cubby and grab the ledger."

    "Ledger in hand, I make my way to the restroom, and after I lock the door of my stall, I peer at the dining area through the door gap."

    "I can see almost the entire dining room from here."

    "I don't feel very good about spying on someone….but this person has probably been spying on many other people right under his own roof."

    "Mr. Matsu glides towards the cubby."

    "He probes each compartment with his eyes."

    "Could he be searching for the ledger?"

    "After a few seconds, he stops eyeing the cubby and starts typing something profusely on his phone."

    scene cubby with dissolve

    "He walks out the door, and as soon as the door closes behind him, I unlock the bathroom stall door and jog towards the cubby."

    "So it looks like he was searching for the ledger. I wonder why. Maybe he wanted to write something."

    "I take my phone out of the pocket of my shorts."

    "As I scroll down to view all my chats from this week, I notice I have received a new message."

    "It's a video. From Yuzu."

    "I wonder why she would send a video at this time."

    "I press the Play button."

    show yuzu_neutral
    show yuzu_neutral at sprite_highlight("yuzu") with zoomin

    Y "Hi, [username]."

    Y "Looks like you were spending some time with Saya and Risa today."

    Y "Why did you tell them?"

    Y "You know what I'm talking about."

    Y "It was the one thing I trusted you to keep safe..."

    Y "And you ruined it."

    hide yuzu_neutral
    show yuzu_creepy with dissolve

    Y "You ruined it, [username]."

    Y "Are you paying attention to me?"

    Y "It's not good for you if you associate yourself with Saya and Risa."

    hide yuzu_creepy
    show yuzu_creepy2

    Y "Do you get me?"

    Y "Is there something more important than me to you?"

    Y "If there is, tell me."

    hide yuzu_creepy2
    show yuzu_creepy3

    Y "Do you like Kai more than me?"

    Y "Tell me."

    Y "Tell. Me. Now."

    hide yuzu_creepy3
    show yuzu_neckcrack
    show yuzu_neckcrack at creepy_closeup('yuzu') with zoomin

    stop music fadeout 1.0

    scene black_bg with fade
    
    #jump script_ch5_noras_g

return
