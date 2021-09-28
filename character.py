class Character:
    """the graphic interface of the progress of the game"""

    head_lvl:str
    body_lvl:str
    foot_lvl:str
    
    ui:str

    def __init__(self) -> None:
        self.reset_state()
    
    def reset_state(self) -> None:
        """clean the interface"""
        self.head_lvl = ""
        self.body_lvl = ""
        self.foot_lvl = ""

    def define_state(self, state:int):
        """to change the way the graphic is showed up"""
        if state > 4:
            self.head_lvl = "°"
            self.body_lvl = ""
            self.foot_lvl = ""
        elif state > 3:
            self.head_lvl = "°"
            self.body_lvl = "|"
            self.foot_lvl = ""
        elif state > 2:
            self.head_lvl = "°"
            self.body_lvl = "-|"
            self.foot_lvl = ""
        elif state > 1:
            self.head_lvl = "°"
            self.body_lvl = "-|-"
            self.foot_lvl = ""
        elif state > 0:
            self.head_lvl = "°"
            self.body_lvl = "-|-"
            self.foot_lvl = "-|"
        else:
            self.head_lvl = "°"
            self.body_lvl = "-|-"
            self.foot_lvl = "_|_"

    def show_ui(self) -> None:
        """prints in console the current state of the interface"""

        self.ui = f"""
        ------
        |    {self.head_lvl}
        |   {self.body_lvl}
        |   {self.foot_lvl}
        """
        print(self.ui)
