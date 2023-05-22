from dyndesign import mergeclasses
import re

class CollatzClassBuilder:
    COMPONENT_DIR = 'components'

    def __init__(self, args):
        self.args = args

    @staticmethod
    def camel_to_snake(value):
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', value).lower()

    def build_class(self):
        classes_to_merge = ['CollatzSequence', 'CollatzOutput']
        for opt_class, value in self.args.__dict__.items():
            if opt_class != 'n' and value:
                classes_to_merge.append(opt_class)
        paths_to_merge = (
            f"{self.COMPONENT_DIR}.{self.camel_to_snake(c)}.{c}"
            for c in classes_to_merge
        )
        return mergeclasses(*paths_to_merge, invoke_all=['output_number', 'output_wrapper'])
