screen select_chapter():

    textbutton _("Chapter 1") xpos 24 ypos 24 action Start("ch_01")
    textbutton _("Chapter 2") xpos 336 ypos 24 action Start("ch_02")
    textbutton _("Chapter 3") xpos 648 ypos 24 action Start("ch_03")
    textbutton _("Chapter 4") xpos 960 ypos 24 action Start("ch_04")

    textbutton _("Back") xpos 12 ypos 639 action Show("main_menu", transition=dissolve)
