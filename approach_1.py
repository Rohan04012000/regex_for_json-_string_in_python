dictionary_order = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},
                                {"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},
                                {"id":650},{"id":651},{"id":652},{"id":653}
                            ],

                    "errors":[{"code":3,
                                "message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}
                            ]
                    }

def finding_numbers_with_id_and_error_as_key(dictionary_order):

    #Main logic code to extract number from orders and errors:
    list_of_numbers_1 = [values['id'] for values in dictionary_order['orders']]
    list_of_numbers_2 = [values['code'] for values in dictionary_order['errors']]

    #return the combined form of obtained list.
    return list_of_numbers_1 + list_of_numbers_2
    #End of Main logic.


print(finding_numbers_with_id_and_error_as_key(dictionary_order))
print(type(finding_numbers_with_id_and_error_as_key(dictionary_order))) #Returned list is a LIST.
