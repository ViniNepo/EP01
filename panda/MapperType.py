from mrjob.job import MRJob
from mrjob.step import MRStep


class MapperType(MRJob):
    isCSVHeader = True

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        if MapperType.isCSVHeader:
            MapperType.isCSVHeader = False
        else:
            for l in line.split(']')[1].split('[')[1].split(','):
                yield l.strip().replace('\'',''), 1

    def reducer(self, chave, valores):
        yield chave, sum(valores)


if __name__ == '__main__': MapperType.run()

