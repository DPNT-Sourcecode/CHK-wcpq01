

# noinspection PyUnusedLocal
# skus = unicode string

PRICES = {
    "A":50,
    "B":30,
    "C":20,
    "D":15,
}

def skus_is_valid(skus):
    for x in skus:
        if str(x).upper() not in "ABCD":
            return False
    return True

def checkout(skus):

    if skus_is_valid:
        result = sum(PRICES[str(x).upper()] for x in list(str(skus)))
        return result
    return -1


# Testing
if __name__ == '__main__':
    print "AfBD = {}, expected: -1".format(checkout("AfBD"))
    print "AB = {}, expected: 80".format(checkout("AB"))


# id = CHK_R1_003, req = checkout(""), resp = -1,
# A
# id = CHK_R1_004, req = checkout("A"), resp = -1,
# B
# id = CHK_R1_005, req = checkout("B"), resp = -1,
# C
# id = CHK_R1_006, req = checkout("C"), resp = -1,
# D
# id = CHK_R1_007, req = checkout("D"), resp = -1,
# a
# id = CHK_R1_008, req = checkout("a"), resp = -1,
# -
# id = CHK_R1_009, req = checkout("-"), resp = -1,
# ABCa
# id = CHK_R1_010, req = checkout("ABCa"), resp = -1,
# AxA
# id = CHK_R1_011, req = checkout("AxA"), resp = -1,
# ABCD
# id = CHK_R1_012, req = checkout("ABCD"), resp = -1,
# A
# id = CHK_R1_013, req = checkout("A"), resp = -1,
# AA
# id = CHK_R1_014, req = checkout("AA"), resp = -1,
# AAA
# id = CHK_R1_015, req = checkout("AAA"), resp = -1,
# AAAA
# id = CHK_R1_016, req = checkout("AAAA"), resp = -1,
# AAAAA
# id = CHK_R1_017, req = checkout("AAAAA"), resp = -1,
# AAAAAA
# id = CHK_R1_018, req = checkout("AAAAAA"), resp = -1,
# B
# id = CHK_R1_019, req = checkout("B"), resp = -1,
# BB
# id = CHK_R1_020, req = checkout("BB"), resp = -1,
# BBB
# id = CHK_R1_021, req = checkout("BBB"), resp = -1,
# BBBB
# id = CHK_R1_022, req = checkout("BBBB"), resp = -1,
# ABCDABCD
# id = CHK_R1_023, req = checkout("ABCDABCD"), resp = -1,
# BABDDCAC
# id = CHK_R1_024, req = checkout("BABDDCAC"), resp = -1,
# AAABB
# id = CHK_R1_025, req = checkout("AAABB"), resp = -1,
# ABCDCBAABCABBAAA
# id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA"), resp = -1,
# Stopping client
# Notify round "CHK_R1", event "deploy"
#
#  - {"method":"checkout","params":[""],"id":"CHK_R1_003"}, expected: 0, got: -1
#  - {"method":"checkout","params":["A"],"id":"CHK_R1_004"}, expected: 50, got: -1
#  - {"method":"checkout","params":["B"],"id":"CHK_R1_005"}, expected: 30, got: -1
