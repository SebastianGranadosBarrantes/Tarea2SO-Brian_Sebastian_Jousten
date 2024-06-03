class Page:
    def __init__(self, initial_position, final_position, page_number):
        self.initial_position = initial_position
        self.final_position = final_position
        self.page_number = page_number
        self.process_id = ''
        self.execution_page_number = ''  # execution page number
        self.process_name = ''
        self.use = False # False if the page is empty True if a process have it

    def clean_page(self):
        self.use = False
        self.process_id = ''
        self.process_name = ''
        self.execution_page_number = ''

    def __str__(self):
        return f'Page number {self.page_number}, Page initial position {self.initial_position}, Page final position {self.final_position}, Page in use {self.use}, process id {self.process_id}, process name {self.process_name}'