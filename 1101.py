while True:
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])

    nums = []

    if m > 1 and n > 1:
        if m < n:
            for n in range(m, n+1):
                nums.append(n)
                res = " ".join(map(str, nums))
                soma = sum(nums)
            print(res, "Sum=%d" % soma)
            nums = []

        elif m > n:
            for n in range(n, m+1):
                nums.append(n)
                res = " ".join(map(str, nums))
                soma = sum(nums)
            print(res, "Sum=%d" % soma)
            nums = []
    else:
        break
