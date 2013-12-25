class AbstractView:
    def get_content_type(self):
        return "application/octet-stream"

    def get_content_encoding(self):
        return None
