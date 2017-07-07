import base64
import hashlib

def rich_dict_to_id(d, length=32):
    s = ""
    for k in sorted(d.keys()):  # TODO this should be recursive
        s += ",{0}-{1}".format(str(k), str(d[k]))
    return base64.b64encode(hashlib.sha256(s).digest())[0:length]



class DataType:
    def __init__(self, type_params):
        self.type_params = type_params
        self.type_id = rich_dict_to_id(type_params)
        self.q = 5

class Data:
    def __init__(self, data_type, metadata, instance_params):
        self.data_type = data_type
        self.type_id = rich_dict_to_id(instance_params)
        self.metadata = metadata
        self.instance_param = instance_params

class JobDef:
    def __init__(self, inputs, outputs):
        self.outputs = outputs
        self.input = inputs
        self.id = 0

class Job:
    def __init__(self, jobdef, metadata, instance_params=None):
        self.jobdef = jobdef
        self.instance_id = rich_dict_to_id(instance_params) if instance_params else None
        self.metadata_id = rich_dict_to_id(metadata)

class Output:
    def __init__(self, job_def, output_type_id, make_parent):
        self.job_def = job_def
        self.output_datatype = output_type_id
        self.instantiate_maker_job = make_parent

    def compute_job(self, data_instance_parameters):
        return self.instantiate_maker_job(data_instance_parameters)

class Input:
    def __init__(self):
        self.q = 6
