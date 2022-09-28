from mrjob.job import MRJob
from mrjob.step import MRStep


class MapperAverage(MRJob):
    isCSVHeader = True
    sizePokemons = 151

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        if MapperAverage.isCSVHeader:
            MapperAverage.isCSVHeader = False
        else:
            damages = line.split('\"')[1].replace('\"', '').replace('[', '').replace(']', '').split(',')
            for damage in damages:
                damageSplit = damage.replace('\'', '').split(':')
                yield damageSplit[0], float(damageSplit[1])

    def reducer(self, chave, valores):
        yield chave, sum(valores) / MapperAverage.sizePokemons


if __name__ == '__main__': MapperAverage.run()

