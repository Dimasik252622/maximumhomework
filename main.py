
# def strcounter(s):
#     for sym in s:
#         counter = 0
#         for sub_sin in s:
#             if sym == sub_sin:
#                 counter += 1
#         print(sym, counter)  -- N ** 2


# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sin in s:
#             if sym == sub_sin:
#                 counter += 1
#         print(sym, counter)
# M * N или N * N если все символы разные

# def strcounter(s):
#     syms_county = {}
#     for sym in s:
#         syms_county[sym] = syms_county.get(sym, 0) + 1
#
#     print(syms_county)
#
# s = 'aaabc'
# strcounter(s) # O(N) = N

