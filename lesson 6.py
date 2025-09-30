def get(name: str,  age: str = '2000') ->str:
    return f'name: {name} age: {2000}'


data = func_name('azamat', '25')
print(data)
print(help(func_name))