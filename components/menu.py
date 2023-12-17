from simple_term_menu import TerminalMenu
from components.logging.logging import logger
from components.request import request

def start():
    main_menu = TerminalMenu(
        menu_entries=["Create Request", "Delete Request", "Send Request", "Quit"],
        title="  netrequester\n",
        menu_cursor = "| ",
        menu_cursor_style = ("fg_blue", "bold"),
        menu_highlight_style = ("bg_yellow", "fg_black"),
        
    )

    main_menu.show()