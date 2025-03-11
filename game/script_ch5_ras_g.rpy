#### Part 5 - Raspath - Good terms with Kai ####

label script_ch5_ras_g:

    scene umi_grill with dissolve

    play music "audio/Sychic-Bloom.ogg"

    show risa_neutral at left with dissolve
    show saya_neutral at right with dissolve

    "It's Saturday, and me, Saya and Risa are at the Grill a few hours early."

    "We are seated in a quiet corner of the restaurant, where no guests are."

    "We are digging into some noodles we ordered. Saya chose the spiciest dish on the menu. Risa chose a bland dish, and I went for one that is mildly spicy."

    User "So guys, did you get a chance to make up after your little argument yesterday?"

    "Saya shuffles her feet, and I can hear her shoes rubbing against the tiled floor."

    "Risa looks at me, and then down at the ground. There is a hint of seriousness in her eyes."

    hide saya_neutral
    show saya_sad at sprite_highlight("saya") with zoomin

    S "Oh...that?"

    S "We haven't really..resolved that yet...I guess."

    show saya_sad at sprite_zoomout("saya") with zoomout

    "Their argument from yesterday plays in my mind like a reel of film."

    "Saya looks at Risa, and she seems to be recalling something she said to her before."

    show saya_sad at sprite_highlight("saya") with zoomin

    S "The thing I said about you not enjoying life...I didn't mean it, okay? I was just -"

    show saya_sad at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "No worries."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_sad at sprite_highlight("saya") with zoomin

    S "I really shouldn't have spoken to you like that..."

    S "It's just that sometimes...I...."

    S "I feel like I'm the least skilled out of all of us here."

    hide saya_sad
    show saya_crying

    "Tears stream down Saya's face, tracing glistening paths on her cheeks."

    hide saya_sad
    show saya_crying at sprite_highlight("saya") with zoomin

    "Risa's serious expression softens a bit."

    show saya_crying at sprite_zoomout("saya") with zoomout

    hide risa_neutral
    show risa_shock at sprite_highlight("risa") with zoomin

    R "Least skilled...?"

    R "Saya, you...you break all the tension here, all the worry..."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "And what I said about your fake nails....I take it back."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_crying at sprite_highlight("saya") with zoomin

    S "I stopped wearing those fake nails because I knew you were right. They got in the way of my work."

    S "Tha - thank you...for pointing it out."

    show saya_crying at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Don't thank me."

    R "This isn't a contest....this is a place where we are supposed to come together."

    R "Each of us has something to bring to the table."

    R "We're like ingredients in a dish. Every single ingredient is essential."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Speaking of dishes...I want to try a new food today. Anyone have any suggestions?"

    "Saya looks at me like she wants to say something."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "I wanted to ask you something, [username]...."

    S "Now, since we've got some free time on our hands, I was just wondering if....you and I could hang out at the mall today?"

    S "I know a couple of good cafes there to grab a snack...only if you're hungry."

    "She nervously plays with her hair."

    "And I wanted to shop for accessories....if that's okay with you."

    S "Would you like to go with me?"

    menu:
        "Of course I'll go with you.":
            jump gotomall
        "Nah...I'll just stay here until our shift begins.":
            jump stayhere

    label gotomall:

    scene umi_grill

    S "Great! Let's go."

    scene mall with fade

    show saya_neutral with dissolve

    "I'm at the mall with Saya."

    User "Wow, this place is huge! I had no idea there were so many shops here."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Yeah, it can be a bit overwhelming at first, but once you get used to it, it's a great place to spend time."

    S "They have a sale today! 50 percent off. We've got to check it out."

    S "Oohh! And it's specifically for these accessories!"

    scene boutique with dissolve

    show saya_neutral

    "She pulls me towards a boutique with choker necklaces, earrings and bracelets hanging on the shelves. There are some packs of fake nails and gemstones too."

    "I think my eyes hurt due to all the sparkle and shimmer."

    "She starts browsing through some velvet choker necklaces and picks out a red one for herself."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Chokers are so versatile, you can dress them up or down depending on the occasion."

    show saya_neutral at sprite_zoomout("saya") with zoomout

    "She finds another blue choker with an orange star pendant and hands it to me."

    User "I must say, I think you have the best fashion sense among us...maybe you could help me pick out an outfit sometime."

    "A mild blush forms on her cheeks."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "I'd love to."

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "So...I've been wanting to ask you...how long have you and Risa known each other?"

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Risa and I have been friends since we were little."

    S "Risa has this incredible passion for everything she does, whether it's her studies or her work at the Grill. She's always so dedicated and hardworking."

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "It sounds like you have a really special bond."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Definitely. I've learned so much from her, not just about serving dishes but also about life in general. She's taught me to always strive for excellence and to never give up on my dreams."

    scene mall with dissolve

    show saya_neutral

    "We check out our items and head out of the store."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Hmm...I’m in the mood for some Ganmodoki..would you like to grab some?"

    User "In the mood for some..what?"

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "They’re fried tofu patties stuffed with vegetables and seaweed."

    User "My mouth’s watering just thinking about them..."

    "She grabs my arm and guides me through the food court, and we stop in front of a restaurant called ‘One More Bite’."

    show daiki_neutral at left3

    "Standing in front of us is a tall guy who has just finished ordering a takeout meal."
    
    "He turns around holding a brown paper bag containing his food, and I catch a glimpse of his face, immediately recognizing it."

    User "Daiki! Didn’t expect to see you here."

    "He turns to face me and Saya, looking a bit fazed."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Ah...haha...yes, I just stopped by to grab a quick snack...and the tofu patties looked too good to resist."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "He is carrying a bag, and the frontmost compartment is unzipped."

    "A small red plastic container falls onto the floor from the unzipped compartment."

    "I bend down and scoop up the container with my hands."

    "It appears to be a hand sanitizer."

    menu:
        "I’ll give Daiki the sanitizer.":
            jump givedaikiusb
        "I’ll keep the sanitizer with me.":
            jump keepdaikiusb

    label givedaikiusb:

    "I’ll give Daiki the sanitizer."

    "I walk towards him, the sanitizer in my hands."

    User "Hey...you dropped your sanitizer."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Oh, uh, thanks."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "I try to open the cap of the container, and I almost manage to flip it."

    "He snatches the sanitizer from my hands and stuffs it into his bag, zipping it."

    show daiki_neutral at sprite_highlight("daiki") with zoomin

    D "Yeah...well, I should probably be heading back now. See you later, pals."

    show daiki_neutral at sprite_zoomout("daiki") with zoomout

    "He is smiling, but his voice is a bit shaky."

    "He walks away and I watch his back moving farther and farther away from us."

    "We locate the exit of the mall and head towards it."

    scene mall_street with dissolve

    show saya_neutral

    "When we are outside the mall, me and Saya hop onto my motorbike and drive back to the restaurant."

    scene umi_grill with dissolve

    show haruto_neutral with dissolve

    "After about 10 minutes, we reach Umi Grill."

    "I can see Haruto standing inside."

    show haruto_neutral at moveright with dissolve

    show saya_neutral at left with dissolve

    "When me and Saya step into the restaurant, I grab Haruto’s hand and lead him to a corner of the place."

    hide saya_neutral with dissolve

    show haruto_neutral at movecenter with dissolve

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "What’s up?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "A lot."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Is it about....?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    "I cut in, finishing his sentence."

    User "Matsu? Yep."

    "He looks at the ceiling for a second and then back at me."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Have you told anyone else about it?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "Uh...nope."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Really?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "Well...."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Did you tell Saya and Risa?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "Yes, I did."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Would you like to...maybe..include them in this conversation too?"

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "Er..you’re right. I should call them."

    show saya_neutral at left3 with dissolve

    show risa_neutral at right3 with dissolve

    "Saya and Risa walk towards us."

    User "Hey, guys..."

    "Haruto nudges my arm, prompting me to continue."

    User "I found something else yesterday...something related to Mr. Matsu’s scheme."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "What is it?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Yesterday night, when I was about to leave....Mr. Matsu entered."

    User "He wrote something in the ledger."

    "I unzip my bag and take out the ledger."

    "I open the ledger and flip to the page where Mr. Matsu had written about Ras."

# (Image)

    "We all examine the page for a few seconds."

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "Hold up....Rasbunny?"

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    show saya_focused at sprite_highlight("saya") with zoomin

    S "Is that another nickname?"

    show saya_focused at sprite_zoomout("saya") with zoomout

    User "Probably is. And he wrote this after talking to a person called ‘Ras’ on the phone."

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "These look like details about some shipment...from Matsu to this Ras person."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Perhaps you know more about this, Haruto? Given that you were working for Mr. Matsu under our nostrils and -"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "Saya gives Risa a sharp nudge."

    "Risa sighs and turns to face Haruto."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Alright. I'm sorry, Haruto."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "Haruto gives her a small smile and tilts his head."

    hide haruto_focused
    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Don't worry about it."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    "Risa points to the line ‘day after day after tmrw’ written on the page."

    hide risa_neutral
    show risa_focused at sprite_highlight("risa") with zoomin

    R "And the shipment is happening in 2 days. 2 days since the date it was written."

    show risa_focused at sprite_zoomout("risa") with zoomout

    hide haruto_neutral
    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "That means...tomorrow."

    H "It doesn’t mention the time though."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    User "Should we...find out what’s in that package?"

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "Definitely, if we want more evidence..."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    User "When Mr. Matsu was speaking to Ras...I overheard that Ras won’t be coming to the courier package place. One of Mr. Matsu’s men will just leave the package there."

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "If we want to find out what’s in that package...we’ll have to....ah, nope, leave it."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    hide saya_focused
    show saya_puzzled at sprite_highlight("saya") with zoomin

    S "We’ll have to do what?"

    show saya_puzzled at sprite_zoomout("saya") with zoomout

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    "Haruto looks at her with a serious expression on his face."

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "Well, I have an idea, but it may not work out."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    hide saya_puzzled
    show saya_neutral at sprite_highlight("saya") with zoomin

    S "We'll never know unless we try, right?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "Fine."

    H "We will need to pose as Ras, and collect the package at the address mentioned here."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    show risa_focused at sprite_highlight("risa") with zoomin

    R "You mean...pretend to be this Ras person?"

    show risa_focused at sprite_zoomout("risa") with zoomout

    show haruto_focused at sprite_highlight("haruto") with zoomin

    H "Exactly."

    H "It doesn’t need any special acting talent. We will just need to be at the specified address on the specified day."

    show haruto_focused at sprite_zoomout("haruto") with zoomout

    "A few seconds pass in silence."

    User "I actually remember something else from Mr. Matsu's talk with Ras yesterday..."

    "Their heads dart toward me."

    User "He said something to him like..'I've never even met you. I wonder if you're real.'"

    hide saya_neutral
    show saya_focused at sprite_highlight("saya") with zoomin

    S "So...Mr. Matsu has never seen Ras before?"

    show saya_focused at sprite_zoomout("saya") with zoomout

    "Haruto turns to me and snaps his fingers."

    hide haruto_focused
    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "If Ras isn't coming in person to get the package..."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "That would make it easier for us to get our hands on the package."

    hide risa_focused
    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Ras could look like anything then, and Mr. Matsu's henchman wouldn't know."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    H "He could strike up a conversation with Matsu's delivery guy."

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "And potentially get more information."

    show saya_neutral at sprite_zoomout("saya") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Exactly."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    "Risa looks at me sternly."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "[username]."

    R "Are you going to tell Yuzu about all this?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "Oh, right. I forgot about Yuzu."

    "My mind flickers back to the video Yuzu had sent me yesterday."

    User "Uh...I'll fill her in on this tomorrow. For sure."

    "They all nod at me."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Wait. I think I know someone who can pretend to be Ras."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Who do you have in mind?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Someone Matsu hasn't seen before."

    H "It's....a friend of mine."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Daiki?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Yeah....I'm pretty sure Mr. Matsu has seen Daiki before."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "I'll get him here in a couple more hours. Trust me on this."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "That's quick."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "So, looks like you're a part of the gang now, eh?"

    "Haruto gives me a mild glare."

    "My mind flashes back to the fact of Haruto having once been a part of a gang."

    User "I meant...{i}our{i} gang."

    scene black_bg with fade

    scene umi_grill with dissolve

    "We've been waiting for a few hours since our discussion ended."

    show haruto_neutral with dissolve
    show kenzo_neutral with dissolve

    "Haruto has brought the guy he told us he'd bring, the guy he said would pose as Ras."

    "He gestures toward the wine-red-haired guy."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Guys, I want you to meet Kenzo."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    "The guy, whose name is apparently Kenzo, looks at us and fidgets with his shirt."

    show kenzo_neutral at sprite_highlight("kenzo") with zoomin

    Ke "Hi...hi. My name is Kenzo."

    show kenzo_neutral at sprite_zoomout("kenzo") with zoomout

    User "Hello, Kenzo."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "So, Kenzo, I told you about our investigation yesterday, so I suppose you are well-briefed about all that's been going on."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show kenzo_neutral at sprite_highlight("kenzo") with zoomin

    Ke "Ye - yes..that's right."

    Ke "It would make me glad if..I could be of some help to you."

    show kenzo_neutral at sprite_zoomout("kenzo") with zoomout

    "I smile at him."

    User "We're very glad that you've have opted to help us."

    H "So, [username], do you mind telling him the plan?"

    "I look at Kenzo."

    User "What we need you to do is act like you are this Ras person, and collect the package from Mr. Matsu's henchman."

    show kenzo_neutral at sprite_highlight("kenzo") with zoomin

    Ke "Wai...."

    Ke "So...so I need to pretend I am..."

    Ke "Someone else?"

    show kenzo_neutral at sprite_zoomout("kenzo") with zoomout

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "He has schizophrenia. He was diagnosed at 9 years old."

    H "That's why he can be a bit...off sometimes."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout






    scene emerald_beach with dissolve

    show risa_neutral with dissolve

    "Risa steps outside the restaurant and onto the sands of the beach."

    "I follow her."

    User "Hey, Risa....how's everything going?"

    "She gives me a wry smile."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Have your...parents..ever disagreed with you doing something?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "I am slightly taken aback by her out-of-the-blue question."

    User "Oh yeah, many times."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Hmm."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Why do you ask?"

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Do they...disagree with you doing something right now?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Nope, I’m sure of it."

    "I look into her eyes."

    User "Why...is something going on?"

    "Her eyes look a bit troubled."

    "My parents...don’t happen to agree with some of my choices."

    "I sense the slightest bit of despair in her voice."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "My father….wanted me to study Law, become a Lawyer like him..."

    R "He said a career in the Sciences was not very lucrative."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "How does he feel about you studying Biology?"

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Eh..."

    R "Sometimes, I feel like I shouldn’t have chosen my path. That I should’ve walked in my father’s footsteps...."

    R "Then there wouldn’t be a rift between us now."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Are you happy with your choice?"

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "It makes me happy..."

    R "But does it make {i}him{i} happy?"

    R "I don’t know."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Does your father want you to be happy?"

    "Risa gazes into the distance for a few seconds. She seems to be lost in the view of the ocean."

    User "Risa, seeing you happy doing what you do...makes him happy too. You just don’t know it."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Are you sure?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "You know, yesterday when me and Saya were at the mall...she told me that you’ve taught her so much. More than just serving dishes here at the Grill."

    "Risa’s eyes widen, and her normally stern visage softens slightly."

    "When you chose Biology, what guided that choice?"

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "I....I just chose it. What do you mean?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Nope."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "I don’t get you."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "When you chose Biology, you listened to your heart."

    User "It’s okay to let your heart lead the way.."

    User "You should know this."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Really?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Yep."

    User "I’m sure your father will come to see the value in your passion for Biology."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "We don’t....really talk that much."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "I have a feeling he will reach out to you in the next few days."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Do you?"

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "Yes. I am pretty sure of it."

    "I give her a reassuring smile."

    scene umi_grill_inside

    menu:
        "Yes, I will tell Kai the truth.":
            jump telltruth
        "No, I won't tell him about it right now.":
            jump donttelltruth

    label telltruth:

    "Yes, I will tell Kai the truth."

    User "Kai....can we talk for a moment?"

    "Kai grins at me."

    show kai_happy at sprite_highlight("kai") with zoomin

    Ka "Sure, what is it?"

    show kai_happy at sprite_zoomout("kai") with zoomout

    "I take a few deep breaths."

    User "I..."

    User "You..."

    "He raises an eyebrow and points at his chest."

    show kai_happy at sprite_highlight("kai") with zoomin

    Ka "Me?"

    show kai_happy at sprite_zoomout("kai") with zoomout

    User "No....it’s..."

    "I fumble for the right words to say."

    User "Kai...."

    hide kai_happy
    show kai_puzzled at sprite_highlight("kai") with zoomin

    Ka "Yes...?"

    show kai_puzzled at sprite_zoomout("kai") with zoomout

    User "Mr. Matsu is carrying out....a money-laundering scheme."

    User "He...he’s using this restaurant as a front for his operations."

    show kai_puzzled at sprite_highlight("kai") with zoomin

    Ka "Wha..."

    show kai_puzzled at sprite_zoomout("kai") with zoomout

    "I can feel my fingers go stiff."

    show kai_puzzled at sprite_highlight("kai") with zoomin

    Ka "What in the..."

    hide kai_puzzled
    show kai_happy at sprite_highlight("kai") with zoomin

    Ka "Ahahaha."

    Ka"[username]...."

    Ka "That’s one wild joke."

    show kai_happy at sprite_zoomout("kai") with zoomout

    User "Kai....it’s not a joke."

    "I open the ledger and show it to him."

    User "This is the book where Mr. Matsu..and Yuzu...wrote down transactions and other details."

    hide kai_puzzled
    show kai_sad

    "The confusion on Kai’s face transitions into a frown."

    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "Yuzu?"

    show kai_sad at sprite_zoomout("kai") with zoomout

    "He looks at Yuzu, his eyes wide with disbelief."

    H "I, uh...was involved in it too, Kai."

    User "Mr. Matsu forced them to help him with his scheme."

    User "He threatened to do things like...reduce Yuzu’s salary...if she didn’t help."

    "Kai shakes his head, unable to process what is being spoken."

    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "So what you’re saying is.."

    Ka "My dad..."

    Ka "My....dad...is..."

    show kai_sad at sprite_zoomout("kai") with zoomout

    User "Kai, I know it’s a lot to digest, but –"

    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "Wait, wait."

    show kai_sad at sprite_zoomout("kai") with zoomout

    "He looks at each one of us, then at the ledger."

    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "How long have you all known about this?"

    show kai_sad at sprite_zoomout("kai") with zoomout

    "Haruto and I exchange knowing glances."

    User "Almost...a week."

    hide kai_sad
    show kai_angry

    "Kai’s face contorts with a mix of anger and confusion."

    "His voice grows harsh."

    show kai_angry at sprite_highlight("kai") with zoomin

    Ka "Nah..."

    Ka "You guys are..."

    Ka "You guys are doing this to defame my father, aren’t you?"

    show kai_angry at sprite_zoomout("kai") with zoomout

    User "No, Kai –"

    Y "It’s not like that, Kai."

    show kai_angry at sprite_highlight("kai") with zoomin

    Ka "Just stop, Yuzu."

    show kai_angry at sprite_zoomout("kai") with zoomout

    "Yuzu looks slightly taken aback."

    hide kai_angry
    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "I need to go home."

    Ka "To think about this."

    show kai_sad at sprite_zoomout("kai") with zoomout

    User "Wait –"

    show kai_sad at sprite_highlight("kai") with zoomin

    Ka "I’ll see you tomorrow."

    show kai_sad at sprite_zoomout("kai") with zoomout
    hide kai_sad with dissolve

    "He turns abruptly and dashes out of the restaurant."

    "We all stand in heavy silence."

    "Saya's hands are fidgety, Risa is playing with the left sleeve of her blouse, and Haruto is just staring at the door of the restaurant."

    "The video Yuzu sent me a few days earlier plays in my mind."

    "Though I am slightly nervous, I decide to tell her that I told Saya and Risa about Mr. Matsu's schemes."

    "I turn to face Yuzu, and speak in a quiet voice."

    User "Also...I’m sorry for...doing that. But I had to."

    hide yuzu_anxious
    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "Doing what?"

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    hide haruto_anxious
    show haruto_neutral

    User "I told Saya and Risa about it."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "About what?"

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "Mr..Mr. Matsu’s schemes."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "Oh...."

    Y "You did?"

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "Ye – yes. Didn't you -"

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "I didn’t know that until now."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "O – Oh?"

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "What?"

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "Oh...I just thought you knew..."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "I don’t remember you telling me this before."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "Bu - but..."

    "I take my phone out of my pocket."

    "I play the video from Yuzu."

    "She looks slightly baffled."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "I..."

    Y "I...didn’t send this."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "What do you mean?"

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "I didn’t send this video."

    Y "I swear it was not me."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "Huh...I thought you used some top-tier editing skills to scare me like that, damn!."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "Well...it sure wasn't me who used those 'top-tier editing skills', then."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    User "So, if you didn’t send it...who did?"

    "Yuzu's face goes slightly pale."

    show yuzu_puzzled at sprite_highlight("yuzu") with zoomin

    Y "It could be..."

    show yuzu_puzzled at sprite_zoomout("yuzu") with zoomout

    "Sensing her unease, I decide to change the topic."

    User "We’ll think about it later."

    User "Uh...Yuzu..."

    User "I was just wondering if you’d like to come with me...to some place around here."

    hide yuzu_puzzled
    show yuzu_neutral at sprite_highlight("yuzu") with zoomin

    Y "You mean...go exploring?"

    show yuzu_neutral at sprite_zoomout("yuzu") with zoomout

    User "Yes."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "Well, I guess you guys forgot we are here too."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    User "No -"

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "I'm just kidding."

    H "Anyways, I'm going to head home now and take a nap."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Napping? When we're supposed to be...."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Investigating, yeah. But that can wait, right? I'm getting squirmy right now...I'm so tired."

    S "See y'all."

    "Haruto looks at me."

    show haruto_neutral at sprite_highlight("haruto") with zoomin

    H "See ya."

    show haruto_neutral at sprite_zoomout("haruto") with zoomout

    show saya_neutral at sprite_zoomout("saya") with zoomout

    hide saya_neutral with dissolve
    hide risa_neutral with dissolve
    hide haruto_neutral with dissolve

    "The three of them exit the restaurant, one by one, leaving Yuzu and I facing each other in the near-empty dining area."

    show yuzu_blush at sprite_highlight("yuzu") with zoomin

    Y "I think I’m a bit busy...I can't go exploring right now."

    "I notice a faint glimmer in her eyes."

    hide yuzu_blush
    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Actually, yes, I’ll come with you. I've got nothing else interesting to do right now."

    scene koishi_district with dissolve

    show yuzu_neutral with dissolve

    "After about 10 minutes of walking, we reach a street lined with places I haven’t been to before."

    "I see massage parlors, beauty salons, restaurants and pubs, food stalls, and shops filled with things like phone cases and bracelets."

    "There is a prominent sign board that reads ’Koishi District’."

    "I take a look around."

    "The smell of deep-fried fish emanates from each food stall. They’re really cooking a lot of fish today."

    scene piercingshop with dissolve

    show yuzu_neutral with dissolve

    "We keep walking until we approach a small shack at the end of the street called 'Naik Piercings."

    Y "Hey, let’s check this place out."

    User "Hmm...it looks like a body piercing shop."

    "There are some sliding glass walls, and I can see everything inside the shack."

    "There is a soothing purple lighting in the room, and I can see a cabinet with an array of what I believe are body piercing instruments scattered on top of it."

    show yuzu_neutral at moveleft
    show rahi_neutral at right with dissolve

    "A girl with medium-length brown hair spots me and Yuzu, and steps out of the shack."

    "She is holding a cigarette which trails smoke as she approaches us."

    User "Uh...hello. You must be..."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Rahi?"

    Ra "Yep, you’re looking at her."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    "She holds the cigarette in front of me."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Would you like to share this?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Uh...no thanks. I don't smoke."

    "She shrugs and takes a drag herself, exhaling slowly."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Suit yourself."

    Ra "Come in. It’s cold out here."

    scene piercingshop_inside

    show rahi_neutral at right with dissolve

    show yuzu_neutral at left with dissolve

    "She guides us inside the shack, and the room feels quite stuffy. The glowing purple light falls on our faces."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "So are you here for a piercing? And which spot would you like to get pierced?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    "Yuzu and I glance at each other."

    User "We were just wandering around this area, and we came across your place."

    "Yuzu inspects some of the body piercing tools placed on the cabinet in her hands."

    hide yuzu_neutral
    show yuzu_awe at sprite_highlight("rahi") with zoomin

    Y "Woah, these are..."

    show yuzu_awe at sprite_zoomout("yuzu") with zoomout

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Nuh-uh-uh. Those are not to be touched."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    "Rahi takes the tools from Yuzu’s hands and places them back on the cabinet."

    hide yuzu_awe
    show yuzu_blush at sprite_highlight("rahi") with zoomin

    Y "Sorry..."

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "It’s alright. Why would you know a thing about my craft?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Yeah..."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Is it your first time in this area?"

    hide yuzu_blush
    show yuzu_neutral

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Yeah."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "What do you think of this place? {i}My{i} place, to be specific."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "It’s...interesting."

    User "I’ve never been to a place like this before."

    "Yuzu turns to face Rahi."

    show yuzu_neutral at sprite_highlight("yuzu") with zoomin

    Y "May I ask..."

    Y "What made you decide to become a piercer?"

    show yuzu_neutral at sprite_zoomout("yuzu") with zoomout

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Hmmm..."

    Ra "I got my ear pierced one day...and I couldn’t stop getting more and more piercings after that."

    Ra "I think metal is a strong, firm, unbreakable material..."

    Ra "It has all the traits I want."

    Ra "So after I graduated with my Bachelor’s degree from Art school 2 years ago, I knew just what I would do with it."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Haha...well...what do you feel about a person with no piercings?"

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Why do you ask?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Because...I’ve personally got none. I was just wond –"

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "I actually have a sale on ear piercings this week, 40 percent off."

    Ra "Perhaps...you’d like to get one done?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    "She looks into my eyes, as if anticipating a response."

    User "Uh...you mean...."

    User "You see, I’m kind of...scared of..sharp things."

    User "The needles...just penetrate deep..through your skin..."

    show yuzu_neutral at sprite_highlight("yuzu") with zoomin

    Y "Stop elaborating."

    show yuzu_neutral at sprite_zoomout("yuzu") with zoomout

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Well, that's just how the real world works, my friend."

    Ra "Plus, the needles are sterilized, so no need to worry."

    Ra "You're in safe hands."

    "She gives me a faint smile."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    "Yuzu and I exchange glances, silently debating whether I should go for it."

    "If I get the piercing done, I can add this experience to my list of my experiences here in Okinawa."

    "Should I take the opportunity?"

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "So, are you up for it?"

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    menu:
        "Yes, I want it.":
            jump getpierced
        "No thank you, I'll pass.":
            jump dontgetpierced

    label dontgetpierced:

    scene piercingshop_inside

    User "No thank you, I'll pass."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "Hmm...fair enough."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "But...I’d really like to know..."

    User "What’s the story behind this horned elephant tattoo of yours?"

    "I point a finger at the horned elephant tattoo on her left thigh."

    hide rahi_neutral
    show rahi_smirk at sprite_highlight("rahi") with zoomin

    Ra "Ah, getting personal now, are we?"

    show rahi_smirk at sprite_zoomout("rahi") with zoomout

    "She chuckles."

    show rahi_smirk at sprite_highlight("rahi") with zoomin

    Ra "My zodiac animal is the bull."

    Ra "The elephant symbolizes power and loyalty, and the bull symbolizes strength and grit. Combine the two, and you’ve got an indestructible chunk of cells."

    show rahi_smirk at sprite_zoomout("rahi") with zoomout

    User "You tattooed it onto yourself?"

    show rahi_smirk at sprite_highlight("rahi") with zoomin

    Ra "Yep."

    show rahi_smirk at sprite_zoomout("rahi") with zoomout

    hide yuzu_neutral
    show yuzu_awe

    User "Did it...hurt?"

    hide rahi_smirk
    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "It just felt a bit ticklish. Like a fish nibbling at my flesh at one of those spas."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    show yuzu_awe at sprite_highlight("yuzu") with zoomin

    Y "Ooohh..."

    show yuzu_awe at sprite_zoomout("yuzu") with zoomout

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "But don’t worry if you’re not up for getting pierced right now. Just enjoy the district and maybe come back when you’re ready."

    Ra "Except from 11 pm to 7 am."

    Ra "You know where to find me."

    show rahi_neutral at sprite_zoomout("rahi") with zoomout

    User "Thanks for the chat, Rahi."

    show rahi_neutral at sprite_highlight("rahi") with zoomin

    Ra "It's a pleasure."

    scene piercing_shop with dissolve

    show yuzu_neutral with dissolve

    "Me and Yuzu step out of the shack and onto the street."

    scene koishi_district with dissolve

    "We start walking back to Umi Grill, passing quirkily-lit shops and food stalls on the way."

    "And as we head back, I wonder how much more of this place I have yet to explore in the coming days."

    stop music fadeout 1.0

    scene black_bg with fade

    #jump script_ch6_ras_g_np

return