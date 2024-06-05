class Page:
    def __init__(self, initial_position, final_position, page_number, memory_id):
        self.initial_position = initial_position
        self.final_position = final_position
        self.page_number = page_number  # actua como el id
        self.process_type = None
        self.process_id = ''
        self.execution_page_number = ''  # execution page number
        self.process_name = ''
        self.use = False # False if the page is empty True if a process have it
        self.memory_id = memory_id

    def clean_page(self):
        self.use = False
        self.process_id = ''
        self.process_name = ''
        self.execution_page_number = ''

    def set_process(self, process_id, process_name, execution_page_number, memory_id):
        self.process_id = process_id
        self.process_name = process_name
        self.execution_page_number = execution_page_number
        self.memory_id = memory_id

    def swap_page(self, memory_id, execution_page_number, process_name, process_id):
        self.process_id = process_id
        self.process_name = process_name
        self.execution_page_number = execution_page_number
        self.memory_id = memory_id

    def __str__(self):
        return f'Page number {self.page_number}, Page initial position {self.initial_position}, Page final position {self.final_position}, Page in use {self.use}, process id {self.process_id}, process name {self.process_name}'