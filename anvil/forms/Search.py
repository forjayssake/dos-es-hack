from anvil import *
import anvil.server

class Search(SearchTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

    
  def search_button_click(self, **event_args):
    search_term = self.search_box.text
    response = anvil.server.call('service_search', search_term, 'false')
    self.lbl_results.text = 'Found ' + str(response['hits']['total']) + ' services in ' + str(response['took']) + ' milliseconds.'
    self.results_panel.items = response['hits']['hits']

  def search_box_pressed_enter(self, **event_args):
    self.search_button_click()