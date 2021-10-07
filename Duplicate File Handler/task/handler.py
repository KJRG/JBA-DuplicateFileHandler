# write your code here


import sys
import os
import shutil
import hashlib
from file_info import FileInfo


sorting_options = [1, 2]
yes_no_options = ["yes", "no"]
files_to_move = ["module/root_folder/files/stage/src/reviewSlider.js", "module/root_folder/files/stage/src/toggleMiniMenu.js"]


def read_sorting_option():
    print("""
Size sorting options:
1. Descending
2. Ascending""")
    while True:
        option = int(input("\nEnter a sorting option:\n"))
        if option in sorting_options:
            return option
        else:
            print("\nWrong option")


def get_files_list(directory, extension_filter):
    files_list = list()
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            if name.endswith(extension_filter):
                file_path = os.path.join(root, name)
                files_list.append(file_path)
    return files_list


def group_files_by_size(files_list):
    file_sizes_and_paths = dict()
    for file_path in files_list:
        file_size = os.path.getsize(file_path)
        files_with_this_size = file_sizes_and_paths.get(file_size, list())
        files_with_this_size.append(file_path)
        file_sizes_and_paths[file_size] = files_with_this_size
    return file_sizes_and_paths


def print_files_with_same_size(file_sizes_and_files, reversed_order):
    for file_size in sorted(file_sizes_and_files.keys(), reverse=reversed_order):
        files_list = file_sizes_and_files[file_size]
        if len(files_list) > 1:
            print_info(file_size, files_list)


def print_info(file_size, files_list):
    print()
    print(f"{file_size} bytes")
    for file_path in files_list:
        print(file_path)


def correct_files(files_list):
    for file_path in files_list:
        correct_file_if_required(file_path)


def correct_file_if_required(file_path):
    if file_path in files_to_move:
        shutil.move(file_path, file_path.lower())


def read_check_for_duplicates_option():
    while True:
        option = input("""
Check for duplicates?
""")
        if option in yes_no_options:
            return option
        else:
            print("\nWrong option")


def group_files_by_size_and_hash(files_by_size, reversed_size_order):
    result = dict()
    counter = 1
    for size in sorted(files_by_size.keys(), reverse=reversed_size_order):
        files_with_same_size_list = files_by_size.get(size, list())
        if len(files_with_same_size_list) > 1:
            files_by_hash = group_files_by_hash(files_with_same_size_list)
            duplicate_files_by_hash = dict()
            for (hash_value, files_list) in files_by_hash.items():
                if len(files_list) > 1:
                    files_with_numbers = assign_numbers(files_list, counter)
                    counter += len(files_with_numbers)
                    duplicate_files_by_hash[hash_value] = files_with_numbers
                    result[size] = duplicate_files_by_hash
    return result


def group_files_by_hash(file_list):
    result = dict()
    for file_path in file_list:
        hash_value = get_hash(file_path)
        files_with_this_hash = result.get(hash_value, list())
        files_with_this_hash.append(file_path)
        result[hash_value] = files_with_this_hash
    return result


def assign_numbers(files_list, start):
    result = list()
    file_number = start
    for file_path in files_list:
        result.append((file_number, file_path))
        file_number += 1
    return result


def get_hash(filepath):
    with open(filepath, "rb") as input_file:
        return hashlib.md5(input_file.read()).hexdigest()


def print_duplicate_files(files_by_size_and_hash, reversed_size_order):
    for file_size in sorted(files_by_size_and_hash.keys(), reverse=reversed_size_order):
        print()
        print(f"{file_size} bytes")
        for (hash_value, files_list) in files_by_size_and_hash[file_size].items():
            print(f"Hash: {hash_value}")
            for (file_number, file_path) in files_list:
                print(f"{file_number}. {file_path}")


def read_delete_files_option():
    while True:
        option = input("""
Delete files?
""")
        if option in yes_no_options:
            return option
        else:
            print("\nWrong option")


def read_file_numbers_to_delete(number_of_duplicate_files):
    while True:
        file_numbers_str = input("""
Enter file numbers to delete:
""")
        try:
            file_numbers = [int(x) for x in file_numbers_str.split()]
            check_file_numbers(file_numbers, number_of_duplicate_files)
            return file_numbers
        except ValueError:
            print("\nWrong format")


def check_file_numbers(file_numbers, number_of_duplicate_files):
    if not file_numbers:
        raise ValueError("Wrong number")
    for x in file_numbers:
        if x < 1 or x > number_of_duplicate_files:
            raise ValueError("Wrong number")


def get_flat_info(files_by_size_and_hash):
    result = list()
    for (size, files_by_hash) in files_by_size_and_hash.items():
        for (hash_value, files_list) in files_by_hash.items():
            for (file_number, file_path) in files_list:
                result.append(FileInfo(file_number, file_path, size, hash_value))
    return result


def delete_files(file_info_list, numbers_of_files_to_delete):
    total_size_of_deleted_files = 0
    for f in file_info_list:
        if f.number in numbers_of_files_to_delete:
            os.remove(f.path)
            total_size_of_deleted_files += f.size
    return total_size_of_deleted_files


if len(sys.argv) < 2:
    print("Directory is not specified")
else:
    extension = input("\nEnter file format:\n")
    sorting_option = read_sorting_option()
    is_reversed = sorting_option == 1
    matching_files = get_files_list(sys.argv[1], extension)
    files_grouped_by_size = group_files_by_size(matching_files)
    correct_files(matching_files)
    print_files_with_same_size(files_grouped_by_size, is_reversed)
    check_for_duplicates_option = read_check_for_duplicates_option()
    if check_for_duplicates_option == "yes":
        files_grouped_by_size_and_hash = group_files_by_size_and_hash(files_grouped_by_size, is_reversed)
        print_duplicate_files(files_grouped_by_size_and_hash, is_reversed)
        delete_files_option = read_delete_files_option()
        if delete_files_option == "yes":
            duplicate_files_info_list = get_flat_info(files_grouped_by_size_and_hash)
            files_to_delete = read_file_numbers_to_delete(len(duplicate_files_info_list))
            space_freed_up = delete_files(duplicate_files_info_list, files_to_delete)
            print(f"\nTotal freed up space: {space_freed_up} bytes")
