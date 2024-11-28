costs = { 'socks':5, 'shoes':60, 'sweater':30}

def get_total(costs: dict, item_list: list, tax: float) -> float:
  if type(costs) != dict:
    return 'First param should be a dictionary'
  if type(item_list) != list:
    return 'Second param should be a list'
  if type(tax) != float:
    return 'Third param should be a float'
  
  subtotal = 0
  for item in item_list:
    if not item in costs:
      continue
    else:
      subtotal+= costs[item]
  
  total = round((subtotal * (1 + tax)), 2)
  print(total)
  return total
