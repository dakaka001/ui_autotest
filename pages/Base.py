

class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def by_id(self, element):
        try:
            return self.driver.find_element_by_id(element)
        except Exception as e:
            print(e)

    def by_id_elements(self, element):
        try:
            return self.driver.find_elements_by_id(element)
        except Exception as e:
            print(e)

    def by_css_selector(self, element):
        try:
            return self.driver.find_element_by_css_selector(element)
        except Exception as e:
            print(e)

    def by_class_name(self, element):
        try:
            return self.driver.find_element_by_class_name(element)
        except Exception as e:
            print(e)

    def by_xpath(self, element):
        try:
            return self.driver.find_element_by_xpath(element)
        except Exception as e:
            print(e)

    def by_name(self, element):
        try:
            return self.driver.find_element_by_name(element)
        except Exception as e:
            print(e)


