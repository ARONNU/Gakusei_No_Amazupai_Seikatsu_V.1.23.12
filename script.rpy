# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Shake Effect
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

        class NonNegative(int):
            def __new__(cls, value, *args, **kwargs):
                return  super(cls, cls).__new__(cls, max(value, 0))

            def __add__(self, other):
                res = super(NonNegative, self).__add__(other)
                return self.__class__(max(res, 0))

            def __sub__(self, other):
                res = super(NonNegative, self).__sub__(other)
                return self.__class__(max(res, 0))

            def __mul__(self, other):
                res = super(NonNegative, self).__mul__(other)
                return self.__class__(max(res, 0))

            def __div__(self, other):
                res = super(NonNegative, self).__div__(other)
                return self.__class__(max(res, 0))

            def __str__(self):
                return "%d" % int(self)

            def __repr__(self):
                return "NonNegative(%d)" % int(self)


define main = Character("[player_name]")
define mom = Character("Mom")
define kai = Character("[some_character]")
define teacher = Character("Ms. Sungji")
define lian = Character("Lian Hui")
define najma = Character("Najma Awad")
define ayani = Character("Ayani Isa")
define chihiro = Character("Chihiro Isii")
define unknown = Character("Unknown Voice")
define hana = Character("Hana")
define guard = Character("Guard")
define justin = Character("Justin")

# Scenes
image home = "scenes/bg_livingroom.png"
image kitchen = "scenes/home.png"
image classroom m = "scenes/bg 1.png"
image classroom a = "scenes/bg 1 (Afternoon).png"
image hallway = "scenes/hallway.png"
image out school = "scenes/school entrance.png"
image room = "scenes/bg_bedroom.png"
image cafeteria = "scenes/bg_cafeteria.png"
image restroom = "scenes/bathroom.png"
image field = "scenes/school field 1.png"
image street = "scenes/town.png"
image clubroom = "scenes/bg 2.png"
image park = "scenes/Park.png"
image hangout = "scenes/AyaniHangoutSpot.png"
image roadside = "scenes/Roadside.png"
image scroom = "scenes/StudentCouncilRoom.png"

# Mom
image mom happy =  im.Scale("characters/adults/Mom/Mother_happy.png", 1620, 1020)
image mom = im.Scale("characters/adults/Mom/Mother_default.png", 1620, 1020)
image mom sad = im.Scale("characters/adults/Mom/Mother_sad.png", 1620, 1020)
image mom angry = im.Scale("characters/adults/Mom/Mother_angry.png", 1620, 1020)

# Teacher
image teacher happy = im.Scale("characters/adults/Teacher/Teacher_happy.png", 1620, 1020)
image teacher = im.Scale("characters/adults/Teacher/Teacher_default.png", 1620, 1020)
image teacher angry = im.Scale("characters/adults/Teacher/Teacher_angry.png", 1620, 1020)

# Ayani
image ayani happy = im.Scale("characters/students/Ayani/Ayani_happy.png", 1620, 1020)
image ayani = im.Scale("characters/students/Ayani/Ayani_default.png", 1620, 1020)
image ayani sad = im.Scale("characters/students/Ayani/Ayani_sad.png", 1620, 1020)
image ayani angry =im.Scale( "characters/students/Ayani/Ayani_angry.png", 1620, 1020)
image ayani shock = im.Scale("characters/students/Ayani/Ayani_shock.png", 1620, 1020)
image ayani highlight = im.Scale("characters/students/Ayani/Ayani_highlighted.png", 1620, 1020)

# Chihiro
image chihiro happy = im.Scale("characters/students/Chi/Chi_happy.png", 1620, 1020)
image chihiro = im.Scale("characters/students/Chi/Chi_default.png", 1620, 1020)
image chihiro sad = im.Scale("characters/students/Chi/Chi_sad.png", 1620, 1020)
image chihiro angry = im.Scale("characters/students/Chi/Chi_angry.png", 1620, 1020)
image chihiro shock = im.Scale("characters/students/Chi/Chi_shocked.png", 1620, 1020)
image chihiro highlight = im.Scale("characters/students/Chi/Chi_highlight.png", 1620, 1020)

# Kai
image kai happy = im.Scale("characters/students/Kai/kai_happy.png", 1620, 1020)
image kai = im.Scale("characters/students/Kai/kai_default.png", 1620, 1020)
image kai sad = im.Scale("characters/students/Kai/kai_sad.png", 1620, 1020)
image kai angry = im.Scale("characters/students/Kai/kai_angry.png", 1620, 1020)
image kai shocked = im.Scale("characters/students/Kai/kai_shocked.png", 1620, 1020)

# Lian Hui
image lian happy = im.Scale("characters/students/Lian/Lian_happy.png", 1620, 1020)
image lian = im.Scale("characters/students/Lian/Lian_default.png", 1620, 1020)
image lian sad = im.Scale("characters/students/Lian/Lian_sad.png", 1620, 1020)
image lian angry = im.Scale("characters/students/Lian/Lian_angry.png", 1620, 1020)
image lian shock = im.Scale("characters/students/Lian/Lian_shocked.png", 1620, 1020)
image lian highlight = im.Scale("characters/students/Lian/Lian_highlight.png", 1620, 1020)

# Najma
image najma happy = im.Scale("characters/students/Najma/Najma_happy.png", 1620, 1020)
image najma = im.Scale("characters/students/Najma/Najma_default.png", 1620, 1020)
image najma sad = im.Scale("characters/students/Najma/Najma_sad.png", 1620, 1020)
image najma angry = im.Scale("characters/students/Najma/Najma_angry.png", 1620, 1020)
image najma shock =im.Scale( "characters/students/Najma/Najma_shocked.png", 1620, 1020)
image najma highlight =im.Scale( "characters/students/Najma/Najma_highlight.png", 1620, 1020)

#Hana Chien
image hana happy = im.Scale("characters/students/Hana/Hana_happy.png", 1620, 1020)
image hana = im.Scale("characters/students/Hana/Hana_default.png", 1620, 1020)
image hana sad = im.Scale("characters/students/Hana/Hana_sad.png", 1620, 1020)
image hana angry = im.Scale("characters/students/Hana/Hana_angry.png", 1620, 1020)
image hana shock = im.Scale("characters/students/Hana/Hana_shock.png", 1620, 1020)

#Justin
image justin happy = im.Scale("characters/students/Justin/Justin_happy.png", 1620, 1020)
image justin = im.Scale("characters/students/Justin/Justin_default.png", 1620, 1020)
image justin angry = im.Scale("characters/students/Justin/Justin_angry.png", 1620, 1020)
image justin shock = im.Scale("characters/students/Justin/Justin_shocked.png", 1620, 1020)

#Guard
image guard = im.Scale("characters/adults/Mrs.Dimaapi/Ms_Dimaapi.png", 1620, 1020)

#splash art scene
image bad ending = im.Scale("splashart/SplashArt_BadEnding.png", 1620, 1020)
image ayani ending = "splashart/Splashart_Ayani.png"
image chi ending = "splashart/Splashart_Chihiro.png"
image lian ending = "splashart/SplashArt_Lian.png"
image najma ending = "splashart/SplashArt_Najma.png"
image neutral ending = im.Scale("splashart/SplashArt_NeutralEnding.png", 1620, 1020)

# point and click part
image Library = "minigame/Childhood_Library.png"
image Library Blurred= "minigame/Childhood_Library_Blurred.png"

image ALbookshelf = "minigame/AL/Childhood_Bookshelf_AyaniLian.png"
image ALbook = im.Scale("minigame/AL/Childhood_childrensbook_AyaniLian.png", 1020, 720)
image ALpostcard= im.Scale("minigame/AL/Childhood_citylights_AyaniLian.png", 1020, 720)
image ALengraving = im.Scale("minigame/AL/Childhood_engraving_AyaniLian.png", 1020, 720)
image ALletter = im.Scale("minigame/AL/Childhood_letter_AyaniLian.png", 1020, 720)
image ALpicture = im.Scale("minigame/AL/Childhood_pic_AyaniLian.png", 1020, 720)

image NCbookshelf =  im.Scale("minigame/NC/Childhood_bookshelf_NamjaChi.png", 1020, 720)
image NCcomic = im.Scale("minigame/NC/Childhood_comicposter_NajmaChi.png", 1020, 720)
image NCpicture=  im.Scale("minigame/NC/Childhood_pic_NamjaChi.png", 1020, 720)
image NCengraving =  im.Scale("minigame/NC/Childhood_engraving_NamjaChi.png", 1020, 720)
image NCletter =  im.Scale("minigame/NC/Childhood_letter_NamjaChi.png", 1020, 720)

image Fridge = "minigame/Fridge1.png"

# stats stuff shenanigans
default grades = NonNegative(0)
default relationship_with_mom = NonNegative(5)
default relationship_with_lian = NonNegative(0)
default relationship_with_najma = NonNegative(0)
default relationship_with_ayani = NonNegative(0)
default relationship_with_chihiro = NonNegative(0)
default relationship_with_kai = NonNegative(0)
default reputation = NonNegative(0)

# quiz pointing system
default score = NonNegative(0)
default score_02 = NonNegative(0)

# The game starts here.

label start:
    play music "audio/early.ogg" loop
    scene black
    show screen gameUI
    $ player_name="You"
    $ some_character = "???"

    "High school is said to be the most exciting chapter of your life."
    "A time where you may set so many goals to achieve to feel fulfillment,"
    "Try new things and make memories you will treasure for a lifetime,"
    "Enjoy and build friendships with different kinds of people and"
    "You may also experience your first love and heartbreak."

    # Room BG

    scene room

    "*yawn* …"
    "Today is your first day of senior year."
    "You wonder what would be different in your last year of high school."
    "What feels like the end is often the beginning."
    "*knocks*"

    show mom happy

    mom "Wake up dear, you don’t want to be late on your first day."
    "You got up and went downstairs."


    #Kitchen BG
    scene kitchen

    "Your mom prepared a nice breakfast for you."

    menu:
        "Eat breakfast":
            $ relationship_with_mom += 2
            jump breakfast

        "Skip breakfast":
            show mom sad
            mom "Are you sure you don’t want to take a few bites before you leave?"
            main "Sorry mom, I’m quite late."

            hide mom
            "You saw your mom’s disappointment as you leave the house."
            $ relationship_with_mom -= 2
            scene black
            "Relationship with mom - 2"
            jump school

    return

label end_of_breakfast:
    scene kitchen

    "You finished your breakfast and get your things ready."

    show mom happy
    main "Thank you for the breakfast, see you later mom!"
    mom "See you later sweetheart! Have fun at school."
    "You made your way out and walked to school."
    jump school

    return

label breakfast:
    scene kitchen

    "You sat down with your mom and she appreciates that you spare time to have breakfast with her."

    show mom
    mom "So what are you looking forward to this year?"

    menu:
        "Better grades":
            main "I want to improve my grades this year."
            show mom
            mom "I see… So I guess you’re interested in going to college after high school."
            main "I'll see…"
            scene black
            "Relationship with mom + 2"
            jump end_of_breakfast

        "Try something new":
            jump conversation_mom

    return

label conversation_mom:
    scene kitchen

    show mom
    main "Maybe I will try something new."
    show mom happy
    mom "Oh, that’s interesting, what do you have in mind?"

    menu:
        "Student Council":
            main "I think joining the student council would be interesting."
            show mom
            mom "Oh honey, I don’t recommend being involved in politics."
            scene black
            "Relationship with mom + 2"
            jump end_of_breakfast

        "Sports":
            main "I think I want to try sports."
            show mom happy
            mom "That’s new to me. You never tried physical activities before. I’m looking forward to it."
            scene black
            "Relationship with mom + 2"
            jump end_of_breakfast

        "Make new friends":
            main "Maybe I'll make new friends."
            mom "That’s nice to hear, dear. Maybe try getting a girlfriend too."
            main "Mom!"
            scene black
            "Relationship with mom + 2"
            jump end_of_breakfast

        "No idea":
            main "I have no idea."
            show mom
            mom "You will figure it out, and tell me about it when you do."
            scene black
            "Relationship with mom + 2"
            jump end_of_breakfast

    return

label school:
    # Outside School
    scene out school
    "There are a lot of new faces but there are still a lot of old faces you have seen in the past few years in your high school years."
    "You looked around and realized, you don’t fit in."
    "You are smart but don’t excel much academically."
    "You are inactive in extracurricular activities."
    "You don’t have friends."
    "You are nobody."
    "This year, you wanted that to change."

    scene black
    "Your choices will greatly affect the story.
    You must choose wisely with whom you hang out with, with what you say, and who you become.
    This chapter of your life will have different endings that will depend on the decisions that you make."

    # School Hallway
    scene hallway
    "You were walking on the hallway."
    "Looking around, admiring the school field, noticing jock kids playing and having fun."
    "You took a glipse of the classrooms and you see group of girls talking about their vacation and other girly things."
    "You look forward to the hallway and accidentally locked eyes with this strangely familiar girl."
    "You tried to look away but she started walking faster towards you."
    main "Oh no..."
    kai "Hey you!"
    "You tried to ignore her"

    menu:
        "Turn around":
            "You decided to turn around."
            show kai happy
            kai "You whimp come back!"
            "You started walking faster."
            "The school bell rang and a lot of students came running to their respective classrooms."
            "You were saved by the bell."
            jump classroom

        "Keep walking":
            jump keep_walking

    return

label keep_walking:
    scene hallway
    "You kept walking hoping it's not you."
    "The both of you gets nearer and near and then she stopped in front of you."
    show kai happy
    kai "You're the whimp sand princess!"

    menu:
        "I don't know what you're talking about":
            main "I don't know what you're talking about."
            "She stared at you with a grin on her face."
            scene hallway

        "Ignore her":
            "You decided to ignore her."
            show kai happy
            kai "Yo! Whimp. Remember me?"
            "She held your shoulders as she looks you straight in the eye."
            "You shook your head in confusion."
            scene hallway

    show kai sad
    kai "You honestly forgot about me?"
    show kai happy
    "She shook her head and laughed."
    "The school bell rang and a lot of students came running to their respective classrooms."
    kai "I guess I'll see you around, whimp."
    hide kai
    "She tapped our shoulders aggressively as she walks away."
    "You don't remember who she is."
    jump classroom

    return


label classroom:
    scene classroom m
    "You walked in your classroom and noticed that your homeroom adviser looks pretty young and seems very approachable."
    "You felt a feeling of relief."
    "She seems nice."
    "At least she's not one of the strict terror menopausal teachers you had in your previous school."

    show teacher happy
    teacher "I see… What’s your name?"

    scene black
    $ player_name = ""
    screen black
    call pronounselection from _call_pronounselection
    $ player_name = renpy.input("Don't be shy. Say your name.")
    $ payer_name = player_name.strip()
    scene classroom m
    show teacher happy
    main "My name is [player_name]."

    if not player_name:
        scene classroom m
        show teacher
        teacher "I'll just call you Frank Lee Gaye, okay?"
        $ player_name = "Frank Lee Gaye"
        $ payer_name = player_name.strip()

    scene classroom m
    show teacher happy
    teacher "Alright {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [player_name], there’s only 4 seats left and I am allowing you to choose your seat.
    Choose wisely, this will be your seat for the rest of the school year."
    hide teacher

    call screen seat

    return

#sit with lian
label seat_lian:
    scene classroom m

    "Ms. Sungji turned toward the stoic yet strikingly admirable female student with a look of admiration."
    "You feel like a worm on the ground next to her from the way she presents herself to how perfect her posture is."
    show teacher happy:
        xpos -300
        ypos 80
    show lian happy:
        xpos 550
        ypos 80
    teacher "With Ms. Hui, I see. She is one of the most eligible students here at Tiger’s High. Not to mention her iron fist she has over the student council."
    lian "Much appreciated, ma’am."
    teacher "Ms. Hui, please do take care of your new seat mate this semester. We don’t want another delinquent adding up to the pile. I am entrusting them to you."
    lian "Consider it done, Ms. Sungji."

    hide lian
    hide teacher
    "Ms. Sungji did her opening remarks and started discussing the important things to know on the first day of school."
    "She is very thorough with detail and you feel like getting lost with her words."
    "She caught you not paying full attention so she asked you to stand up."

    show teacher
    teacher "I guess {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [player_name] is on [their!t] little journey in the clouds"
    teacher "Why not tell us about what I just said?"

    menu:
        "Ground rules":
            main "You were talking about the ground rules."
            show teacher happy
            teacher "Correct! I thought you were not listening."
            "Ms. Sungji smiles at you and continues talking."
            "That was close."
            "Lian Hui looks at you and smiled. She must be impressed."
            $ relationship_with_lian += 2
            $ grades += 2
            $ reputation += 2
            scene black
            "Relationship with Lian + 2"
            "Grades + 2"
            "Reputation + 2"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "School Mission and Vision":
            main "You were talking about the mission and vision of the school."
            teacher "Hmmm... nice guess. I was talking about the ground rules. Please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Lian Hui looks at you with a blank expression. She must be disappointed."
            $ relationship_with_lian -= 2
            $ grades -= 1
            scene black
            "Relationship with Lian - 2"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Admit that you were not listening":
            main "I'm sorry ma'am I wasn't paying attention."
            teacher "Just like I thought, please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Lian Hui looks at with disappointment. She must not liked that."
            $ relationship_with_lian -= 1
            $ grades -= 1
            scene black
            "Relationship with Lian - 1"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Uhhh...":
            main "Uhhh..."
            teacher "Hmmm?"
            main "Uhhhh..."
            teacher "Alright please pay attention."
            "Lian Hui looks at with disappointment. She must not liked that."
            $ relationship_with_lian -= 2
            $ grades -= 2
            scene black
            "Relationship with Lian - 2"
            "Grades - 2"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch


    return

#sit with najma
label seat_najma:
    scene classroom m

    "Ms. Sungji turned towards a tall female with a noticeably larger and leaner frame than other female students. She must be an athlete."
    show teacher happy:
        xpos -300
        ypos 80
    show najma:
        xpos 550
        ypos 80
    teacher "Ah, our class athlete, Ms. Awad! She is one of the strongest competitors here in Tiger High.
    If you are interested, Ms. Awad and her team might be looking for a new member in their club. Isn’t that right, Ms. Awad?"
    show najma happy:
        xpos 550
        ypos 60
    najma "Ah! No need for the formality. Just call me Najma. And yes, but we do follow the saying “Survival of the fittest” in our club."
    teacher "Oh? Then I guess you have to put on a little bit of muscle if you really are interested in joining Najma’s team. What do you say, Najma?"
    najma "Haha! As long as they got what it takes to pass the initiation and training then I can train this cub right here if they really are interested."
    teacher "Well, that settles it. Please keep your voices down in class and behave, both of you."

    hide teacher
    hide najma
    "Najma smirked and you nodded softly."

    "Ms. Sungji did her opening remarks and started discussing the important things to know on the first day of school."
    "She is very thorough with detail and you feel like getting lost with her words."
    "She caught you not paying full attention so she asked you to stand up."

    show teacher
    teacher "I guess {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [player_name] is on [their!t] little journey in the clouds"
    teacher "Why not tell us about what I just said?"

    menu:
        "Ground rules":
            main "You were talking about the ground rules."
            show teacher happy
            teacher "Correct! I thought you were not listening."

            "Ms. Sungji smiles at you and continues talking."
            "That was close."
            "Najma tapped your back and smiled at you."
            $ relationship_with_najma += 2
            $ grades += 2
            $ reputation += 2
            scene black
            "Relationship with Najma + 2"
            "Grades + 2"
            "Reputation + 2"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "School Mission and Vision":
            main "You were talking about the mission and vision of the school."
            teacher "Hmmm... nice guess. I was talking about the ground rules. Please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Najma tapped your back and smiled at you."
            $ grades -= 1
            scene black
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Admit that you were not listening":
            main "I'm sorry ma'am I wasn't paying attention."
            teacher "Just like I thought, please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Najma tapped your back and chuckled."
            $ relationship_with_najma += 2
            $ grades -= 1
            scene black
            "Relationship with Najma + 2"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Uhhh...":
            main "Uhhh..."
            teacher "Hmmm?"
            main "Uhhhh..."
            teacher "Alright please pay attention."
            "Najma chuckled and shook her head."
            $ relationship_with_najma += 1
            $ grades -= 1
            scene black
            "Relationship with Najma + 1"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch


    return

#sit with ayani
label seat_ayani:
    scene classroom m

    "Ms. Sungji turned towards the intriguing young lady with unique style and features."
    "You approached your seat slowly as she gazed to you with an intimidating look."
    show teacher:
        xpos -300
        ypos 80
    show ayani angry:
        xpos 550
        ypos 80
    ayani "Ma'am, [they!t] can't sit with me."
    teacher "Why not? You can't just refuse-"
    show ayani angry at Position(xpos=550, ypos=80, xanchor=0, yanchor=0), Shake(None, .3, dist=5)
    ayani "I refuse. I don't like him."
    show teacher happy
    "Ms. Sungji smiled at the both of you with excitement."
    show teacher happy
    teacher "I think you will be good friends at the end of the year. I'm looking forward to it."
    hide teacher
    "Ayani groaned and turned to you."
    show ayani angry
    ayani "Don't talk to me, or look at me, or try to do anything with me, got it?"
    hide ayani
    "She's feisty and you just nervously nodded."

    "Ms. Sungji did her opening remarks and started discussing the important things to know on the first day of school."
    "She is very thorough with detail and you feel like getting lost with her words."
    "She caught you not paying full attention so she asked you to stand up."

    show teacher
    teacher "I guess {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [player_name] is on [their!t] little journey in the clouds"
    teacher "Why not tell us about what I just said?"

    menu:
        "Ground rules":
            main "You were talking about the ground rules."
            show teacher happy
            teacher "Correct! I thought you were not listening."
            "Ms. Sungji smiles at you and continues talking."
            "That was close."
            "Ayani smirked. You don't know if that's a good thing."
            $ relationship_with_ayani += 1
            $ grades += 2
            $ reputation += 2
            scene black
            "Relationship with Ayani + 1"
            "Grades + 2"
            "Reputation + 2"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "School Mission and Vision":
            main "You were talking about the mission and vision of the school."
            teacher "Hmmm... nice guess. I was talking about the ground rules. Please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Ayani chuckled. You don't know if that'a good thing."
            $ relationship_with_ayani += 2
            $ grades -= 1
            scene black
            "Relationship with Ayani + 1"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Admit that you were not listening":
            main "I'm sorry ma'am I wasn't paying attention."
            teacher "Just like I thought, please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Ayani chuckled. You don't know if that'a good thing."
            $ relationship_with_ayani += 1
            $ grades -= 1
            scene black
            "Relationship with Ayani + 1"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Uhhh...":
            main "Uhhh..."
            teacher "Hmmm?"
            main "Uhhhh..."
            teacher "Alright please pay attention."
            "Ayani chuckled. You don't know if that'a good thing."
            $ relationship_with_ayani += 2
            $ grades -= 1
            scene black
            "Relationship with Ayani + 2"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

    return

#sit with chihiro
label seat_chihiro:
    scene classroom m

    "Ms. Sungji turned towards the shy girl sitting at the back of the class. She seems to not interact with anyone and enjoy her company alone."
    show teacher happy:
        xpos -300
        ypos 80
    show chihiro:
        xpos 550
        ypos 80
    teacher "I think Ms. Cihiro would appreciate you sitting next to her in class."
    "Chihiro didn't say anything but she just smiled softly to Ms. Sungji and you."
    "She seems to be very shy and timid."
    show teacher happy
    teacher "I expect the two of you to be my most behave students, but at the end of the year I expect more interactions from the two of you and the class."

    hide chihiro
    hide teacher

    "Ms. Sungji did her opening remarks and started discussing the important things to know on the first day of school."
    "She is very thorough with detail and you feel like getting lost with her words."
    "She caught you not paying full attention so she asked you to stand up."

    show teacher
    teacher "I guess {0}Mr.{/0}{1}Ms.{/1}{2}Mx.{/2} [player_name] is on [their!t] little journey in the clouds"
    teacher "Why not tell us about what I just said?"

    menu:
        "Ground rules":
            main "You were talking about the ground rules."
            show teacher happy
            teacher "Correct! I thought you were not listening."
            "Ms. Sungji smiles at you and continues talking."
            "That was close."
            "Chihiro didn't react at all."
            $ relationship_with_chihiro += 2
            $ grades += 2
            $ reputation += 2
            scene black
            "Relationship with Chihiro + 2"
            "Grades + 2"
            "Reputation + 2"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "School Mission and Vision":
            main "You were talking about the mission and vision of the school."
            teacher "Hmmm... nice guess. I was talking about the ground rules. Please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Chihiro didn't react at all."
            $ relationship_with_chihiro -= 1
            $ grades -= 1
            scene black
            "Relationship with Chihiro - 1"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Admit that you were not listening":
            main "I'm sorry ma'am I wasn't paying attention."
            teacher "Just like I thought, please pay attention."
            "You really need to pay attention in class, it's just the first day and you're already messing it up."
            "Chihiro didn't react at all."
            $ relationship_with_chihiro -= 2
            $ grades -= 1
            scene black
            "Relationship with Ayani - 2"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch

        "Uhhh...":
            main "Uhhh..."
            teacher "Hmmm?"
            main "Uhhhh..."
            teacher "Alright please pay attention."
            "Chihiro giggled softly."
            $ relationship_with_chihiro += 2
            $ grades -= 1
            scene black
            "Relationship with Chihiro + 2"
            "Grades - 1"
            scene classroom m
            "Ms. Sungji continued discussing."
            jump lunch


    return

label lunch:
    scene classroom m with fade

    "Lunch Break..."
    "Everyone is shoving their stuff in their bags as you looked around."

    menu:
        "Eat lunch alone.":
            "You decided to just go alone for now."
            "On your way out, Lian chased you and asked."
            show lian happy
            lian "Hey, do you wanna go eat lunch with us?"
            "Her smile is bright and you just can't refuse."
            main "Oh, sure... Thanks."
            "She giggled and tapped your shoulder."
            lian "No need to thank me. Anyway please wait for me."
            hide lian
            "You waited for her to finish fixing her things and then you both proceed to the cafeteria together."
            jump cafeteria_lian

        "Ask Lian Hui":
            "You nervously appraoched Lian Hui."
            "With your shaky voice you asked,"
            show lian
            main "Hey, Lian Hui, is it okay if I each lunch with you?"
            show lian happy
            lian "Yeah, of course, sure."
            "You waited for her to finish fixing her things and then you both proceed to the cafeteria"
            jump cafeteria_lian

        "Ask Najma Awad":
            show najma
            main "Hey Najma, is it okay if I eat lunch with you?"
            najma "Yeah, yeah."
            hide najma
            "However, she doesn't seem to be paying attention to you."
            "A lot of jock kids are surrounding her and they were quite too loud."
            jump cafeteria_lian

        "Ask Ayani Isa":
            $ reputation -= 2
            show ayani
            main "Hey Ayani-"
            show ayani angry at center, Shake(None, .3, dist=5)
            ayani "Why are you talking to me? Leave me alone."
            hide ayani
            "Ayani walked away from you as she shook her head."
            main "Ah what has gotten into me?"
            "You walked alone to the cafeteria."
            scene black
            "Reputation - 2"
            jump cafeteria_lian

        "Ask Chihiro Issi":
            $ reputation -= 1
            show chihiro
            main "Hey Chihiro, is it okay if I eat lunch with you?"
            hide chihiro
            "Chihiro was startled and she ran away from you."
            scene black
            "Reputation - 2"
            jump cafeteria_lian

    return

label cafeteria_lian:
    stop music
    scene cafeteria
    play music "audio/cafeteria.ogg" loop

    "You grabbed lunch together with Lian and you were able to sit with her and her friends from the Student Council."
    show lian happy
    lian "Hey everyone, this is [player_name]. [theyre!t!c] from my class."
    "Everyone was nice to you and they are all so proper."
    "The formality made you a bit uncomfortable but they seem genuinely nice."
    lian "Have you ever considered joining clubs? Help in the student council perhaps?"
    main "I was never in any clubs. But..."
    $ join_student_council = False
    $ join_sports_club = False

    menu:
        "I still don't have plans in joining one.":
            main "I still don't have plans in joining one. It might not be for me."
            scene black
            $ relationship_with_lian -=2
            "Relationship with Lian - 2"
            jump najma_appearance

        "I might try something new this year.":
            main "I might try something new this year."
            lian "Hmmm what club interests you?"

            menu:
                "The Student Council":
                    $ relationship_with_lian +=2
                    scene black
                    "Relationship with Lian + 2"
                    scene cafeteria
                    show lian
                    main "I think I might consider joining the student council. Do you by chance need new members?"
                    show lian happy
                    lian "That's nice to hear, and yes. I need a new assistant."

                    menu:
                        "Give it a go" if join_student_council == False:
                            main "Then I guess I can be your new assistant."
                            lian "Alrighty then, you'll be my assistant starting from now on. I hope you can handle responsibilities."
                            "Lian Hui seems really impressed."
                            $ relationship_with_lian +=2
                            $ join_student_council = True
                            "You have joined the Student Council"
                            scene black
                            "Relationship with Lian + 2"
                            jump najma_appearance

                        "Pass":
                            main "I'm not sure but is there another open position?"
                            "Lian Hui seemed disappointed."
                            lian "Yeah, I'm sure there are other open positions as of now..."
                            "Lian Hui looked away and joined her friends' conversation."
                            $ relationship_with_lian -=2
                            "Relationship with Lian - 2"
                            jump najma_appearance

                        "I'll think about it.":
                            main "I'll think about it."
                            "Lian gave you a soft smile."
                            lian "Alrighty then. Think about it thoroughly."
                            $ relationship_with_lian -=1
                            scene black
                            "Relationship with Lian - 1"
                            jump najma_appearance


                "The Sports CLub" if join_sports_club == False:
                    main "I think the sports club is quite interesting."
                    lian "You should impress Najma for that. If she thinks you can survive in the club, you'll get in. You must put effort into it, though."
                    $ join_sports_club = True
                    jump najma_appearance

                "The Book Club":
                    main "I might join the book club."
                    show lian happy
                    lian "Hehehe... [player_name] we don't have a book club. You plan starting your own?"
                    "You felt embarrassed because you know nothing about the existing clubs."
                    show lian
                    lian "You might be interested in being my assistant. I can make you read a lot of documents and organize some for me."

                    menu:
                        "Give it a go" if join_student_council == False:
                            main "Then I guess I can be your new assistant."
                            lian "Alrighty then, you'll be my assistant starting from now on. I hope you can handle responsibilities."
                            "Lian Hui seems really impressed."
                            $ relationship_with_lian +=2
                            $ join_student_council = True
                            "You have joined the Student Council"
                            scene black
                            "Relationship with Lian + 2"
                            jump najma_appearance

                        "Pass":
                            main "I'm not sure it's not really my thing."
                            "Lian Hui seemed disappointed."
                            lian "Oh, I see. It's okay. Good luck finding a club that interest you"
                            "Lian Hui looked away embarassed and joined her friends' conversation."
                            $ relationship_with_lian -=2
                            scene black
                            "Relationship with Lian - 2"
                            jump najma_appearance

                        "I'll think about it.":
                            main "I'll think about it."
                            "Lian gave you a soft smile."
                            lian "Alrighty then. Think about it thoroughly."
                            jump najma_appearance

                "I don't know":
                    main "I don't know..."
                    lian "You might be interested in being my assistant. I can make you read a lot of documents and organize some for me."

                    menu:
                        "Give it a go" if join_student_council == False:
                            main "Then I guess I can be your new assistant."
                            lian "Alrighty then, you'll be my assistant starting from now on. I hope you can handle responsibilities."
                            "Lian Hui seems really impressed."
                            $ relationship_with_lian +=2
                            $ join_student_council = True
                            "You have joined the Student Council"
                            scene black
                            "Relationship with Lian + 2"
                            jump najma_appearance

                        "Pass":
                            main "I'm not sure it's not really my thing."
                            "Lian Hui seemed disappointed."
                            lian "Oh, I see. It's okay. Good luck finding a club that interest you"
                            "Lian Hui looked away embarassed and joined her friends' conversation."
                            $ relationship_with_lian -=2
                            scene black
                            "Relationship with Lian - 2"
                            jump najma_appearance

                        "I'll think about it.":
                            main "I'll think about it."
                            "Lian gave you a soft smile."
                            lian "Alrighty then. Think about it thoroughly."
                            $ relationship_with_lian -=1
                            scene black
                            "Relationship with Lian - 1"
                            jump najma_appearance

    return

label najma_appearance:
    scene cafeteria
    play sound "audio/cheer.ogg"
    "The students started cheering and screaming out of excitement."
    "You looked at the cafeteria entry and saw Najma Awad and the rest of the sports club."
    "They're quite a celebrity and everyone seems to like them."
    "Her group goes around and give people high fives."
    show lian happy
    lian "Ah, Najma and her club. They're really famous. They bring pride to the school. I'm so proud of them."
    "She waved at Najma and she did wave back."
    main "You guys are close?"
    lian "Yeah, we're good friends. Najma is really nice too."
    "Najma and the rest of her group started approaching your table and you were a bit nervous."
    show lian happy at left:
        xpos -300
        ypos 1100
    show najma happy:
        xpos 550
        ypos 80
    najma "Hey Lian! What's up my president? You got a new member?"

    if join_student_council == True:
        lian "Ah yes, this is [player_name]. [theyre!t!c] my new assistant so you will see him/her around with me all the time."
        "She giggled as she bumped her shoulders to yours."
        "You give back a shy giggle."

    if join_sports_club == True:
        lian "Actually, [they!t] is interested in your club."
        najma "Really? Hmmmmmm... If you join the sports club you just need a little more training and a lot of muscle. I see potential in you."
        main "Hehe... Thank you."
    "Najma nods and smiled at the both of you."
    najma "Alrighty then, we're going to get some protein. See you guys around."
    hide najma
    "Najma and her group walked towards the table near the water fountain which is seemed to be reserved for them."
    "You feel a bit out of place as Lian and her friends talk about things you have no idea about so now you need
    another place to go."

    menu:
        "Go to outside the cafeteria.":
            jump someone_familiar

        "Go to the restroom.":
            jump sobbing_chihiro

    return

label someone_familiar:
    scene field
    stop music
    play music "audio/hallway.ogg" loop
    "You decided to go outside."
    "As you walk around, you noticed someone very familiar acting very suspicious."

    menu:
        "Follow them":
            "You decided to follow them and it was Ayani."
            "She was talking to other students and passing things secretly."
            "She saw you spying on her."
            "You tried to pretend that you didn't see anything."
            "She started walking towards you."
            show ayani angry
            ayani "Dude what's wrong with you? Why do you keep following me?"

            menu:
                "I wasn't following you":
                    main "I wasn't following you. I was just-"
                    ayani "Then what are you doing here? Spying on me, huh?"
                    main "No I-"
                    ayani "I'm not doing anything illegal in here so don't even dare to report me to or whatever
                    leechy thing you have in mind or I will crush you."
                    hide ayani
                    "Ayani walked away. She looked back at you giving a threatening gaze."
                    $ relationship_with_ayani -= 2
                    scene black
                    "Relationship wtih Ayani - 2"
                    jump sobbing_chihiro

                "What were you doing?":
                    main "What are you doing?"
                    ayani "It's none of your business, you stalker!"

                    menu:
                        "I am not a stalker.":
                            main "Hey, I am not a stalker."
                            show ayani angry at center, Shake(None, .3, dist=5)
                            ayani "Then what are you doing here? Spying on me, huh?"
                            main "No I-"
                            ayani "I'm not doing anything illegal in here so don't even dare to report me to or whatever
                            leechy thing you have in mind or I will crush you."
                            hide ayani
                            "Ayani walked away. She looked back at you giving a threatening gaze."
                            $ relationship_with_ayani -= 2
                            scene black
                            "Relationship wtih Ayani - 2"
                            jump sobbing_chihiro

                        "Is it something illegal?":
                            main "Is it something illegal?"
                            show ayani
                            "Ayani paused for a bit."
                            "She was just staring at you and couldn't open her mouth. It was quite an awkward silence."
                            "She took a deep breath."
                            show ayani sad
                            ayani "Look, this is not illegal. But it's something I may not be proud of."

                            menu:
                                "I wouldn't judge you.":
                                    main "I wouldn't judge you."
                                    show ayani
                                    ayani "See that guy over there? Mr. All Perfect and Smiley?"
                                    main "Yeah... He has always been the top student."
                                    ayani "I do his homework and other school requirements."
                                    main "So you're the real stop student?"
                                    "Ayani turned red and looked away."
                                    ayani "Not really..."
                                    show ayani angry
                                    ayani "You know what? Get lost."
                                    hide ayani
                                    "Ayani walked away."
                                    $ relationship_with_ayani += 2
                                    scene black
                                    "Relationship wtih Ayani + 2"
                                    jump sobbing_chihiro

                                "I'm not interested.":
                                    main "If you don't want to tell me it's fine I'm not interested."
                                    hide ayani
                                    "Ayani was just silent as she gives you a concerning look."
                                    show ayani
                                    ayani "Just stop following me and pretend you saw nothing."
                                    hide ayani
                                    "Ayani walked away and looked back at you with the same concerning look."
                                    $ relationship_with_ayani -= 1
                                    scene black
                                    "Relationship wtih Ayani - 1"
                                    jump sobbing_chihiro

        "Ignore":
            "You decided to just ignore it since it is none of your business."
            "You refuse to get involved with other things."
            jump sobbing_chihiro

    return

label sobbing_chihiro:
    scene restroom
    stop music
    play music "audio/chihiro.ogg" fadein 5 loop

    "You decided to go to the restroom instead."
    "It's relieving that the restroom is clean and smells decent."
    "Suddenly you heard some quiet sobbing."

    menu:
        "Check it out":
            "You decided to check where the sobbing is coming from."
            "You walk towards the last cubicle."

            menu:
                "Knock":
                    "You knocked the door."
                    "*knock knock*"
                    "The sobbing stopped."

                    menu:
                        "Are you okay in there?":
                            main "Are you okay in there?"
                            unknown "Yeah, I'm fine..."
                            "Said a female voice."
                            unknown "Wait... aren't you a guy?"
                            main "Yeah... this is the mens' restroom."
                            unknown "Oh my God!"
                            "She quickly opens the door."
                            show chihiro sad
                            "It was Chihiro. Her eyes were swollen from crying."

                            menu:
                                "Ask her what's wrong.":
                                    main "Hey what's wrong? What happened?"
                                    "Chihiro looked at you shyly. Her eyes are sparkling because of her tears."
                                    hide chihiro
                                    $ relationship_with_chihiro += 1
                                    scene black
                                    "Relationship with Chihiro + 1"
                                    scene restroom
                                    show chihiro
                                    chihiro "I'm really sorry you have to see me like this.
                                    And I'm really sorry for trespassing the men's restroom. I didn't know. I just want to get away..."

                                    menu:
                                        "It's okay. Just don't get lost next time.":
                                            scene restroom
                                            show chihiro
                                            main "It's okay. Just don't get lost next time."
                                            show chihiro
                                            chihiro "Yeah... I'm really sorry I should leave now."
                                            hide chihiro
                                            "Chihiro left the restroom."
                                            $ relationship_with_chihiro += 1
                                            scene black
                                            "Relationship with Chihiro + 1"
                                            scene restroom

                                            menu:
                                                "Okay, see you.":
                                                    scene restroom
                                                    main "Okay, see you."
                                                    "Chihiro nodded softly and left the restroom."
                                                    $ relationship_with_chihiro -= 1
                                                    scene black
                                                    "Relationship with Chihiro - 1"
                                                    jump end_of_lunch

                                                "Wait.":
                                                    scene restroom
                                                    main "Wait."
                                                    "Chihiro looked at you."

                                                    menu:
                                                        "I'm here if you need someone to talk to.":
                                                            show chihiro happy
                                                            main "I'm here if you need someone to talk to."
                                                            "Chihiro smiled and softly nodded."
                                                            "She reached for the door and looked back at you."
                                                            show chihiro happy
                                                            chihiro "Thank you."
                                                            hide chihiro
                                                            "Chihiro left the restroom."
                                                            $ relationship_with_chihiro += 2
                                                            scene black
                                                            "Relationship with Chihiro + 2"
                                                            jump end_of_lunch

                                                        "Nevermind.":
                                                            show chihiro
                                                            main "Nevermind."
                                                            chihiro "Yeah... I'm really sorry I should leave now."
                                                            hide chihiro
                                                            "Chihiro left the room."
                                                            jump end_of_lunch

                                        "What happened?":
                                            scene restroom
                                            show chihiro sad
                                            "Chihiro was too embarassed to respond. She shyly looks at you."
                                            chihiro "My dog died... He meant the world to me, and now he left me."
                                            main "I'm really sorry to hear that, Chihiro. But I am sure he lived a happy fulfilled life."
                                            chihiro "He was my best friend and our friendship was amazing."
                                            main "You must cherish those precious memories you had together. And keep going. Fighting!"
                                            "You tried to cheer her up and it worked."
                                            show chihiro happy
                                            "Chihiro giggled softly and nodded."
                                            "She was smiling brightly and honestly, she looks adorable."
                                            $ relationship_with_chihiro += 2
                                            scene black
                                            "Relationship with Chihiro + 2"
                                            scene restroom

                                            menu:
                                                "I'm here if you need someone to talk to.":
                                                    scene restroom
                                                    show chihiro
                                                    main "I'm here if you need someone to talk to."
                                                    hide chihiro
                                                    "Chihiro smiled and softly nodded."
                                                    show chihiro happy
                                                    chihiro "Alright I have to head to the library now.
                                                    Ms. Sungji asked me to help her out with some things a few minutes before our next class."
                                                    main "Alright, good luck then."
                                                    "You smiled at her and she smiled back."
                                                    "She reached for the door and looked back at you."
                                                    show chihiro
                                                    chihiro "Thank you."
                                                    hide chihiro
                                                    "Chihiro left the restroom."
                                                    $ relationship_with_chihiro += 2
                                                    scene black
                                                    "Relationship with Chihiro + 2"
                                                    scene restroom
                                                    jump end_of_lunch

                                                "Say nothing":
                                                    show chihiro
                                                    chihiro "Alright I have to head to the library now.
                                                    Ms. Sungji asked me to help her out with some things a few minutes before our next class."
                                                    main "Alright, good luck then."
                                                    show chihiro happy
                                                    "You smiled at her and she smiled back."
                                                    hide chihiro
                                                    "Chihiro left the room."
                                                    jump end_of_lunch
                                "Say nothing":
                                    scene restroom
                                    show chihiro
                                    chihiro "I'm really sorry I should leave now."
                                    hide chihiro
                                    "Chihiro left the restroom."
                                    "You went back to the classroom."
                                    jump end_of_lunch

                        "Leave":
                            "You decided to just ignore it since it is none of your business. You refuse to get involved with other things."
                            "You went back to the classroom."
                            jump end_of_lunch

                "Are you okay?":
                    main "Are you okay in there?"
                    unknown "Yeah, I'm fine..."
                    "Said a female voice."
                    unknown "Wait... aren't you a guy?"
                    main "Yeah... this is the mens' restroom."
                    unknown "Oh my God!"
                    "She quickly opens the door."
                    show chihiro sad
                    "It was Chihiro. Her eyes were swollen from crying."

                    menu:
                        "Ask her what's wrong.":
                            main "Hey what's wrong? What happened?"
                            "Chihiro looked at you shyly. Her eyes are sparkling because of her tears."
                            hide chihiro
                            $ relationship_with_chihiro += 1
                            scene black
                            "Relationship with Chihiro + 1"
                            scene restroom
                            show chihiro sad
                            chihiro "I'm really sorry you have to see me like this."
                            chihiro "And I'm really sorry for trespassing the men's restroom."
                            chihiro "I didn't know. I just want to get away..."

                            menu:
                                "It's okay. Just don't get lost next time.":
                                    scene restroom
                                    show chihiro
                                    main "It's okay. Just don't get lost next time."
                                    chihiro "Yeah... I'm really sorry I should leave now."
                                    hide chihiro
                                    "Chihiro left the restroom."
                                    $ relationship_with_chihiro += 1
                                    scene black
                                    "Relationship with Chihiro + 1"
                                    scene restroom

                                    menu:
                                        "Okay, see you.":
                                            scene restroom
                                            main "Okay, see you."
                                            $ relationship_with_chihiro -= 1
                                            scene black
                                            "Relationship with Chihiro - 1"
                                            scene restroom
                                            "Chihiro nodded softly and left the restroom."
                                            jump end_of_lunch

                                        "Wait.":
                                            main "Wait."
                                            "Chihiro looked at you."

                                            menu:
                                                "I'm here if you need someone to talk to.":
                                                    main "I'm here if you need someone to talk to."
                                                    show chihiro happy
                                                    "Chihiro smiled and softly nodded."
                                                    "She reached for the door and looked back at you."
                                                    show chihiro happy
                                                    chihiro "Thank you."
                                                    hide chihiro
                                                    "Chihiro left the restroom."
                                                    $ relationship_with_chihiro += 2
                                                    scene black
                                                    "Relationship with Chihiro + 2"
                                                    jump end_of_lunch

                                                "Nevermind.":
                                                    show chihiro
                                                    chihiro "Yeah... I'm really sorry I should leave now."
                                                    hide chihiro
                                                    "Chihiro left the room."
                                                    $ relationship_with_chihiro -= 2
                                                    scene black
                                                    "Relationship with Chihiro - 2"
                                                    jump end_of_lunch

                                "What happened?":
                                    scene restroom
                                    "Chihiro was too embarassed to respond. She shyly looks at you."
                                    show chihiro sad
                                    chihiro "My dog died... He meant the world to me, and now he left me."
                                    main "I'm really sorry to hear that, Chihiro. But I am sure he lived a happy fulfilled life."
                                    chihiro "He was my best friend and our friendship was amazing."
                                    main "You must cherish those precious memories you had together. And keep going. Fighting!"
                                    show chihiro happy
                                    "You tried to cheer her up and it worked."
                                    "Chihiro giggled softly and nodded."
                                    "She was smiling brightly and honestly, she looks adorable."
                                    $ relationship_with_chihiro += 2
                                    scene black
                                    "Relationship with Chihiro + 2"
                                    scene restroom

                                    menu:
                                        "I'm here if you need someone to talk to.":
                                            scene restroom
                                            show chihiro
                                            main "I'm here if you need someone to talk to."
                                            "Chihiro smiled and softly nodded."
                                            show chihiro happy
                                            chihiro "Alright I have to head to the library now.
                                            Ms. Sungji asked me to help her out with some things a few minutes before our next class."
                                            main "Alright, good luck then."
                                            "You smiled at her and she smiled back."
                                            "She reached for the door and looked back at you."
                                            show chihiro happy
                                            chihiro "Thank you."
                                            hide chihiro
                                            "Chihiro left the restroom."
                                            $ relationship_with_chihiro += 2
                                            scene black
                                            "Relationship with Chihiro + 2"
                                            scene restroom
                                            jump end_of_lunch

                                        "Say nothing":
                                            show chihiro
                                            chihiro "Alright I have to head to the library now.
                                            Ms. Sungji asked me to help her out with some things a few minutes before our next class."
                                            main "Alright, good luck then."
                                            show chihiro happy
                                            "You smiled at her and she smiled back."
                                            hide chihiro
                                            "Chihiro left the room."
                                            jump end_of_lunch
                        "Say nothing":
                            scene restroom
                            show chihiro
                            chihiro "I'm really sorry I should leave now."
                            hide chihiro
                            "Chihiro left the restroom."
                            "You went back to the classroom."
                            jump end_of_lunch

        "Ignore":
            "You decided to just ignore it since it is none of your business. You refuse to get involved with other things."
            "You walked out of the restroom."
            jump end_of_lunch

    return


label end_of_lunch:
    stop music
    play music "audio/late.ogg" fadein 1
    scene classroom a with fade

    "You went back to the classroom and got ready for your next class."
    "All of your classes went well and nothing much important happened."
    "Just a typical high school first day."
    "Since it's the first day, there were no extracurricular activities yet
    for non-members to give time to the club leaders to prepare for tomorrow's recruitment."
    "You decided to go home as soon as possible to avoid that one girl you met earlier in the hallway."
    jump ending_ch01

    return

label ending_ch01:
    scene kitchen

    main "Mom! I'm home."
    show mom happy
    mom "Hey sweetie, welcome home!"
    "You sat down to eat snacks prepared by your mom. It was really nice."
    show mom
    mom "So how was your day?"

    menu:
        "I made friends":
            main "I made some friends..."
            show mom happy
            mom "Oh really? That's nice to hear, tell me about them."
            main "Well there's this girl from my class.."
            "Your mom seems to be so excited for you. She listened to your story with full attention."
            $ relationship_with_mom += 2
            scene black
            "Relationship with mom + 2"
            jump ch_02

        "I joined a club":
            main "I joined a club."
            show mom happy
            mom "Really?!"
            "Your mom was so surprised."
            show mom happy
            mom "So honey, what club is it?"
            main "So there's this girl from my class and she asked me to join her club..."
            hide mom
            "Your mom seems to be so excited for you. She listened to your story with full attention."
            $ relationship_with_mom += 2
            scene black
            "Relationship with mom + 2"
            jump ch_02

        "Boring":
            main "It was boring."
            show mom sad
            "Your mom seems to be disappointed. But she still smiled at you and hugged you."
            show mom sad
            mom "I'm pretty sure something else happened. Wanna tell me about it?"
            "Your mom looked at you with concern."
            show mom happy
            mom "I don't care if it's boring for you. I might find it interesting."
            "You tried to tell your mom what happened but you are just so uninterested to talk about it."
            $ relationship_with_mom -= 2
            scene black
            "Relationship with mom - 2"
            jump ch_02

    return


label ch_02:
    scene black

    show text "{color=#ffffff}{size=+35}END OF CHAPTER 1{/size}{/color}" with dissolve

    $renpy.pause(4.0)

    show text "{color=#ffffff}{size=+35}CHAPTER 2{/size}{/color}" with dissolve

    $renpy.pause(4.0)
    hide text
    stop music
    play music "audio/early.ogg" fadein 1

    "High school is not just about the excitement and the fun part of your life."
    "It is also the time when you build your skills to have better opportunities for your future."
    "Discover your capabilities and your limitations and try and exceed them."
    "This is when you unlock your potential and train yourself for the challenges of tomorrow."
    "You may also experience defeat and discouragement but you must always believe in yourself."

    scene room
    "*yawn*"
    "Today is your second day of senior year."
    "You wonder what would be so exciting and challenging this day has to offer."
    "Are you going to be active in class?"
    "Would you pay attention to your teachers?"
    "You need to set your goals,and your expectations."
    "Who are you going to be?"
    "*knocks*"
    show mom
    mom "Wake up dear, Breakfast is ready."
    "You got up and went downstairs."

    scene kitchen
    "As usual, your mom wakes you up to eat breakfast she prepared just for you. "
    show mom happy
    mom "[player_name], sweetie, food is ready! You dont want to be late for school."
    "As you get downstairs you see that your mom made a couple of choices for breakfast."

    menu:
        "Big Breakfast":
            "You grab a few portion from each of the food prepared. Your mom is delighted and gave you a huge warm smile."
            scene black
            $ relationship_with_mom += 2
            "Relationship with Mom + 2"
            scene kitchen
            show mom

        "Pancakes":
            "You decided to go for the pancakes."
            mom "Are you sure you don't want to try the other food on the table?"
            scene black
            $ relationship_with_mom += 1
            "Relationship with Mom + 1"
            scene kitchen
            show mom

            menu:
                "Try the other options.":
                    "You grab a few portion from each of the food prepared. Your mom is delighted and gave you a huge warm smile."
                    scene black
                    $ relationship_with_mom += 1
                    "Relationship with Mom + 1"
                    scene kitchen
                    show mom

                "Stick with pancakes.":
                    "You decided to just stick with the pancakes. Your mom smiled weakly
                    but she still appreciate that you tried at least on of the food on the table."

        "Cereal":
            "You decided to go for cereal."
            mom "Are you sure you don't want to try the other food on the table?"
            scene black
            $ relationship_with_mom -= 1
            "Relationship with Mom - 1"
            scene kitchen
            show mom

            menu:
                "Try the other options.":
                    "You grab a few portion from each of the food prepared. Your mom is delighted and gave you a huge warm smile."
                    scene black
                    $ relationship_with_mom += 1
                    "Relationship with Mom + 1"
                    scene kitchen
                    show mom

                "Stick with cereal":
                    "You decided to just stick with cereal. Your mom looks a little bit disappointed as you ignore the food she prepared for you.
                    But she still gave you a weak smile as she appreciates that you are eating breakfast with her."

        "Skip breakfast":
            mom "Are you sure you don't want to try the other food on the table?"
            scene black
            $ relationship_with_mom -= 2
            "Relationship with Mom - 2"
            scene kitchen
            show mom

    "You're about to be late so you decided to hurry up. You reached for the door."
    show mom happy
    mom "Good luck with school sweetie!"
    menu:
        "Say something. ":
            main"Thanks mom, see you later."
            scene black
            $ relationship_with_mom += 2
            "Relationship with Mom + 2"
            jump otw_school

        "Ignore her":
            "You decided to not say anything and just leave."
            scene black
            $ relationship_with_mom -= 2
            "Relationship with Mom - 2"
            jump otw_school

    return

label otw_school:
    scene street
    "As you walk your way to school, you saw Chihiro on the opposite side of the street."
    "She is walking slowly with a blank cold expression on her face."

    menu:
        "Approach Chihiro":
            "You decided to approach Chihiro."
            main "Hey! Good morning, Chihiro."
            $ relationship_with_chihiro += 2
            scene black
            "Relationship with Chihiro + 2"
            scene street

            if relationship_with_chihiro >= 5:
                show chihiro happy
                "Chihiro smiled at you and softly responded."
                chihiro "Good morning, [player_name]."

            else:
                "Chihiro softly smiled but didn't say anything."

            "You walked to school together."
            jump front_gate

        "Ignore":
            "You decided to just ignore her."
            "You walked to school alone."
            main "Hey! Good morning, Chihiro."
            $ relationship_with_chihiro -= 2
            scene black
            "Relationship with Chihiro - 2"
            jump front_gate

    return

label front_gate:
    scene out school
    "You reached the school premises. As usual, there are a lot of students and it somehow overwhelms you."
    "You looked around and saw Lian greeting students as they enter the school gate.
    Her smile is as bright as the sun and her presence feels warm."
    "On the other side of the gate, you saw Ayani looking grumpy as always.
    She looks very intimidating but she seems to be nice personally. She seems to be waiting for someone."
    "From the outside, you can see Najma and the rest of the sports club having their morning jog.
    They look so lively and full of energy this early and they seem to be so inspiring."

    menu:
        "Approach Lian.":
            "You walked towards Lian and she greeted you with a big smile."
            show lian happy
            lian "Good morning, [player_name]! Have a nice day ahead of you. See you in class."
            scene black
            $ relationship_with_lian += 2
            "Relationship with Lian + 2"
            scene out school
            show lian happy

            menu:
                "Ask her if she wants to go to class together.":
                    main "Hey Lian, do you want to go to class together?"

                    if relationship_with_lian >= 5:
                        lian "Sure but I have to stay here in a bit to greet the other students."

                        menu:
                            "Wait for her.":
                                main "It's okay, I will wait for you. I might actually greet everyone with you too."
                                "She appreciates that and you exchange smiles."
                                hide lian
                                "After greeting the students, you walked to class together."
                                scene black
                                $ relationship_with_lian += 2
                                "Relationship with Lian + 2"
                                jump classroom_02

                            "Go to class alone.":
                                main "Oh, okay. See you in class then."
                                lian "Okay, see you!"
                                hide lian
                                "She just smiled softly and continue greeting other students."
                                "You entered the school gate and went to class alone."
                                jump classroom_02


                    else:
                        show lian
                        lian "Oh, I have to stay here in a bit to greet the other students. You can go to class first."
                        hide lian
                        "You entered the school gate and went to class alone."
                        jump classroom_02

                "Go to class alone.":
                    hide lian
                    "You nodded as you enter the school gate and went to class alone."
                    scene black
                    $ relationship_with_lian -= 1
                    "Relationship with Lian - 1"
                    jump classroom_02

        "Approach Ayani.":
            "You walked towards Ayani."
            scene black
            $ relationship_with_ayani += 1
            "Relationship with Ayani + 1"
            scene out school

            if relationship_with_ayani >= 4:
                show ayani happy
                "She nodded her head as she acknowledge your existence."
                scene black
                $ relationship_with_ayani += 1
                "Relationship with Ayani + 1"
                scene out school

            else:
                "She ignores you and doesn't even bother looking at you. It seems like she dislikes you."

            "After a while, the creepy girl in the hallway came and approached the two of you."
            "She burst out laughing."
            show ayani happy at left:
                xpos -300
                ypos 1100
            show kai happy:
                xpos 550
                ypos 80
            kai "Wow Ayani, you replaced me with this loser? What are you guys doing together?"

            if relationship_with_ayani >= 4:
                show ayani at left:
                    xpos -300
                    ypos 1100
                show kai happy:
                    xpos 550
                    ypos 80
                ayani "Leave him alone Kai, we're good."
                $ some_character = "Kai"
                "You smiled at Ayani wordlessly saying thank you."
                kai "Really?"
                "Kai still can't stop giggling and teasing you."
                ayani "Let's go to class. I don't want to be late it's awkward walking in."
                "You followed them to class. It  was a bit weird since Kai is looking at you weirdly."
                jump classroom_02

            else:
                "Ayani isn't bothered and ignored you both."
                "The creepy girl still can't stop giggling and teasing you."
                ayani "Let's go to class. I don't want to be late it's awkward walking in."
                "You followed them to class. It  was a bit weird since Kai is looking at you weirdly."
                jump classroom_02

        "Ignore them.":
            "You decided to ignore both of them and go on your own. But all of a sudden, Kai approached you."
            show kai happy
            kai "Mornin' loser. Are you still gonna ignore me?"
            "You decided to ignore her."
            show kai shocked
            kai "C'mon man it seems like we weren't besties when we were little. Seriously forgot about me?"
            "You paused for a bit and tried to remember."
            "Then you realize it's Kai. Your childhood bestfriend. She looks a lot different now."
            $ some_character = "Kai"
            main "Kai? You look a lot different now. You're ..."
            "You looked at ther from head to toe."
            main "... a lot taller."
            show kai sad
            kai "Really? That's all you can say after leaving me for years?"
            "Kai walked away as she shook her head. You saw her approaching Ayani and they walked to class together."
            jump classroom_02

    return

label classroom_02:
    scene classroom m
    show teacher

    teacher "Good morning class! It's our second day but I believe that we have to start our lessons for this semester."
    teacher "Let's kickstart this semester with a little quiz, shall we?"
    teacher "Here we go."
    jump ch2question_1


    return

label ch2question_1:
    stop music
    play music "audio/quiz.ogg"
    show screen quiz_score
    teacher "Which core ingredient is important to cook a savory dish?"
    menu:
        "Salt":
            $ score += 1
            jump ch2question_2
        "Butter":
            jump ch2question_2
        "Egg":
            jump ch2question_2
    return

label ch2question_2:
    teacher "Brazil is the biggest producer of?"
    menu:
        "Coffee":
            $ score += 1
            jump ch2question_3
        "Oil":
            jump ch2question_3
        "Rice":
            jump ch2question_3
    return

label ch2question_3:
    teacher "Saudi Arabia is the biggest producer of?"
    menu:
        "Oil":
            $ score += 1
            jump ch2question_4
        "Coffee":
            jump ch2question_4
        "Salt":
            jump ch2question_4
    return

label ch2question_4:
    teacher "What is the currency of the UK?"
    menu:
        "Pound":
            $ score += 1
            jump ch2question_5
        "Euro":
            jump ch2question_5
        "Dollar":
            jump ch2question_5
    return

label ch2question_5:
    teacher "What is a tomato?"
    menu:
        "Fruit":
            $ score += 1
            jump ch2question_6
        "Vegetable":
            jump ch2question_6
        "Herb":
            jump ch2question_6
    return

label ch2question_6:
    teacher "What is a great remedy for weight loss?"
    menu:
        "Green Tea":
            $ score += 1
            jump ch2question_7
        "Nestea":
            jump ch2question_7
        "Gatorade":
            jump ch2question_7
    return

label ch2question_7:
    teacher "What pulls the sea water with its gravitational force?"
    menu:
        "Moon":
            $ score += 1
            jump ch2question_8
        "Sun":
            jump ch2question_8
        "Jupiter":
            jump ch2question_8
    return

label ch2question_8:
    teacher "Which is the second planet from the earth?"
    menu:
        "Mars":
            $ score += 1
            jump ch2question_9
        "Uranus":
            jump ch2question_9
        "Mercury":
            jump ch2question_9
    return

label ch2question_9:
    teacher "Evaluate the expression 5(3X + Y) / 10. Use X = 3, Y = 11"
    menu:
        "10":
            $ score += 1
            jump ch2question_10
        "11":
            jump ch2question_10
        "12":
            jump ch2question_10
    return

label ch2question_10:
    teacher "When did the most latest pandemic occured?"
    menu:
        "2020":
            $ score += 1
            jump end_quizch2
        "2012":
            jump end_quizch2
        "2023":
            jump end_quizch2
    return

label end_quizch2:
    hide screen quiz_score
    if score <= 5:
        show teacher
        teacher "You only got [score] points. That was unfortunate of you. Better luck next time, [player_name]."
    else:
        show teacher happy
        teacher "Congratualtions, [player_name]! You got [score] points! You did very well!"

    #route choosing blah blah base sa stats

    if score == 10:
        $ relationship_with_lian += 5
        scene black
        "Relationship with Lian + 5"
    elif score >= 8 and score < 10:
        $ relationship_with_ayani += 5
        scene black
        "Relationship with Ayani + 5"
    elif score >= 5 and score < 8:
        $ relationship_with_najma += 5
        scene black
        "Relationship with Najma + 5"
    elif score < 5 and score != 0:
        $ relationship_with_chihiro += 5
        scene black
        "Relationship with Chihiro + 5"

    $ lian_v_ayani = False
    $ najma_v_chihiro = False

    if relationship_with_lian >= 7 or relationship_with_ayani >= 6 and lian_v_ayani == False:
        $ lian_v_ayani = True
        jump lian_v_ayani
    elif relationship_with_najma >= 7 or relationship_with_chihiro >= 5 and najma_v_chihiro == False:
        $ najma_v_chihiro = True
        jump najma_v_chihiro
    elif relationship_with_mom >= 4:
        jump neutral_ending_scene
    else:
        jump bad_ending_scene
    return

#Lian vs Ayani
label lian_v_ayani:
    stop music
    play music "audio/hallway.ogg"
    scene hallway
    "There's more time to participate in extracurricular activities."

    menu:
        "Find Lian and ask her about the student council.":
            "You decided to look for Lian and ask her about the student council."
            "You walked to the second floor and saw Lian and the student council vice president, Hana Chien."
            "They were talking about a charity program but they seem to be not agreeing with the concept."
            "You knocked on the door and they both looked at you."
            show lian happy at left:
                xpos -300
                ypos 1100
            show hana angry:
                xpos 550
                ypos 80
            lian "Hey [player_name]! Come in."
            hide lian
            hide hana
            "You walked in the room and Hana gave you a darkened gaze."
            "She seems scary, like Ayani."
            "Well, you realized she looks a lot like Ayani."
            "Are they related?"
            scene clubroom

            if join_student_council == True:
                show lian happy at left:
                    xpos -300
                    ypos 1100
                show hana:
                    xpos 550
                    ypos 80
                lian "Hana, this is [player_name], the new student. [player_name], this is Hana, the student council's vice president.s [player_name], my new assistant and our new member.
                [player_name], this is Hana, the student council's vice president."
                show hana happy:
                    xpos 550
                    ypos 80
                "Hana nodded and smiled weakly at you, you can't tell if she likes you now or not."
                $ relationship_with_lian += 2
                $ reputation += 2
                scene black
                hide lian
                "Relationship with Lian + 2"
                "Reputation + 2"
                jump ending_ch02

            else:
                show lian happy at left:
                    xpos -300
                    ypos 1100
                show hana:
                    xpos 550
                    ypos 80
                lian "Hana, this is [player_name], the new student.
                [player_name], this is Hana, the student council's vice president."
                "Hana just nodded but it still seems like she doesn't like you."
                lian "So, have you changed your mind? Do you wanna join the student council now?"
                lian "I mean the spots I offered are still available and so far I don't have anyone in mind that would fit the job."

                menu:
                    "Join the Student Council" if join_student_council == False:
                        $ join_student_council = True
                        $ relationship_with_lian += 2
                        $ reputation += 2
                        main "Yeah I've been thinking of joining and I guess I'm here to tell you I'm in."
                        lian "Perfect! Welcome to the Student Council, [player_name]."
                        "It feels nice to see her that happy."
                        "Hana seems to be a bit shy and not really into showing her emotions."
                        "But she seems happy and smile too as she sees Lian happy too."
                        hide lian
                        hide hana
                        scene black
                        "The first day of you being a member of the student council was very productive."
                        "It was tiring but it was surprisingly fun. You enjoyed and learned a lot as well."
                        "You look forward to the how your decision in joining the student council will change you and shape you as a better person."
                        "Relationship with Lian + 2"
                        "Reputation + 2"
                        jump ending_ch02

                    "Reject the offer":
                        $ relationship_with_lian -= 2
                        main "Yeah, about that..."
                        "You paused for a bit."
                        "You noticed that Lian seems to be so excited."
                        "Are you sure you want to reject the offer?"

                        menu:
                            "Yes.":
                                $ relationship_with_lian -= 2
                                main "I'm sorry Lian but I don't think the student council is for me."
                                show lian sad at left:
                                    xpos -300
                                    ypos 1100
                                show hana angry:
                                    xpos 550
                                    ypos 80
                                "The smile on Lian's face faded. She seems to be so disappointed with what you said."
                                "Hana shook her head and looked away."
                                hide lian
                                lian "Oh, I see. It's okay... That's okay."
                                show lian at left:
                                    xpos -300
                                    ypos 1100
                                "Lian smiled softly."
                                "It's a bit awkward."
                                "You decided to just walk out of the room."
                                main "I guess I will just see you guys around."
                                "They both just nodded as you leave the room."
                                hide lian
                                scene black
                                "Relationship with Lian - 4"
                                jump ending_ch02

                            "No." if join_student_council == False:
                                $ join_student_council = True
                                $ relationship_with_lian += 1
                                main "But I can reconsider..."
                                "That sparked hope on Lian's eyes."
                                lian "Perfect! Welcome to the Student Council, [player_name]."
                                "Lian seems to be so delighted with your decision and you can see how big her smile is."
                                "It feels nice to see her that happy."
                                "Hana seems to be a bit shy and not really into showing her emotions."
                                "But she seems happy and smile too as she sees Lian happy too."
                                hide lian
                                hide hana
                                scene black
                                "The first day of you being a member of the student council was very productive."
                                "It was tiring but it was surprisingly fun. You enjoyed and learned a lot as well."
                                "You look forward to the how your decision in joining the student council will change you and shape you as a better person."
                                "Relationship with Lian + 1"
                                jump ending_ch02

        "Go home.":
            stop music
            play music "audio/late.ogg"
            scene street
            "You just decided to go home instead."
            "You thought maybe clubs and extracurricular activities are not for you."
            "On your way home you saw Ayani in a rush."
            "You asked yourself,"
            main "Why is she always doing suspicious stuff?"

            menu:
                "Approach her.":
                    "You decided to follow her."
                    "She walks fast and its hard following her without being caught."
                    "She started walking in narrow streets and you start to feel uncomfortable about it."

                    menu:
                        "Keep on following her.":
                            $ relationship_with_ayani -= 1
                            $ reputation -= 2
                            "The streets gets even more narrow but you're still dying to know where she would go."
                            "Then, you lost her."
                            "You're lost."
                            "You don't know your way back."
                            "As you turn around, she was there looking so furious at you."
                            show ayani
                            main "Ahhh! Ayani!"
                            show ayani angry at center, Shake(None, .3, dist=5)
                            ayani "WHY THE HELL ARE YOU FOLLOWING ME?"
                            main "It's not like tha-"
                            "Before you can finish talking, she slapped you."
                            ayani "Leave me alone, creep."
                            hide ayani
                            "Ayani walked away."
                            "That was quite embarrassing."
                            "You decided to walk home."
                            scene black
                            "Relationship with Ayani - 1"
                            "Reputation - 2"
                            jump ending_ch02

                        "Go home.":
                            "You lost Ayani and decided to just go home instead."
                            "Luckily, you found yourself back to the main street and you walked back home."
                            jump ending_ch02

                "Ignore her.":
                    "You just decided to ignore her."
                    "She has her own personal life and it's not really your business."
                    "You just decided to walk home."
                    jump ending_ch02

    return

#Najma vs Chihiro
label najma_v_chihiro:
    stop music
    play music "audio/hallway.ogg"
    scene hallway
    "There's more time to participate in extracurricular activities."

    menu:
        "Find Najma and ask her about the sports club.":
            "You decided to look for Najma and ask her about the sports club."
            "You walked to the school gym and saw Najma and a few other student atheletes."
            "They were talking about the sports fest and other sports related program but they seem to be worried about something."
            "You slowly walked in the gym and sat on the bleachers."
            "Some students noticed you and can't help but to look at you."
            "Najma turned around and from a worried expression, her face sparked hope."
            show najma happy
            najma "Thank the god of Sports! Hey,[player_name], come here."
            "The other student atheletes started murmuring but they seem to be excited."
            "You walked towards them and Najma threw her arm on your shoulder."

            if join_sports_club == True:
                $ relationship_with_najma += 2
                $ reputation += 2
                najma "Everyone, this is [player_name], the heavens answered our prayers and granted us a new member."
                "Everyone started cheering. It was a bit overwhelming."
                najma "Although, you need a little bit more protein and muscle. But don't worry we're all here to help you and encourage you."
                hide najma
                scene black
                "The first day of you being a member of the sports council was very exhausting."
                "It was tiring but it was surprisingly fun. You enjoyed and learned a lot as well."
                "You look forward to how your decision in joining the sports club will change you and shape you as a better person."
                "Relationship with Najma + 2"
                "Reputation + 2"
                jump ending_ch02

            else:
                najma "So [player_name], what brought you here? Wanna join the sports club?"
                najma "I mean we are in need of one more member to be able to successfully plan the sports fest. And we don't require premade athletes.
                In here we believe that everyone is welcome and we aim to change people to the best version of themselves."

                menu:
                    "Join the Sports Club" if join_sports_club == False:
                        $ join_sports_club = True
                        $ relationship_with_najma += 2
                        $ reputation += 2
                        main "Yeah I've been thinking of joining and I guess I'm here to tell you I'm in."
                        najma "Poggers! Welcome to the Sports Club, [player_name]."
                        "Najma seems to be so delighted with your decision and you can see how big her smile is."
                        "It feels nice to see her that happy."
                        najma "Everyone, this is [player_name], the heavens answered our prayers and granted us a new member."
                        "Everyone started cheering. It was a bit overwhelming."
                        najma "Although, you need a little bit more protein and muscle. But don't worry we're all here to help you and encourage you."
                        hide najma
                        scene black
                        "The first day of you being a member of the sports council was very exhausting."
                        "It was tiring but it was surprisingly fun. You enjoyed and learned a lot as well."
                        "You look forward to how your decision in joining the sports club will change you and shape you as a better person."
                        "Relationship with Najma + 2"
                        "Reputation + 2"
                        jump ending_ch02

                    "Reject the offer":
                        $ relationship_with_najma -=2
                        main "Yeah, about that..."
                        "You paused for a bit."
                        "You noticed that Najma seems to be so excited."
                        "Are you sure you want to reject the offer?"
                        menu:
                            "Yes.":
                                $ relationship_with_najma -= 2
                                main "I'm sorry Najma but I don't think the sports club is for me."
                                show najma sad
                                "The smile on Najma's face faded. She seems to be so disappointed with what you said."
                                "The other student athletes shook also look devastated."
                                najma "Oh, I see. It's okay... That's okay."
                                "Najma frowned but she still tried to smile at you softly."
                                "It's a bit awkward."
                                main "Aight, I guess I'm gonna go now."
                                hide najma
                                "You decided to just walk out of the gym."
                                main "I guess I will just see you guys around."
                                "Everyone just nodded as you leave the place."
                                scene black
                                "Relationship with Najma - 4"
                                jump ending_ch02

                            "No." if join_sports_club == False:
                                $ join_sports_club = True
                                $ relationship_with_najma += 1
                                main "But I can reconsider..."
                                "That sparked hope on Najma's eyes."
                                main "I guess I can try?"
                                najma "Perfect! Welcome to the Sports Club, [player_name]."
                                "Najma seems to be so delighted with your decision and you can see how big her smile is."
                                "It feels nice to see her that happy."
                                "Everyone started cheering. It was a bit overwhelming."
                                najma "Although, you need a little bit more protein and muscle. But don't worry we're all here to help you and encourage you."
                                hide najma
                                scene black
                                "The first day of you being a member of the sports club was very exhausting."
                                "It was tiring but it was surprisingly fun. You enjoyed and learned a lot as well."
                                "You look forward to how your decision in joining the sports club will change
                                you and shape you as a better person."
                                "Relationship with Najma + 1"
                                jump ending_ch02

        "Go home.":
            stop music
            play music "audio/late.ogg"
            scene street
            "You just decided to go home instead."
            "You thought maybe clubs and extracurricular activities are not for you."
            "On your way home you saw Chihiro walking alone."
            "You are thinking whether to approach her or not."

            menu:
                "Approach her.":
                    "You decided to approach her."
                    "You walk towards her way and she looks at you slowly."
                    show chihiro
                    chihiro "Hey [player_name]."
                    "She said softly."

                    menu:
                        "Are you walking home alone?":
                            $ relationship_with_chihiro -= 1
                            main "Are you walking home alone?"
                            "Chihiro paused for a bit."
                            chihiro "Oh, actually I'm waiting for someone. I totally forgot. Thanks for remind me."
                            hide chihiro
                            "Chihiro turned around and went back to the school gate."
                            "Before she gets too far she turned back."
                            show chihiro
                            chihiro "Stay safe on your way home, [player_name]."
                            hide chihiro
                            "You just nodded and walked home."
                            scene black
                            "Relationship with Chihiro - 1"
                            jump ending_ch02

                        "Wanna walk home together?":
                            $ relationship_with_chihiro += 2
                            main "Wanna walk home together?"
                            show chihiro happy
                            "Chihiro blushed and slowly looked at you."
                            "Chihiro started stuttering, and this is expected of her since she is very shy and awkward to talk to."
                            chihiro "Yeah... sure we can walk... together."
                            "You gave her a smile and you started walking."
                            "Chihiro looks adorable when she's flusttered."
                            "You kind of get hints she has a crush on you, but maybe she's just too shy and gets startled by everything."
                            "A total softie."
                            scene black
                            "Relationship with Chihiro + 2"
                            jump ending_ch02

                "Ignore her.":
                    "You just decided to ignore her."
                    "She has her own personal life and it's not really your business."
                    "You just decided to walk home."
                    jump ending_ch02

    return

label ending_ch02:
    stop music
    play music "audio/late.ogg"
    scene kitchen

    "You finally got home after a long day at school."
    main "Hey, mom! I'm home."
    show mom happy
    mom "[player_name], sweetie, welcome home! How was your day?"

    menu:
        "I made friends":
            main "I made some friends..."
            show mom happy
            mom "Oh really? That's nice to hear, tell me about them."
            main "Well there's this girl from my class.."
            "Your mom seems to be so excited for you. She listened to your story with full attention."
            $ relationship_with_mom += 2
            scene black
            "Relationship with mom + 2"
            jump ch_03

        "I joined a club":
            main "I joined a club."
            show mom happy
            mom "Really?!"
            "Your mom was so surprised."
            show mom happy
            mom "So honey, what club is it?"
            main "So there's this girl from my class and she asked me to join her club..."
            hide mom
            "Your mom seems to be so excited for you. She listened to your story with full attention."
            $ relationship_with_mom += 2
            scene black
            "Relationship with mom + 2"
            jump ch_03

        "Boring":
            main "It was boring."
            show mom sad
            "Your mom seems to be disappointed. But she still smiled at you and hugged you."
            show mom sad
            mom "I'm pretty sure something else happened. Wanna tell me about it?"
            "Your mom looked at you with concern."
            show mom happy
            mom "I don't care if it's boring for you. I might find it interesting."
            "You tried to tell your mom what happened but you are just so uninterested to talk about it."
            $ relationship_with_mom -= 1
            scene black
            "Relationship with mom - 1"
            jump ch_03

    return

label ch_03:
    scene black

    show text "{color=#ffffff}{size=+35}END OF CHAPTER 2{/size}{/color}" with dissolve

    $renpy.pause(4.0)

    show text "{color=#ffffff}{size=+35}CHAPTER 3{/size}{/color}" with dissolve

    $renpy.pause(4.0)
    hide text

    "They say the only way to have a friend is to be one."
    "Little did we know that as we build friendship,"
    "we also build a part of ourselves."
    "Friendship is another word for love."
    "And how wonderful it is to love,"
    "and to be loved."

    stop music
    play music "audio/early.ogg"
    scene room

    "*yawn* …"
    "A lot of days have passed since the first day of class."
    "You have chosen paths and made decisions that shapes the life you have today."
    "You wonder what else could happen this year."
    "Would there be any chance that you would get to know your friends better?"
    "Or get to know yourself deeper?"
    "Everything would depend on what you will focus on"
    "and things will base on your priorities."

    scene black
    "Something feels odd..."

    scene kitchen
    "Mom isn't here today..."
    "You saw a note on the fridge and it states:"
    "Note: Hey sweetie, I will be gone for a day or two,
    I'm sorry I haven't prepared breakfast and forgot to tell you last night since you
    were very busy and I didn't want to bother you. There are other food available in the fridge. I will try to be home tomorrow morning.
    I love you! -Love, Mom"
    "Seems like you need to prepare your own breakfast."

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    init: ### just setting variables in advance so there are no undefined variable problems
        $ timer_range = 0
        $ timer_jump = 0
        $ time = 0

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
            ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
            # ^This is the timer bar.

    label questiontime1:
        scene kitchen
        show countdown
        label menu1:
            $ time = 12                                     ### set variable time to 3
            $ timer_range = 12                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
            show screen countdown                          ### call and start the timer
            show Fridge at center

            menu:
                "Pick the Sandwich.":
                    hide screen countdown                  ### stop the timer
                    "You picked the sandwich."
                    main "Mom will be delighted if I eat what she made." #change ayani to main
                    $ relationship_with_mom += 2
                    scene black
                    "Relationship with mom + 2"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

                "Pick the Ice Cream.":
                    hide screen countdown                  ### stop the timer
                    "You picked the ice cream."
                    main "Hehehe...This will kickstart my sugar-rush."
                    $ relationship_with_mom -= 1
                    scene black
                    "Relationship with mom - 1"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

                "Pick the Cake.":
                    hide screen countdown                  ### stop the timer
                    "You picked the cake."
                    main "Atleast I ate something."
                    $ relationship_with_mom += 1
                    scene black
                    "Relationship with mom + 1"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

                "Pick the Cookie.":
                    "You picked the cookie."
                    hide screen countdown                  ### stop the timer
                    main "Atleast I ate something."
                    $ relationship_with_mom += 1
                    scene black
                    "Relationship with mom + 1"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

                "Pick the Soju.":
                    "You picked the Soju."
                    hide screen countdown                  ### stop the timer
                    main "Hmmmm Let's do a little experimenting before school."
                    $ relationship_with_mom -= 5
                    scene black
                    "Relationship with mom - 5"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

                "Pick the Bento.":
                    "You picked the Bento."
                    hide screen countdown                  ### stop the timer
                    main "Sheeesh, I thought Mom forgot. She really loves me :>"
                    $ relationship_with_mom += 1
                    scene black
                    "Relationship with mom + 6"
                    if lian_v_ayani == True:
                        jump lian_v_ayani_ch03

                    elif najma_v_chihiro == True:
                        jump najma_v_chihiro_ch03

        label menu1_slow:
            $ relationship_with_mom -= 3
            scene black
            "You can't decide what kind of food you want to eat."
            "You didn't notice the time"
            main "Oh no I will be late for School"
            "Relationship with mom - 3"

    return

label lian_v_ayani_ch03:
    scene street

    "As you get close to your school, you notice Ayani walking out of a convinience store."
    "She is putting down her hair from a ponytail and fixing her school uniform."

    menu:
        "Approach Ayani.":
            "You decided to approach Ayani."
            main "Hey Ayani! Goo-"
            "Before you can greet her, she gave you a big frown and started walking away fast."

            menu:
                "Follow her.":
                    show ayani angry
                    "You still decided to follow her."
                    show ayani angry at center, Shake(None, .3, dist=5)
                    ayani "What is wrong with you?"

                    menu:
                        "Just trying be friendly.":
                            if relationship_with_ayani >= 5:
                                $ relationship_with_ayani += 1
                                main "Just trying to be friendly."
                                ayani "I think you're getting too friendly."
                                ayani "What do you want?"
                                main "Nothing I just saw you and maybe I should approach you."
                                show ayani happy
                                "Ayani smiled softly."
                                main "Wanna walk to school together?"
                                ayani "Aren't we doing that already?"
                                hide ayani
                                scene black
                                "Relationship with Ayani + 1"
                                jump outschool_lian_ch03

                            else:
                                $ relationship_with_ayani -= 1
                                main "Just trying to be friendly."
                                ayani "I think you're getting too friendly."
                                ayani "Leave me alone weirdo."
                                "Ayani looked at you with a disgusted look."
                                hide ayani
                                "She walked faster and left you alone."
                                "You walked to school alone."
                                jump outschool_lian_ch03

                        "Well, I just want to greet my friend.":
                            $ relationship_with_ayani += 1
                            if relationship_with_ayani >= 5:
                                $ relationship_with_ayani += 2
                                main "Well, I just want to greet my friend."
                                ayani "Hmmm... who told you we're friends?"
                                show ayani happy
                                "Ayani giggled."
                                ayani "Sorry that sounded harsh, we're acquaintances I guess."
                                ayani "So what do you want?"
                                main "Nothing I just saw you and maybe I should approach you."
                                "Ayani smiled softly."
                                main "Wanna walk to school together?"
                                ayani "Aren't we doing that already?"
                                hide ayani
                                scene black
                                "Relationship with Ayani + 2"
                                jump outschool_lian_ch03

                            else:
                                $ relationship_with_ayani -= 1
                                main "Well, I just want to greet my friend."
                                ayani "We're not friends. Never."
                                ayani "Leave me alone weirdo."
                                "Ayani looked at you with a disgusted look."
                                "She walked faster and left you alone."
                                "You walked to school alone."
                                scene black
                                "Relationship with Ayani - 1"
                                jump outschool_lian_ch03

                "Let her be.":
                    "She walked faster and left you alone."
                    "You walked to school alone."
                    jump outschool_lian_ch03

        "Ignore her.":
            "You decided to just ignore her. Bothering her isnt much worth your time."
            jump outschool_lian_ch03

    return

label outschool_lian_ch03:
    scene out school

    "You finally reached the school gate."
    "You walked along the other students but on your way in the guard stopped you."
    show guard
    guard "School ID?"
    "You looked down on your chest and realized you don't have your ID on."
    "You started panicking and kept searching your bag."
    "You can't go back home to fetch your ID."
    "And then suddenly..."
    show guard at left:
        xpos -300
        ypos 1100
    show lian:
        xpos 550
        ypos 80
    lian "Good morning Mrs. Dimaapi, this is [player_name], [they!t] is a new student. [they!t!c] still don't have an ID issued."
    "She paused."
    lian "As the president of the student council, I can assure you that [they!t] will get his/her ID tomorrow."
    "Mrs. Dimaapi couldn't do anything but to let you in the school premises."
    "Lian held your arm and you walked to class together."
    jump classroom_lian_ch03

    return

label classroom_lian_ch03:
    scene classroom m

    "You finally reached your classroom."
    show lian
    main "Thank you, Lian."
    show lian happy
    "Lian smiled at you."
    lian "Anytime, [player_name]."
    hide lian
    "You went to your seat and so does Lian."
    show teacher
    teacher "Good morning class! It's our second day but I believe that we have to start our lessons for this quarter."
    teacher "Let's kickstart this quarter with a little quiz, shall we?"
    teacher "Here we go."
    jump alch3question_1

    return

label alch3question_1:
    $ score = Non
    stop music
    play music "audio/quiz.ogg"
    show screen quiz_score
    teacher "Which core ingredient is important when preparing sushi?"
    menu:
        "Rice":
            $ score += 1
            jump alch3question_2
        "Salt":
            jump alch3question_2
        "Wasabi":
            jump alch3question_2
    return

label alch3question_2:
    teacher "He invented/patented the light bulb."
    menu:
        "Nikola Tesla":
            jump alch3question_3
        "Joe Biden":
            jump alch3question_3
        "Thomas Edison":
            $ score += 1
            jump alch3question_3
    return

label alch3question_3:
    teacher "Also known a H20"
    menu:
        "Koy":
            jump alch3question_4
        "Water":
            $ score += 1
            jump alch3question_4
        "Magma":
            jump alch3question_4
    return

label alch3question_4:
    teacher "What is the currency of the Philippines?"
    menu:
        "Pound":
            jump alch3question_5
        "Peso":
            $ score += 1
            jump alch3question_5
        "Dollar":
            jump alch3question_5
    return

label alch3question_5:
    teacher "Bacon is made from pork-"
    menu:
        "Belly":
            $ score += 1
            jump alch3question_6
        "Shoulder":
            jump alch3question_6
        "Leg":
            jump alch3question_6
    return

label alch3question_6:
    teacher "The essence of what to be or a being in a state of being?"
    menu:
        "Existence":
            $ score += 1
            jump alch3question_7
        "Ecstacy":
            jump alch3question_7
        "Elaborate":
            jump alch3question_7
    return

label alch3question_7:
    teacher "The largest Desert in the world?"
    menu:
        "Sahara":
            jump alch3question_8
        "Antarctica":
            $ score += 1
            jump alch3question_8
        "Saudi Arabia":
            jump alch3question_8
    return

label alch3question_8:
    teacher "What programming language is based on an animal?"
    menu:
        "Pyhton":
            $ score += 1
            jump alch3question_9
        "Snake":
            jump alch3question_9
        "Cobra":
            jump alch3question_9
    return

label alch3question_9:
    teacher "This part of the body is also considered as our crown. "
    menu:
        "Hair":
            $ score += 1
            jump alch3question_10
        "Head":
            jump alch3question_10
        "Brain":
            jump alch3question_10
    return

label alch3question_10:
    teacher "Who is the latest president of the Philippines?"
    menu:
        "Arnold Duterte":
            jump end_quizalch3
        "Bong Bong Marcos":
            $ score += 1
            jump end_quizalch3
        "Corny Aquino":
            jump end_quizalch3
    return

label end_quizalch3:
    hide screen quiz_score
    if score <= 10:
        show teacher
        teacher "You only got [score] points. That was unfortunate of you. Better luck next time, [player_name]."
        jump breaktime_lian_ch03
    else:
        show teacher happy
        teacher "Congratualtions, [player_name]! You got [score] points! You did very well!"
        jump breaktime_lian_ch03

    return

label breaktime_lian_ch03:
    scene black
    "Break Time..."
    scene hallway with fade
    play music "audio/hallway.ogg" loop

    "Classes were a bit tiring."
    "You have a short break from class before you continue to the next one."
    "You were strolling on the hallway and reached the library."

    jump alminigame

    return
    label alminigame:
        scene Library
        "There were only a few students in the library."
        "You walked at the back of the library and found old dusty shelves and a few books."
        "You noticed something in a particular shelf"

        call screen al_screen_library

    label al_pic_click:
        scene Library Blurred
        "There is a photo pinned on the old cork board behind the dusty shelf"
        show ALpicture at truecenter
        "You noticed two familiar faces. Ayani and Lian as kids"
        "Maybe they used to be bestfriends, or maybe still friends. You don't know."
        hide ALpicture
        call screen al_screen_library
        return

    label al_engraving_click:
        scene Library Blurred
        show ALengraving at truecenter
        "A + L, Best Friends Forever."
        "Hmmm... You wonder what those letters stand for."
        hide ALengraving
        call screen al_screen_library
        return

    label al_book_click:
        scene Library Blurred
        show ALbook
        "You took the dusty children's book and blew off the dust on the cover."
        "There are things in between the pages"
        hide ALbook
        "The first one was a postcard with a sloppy handwriting"
        show ALpostcard at truecenter
        "City of Lights."
        "Someday we will go to the City of Lights together."
        "Love, Ayani"
        hide ALpostcard
        "there was also a handwritten letter."
        "The handwriting is was full of etiquette and emotion."
        show ALletter at truecenter
        "To my bestest friend, Ayani.."
        "I am very thankful you are my best friend."
        "Hanging out is always so fun with you."
        "You are truly my sister from another mister."
        "Love, Lian H."
        hide ALletter
        "Huh... Ayani and Lian used to be best friends?"
        call screen al_screen_library
        return

    label allibrary_choice:
        scene Library
        menu:
            "Continue lookin at the shelf.":
                call screen al_screen_library
            "Exit the establishment.":
                jump alnext_scene
        return

label alnext_scene:
    scene black
    "You walked out of the library and went back to the classroom."
    scene classroom a with fade
    "Class finally finished."
    if join_student_council == True:
        "But you joined the student council."
        "You need to attend the after class meeting."
        "You went to the second floor and looked for Lian."
        scene hallway
        "As you approach the door, it was dark inside but someone is talking."
        show hana at center
        "It was Hana Chien."
        "Seems like she is talking to someone on the phone."
        hide hana at center
        show hana angry at center, Shake(None, .3, dist=5)
        hana "Gosh! It's getting harder to deal with her."
        "She sounds so upset, and you wonder who is referring to."
        show hana angry at center, Shake(None, .3, dist=5)
        hana "Why do I have to do this? I'm so sick of this."
        hana "I did everything to sabotage every possible way to ruin her."
        hana "But for some reason, life is just way too nice on her."
        hana "Then there's this new-"
        "Hana paused."
        "It seems like she noticed that someone is listening to her."
        menu:
            "Enter the room.":
                hide hana angry
                scene scroom
                "You decided to enter the room."
                "But before that you decided to put on earphones first so she wouldn't suspect that you're listening to her."
                "You entered the room while looking down."
                "You slowly looked at her and removed one earbud."
                main "Oh, hello there miss vice president."
                show hana happy
                "Hana looked at you with an annoyed look."
                main "Oh am I too early? I thought-"
                hide hana happy
                "Before you can finish talking Hana stormed off the room."
                "That was weird and awkward."
                "After a few minutes Lian and Hana entered the room."
                show hana happy at right
                show lian happy at left
                "Hana seems to be completely different."
                "She looks so bright, like a completely different person from earlier."
                "You decided to ignore it for now."
                hide hana happy at right
                hide lian happy at left
                scene black with fade
                "The meeting was not that long yet it was productive."
                show lian
                "Lian is really impressive."
                "She gets to think of creative ways to find solutions to the problems the student council needs to solve."
                "However, you're still bothered by what you heard from Hana."
                hide lian
                menu:
                    "Confront Hana":
                        "You decided to confront Hana about the phone call from earlier."
                        main "Hey, Hana... Can I talk to you for a sec?"
                        show hana happy
                        "Hana forced a smile."
                        hana "Sure, [player_name]."
                        main "About earlier..."
                        hana "Oh I'm sorry I was just not feeling well."
                        "She forced another faker smile."
                        "It made you very uncomfortable."
                        "She's acting so weird."
                        "Before you can say anything again, Lian placed her arm on your shoulder."
                        hide hana happy
                        show lian
                        lian "Hey guys, I see that you are getting along."
                        main "No, yeah.. Uhh.."
                        "You don't know what to say."
                        show hana at right
                        hana "Hehe, yeah [player_name] is very nice and friendly."
                        hide lian
                        hide hana at right
                        menu:
                            "I just want to check on Hana.":
                                show hana at right
                                show lian at left
                                lian"Hana? What's wrong?"
                                "Hana started getting breathing heavily and seems like she's panicking."
                                hide hana at right
                                show hana shock at right
                                hana "Uhhh..."
                                lian "You know I'm always here for you right? You can talk to me."
                                main "She seems so upset earlier and I want to apologize for accidentally evesdropping."
                                hide lian at left
                                show lian sad at left
                                lian "Oh..."
                                hana" Yeah... It's fine. I just had a bad day."
                                hide hana shock at right
                                show hana happy at right
                                "She forced the fake smile again."
                                "It gets even more awkward."
                                main "Oh... I hope you feel better soon."
                                "You walked away since you can't handle the situation."
                                jump al_goinghome

                            "Don't say anything.":
                                show lian happy at left
                                show hana happy at left
                                lian "Oh that's great! I hope you guys become close since we will be working together more in the future."
                                "Lian hugged you both and walked away since she still need to personally talk to some members."
                                "Hana looked at you with a dead gaze."
                                hide lian happy
                                show hana angry at center
                                hana "You know nothing, you heard nothing."
                                "It was threatening."
                                "It gets even more awkward."
                                hide hana angry
                                "You walked away since you can't handle the situation."
                                jump al_goinghome
                    "Ignore.":
                        "You decided to just ignore her and forget what happened."
                        jump al_goinghome

            "Stay quiet and listen more.":
                "You decided to stay quiet and listen more."
                show hana at center
                hana "Oh, sorry I thought someone's coming."
                hana "Anyway, I hope the meeting goes bad because I'm tired of little miss perfect."
                "You wonder if she's talking about Lian."
                "She sounds so upset but they're best friends."
                "You got a bit lost on your train of thoughts."
                hide hana
                show lian happy at center
                lian "Hey, [player_name]! Are you just gonna stare at the door? It won't open itself."
                "Lian cheerfully joked as she open the door for the both of you."
                hide lian happy at center
                "As you enter the room, Hana was there cleaning up and fixing her stuff."
                show hana happy at center
                hana "Oh hey there, I got here a bit too early."
                "She forced a soft fake smile."
                "It was weird."
                "Then she looked at you and her mood change."
                hide hana happy
                show hana
                "You can tell she dislikes you."
                scene black with fade
                "The meeting was not that long yet it was productive."
                "Lian is really impressive."
                "She gets to think of creative ways to find solutions to the problems the student council needs to solve."
                scene hallway
                "However, you're still bothered by what you heard from Hana."
                menu :
                    "Confront Hana":
                        "You decided to confront Hana about the phone call from earlier."
                        main "Hey, Hana... Can I talk to you for a sec?"
                        show hana happy
                        "Hana forced a smile."
                        hana "Sure, [player_name]."
                        main "About earlier..."
                        hana "Oh I'm sorry I was just not feeling well."
                        "She forced another faker smile."
                        "It made you very uncomfortable."
                        "She's acting so weird."
                        "Before you can say anything again, Lian placed her arm on your shoulder."
                        hide hana happy
                        show lian
                        lian "Hey guys, I see that you are getting along."
                        main "No, yeah.. Uhh.."
                        "You don't know what to say."
                        show hana at right
                        hana "Hehe, yeah [player_name] is very nice and friendly."
                        hide lian
                        hide hana at right
                        menu:
                            "I just want to check on Hana.":
                                show hana at right
                                show lian at left
                                lian"Hana? What's wrong?"
                                "Hana started getting breathing heavily and seems like she's panicking."
                                hide hana at right
                                show hana shock at right
                                hana "Uhhh..."
                                lian "You know I'm always here for you right? You can talk to me."
                                main "She seems so upset earlier and I want to apologize for accidentally evesdropping."
                                hide lian at left
                                show lian sad at left
                                lian "Oh..."
                                hana" Yeah... It's fine. I just had a bad day."
                                hide hana shock at right
                                show hana happy at right
                                "She forced the fake smile again."
                                "It gets even more awkward."
                                main "Oh... I hope you feel better soon."
                                "You walked away since you can't handle the situation."
                                jump al_goinghome

                            "Don't say anything.":
                                show lian happy at left
                                show hana happy at left
                                lian "Oh that's great! I hope you guys become close since we will be working together more in the future."
                                "Lian hugged you both and walked away since she still need to personally talk to some members."
                                "Hana looked at you with a dead gaze."
                                hide lian happy
                                show hana angry at center
                                hana "You know nothing, you heard nothing."
                                "It was threatening."
                                "It gets even more awkward."
                                hide hana angry
                                "You walked away since you can't handle the situation."
                                jump al_goinghome

                    "Ignore.":
                        "You decided to just ignore her and forget what happened."
                        jump al_goinghome

        label al_goinghome:
            scene scroom
            "Finally, it's time to go home."
            "On your way out the building, you heard a soft sob."
            menu:
                "Check it out.":
                    scene black with fade
                    "You decided to check it out."
                    "You went to where it was coming from."
                    "It was coming from the other hallway."
                    scene hallway with fade
                    show lian sad at center
                    "You saw Lian against the wall wiping her tears."
                    main "Hey Lian, what's wrong?"
                    "Lian ran to you and hugged you."
                    hide lian sad
                    scene black with fade
                    menu:
                        "Hug her back.":
                            "You decided to hug her back."
                            "She hugged you tighter."
                            $relationship_with_lian += 2
                            "relationship with lian + 2"

                        "Let her hug you.":
                            "You didn't hug back but let her hug you."

                    "She didn't say anything but she kept crying."
                    main "It's okay..."
                    "You can feel her heart beat."
                    main "Cry it all out..."
                    "Lian slowly pulled away."
                    scene hallway
                    show lian sad
                    "She looks pretty even when she's crying."
                    menu:
                        "Wipe her tears":
                            "You decided to wipe her tears."
                            $relationship_with_lian += 2
                            "relationship with lian + 2"

                        "Let her be.":
                            "You decided to just let her be."

                    show lian sad
                    "She looked straight to your eyes."
                    "You can feel her pain."
                    main "Want to tell me what happened?"
                    "Lian took a deep breath."
                    lian" Someone has been sabotaging the events we planned."
                    lian "Before, someone stole the charity funds..."
                    lian "Then the decorations..."
                    lian "Now the documents from the school."
                    lian "I just don't understand why someone would do this."
                    lian "These events are for the students of Tiger High."
                    menu:
                        "It's not your fault.":
                            main "It's not your fault."
                            lian" Well, it's my responsibility as the student council president."
                            lian "When I got elected I promised to serve them, and I don't want to break that promise with a messed up plan."
                            $relationship_with_lian += 2
                            "relationship with lian + 2"
                            menu:
                                "I might have an idea who.":
                                    main "I might have an idea who."
                                    main "But I don't want to falsely accuse someone."
                                    hide lian sad
                                    show lian at center
                                    lian "I'm listening."
                                    main "It's just I thought I heard someone talking about 'sabotaging' earlier."
                                    main "But I'm not sure if it's related."
                                    lian "Who is it?"
                                    "You can't tell her because you might be wrong and you might ruin a friendship."
                                    lian "I won't get mad."
                                    lian "I just want to know so I can talk to them."
                                    lian "I can sort things out."
                                    "You took a deep breath."
                                    main "I think I heard Hana on the phone with someone."
                                    hide lian
                                    show lian shock at center
                                    main "And she was upset and complaining about sabotaging and a mentioned a 'little miss perfect'"
                                    hide lian shock
                                    show lian sad  at center
                                    "Lian looked down and sobbed."
                                    main "But I'm not sure."
                                    lian "I'm gonna go talk to her."
                                    main "Lian wait."
                                    "Lian wiped her tears and ran back to the second floor."
                                    hide lian sad
                                    "She stopped by the stairs."
                                    "You peaked and saw Hana in action with her sabotage."
                                    "Lian turned around and looked at you."
                                    "Her eyes started getting teary again."
                                    $relationship_with_lian += 2
                                    "relationship with lian + 2"
                                    menu:
                                        "Hug her.":
                                            "You decided to hug her."
                                            "She was crying for a bit and you stayed with her."
                                            "After a few conversation, you both decided to go home."
                                            show lian
                                            lian "Thank you very much, [player_name]. I really appreciate it."
                                            "Lian smiled at you weakly. She's still sad and disappointed but you know she feels a lot better."
                                            main "Hey Lian, wanna walk home together? Maybe we can grab snacks to cheer you up."
                                            "Lian seems to love that idea."
                                            "Lian she nodded cheerfully and you walked out the school together."
                                            hide lian
                                            $relationship_with_lian += 2
                                            "relationship with lian + 2"
                                            scene hangout with fade
                                            "Lian seems to be enjoying the evening sky."
                                            "Her eyes sparkle together with the dim street lights."
                                            "You stroll around the park nearby and grabbed some street food."
                                            "Lian seems to enjoy and you can tell you successfully cheered her up."
                                            lian "It's getting late now,[player_name]."
                                            lian "I think it's time to go home."
                                            show lian ending
                                            lian "Thank you so much for doing this for me."
                                            "Lian gave you a big hug to express her gratitude."
                                            main "You're always welcome, Lian."
                                            "Lian appreciates your concern and gave you a sweet smile."
                                            main "Ummm Lian.."
                                            menu:
                                                "I always believe in you." :
                                                        main "I always believe in you."
                                                        main "I'm here whenever you need my help."
                                                        main "You can do this and tomorrow I promise you we can find solutions. Together."
                                                        "You walked home together."
                                                        $relationship_with_lian += 2
                                                        "relationship with lian + 2"
                                                        jump lian_ending_scene


                                                "Nothing.":
                                                    main "Nothing."
                                                    "Lian gave you a soft smile."
                                                    "You went on your seperate ways and went home."
                                                    jump graduation_time

                                        "Don't do anything.":
                                            show lian sad
                                            "She was crying for a bit but you stayed with her."
                                            "After a few conversation, you both decided to go home."
                                            lian "Thank you very much, [player_name]. I really appreciate it."
                                            "Lian smiled at you weakly. She's still sad and disappointed but you know she feels a lot better."
                                            lian "I guess we should go home now. See you tomorrow!"
                                            "Lian walked away and waved you goodbye."
                                            "You walked home alone after."
                                            $relationship_with_lian -= 2
                                            "relationship with lian - 2"
                                            jump graduation_time


                                "Don't say anything.":
                                    show lian sad
                                    "You didn't say anything."
                                    "Lian smiled at you softly and wiped her tears."
                                    lian "It's okay. I can do this."
                                    lian "I'm sorry you have to see me like this."
                                    "Lian fixed herself and walked away."
                                    "You walked home alone after."
                                    $relationship_with_lian -= 3
                                    "relationship with lian - 3"
                                    jump graduation_time


                        "I might have an idea who.":
                            scene hangout
                            main "I might have an idea who."
                            main "But I don't want to falsely accuse someone."
                            main "It's just I thought I heard someone talking about 'sabotaging' earlier."
                            main "But I'm not sure if it's related."
                            lian "Who is it?"
                            "You can't tell her because you might be wrong and you might ruin a friendship."
                            lian "I won't get mad."
                            lian "I just want to know so I can talk to them."
                            lian "I can sort things out."
                            "You took a deep breath."
                            main "I think I heard Hana on the phone with someone."
                            hide lian
                            show lian shock at center
                            main "And she was upset and complaining about sabotaging and a mentioned a 'little miss perfect'"
                            hide lian shock
                            show lian sad  at center
                            "Lian looked down and sobbed."
                            main "But I'm not sure."
                            lian "I'm gonna go talk to her."
                            main "Lian wait."
                            "Lian wiped her tears and ran back to the second floor."
                            hide lian sad
                            "She stopped by the stairs."
                            "You peaked and saw Hana in action with her sabotage."
                            "Lian turned around and looked at you."
                            "Her eyes started getting teary again."
                            $relationship_with_lian += 2
                            "relationship with lian + 2"
                            menu:
                                "Hug her.":
                                    "You decided to hug her."
                                    "She was crying for a bit and you stayed with her."
                                    "After a few conversation, you both decided to go home."
                                    show lian
                                    lian "Thank you very much, [player_name]. I really appreciate it."
                                    "Lian smiled at you weakly. She's still sad and disappointed but you know she feels a lot better."
                                    main "Hey Lian, wanna walk home together? Maybe we can grab snacks to cheer you up."
                                    "Lian seems to love that idea."
                                    "Lian she nodded cheerfully and you walked out the school together."
                                    hide lian
                                    $relationship_with_lian += 2
                                    "relationship with lian + 2"
                                    scene hangout with fade
                                    "Lian seems to be enjoying the evening sky."
                                    "Her eyes sparkle together with the dim street lights."
                                    "You stroll around the park nearby and grabbed some street food."
                                    "Lian seems to enjoy and you can tell you successfully cheered her up."
                                    lian "It's getting late now,[player_name]."
                                    lian "I think it's time to go home."
                                    show lian ending
                                    lian "Thank you so much for doing this for me."
                                    "Lian gave you a big hug to express her gratitude."
                                    main "You're always welcome, Lian."
                                    "Lian appreciates your concern and gave you a sweet smile."
                                    main "Ummm Lian.."
                                    menu:
                                        "I always believe in you." :
                                                main "I always believe in you."
                                                main "I'm here whenever you need my help."
                                                main "You can do this and tomorrow I promise you we can find solutions. Together."
                                                "You walked home together."
                                                $relationship_with_lian += 2
                                                "relationship with lian + 2"
                                                jump lian_ending_scene


                                        "Nothing.":
                                            main "Nothing."
                                            "Lian gave you a soft smile."
                                            "You went on your seperate ways and went home."
                                            jump graduation_time

                                "Don't do anything.":
                                    show lian sad
                                    "She was crying for a bit but you stayed with her."
                                    "After a few conversation, you both decided to go home."
                                    lian "Thank you very much, [player_name]. I really appreciate it."
                                    "Lian smiled at you weakly. She's still sad and disappointed but you know she feels a lot better."
                                    lian "I guess we should go home now. See you tomorrow!"
                                    "Lian walked away and waved you goodbye."
                                    "You walked home alone after."
                                    $relationship_with_lian -= 2
                                    "relationship with lian - 2"
                                    jump graduation_time

                        "Don't say anything.":
                            "You didn't say anything."
                            "Lian smiled at you softly and wiped her tears."
                            lian "It's okay. I can do this."
                            lian "I'm sorry you have to see me like this."
                            "Lian fixed herself and walked away."
                            "You walked home alone after."
                            $relationship_with_lian -= 2
                            "relationship with lian - 2"
                            jump graduation_time
                            return

                "Ignore.":
                    "You decided to just ignore the noise you heard."
                    "It's none of your business."
                    "You walked home."
                    jump graduation_time
                    return

    else:
        scene black with fade
        "Since you didn't join any club,or have any friends to hang out with after class,"
        "You can go straight home."
        "But their was an accident in the usual route you take so it was blocked."
        "You decided to take a longer route."
        "You decided to take a longer route."
        scene hangout with fade
        "On your way home you saw Ayani."
        menu:
            "Approach her.":
                "You decided to approach her."
                main "Hey Ayani."
                if relationship_with_ayani >= 9:
                    show ayani happy at center
                    ayani "Hey, [player_name]."
                    "She said softly."
                    "She looks a bit down."
                    main "Are you okay?"
                    ayani "Not really..."
                    "You sat beside her."
                    ayani "laid her head on your shoulder."
                    "You're worried she'll hear how loud your heart is beating."
                    menu:
                        "I'm here for you.":
                            main "I'm here for you."
                            "Ayani hugged your arm."
                            ayani "Thanks, wimp."
                            main "You're calling me a wimp too now?"
                            "You both chuckled."
                            ayani "Kai told me you're one of her childhood bestfriends..."
                            "Now you remember her."
                            "You realized why she talks to you that way."
                            main "Yeah... Couldn't really recognize her."
                            ayani "Them."
                            main "I couldn't really recognize them."
                            "Ayani nodded her head."
                            ayani "I used to have a childhood bestfriend too."
                            ayani "Kai and I are the same."
                            ayani "We were abandoned."
                            ayani "But I understand why you left."
                            ayani "I still care about my childhood bestfriend."
                            ayani "And I know she needs me right now."
                            ayani "But I couldn't help her."
                            ayani "I can't do anything."
                            menu:
                                "Lian?":
                                    main "Lian?"
                                    hide ayani
                                    show ayani shock at center
                                    ayani "How did you know?"
                                    menu:
                                        "The abandoned part of the library.":
                                            main "The abandoned part of the library."
                                            hide ayani shock
                                            show ayani happy
                                            ayani "I knew it, someone else was there."
                                            ayani "I hoped it was her, but it turns out it was you."
                                            ayani "I'm not mad though."
                                            "Ayani looked at you and smiled."
                                            "You had a few more conversation and you were able to get to know her better."
                                            ayani "Thank you. Thank you for being here for me."
                                            ayani "And I'm sorry I was mean to you."
                                            show ayani ending with fade
                                            "Ayani gave you a hug and a kiss on your left cheek."
                                            "You spent the time appreciating the evening sky with Ayani."
                                            $relationship_with_ayani += 5
                                            "relationship with ayani + 5"
                                            jump ayani_ending_scene

                                        "Wild guess.":
                                            main "Wild guess."
                                            hide ayani shock
                                            show ayani happy
                                            ayani "Your guesses are accurate."
                                            "Ayani chuckled."
                                            ayani "What made you think I was ever be friends with Lian?"
                                            ayani "I mean, we're completely different."
                                            ayani "Just look at her."
                                            ayani "We live in the same town but in a completely different world."
                                            ayani "Some friendships are just not meant to be."
                                            ayani "You can't always choose your friends."
                                            ayani "Which is quite sad."
                                            "Ayani talked about more of her feelings and you gladly listened."
                                            jump graduation_time

                                "Najma?":
                                    main "Najma?"
                                    show ayani shock
                                    "Ayani cringed."
                                    ayani "The butch loud lesbian?"
                                    ayani "No. She's annoying."
                                    ayani "I would never be friends with her."
                                    "Ayani chuckled."
                                    ayani "It doesn't mean I'm friendly to weirdos like you I would be friends with other weirdos."
                                    hide ayani shock
                                    show ayani happy
                                    "Ayani kept on laughing."
                                    ayani "But you're a special weirdo."
                                    "You spent some time throwing jokes and cheering Ayani up."
                                    "After a while the both of you decided to go home before it gets dark."
                                    "You guess you're officially friends now."
                                    $relationship_with_ayani -= 2
                                    "Relationship with Ayani - 2"
                                    jump graduation_time

                                "Chihiro?":
                                    main "Chihiro?"
                                    show ayani shock
                                    "Ayani look confused."
                                    ayani "Who?"
                                    ayani "Wait, you mean the shy quiet girl in class?"
                                    ayani "I've never even heard her spoke."
                                    hide ayani shock
                                    "Ayani chuckled."
                                    ayani "It doesn't mean I'm friendly to weirdos like you I would be friends with other weirdos."
                                    ayani "kept on laughing."
                                    "ayani But you're a special weirdo."
                                    "You spent some time throwing jokes and cheering Ayani up."
                                    "After a while the both of you decided to go home before it gets dark."
                                    "You guess you're officially friends now."
                                    $relationship_with_ayani -= 1
                                    "Relationship with Ayani - 1"
                                    jump graduation_time

                                "Who?":
                                    main "Who?"
                                    ayani "Won't tell."
                                    "You still had a few little conversations but Ayani said she needs to go home before it gets dark."
                                    "You walked home together."
                                    "That was a nice wholesome time with Ayani."
                                    $relationship_with_ayani -= 1
                                    "Relationship with Ayani - 1"
                                    jump graduation_time

                                "Don't say anything":
                                    ayani "Well yeah, I need to completely move on from it."
                                    ayani "It was years and years ago."
                                    "You still had a few little conversations but Ayani said she needs to go home before it gets dark."
                                    "You walked home together."
                                    "That was a nice wholesome time with Ayani."
                                    $relationship_with_ayani -= 2
                                    "Relationship with Ayani - 2"
                                    jump graduation_time

                        "Don't say anything.":
                            show ayani
                            ayani "Thanks, wimp."
                            "You still had a few little conversations but Ayani said she needs to go home before it gets dark."
                            "You walked home together."
                            "That was a nice wholesome time with Ayani."
                            jump graduation_time

                else:
                    show ayani angry at center
                    ayani "What do you want loser?"
                    ayani "Geez man you gotta stop being such a creep."
                    "Ayani started getting even more upset."
                    ayani "Why do you even keep on stalking me?"
                    ayani "What the hell is wrong with you?!"
                    show ayani angry at center, Shake(None, .3, dist=5)
                    "Ayani couldn't stop talking meanly to you and you didn't have a choice but to walk away."
                    "You kind of upset her more."
                    "She will hate you forever."
                    jump graduation_time
                    return

            "Ignore":
                "You decided to just ignore her since approaching her is a bit hard."
                "You walked home."
                jump graduation_time
                return
















































label najma_v_chihiro_ch03:
    scene street

    "On your way to school you saw a few classmates you're acquainted with."
    "Chihiro and Najma are walking to school together."
    "You didn't expect them to be friends,"
    "or even know each other in the first place."

    menu:
        "Call Chihiro":
            $ relationship_with_chihiro += 2
            main "Chihiro!"
            "Chihiro turned to you."
            "Chihiro waved at you softly with a gentle sweet smile."
            "You walk towards her."
            show chihiro happy at left:
                xpos -300
                ypos 1100
            show najma happy:
                xpos 550
                ypos 80
            najma "Wow I didn't know you were friends."
            najma "I mean I should've expected that."
            hide chihiro
            hide najma
            scene black
            "Relationship with Chihiro + 2"
            scene street
            "As you guys were talking, a tall athletic guy approached you."
            show justin happy
            justin "Hey!"
            main "Hey..."
            hide justin happy
            show justin happy at left:
            show najma happy at right:
            najma "Sup bro!"
            hide justin
            hide najma
            "Justin ignored you both and went to Chihiro."
            "He hugged her and kissed her forehead."
            show justin at left:
                xpos -300
                ypos 1100
            show chihiro:
                xpos 550
                ypos 80
            justin "I see you got a new friend."
            chihiro "This is [player_name]."
            chihiro "[theyre!t!c] are from our class."
            "Justin looked at you from head to toe."
            justin "I'm Justin. Chihiro's boyfriend."
            hide chihiro
            show justin at left:
                xpos -300
                ypos 1100
            show najma:
                xpos 550
                ypos 80
            najma "The captain of the basketball team."
            justin "Yeah, I'm surprised you don't know me."
            hide najma
            show justin at left:
                xpos -300
                ypos 1100
            show chihiro:
                xpos 550
                ypos 80
            chihiro "[they!t!c] new."
            hide chihiro
            show justin at left:
                xpos -300
                ypos 1100
            show najma:
                xpos 550
                ypos 80
            najma "[they!t!c] new."
            main "I'm new."
            "Justin keeps clinging on Chihiro and she seems uncomfortable."
            main "Chi-"
            "Before you can speak, Najma interrupted you."
            najma "Hey why won't you come with me for a sec."
            "Najma dragged Justin away from the both of you."
            hide justin
            hide najma
            show chihiro
            chihiro "Najma always have my back, I'm grateful for her."
            main "She's a nice person."
            main "I just didn't expect you to be friends."
            chihiro "We're not just friends."
            "Chihiro paused."
            chihiro "We're sisters."
            main "Wait- really?"
            "Chihiro nodded softly."
            chihiro "She's my stepsister."
            main "I see."

            menu:
                "Ask about Justin.":
                    main "So Justin's your boyfriend?"
                    "Chihiro shrugged."
                    chihiro "Yeah..."
                    main "You don't seem to like him."
                    main "Why are you even with him?"
                    "Chihiro didn't answer."
                    "You walked to school together in silence."
                    jump outschool_najma_ch03

                "Ask about Najma.":
                    main "It's nice to see that you're close with your sister."
                    chihiro "Yeah, we were childhood bestfriends too."
                    chihiro "We were neighbors and we grew up playing together,"
                    chihiro "Until our parents decided to-"
                    chihiro "Anyway we're late for class."
                    main "Yeah, yeah. Let's go."
                    "You walked to school together and it's nice to see Chihiro opening up a little."
                    jump outschool_najma_ch03

                "Don't say anything.":
                    chihiro "Alrighty, then. Let's walk to school now."
                    "You walked to school together and it's nice to see Chihiro opening up a little."
                    jump outschool_najma_ch03

        "Call Najma":
            $ relationship_with_najma += 2
            main "Hey, Najma!"
            "Najma turned to you."
            "Najma gave you a big wave and a bright smile."
            "You walk towards them."
            show najma happy
            najma "Sup, bro."

            if join_sports_club == True:
                najma "I see you're gaining a bit for that muscle. Good job!"
                "Najma placed her arms over your shoulder."
                najma "Chi, you know [player_name]? New member, sports stuff."
                "Chihiro giggled and nodded softly."
                "That's weird."

            else:
                najma "Still haven't reconsidered joining the sports club?"
                "You shook your head."
                "Najma chuckled."
                najma "You're gaining the muscle though."
                najma "Anyway, Chi, [player_name], [player_name], Chi."

            "As you guys were talking, a tall athletic guy approached you."
            show justin happy
            justin "Hey!"
            main "Hey..."
            show justin happy at left:
                xpos -300
                ypos 1100
            show najma happy at right:
                xpos -300
                ypos 1100
            najma "Sup bro!"
            hide justin
            hide najma
            "Justin ignored you both and went to Chihiro."
            "He hugged her and kissed her forehead."
            show justin at left:
                xpos -300
                ypos 1100
            show chihiro:
                xpos 550
                ypos 80
            justin "I see you got a new friend."
            chihiro "This is [player_name]."
            chihiro "[theyre!t!c] are from our class."
            "Justin looked at you from head to toe."
            justin "I'm Justin. Chihiro's boyfriend."
            hide chihiro
            show justin at left:
                xpos -300
                ypos 1100
            show najma:
                xpos 550
                ypos 80
            najma "The captain of the basketball team."
            justin "Yeah, I'm surprised you don't know me."
            hide najma
            show justin at left:
                xpos -300
                ypos 1100
            show chihiro:
                xpos 550
                ypos 80
            chihiro "[they!t!c] new."
            hide chihiro
            show justin at left:
                xpos -300
                ypos 1100
            show najma:
                xpos 550
                ypos 80
            najma "[they!t!c] new."
            main "I'm new."
            "Justin keeps clinging on Chihiro and she seems uncomfortable."
            main "Chi-"
            "Before you can speak, Najma interrupted you."
            najma "Hey why won't you come with me for a sec."
            "Najma dragged Justin away from the both of you."
            hide justin
            hide najma
            show chihiro
            chihiro "Najma always have my back, I'm grateful for her."
            main "She's a nice person."
            main "I just didn't expect you to be friends."
            chihiro "We're not just friends."
            "Chihiro paused."
            chihiro "We're sisters."
            main "Wait- really?"
            "Chihiro nodded softly."
            chihiro "She's my stepsister."
            main "I see."

            menu:
                "Ask about Justin.":
                    main "So Justin's your boyfriend?"
                    "Chihiro shrugged."
                    chihiro "Yeah..."
                    main "You don't seem to like him."
                    main "Why are you even with him?"
                    "Chihiro didn't answer."
                    "You walked to school together in silence."
                    jump outschool_najma_ch03

                "Ask about Najma.":
                    main "It's nice to see that you're close with your sister."
                    chihiro "Yeah, we were childhood bestfriends too."
                    chihiro "We were neighbors and we grew up playing together,"
                    chihiro "Until our parents decided to-"
                    chihiro "Anyway we're late for class."
                    main "Yeah, yeah. Let's go."
                    "You walked to school together and it's nice to see Chihiro opening up a little."
                    jump outschool_najma_ch03

                "Don't say anything.":
                    chihiro "Alrighty, then. Let's walk to school now."
                    "You walked to school together and it's nice to see Chihiro opening up a little."
                    jump outschool_najma_ch03

        "Ignore them.":
            "You decided to just ignore them."
            "You walked to school alone."
            jump outschool_najma_ch03

    return

label outschool_najma_ch03:
    scene out school

    "You finally reached the school gate."
    "You walked along the other students but on your way in the guard stopped you."
    show guard
    guard "School ID?"
    "You looked down on your chest and realized you don't have your ID on."
    "You started panicking and kept searching your bag."
    "You can't go back home to fetch your ID."
    "And then suddenly..."
    show guard at left:
        xpos -300
        ypos 1100
    show najma:
        xpos 550
        ypos 80
    najma "Good morning Mrs. D, this is [player_name], [they!t] is a new student. He/She still don't have an ID issued."
    "She paused."
    najma "You'll let [them!t] in right?"
    "Mrs. Dimaapi shook her head and laughed."
    guard "Alrighty just make sure tomorrow you have that ID."
    hide najma
    hide guard
    "You, Najma and Chihiro walked to class together."
    jump classroom_najma_ch03

    return

label classroom_najma_ch03:
    scene classroom m
    "You finally reached your classroom."
    show chihiro at left:
        xpos -300
        ypos 1100
    show najma:
        xpos 550
        ypos 80
    main "Thank you, guys."
    show chihiro happy at left:
        xpos -300
        ypos 1100
    show najma happy:
        xpos 550
        ypos 80
    "They both smiled at you."
    najma "Anytime, [player_name]."
    "You went to your seat."

    hide chihiro happy
    hide najma happy
    show teacher
    teacher "Good morning class!."
    teacher "Let's continue and add your grades with a little quiz, shall we?"
    teacher "Here we go."
    jump ch3question_1


    return

label ch3question_1:
    stop music
    play music "audio/quiz.ogg"
    show screen quiz_score2
    teacher "Which core ingredient is important when preparing sushi?"
    menu:
        "Rice":
            $ score_2 += 1
            jump ch3question_2
        "Salt":
            jump ch3question_2
        "Wasabi":
            jump ch3question_2
    return

label ch3question_2:
    teacher "He invented/patented the light bulb."
    menu:
        "Nikola Tesla":
            jump ch3question_3
        "Joe Biden":
            jump ch3question_3
        "Thomas Edison":
            $ score_2 += 1
            jump ch3question_3
    return

label ch3question_3:
    teacher "Also known a H20"
    menu:
        "Koy":
            jump ch3question_4
        "Water":
            $ score_2 += 1
            jump ch3question_4
        "Magma":
            jump ch3question_4
    return

label ch3question_4:
    teacher "What is the currency of the Philippines?"
    menu:
        "Pound":
            jump ch3question_5
        "Peso":
            $ score_2 += 1
            jump ch3question_5
        "Dollar":
            jump ch3question_5
    return

label ch3question_5:
    teacher "Bacon is made from pork-"
    menu:
        "Belly":
            $ score_2 += 1
            jump ch3question_6
        "Shoulder":
            jump ch3question_6
        "Leg":
            jump ch3question_6
    return

label ch3question_6:
    teacher "The essence of what to be or a being in a state of being?"
    menu:
        "Existence":
            $ score_2 += 1
            jump ch3question_7
        "Ecstacy":
            jump ch3question_7
        "Elaborate":
            jump ch3question_7
    return

label ch3question_7:
    teacher "The largest Desert in the world?"
    menu:
        "Sahara":
            jump ch3question_8
        "Antarctica":
            $ score_2 += 1
            jump ch3question_8
        "Saudi Arabia":
            jump ch3question_8
    return

label ch3question_8:
    teacher "What programming language is based on an animal?"
    menu:
        "Pyhton":
            $ score_2 += 1
            jump ch3question_9
        "Snake":
            jump ch3question_9
        "Cobra":
            jump ch3question_9
    return

label ch3question_9:
    teacher "This part of the body is also considered as our crown. "
    menu:
        "Hair":
            $ score_2 += 1
            jump ch3question_10
        "Head":
            jump ch3question_10
        "Brain":
            jump ch2question_10
    return

label ch3question_10:
    teacher "Who is the latest president of the Philippines?"
    menu:
        "Arnold Duterte":
            jump end_quizch3
        "Bong Bong Marcos":
            $ score_2 += 1
            jump end_quizch3
        "Corny Aquino":
            jump end_quizch3
    return

label end_quizch3:
    hide screen quiz_score
    if score <= 13:
        show teacher
        teacher "You only got [score] points. That was unfortunate of you. Better luck next time, [player_name]."
        jump breaktime_najma_ch03
    else:
        show teacher happy
        teacher "Congratualtions, [player_name]! You got [score] points! You did very well!"
        jump breaktime_najma_ch03

    return


label breaktime_najma_ch03:
    scene black
    "Break Time..."
    scene hallway with fade
    play music "audio/hallway.ogg" loop

    "Classes were a bit tiring."
    "You have a short break from class before you continue to the next one."
    "You were strolling on the hallway and reached the library."

    label ncminigame:
        scene Library
        "There were only a few students in the library."
        "You walked at the back of the library and found old dusty shelves and a few books."
        "You noticed something in a particular shelf"
        call screen nc_screen_library
        return

    label nc_pic_click:
        scene Library Blurred
        "There are a few photos pinned on the old cork board behind the dusty shelf."
        "You noticed two familiar faces. Chihiro and Najma as kids."
        show NCpicture at truecenter
        "So they were really best friends growing up."
        hide NCpicture
        call screen nc_screen_library
        return


    label nc_engraving_click:
        scene Library Blurred
        show NCengraving at truecenter
        "C + N, The Princess and the Knight."
        "Hmmm... You wonder what those letters stand for."
        hide NCengraving
        call screen nc_screen_library
        return


    label nc_book_click:
        scene Library Blurred
        "You took the dusty children's book and blew off the dust on the cover."
        "There's something in between the pages"
        show NCletter at truecenter
        "A handwritten letter. The handwriting is sloppy. It is probably written by child."
        "To: Chi"
        "I am upset that we will be sisters tomorrow. "
        "I don't want that. That would be weird."
        "I want to be your prince someday."
        "From: Naj"
        "Huh... that's an interesting letter from Najma."
        hide NCletter
        call screen nc_screen_library
        return


    label nc_poster_click:
        scene Library Blurred
        show NCcomic at truecenter
        "Lady Knight. I will always protect you. Love, Najma."
        "Hmmm... from Najma. Interesting..."
        hide NC poster
        call screen nc_screen_library
        return

    label nclibrary_choice:
        scene Library
        menu:
            "Continue lookin at the shelf.":
                call screen nc_screen_library
            "Exit the establishment.":
                jump ncnext_scene
        return

label ncnext_scene:
    scene black with fade
    "You walked out of the library and went back to the classroom."
    $renpy.pause(1.0)
    scene classroom a with fade
    "Class finally finished."
    if join_sports_club == True:
        scene black
        "But you joined the sports club."
        "You need to attend the after class meeting."
        "You went to the school gym and looked for Najma."
        scene field with fade
        "When you got there, someone bumped into you"
        "It was just Justin."
        show justin happy at center
        "Justin nodded at you."
        justin "Sup loser."
        "You nodded back at him but didn't say anything back."
        show justin angry at center
        justin "You need to stay away from my girl."
        main "Chihiro?"
        justin "Chihiro"
        main "We're just friends, plus she doesn't speak much."
        justin "And earlier she spoke too much."
        main "Well she could socialize more."
        justin "I don't like you."
        menu:
            "I don't like your either.":
                main "I don't like you either."
                show justin angry at center, Shake(None, .3, dist=5)
                "Justin stood up and went to you angrily."
                $ reputation += 2
                "Reputation + 2"

            "Don't say anything.":
                "You decided to not say anything."
                justin "You know what?"
                show justin angry at center, Shake(None, .3, dist=5)
                "Justin stood up and went to you angrily."

                "He was about to lift you up with your shirt."
                "Luckily Najma came."
                show najma shock at left:
                    xpos -300
                    ypos 1100
                show justin:
                    xpos 550
                    ypos 80

                najma "Guys what the hell is happening here?"
                justin "Nothing. We're just talking."
                najma "Justin stop picking on new members."
                najma "This is why no one wants to join."
                justin "How is this my fault, I'm not doing anything."
                najma "You're going too far."
                najma "Everyone reports you being a big bully."
                hide najma shock
                hide justin
                show justin angry at center, Shake(None, .3, dist=5)
                "Justin got upset and threw his chair across the court."
                show najma angry at left:
                    xpos -300
                    ypos 1100
                show justin angry:
                    xpos 550
                    ypos 80
                najma "I can't believe Chihiro is dating a prick like you!"
                justin "I'm a what now? Huh, girlie?"
                najma "Don't you start."
                show najma angry at left, Shake(None, .3, dist=5):
                    xpos -300
                    ypos 1100
                show justin angry at right, Shake(None, .3, dist=5):
                    xpos 550
                    ypos 80
                "Najma and Justin started shouting at each other."
                "You managed to stop them from being physical."
                justin "She will never like you, you're not a guy."
                najma "You know what that's-"
                "You got infront of Najma and shook your head."
                "Najma sighed."
                najma "You're right he's not worth it."
                "Najma grabbed you with her and walked out of the gym."
                najma "I'm sorry you had to see that."
                main "It's okay."
                menu:
                    "Hangout with Najma":
                        show najma at center
                        main"Hey wanna hang out?"
                        main"Maybe cool off and try to release the stress from what happened earlier?"
                        hide najma
                        show najma happy at center
                        "Najma smiled."
                        najma "Yeah, sure that would be fun. Let's grab some slushie too."
                        hide najma happy at center
                        $ renpy.pause(2.0)
                        scene street with fade
                        "You and Najma decided to hang out for the rest of the day."
                        "You went to the nearby convinient store first."
                        "Najma got some strawberry and orange slushie."
                        "You went for the same one."
                        "You got out of the convinient store and walked the streets with her."
                        show najma happy at center
                        najma "Did you know this is also Chihiro's favorite flavor?"
                        main "No surprise."
                        najma "She actually discovered this combination."
                        najma "The soury-sweet strawberry flavor and the citrus refreshing orange flavor."
                        najma "Perfect."
                        menu:
                            "Just like her?":
                                najma "Yeah, just like her."
                                $ relationship_with_najma += 3
                                "relationship with Najma + 3"
                                menu:
                                    "Ask her about her relationship with Chihiro.":
                                        main "So Chihiro and you..."
                                        if relationship_with_najma >= 6:
                                            najma "Yeah, I know it's quite obvious."
                                            najma "It's weird but I've been in love with her since we were little."
                                            menu:
                                                "The Knight and The Princess":
                                                    main "The Knight and The Princess."
                                                    $ relationship_with_najma += 3
                                                    show najma shock at center
                                                    najma "Yeah, that's our favorite story book as kids."
                                                    hide najma shock at center
                                                    show najma happy at center
                                                    najma "Still mine."
                                                    najma "I've always been her knight, and she's my princess."
                                                    "Relationship with Najma + 3"
                                                    return

                                                "The Sun and Moon":
                                                    main "The Sun and Moon"
                                                    najma "Hmmm?"
                                                    main "Oh never mind."
                                                    return

                                                "Twin Flowers":
                                                    main "Twin Flowers"
                                                    najma "Hmmm?"
                                                    main "Oh never mind."
                                                    return

                                                    hide najma happy at center
                                                    show najma sad at center
                                                    najma "I just wish it was me and her that's together. Not our parents."
                                                    menu:
                                                        "Have you tried telling her?":
                                                            main "Have you tried telling her?"
                                                            hide najma sad at center
                                                            show najma shock at center
                                                            najma "No, I'm scared."
                                                            "Najma paused."
                                                            show najma at center
                                                            hide najma at center
                                                            show najma sad at center
                                                            najma "I'm scared to lose her."
                                                            najma "I'm scared she will start avoiding me."
                                                            main "At least you tried."
                                                            main "If she won't feel the same and start avoiding you,"
                                                            main "At least you told her what you truly felt."
                                                            main "But I'm not sure if it will be worth the risk."
                                                            najma "Why can't we just be with people we want?"
                                                            main "The world is not fair that way."
                                                            najma "Aight let's just do something fun today."
                                                            najma "No need to dwell over things we can't really do much."
                                                            najma"I think I'm satisfied by just loving her by secret."
                                                            "Najma swiped some tears on her eyes."
                                                            hide najma sad at center
                                                            show najma ending
                                                            najma "Thank you for being with me at my most vulnerable moment."
                                                            najma "I appreciate it."
                                                            "You proceed to just walk around the town with her and throw some jokes around."
                                                            "It was a fun day with her."
                                                            jump najma_ending_scene

                                                        "How did she end up with Justin?":
                                                            main "How did she end up with Justin?"
                                                            "Najma was just silent."
                                                            show najma sad at center
                                                            main "I am sorry shouldve not asked."
                                                            najma "I was a coward."
                                                            najma "I had the chance to tell her."
                                                            najma "A lot times I could've told her what I truly felt."
                                                            najma "I took every chance for granted."
                                                            najma "I was a coward and now I've lost her."
                                                            main "I don't think it's too late."
                                                            najma "How can you tell?"
                                                            main "She doesn't seem to smile as much when she's around you."
                                                            najma "She's happy around me because she's comfortable."
                                                            najma "And she trusts me."
                                                            najma "Let's not talk about it, okay?"
                                                            najma "Let's just go home."
                                                            "You went the separate ways and went home alone."
                                                            hide najma sad at center
                                                            jump graduation_time

                                                        "Don't say anything.":
                                                            "You decided to not a say anything."
                                                            najma "Let's not talk about it, okay?"
                                                            najma "Let's just go home."
                                                            "You went the separate ways and went home alone."
                                                            jump graduation_time

                                        else:
                                            najma "Let's not talk about it, okay?"
                                            najma "Let's just go home."
                                            "You went the separate ways and went home alone."
                                            jump graduation_time

                                    "Don't say anything":
                                        "You decided to not a say anything."
                                        najma "Let's not talk about it, okay?"
                                        najma "Let's just go home."
                                        "You went the separate ways and went home alone."
                                        jump graduation_time
                                        return

                            "Just like you.":
                                main "Just like you."
                                show najma shock at center
                                najma "looked at you confused."
                                najma "Am I getting the wrong idea?"
                                jump graduation_time

                            "Don't say anything.":
                                "You decided to not a say anything."
                                najma "I'm kind of tired today, might take a rest for the rest of the day."
                                najma "Thanks for the slushie though."
                                najma "Let's just go home."
                                "You went the separate ways and went home alone."

                    "Go Home":
                        "You decided to not a say anything."
                        najma "Let's not talk about it, okay?"
                        najma "Let's just go home."
                        "You went the separate ways and went home alone."
                        jump graduation_time

    else:
        scene black
        "Since you didn't join any club,or have any friends to hang out with after class,"
        "You can go straight home."
        scene roadside with fade
        "On your way home you saw Chihiro."
        "She seems to be in disarray as you bumped into her."
        show chihiro at center
        chihiro "I'm sorry I didn't see you."
        main "Oh, Chihiro, it's okay."
        menu:
            "Ask her if she's okay":
                main "Are you okay?"
                if relationship_with_chihiro >= 6:
                    chihiro "Honestly, no. I'm not okay..."
                    hide chihiro
                    show chihiro sad at center
                    "Chihiro burst into tears."
                    menu:
                        "Comfort her.":
                            $ relationship_with_chihiro + 3
                            "You decided to hug Chihiro."
                            "Chihiro hugged you back."
                            "You stroked your hand on the back of her head."
                            main "You can talk to me about it."
                            main "I'm here to listen."
                            chihiro "I can't take him anymore."
                            main "Justin?"
                            chihiro "Yeah, he's so full of himself."
                            chihiro "I just want to be free."
                            main "Is he too controlling?"
                            "Chihiro nodded."
                            main "You shouldn't let someone like him boss over you."
                            chihiro "I don't know what to do."
                            "relationship with chihiro + 3"
                            menu:
                                "Talk to him.":
                                    main "You can talk to him."
                                    "Chihiro looked down."
                                    main "Oh, you're scared of him."
                                    "Chihiro nodded softly."
                                    main "Well, you shouldn't. Because..."
                                    menu:
                                        "I'm here for you.":
                                            main "Because I'm here for you."
                                            show chihiro at center
                                            "Chihiro looked at you right on the eyes."
                                            "Chihiro kissed you on the cheek."
                                            "You turned red."
                                            hide chihiro at center
                                            show chihiro happy at center
                                            "You couldn't move nor say anything."
                                            "Chihiro giggled softly."
                                            chihiro "Wanna go to my favorite spot?"
                                            menu:
                                                "Agree.":
                                                    main "Yeah, sure."
                                                    scene park with fade
                                                    "Chihiro brought you to her favorite spot in town."
                                                    "It was beautiful."
                                                    "Just like her."
                                                    "You talked about things and you successfully cheered her up."
                                                    "She's an innocent pure soul."
                                                    "You watched the sunset with her."
                                                    jump chihiro_ending_scene

                                                "Go home.":
                                                    main "No, thanks."
                                                    chihiro "No."
                                                    chihiro "You don't have the right to reject me."
                                                    chihiro "Oh, you're not going anywhere."
                                                    chihiro "You are mine."
                                                    jump secret_bad_ending_scene

                                        "Najma is there for you.":
                                            show chihiro
                                            main "Najma is there for you."
                                            chihiro "Yeah, she has always been there for me."
                                            chihiro "Since we were little."
                                            chihiro "I'm glad now she's my sister."
                                            main "See, you've got someone."
                                            main "I guess I'm here for you too since we're friends now, right?"
                                            hide chijiro
                                            show chihiro happy
                                            chihiro "Yeah, we're friends now."
                                            "Chihiro giggled softly."
                                            "You walked her home and you walked home after."
                                            $ relationship_with_chihiro += 2
                                            "relationship with chihiro + 2"
                                            jump graduation_time

                                "Let's talk to him.":
                                    main "Let's talk to him."
                                    chihiro "Aren't you scared of him?"
                                    main "No, because..."
                                    "I'm here for you."
                                    main "Because I'm here for you."
                                    "Chihiro looked at you right on the eyes."
                                    "Chihiro kissed you on the cheek."
                                    "You turned red."
                                    "You couldn't move nor say anything."
                                    "Chihiro giggled softly."
                                    chihiro "Wanna go to my favorite spot?"
                                    menu:
                                        "I'm here for you.":
                                            main "Because I'm here for you."
                                            "Chihiro looked at you right on the eyes."
                                            "Chihiro kissed you on the cheek."
                                            "You turned red."
                                            "You couldn't move nor say anything."
                                            "Chihiro giggled softly."
                                            chihiro "Wanna go to my favorite spot?"
                                            menu:
                                                "Agree.":
                                                    main "Yeah, sure."
                                                    scene park with fade
                                                    "Chihiro brought you to her favorite spot in town."
                                                    "It was beautiful."
                                                    "Just like her."
                                                    "You talked about things and you successfully cheered her up."
                                                    "She's an innocent pure soul."
                                                    "You watched the sunset with her."
                                                    jump chihiro_ending_scene

                                                "Go home.":
                                                    main "No, thanks."
                                                    chihiro "No."
                                                    chihiro "You don't have the right to reject me."
                                                    chihiro "Oh, you're not going anywhere."
                                                    chihiro "You are mine."
                                                    jump secret_bad_ending_scene

                                        "Najma is there for you.":
                                            show chihiro
                                            main "Najma is there for you."
                                            chihiro "Yeah, she has always been there for me."
                                            chihiro "Since we were little."
                                            chihiro "I'm glad now she's my sister."
                                            main "See, you've got someone."
                                            main "I guess I'm here for you too since we're friends now, right?"
                                            hide chijiro
                                            show chihiro happy
                                            chihiro "Yeah, we're friends now."
                                            "Chihiro giggled softly."
                                            "You walked her home and you walked home after."
                                            $ relationship_with_chihiro += 2
                                            "relationship with chihiro + 2"
                                            jump graduation_time

                        "Don't say anything.":
                            "You didn't do anything."
                            show chihiro sad at center
                            "Chihiro felt worse."
                            chihiro "I'm sorry you have to see this."
                            "Chihiro ran away."
                            "You went home alone."
                            $relationship_with_chihiro -= 2
                            "relationship with chihiro - 2"
                            jump graduation_time


                else:
                    chihiro "Yeah, I'm fine."
                    main "Are you sure?"
                    chihiro "Yeah."
                    main "Are you sure you can go home on your own?"
                    chihiro "Yes."
                    "She ran away from you."
                    "You went home alone."
                    jump graduation_time

            "Go home.":
                main "Be careful on your way home and watch your surroundings so you won't bump to people again."
                "You went the separate ways and went home alone."
                $ relationship_with_chihiro -= 3
                "relationship with chihiro - 3"
                jump graduation_time
                return




























































label graduation_time:
    if relationship_with_mom >= 9 or reputation >= 10 or grades >= 15:
        jump neutral_ending_scene
    else:
        jump bad_ending_scene
    return

label lian_ending_scene:
    scene black
    $renpy.pause(2.0)
    show lian ending with fade
    "You and Lian became one another's pillar."
    $renpy.pause(1.0)
    "She decided to forgive and confront her sister, Hana."
    $renpy.pause(1.0)
    "Hana decided to give up pestering Lian and transferred to another school."
    $renpy.pause(1.0)
    "Lian also made up with ayani because of you constantly asking what their relationship is."
    $renpy.pause(1.0)
    "The rest of your school days were full of responsibility and honor with the help of everyone."
    scene black
    $renpy.pause(2.0)
    "You have unlocked Lian's Ending"
    jump credits_scene
    return



label ayani_ending_scene:
    scene black
    $renpy.pause(2.0)
    show ayani ending with fade
    "Due to Ayani being able to open up to you,she mustered up courage to talk to Lian after so many years."
    $renpy.pause(1.0)
    "Lian and Ayani found time to reignite their friendship.."
    $renpy.pause(1.0)
    "Ayani really appreciates your presence and had grown soft when you're around."
    $renpy.pause(1.0)
    "She clings to you whenever you are around."
    $renpy.pause(1.0)
    "The remaining days before graduation was full of bliss, hugs and envy looks (lol). "
    scene black
    $renpy.pause(2.0)
    "You have unlocked Ayani's Ending"
    jump credits_scene
    return


label najma_ending_scene:
    scene black
    $renpy.pause(2.0)
    show najma ending with fade
    "You found a friend by connecting and not leaving people on their most vulnerable moment."
    $renpy.pause(1.0)
    "She decided to confess her love to Chihiro and was rejected."
    $renpy.pause(1.0)
    "But she decided she will support Chihiro on her endeavors and happiness."
    $renpy.pause(1.0)
    "Your time with Najma was full of warmth and joy"
    $renpy.pause(1.0)
    "You spend the rest of your school days with an active participation in school activities with Najma"
    scene black
    $renpy.pause(2.0)
    "You have unlocked Najma's Ending"
    jump credits_scene
    return

label chihiro_ending_scene:
    scene black
    $renpy.pause(2.0)
    show chi ending with fade
    "Chihiro smacks a kiss on your right cheek after your intimate talk with one another."
    $renpy.pause(1.0)
    "She decided to break up with Justin and you were bullied for the whole semester."
    $renpy.pause(1.0)
    "But it was all worth it because you have both the support of Najma and Chihiro."
    $renpy.pause(1.0)
    "Your time with Chihiro during the semester was wholesome, relax and calm."
    $renpy.pause(1.0)
    "But you can't feel to get a grasp on her true self... Maybe you can ask her next time..."
    scene black
    $renpy.pause(2.0)
    "You have unlocked Chihiro's Ending"
    jump credits_scene
    return

label neutral_ending_scene:
    scene black
    $renpy.pause(2.0)
    show neutral ending with fade
    "After the school semester, even though you have no strong connection with the people around you."
    "You realized that your Mother was always there in your worse and better times."
    $renpy.pause(1.0)
    "You rushed home and hugged your mother with all your feelings."
    $renpy.pause(1.0)
    main "Thank you foralways being there for me, Mom"
    main "I love you."
    $renpy.pause(1.0)
    mom "I love you too, [player_name]."
    mom "I will always love you whatever happens to you."
    scene black
    $renpy.pause(2.0)
    "You have unlocked the Neutral Ending"
    jump credits_scene
    return

label bad_ending_scene:
    scene black
    $renpy.pause(2.0)
    show bad ending with fade
    "After 4 months you have lost your will to socialize and have a connection to the people around you."
    $renpy.pause(1.0)
    "Even the relationship with your mom has crumbled"
    $renpy.pause(1.0)
    "You sit in an empty classroom... "
    $renpy.pause(1.0)
    "Wondering and regretting your past interactions with the people around you."
    scene black
    $renpy.pause(2.0)
    "You have unlocked the Bad Ending"
    jump credits_scene
    return

label secret_bad_ending_scene:
    scene black
    $renpy.pause(2.0)
    show bad ending with fade
    "After what Chihiro did to you, you've been spacing out."
    $renpy.pause(1.0)
    "The trauma that bought by that two faced psychotic girl was always lingering."
    $renpy.pause(1.0)
    "As you sit in an empty classroom... "
    $renpy.pause(1.0)
    "You decided to end it all and climbed on a chair with a wire on your hand."
    scene black
    $renpy.pause(2.0)
    "You have unlocked the Secret Bad Ending"
    jump credits_scene
    return

label credits_scene:
    scene black
    show text "{color=#ffffff}{size=+30}CREDITS{/size}{/color}" with dissolve

    $ renpy.pause(3.0)

    show text "{color=#ffffff}{size=+20}Created by\n Ujos Studio{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}Lead Project Manager \n Aronn Marc Duran{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}Art Director and Lead Graphic Designer \n Dana Rae Hernandez{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}Story Board Manager and Sound Designer \n Anne Trishia Aseoche{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}QA Manager and Lead Game Developer \n Jan Joshua Aus and Aronn Marc Duran{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}Credits to the owners of the music{/size}{/color}" with dissolve

    $ renpy.pause(4.0)

    show text "{color=#ffffff}{size=+20}Thank You For Playing the Alpha Version{/size}{/color}" with dissolve

    $ renpy.pause(4.0)


    return
