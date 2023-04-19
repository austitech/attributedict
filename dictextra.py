

class AttributeDict(dict):
    def __getattr__(self, key):
        item = self.get(key)
        
        if isinstance(item, dict):
            item = self.handle_dict_value(item)
            return item
        
        elif isinstance(item, list) or isinstance(item, tuple):
            item = self.handle_iterable_value(item)
            return item

        else:
            return item

    def handle_dict_value(self, value):
        if not isinstance(value, dict):
            return value
        else:
            return AttributeDict(value)
        
    def handle_iterable_value(self, iterable):
        new_iterable = [
            self.handle_dict_value(item) for item in iterable
        ]
        return new_iterable
