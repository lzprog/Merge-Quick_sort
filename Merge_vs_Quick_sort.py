import time

def merge_sort(vet, begin, finish):
    if begin < finish: 
        mid = (finish + begin) // 2
        merge_sort(vet, begin, mid)
        merge_sort(vet, mid+1, finish)
        merge(vet, begin, mid, finish)

def merge(vet, begin, mid, finish):

    n1 = begin 
    n2 = mid + 1
    aux = [] 

    while n1 <= mid and n2 <= finish:
        if vet[n1] < vet[n2]:
            aux.append(vet[n1])
            n1 = n1 + 1
        else:
            aux.append(vet[n2])
            n2 = n2 + 1
    
    while n1 <= mid:
        aux.append(vet[n1])
        n1 = n1 + 1
    while n2<= finish:
        aux.append(vet[n2])
        n2 = n2 + 1
    for i in range(begin, finish + 1):
        vet[i] = aux[i - begin]

def quick_sort(vet, begin, finish):
    if begin < finish:
        p = part(vet, begin, finish)
        quick_sort(vet, begin, p-1)
        quick_sort(vet, p+1, finish)

def part(vet, begin, finish):
    pivot = vet[finish]
    i = begin - 1
    for j in range(begin, finish):
        if vet[j] <= pivot:
            i = i + 1
            temp = vet[i]
            vet[i] = vet[j]
            vet[j] = temp
    temp = vet[i+1]
    vet[i+1] = vet[finish]
    vet[finish] = temp
    return i+1

#leitura e teste dos arquivos
#quick_sort da erro para vetores muito grandes em py
#tempo máx. de merge_sort ~~ 78s

print("FILE: 100.TXT \n")
arq = open("100.txt", "r+")
content = []
for line in arq:
    numbers = line.strip().split(",")
    content.extend(int(num) for num in numbers)
start_timer1 = time.time()
merge_sort(content, 0, len(content) - 1)
end_timer1 = time.time()
start_timer2 = time.time()
quick_sort(content, 0, len(content) - 1)
end_timer2 = time.time()
arq.close()
print(f"tempo (merge) : {end_timer1 - start_timer1}\n tempo(quick) : {end_timer2 - start_timer2}\n")

print("FILE: 500.TXT \n")
arq = open("500.txt", "r+")
content = []
for line in arq:
    numbers = line.strip().split(",")
    content.extend(int(num) for num in numbers)
start_timer1 = time.time()
merge_sort(content, 0, len(content) - 1)
end_timer1 = time.time()
start_timer2 = time.time()
quick_sort(content, 0, len(content) - 1)
end_timer2 = time.time()
arq.close()
print(f"tempo (merge) : {end_timer1 - start_timer1}\n tempo(quick) : {end_timer2 - start_timer2}\n")

print("FILE: 1000.TXT \n")
arq = open("1000.txt", "r+")
content = []
for line in arq:
    numbers = line.strip().split(",")
    content.extend(int(num) for num in numbers)
start_timer1 = time.time()
merge_sort(content, 0, len(content) - 1)
end_timer1 = time.time()
start_timer2 = time.time()
#quick_sort(content, 0, len(content) - 1)
end_timer2 = time.time()
arq.close()
print(f"tempo (merge) : {end_timer1 - start_timer1}\n tempo(quick) : {end_timer2 - start_timer2}\n")




