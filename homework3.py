import os

def sorts_files_by_text_length(file_list: list, locations):
    list_all_files = []
    dict_help = {}
    for _i, _j in enumerate(file_list):
        full_path = os.path.join(os.getcwd(), locations, _j)
        with open(full_path, 'r', encoding='utf-8') as files:
            list_all_files.append(files.readlines())
            dict_help.setdefault(len(list_all_files[_i]), _j)
    list_all_files.sort()
    list_all_files.reverse()

    with open('sort_files.txt', 'w', encoding='utf-8') as files:
        for _i in list_all_files:
            files.write(dict_help[len(_i)])
            files.write('\n')
            files.write(str(len(_i)))
            files.write('\n')
            files.writelines(_i)
            files.write('\n')
        # print(files)


sorts_files_by_text_length(['1.txt', '2.txt', '3.txt'], 'a_group_of_files_to_merge')





