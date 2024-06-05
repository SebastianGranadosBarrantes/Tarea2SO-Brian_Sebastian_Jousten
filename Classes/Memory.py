from .Pages import Page


class Memory:
    def __init__(self, size_memory, amount_pages, pages_size, memory_id):
        self.size_memory = size_memory
        self.pages_size = pages_size
        self.amount_pages = amount_pages
        self.all_pages = []
        self.memory = []
        self.available_pages = []
        self.used_pages = []
        self.unused_pages_id = []
        self.memory_id = memory_id
        self.define_memory()


    def define_memory(self):
        """
        Define memory for memory pages.
        :return:
        """
        pages_initial_position = 0
        for page in range(self.amount_pages):
            new_page = Page(pages_initial_position, (pages_initial_position + self.pages_size) - 1, page, self.memory_id)
            self.memory.append(new_page)
            self.available_pages.append(new_page)
            self.all_pages.append(new_page)
            pages_initial_position += self.pages_size
            self.unused_pages_id.append(page + 1)

    def add_process_to_memory(self, process_id, process_name, process_type):
        """
        Add process to memory.
        :param process_id:
        :param process_name:
        :return:
        """
        if len(self.available_pages) >= 1:
            page = self.available_pages.pop(0) # The list of available pages most be ordered
            # self.available_pages.sort()
            page.process_id = process_id
            page.process_type = process_type
            page.process_name = process_name
            page.use = True
            page.execution_page_number = self.unused_pages_id.pop(0)
            self.unused_pages_id.sort()
            self.used_pages.append(page)
            return page
        else:
            return False

    def delete_process_in_memory(self, process_id):

        pages_to_remove = []
        print(f'el id del proceso es {process_id}')
        for page in self.used_pages:
            print(f'el id del page es {page.process_id}')
            if page.process_id == process_id:
                self.unused_pages_id.append(page.execution_page_number)
                self.unused_pages_id.sort()
                self.available_pages.append(page)
                pages_to_remove.append(page)
                page.clean_page()

        for page in pages_to_remove:
            self.used_pages.remove(page)

    def clean_page_per_number(self, page_number):
        page_to_clean = None
        for page in self.used_pages:
            if page.page_number == page_number:
                page_to_clean = page
                break

        if page_to_clean is not None:
            self.unused_pages_id.append(page_to_clean.execution_page_number)
            self.unused_pages_id.sort()
            self.available_pages.append(page_to_clean)
            page_to_clean.clean_page()
            self.used_pages.remove(page_to_clean)

    def get_first_page_process(self, process_id):
        for page in self.used_pages:
            if page.process_id == process_id:
                return page
        return None
    def get_page_for_swap(self):
        pages_process_count = {}
        for page in self.all_pages:
            process_id = page.process_id
            if process_id == '':
                return page
            elif process_id in pages_process_count:
                pages_process_count[process_id] += 1

            else:
                pages_process_count[process_id] = 1

        for process, amount in pages_process_count.items():
            page = self.get_first_page_process(process)
            if amount == 1:
                continue

            elif amount > 1:
                return self.get_first_page_process(process)

        return -1
