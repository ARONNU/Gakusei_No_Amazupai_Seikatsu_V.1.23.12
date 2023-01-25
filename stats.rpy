screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/button_stats.png"
        action ShowMenu("stats")

screen stats:

    frame:
        background "UI/stats_bg.png"
        xalign 0.4
        yalign 0.1
        xpadding 50
        ypadding 50

        hbox:
            spacing 40
            xpos 120

            vbox:
                spacing 10
                ypos 165
                text "Grades" size 40
                text "Reputation" size 40
                text "Relationship with mom" size 40
                text "Relationship with Lian" size 40
                text "Relationship with Najma" size 40
                text "Relationship with Ayani" size 40
                text "Relationship with Chihiro" size 40

            vbox:
                spacing 10
                ypos 165
                text "[grades]" size 40
                text "[reputation]" size 40
                text "[relationship_with_mom]" size 40
                text "[relationship_with_lian]" size 40
                text "[relationship_with_najma]" size 40
                text "[relationship_with_ayani]" size 40
                text "[relationship_with_chihiro]" size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/button_return.png"
        action Return()
