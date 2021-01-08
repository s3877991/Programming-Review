abc_count = {}
start_letter = ord('a')                 # chu cai dau tien
end_letter = ord('z')                   # chu cai cuoi cung
for c_num in range(start_letter, end_letter+1):
    abc_count[chr(c_num)] = 0           # so chu cai ban dau = 0
s = input("Enter any English text: ")
for letter in s:
    if letter == ' ':                   # neu ki tu trong chuoi NULL thì bo qua và tiep thuc vs ki tu tiep theo
        continue
    abc_count[letter.lower()] += 1      # tra ve bang chu thuong khi co chu HOA
for k, v in abc_count.items():
    print(k, ':', v)                    # ghi list so chu cai trong chuoi
