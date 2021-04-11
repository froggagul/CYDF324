import json

class Model():
    def __init__(self):
        pass
    def search(self, search_term):
        with open('data.json', 'r', encoding='utf-8') as f:
            phone_data = json.load(f)
            # print(phone_data)

        def does_include_term(target):
            if search_term not in target:
                return False
            return True

        result_dict = {}
        for name in phone_data:
            if does_include_term(name):
                result_dict[name] = phone_data[name]
            else:
                value_search_result = list(filter(does_include_term, phone_data[name]))
                if (len(value_search_result) > 0):
                    result_dict[name] = value_search_result
        
        result_list = []
        for name in result_dict:
            for phone_number in result_dict[name]:
                result_list.append(f'{name} : {phone_number}')
        # names = list(phone_data.keys())
        # result_names = filter(does_include_term, names)

        # print(list(result_names))
        # # def search_by_value(term):

        return sorted(result_list)
    
    def addPhoneInfo(self, name, phone_number):
        with open('data.json', 'r', encoding='utf-8') as f:
            phone_data = json.load(f)

        print(name, phone_number)
        if name in phone_data:
            if phone_number not in phone_data[name]:
                phone_data[name].append(phone_number)
        else:
            phone_data[name] = [phone_number]

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(phone_data, f)
