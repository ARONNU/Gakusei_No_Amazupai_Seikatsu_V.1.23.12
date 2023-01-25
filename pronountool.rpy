################################################################################
## Pronoun Tool
################################################################################

# Hello! This is Pronoun Tool, a simple tool to select and display pronouns in your Ren'Py game, made by npckc (https://npckc.site)!

# Lines that begin with TODO: are sections where you may be required to do something with the code, so you can Ctrl+F TODO: to make sure you haven't missed anything.

# TODO: Please copy this file (pronountool.rpy) to the game folder of your Ren'Py game.

# Once you've done that, follow the instructions in this file and you should be OK! It's a bit long, but I hope you'll keep with me until the end.

# You can put this project into your Ren'Py projects directory and launch it to see the tool in action.

# If you use this tool, I would appreciate it if you can credit npckc (https://npckc.site or https://npckc.itch.io) or the tool in some way, but it isn't required.

################################################################################
## Table of Contents
################################################################################

# P1: Pronoun Initialisation
# P2: Displaying Different Text Depending on Chosen Pronouns
# P3: Pronouns as Variables
# P4: Pronoun Text Tags
# P5: Pronoun Options Menu
# P6: Pronoun Selection Menu
# P7: Display Pronouns
# P8: Notes
# P9: Licence

################################################################################
## P1: Pronoun Initialisation
################################################################################

# This defines the pronouns that can be used by the main character. For this example, we will be using the English pronouns he/him, she/her and they/them, but you can use others in your game and more than three if you wish.

# The numbers in the # comment next to each pronoun show the position of the pronoun in the list and are only for reference.

# Note: the __ at the beginning of each line is to make the pronouns translatable.

default pronounlist = [
    __("he/him"), # 0
    __("she/her"), # 1
    __("they/them"), # 2
    # __("PRONOUN GOES HERE"), # 3
]

# TODO: If you would like to add more pronouns, replace the above "PRONOUN GOES HERE" with the pronouns you want to use and remove the # at the beginning of the line. You can add as many pronouns as necessary.

# The next code sets the default pronouns for the main character. For this example, the default is set to "2", making "they/them" the default pronouns.

# TODO: Change the pronoun variable to a different number for different default pronouns.

default pronoun = 2
default selectedpronouns = pronounlist[pronoun]

# Here is an example of how to show the pronouns in your game.

label examplepronouns:

    "Show the currently selected pronoun with this code: [selectedpronouns!t]"

    "Show a pronoun in the list with this code: [pronounlist[0]!t]"

    "Change the number in the variable to change the pronoun displayed. Here is an example showing #1 in the pronoun list: [pronounlist[1]!t]"

# Note: the !t at the end of the variable is to make the pronoun display properly in translations. If your game will not be available in more than one language, you can choose to not include the !t, e.g., [selectedpronouns].

################################################################################
## P2: Displaying Different Text Depending on Chosen Pronouns
################################################################################

# There are two ways to display different text depending on the pronouns that are chosen, and each have their pros and cons.

# 1. Using variables for the pronouns (detailed in P3: Pronouns as Variables)
# - Easier to type
# - Works with self-voicing in Ren'Py versions below 7.4
# - Complicated for translations

# Note: The default tool only has variables set up for English. You will need to change the pronouns to fit if you are using a different language.

# 2. Using custom text tags (detailed in P4: Pronoun Text Tags)
# - Harder to type
# - Does not work with self-voicing in Ren'Py versions below 7.4
# - Works better for translations

# Use whichever works best for you!

################################################################################
## P3: Pronouns as Variables
################################################################################

# This following are pronouns as variables, defined in lists with variations of pronouns to make it easier for you to type dialogue, like so.

# TODO: If you have changed/added pronouns, they need to be changed/added here as well.

default theylist = [
    __("he"), #0
    __("she"), #1
    __("they"), #2
    # __("PRONOUN GOES HERE"), #3
]

default themlist = [
    __("him"), #0
    __("her"), #1
    __("them"), #2
    # __("PRONOUN GOES HERE"), #3

]

default theirlist = [
    __("his"), #0
    __("her"), #1
    __("their"), #2
    # __("PRONOUN GOES HERE"), #3
]

default theirslist = [
    __("his"), #0
    __("hers"), #1
    __("theirs"), #2
    # __("PRONOUN GOES HERE"), #3

]

default theyrelist = [
    __("he's"), #0
    __("she's"), #1
    __("they're"), #2
    # __("PRONOUN GOES HERE"), #3

]

# TODO: The following are lists with common English verb conjugations, but as there are many irregular verbs in English, you can add more as necessary to fit your game.

# For verbs that conjugate with -s like "walk", e.g., he/she walks, they walk.
default slist = [
    __("s"), #0
    __("s"), #1
    __(""), #2
    # __("VERB CONJUGATION GOES HERE"), #3
]

# For verbs that conjugate with -es like "go", e.g., he/she goes, they go.
default eslist = [
    __("es"), #0
    __("es"), #1
    __(""), #2
    # __("VERB CONJUGATION GOES HERE"), #3
]

# For the verb "to be", e.g., he/she is, they are.
default arelist = [
    __("is"), #0
    __("is"), #1
    __("are"), #2
    # __("VERB CONJUGATION GOES HERE"), #3
]

# This sets the default pronouns for each variable.

default they = theylist[pronoun]
default them = themlist[pronoun]
default their = theirlist[pronoun]
default theirs = theirslist[pronoun]
default theyre = theyrelist[pronoun]
default s = slist[pronoun] # TODO: If you want to use "s" for a character or a variable elsewhere, you will have to change the "s" here to something else (e.g., default ss = slist[pronoun]). You would also need to change it in pronounselection.

default es = eslist[pronoun]
default are = arelist[pronoun]

# TODO: If you added more lists, you would need to add defaults for them here as well.

# You would then be able to type dialogue like the following.

label examplevariablepronouns:
    # With variables
    "[they!t!c] went to the supermarket with [their!t] friend." # The !c at the end of the first variable is to capitalise the first letter of the variable.

    # How the text should be displayed for each set of pronouns
    "He went to the supermarket with his friend." # he/him
    "She went to the supermarket with her friend." # she/her
    "They went to the supermarket with their friend." # they/them

    # With variables
    "[they!t!c] go[es] and eat[s] the apple."

    # How the text should be displayed for each set of pronouns
    "He goes and eats the apple." # he/him
    "She goes and eats the apple." # she/her
    "They go and eat the apple." # they/them

    # With variables
    "I think [they!t] [are!t] saying that the book is [theirs!t]."

    # How the text should be displayed for each set of pronouns
    "I think he is saying that the book is his." # he/him
    "I think she is saying that the book is hers." # she/her
    "I think they are saying that the book is theirs." # they/them

# Another benefit to this is that since there is only one variable being displayed, self-voicing will function normally as well.

# However, using specific pronoun variables can make it harder to do translations (as pronouns and other gender-related grammar rules are not used the same way in every language).

# For example, for the first sentence above, the only variables needed would be [they!t!c] and [their!t] in English, but if you were to translate it to French, it would need to be something like this:

# Past participle for French
default pplist = [
    __(""),
    __("e"),
    __(".e"),
]

default pp = pplist[pronoun]

label examplevariablepronounsfrench:
    # With variables
    "[they!t!c] est allé[pp!t] au supermarché avec son ami."

    # How the text should be displayed for each set of pronouns
    "Il est allé au supermarché avec son ami." # For il/lui (he/him).
    "Elle est allée au supermarché avec son ami." # For elle (she/her), with "e" after the past participle.
    "Iel est allé.e au supermarché avec son ami." # For iel (they/them), with ".e" after the past participle.

# The first variable would be fine, replaced either with il, elle or lui, but for the next variable, you would need to create a new variable that would add the appropriate text for each set of pronouns after past participles. On the other hand, the second variable used in the English version is irrelevant, as in French, possessive nouns must agree with the gender of the noun they are referring to rather than the gender of the possessor.

# Please keep this in mind if you may be translating the game in the future. It would probably be best to use these alongside the text tags, which are explained below.

################################################################################
## P4: Pronoun Text Tags
################################################################################

# The following are text tags to be used in dialogue for each different pronoun. There are only three text tags in this tool by default, but you can add more if necessary.

# You can look at script.rpy for an example.

# Note: Self-voicing will read all text in text tags regardless of the selected pronoun if you on a version of Ren'Py lower than 7.4. The only way to avoid this issue is to use variables as discussed in the section Pronouns as Variables.

init python:

    # This tag corresponds with #0 in the list, which is "he/him" in this example.
    def tag_0(tag, argument, contents):
        if pronoun == 0:
            return contents

        return []

    # This tag corresponds with #1 in the list, which is "she/her" in this example.
    def tag_1(tag, argument, contents):
        if pronoun == 1:
            return contents

        return []

    # This tag corresponds with #2 in the list, which is "they/them" in this example.
    def tag_2(tag, argument, contents):
        if pronoun == 2:
            return contents

        return []

    # def tag_3(tag, argument, contents): # Change 3 to the correct number if you have more pronouns
    #     if pronoun == 3: # Change 3 to the correct number if you have more pronouns
    #         return contents

    #     return []

    # TODO: Make sure to add one tag for each new pronoun option you included. For example, if you added one set of pronouns, you would remove the #s from the above tag_3.

    # The following are the text tags that you would actually use in the dialogue. In this example, they correspond to the following:

    # {0}he/him{/0}
    # {1}she/her{/1}
    # {2}they/them{/2}

    config.custom_text_tags['0'] = tag_0
    config.custom_text_tags['1'] = tag_1
    config.custom_text_tags['2'] = tag_2
    # config.custom_text_tags['3'] = tag_3

    # TODO: Make sure to add one new config.custom_text_tag for each new pronoun option you included. For example, if you added one set of pronouns, you would remove the # from the above config.custom_text_tags['3'].

# TODO: Next, we add these tags to the history screen to make sure that they are displayed properly. In your screens.rpy file (or wherever your history screen is), change the following code (with version differences):

# define gui.history_allow_tags = set() (versions before Ren'Py 7.4)

# OR

# define gui.history_allow_tags = { "alt", "noalt" } (Ren'Py versions 7.4 and above)

# to this code (remove the #):

# define gui.history_allow_tags = { "alt", "noalt", "0", "1", "2", } # TODO: If you have added custom text tags, add them here too.

# Note: The "alt" and "noalt" are for Ren'Py 7.4 version compatibility.

# You can look at screens.rpy for an example.

# This is a guide showing how to use the tags.

label exampletexttags:

    "{0}Text in this tag will only show up when pronoun #0 (he/him in the example) is selected.{/0}"
    "{1}Text in this tag will only show up when pronoun #1 (she/her in the example) is selected.{/1}"
    "{2}Text in this tag will only show up when pronoun #2 (they/them in the example) is selected.{/2}"

    "You can use multiple tags in the same text, like so: {0}He{/0}{1}She{/1}{2}They{/2} walk{0}s{/0}{1}s{/1} to the park with {0}his{/0}{1}her{/1}{2}their{/2} dog."

    # Note: If text tags are currently displayed in dialogue when the pronouns are changed, they will not be updated immediately as the dialogue is already on screen, but the text tags for the selected pronoun will be displayed properly for the next dialogue.

################################################################################
## P5: Pronoun Options Menu
################################################################################

# This can be used if you want a menu ONLY for pronoun options. You can also copy and paste the buttons into the default Ren'Py preferences screen.

screen pronounoptions():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            style_prefix "check"
            label _("Pronoun Options")
            if not main_menu:
                textbutton _("Select Pronouns") action Call("pronounselection") # This shows the pronoun selection menu if the game is currently being played.
            textbutton _("Display Pronouns") action ToggleVariable("persistent.displaypronouns") # Remove this button if you do not want the game to display pronouns in-game.

            textbutton ("") # Adds space between pronoun options and return button.

            textbutton _("Return") action ShowMenu("preferences") # Returns user to the Preferences menu. Remove if unnecessary.

# TODO: If you use the above screen, please add the following textbutton to a screen somewhere, like the Preferences screen in your screens.rpy file.

# textbutton _("Pronouns") action ShowMenu("pronouns")

# Remove the # when pasting in the preferences screen.

# You can look at screens.rpy for an example.

################################################################################
## P6: Pronoun Selection Menu
################################################################################

# This tool uses a choice menu to allow the player to select pronouns. If you want to customise the choice menu for this screen, please refer to Ren'Py's documentation: https://www.renpy.org/doc/html/screen_special.html#choice

# TODO: Call the choice menu from in-game by using the following code.

# call pronounselection

# You can look at script.rpy for an example.

# Below is the pronoun selection menu label.

label pronounselection:

    menu:
        "Please select your pronouns."
        "[pronounlist[0]!t]":
            $ pronoun = 0
        "[pronounlist[1]!t]":
            $ pronoun = 1
        "[pronounlist[2]!t]":
            $ pronoun = 2
        # "[pronounlist[3]!t]":
        #     $ pronoun = 3

        # TODO: Make sure to add any extra pronouns you included. For example, if you added one pronoun, you would remove the #s at the beginning of the commented-out option to add in your pronoun.

    $ selectedpronouns = pronounlist[pronoun]

    # This calls the label for updating self-voicing text tags.

    call tts_tag_update from _call_tts_tag_update

    # TODO: The following are used in this guide to set the pronoun variables to match the selected pronouns (as explained below). These would need to be changed if you need more/different variables (e.g., for translations).

    $ they = theylist[pronoun]
    $ them = themlist[pronoun]
    $ their = theirlist[pronoun]
    $ theyre = theyrelist[pronoun]
    $ theirs = theirslist[pronoun]
    $ s = slist[pronoun] # TODO: If you want to use "s" for a character or a variable elsewhere, you will have to change the "s" here to something else (e.g., default ss = slist[pronoun]). You would also need to change it in pronounselection.
    $ es = eslist[pronoun]
    $ are = arelist[pronoun]

    return

# This is the label specifically for updating the self-voicing text tags on Ren'Py 7.4 or higher. This will only execute on Ren'Py 7.4 or higher.

label tts_tag_update:

    # This checks the Ren'Py version and will only execute the below code on REn'Py 7.4 or higher.

    if renpy.version_tuple[0] < 7:
        return
    else:
        if renpy.version_tuple[0] == 7 and renpy.version_tuple[1] < 4:
            return

    # This resets the custom text tags that are self-voiced.

    $ config.tts_filter_tags = [ "noalt", "rt", "art", "0", "1", "2", ] # TODO: If you have added custom text tags, add them here too.

    # This makes it so that the selected pronoun's text tag will be self-voiced.

    $ pronountexttag = str(pronoun)

    if pronountexttag in config.tts_filter_tags:
        $ config.tts_filter_tags.remove(pronountexttag)

    return

# This label ensures that even after loading, the self-voicing text tags work.

# TODO: This uses Ren'Py's after_load label for executing code after loading. If you are using this label elsewhere, please just include the code from here in your after_load label, and comment out this label.

label after_load:

    call tts_tag_update from _call_tts_tag_update_1

    return

################################################################################
## P7: Display Pronouns
################################################################################

# The following code makes it possible to display pronouns next to characters' names in-game.

# This code sets pronouns to be displayed by default.

# TODO: If you would like to be hidden by default, change True to False.

default persistent.displaypronouns = True

# TODO: Next, define the pronouns for each of your characters. This is done by adding the "show_pronouns=###" argument to a Character/DynamicCharacter, with ### replaced by the pronouns you want to ues.

# Example: The narrator of this tool. Their pronouns are they/them, so for show_pronouns we use pronounlist[2].
define p = Character(_("Pronoun Parrot"), image="pronounparrot", show_pronouns="[pronounlist[2]!t]")

# Example: To show the main character with their selected pronouns, use the selectedpronouns variable.

# TODO: Change MCEXAMPLE and MAIN CHARACTER NAME HERE to fit your main character. Alternatively, use a DynamicCharacter instead if your game allows the player to input their own name. You can see an example of a DynamicCharacter in script.rpy.

define MCEXAMPLE = Character(_("MAIN CHARACTER NAME HERE"), show_pronouns="[selectedpronouns!t]")

# You can also set characters with changing pronouns in the same way. Here is a variable to set a genderflux character's pronouns to she/her first.

default gfpronouns = pronounlist[1]

# Then, the variable is set to the show_pronouns argument for the genderflux character.

define gfc = Character(_("Genderflux Character"), show_pronouns="[gfpronouns!t]")

# If you change the gfpronouns variable in-game, the pronouns displayed for the genderflux character will also change. Below is an example code setting the genderflux character's pronouns to they/them.

# $ gfpronouns = pronounlist[2]

# Note: If you do not list pronouns for a character, pronouns will not be displayed for that character.

# TODO: On the say screen in screens.rpy, you need to add the "** kwargs" to the screen to make it work, like so:

# screen say(who, what, **kwargs): # **kwargs comes after what

# TODO: Then, you need to add the code to actually show the pronouns on the say screen. Position it as you like.

# if persistent.displaypronouns:
#     text kwargs.get("pronouns", "")

# You can see an example of the say screen in screens.rpy.

################################################################################
## P8: Notes
################################################################################

# That's the end of the explanations! This tool should give you the basics to add a pronoun selection and display system to your Ren'Py game. It should be fairly easy to change the code to add anything specific you want for your game as well.

# While I used English for the example, this should work for any language you need it to with some tweaking. You can take a look at one of my previous games, Tomato CLinic (https://npckc.itch.io/tomato-clinic), for an example of this code actually used in a full game with multiple languages, though it's an earlier version made in Ren'Py 7.3.5 without pronoun display/full self-voicing support.

# I have tried to include as many options as possible while also keeping the tool simple and making sure it works with translations. It took me a while to figure out how to get pronouns to work in my own game, so I hope this tool will be able to help people implement pronouns more easily!

################################################################################
## P9: Licence
################################################################################

# Copyright 2020 npckc

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
