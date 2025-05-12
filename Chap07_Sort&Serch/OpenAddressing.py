M = 13 # 해쉬테이블 크기

class HashTable:
    # 생성자
    def __init__(self):
        self.table = [0] * M

    # 키 값에 대한 해쉬테이블에 대한 위치
    def hashFn(self, key):
        return key % M # ex) 45는 idx 6에 위치
    
    # 위에 hashFn과 같이 이용용
    def hashFn2(self, key):
        return 11 - (key % 11) # M보다 작은 소수 중 제일 큰 소수
    
    def insert(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M # 선형 조사법 
            # bucket = (hashVal + i**2) % M # 이차 조사법 
            bucket = (hashVal + i * self.hashFn2(hashVal)) % M # 이중 해싱법

            if self.table[bucket] == 0:
                self.table[bucket] = key
                break
    
    def search(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M # 선형 조사법 
            # bucket = (hashVal + i**2) % M # 이차 조사법 
            bucket = (hashVal + i * self.hashFn2(hashVal)) % M # 이중 해싱법


            if self.table[bucket] == 0:
                return -1 # 비어있게 되는 경우
            elif self.table[bucket] == key: # 해당되는 위치에 있는 경우
                return bucket
            
    def delete(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M # 선형 조사법 
            # bucket = (hashVal + i**2) % M # 이차 조사법 
            bucket = (hashVal + i * self.hashFn2(hashVal)) % M # 이중 해싱법


            if self.table[bucket] == 0:
                print("No key to delete.")
                return
            elif self.table[bucket] == key: # 해당되는 위치에 있는 경우
                print("Deleted [%d] at bucket[%d]." %(key, bucket))
                self.table[bucket] = -1
                return bucket

    def display(self):
        print("\nBucket    Key")
        print("===============")

        for i in range(M):
            print("HT[%2d] :   %2d" %(i, self.table[i]))

if __name__ == "__main__":
    HT = HashTable()

    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print("h(%2d) = %2d " %(d, HT.hashFn(d)), end="")
        HT.insert(d)
        print(HT.table)

    HT.display()

    print("Search(46) ---> ", HT.search(46))
    HT.delete(9); HT.display()