class Dict:
    def __init__(self):
        pass
res = Dict()
print(dir(res.__dict__))
print(dir(Dict.__dict__))