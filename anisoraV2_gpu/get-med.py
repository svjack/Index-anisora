datas=[
    [3, 12, 38, 55, 68, 72, 76, 79, 82, 84, 87, 89, 91, 92, 94, 96],
    [2, 5, 9, 16, 29, 42, 58, 68, 75, 79, 83, 88, 92, 94, 95, 96],
    [1, 3, 7, 13, 24, 36, 44, 54, 63, 71, 78, 85, 89, 93, 95, 96],
    [3, 10, 39, 60, 73, 77, 81, 84, 86, 88, 90, 92, 93, 94, 95, 96],
    [2, 5, 11, 21, 36, 51, 65, 73, 80, 85, 88, 91, 93, 94, 95, 96],
    [1, 3, 6, 11, 20, 36, 49, 65, 71, 77, 83, 87, 91, 94, 95, 96],
    [2, 6, 15, 26, 39, 49, 57, 64, 70, 74, 80, 86, 90, 93, 95, 96],
    [1, 4, 9, 17, 30, 49, 63, 71, 81, 86, 89, 91, 93, 94, 95, 96],
    [4, 13, 29, 45, 58, 67, 73, 76, 80, 84, 88, 90, 92, 94, 95, 96],
]
def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    middle_index = n // 2
    return sorted_arr[middle_index]

opt=[]
leng=len(datas[0])
len_datas=len(datas)
for i in range(leng):
    tmp=[datas[j][i]for j in range(len_datas)]
    opt.append(calculate_median(tmp))
print(opt)
#544P#96-12#[5, 20, 54, 63, 71, 79, 82, 87, 91, 94, 95, 96]