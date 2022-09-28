
## EP01 - POKEMONS

Como rodar o projeto

### Passo  1 - Fazer a extração dos pokemons 
```cmd
cd scrapy

scrapy runspider PokemonSpider.py -O pokemons.json
```

### Passo  2 - Criar a versão final do CSV com pandas 
```cmd
cd panda

python Converter.py
```

### Passo  3 - Criar as métricas de média de dano dos pokemons e pegar os tipos de pokemons
```cmd
cd mappers

python MapperType.py pokemons.csv > types

python MapperAverage.py pokemons.csv > average
```