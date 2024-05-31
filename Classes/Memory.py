from .Pages import Page


class Memory:
    def __init__(self, size_memory, amount_pages, pages_size):
        self.size_memory = size_memory
        self.pages_size = pages_size
        self.amount_pages = amount_pages
        self.memory = []
        self.available_pages = []
        self.used_pages = []
        self.unused_pages_id = []
        self.define_memory()


    def define_memory(self):
        pages_initial_position = 0
        for page in range(self.amount_pages):
            new_page = Page(pages_initial_position, (pages_initial_position + self.pages_size) - 1, page)
            self.memory.append(new_page)
            self.available_pages.append(new_page)
            pages_initial_position += self.pages_size
            self.unused_pages_id.append(page + 1)


    def add_process_to_memory(self, process_id, process_name):
        page = self.available_pages.pop(0) # The list of available pages most be ordered
        page.process_id = process_id
        page.process_name = process_name
        page.use = True
        page.execution_page_number = self.unused_pages_id.pop(-1)
        self.unused_pages_id.sort()
        self.used_pages.append(page)

    def delete_process_in_memory(self, process_id, page_number):
        page_to_clean = None
        for page in self.used_pages:
            if page.process_id == process_id and page.page_number == page_number:
                self.unused_pages_id.append(page.execution_page_number)
                self.unused_pages_id.sort()
                page_to_clean = page

        if page_to_clean:
            self.used_pages.remove(page_to_clean)
            page_to_clean.clean_page()
            self.available_pages.append(page_to_clean)
        else:
            print('Error, page not found')
