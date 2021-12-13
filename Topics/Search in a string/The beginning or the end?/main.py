string_exp = input()
sub_index_f = string_exp.index('old')
sub_index_r = string_exp.rindex('old')
print(f"{sub_index_r if sub_index_r > sub_index_f else sub_index_r}")