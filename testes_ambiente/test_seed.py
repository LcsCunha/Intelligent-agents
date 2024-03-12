import random

def test_seed_return():
    seed = []
    for i in range(10):
      seed.append(" ")
    
    seed.append("lixo")

    assert seed == [" ", " ", " ",  " ",  " ",  
                    " ",  " ",  " ",  " ",  " ", "lixo"]
    
def test_coin_flip_seed():
  seed = 100

  for i in range(1000):
    seed = random.randint(0, 1)
    if seed == 1:
       break
  
  assert seed == 1

