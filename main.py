from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import (
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge,
)
from kivy.uix.floatlayout import FloatLayout

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    FloatLayout:
        size_hint_y: None
        height: "48dp"
        pos_hint: {"bottom": 1}

        MDTabsPrimary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}

            MDDivider:
'''


class Example(MDApp):
    def on_start(self):
        super().on_start()
        for tab_icon, tab_name in {
            "list-box-outline": "List",
            "camera": "Camera",
            "help": "Help",
        }.items():
            if tab_icon == "list-box-outline":
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            MDTabsBadge(
                                text="99",
                            ),
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            else:
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            self.root.ids.tabs.switch_tab(icon="airplane")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()
