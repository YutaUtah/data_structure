#
#
def MergeSort(num_list):
    n = len(num_list)

    if len(num_list) == 1:
        return num_list

    # 1. 整列されていないリストを２つのサブリストに分割する
    mid = int(round(n / 2))

    left = num_list[:mid]
    right = num_list[mid:]

    print(left, right)

    # 2. 分割したリスト（サブリスト）を整列する。サブリストもマージソートを使って整列させる。（再帰関数）
    l = MergeSort(left)
    r = MergeSort(right)

    # 3. 2つのサブリストをマージして１つの整列済みリストにする
    return Merge(l, r)


# 整列済みリストA、Bを使って、整列済みリストCを作成する
def Merge(A, B):
    C = []
    #   print("A",A)
    #   print("B",B)

    # 1. AとBの先頭の数字を比較し、小さい方をCに追加し追加した値はリストから削除する
    # 2. 手順1をどちらか一方のリストが空になるまで繰り返す。
    while (len(A) > 0) and (len(B) > 0):
        if A[0] < B[0]:
            C.append(A[0])
            del A[0]
        else:
            C.append(B[0])
            del B[0]

    # 3. 残った要素をCの末尾に追加する
    if len(A) > 0:
        C.extend(A)
    else:
        C.extend(B)

    #   print("C",C)
    return C