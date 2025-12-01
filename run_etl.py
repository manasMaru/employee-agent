from src.employee_transformation import Extractor, Transformer, Loader

e=Extractor()
raw_data=e.extract()

t=Transformer()
transformed=t.transform(raw_data)

l=Loader()
l.load(transformed)