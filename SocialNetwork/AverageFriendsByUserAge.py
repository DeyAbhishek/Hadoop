from mrjob.job import MRJob

class MRAverageFriendsByUserAge(MRJob):

    def mapper(self, _, line):
        (id, name, age, numFriends) = line.split(',')
        yield age, float(numFriends)
        
    def reducer(self, age, friends):
        total = 0
        num = 0
        for fr in friends:
            total += fr
            num += 1
        yield age, total / num
        
if __name__ == '__main__':
    MRAverageFriendsByUserAge.run()