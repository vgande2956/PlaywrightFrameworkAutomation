class Homepage:
    def __init__(self, page):
        self.page = page
        self.products_label = page.get_by_text("Products")
    
    def validate_homepage(self):
        assert self.products_label.is_visible()
        
    