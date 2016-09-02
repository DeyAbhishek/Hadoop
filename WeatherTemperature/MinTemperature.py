from mrjob.job import MRJob

class MRMinTemperature(MRJob):
        
            def ConvertToFahrenheit(self, tenthsOfCelcius):
                celcius = float(tenthsOfCelcius) / 10.0
                fahrenheit = celcius * 1.8 + 32.0
                return fahrenheit
                
            def mapper(self, _, line):
                (location, date, type, data, x, y, z, w) = line.split(',')
                if (type == 'TMIN'):
                    temperature = self.ConvertToFahrenheit(data)
                    yield location, temperature
                    
            def reducer(self, location, temperatures):
                yield location, min(temperatures)
                
                
if __name__ == '__main__':
    MRMinTemperature.run()