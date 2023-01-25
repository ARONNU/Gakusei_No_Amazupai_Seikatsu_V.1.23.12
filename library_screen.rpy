screen al_screen_library():
    imagemap:
        ground "minigame/AL/Childhood_Bookshelf_AyaniLian.png"
        hotspot(297, 616, 427, 321) action Jump("al_pic_click")
        hotspot(741, 576, 210, 240) action Jump("al_engraving_click")
        hotspot(1430, 616, 333, 337) action Jump("al_book_click")

    imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -20
            yoffset -10
            idle "UI/button_return.png"
            action Jump ("allibrary_choice")

screen nc_screen_library():
    imagemap:
        ground "minigame/NC/Childhood_bookshelf_NamjaChi.png"
        hotspot(1205, 5, 435, 327) action Jump("nc_pic_click")
        hotspot(226, 399, 280, 187) action Jump("nc_engraving_click")
        hotspot(622, 378, 240, 411) action Jump("nc_book_click")
        hotspot(1470, 830, 195, 248) action Jump("nc_poster_click")

    imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -20
            yoffset -10
            idle "UI/button_return.png"
            action Jump ("nclibrary_choice")
