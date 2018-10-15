from anvil import *
import anvil.server

class searchResultTemplate(searchResultTemplateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    self.column_panel_2.visible = False
    # Any code you write here will run when the form opens.

  def show_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    current_state = self.column_panel_2.visible
    self.column_panel_2.visible = not current_state

