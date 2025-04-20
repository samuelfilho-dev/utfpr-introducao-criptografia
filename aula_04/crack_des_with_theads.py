import itertools
import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import threading
from queue import Queue
from tqdm import tqdm

NUM_THREADS = 8
CHUCK_SIZE = 10000 # Number of keys to try per thread

class Result:
    def __init__(self):
        self.key = None
        self.text = None
        self.lock = threading.Lock()

class TriesCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            self.value += 1
            return self.value


def load_wordlist(path):
    with open(path, 'r', errors='ignore') as f:
        for line in f:
            word = line.strip()
            yield word.ljust(8, '\0')[:8].encode()
            yield word.upper().ljust(8, '\0')[:8].encode()
            yield word.lower().ljust(8, '\0')[:8].encode()
            yield word.capitalize().ljust(8, '\0')[:8].encode()


def generate_key(queue):
    for choice in itertools.product(range(256), repeat=8):
        key = adjust_key_equality(bytes(choice))
        queue.put(key)

    for _ in range(NUM_THREADS):
        queue.put(None)



def adjust_key_equality(key):
    adjust_key = bytearray(key)
    for i in range(len(adjust_key)):
        byte = adjust_key[i]
        equality = bin(byte).count('1') % 2
        if equality == 0:
            adjust_key[i] ^= 1
    return bytes(adjust_key)



def worker(queue, cypher_text, iv, result, tries):
    """Função executada por cada thread"""
    while True:
        key_try = queue.get()
        if key_try is None:
            break
        try:
            print(f'Tentando chave: {key_try}', end='\r')
            cipher = DES.new(key_try, DES.MODE_ECB, iv=0) # Pode colocar IV (Initialization Vector) aqui
            plain_text = unpad(cipher.decrypt(cypher_text), DES.block_size)
            
            if all(32 <= byte <= 126 for byte in plain_text):
                with result.lock:
                    result.key = key_try
                    result.text = plain_text.decode('ascii', errors='ignore')
                break
        except:
            pass
            
        tries.increment()

def parallel_brute_force(cypher_text, iv, max_tries):
    queue = Queue(CHUCK_SIZE * 2)
    result = Result()
    counter = TriesCounter()
    threads  = []

    # Start
    for _ in range(NUM_THREADS):
        t = threading.Thread(
            target=worker,
            args=(queue, cypher_text, iv, result, counter)
        )
        t.start()
        threads.append(t)
        
        start_time = time.time()
        total_tries = 0

        with tqdm(desc="\nProcessando Word List") as pbar:
            for key in load_wordlist('./aula_04/wikipedia_pt_vowels_no_compounds_top-1000000.txt'):
                if result.key is not None:
                    break

                if max_tries and counter.value >= max_tries:
                    break

                queue.put(key)
                total_tries += 1
                pbar.update(1)
        
        for _ in range(NUM_THREADS):
            queue.put(None)
        
        for t in threads:
            t.join()
        
        total_time = time.time() - start_time

        if result:
             print(f"\nChave encontrada após {counter.value} tentativas!")
             print(f"Tempo total: {total_time:.2f} segundos")
             print(f"Velocidade: {counter.value / max(1, total_time):,.0f} chaves/s")
             print(f"Chave: {result.key}")
             print(f"Texto decifrado: {result.text}")
             return result.text
        else:
            print(f"\nChave não encontrada após {max_tries} tentativas.")
            return None


if __name__ == '__main__':
    with open('aula_04/output.txt', 'rb') as f:
        cypher_text = f.read()

    print("\nIniciando ataque de força bruta paralela contra DES...")
    print(f"Total de combinações possíveis: {2**56:,} (72 quatrilhões)")
    print(f"Usando {NUM_THREADS} threads paralelas")

    key = parallel_brute_force(cypher_text, None, max_tries=2**56)

    """
    Tentei fazer a questão 03 mas não consegui quebrar a chave
    DES, mesmo com 8 threads.
    """