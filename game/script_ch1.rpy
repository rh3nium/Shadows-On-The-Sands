# Characters
define Y = Character("Yuzu")
define Mr = Character("Mr. Matsu")
define H = Character("Haruto")
define S = Character("Saya")
define R = Character("Risa")
define Ka = Character("Kai")
define D = Character("Daiki")
define Ke = Character("Kenzo")
define Ra = Character("Rahi")
define SR = Character("Saya & Risa")
# Define User character after username and gender are input
define User = Character("", dynamic=True)

# Character Images
image matsu_neutral = im.Scale("images/characterimages/mrmatsu/matsu_neutral.png", 768, 1128) #DONE
image matsu_happy = im.Scale("images/characterimages/mrmatsu/matsu_happy.png", 768, 1128)
image matsu_anxious = im.Scale("images/characterimages/mrmatsu/matsu_anxious.png", 512, 768)
image matsu_angry = im.Scale("images/characterimages/matsu/matsu_angry.png", 768, 1128)
image matsu_thinking = im.Scale("images/characterimages/mrmatsu/matsu_thinking.png", 768, 1128)
image matsu_shock = im.Scale("images/characterimages/mrmatsu/matsu_shock.png", 768, 1128)

image yuzu_neutral = im.Scale("images/characterimages/yuzu/yuzu_neutral.png", 768, 1128) #DONE
image yuzu_happy = im.Scale("images/characterimages/yuzu/yuzu_happy.png", 768, 1128) #DONE
image yuzu_sad = im.Scale("images/characterimages/yuzu/yuzu_sad.png", 768, 1128) #DONE
image yuzu_blush = im.Scale("images/characterimages/yuzu/yuzu_blush.png", 768, 1128) #DONE
image yuzu_anxious = im.Scale("images/characterimages/yuzu/yuzu_anxious.png", 768, 1128) 
image yuzu_crying = im.Scale("images/characterimages/yuzu/yuzu_crying.png", 768, 1128) #DONE
image yuzu_angry = im.Scale("images/characterimages/yuzu/yuzu_angry.png", 512, 768)
image yuzu_shock = im.Scale("images/characterimages/yuzu/yuzu_shock.png", 768, 1128) #DONE
image yuzu_thinking = im.Scale("images/characterimages/yuzu/yuzu_thinking.png", 768, 1128)
image yuzu_kneesdown = im.Scale("images/characterimages/yuzu/yuzu_kneesdown.png", 768, 1128)
image yuzu_bindi = im.Scale("images/characterimages/yuzu/yuzu_bindi.png", 768, 1128) #DONE
image yuzu_facegems = im.Scale("images/characterimages/yuzu/yuzu_facegems.png", 768, 1128) #DONE
image yuzu_creepy = im.Scale("images/characterimages/yuzu/yuzu_creepy.png", 768, 1128) #DONE
image yuzu_creepy2 = im.Scale("images/characterimages/yuzu/yuzu_creepy2.png", 768, 1128) #DONE
image yuzu_creepy3 = im.Scale("images/characterimages/yuzu/yuzu_creepy3.png", 768, 1128) #DONE
image yuzu_neckcrack = im.Scale("images/characterimages/yuzu/yuzu_neckcrack.png", 768, 1128) #DONE

image saya_neutral = im.Scale("images/characterimages/saya/saya_neutral.png", 768, 1128) #DONE
image saya_happy = im.Scale("images/characterimages/saya/saya_happy.png", 768, 1128) #DONE
image saya_sad = im.Scale("images/characterimages/saya/saya_sad.png", 768, 1128) #DONE
image saya_blush = im.Scale("images/characterimages/saya/saya_blush.png", 768, 1128)
image saya_anxious = im.Scale("images/characterimages/saya/saya_anxious.png", 768, 1128)
image saya_angry = im.Scale("images/characterimages/saya/saya_angry.png", 768, 1128)
image saya_thinking = im.Scale("images/characterimages/saya/saya_thinking.png", 768, 1128) #DONE
image saya_crying = im.Scale("images/characterimages/saya/saya_crying.png", 768, 1128) #DONE
image saya_shock = im.Scale("images/characterimages/saya/saya_shock.png", 768, 1128)
image saya_puzzled = im.Scale("images/characterimages/saya/saya_puzzled.png", 768, 1128)

image risa_neutral = im.Scale("images/characterimages/risa/risa_neutral.png", 768, 1128) #DONE
image risa_happy = im.Scale("images/characterimages/risa/risa_happy.png", 768, 1128) #DONE
image risa_sad = im.Scale("images/characterimages/saya/risa_sad.png", 768, 1128)
image risa_blush = im.Scale("images/characterimages/risa/risa_blush.png", 768, 1128)
image risa_anxious = im.Scale("images/characterimages/risa/risa_anxious.png", 768, 1128)
image risa_angry = im.Scale("images/characterimages/risa/risa_angry.png", 768, 1128)
image risa_thinking = im.Scale("images/characterimages/risa/risa_thinking.png", 768, 1128) #DONE
image risa_shock = im.Scale("images/characterimages/risa/risa_shock.png", 768, 1128)
image risa_puzzled = im.Scale("images/characterimages/risa/risa_puzzled.png", 768, 1128)

image haruto_neutral = im.Scale("images/characterimages/haruto/haruto_neutral.png", 768, 1128) #DONE
image haruto_happy = im.Scale("images/characterimages/haruto/haruto_happy.png", 768, 1128)
image haruto_smirk = im.Scale("images/characterimages/haruto/haruto_smirk.png", 768, 1128) #DONE
image haruto_anxious = im.Scale("images/characterimages/haruto/haruto_anxious.png", 768, 1128)
image haruto_thinking = im.Scale("images/characterimages/haruto/haruto_thinking.png", 768, 1128)
image haruto_shock = im.Scale("images/characterimages/haruto/haruto_shock.png", 768, 1128)

image kai_neutral = im.Scale("images/characterimages/kai/kai_neutral.png", 768, 1128) #DONE
image kai_happy = im.Scale("images/characterimages/kai/kai_happy.png", 768, 1128)
image kai_sad = im.Scale("images/characterimages/kai/kai_sad.png", 768, 1128)
image kai_smirk = im.Scale("images/characterimages/kai/kai_smirk.png", 768, 1128)
image kai_thinking = im.Scale("images/characterimages/kai/kai_thinking.png", 768, 1128)
image kai_anxious = im.Scale("images/characterimages/kai/kai_anxious.png", 768, 1128)
image kai_angry = im.Scale("images/characterimages/kai/kai_angry.png", 768, 1128)
image kai_disapproving = im.Scale("images/characterimages/kai/kai_disapproving.png", 768, 1128)
image kai_shock = im.Scale("images/characterimages/kai/kai_shock.png", 768, 1128)

image daiki_neutral = im.Scale("images/characterimages/daiki/daiki_neutral.png", 768, 1128) #DONE
image daiki_happy = im.Scale("images/characterimages/daiki/daiki_happy.png", 768, 1128) 
image daiki_smirk = im.Scale("images/characterimages/daiki/daiki_smirk.png", 768, 1128) #DONE
image daiki_anxious = im.Scale("images/characterimages/daiki/daiki_anxious.png", 768, 1128)
image daiki_angry = im.Scale("images/characterimages/daiki/daiki_angry.png", 768, 1128)
image daiki_thinking = im.Scale("images/characterimages/daiki/daiki_thinking.png", 768, 1128)

image kenzo_neutral = im.Scale("images/characterimages/kenzo/kenzo_neutral.png", 768, 1128)
image kenzo_happy = im.Scale("images/characterimages/kenzo/kenzo_happy.png", 768, 1128)
image kenzo_smirk = im.Scale("images/characterimages/kenzo/kenzo_smirk.png", 768, 1128)
image kenzo_anxious = im.Scale("images/characterimages/kenzo/kenzo_anxious.png", 768, 1128)
image kenzo_angry = im.Scale("images/characterimages/kenzo/kenzo_angry.png", 768, 1128)
image kenzo_thinking = im.Scale("images/characterimages/kenzo/kenzo_thinking.png", 768, 1128)

image rahi_neutral = im.Scale("images/characterimages/rahi/rahi_neutral.png", 768, 1128) #DONE
image rahi_happy = im.Scale("images/characterimages/rahi/rahi_happy.png", 768, 1128) #DONE
image rahi_blush = im.Scale("images/characterimages/rahi/rahi_blush.png", 768, 1128) #DONE
image rahi_smirk = im.Scale("images/characterimages/rahi/rahi_smirk.png", 768, 1128) #DONE
image rahi_anxious = im.Scale("images/characterimages/rahi/rahi_anxious.png", 768, 1128)
image rahi_angry = im.Scale("images/characterimages/rahi/rahi_angry.png", 768, 1128)
image rahi_thinking = im.Scale("images/characterimages/rahi/rahi_thinking.png", 768, 1128)

# Background Images
image umigrill_inside_noon = "images/bgimages/umi_grill_inside_noon.png"
image umigrill_inside_evening = "images/bgimages/umi_grill_inside_evening.png"
image umigrill_inside_night = "images/bgimages/umi_grill_inside_night.png"

image umigrill_outside_noon = "images/bgimages/umi_grill_outside_noon.png"
image umigrill_outside_evening = "images/bgimages/umi_grill_outside_evening.png"
image umigrill_outside_night = "images/bgimages/umi_grill_outside_night.png"

image emeraldbeach_noon = im.Scale("images/bgimages/emerald_beach_noon.png", 1920, 1080)
image emeraldbeach_evening = im.Scale("images/bgimages/emerald_beach_evening.png", 1920, 1080)
image emeraldbeach_night = im.Scale("images/bgimages/emerald_beach_night.png", 1920, 1080)

image foodstall = "images/bgimages/food_stall.png"

image piercingshop = "images/bgimages/piercing_shop.png"

image yuzu_closeup = im.Scale("images/bgimages/yuzu_closeup.png", 1920, 1080)
image saya_closeup = im.Scale("images/bgimages/saya_closeup.png", 1920, 1080)
image haruto_closeup = im.Scale("images/bgimages/haruto_closeup.png", 1920, 1080)
image risa_closeup = "images/bgimages/risa_closeup.png"
image matsu_closeup = "images/bgimages/matsu_closeup"
image kai_closeup = "images/bgimages/kai_closeup.png"
image daiki_closeup = "images/bgimages/kai_closeup.png"
image rahi_closeup = im.Scale("images/bgimages/rahi_closeup.png", 1920, 1080)

image black_bg = im.Scale("images/bgimages/blackbg.png", 1920, 1080)

# Fonts
define gui.text_font = "fonts/PT_Serif/PTSerif-Regular.ttf"
define gui.name_text_font = "fonts/PT_Serif/PTSerif-Bold.ttf"
define gui.interface_text_font = "fonts/PT_Serif/PTSerif-Regular.ttf"
define gui.bold_font = "fonts/PT_Serif/PTSerif-Bold.ttf"
define gui.text_size = 30


#### Start Screens ####
label start:

# Ask user to enter their name, ensure it's not empty
    $ username = ""
    while not username:
        $ username = renpy.input("Please enter your name:")
        $ username = username.strip()  # Remove any trailing whitespace
        
# Ask user to select their gender
        menu:
            "Please select your gender:"
            "Male":
                $gender = "Male"
                jump script_ch1
            "Female":
                $gender = "Female"
                jump script_ch1
            "Other":
                $gender = "Other"
                jump script_ch1

    # Define User character with entered username and selected gender
    $ User = Character(username, gender=gender)


#### Part 1 ####

    label script_ch1:

    $ User = Character(username, gender=gender)

    scene emeraldbeach_evening

    play music "audio/Sychic-Saturn.ogg"

    "It is my first evening in Okinawa, Japan."

    "Sand makes its way into my sandals as I step onto the shore of Emerald Beach."

    "I see an endless array of restaurants, and the electronic music tunes blasting in each restaurant overlap with one another. Throngs of people are in each restaurant, dancing."

    "The wind is cool and salty, a stark contrast from the warm breeze in my city of Bengaluru in India, I left behind just days ago."

    "The only place where I have visited an 'Emerald Beach' is Goa, a coastal state in India, where I went with my cousins a few years ago."
    
    "I finally approach the restaurant I am looking for directions to on my phone. I had applied for a job as a restaurant hostess here two weeks ago, and had secured the job after an interview with the restaurant manager."

    "A hanging wooden plank at the entrance of the place reads 'Umi Grill'."

    "There is another plank under it with the tagline 'Sea-tisfy your tastebuds.'"

    scene umigrill_inside_evening with dissolve

    "As I step inside the restaurant, I notice the air is thick with the aroma of grilled fish and prawns, and the sound of crashing waves on the beach is muffled by the booming music."

    "My heart races with excitement."

    show matsu_neutral with dissolve

    "A middle-aged man wearing a button-down shirt and trousers approaches me. He's the same man who conducted my job interview through video call."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Oh hello there, you must be [username]. I'm Mr. Toshiru Matsu. Welcome to Umi Grill. We are delighted about having you join our team."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "Ah yes, that's me. [username]. Thank you, Mr. Matsu. It's nice to see you again. I'm eager to start working here."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "So you've signed up to work as a host in the evening shift. You will need to be here every evening, from 5 p.m. to 11 p.m."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    User "I understand."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Now let me walk you through your responsibilities as a host here."

    Mr "Your duties will include greeting customers, escorting them to their tables, managing waitlists, managing reservations, giving customers menus, explaining to them the menu items and any special offers."

    Mr "You must also communicate with the waiters and kitchen staff, and handle any inquiries or complaints the customers may have."

    Mr "You must also maintain the host stand."
    
    User "What exactly is a 'host stand'?"
    
    Mr "I'm getting to that. This host stand is the area where you hosts will usually stand and greet guests. "

    Mr "The menus will be kept on this desk. There is also a computer for you to record and manage the reservations."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "I nod, absorbing every word."

    "He pulls out a grey brooch with my name, [username], engraved on it from his pocket and hands it to me."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "Also, you'll need to wear this at all times."

    show matsu_neutral at sprite_zoomout("matsu") with zoomout

    "I take the pin and put it on my shirt."

    show matsu_neutral at sprite_highlight("matsu") with zoomin

    Mr "If you have any questions, don't hesitate to approach me."

    Mr "And...one more thing. Customer satisfaction is our top priority here at Umi Grill."

    Mr "We always strive to ensure that every guest leaves our restaurant satisifed."

    hide matsu_neutral with dissolve

    show yuzu_happy with dissolve

    "A girl wearing a cami top and wrap around skirt approaches me."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Oh, you must be the new host, right?"

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "Yeah, my name is [username]. It's nice to meet you. Wow, it's really busy this evening, isn't it?"

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Oh, definitely! The evenings are always bustling here, especially with the beach crowd."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "I can imagine. It's amazing how many people come to Umi Grill."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Yeah. But it's also a lot of hard work to make sure they are satisfied! By the way, my name is Yuzu. Yuzu Shibata."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "I like your name. It's only been a few days since I arrived here, but....I don't feel like leaving this place."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Aw, thanks! Well, that's Okinawa for you. Once you step in, you never feel like stepping out."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "Mhm."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Well, you'll get the hang of working here in a bit. Just follow what I am doing."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    "Yuzu and I spend time greeting guests with 'Hello' or 'Welcome to Umi Grill', and ensuring that the atmosphere is pleasant."

    "I find that initially my voice is drowned by the crashing waves on the beach, but I get louder after a while."

    "I resist the urge to tap my feet along to the ambient music playing."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Hey, [username], why don't we grab a bite to eat at that food stall down the street? I'm craving some Onigiri."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "What's Onigiri?"

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Rice balls wrapped in seaweed."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "Have you been to that stall before?"

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "I've been there a couple of times while working."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "Perfect. Lead the way, Yuzu."

    scene foodstall with dissolve
    
    show yuzu_happy with dissolve
    show saya_happy at right3 with dissolve
    show risa_neutral at left3 with dissolve

    "We and two other hostesses walk down the shore to a stall."

    "The smell of salmon and White Rice fills my nostrils. I don't really mind all the strong smells of seafood even though I am a vegetarian."

    "Yuzu looks at the chef in the food stall, who is busy rolling steamed rice into small balls."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "I'd like to order one plate of Onigiri filled with grilled salmon flakes."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    "My eyes dart across the items on the menu board."

    User "I'll have a plate of Negi Miso Onigiri."

    "As we wait for our food to arrive, I strike up a conversation with the other hostesses who have joined us."

    User "So, how long have you all been working at Umi Grill?"

    show saya_happy at sprite_highlight("saya") with zoomin

    S "I've been here for about a year now. It's a fun job, especially during the busy season when the beach is packed with tourists."

    show saya_happy at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "I've been working here for two years. I started as a part-time hostess while I was in my first year of college, but I enjoyed it so much that I decided to stay on."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Yeah, the atmosphere here is unlike anywhere else. Plus, Mr. Matsu is a great boss. He really takes care of his employees."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "I'm glad to hear that. I'm really excited to be a part of the team."

    show saya_happy at sprite_highlight("saya") with zoomin

    S "And we're glad you have joined us!"

    show saya_happy at sprite_zoomout("saya") with zoomout

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Mr. Matsu has owned Umi Grill for 17 years."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "17 years? I had not known about that until now."

    User "That's really commendable. His dedication towards the restaurant...he must really love to serve people great food."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "I'm currently studying to become a marine biologist. I am fascinated by the ocean and aquatic life. Always have been since I was a kid."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    show saya_happy at sprite_highlight("saya") with zoomin

    S "I study psychology. Writing poems is my passion. I want to publish my own book of poetry one day."

    show saya_happy at sprite_zoomout("saya") with zoomout

    User "That sounds amazing! Well, I am studying Product Design. I want to work at a Product Design studio or open my own company someday."

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Impressive."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "Our food arrives, and the aroma of freshly made Onigiri fills the air. I take a moment to admire the neat presentation of the rice balls, each wrapped in a delicate sheet of seaweed."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Dig in, [username]! You're going to love these Onigiri."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    User "I can't wait to try them."

    "I take a bite of the Negi Miso Onigiri, savoring the combination of flavors. The savory miso filling and the crunch of the fresh green onions create a delightful harmony on my taste buds."

    User "Wow, this is delicious! I never knew vegetarian sushi could be so flavorful."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Haha, well, it's not Sushi, it's Onigiri. Okinawan cuisine has something for everyone, even vegetarians like you. You'll find plenty of tasty options here."

    Y "And I forgot to tell you this earlier, but...."

    Y "I'm studying Anthropology at college. I'm interested in learning about what our society was like in the past."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    show saya_happy at sprite_highlight("saya") with zoomin

    S "Eh, that's sweet Yuzu, but I've gotta admit...I'm not really into cavemen...they're not my type."

    show saya_happy at sprite_zoomout("saya") with zoomout

    "I suppress a chuckle."

    "After finishing our meals, we bid farewell to the food stall owner and make our way back to Umi Grill, ready to continue our evening shift."

    scene emeraldbeach_evening with dissolve
    show yuzu_happy with dissolve
    show saya_neutral at right3 with dissolve
    show risa_neutral at left3 with dissolve

    "As we walk, I can't shake off the feeling of excitement and anticipation for the adventures that lie ahead in Okinawa."

    scene umigrill_inside_evening with dissolve
    show yuzu_happy with dissolve
    show saya_neutral at right3 with dissolve
    show risa_neutral at left3 with dissolve

    "As we step back into the restaurant, the lively atmosphere envelops us once again, and I can't help but feel a sense of belonging in this bustling seaside eatery."

    "Yuzu gives me a reassuring smile as we resume our duties as hostesses, seamlessly slipping back into the rhythm of the evening shift."

    "Despite the hectic pace, there's a certain joy in the hustle and bustle of the restaurant, and I find myself energized by the excitement of it all."

    "Yuzu turns to me."

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "So..."

    Y "I didn't ask you this earlier..but I think I should have."

    Y "Where are you from?"

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    show saya_neutral at sprite_highlight("saya") with zoomin

    S "Why don't we each answer that question, one by one?"

    show saya_neutral at sprite_zoomout("saya") with zoomout

    User "I'll go first, because Yuzu asked me."

    User "I'm from India."

    User "I was born and raised in a city called Bengaluru, and I moved here a few days ago for college."

    User "Bengaluru is a large city..."

    User "Not really a beachy city though."

    User "You could spend a lifetime exploring it."

    User "The amount of traffic on the roads here isn't even half the amount over there every day."

    hide yuzu_happy
    show yuzu_blush

    show yuzu_blush at sprite_highlight("yuzu") with zoomin

    Y "Wait....India?"

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    "She seems to hesitate for a bit."

    show yuzu_blush at sprite_highlight("yuzu") with zoomin

    Y "I, uh..."

    Y "I am very much into Ayurveda, actually."
 
    Y "I...know many home remedies by heart."

    Y "Such as..."

    Y "Nimbu juice."

    Y "Which is lemon juice."

    Y "The benefits of Nimbu juice include clear skin, weight loss, good digestion, good blood sugar levels -"

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    User "Whoa...you've got some good general knowledge."

    User "More knowledge than I have, to be frank."

    show yuzu_blush at sprite_highlight("yuzu") with zoomin

    Y "Ehe...thanks."

    Y "I...sometimes make Nimbu juice for myself.."

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    User "Really? Could I maybe...try it sometime?"

    show yuzu_blush at sprite_highlight("yuzu") with zoomin

    Y "Uh..."

    Y "Oh...well, of course I'll let you try it sometime...but...."

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    User "I'm sure it will taste great."

    "Her eyes light up and she gives me a shy smile."

    User "Now, I'd like to know more about where you were born."

    hide yuzu_blush
    show yuzu_happy
    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Oh, me? Uh...I was born right here in Okinawa. Not in the city though, in a small town."

    Y "A beachside town."

    Y "Since I was born, my mother has worked as a pharmacist...and my father has worked as a civil engineer in the government."
    
    Y "My town was so small that I knew all my neighbors' first and last names by heart."

    Y "As my neighbors moved out, I sort of forgot their names."

    hide yuzu_happy
    show yuzu_blush

    Y "I guess that happens over time, doesn't it? Ehe...."

    show yuzu_blush at sprite_zoomout("yuzu") with zoomout

    User "Do you prefer the city over your town?"

    hide yuzu_blush
    show yuzu_happy

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Um....that's a hard question."

    Y "I'll have to say I like both of them equally."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    hide saya_neutral
    show saya_happy

    show saya_happy at sprite_highlight("saya") with zoomin

    S "So...I guess I'll have a go now...hehe."
    
    S "I was born in the city here in Okinawa. The city was always...bustling."

    show saya_happy at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "I was born here in the city as well."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    User "How did you like the city?"

    show saya_happy at sprite_highlight("saya") with zoomin

    S "I loved it! That's why I never moved out. I live in an apartment there."

    S "Come on Risa, don't hide the fact that you love it too!"

    show saya_happy at sprite_zoomout("saya") with zoomout

    show risa_neutral at sprite_highlight("risa") with zoomin

    R "Eh....it's alright."

    R "I prefer staying somewhere less....crowded."

    R "Like my college town."

    R "It's so peaceful there...I like taking a walk outside in the gardens there every morning."

    show risa_neutral at sprite_zoomout("risa") with zoomout

    "As the night wears on, I become more confident in my role as a host, greeting guests with a warm smile and guiding them to their tables with ease."

    "I no longer need Yuzu's guidance."

    "The sound of laughter and conversation fills the air, creating a vibrant backdrop to the evening."

    "As the clock strikes eleven and our shift comes to an end, I bid farewell to my fellow hostesses with a sense of gratitude for their warm welcome and camaraderie."

    show saya_happy at sprite_highlight("saya") with zoomin

    S "We have a text messaging group - two groups, actually - one with Mr. Matsu and the rest of the staff, and one with just the hosts...us, I mean. I'll add you to both of them."

    show saya_happy at sprite_zoomout("saya") with zoomout

    show yuzu_happy at sprite_highlight("yuzu") with zoomin

    Y "Wait [username], one more thing. Remember to wear sandals tomorrow, I wouldn't advise you to wear sneakers on the beach."

    show yuzu_happy at sprite_zoomout("yuzu") with zoomout

    "I look down at my shoes."

    User "I'll remember that. Well...I'll try to remember."

    scene emeraldbeach_night with dissolve

    "Stepping out into the cool night air, I feel a sense of excitement for the adventures that lie ahead."

    "Tonight may have been just the beginning, but I know that with each passing day, I will continue to discover new joys and experiences in this beautiful corner of the world."

    "I open my phone to see that I am added to two group chats, and there is also one new message in the Umi Grill Staff Group."

    Y "{i}[username] has joined our team. Welcome Umi Grill, [username]!{i}"

    "As I make my way back to my college dorm on my motorbike, the sound of the waves crashing against the shore fills me with a sense of peace and contentment."

    "As I ride back home, I can't help but feel excited to be at the restaurant again the next day."

    stop music fadeout 1.0

    scene black_bg with fade

    jump script_ch2

return