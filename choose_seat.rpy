screen seat:

        default tt = Tooltip("Select your seat")

        imagebutton:
            xpos -250
            ypos 80
            idle "characters/students/Ayani/Ayani_default.png"
            hover "characters/students/Ayani/Ayani_highlighted.png"
            focus_mask True
            hovered tt.Action("Sit with Ayani Isa")
            action Jump("seat_ayani")

        imagebutton:
            xpos -70
            ypos 80
            idle "characters/students/Chi/Chi_default.png"
            hover "characters/students/Chi/Chi_highlighted.png"
            focus_mask True
            hovered tt.Action("Sit with Chihiro Isii")
            action Jump("seat_chihiro")

        imagebutton:
            xpos 350
            ypos 80
            idle "characters/students/Lian/Lian_default.png"
            hover "characters/students/Lian/Lian_highlighted.png"
            focus_mask True
            hovered tt.Action("Sit beside Lian Hui")
            action Jump("seat_lian")

        imagebutton:
            xpos 820
            ypos 80
            idle "characters/students/Najma/Najma_default.png"
            hover "characters/students/Najma/Najma_highlighted.png"
            focus_mask True
            hovered tt.Action("Sit with Najma Awad")
            action Jump("seat_najma")

        frame:
            xalign 0.1
            yalign 0.9
            xpadding 100
            ypadding 50

            hbox:
                spacing 40


                vbox:
                    spacing 10
                    text tt.value
