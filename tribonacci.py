def tribonacci_sequence(start_sequence, length):
    if length == 0: #if length is zero then returning empty array
        return []
    if length <= 3: #for anything less than 3 just returning the starting values
        return start_sequence[:length]
    seq = start_sequence[:3]
    for i in range(3,length):
        next_seq_no = seq[i-1]+seq[i-2]+seq[i-3] #adding the previous 3 entries
        seq.append(next_seq_no) #adding the new element

    return seq
#testing our code for various scenarios
print(tribonacci_sequence([0, 0, 1],0))
print(tribonacci_sequence([0, 0, 1],1))
print(tribonacci_sequence([0, 0, 1],2))
print(tribonacci_sequence([0, 0, 1],3))
print(tribonacci_sequence([0, 0, 1],8))
print(tribonacci_sequence([0, 0, 1],15))