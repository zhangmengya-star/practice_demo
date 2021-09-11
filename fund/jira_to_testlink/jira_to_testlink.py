import os
import json


def get_case_list(file_name):
    file_path = os.path.dirname(__file__) + file_name

    with open(file_path, 'r') as f:
        content = f.read()
        content_dict = json.loads(content)
        case_list = content_dict['stepBeanCollection']

        # for case in case_list:
        #     test_step = case['step']
        #     test_data = case['data']
        #     test_result = case['result']
        #     change_from_markdown_to_ordered(test_result)
        # todo
        case = case_list[4]
        # test_step = case['step']
        # test_data = case['data']
        test_result = case['result']
        change_from_markdown_to_ordered(test_result)


def change_from_markdown_to_ordered(content):
    separator = '#'
    steps = content.split('\n')
    separator_num_list = []
    for step in steps:
        separator_num = step.count(separator)
        separator_num_list.append(separator_num)

    first_count = 0
    second_count = 0
    third_count = 0
    fourth_count = 0
    fifth_count = 0
    for i in range(len(separator_num_list)):
        if separator_num_list[i] == 1:
            first_count += 1
            second_count = 0
            third_count = 0
            fourth_count = 0
            fifth_count = 0
            test = str(first_count)
            print(test)
        if separator_num_list[i] == 2:
            second_count += 1
            third_count = 0
            fourth_count = 0
            fifth_count = 0
            test = str(first_count) + '.' + str(second_count)
            print(test)
        if separator_num_list[i] == 3:
            third_count += 1
            fourth_count = 0
            fifth_count = 0
            test = str(first_count) + '.' + str(second_count) + '.' + str(third_count)
            print(test)
        if separator_num_list[i] == 4:
            fourth_count += 1
            fifth_count = 0
            test = str(first_count) + '.' + str(second_count)
            + '.' + str(third_count) + '.' + str(fourth_count)
            print(test)
        if separator_num_list[i] == 5:
            fifth_count += 1
            test = str(first_count) + '.' + str(second_count)
            + '.' + str(third_count) + '.' + str(fourth_count)
            + '.' + str(fifth_count)
            print(test)


if __name__ == '__main__':
    get_case_list('/YBCQA-878.txt')
