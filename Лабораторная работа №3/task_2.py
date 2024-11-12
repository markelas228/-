def find_common_participants(participants_first_group, participants_second_group, separator=','):
    first_group_list = participants_first_group.split(separator)
    second_group_list = participants_second_group.split(separator)
    common_participants = set(first_group_list).intersection(set(second_group_list))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)
