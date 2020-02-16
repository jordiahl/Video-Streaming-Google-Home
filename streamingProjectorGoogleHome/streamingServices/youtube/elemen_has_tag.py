class element_has_tag(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self,tag_name):
    self.tag_name = tag_name

  def __call__(self, driver):
    element = driver.find_elements_by_tag_name(self.tag_name)  # Finding the referenced element
    if element != None:
        return element
    else:
        return False
