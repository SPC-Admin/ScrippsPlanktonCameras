import json

def field_reducer(data,field,wrapper=None):

    output = []

    for d in data:
        dict = json.loads(d.decode())
        if wrapper is not None:
            output.extend([x[field] for x in dict[wrapper]])
        else:
            output.extend([x[field] for x in dict])

    # remove duplicates
    return sorted(list(set(output)))

def sum_append_extend_reducer(data,sum_fields,extend_fields,append_fields,wrapper=None):

    # initialize the sum and concat fields
    output = {}

    for sf in sum_fields:
        output[sf] = 0.0

    for ef in extend_fields:
        output[ef] = []

    for af in append_fields:
        output[af] = []


    for d in data:

        try:
            dict = json.loads(d.decode())

            for sf in sum_fields:
                # test for wrapper needed
                if wrapper is None:
                    output[sf] = output[sf] + dict[sf]
                else:
                    output[sf] = output[sf] + dict[wrapper][sf]

            for ef in extend_fields:
                # test for wrapper needed
                if wrapper is None:
                    output[ef].extend(dict[ef])
                else:
                    output[ef].extend(dict[wrapper][ef])

            for af in append_fields:
                # test for wrapper needed
                if wrapper is None:
                    output[af].append(dict[af])
                else:
                    output[af].append(dict[wrapper][af])

        except:
            pass

    if wrapper is None:
        return output
    else:
        tmp = {}
        tmp[wrapper] = output
        return tmp

def image_list_reducer(server_data):

    return server_data

def label_reducer(server_data):

    return field_reducer(server_data,'name','labels')


def annotator_reducer(server_data):

    return field_reducer(server_data,'name','annotators')
